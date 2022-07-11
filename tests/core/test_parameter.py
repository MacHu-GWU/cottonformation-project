# -*- coding: utf-8 -*-

import pytest
from pytest import raises
from cottonformation.core.model import (
    Parameter, Output, Export,
    Ref, constant,
)


class TestParameter:
    def test_init(self):
        Parameter(
            "ProjectName",
            Type=Parameter.TypeEnum.String,
        )

        Parameter(
            "ProjectName",
            Type=Parameter.TypeEnum.AWS_EC2_Image_Id,
        )

        Parameter(
            "ProjectName",
            Type="AWS::SSM::Parameter::Value<String>",
        )

        with raises(ValueError):
            Parameter(
                "ProjectName",
                Type="Not a valid type!",
            )

    def test_ref(self):
        assert isinstance(Parameter("p", Type="String").ref(), Ref)

    def test_serialize(self):
        p = Parameter(
            "ProjectName",
            Type=Parameter.TypeEnum.String,
            Description="The project name",
            Default="my-project"
        )
        assert p.serialize() == {
            "Type": "String",
            "Description": "The project name",
            "Default": "my-project",
        }

    def test_eval(self):
        p = Parameter(
            "ProjectName",
            Type=Parameter.TypeEnum.String,
        )
        assert p.eval() == {
            constant.IntrinsicFunction.REF: "ProjectName"
        }


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
