# -*- coding: utf-8 -*-

import boto3
import cottonformation as cf
from cottonformation.stacks.vpc import VpcStack
import pysecret
from pathlib_mate import Path

# ------ load secret data ------
# below is a code snippet that load config and secret data
# for testing, you can comment it out and manually pass in hard code value
here = Path(__file__).parent
config_file = Path(here, "config.json")
config = pysecret.JsonSecret.new(secret_file=config_file.abspath)
# ------------------------------

vpc_stack = VpcStack(
    project_name=config.get("example-stack.vpc.project_name"),
    stage=config.get("example-stack.vpc.stage"),
    vpc_cidr_seed=config.get("example-stack.vpc.vpc_cidr_seed"),
    n_az_used=config.get("example-stack.vpc.n_az_used"),
    n_subnet_per_az_per_public_private=config.get("example-stack.vpc.n_subnet_per_az_per_public_private"),
    sg_authorized_ips=config.get("example-stack.vpc.sg_authorized_ips")
)

tpl = cf.Template()
tpl.add(vpc_stack.rg1_vpc)
tpl.add(vpc_stack.rg2_subnet)
tpl.add(vpc_stack.rg3_route)
tpl.add(vpc_stack.rg4_security_group)

tpl.batch_tagging(dict(ProjectName=vpc_stack.project_name, Stage=vpc_stack.stage))

if __name__ == "__main__":
    boto_ses = boto3.session.Session(profile_name="aws_sanhe_dev1_us_east_2")
    bucket = "616773776376-us-east-2-artifacts"
    # boto_ses = boto3.session.Session(profile_name="aws_sanhe_dev2_us_east_2")
    # bucket = "190823475593-us-east-2-artifacts"
    env = cf.Env(boto_ses=boto_ses)
    env.deploy(
        template=tpl,
        stack_name=vpc_stack.stack_name,
        bucket_name=bucket,
    )
