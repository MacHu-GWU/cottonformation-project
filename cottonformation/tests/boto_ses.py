# -*- coding: utf-8 -*-

import boto3

aws_profile = "eq_sanhe"
region = "us-east-1"
boto_ses = boto3.session.Session(profile_name=aws_profile, region_name=region)
bucket = "eq-sanhe-for-everything"
