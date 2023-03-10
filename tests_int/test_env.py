# -*- coding: utf-8 -*-

import cottonformation as cf

from cottonformation.tests.boto_ses import bsm
from cottonformation.tests.stacks.iam_stack import (
    make_tpl_1,
    make_tpl_2,
    make_tpl_3,
    make_tpl_4,
)
from aws_cloudformation import better_boto


env = cf.Env(bsm)


def test_case_1():
    stack_name = "cf-int-test"
    bucket = "aws-data-lab-sanhe-for-everything-us-east-1"

    params = [
        cf.ParameterValue(
            key="ProjectName",
            value="cf-int-test"
        )
    ]

    def delete_it():
        env.delete(
            stack_name=stack_name,
            skip_prompt=True,
        )

    def deployment_1():
        env.deploy(
            stack_name=stack_name,
            bucket=bucket,
            template=make_tpl_1(),
            parameters=params,
            skip_prompt=True,
            include_named_iam=True,
        )

    def deployment_2():
        env.deploy(
            stack_name=stack_name,
            bucket=bucket,
            template=make_tpl_2(),
            parameters=params,
            skip_prompt=True,
            include_named_iam=True,
        )

    def inspect_output():
        stack = better_boto.describe_live_stack(bsm=bsm, name=stack_name)
        print(stack.outputs["Policy222Arn"])


    def deployment_3():
        env.deploy(
            stack_name=stack_name,
            bucket=bucket,
            template=make_tpl_3(),
            parameters=params,
            skip_prompt=True,
            include_named_iam=True,
            plan_nested_stack=True,
        )

    def deployment_4():
        env.deploy(
            stack_name=stack_name,
            bucket=bucket,
            template=make_tpl_4(),
            parameters=params,
            skip_prompt=True,
            include_named_iam=True,
            plan_nested_stack=True,
        )

    delete_it()
    deployment_1()
    deployment_2()
    inspect_output()
    deployment_3()
    deployment_4()
    delete_it()


if __name__ == "__main__":
    from cottonformation.tests import run_cov_test

    run_cov_test(__file__, "cottonformation.core.env")
