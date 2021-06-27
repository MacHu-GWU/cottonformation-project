# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx
from cottonformation.core.model import (
    Ref, Base64, Cidr, FindInMap, GetAtt, GetAZs, ImportValue,
    Join, Select, Split, Sub, Transform,
    Parameter, Resource, Output,
)
from cottonformation.tests.helpers import jprint


class TestRef:
    def test(self):
        p = Parameter("Name", Type=Parameter.TypeEnum.String)
        ref = Ref(p)
        assert ref.serialize() == {"Ref": "Name"}


class TestSub:
    def test(self):
        sub = Sub("${arg1}", dict(arg1=Ref("Id1")))
        assert sub.serialize() == {
            "Fn::Sub": [
                "${arg1}",
                {"arg1": {"Ref": "Id1"}}
            ]
        }





if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
