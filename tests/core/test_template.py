# -*- coding: utf-8 -*-

import pytest
from pytest import raises
import cottonformation as ctf
from cottonformation.res import s3


class TestTemplate:
    def test_add(self):
        tpl = ctf.Template()
        b1 = s3.Bucket("b", p_BucketName="b1")
        b2 = s3.Bucket("b", p_BucketName="b2")
        b3 = s3.Bucket("b", p_BucketName="b3")

        tpl.add(b1)

        with raises(ValueError):
            tpl.add(b2)
        assert tpl.Resources["b"].p_BucketName == "b1"

        tpl.add_or_update(b2)
        assert tpl.Resources["b"].p_BucketName == "b2"

        tpl.add_or_ignore(b3)
        assert tpl.Resources["b"].p_BucketName == "b2"


        tpl = ctf.Template()
        p1 = ctf.Parameter("p", Type=ctf.Parameter.TypeEnum.String, Description="p1")
        p2 = ctf.Parameter("p", Type=ctf.Parameter.TypeEnum.String, Description="p2")
        p3 = ctf.Parameter("p", Type=ctf.Parameter.TypeEnum.String, Description="p3")

        tpl.add(p1)

        with raises(ValueError):
            tpl.add(p1)

        tpl.add_or_update(p2)
        assert tpl.Parameters["p"].Description == "p2"

        tpl.add_or_ignore(p3)
        assert tpl.Parameters["p"].Description == "p2"


    def test_complex_tpl_case1(self):
        import cottonformation as ctf
        from cottonformation.res import iam, awslambda

        tpl = ctf.Template()

        param_env_name = ctf.Parameter(
            "EnvName",
            Type=ctf.Parameter.TypeEnum.String,
        )
        tpl.add(param_env_name)

        iam_role_for_lambda = iam.Role(
            "IamRoleForLambdaExecution",
            rp_AssumeRolePolicyDocument=ctf.helpers.iam.AssumeRolePolicyBuilder(
                ctf.helpers.iam.ServicePrincipal.awslambda()
            ).build(),
            p_RoleName=ctf.Sub("${EnvName}-iam-role-for-lambda", dict(EnvName=param_env_name.ref())),
            p_Description="Minimal iam role for lambda execution",
            p_ManagedPolicyArns=[
                ctf.helpers.iam.AwsManagedPolicy.AWSLambdaBasicExecutionRole,
            ]
        )
        tpl.add(iam_role_for_lambda)

        lbd_source_code = """
        def handler(event, context):
            return "hello cottonformation"
        """.strip()

        lbd_func = awslambda.Function(
            "LbdFuncHelloWorld",
            rp_Code=awslambda.FunctionCode(
                p_ZipFile=lbd_source_code,
            ),
            rp_Role=iam_role_for_lambda.rv_Arn,
            p_MemorySize=256,
            p_Timeout=3,
            p_Runtime=ctf.helpers.awslambda.LambdaRuntime.python37,
            p_Handler="index.handler"
        )
        tpl.add(lbd_func)

        out_lambda_role_arn = ctf.Output(
            "LbdRoleArn",
            Description="aws lambda basic execution iam role for reuse",
            Value=iam_role_for_lambda
        )
        tpl.add(out_lambda_role_arn)

        print(tpl.to_json())



if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
