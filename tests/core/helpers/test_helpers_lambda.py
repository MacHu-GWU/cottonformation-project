# -*- coding: utf-8 -*-

import pytest
from cottonformation.core.helpers import awslambda


def test_create_permission_for_s3_event():
    perm = awslambda.create_permission_for_s3_event(
        logic_id="LogicId",
        func="my-func",
        bucket="my-bucket",
    )


def test_create_permission_for_kinesis_data_stream():
    perm = awslambda.create_permission_for_kinesis_data_stream(
        logic_id="LogicId",
        func="my-func",
        data_stream="my-stream",
    )


def test_create_permission_for_firehose_delivery_stream():
    perm = awslambda.create_permission_for_firehose_delivery_stream(
        logic_id="LogicId",
        func="my-func",
        delivery_stream="my-stream",
    )


def test_create_permission_for_sns():
    perm = awslambda.create_permission_for_sns(
        logic_id="LogicId",
        func="my-func",
        topic="my-topic",
    )


def test_create_permission_for_sqs():
    perm = awslambda.create_permission_for_sqs(
        logic_id="LogicId",
        func="my-func",
        queue="my-queue",
    )


def test_create_permission_for_dynamodb():
    perm = awslambda.create_permission_for_dynamodb(
        logic_id="LogicId",
        func="my-func",
        table="my-table",
    )


def test_create_permission_for_code_commit():
    perm = awslambda.create_permission_for_code_commit(
        logic_id="LogicId",
        func="my-func",
        repo="my-repo",
    )


def test_create_permission_for_cloudwatch_event():
    perm = awslambda.create_permission_for_cloudwatch_event(
        logic_id="LogicId",
        func="my-func",
        rule="my-rule"
    )


def test_create_permission_for_msk():
    perm = awslambda.create_permission_for_msk(
        logic_id="LogicId",
        func="my-func",
        cluster="my-cluster",
        topic="my-topic",
    )


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
