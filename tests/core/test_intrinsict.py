# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx
from cottonformation.core.model import (
    Ref, Base64, Cidr, FindInMap, GetAtt, GetAZs, ImportValue,
    Join, Select, Split, Sub, Transform,
    Parameter, Resource, Output, constant
)
from cottonformation.tests.helpers import jprint


class TestRef:
    def test(self):
        p = Parameter("Name", Type=Parameter.TypeEnum.String)
        ref = Ref(p)
        assert ref.serialize() == {"Ref": "Name"}


class TestSub:
    def test_init(self):
        p = Parameter("Name", Type=Parameter.TypeEnum.String)

        with raises(TypeError):
            Sub()

        with raises(TypeError):
            Sub("${arg1}")

        with raises(TypeError):
            Sub("${arg1}", "value1")

        Sub("${arg1}", dict(arg1="value1"))
        Sub("${arg1}", dict(arg1=p.ref()))

    def test(self):
        p1 = Parameter("p1", Type=Parameter.TypeEnum.String)
        p2 = Parameter("p2", Type=Parameter.TypeEnum.String)
        sub = Sub.from_params("{}-{}", p1, p2)
        assert sub.serialize() == {
            constant.IntrinsicFunction.SUB: [
                "${p1}-${p2}",
                {
                    "p1": {constant.IntrinsicFunction.REF: "p1"},
                    "p2": {constant.IntrinsicFunction.REF: "p2"}
                }
            ]
        }

    def test_serialize(self):
        sub = Sub("${arg1}", dict(arg1="value1"))
        assert sub.serialize() == {
            "Fn::Sub": [
                "${arg1}",
                {"arg1": "value1"}
            ]
        }

        sub = Sub("${arg1}", dict(arg1=Ref("Id1")))
        assert sub.serialize() == {
            "Fn::Sub": [
                "${arg1}",
                {"arg1": {"Ref": "Id1"}}
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
        assert b64.serialize() == {
            constant.IntrinsicFunction.BASE64: "the-token"
        }


class TestGetAzs:
    def test(self):
        assert GetAZs.n_th(1).serialize() == {
            constant.IntrinsicFunction.SELECT: [
                0,
                {constant.IntrinsicFunction.GET_AZS: ""}
            ]
        }

        with raises(ValueError):
            GetAZs.n_th(0)

if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
