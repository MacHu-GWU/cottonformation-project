# -*- coding: utf-8 -*-

from boto_session_manager import BotoSesManager

aws_profile = "aws_data_lab_sanhe_us_east_1"
region = "us-east-1"

bsm = BotoSesManager(profile_name=aws_profile, region_name=region)
boto_ses = bsm.boto_ses

bucket = "aws-data-lab-sanhe-for-everything-us-east-1"
