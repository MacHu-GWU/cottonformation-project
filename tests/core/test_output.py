# -*- coding: utf-8 -*-

import pytest
from pytest import raises
from cottonformation.core.model import (
    Parameter, Export, Output, Ref, Sub, serialize,
)
from cottonformation.tests.helpers import jprint


class TestExport:
    def test_init_and_seialize(self):
        e = Export(Name="PublicIp")
        assert e.serialize() == {"Name": "PublicIp"}

        p = Parameter(
            "PublicIpExportName",
            Type=Parameter.TypeEnum.String,
        )
        e = Export(Name=Ref(p))
        assert e.serialize() == {"Name": {"Ref": "PublicIpExportName"}}


class TestOutput:
    def test_init_and_serialize(self):
        from cottonformation.res import ec2

        o = Output(
            "PublicIp",
            Description="The Public Ip",
            Value="0.0.0.0",
        )
        assert o.serialize() == {"Description": "The Public Ip", "Value": "0.0.0.0"}

        p = Parameter(
            "EC2Name",
            Type=Parameter.TypeEnum.String,
        )
        ec2_inst = ec2.Instance("MyEC2")

        o = Output(
            "PublicIp",
            Description=Sub(
                "The Public Ip for ${ec2_name}",
                dict(ec2_name=p.ref()),
            ),
            Value=ec2_inst.rv_PublicIp,
        )
        assert o.serialize() == {
            "Value": {
                "Fn::GetAtt": [
                    "MyEC2",
                    "PublicIp"
                ]
            },
            "Description": {
                "Fn::Sub": [
                    "The Public Ip for ${ec2_name}",
                    {"ec2_name": {"Ref": "EC2Name"}}
                ]
            }
        }


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
