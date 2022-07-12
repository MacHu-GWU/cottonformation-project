# -*- coding: utf-8 -*-

"""
Example of cottonformation without intrinsic function.
"""

import attr
from boto_session_manager import BotoSesManager
import cottonformation as cf
from cottonformation.res import s3


# use Python data class to replace the CloudFormation Parameter System
@attr.s
class Params:
    project_name: str = attr.ib(default="cf-example-intrinsic-function")

# initialize params object
params = Params()

# get value of Pseudo Parameter value from AWS boto3 session
bsm = BotoSesManager()
aws_account_id = bsm.aws_account_id
aws_region = bsm.aws_region

tpl = cf.Template(
    Description="Intrinsic Function Example",
)

bucket = s3.Bucket(
    "S3Bucket",
    p_BucketName="-".join([aws_account_id, aws_region, params.project_name]),
    p_Tags=cf.Tag.make_many(
        Project=params.project_name,
    ),
)
tpl.add(bucket)

output_bucket_arn = cf.Output(
    "S3BucketArn",
    Value=cf.GetAtt(bucket, "Arn"),
    Export=cf.Export(
        # use f-string to replace Sub
        Name=f"{params.project_name}-s3-bucket"
    ),
)
tpl.add(output_bucket_arn)

if __name__ == "__main__":
    print(tpl.to_json())
