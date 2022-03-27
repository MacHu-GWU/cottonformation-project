# -*- coding: utf-8 -*-

from typing import Union
from ...res import (
    awslambda, s3, kinesis, kinesisfirehose, sns, sqs, dynamodb,
    codecommit, events, msk,
)
from ..model import AWS_ACCOUNT_ID, AWS_REGION, Sub


class LambdaRuntime:
    """
    Aws Lambda related constant helpers.

    This data is based on https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html
    """
    nodejs14 = "nodejs14.x"
    nodejs12 = "nodejs12.x"
    nodejs10 = "nodejs10.x"

    python39 = "python3.9"
    python38 = "python3.8"
    python37 = "python3.7"
    python36 = "python3.6"
    python27 = "python2.7"

    ruby27 = "ruby2.7"
    ruby25 = "ruby2.5"

    java11 = "java11"
    java8amzlinux2 = "java8.al2"
    java8amzlinux1 = "java8"

    go1x = "go1.x"

    dotnet31 = "dotnetcore3.1"
    dotnet21 = "dotnetcore2.1"

    custom_amzlinux2 = "provided.al2"
    custom_amzlinux1 = "provided"


def _to_func_arn(func: Union[str, awslambda.Function]):
    if isinstance(func, str):
        function_name = Sub(
            string="arn:aws:lambda:${aws_region}:${aws_account_id}:function:${func_name}",
            data=dict(
                aws_account_id=AWS_ACCOUNT_ID,
                aws_region=AWS_REGION,
                func_name=func,
            ),
        )
    else:
        function_name = func.rv_Arn
    return function_name


def create_permission_for_s3_event(
    logic_id: str,
    func: Union[str, awslambda.Function],
    bucket: Union[str, s3.Bucket],
) -> awslambda.Permission:
    """
    .. note::

        The s3 bucket has to be in the same region of lambda function.

    .. note::

        The source arn has to be a bucket without any prefix, otherwise it
        won't pass the validation.

    Ref:

    - https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html
    """
    func_arn = _to_func_arn(func)
    if isinstance(bucket, str):
        if bucket.startswith("arn:aws:s3:::"):
            source_arn = bucket
        else:
            source_arn = f"arn:aws:s3:::{bucket}"
    else:
        source_arn = Sub(
            string="arn:aws:s3:::${bucket}",
            data=dict(bucket=bucket.ref())
        )
    return awslambda.Permission(
        logic_id,
        rp_FunctionName=func_arn,
        rp_Action="lambda:InvokeFunction",
        rp_Principal="s3.amazonaws.com",
        p_SourceArn=source_arn,
        p_SourceAccount=AWS_ACCOUNT_ID,
    )


def create_permission_for_kinesis_data_stream(
    logic_id: str,
    func: Union[str, awslambda.Function],
    data_stream: Union[str, kinesis.Stream]
):
    """
    Ref:

    - https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html
    """
    func_arn = _to_func_arn(func)
    if isinstance(data_stream, str):
        if data_stream.startswith("arn:aws:kinesis:"):
            source_arn = data_stream
        else:
            source_arn = Sub(
                string="arn:aws:kinesis:${aws_region}:${aws_account_id}:stream/${data_stream}",
                data=dict(
                    aws_account_id=AWS_ACCOUNT_ID,
                    aws_region=AWS_REGION,
                    data_stream=data_stream,
                )
            )
    else:
        source_arn = data_stream.rv_Arn
    return awslambda.Permission(
        logic_id,
        rp_FunctionName=func_arn,
        rp_Action="lambda:InvokeFunction",
        rp_Principal="kinesis.amazonaws.com",
        p_SourceArn=source_arn,
        p_SourceAccount=AWS_ACCOUNT_ID,
    )


def create_permission_for_firehose_delivery_stream(
    logic_id: str,
    func: Union[str, awslambda.Function],
    delivery_stream: Union[str, kinesisfirehose.DeliveryStream]
):
    """
    Ref:

    - https://docs.aws.amazon.com/lambda/latest/dg/services-kinesisfirehose.html
    """
    func_arn = _to_func_arn(func)
    if isinstance(delivery_stream, str):
        if delivery_stream.startswith("arn:aws:firehose:"):
            source_arn = delivery_stream
        else:
            source_arn = Sub(
                string="arn:aws:firehose:${aws_region}:${aws_account_id}:deliverystream/${delivery_stream}",
                data=dict(
                    aws_account_id=AWS_ACCOUNT_ID,
                    aws_region=AWS_REGION,
                    delivery_stream=delivery_stream,
                )
            )
    else:
        source_arn = delivery_stream.rv_Arn
    return awslambda.Permission(
        logic_id,
        rp_FunctionName=func_arn,
        rp_Action="lambda:InvokeFunction",
        rp_Principal="firehose.amazonaws.com",
        p_SourceArn=source_arn,
        p_SourceAccount=AWS_ACCOUNT_ID,
    )


def create_permission_for_sns(
    logic_id: str,
    func: Union[str, awslambda.Function],
    topic: Union[str, sns.Topic]
):
    """
    Ref:

    - https://docs.aws.amazon.com/lambda/latest/dg/with-sns.html
    """
    func_arn = _to_func_arn(func)
    if isinstance(topic, str):
        if topic.startswith("arn:aws:sns:"):
            source_arn = topic
        else:
            source_arn = Sub(
                string="arn:aws:sns:${aws_region}:${aws_account_id}:${sns_topic}",
                data=dict(
                    aws_account_id=AWS_ACCOUNT_ID,
                    aws_region=AWS_REGION,
                    sns_topic=topic,
                )
            )
    else:
        source_arn = topic.ref()
    return awslambda.Permission(
        logic_id,
        rp_FunctionName=func_arn,
        rp_Action="lambda:InvokeFunction",
        rp_Principal="sns.amazonaws.com",
        p_SourceArn=source_arn,
        p_SourceAccount=AWS_ACCOUNT_ID,
    )


def create_permission_for_sqs(
    logic_id: str,
    func: Union[str, awslambda.Function],
    queue: Union[str, sqs.Queue]
):
    """
    Ref:

    - https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html
    """
    func_arn = _to_func_arn(func)
    if isinstance(queue, str):
        if queue.startswith("arn:aws:sqs:"):
            source_arn = queue
        else:
            source_arn = Sub(
                string="arn:aws:sqs:${aws_region}:${aws_account_id}:${queue}",
                data=dict(
                    aws_account_id=AWS_ACCOUNT_ID,
                    aws_region=AWS_REGION,
                    queue=queue,
                )
            )
    else:
        source_arn = queue.ref()
    return awslambda.Permission(
        logic_id,
        rp_FunctionName=func_arn,
        rp_Action="lambda:InvokeFunction",
        rp_Principal="sqs.amazonaws.com",
        p_SourceArn=source_arn,
        p_SourceAccount=AWS_ACCOUNT_ID,
    )


def create_permission_for_dynamodb(
    logic_id: str,
    func: Union[str, awslambda.Function],
    table: Union[str, dynamodb.Table]
):
    """
    Ref:

    - https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html
    """
    func_arn = _to_func_arn(func)
    if isinstance(table, str):
        if table.startswith("arn:aws:dynamodb:"):
            source_arn = table
        else:
            source_arn = Sub(
                string="arn:aws:dynamodb:${aws_region}:${aws_account_id}:table/${table}",
                data=dict(
                    aws_account_id=AWS_ACCOUNT_ID,
                    aws_region=AWS_REGION,
                    table=table,
                )
            )
    else:
        source_arn = table.rv_Arn
    return awslambda.Permission(
        logic_id,
        rp_FunctionName=func_arn,
        rp_Action="lambda:InvokeFunction",
        rp_Principal="dynamodb.amazonaws.com",
        p_SourceArn=source_arn,
        p_SourceAccount=AWS_ACCOUNT_ID,
    )


def create_permission_for_code_commit(
    logic_id: str,
    func: Union[str, awslambda.Function],
    repo: Union[str, codecommit.Repository]
):
    """
    Ref:

    - https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html
    """
    func_arn = _to_func_arn(func)
    if isinstance(repo, str):
        if repo.startswith("arn:aws:codecommit:"):
            source_arn = repo
        else:
            source_arn = Sub(
                string="arn:aws:codecommit:${aws_region}:${aws_account_id}:${repo}",
                data=dict(
                    aws_account_id=AWS_ACCOUNT_ID,
                    aws_region=AWS_REGION,
                    repo=repo,
                )
            )
    else:
        source_arn = repo.rv_Arn
    return awslambda.Permission(
        logic_id,
        rp_FunctionName=func_arn,
        rp_Action="lambda:InvokeFunction",
        rp_Principal="codecommit.amazonaws.com",
        p_SourceArn=source_arn,
        p_SourceAccount=AWS_ACCOUNT_ID,
    )


def create_permission_for_cloudwatch_event(
    logic_id: str,
    func: Union[str, awslambda.Function],
    rule: Union[str, events.Rule]
):
    """
    Ref:

    - https://docs.aws.amazon.com/lambda/latest/dg/services-cloudwatchevents.html
    """
    func_arn = _to_func_arn(func)
    if isinstance(rule, str):
        if rule.startswith("arn:aws:events:"):
            source_arn = rule
        else:
            source_arn = Sub(
                string="arn:aws:events:${aws_region}:${aws_account_id}:rule/${rule}",
                data=dict(
                    aws_account_id=AWS_ACCOUNT_ID,
                    aws_region=AWS_REGION,
                    rule=rule,
                )
            )
    else:
        source_arn = rule.rv_Arn
    return awslambda.Permission(
        logic_id,
        rp_FunctionName=func_arn,
        rp_Action="lambda:InvokeFunction",
        rp_Principal="events.amazonaws.com",
        p_SourceArn=source_arn,
        p_SourceAccount=AWS_ACCOUNT_ID,
    )


def create_permission_for_msk(
    logic_id: str,
    func: Union[str, awslambda.Function],
    cluster: Union[str, msk.Cluster],
    topic: str,
    cluster_uuid: str = None,
):
    """
    Ref:

    - https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html
    """
    func_arn = _to_func_arn(func)
    if isinstance(cluster, str):
        if cluster.startswith("arn:aws:kafka:"):
            source_arn = cluster
        else:
            source_arn = Sub(
                string="arn:aws:kafka:${aws_region}:${aws_account_id}:topic/${cluster_name}/${cluster_uuid}/${topic}",
                data=dict(
                    aws_account_id=AWS_ACCOUNT_ID,
                    aws_region=AWS_REGION,
                    cluster_name=cluster,
                    cluster_uuid=cluster_uuid,
                    topic=topic,
                )
            )
    else:
        source_arn = Sub(
            string="${cluster_arn}/${topic}",
            data=dict(
                cluster_arn=cluster.ref(),
                topic=topic,
            )
        )
    return awslambda.Permission(
        logic_id,
        rp_FunctionName=func_arn,
        rp_Action="lambda:InvokeFunction",
        rp_Principal="kafka.amazonaws.com",
        p_SourceArn=source_arn,
        p_SourceAccount=AWS_ACCOUNT_ID,
    )
