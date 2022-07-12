# -*- coding: utf-8 -*-

"""
Example of cottonformation without condition function.
"""

import attr
from boto_session_manager import BotoSesManager
import cottonformation as cf
from cottonformation.res import s3


# use Python data class to replace the CloudFormation Parameter System
@attr.s
class Params:
    main_aws_region: str = attr.ib(default="us-east-1")


# initialize params object
params = Params()

# get value of Pseudo Parameter value from AWS boto3 session
bsm = BotoSesManager()
aws_account_id = bsm.aws_account_id
aws_region = bsm.aws_region

tpl = cf.Template(
    Description="Conditional Function Example",
)

# use if else logic to declare conditional resource
if params.main_aws_region == aws_region:
    iam_role_for_ec2 = s3.Bucket(
        "IamRoleForEC2",
        p_BucketName=cf.Join(
            "-", [aws_account_id, "cottonformation", "example", "condition", "for-ec2"]
        ),
    )
    tpl.add(iam_role_for_ec2)

ec2_server = s3.Bucket(
    "Ec2Server",
    p_BucketName=cf.Join(
        "-",
        [cf.AWS_ACCOUNT_ID, "cottonformation", "example", "condition", "ec2-server"],
    ),
    p_Tags=cf.Tag.make_many(
        # use if else statement to replace Condition Function If
        IsMainAwsRegion="Y"
        if params.main_aws_region == aws_region
        else "N"
    ),
)
tpl.add(ec2_server)

if __name__ == "__main__":
    tpl.to_json()
