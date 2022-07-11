# -*- coding: utf-8 -*-

import pytest

import attr
import cottonformation as cf
from cottonformation.res import s3


@attr.s
class Stack(cf.Stack):
    def __attrs_post_init__(self):
        self.mk_rg_01_param()
        self.mk_rg_02_s3_bucket()

    def mk_rg_01_param(self):
        self.rg01_param = cf.ResourceGroup()
        self.param_project_name = cf.Parameter("ProjectName", Type=cf.Parameter.TypeEnum.String)
        self.param_stage = cf.Parameter("Stage", Type=cf.Parameter.TypeEnum.String)

        self.rg01_param.add(self.param_project_name)
        self.rg01_param.add(self.param_stage)

        self.derived_param_env_name = cf.Sub(
            "${project_name}-${stage}",
            dict(
                project_name=self.param_project_name,
                stage=self.param_stage,
            ),
        )

    def mk_rg_02_s3_bucket(self):
        self.rg2_s3_bucket = cf.ResourceGroup()

        self.s3_bucket_artifact_name = cf.Join(
            "-",
            [cf.AWS_ACCOUNT_ID, cf.AWS_REGION, self.derived_param_env_name, "artifacts"]
        )
        self.s3_bucket_artifact = s3.Bucket(
            "S3BucketArtifacts",
            p_BucketName=self.s3_bucket_artifact_name,
        )
        self.rg2_s3_bucket.add(self.s3_bucket_artifact)

        self.s3_bucket_artifact_arn = cf.GetAtt(self.s3_bucket_artifact, "Arn")
        self.output_s3_bucket_artifact_arn = cf.Output(
            "S3BucketArtifactArn",
            Value=self.s3_bucket_artifact_arn,
        )
        self.rg2_s3_bucket.add(self.output_s3_bucket_artifact_arn)

        self.output_s3_bucket_artifact_name = cf.Output(
            "S3BucketArtifactName",
            Value=self.s3_bucket_artifact.ref(),
        )
        self.rg2_s3_bucket.add(self.output_s3_bucket_artifact_arn)


@pytest.fixture
def stack() -> Stack:
    return Stack()


@pytest.fixture
def template(stack) -> cf.Template:
    template = cf.Template(
        Description="ABC Company AWS Infra",
        Metadata=dict(
            Owner="ABC Company",
            CreateBy="john.david@company.com",
        )
    )
    return template
