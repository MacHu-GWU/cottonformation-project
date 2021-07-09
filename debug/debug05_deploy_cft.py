# -*- coding: utf-8 -*-

import boto3
from cottonformation.core.template import Template
from cottonformation.core.model import (
    Parameter, Output,
    Ref, Sub, serialize,
)
from cottonformation.res import (
    s3,
)
from cottonformation.core.env import Env

tpl = Template()

param_project_name = Parameter(
    "ProjectName",
    Type=Parameter.TypeEnum.String,
    Default="cottonformation-dev",
)
tpl.add(param_project_name)

bucket = s3.Bucket(
    "MyBucket",
    p_BucketName=Sub("${ProjectName}-bucket", dict(ProjectName=param_project_name.ref())),
)
tpl.add(bucket)

out_bucket_domain_name = Output(
    "MyBucketDomainName",
    Value=bucket.rv_DomainName,
)
tpl.add(out_bucket_domain_name)

# tpl.to_json_file("tpl.json")

# print(tpl.Parameters["ProjectName"])
# print(serialize(tpl.Parameters["ProjectName"]))
# print(serialize(tpl.Parameters))

# print(tpl.Resources["MyBucket"])
# print(serialize(tpl.Resources["MyBucket"]))

# print(tpl.Outputs)
# print(serialize(tpl.Resources["MyBucket"]))


boto_ses = boto3.session.Session(profile_name="eq_sanhe")
env = Env(boto_ses=boto_ses)
env.deploy(
    template=tpl,
    stack_name="test-stack",
    bucket_name="eq-sanhe-for-everything",
)
