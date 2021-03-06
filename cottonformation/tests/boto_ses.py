# -*- coding: utf-8 -*-

import boto3
from boto_session_manager import BotoSesManager

aws_profile = "aws_data_lab_sanhe"
region = "us-east-1"

boto_ses = boto3.session.Session(profile_name=aws_profile, region_name=region)
bsm = BotoSesManager(profile_name=aws_profile, region_name=region)

bucket = "aws-data-lab-sanhe-for-everything"
