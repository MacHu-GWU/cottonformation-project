# -*- coding: utf-8 -*-

"""
This is an example about how to deploy CloudFormation and integrate it with
your DevOps automation scripts.

The CloudFormation template will be generated from a python script that taking
all configurations and smartly decide which AWS resource and the naming convention
should be created. You can extend it by changing the
``./cottonformation/cf/__init__.py`` file.

``troposphere_mate`` allows you to deploy your CloudFormation stack to AWS
from Python.
"""

import boto3
from cottonformation.cf import config, template, param_env_name
from troposphere_mate import StackManager

boto_ses = boto3.session.Session(
    profile_name=config.AWS_PROFILE_FOR_BOTO3.get_value(),
    region_name=config.AWS_REGION.get_value(),
)

sm = StackManager(boto_ses=boto_ses, cft_bucket=config.S3_BUCKET_FOR_DEPLOY.get_value())

sm.deploy(
    template=template,
    stack_name="pygitrepo-{}".format(config.ENVIRONMENT_NAME.get_value()),
    stack_parameters={
        param_env_name.title: "pygitrepo-{}".format(config.ENVIRONMENT_NAME.get_value()),
    },
    include_iam=True
)
