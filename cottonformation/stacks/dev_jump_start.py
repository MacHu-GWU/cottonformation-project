# -*- coding: utf-8 -*-

import attr
import cottonformation as cf
from cottonformation.res import (
    s3, iam,
)


@attr.s
class DevJumpStartStack(cf.Stack):
    main_aws_region = attr.ib()
    aws_account_id = attr.ib()
    aws_region = attr.ib()

    @property
    def stack_name(self):
        return "dev-jump-start"

    def mk_rg1_s3(self):
        self.rg1_s3 = cf.ResourceGroup()

        self.s3_bucket_artifacts = s3.Bucket(
            "S3BucketForArtifacts",
            p_BucketName=f"{self.aws_account_id}-{self.aws_region}-artifacts"
        )
        self.rg1_s3.add(self.s3_bucket_artifacts)

        self.s3_bucket_data = s3.Bucket(
            "S3BucketForData",
            p_BucketName=f"{self.aws_account_id}-{self.aws_region}-data"
        )
        self.rg1_s3.add(self.s3_bucket_data)

    def mk_rg2_iam_role(self):
        """
        Create a Jumpbox on Public Subnet for developer to use.
        """
        self.rg2_iam_role = cf.ResourceGroup()

        if self.main_aws_region == self.aws_region:
            self.iam_role_any_service_for_admin = iam.Role(
                "IamRoleAnyServiceForAdmin",
                rp_AssumeRolePolicyDocument=cf.helpers.iam.AssumeRolePolicyBuilder(
                    cf.helpers.iam.ServicePrincipal.ec2(),
                    cf.helpers.iam.ServicePrincipal.cloud9(),
                    cf.helpers.iam.ServicePrincipal.awslambda(),
                    cf.helpers.iam.ServicePrincipal.ecs(),
                    cf.helpers.iam.ServicePrincipal.eks(),
                    cf.helpers.iam.ServicePrincipal.glue(),
                    cf.helpers.iam.ServicePrincipal.sagemaker(),
                    cf.helpers.iam.ServicePrincipal.textract(),
                    cf.helpers.iam.ServicePrincipal.comprehend(),
                    cf.helpers.iam.ServicePrincipal.rekognition(),
                    cf.helpers.iam.ServicePrincipal.stepfunctions(),
                    cf.helpers.iam.ServicePrincipal.kinesis(),
                    cf.helpers.iam.ServicePrincipal.firehose(),
                    cf.helpers.iam.ServicePrincipal.apigateway(),
                    cf.helpers.iam.ServicePrincipal.elasticbeanstalk(),
                    cf.helpers.iam.ServicePrincipal.rds(),
                    cf.helpers.iam.ServicePrincipal.dynamodb(),
                    cf.helpers.iam.ServicePrincipal.opensearch(),
                    cf.helpers.iam.ServicePrincipal.elasticache(),
                    cf.helpers.iam.ServicePrincipal.memorydb(),
                    cf.helpers.iam.ServicePrincipal.sns(),
                    cf.helpers.iam.ServicePrincipal.sqs(),
                ).build(),
                p_RoleName=f"any-service-for-admin",
                p_ManagedPolicyArns=[
                    cf.helpers.iam.AwsManagedPolicy.AdministratorAccess,
                ]
            )
            self.rg2_iam_role.add(self.iam_role_any_service_for_admin)

    def post_hook(self):
        self.mk_rg1_s3()
        self.mk_rg2_iam_role()
