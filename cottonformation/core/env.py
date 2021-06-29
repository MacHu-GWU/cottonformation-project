# -*- coding: utf-8 -*-

"""
AWS Environment and Deployment component.
"""

import hashlib
import typing

from .template import Template
from ..res.cloudformation import Stack


DEFAULT_CFT_S3_PREFIX = "cloudformation/upload"


def md5_of_text(text):
    md5 = hashlib.md5()
    md5.update(text.encode("utf-8"))
    return md5.hexdigest()


class Env:
    """
    Environment is simply a abstraction layer with a boto3 session object
    connected to AWS, allowing you to perform AWS API call.

    You are responsible to create you own boto3 session object.
    
    1. Local laptop environment, using default AWS credential based on the
        environment variable https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html,
        or based on the default profile in ``~/.aws/credentials``:
    
    .. code-block:: python
    
        import boto3

        boto_ses = boto3.session.Session()

    2. Local laptop environment, using named profile. You have to configure the
        ``~/.aws/credentials`` and ``~/.aws/config`` file. Here's how
        https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html:

    .. code-block:: python

        boto_ses = boto3.session.Session(profile_name="your_aws_profile")

    3. EC2 or AWS Lambda environment, using IAM role. It is exactly same to #1

    4. Load credential in a secue way, manually pass in credential to the session:

    .. code-block:: python

        boto_ses = boto3.session.Session(
            aws_access_key_id="your_access_key",
            aws_secret_access_key="your_secret_access_key",
            region_name="us-east-1",
        )

    :type boto_ses: boto3.session.Session
    """

    def __init__(self, boto_ses):
        self.boto_ses = boto_ses
        self.s3_client = self.boto_ses.client("s3")
        self.cf_client = self.boto_ses.client("cloudformation")

    def upload_template(self,
                        template: Template,
                        bucket_name: str,
                        prefix: str = DEFAULT_CFT_S3_PREFIX) -> typing.Tuple[str, str]:
        """
        Upload cloudformation template to s3 bucket and returns template url.
        It is a format like this https://s3.amazonaws.com/<s3-bucket-name>/<s3-key>

        :return: s3 url of the template file
        """
        tpl_content = template.to_json()
        fname = md5_of_text(tpl_content)
        ext = ".json"
        if prefix.endswith("/"):
            prefix = prefix[:-1]
        s3_key = f"{prefix}/{fname}{ext}"
        self.s3_client.put_object(
            Body=tpl_content,
            Bucket=bucket_name,
            Key=s3_key,
        )
        template_url = "https://s3.amazonaws.com/{}/{}".format(bucket_name, s3_key)
        s3_console_url = "https://s3.console.aws.amazon.com/s3/object/{}?prefix={}".format(
            bucket_name, s3_key
        )
        return template_url, s3_console_url

    def package(self,
                template: Template,
                bucket_name: str,
                prefix: str = DEFAULT_CFT_S3_PREFIX,
                verbose: bool = True,
                _is_master: bool = True):

        stack_resource: Stack
        for stack_resource in template.Resources.values():
            if stack_resource.AWS_OBJECT_TYPE != Stack.AWS_OBJECT_TYPE:
                continue

            nested_template = template.NestedStack[stack_resource.id]
            self.package(
                template=nested_template,
                bucket_name=bucket_name,
                prefix=prefix,
                verbose=verbose,
                _is_master=False
            )

            nested_template_url, nested_template_s3_console_url = self.upload_template(
                template=nested_template,
                bucket_name=bucket_name,
                prefix=prefix,
            )
            stack_resource.rp_TemplateURL = nested_template_url

            if verbose:
                msg = (
                    "upload the Template('{}') for nested Template('{}').Stack('{}') "
                    "to s3: {}. view it in aws console: {}"
                ).format(
                    nested_template.Description,
                    template.Description,
                    stack_resource.id,
                    nested_template_url,
                    nested_template_s3_console_url,
                )
                print(msg)


    def deploy(self,
               template: Template,
               stack_name: str,
               bucket_name: str,
               prefix: str = DEFAULT_CFT_S3_PREFIX,
               stack_tags: dict = None,
               stack_parameters: dict = None,
               execution_role_arn: str = None,
               include_iam: bool = False,
               verbose: bool = True) -> dict:
        stack_console_url = "https://console.aws.amazon.com/cloudformation/home?region={aws_region}#/stacks?filteringStatus=active&filteringText={stack_name}&viewNested=true&hideStacks=false&stackId=".format(
            aws_region=self.boto_ses.region_name,
            stack_name=stack_name,
        )
        if verbose:
            print(f"open cloudformation console for status: {stack_console_url}")

        self.package(
            template=template,
            bucket_name=bucket_name,
            prefix=prefix,
            verbose=verbose
        )

        template_url, s3_console_url = self.upload_template(template, bucket_name, prefix)
        if verbose:
            print(f"view raw cloudformation Template('{template.Description}') in console {s3_console_url}")
        # check if stack already exists
        try:
            res = self.cf_client.describe_stacks(
                StackName=stack_name
            )
            if len(res["Stacks"]) == 1:
                stack_exists_flag = True
            else:
                stack_exists_flag = False
        except:
            stack_exists_flag = False

        # pre-process arguments
        if stack_parameters is None:
            stack_parameters = dict()

        Parameters = [
            {
                "ParameterKey": key,
                "ParameterValue": value,
            }
            for key, value in stack_parameters.items()
        ]

        if stack_tags is None:
            stack_tags = dict()

        Tags = [
            {
                "Key": key,
                "Value": value
            }
            for key, value in stack_tags.items()
        ]

        Capabilities = list()
        if include_iam:
            Capabilities.append("CAPABILITY_NAMED_IAM")

        # execute create_stack or update_stack
        create_or_update_stack_kwargs = dict(
            StackName=stack_name,
            TemplateURL=template_url,
        )
        if len(Capabilities):
            create_or_update_stack_kwargs["Capabilities"] = Capabilities
        if len(Parameters):
            create_or_update_stack_kwargs["Parameters"] = Parameters
        if len(Tags):
            create_or_update_stack_kwargs["Tags"] = Tags
        if execution_role_arn:
            create_or_update_stack_kwargs["RoleARN"] = execution_role_arn

        response: dict = None
        if stack_exists_flag is True:  # run update_stack
            update_stack_kwargs = create_or_update_stack_kwargs
            update_stack_response = self.cf_client.update_stack(**update_stack_kwargs)
            response = update_stack_response
        else:  # run create_stack
            create_stack_kwargs = create_or_update_stack_kwargs
            create_stack_response = self.cf_client.create_stack(**create_stack_kwargs)
            response = create_stack_response

        return response
