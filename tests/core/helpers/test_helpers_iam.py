# -*- coding: utf-8 -*-

import pytest
from cottonformation.core import helpers
from cottonformation.tests.helpers import jprint


class TestAssumeRolePolicyBuilder:
    def test_build(self):
        expected = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": "arn:aws:iam::111122223333:root"
                    },
                    "Action": "sts:AssumeRole",
                    "Condition": {
                        "StringEquals": {
                            "sts:ExternalId": "ext"
                        },
                        "Bool": {
                            "aws:MultiFactorAuthPresent": "true"
                        }
                    }
                },
                {
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": "arn:aws:iam::444455556666:root"
                    },
                    "Action": "sts:AssumeRole",
                },
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": [
                            "ec2.amazonaws.com",
                            "lambda.amazonaws.com",
                            "ecs.amazonaws.com",
                        ]
                    },
                    "Action": "sts:AssumeRole"
                },
            ]
        }
        assert helpers.iam.AssumeRolePolicyBuilder(
            helpers.iam.ServicePrincipal.ec2(),
            helpers.iam.ServicePrincipal.awslambda(),
            "ecs.amazonaws.com",
            helpers.iam.AccountPrincipal("111122223333", external_id="ext", mfa_auth=True),
            "444455556666",
        ).build() == expected


class TestAwsManagedPolicy:
    def test(self):
        _ = helpers.iam.AwsManagedPolicy.AmazonEC2FullAccess
        _ = helpers.iam.AwsManagedPolicy.AWSLambdaBasicExecutionRole


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
