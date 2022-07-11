# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx
from cottonformation.core.model import (
    Ref,
    Base64,
    Cidr,
    FindInMap,
    GetAtt,
    GetAZs,
    ImportValue,
    Join,
    Select,
    Split,
    Sub,
    Transform,
    Parameter,
    Resource,
    Output,
    constant,
)


class TestRef:
    def test_init(self, stack):
        Ref(stack.param_project_name)
        Ref(stack.s3_bucket_artifact)
        Ref(stack.param_project_name.id)

        with pytest.raises(TypeError):
            Ref(stack.output_s3_bucket_artifact_arn)

        with pytest.raises(TypeError):
            Ref()

    def test_serialize(self, stack):
        assert Ref(stack.param_project_name.id).serialize() == {
            constant.IntrinsicFunction.REF: stack.param_project_name.id,
        }

        assert Ref(stack.param_project_name).serialize() == {
            constant.IntrinsicFunction.REF: stack.param_project_name.id,
        }

        assert Ref(stack.s3_bucket_artifact).serialize() == {
            constant.IntrinsicFunction.REF: stack.s3_bucket_artifact.id,
        }

    def test_eval(self, stack):
        assert Ref(stack.param_project_name.id).eval() == {
            constant.IntrinsicFunction.REF: stack.param_project_name.id,
        }

        assert Ref(stack.param_project_name).eval() == {
            constant.IntrinsicFunction.REF: stack.param_project_name.id,
        }

        assert Ref(stack.s3_bucket_artifact).eval() == {
            constant.IntrinsicFunction.REF: stack.s3_bucket_artifact.id,
        }


class TestSub:
    def test_init(self, stack):
        Sub("${arg}", dict(arg="value"))
        Sub(
            "${project_name}-${stage}",
            dict(project_name="my-app", stage="dev"),
        )
        Sub(
            "${project_name}-${stage}",
            dict(project_name=stack.param_project_name, stage=stack.param_stage),
        )

        with raises(TypeError):
            Sub()

        with raises(TypeError):  # missing data argument
            Sub("${arg1}")

        with raises(TypeError):
            Sub("${arg1}", "value1")  # pure value won't work

        with raises(ValueError) as e:
            Sub("${arg1}", dict(arg2="value1"))  # arg name doesn't match

    def test_from_params(self):
        p1 = Parameter("p1", Type=Parameter.TypeEnum.String)
        p2 = Parameter("p2", Type=Parameter.TypeEnum.String)
        sub = Sub.from_params("{}-{}", p1, p2)
        assert sub.serialize() == {
            constant.IntrinsicFunction.SUB: [
                "${p1}-${p2}",
                {
                    "p1": {constant.IntrinsicFunction.REF: "p1"},
                    "p2": {constant.IntrinsicFunction.REF: "p2"},
                },
            ]
        }

    def test_serialize(self):
        # 1. raw value
        sub = Sub("${arg1}", dict(arg1="value1"))
        assert sub.serialize() == {
            constant.IntrinsicFunction.SUB: ["${arg1}", {"arg1": "value1"}]
        }

        # 2. ref value
        sub = Sub("${arg1}", dict(arg1=Ref("Id1")))
        assert sub.serialize() == {
            constant.IntrinsicFunction.SUB: ["${arg1}", {"arg1": {"Ref": "Id1"}}]
        }

        # 3. Parameter
        param = Parameter("Param", Type=Parameter.TypeEnum.String)
        sub = Sub("${p}", dict(p=param))
        assert sub.serialize() == {
            constant.IntrinsicFunction.SUB: [
                "${p}",
                {"p": {constant.IntrinsicFunction.REF: "Param"}},
            ]
        }

        # 4. Resource
        obj = Resource("Object")
        sub = Sub("${obj}", dict(obj=obj))
        assert sub.serialize() == {
            constant.IntrinsicFunction.SUB: [
                "${obj}",
                {"obj": {constant.IntrinsicFunction.REF: "Object"}},
            ]
        }


class TestJoin:
    def test_init(self):
        # 1. good case
        p = Parameter("Parameter", Type=Parameter.TypeEnum.String)
        r = Resource("Resource")
        Join(delimiter="-", list_of_values=["a"])
        Join(
            delimiter="-", list_of_values=["a", {constant.IntrinsicFunction.REF: p.id}]
        )
        Join(
            delimiter="-", list_of_values=["a", {constant.IntrinsicFunction.REF: r.id}]
        )
        Join(delimiter="-", list_of_values=["a", p.ref()])
        Join(delimiter="-", list_of_values=["a", r.ref()])
        Join(delimiter="-", list_of_values=["a", p])
        Join(delimiter="-", list_of_values=["a", r])
        Join(delimiter="-", list_of_values=["a", p, r, p.ref(), r.ref()])

        Join(delimiter="-", list_of_values=["a"])
        Join(delimiter={constant.IntrinsicFunction.REF: p.id}, list_of_values=["a"])
        Join(delimiter=p, list_of_values=["a"])
        Join(delimiter=p.ref(), list_of_values=["a"])

        # 2. bad case
        with pytest.raises(TypeError):
            Join(delimiter=1, list_of_values=["a"])

        with pytest.raises(TypeError):
            Join(delimiter=["-", "_"], list_of_values=["a"])

        with pytest.raises(TypeError):
            Join(delimiter=r, list_of_values=["a"])

        with pytest.raises(TypeError):
            Join(delimiter="-", list_of_values="a")

        with pytest.raises(TypeError):
            Join(delimiter="-", list_of_values=1)

    def test_serialize(self):
        p = Parameter("Parameter", Type=Parameter.TypeEnum.String)
        r = Resource("Resource")

        join = Join(delimiter="-", list_of_values=["a", "b"])
        assert join.serialize() == {constant.IntrinsicFunction.JOIN: ["-", ["a", "b"]]}

        join = Join(
            delimiter="-", list_of_values=["a", {constant.IntrinsicFunction.REF: p.id}]
        )
        assert join.serialize() == {
            constant.IntrinsicFunction.JOIN: [
                "-",
                ["a", {constant.IntrinsicFunction.REF: p.id}],
            ]
        }

        join = Join(delimiter="-", list_of_values=["a", Ref(r)])
        assert join.serialize() == {
            constant.IntrinsicFunction.JOIN: [
                "-",
                ["a", {constant.IntrinsicFunction.REF: r.id}],
            ]
        }

        join = Join(delimiter="-", list_of_values=["a", p, r])
        assert join.serialize() == {
            constant.IntrinsicFunction.JOIN: [
                "-",
                [
                    "a",
                    {constant.IntrinsicFunction.REF: p.id},
                    {constant.IntrinsicFunction.REF: r.id},
                ],
            ]
        }

        join = Join(delimiter=p, list_of_values=["a"])
        assert join.serialize() == {
            constant.IntrinsicFunction.JOIN: [
                {constant.IntrinsicFunction.REF: p.id},
                [
                    "a",
                ],
            ]
        }

        join = Join(
            delimiter={constant.IntrinsicFunction.REF: p.id}, list_of_values=["a"]
        )
        assert join.serialize() == {
            constant.IntrinsicFunction.JOIN: [
                {constant.IntrinsicFunction.REF: p.id},
                [
                    "a",
                ],
            ]
        }

        join = Join(delimiter=Ref(p), list_of_values=["a"])
        assert join.serialize() == {
            constant.IntrinsicFunction.JOIN: [
                {constant.IntrinsicFunction.REF: p.id},
                [
                    "a",
                ],
            ]
        }


class TestBase64:
    def test_init(self):
        p = Parameter("Token", Type=Parameter.TypeEnum.String)

        with raises(Exception):
            Base64()

        with raises(TypeError):
            Base64(1)

        with raises(TypeError):
            Base64(p)

        Base64("the-token")
        Base64(p.ref())

    def test_serialize(self):
        p = Parameter("Token", Type=Parameter.TypeEnum.String)

        b64 = Base64(Ref(p))
        assert b64.serialize() == {
            constant.IntrinsicFunction.BASE64: {
                constant.IntrinsicFunction.REF: p.id,
            }
        }

        b64 = Base64("the-token")
        assert b64.serialize() == {constant.IntrinsicFunction.BASE64: "the-token"}


class TestGetAzs:
    def test(self):
        assert GetAZs.n_th(1).serialize() == {
            constant.IntrinsicFunction.SELECT: [
                0,
                {constant.IntrinsicFunction.GET_AZS: ""},
            ]
        }

        with raises(ValueError):
            GetAZs.n_th(0)


class TestSelect:
    def test(self):
        param = Parameter("RegionList", Type=Parameter.TypeEnum.CommaDelimitedList)
        select = Select(2, Ref(param))
        assert select.serialize() == {
            constant.IntrinsicFunction.SELECT: [
                2,
                {constant.IntrinsicFunction.REF: param.id},
            ]
        }


class TestImportValue:
    def test(self):
        imp = ImportValue("password")
        assert imp.serialize() == {constant.IntrinsicFunction.IMPORT_VALUE: "password"}
        sub = Sub("${env}-password", dict(env="dev"))
        imp = ImportValue(sub)
        assert imp.serialize() == {constant.IntrinsicFunction.IMPORT_VALUE: sub.eval()}


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
