# -*- coding: utf-8 -*-

import pytest
from pytest import raises
import cottonformation as ctf
from cottonformation.res import s3
from pprint import pprint
from collections import OrderedDict


class TestTemplateDependencySolver:
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
        out_b1 = ctf.Output("b1", Value=0, DependsOn=res_b1)

        for obj in [
            p_1, p_2, res_a, res_a1, res_a2, res_b, res_b1, res_b2, out_a1, out_b1,
        ]:
            tpl.add_one(obj)

        assert tpl._deps_data_need_build_flag == True
        _ = tpl.deps_on_data
        assert tpl._deps_data_need_build_flag == False

        assert tpl._deps_sort_need_build_flag == True
        _ = tpl.deps_sort
        assert tpl._deps_sort_need_build_flag == False

        assert tpl.deps_on_data == OrderedDict([
            ('1-Parameter--p1', set()),
            ('1-Parameter--p2', set()),
            ('5-Resource--a', set()),
            ('5-Resource--a1', {'5-Resource--a'}),
            ('5-Resource--a2', {'5-Resource--a'}),
            ('5-Resource--b', set()),
            ('5-Resource--b1', {'5-Resource--b'}),
            ('5-Resource--b2', {'5-Resource--b'}),
            ('6-Output--a1', {'5-Resource--a1'}),
            ('6-Output--b1', {'5-Resource--b1'})
        ])
        assert tpl.deps_by_data == OrderedDict([
            ('1-Parameter--p1', set()),
            ('1-Parameter--p2', set()),
            ('5-Resource--a', {'5-Resource--a2', '5-Resource--a1'}),
            ('5-Resource--a1', {'6-Output--a1'}),
            ('5-Resource--a2', set()),
            ('5-Resource--b', {'5-Resource--b1', '5-Resource--b2'}),
            ('5-Resource--b1', {'6-Output--b1'}),
            ('5-Resource--b2', set()),
            ('6-Output--a1', set()),
            ('6-Output--b1', set())]
        )
        assert tpl.deps_sort == OrderedDict([
            ('1-Parameter--p1', 0),
            ('1-Parameter--p2', 0),
            ('5-Resource--a', 0),
            ('5-Resource--b', 0),
            ('5-Resource--a1', 1),
            ('5-Resource--a2', 1),
            ('5-Resource--b1', 1),
            ('5-Resource--b2', 1),
            ('6-Output--a1', 2),
            ('6-Output--b1', 2)
        ])

    def test_cycle_dependency(self):
        tpl = ctf.Template()
        a = s3.Bucket("a", ra_DependsOn="c")
        b = s3.Bucket("b", ra_DependsOn=a)
        c = s3.Bucket("c", ra_DependsOn=b)
        for r in [a, b, c]:
            tpl.add_one(r)

        with raises(Exception):  # CircularDependencyError
            _ = tpl.deps_sort


class TestTemplateAddAWSObject:
    def test_add_one_good_case(self):
        tpl = ctf.Template()
        assert len(tpl.Parameters) == 0
        assert len(tpl.Resources) == 0
        assert len(tpl.Outputs) == 0

        p = ctf.Parameter("p", Type=ctf.Parameter.TypeEnum.String)
        tpl.add_one(p)
        assert len(tpl.Parameters) == 1

        b = s3.Bucket("b", p_BucketName="b1")
        tpl.add_one(b)
        assert len(tpl.Resources) == 1

        b = s3.Bucket("b", p_BucketName="b2")
        tpl.add_one(b, add_or_ignore=True)
        assert tpl.Resources["b"].p_BucketName == "b1"
        assert len(tpl.Resources) == 1

        b = s3.Bucket("b", p_BucketName="b2")
        tpl.add_one(b, add_or_update=True)
        assert tpl.Resources["b"].p_BucketName == "b2"
        assert len(tpl.Resources) == 1

        o = ctf.Output("o", Value=b.rv_WebsiteURL)
        tpl.add_one(o)
        assert len(tpl.Parameters) == 1
        assert len(tpl.Resources) == 1
        assert len(tpl.Outputs) == 1

    def test_add_one_exceptions(self):
        tpl = ctf.Template()
        b = s3.Bucket("b", p_BucketName="b")
        tpl.add_one(b)
        with raises(TypeError):
            tpl.add_one(1)
        with raises(ValueError):
            tpl.add_one(b, add_or_ignore=True, add_or_update=True)
        with raises(ctf.exc.AWSObjectLogicIdConlictError):
            tpl.add_one(b)

    def test_add_with_dependencies(self):
        # when adding an object having dependencies, it should also
        # add dependency objects to the template too.
        tpl = ctf.Template()

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

        assert tpl.n_named_object == 0

        tpl.add(o_1)
        tpl.add(o_2)
        assert tpl.n_named_object == 10

        tpl.add(o_a)
        tpl.add(o_b)
        assert tpl.n_named_object == 12

    def test_add_atomic(self):
        tpl = ctf.Template()
        b3 = s3.Bucket("b3", p_BucketName="b3-before")
        tpl.add_one(b3)

        b1 = s3.Bucket("b1", ra_DependsOn="not-exists")
        b2 = s3.Bucket("b2", ra_DependsOn=b1)
        b3 = s3.Bucket("b3", p_BucketName="b3-after", ra_DependsOn=b2)
        with raises(ctf.exc.AWSObjectNotExistsError):
            tpl.add(b3)

        assert tpl.n_named_object == 1
        assert tpl.Resources["b3"].p_BucketName == "b3-before"


class TestTemplateRemoveAWSObject:
    def test_remove_one_good_case(self):
        tpl = ctf.Template()
        b = s3.Bucket("b", p_BucketName="b")
        tpl.add(b)
        assert len(tpl.Resources) == 1

        # successfully removed, and the update_flag return value is correct
        assert tpl.remove_one(b) == True
        assert len(tpl.Resources) == 0

        # raise exception when remove a non-exists value
        with raises(ctf.exc.AWSObjectNotExistsError):
            tpl.remove_one(b)

        assert tpl.remove_one(b, ignore_not_exists=True) == False

    def test_remove_one_exceptions(self):
        tpl = ctf.Template()
        with raises(TypeError):
            tpl.remove_one(1)

    def test_remove_with_dependency_simple_cases(self):
        b1 = s3.Bucket("b1")
        b2 = s3.Bucket("b2", ra_DependsOn=b1)
        b3 = s3.Bucket("b3", ra_DependsOn=[b2, b1])

        objects = [b1, b2, b3]
        tpl = ctf.Template.from_many_objects(objects)
        assert tpl.n_named_object == 3
        tpl.remove(b1)
        assert tpl.n_named_object == 0

    def test_remove_with_dependent_complex_case(self):
        """
        If remove an object that there are many other objects depends on this,
        otherr objects are also removed.
        """
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
        tpl = ctf.Template.from_many_objects(res_list)
        tpl.remove(res_b)
        assert tpl._iterate_addable_keys() == ['1-Parameter--p1', '1-Parameter--p2', '5-Resource--a', '5-Resource--a1',
                                               '5-Resource--a2', '6-Output--oa']

        tpl = ctf.Template.from_many_objects(res_list)
        tpl.remove(res_b1)
        assert tpl._iterate_addable_keys() == ['1-Parameter--p1', '1-Parameter--p2', '5-Resource--a', '5-Resource--a1',
                                               '5-Resource--a2', '5-Resource--b', '5-Resource--b2', '6-Output--o2',
                                               '6-Output--oa']

        tpl = ctf.Template.from_many_objects(res_list)
        tpl.remove(res_b2)
        assert tpl._iterate_addable_keys() == ['1-Parameter--p1', '1-Parameter--p2', '5-Resource--a', '5-Resource--a1',
                                               '5-Resource--a2', '5-Resource--b', '5-Resource--b1', '6-Output--o1',
                                               '6-Output--oa']

        tpl = ctf.Template.from_many_objects(res_list)
        tpl.remove(p_1)
        assert tpl._iterate_addable_keys() == ['1-Parameter--p2', '5-Resource--a', '5-Resource--a2', '5-Resource--b',
                                               '5-Resource--b2', '6-Output--o2']

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
            rp_Code=awslambda.PropFunctionCode(
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
