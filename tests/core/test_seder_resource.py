# -*- coding: utf-8 -*-

import pytest
from cottonformation.res import iam, s3
from cottonformation.tests.helpers import jprint

_ = jprint


def test_easiest_case():
    """
    This is easiest case. No nested, no
    """
    iam_role = iam.Role(
        id="Name",
        rp_AssumeRolePolicyDocument={"key": "value"},
        p_RoleName="test-role",
        p_Policies=[
            iam.PropRolePolicy(
                rp_PolicyName="first-policy",
                rp_PolicyDocument={"key": "value"}
            )
        ],
    )
    assert iam_role.serialize() == {
        "Type": "AWS::IAM::Role",
        "Properties": {
            "AssumeRolePolicyDocument": {"key": "value"},
            "Policies": [
                {
                    "PolicyDocument": {"key": "value"},
                    "PolicyName": "first-policy"
                }
            ],
            "RoleName": "test-role"
        }
    }


def test_init_from_dict():
    iam_role = iam.Role(
        id="Name",
        rp_AssumeRolePolicyDocument={"key": "value"},
        p_RoleName="test-role",
        p_Policies=[
            {
                "rp_PolicyName": "first-policy",
                "rp_PolicyDocument": {"key": "value"}
            },
        ],
    )
    assert iam_role.serialize() == {
        "Type": "AWS::IAM::Role",
        "Properties": {
            "AssumeRolePolicyDocument": {"key": "value"},
            "Policies": [
                {
                    "PolicyDocument": {"key": "value"},
                    "PolicyName": "first-policy"
                }
            ],
            "RoleName": "test-role"
        }
    }


def test_intrinsic_function():
    bucket = s3.Bucket(id="MyBucket")


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
