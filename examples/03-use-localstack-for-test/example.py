# -*- coding: utf-8 -*-

"""
A sample script that use cottonformation with localstack
"""

from boto_session_manager import BotoSesManager, AwsServiceEnum
import cottonformation as cft
from cottonformation.res import s3
from rich import print as rprint

tpl = cft.Template()
s3_bucket = s3.Bucket("MyBucket", p_BucketName="my-bucket")
tpl.add(s3_bucket)

endpoint_url = "http://localhost.localstack.cloud:4566"
bsm = BotoSesManager(default_client_kwargs=dict(endpoint_url=endpoint_url))

env = cft.Env(bsm=bsm)
env.deploy(template=tpl, stack_name="my-stack")
# env.delete(stack_name="my-stack")

s3_client = bsm.get_client(AwsServiceEnum.S3)
cf_client = bsm.get_client(AwsServiceEnum.CloudFormation)

res = cf_client.list_stacks()
rprint(res)
res = s3_client.list_buckets()
rprint(res)
