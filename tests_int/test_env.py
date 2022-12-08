# -*- coding: utf-8 -*-

import cottonformation as cf
from cottonformation.tests.boto_ses import bsm
from cottonformation.tests.stacks.iam_stack import (
    make_tpl_1,
    make_tpl_2,
    make_tpl_3,
    make_tpl_4,
)

env = cf.Env(bsm)


def test_case_1():
    stack_name = "cottonformation-int-test-env-module"
    bucket = "aws-data-lab-sanhe-for-everything-us-east-1"

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
            skip_prompt=True,
            include_named_iam=True,
        )

    def deployment_2():
        env.deploy(
            stack_name=stack_name,
            bucket=bucket,
            template=make_tpl_2(),
            skip_prompt=True,
            include_named_iam=True,
        )

    def deployment_3():
        env.deploy(
            stack_name=stack_name,
            bucket=bucket,
            template=make_tpl_3(),
            skip_prompt=True,
            include_named_iam=True,
        )

    def validate_1():
        env.validate(
            template=make_tpl_3(),
            bucket=bucket,
        )

    def deployment_4():
        env.deploy(
            stack_name=stack_name,
            bucket=bucket,
            template=make_tpl_4(),
            skip_prompt=True,
            include_named_iam=True,
        )

    # delete_it()
    # deployment_1()
    # deployment_2()
    # deployment_3()
    validate_1()
    # deployment_4()
    # delete_it()


if __name__ == "__main__":
    from cottonformation.tests import run_cov_test

    run_cov_test(__file__, "cottonformation.core.env")
