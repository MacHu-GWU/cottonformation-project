# -*- coding: utf-8 -*-

"""
This is an example CloudFormation stack to explain the ``Condition Function``
implementation in ``cottonformation``.

Consider the following use case.

1. You have a multi-region stack that will be deployed to many AWS Region in
the same AWS Account. For those globally unique resources like IAM Role,
you only want to create once in the "Main AWS Region". For example, your
main region is us-east-1, you only want to create IAM role in us-east-1
CloudFormation stack.

2. You may have multiple EC2 deployed in different region. You want to create
a tag to indicate that whether if it is in the "Main AWS Region". So you can
execute the same business logic in different ways.
"""

# First, import cottonformation, I prefer to use cf for a short name
import cottonformation as cf

# import the aws service module you need
from cottonformation.res import s3

# create a ``Template`` object to represent your cloudformation template
tpl = cf.Template(
    Description="Conditional Function Example",
)

# create main aws region ``Parameter`` object
param_main_aws_region = cf.Parameter(
    "MainAWSRegion",
    Type=cf.Parameter.TypeEnum.String,
    Default="us-east-1",
)
tpl.add(param_main_aws_region)

# create
condition_is_main_aws_region = cf.Equals(
    "IsMainAWSRegion",
    cf.AWS_REGION,
    param_main_aws_region,
)
tpl.add(condition_is_main_aws_region)

# this is a conditional IAM Role, only exists in the main aws region
# we don't want to create a REAL Role, so we create a S3 Bucket instead for
# demonstration purpose
iam_role_for_ec2 = s3.Bucket(
    "IamRoleForEC2",
    p_BucketName=cf.Join(
        "-", [cf.AWS_ACCOUNT_ID, "cottonformation", "example", "condition", "for-ec2"]
    ),
    ra_Condition=condition_is_main_aws_region,
)
tpl.add(iam_role_for_ec2)

# we don't want to create a REAL Role, so we create a S3 Bucket instead for
# demonstration purpose
ec2_server = s3.Bucket(
    "Ec2Server",
    p_BucketName=cf.Join(
        "-",
        [cf.AWS_ACCOUNT_ID, "cottonformation", "example", "condition", "ec2-server"],
    ),
    p_Tags=cf.Tag.make_many(
        # this is a dynamic value
        IsMainAwsRegion=cf.If(condition_is_main_aws_region, "Y", "N")
    ),
)
tpl.add(ec2_server)

if __name__ == "__main__":
    # your private aws account session and bucket for testing
    from cottonformation.tests.boto_ses import bsm

    # create an environment for deployment, it is generally a boto3 session
    # manager and an optional s3 bucket to upload cloudformation template
    env = cf.Env(bsm=bsm)

    # validate the template
    env.validate(tpl)

    # pretty print the template
    print(tpl.to_json())

    # json view of this template
    _ = {
        "AWSTemplateFormatVersion": "2010-09-09",
        "Description": "Conditional Function Example",
        "Metadata": {"cottonformation": {"version": "0.0.8"}},
        "Parameters": {"MainAWSRegion": {"Type": "String", "Default": "us-east-1"}},
        "Conditions": {
            "IsMainAWSRegion": {
                "Fn::Equals": [{"Ref": "AWS::Region"}, {"Ref": "MainAWSRegion"}]
            }
        },
        "Resources": {
            "IamRoleForEC2": {
                "Type": "AWS::S3::Bucket",
                "Condition": "IsMainAWSRegion",
                "Properties": {
                    "BucketName": {
                        "Fn::Join": [
                            "-",
                            [
                                {"Ref": "AWS::AccountId"},
                                "cottonformation",
                                "example",
                                "condition",
                                "for-ec2",
                            ],
                        ]
                    }
                },
            },
            "Ec2Server": {
                "Type": "AWS::S3::Bucket",
                "Properties": {
                    "BucketName": {
                        "Fn::Join": [
                            "-",
                            [
                                {"Ref": "AWS::AccountId"},
                                "cottonformation",
                                "example",
                                "condition",
                                "ec2-server",
                            ],
                        ]
                    },
                    "Tags": [
                        {
                            "Key": "IsMainAwsRegion",
                            "Value": {"Fn::If": ["IsMainAWSRegion", "Y", "N"]},
                        }
                    ],
                },
            },
        },
    }

    stack_name = "cottonformation-example-condition"
    # deploy this example
    env.deploy(tpl, stack_name=stack_name)

    # clean up AWS resources for this example
    env.delete(stack_name=stack_name)
