# -*- coding: utf-8 -*-

"""
Cloudformation Template Generation.
"""

from troposphere_mate import Template, Parameter, iam, canned, helper_fn_sub, Ref

from ..devops.config_init import config

template = Template()

param_env_name = Parameter(
    "EnvironmentName",
    Type="String",
    Default=config.ENVIRONMENT_NAME.get_value()
)

template.add_parameter(param_env_name)

ec2_iam_policy = iam.ManagedPolicy(
    "EC2IamPolicy",
    template=template,
    PolicyDocument={
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::*/*"
            }
        ]
    }
)

ec2_iam_role = iam.Role(
    "EC2IamRole",
    template=template,
    RoleName=helper_fn_sub("{}-ec2-role", param_env_name),
    AssumeRolePolicyDocument=canned.iam.create_assume_role_policy_document([
        canned.iam.AWSServiceName.amazon_Elastic_Compute_Cloud_Amazon_EC2,
    ]),
    ManagedPolicyArns=[
        ec2_iam_policy.iam_managed_policy_arn,
    ],
)

template.create_resource_type_label()

# give all aws resource common tags
common_tags = {
    "EnvironmentName": Ref(param_env_name),
}
template.update_tags(common_tags)
