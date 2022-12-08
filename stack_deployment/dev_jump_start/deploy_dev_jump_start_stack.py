# -*- coding: utf-8 -*-

from boto_session_manager import BotoSesManager
from pathlib_mate import Path
import cottonformation as cf
from cottonformation.stacks.dev_jump_start import DevJumpStartStack

aws_profile = "aws_sanhe_dev2_us_east_2"
main_aws_region = "us-east-1"

aws_region = "us-east-1"
# aws_region = "us-east-2"
# aws_region = "us-west-1"
# aws_region = "us-west-2"


bsm = BotoSesManager(profile_name=aws_profile, region_name=aws_region)
aws_account_id = bsm.aws_account_id

dir_here = Path.dir_here(__file__)


def deploy_stack():
    stack = DevJumpStartStack(
        aws_account_id=aws_account_id,
        main_aws_region=main_aws_region, aws_region=aws_region,
    )

    tpl = cf.Template()
    tpl.add(stack.rg1_s3)
    tpl.add(stack.rg2_iam_role)

    tpl.batch_tagging(dict(ProjectName="DevJumpBox"))

    p_tpl_json = Path(dir_here, "dev-jump-start-stack.json")
    p_tpl_yml = Path(dir_here, "dev-jump-start-stack.yml")
    tpl.to_json_file(p_tpl_json.abspath)
    tpl.to_yml_file(p_tpl_yml.abspath)

    env = cf.Env(bsm=bsm)
    env.deploy(
        template=tpl,
        stack_name=stack.stack_name,
        include_iam=True,
    )


def create_s3_folder():
    from s3pathlib import S3Path, context

    context.attach_boto_session(bsm.boto_ses)

    bucket = f"{aws_account_id}-{aws_region}-artifacts"
    p_list = [
        S3Path(bucket, "artifacts", "README.txt"),
        S3Path(bucket, "athena", "results", "README.txt"),
        S3Path(bucket, "lambda", "README.txt"),
        S3Path(bucket, "lambda", "artifacts", "README.txt"),
        S3Path(bucket, "glue", "README.txt"),
        S3Path(bucket, "glue", "scripts", "README.txt"),
        S3Path(bucket, "glue", "sparkHistoryLogs", "README.txt"),
        S3Path(bucket, "glue", "temporary", "README.txt"),
        S3Path(bucket, "cloudformation", "README.txt"),
        S3Path(bucket, "cloudtrail", "README.txt"),
        S3Path(bucket, "cloudwatch", "README.txt"),
        S3Path(bucket, "github", "README.txt"),
        S3Path(bucket, "gitlab", "README.txt"),
        S3Path(bucket, "tests", "unittest", "README.txt"),
        S3Path(bucket, "tests", "integration-test", "README.txt"),
        S3Path(bucket, "tests", "load-test", "README.txt"),
        S3Path(bucket, "datalake", "README.txt"),
        S3Path(bucket, "poc", "README.txt"),
    ]
    for p in p_list:
        p.write_text("S3 folder placeholder")


deploy_stack()
create_s3_folder()
