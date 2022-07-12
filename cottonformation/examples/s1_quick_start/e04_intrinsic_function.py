# -*- coding: utf-8 -*-

"""
In 90% of the case, it is unnecessary with ``cottonformation``. Because you are
writing CloudFormation in Python, and it is way easier and manageable
to do so in Python.

However, ``cottonformation`` has the ability to use the native Intrinsic Functions.
"""

# First, import cottonformation, I prefer to use cf for a short name
import cottonformation as cf

# import the aws service module you need
from cottonformation.res import s3

# create a ``Template`` object to represent your cloudformation template
tpl = cf.Template(
    Description="Intrinsic Function Example",
)

# create project name ``Parameter`` object
# it is a common prefix for all naming convention
param_project_name = cf.Parameter(
    "ProjectName",
    Type=cf.Parameter.TypeEnum.String,
    Default="cf-example-intrinsic-function",
)
tpl.add(param_project_name)

# create a dummy ``Resource`` object for aws s3 bucket
# this bucket object is just a data container to demonstrate intrinsic function
bucket = s3.Bucket(
    "S3Bucket",
    p_BucketName=cf.Join(
        delimiter="-",
        list_of_values=[
            cf.AWS_ACCOUNT_ID,
            cf.AWS_REGION,
            param_project_name,
        ],
    ),
    # a Ref example
    p_Tags=cf.Tag.make_many(
        Project1=cf.Ref(param_project_name),  # you can Ref
        Project2=param_project_name.ref(),  # or use the oop style Ref
        Project3=param_project_name,  # or just use Parameter itself
    ),
)
tpl.add(bucket)

output_bucket_arn = cf.Output(
    "S3BucketArn",
    # a Fn::GetAttr example
    Value=cf.GetAtt(bucket, "Arn"),  # you can use ``bucket.rv_Arn`` shortcut too
    # an Output.Export example, you can use
    # cf.ImportValue(name="my-project-name-s3-bucket") to reference it later
    Export=cf.Export(
        # a Fn::Sub example
        # cottonformation is smart enough to pass in a parameter object
        # directly without reference
        Name=cf.Sub(
            "${project_name}-s3-bucket",
            dict(project_name=param_project_name),
        )
    ),
)
tpl.add(output_bucket_arn)

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
        "Description": "Intrinsic Function Example",
        "Metadata": {"cottonformation": {"version": "0.0.7"}},
        "Parameters": {
            "ProjectName": {
                "Type": "String",
                "Default": "cf-example-intrinsic-function",
            }
        },
        "Resources": {
            "S3Bucket": {
                "Type": "AWS::S3::Bucket",
                "Properties": {
                    "BucketName": {
                        "Fn::Join": [
                            "-",
                            [
                                {"Ref": "AWS::AccountId"},
                                {"Ref": "AWS::Region"},
                                {"Ref": "ProjectName"},
                            ],
                        ]
                    },
                    "Tags": [
                        {"Key": "Project1", "Value": {"Ref": "ProjectName"}},
                        {"Key": "Project2", "Value": {"Ref": "ProjectName"}},
                        {"Key": "Project3", "Value": {"Ref": "ProjectName"}},
                    ],
                },
            }
        },
        "Outputs": {
            "S3BucketArn": {
                "Value": {"Fn::GetAtt": ["S3Bucket", "Arn"]},
                "Export": {
                    "Name": {
                        "Fn::Sub": [
                            "${project_name}-s3-bucket",
                            {"project_name": {"Ref": "ProjectName"}},
                        ]
                    }
                },
            }
        },
    }

    stack_name = "cottonformation-example-intrinsic-func"
    # deploy this example
    env.deploy(tpl, stack_name=stack_name)

    # clean up AWS resources for this example
    # env.delete(stack_name=stack_name)
