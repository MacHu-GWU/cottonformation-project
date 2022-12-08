# -*- coding: utf-8 -*-

"""
AWS Environment and Deployment component.
"""

import typing as T
import sys
import hashlib

from aws_cloudformation import deploy_stack, remove_stack
from aws_cloudformation.stack import Parameter

from .template import Template
from .console import get_s3_console_url
from ..res.cloudformation import Stack

if T.TYPE_CHECKING:
    from boto_session_manager import BotoSesManager

DEFAULT_S3_PREFIX_FOR_TEMPLATE = "cloudformation/template"
DEFAULT_S3_PREFIX_FOR_STACK_POLICY = "cloudformation/policy"

DEFAULT_UPDATE_DELAYS = 5
DEFAULT_UPDATE_TIMEOUT = 60
DEFAULT_CHANGE_SET_DELAYS = 5
DEFAULT_CHANGE_SET_TIMEOUT = 60


def md5_of_text(text: str) -> str:
    """
    Return md5 of text.
    """
    md5 = hashlib.md5()
    md5.update(text.encode("utf-8"))
    return md5.hexdigest()


def detect_template_type(template: str) -> str:
    """
    Detect whether CloudFormation template is JSON or YAML.

    :return: "json" or "yaml"
    """
    if template.strip().startswith("{"):
        return "json"
    else:  # pragma: no cover
        return "yaml"


class Env:
    """
    Environment is simply an abstraction layer with a boto3 session object
    connected to AWS, allowing you to perform AWS API call.

    You are responsible to create you own boto session manager object.
    You can find more information about ``BotoSesManager`` at
    https://github.com/MacHu-GWU/boto_session_manager-project

    1. Local laptop environment, using default AWS credential based on the
        environment variable https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html,
        or based on the default profile in ``~/.aws/credentials``:

    .. code-block:: python

        import boto3

        bsm = BotoSesManager()

    2. Local laptop environment, using named profile. You have to configure the
        ``~/.aws/credentials`` and ``~/.aws/config`` file. Here's how
        https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html:

    .. code-block:: python

        bsm = BotoSesManager(profile_name="your_aws_profile")

    3. EC2 or AWS Lambda environment, using IAM role. It is exactly same to #1

    4. Load credential in a secure way, manually pass in credential to the session:

    .. code-block:: python

        bsm = BotoSesManager(
            aws_access_key_id="your_access_key",
            aws_secret_access_key="your_secret_access_key",
            region_name="us-east-1",
        )

    .. versionadded:: 1.0.1
    """

    def __init__(
        self,
        bsm: "BotoSesManager" = None,
        is_us_gov_cloud: bool = False,
    ):
        if bsm is None:
            self.bsm = BotoSesManager()
        else:
            self.bsm = bsm
        self.is_us_gov_cloud = is_us_gov_cloud

    @property
    def s3_client(self):
        return self.bsm.get_client("s3")

    @property
    def cf_client(self):
        return self.bsm.get_client("cloudformation")

    def upload_template(
        self,
        template: Template,
        bucket: str,
        prefix: str = DEFAULT_S3_PREFIX_FOR_TEMPLATE,
    ) -> T.Tuple[str, str]:
        """
        Upload cloudformation template to s3 bucket and returns template url.
        It is a format like this https://s3.amazonaws.com/<s3-bucket-name>/<s3-key>

        :return: s3 url of the template file

        .. versionadded:: 1.0.1
        """
        template_body = template.to_json()
        filename = md5_of_text(template_body)
        template_type = detect_template_type(template_body)
        if prefix.endswith("/"):
            prefix = prefix[:-1]
        key = f"{prefix}/{filename}.{template_type}"
        self.s3_client.put_object(
            Bucket=bucket,
            Key=key,
            Body=template_body,
        )
        template_url = "https://s3.amazonaws.com/{}/{}".format(bucket, key)
        s3_console_url = get_s3_console_url(
            bucket=bucket,
            prefix=key,
            is_us_gov_cloud=self.is_us_gov_cloud,
        )
        return template_url, s3_console_url

    def package(
        self,
        template: Template,
        bucket: str,
        prefix: str = DEFAULT_S3_PREFIX_FOR_TEMPLATE,
        verbose: bool = True,
        _is_master: bool = True,
    ):
        """
        Automatically upload nested stack template and update template url
        in your CloudFormation code.

        It's a depth-first-search.
        """
        stack_resource: Stack
        for stack_resource in template.Resources.values():
            if stack_resource.AWS_OBJECT_TYPE != Stack.AWS_OBJECT_TYPE:
                continue

            nested_template = template.NestedStack[stack_resource.id]
            self.package(
                template=nested_template,
                bucket=bucket,
                prefix=prefix,
                verbose=verbose,
                _is_master=False,
            )

            if bucket is None:
                raise ValueError(
                    "Because you have a nested template, "
                    "you have to upload template to S3 bucket! "
                    "However ``bucket_name`` is None"
                )
            nested_template_url, nested_template_s3_console_url = self.upload_template(
                template=nested_template,
                bucket=bucket,
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

    def deploy(
        self,
        stack_name: str,
        template: Template,
        use_previous_template: T.Optional[bool] = None,
        bucket: T.Optional[str] = None,
        prefix: T.Optional[str] = DEFAULT_S3_PREFIX_FOR_TEMPLATE,
        parameters: T.List[Parameter] = None,
        tags: dict = None,
        execution_role_arn: T.Optional[str] = None,
        include_iam: bool = False,
        include_named_iam: bool = False,
        include_macro: bool = False,
        stack_policy: T.Optional[str] = None,
        prefix_stack_policy: T.Optional[str] = DEFAULT_S3_PREFIX_FOR_STACK_POLICY,
        resource_types: T.Optional[T.List[str]] = None,
        client_request_token: T.Optional[str] = None,
        enable_termination_protection: T.Optional[bool] = None,
        disable_rollback: T.Optional[bool] = None,
        wait: bool = True,
        delays: T.Union[int, float] = DEFAULT_UPDATE_DELAYS,
        timeout: T.Union[int, float] = DEFAULT_UPDATE_TIMEOUT,
        plan_nested_stack: bool = True,
        skip_plan: bool = False,
        skip_prompt: bool = False,
        change_set_delays: T.Union[int, float] = DEFAULT_CHANGE_SET_DELAYS,
        change_set_timeout: T.Union[int, float] = DEFAULT_CHANGE_SET_TIMEOUT,
        verbose: bool = True,
    ):
        """
        Deploy (create or update) an AWS CloudFormation stack. But way more powerful
        than the original boto3 API.

        Reference:

        - Create Stack Boto3 API: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.create_stack
        - Update Stack Boto3 API: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.update_stack

        :param stack_name: the stack name or unique stack id
        :param template: :class:`~cottonformation.core.template.Template` object
        :param use_previous_template: see "Update Stack Boto3 API" link
        :param bucket: default None; if given, automatically upload template to S3
            before deployment. see :func:`~aws_cloudformation.better_boto.upload_template_to_s3`
            for more details.
        :param prefix: the s3 prefix where you want to upload the template to
        :param parameters: see "Update Stack Boto3 API" link
        :param tags: see "Update Stack Boto3 API" link
        :param execution_role_arn: see "Update Stack Boto3 API" link
        :param include_iam: see "Capacities" part in "Update Stack Boto3 API" link
        :param include_named_iam: see "Capacities" part in "Update Stack Boto3 API" link
        :param include_macro: see "Capacities" part in "Update Stack Boto3 API" link
        :param stack_policy: Stack Policy JSON or Yaml body in text, or the
            s3 uri pointing to a Stack Policy JSON template file.
        :param prefix_stack_policy: see "Update Stack Boto3 API" link
        :param resource_types: see "Update Stack Boto3 API" link
        :param client_request_token: see "Update Stack Boto3 API" link
        :param enable_termination_protection: see "Create Stack Boto3 API" link
        :param disable_rollback: see "Update Stack Boto3 API" link
        :param wait: default True; if True, then wait the create / update action
            to success or fail; if False, then it is an async call and return immediately;
            note that if you have skip_plan is False (using change set), you always
            have to wait the change set creation to finish.
        :param delays: how long it waits (in seconds) between two
            "describe_stacks" api call to get the stack status
        :param timeout: how long it will raise timeout error
        :param skip_plan: default False; if False, force to use change set to
            create / update; if True, then do create / update without change set.
        :param skip_prompt: default False; if False, you have to enter "Yes"
            in prompt to do deployment; if True, then execute the deployment directly.
        :param change_set_delays: how long it waits (in seconds) between two
            "describe_change_set" api call to get the change set status
        :param change_set_timeout: how long it will raise timeout error
        :param verbose: whether you want to log information to console

        :return: Nothing

        .. versionadded:: 1.0.1
        """
        stack_console_url = "https://console.aws.amazon.com/cloudformation/home?region={aws_region}#/stacks?filteringStatus=active&filteringText={stack_name}&viewNested=true&hideStacks=false&stackId=".format(
            aws_region=self.bsm.aws_region,
            stack_name=stack_name,
        )
        if verbose:
            print(f"open cloudformation console for status: {stack_console_url}")

        self.package(
            template=template,
            bucket=bucket,
            prefix=prefix,
            verbose=verbose,
        )

        deploy_stack(
            bsm=self.bsm,
            stack_name=stack_name,
            template=template.to_json(),
            use_previous_template=use_previous_template,
            bucket=bucket,
            prefix=prefix,
            parameters=parameters,
            tags=tags,
            execution_role_arn=execution_role_arn,
            include_iam=include_iam,
            include_named_iam=include_named_iam,
            include_macro=include_macro,
            stack_policy=stack_policy,
            prefix_stack_policy=prefix_stack_policy,
            resource_types=resource_types,
            client_request_token=client_request_token,
            enable_termination_protection=enable_termination_protection,
            disable_rollback=disable_rollback,
            wait=wait,
            delays=delays,
            timeout=timeout,
            plan_nested_stack=plan_nested_stack,
            skip_plan=skip_plan,
            skip_prompt=skip_prompt,
            change_set_delays=change_set_delays,
            change_set_timeout=change_set_timeout,
            verbose=verbose,
        )

    def delete(
        self,
        stack_name: str = None,
        retain_resources: T.Optional[T.List[str]] = None,
        role_arn: T.Optional[bool] = None,
        client_request_token: T.Optional[str] = None,
        wait: bool = True,
        delays: T.Union[int, float] = DEFAULT_UPDATE_DELAYS,
        timeout: T.Union[int, float] = DEFAULT_UPDATE_TIMEOUT,
        skip_prompt: bool = False,
        verbose: bool = True,
    ):
        """
        Delete an AWS CloudFormation Stack.

        Reference:

        - Delete Stack Boto3 API: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.delete_stack

        :param stack_name: the stack name or unique stack id
        :param retain_resources: see "Delete Stack Boto3 API" link
        :param role_arn: see "Delete Stack Boto3 API" link
        :param client_request_token: see "Delete Stack Boto3 API" link
        :param wait: default True; if True, then wait the delete action
            to success or fail; if False, then it is an async call and return immediately.
        :param delays: how long it waits (in seconds) between two
            "describe_stacks" api call to get the stack status
        :param timeout: how long it will raise timeout error
        :param skip_prompt: default False; if False, you have to enter "Yes"
            in prompt to do deletion; if True, then execute the deletion directly.
        :param verbose: whether you want to log information to console

        .. versionadded:: 1.0.1
        """
        remove_stack(
            bsm=self.bsm,
            stack_name=stack_name,
            retain_resources=retain_resources,
            role_arn=role_arn,
            client_request_token=client_request_token,
            wait=wait,
            delays=delays,
            timeout=timeout,
            skip_prompt=skip_prompt,
            verbose=verbose,
        )

    def validate(
        self,
        template: Template,
        bucket: str = None,
        prefix: str = DEFAULT_S3_PREFIX_FOR_TEMPLATE,
    ) -> dict:
        """
        Validate if a :class:`~cottonformation.core.template.Template` object
        is valid.

        TODO: not a stable API

        .. versionadded:: 0.0.8
        """
        template_body = template.to_json(human_readable=False)
        kwargs = dict()
        if sys.getsizeof(template_body) >= 51200:
            if bucket is None:
                raise ValueError(
                    "the body of Template is too large! you have to specify "
                    "``bucket_name`` argument to upload it to S3!"
                )
            template_url, _ = self.upload_template(
                template=template,
                bucket=bucket,
                prefix=prefix,
            )
            kwargs["TemplateURL"] = template_url
        else:
            kwargs["TemplateBody"] = template_body

        return self.cf_client.validate_template(**kwargs)
