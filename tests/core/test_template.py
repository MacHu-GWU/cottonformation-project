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

        assert tpl.add(b1) == True

        with raises(ValueError):
            tpl.add(b2)
        assert tpl.Resources["b"].p_BucketName == "b1"

        assert tpl.add_or_update(b2) == True
        assert tpl.Resources["b"].p_BucketName == "b2"

        assert tpl.add_or_ignore(b3) == False
        assert tpl.Resources["b"].p_BucketName == "b2"

        tpl = ctf.Template()
        p1 = ctf.Parameter("p", Type=ctf.Parameter.TypeEnum.String, Description="p1")
        p2 = ctf.Parameter("p", Type=ctf.Parameter.TypeEnum.String, Description="p2")
        p3 = ctf.Parameter("p", Type=ctf.Parameter.TypeEnum.String, Description="p3")

        assert tpl.add(p1) == True

        with raises(ValueError):
            tpl.add(p1)

        assert tpl.add_or_update(p2) == True
        assert tpl.Parameters["p"].Description == "p2"

        assert tpl.add_or_ignore(p3) == False
        assert tpl.Parameters["p"].Description == "p2"

    def test_add_error(self):
        tpl = ctf.Template()
        b = s3.Bucket("b", p_BucketName="b")
        with raises(TypeError):
            tpl.add(1)
        with raises(ValueError):
            tpl._add(b, add_or_ignore=True, add_or_update=True)

    def test_remove(self):
        tpl = ctf.Template()
        b = s3.Bucket("b", p_BucketName="b")

        tpl.add(b)
        assert len(tpl.Resources) == 1

        assert tpl.remove(b) == True
        assert len(tpl.Resources) == 0

        with raises(ValueError):
            tpl.remove(b)

        assert tpl.remove_and_ignore(b) == False

    def test_dependencies(self):
        tpl = ctf.Template()

        p_1 = ctf.Parameter("p1", Type="String")
        p_2 = ctf.Parameter("p2", Type="String")

        res_a = s3.Bucket("a")
        res_a1 = s3.Bucket("a1", ra_DependsOn=res_a)
        res_a2 = s3.Bucket("a2", ra_DependsOn=res_a)

        res_b = s3.Bucket("b")
        res_b1 = s3.Bucket("b1", ra_DependsOn=res_b)
        res_b2 = s3.Bucket("b2", ra_DependsOn=res_b)

        out_a1 = ctf.Output("a1", Value=0, DependsOn=res_a1)
        out_b1 = ctf.Output("a2", Value=0, DependsOn=res_b1)

        for obj in [
            p_1, p_2, res_a, res_a1, res_a2, res_b, res_b1, res_b2, out_a1, out_b1,
        ]:
            tpl.add(obj)

        assert tpl._deps_data_need_build_flag == True
        _ = tpl.deps_on_data
        assert tpl._deps_data_need_build_flag == False

        assert tpl._deps_sort_need_build_flag == True
        _ = tpl.deps_sort
        assert tpl._deps_sort_need_build_flag == False

        assert list(tpl.deps_on_data) == [
            "1-Parameter--p1", "1-Parameter--p2",
            "5-Resource--a", "5-Resource--a1", "5-Resource--a2",
            "5-Resource--b", "5-Resource--b1", "5-Resource--b2",
            "6-Output--a1", "6-Output--a2"
        ]

    def test_remove_with_dependent(self):
        p_1 = ctf.Parameter("p1", Type="String")
        p_2 = ctf.Parameter("p2", Type="String")

        res_a = s3.Bucket("a")
        res_a1 = s3.Bucket("a1", ra_DependsOn=[res_a, p_1])
        res_a2 = s3.Bucket("a2", ra_DependsOn=[res_a, p_2])

        res_b = s3.Bucket("b")
        res_b1 = s3.Bucket("b1", ra_DependsOn=[res_b, p_1])
        res_b2 = s3.Bucket("b2", ra_DependsOn=[res_b, p_2])

        o_1 = ctf.Output("o1", Value=0, DependsOn=[res_a1, res_b1])
        o_2 = ctf.Output("o2", Value=0, DependsOn=[res_a2, res_b2])
        o_a = ctf.Output("oa", Value=0, DependsOn=[res_a1, res_a2])
        o_b = ctf.Output("ob", Value=0, DependsOn=[res_b1, res_b2])

        res_list = [
            p_1, p_2,
            res_a, res_a1, res_a2, res_b, res_b1, res_b2,
            o_1, o_2, o_a, o_b,
        ]
        def mk_tpl() -> ctf.Template:
            tpl = ctf.Template()
            for res in res_list:
                tpl.add(res)
            return tpl

        tpl = mk_tpl()
        tpl.remove(res_b)
        assert tpl._iterate_addable_keys() == ['1-Parameter--p1', '1-Parameter--p2', '5-Resource--a', '5-Resource--a1', '5-Resource--a2', '6-Output--oa']

        tpl = mk_tpl()
        tpl.remove(res_b1)
        assert tpl._iterate_addable_keys() == ['1-Parameter--p1', '1-Parameter--p2', '5-Resource--a', '5-Resource--a1', '5-Resource--a2', '5-Resource--b', '5-Resource--b2', '6-Output--o2', '6-Output--oa']

        tpl = mk_tpl()
        tpl.remove(res_b2)
        assert tpl._iterate_addable_keys() == ['1-Parameter--p1', '1-Parameter--p2', '5-Resource--a', '5-Resource--a1', '5-Resource--a2', '5-Resource--b', '5-Resource--b1', '6-Output--o1', '6-Output--oa']

        tpl = mk_tpl()
        tpl.remove(p_1)
        assert tpl._iterate_addable_keys() == ['1-Parameter--p2', '5-Resource--a', '5-Resource--a2', '5-Resource--b', '5-Resource--b2', '6-Output--o2']

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
        tpl.to_json()


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
