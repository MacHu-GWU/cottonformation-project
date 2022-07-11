# -*- coding: utf-8 -*-

import pytest
from cottonformation.core.model import (
    Equals,
    Not,
    And,
    Or,
    If,
    Sub,
    Parameter,
    Resource,
    constant,
)
from cottonformation.core.template import Template
from cottonformation.res import s3, ssm


@pytest.fixture
def equal_condition() -> Equals:
    return Equals("ThisEqualToThat", value_one="a", value_two=Sub("${v}", dict(v="b")))


@pytest.fixture
def not_condition(equal_condition) -> Not:
    return Not(
        "ThisNotEqualToThat",
        equal_condition,
    )


@pytest.fixture
def and_condition(equal_condition) -> And:
    return And(
        "AndCondition",
        [equal_condition, equal_condition.ref()],
    )


@pytest.fixture
def or_condition(equal_condition) -> Or:
    return Or(
        "OrCondition",
        [equal_condition, equal_condition.ref()],
    )


@pytest.fixture
def if_condition(equal_condition) -> If:
    return If(
        equal_condition,
        "good",
        Sub("${v}", data=dict(v="bad")),
    )


class TestEqual:
    def test_serialize(self, equal_condition):
        assert equal_condition.serialize() == {
            constant.ConditionFunction.EQUALS: [
                "a",
                {constant.IntrinsicFunction.SUB: ["${v}", {"v": "b"}]},
            ]
        }

        condition = Equals(
            "ThisEqualToThat",
            value_one="a",
            value_two="b",
        )
        assert condition.serialize() == {constant.ConditionFunction.EQUALS: ["a", "b"]}

        p = Parameter("Name", Type=Parameter.TypeEnum.String)
        r = Resource("MyIamRole")
        condition = Equals("ThisEqualToThat", p, r)
        assert condition.serialize() == {
            constant.ConditionFunction.EQUALS: [
                {constant.IntrinsicFunction.REF: "Name"},
                {constant.IntrinsicFunction.REF: "MyIamRole"},
            ]
        }

    def test_eval(self, equal_condition):
        assert equal_condition.eval() == equal_condition.id

    def test_associating_a_condition_in_resource_and_property(self, equal_condition):
        if_condition = If(
            equal_condition,
            "bucket-yes",
            "bucket-no",
        )
        bucket = s3.Bucket(
            "MyBucket",
            p_BucketName=if_condition,
            ra_Condition=equal_condition,
        )
        bucket_json = bucket.serialize()
        assert (
            bucket_json[constant.CloudFomation.Properties]["BucketName"]
            == if_condition.serialize()
        )
        assert (
            bucket_json[constant.ResourceAttribute.CONDITION]
            == equal_condition.serialize()
        )


class TestNot:
    def test_serialize(self, equal_condition, not_condition):
        assert not_condition.serialize() == {
            constant.ConditionFunction.NOT: [equal_condition.serialize()]
        }

    def test_eval(self, not_condition):
        assert not_condition.eval() == not_condition.id


class TestAnd:
    def test_serialize(self, equal_condition, and_condition):
        assert and_condition.serialize() == {
            constant.ConditionFunction.AND: [
                equal_condition.serialize(),
                equal_condition.ref(),
            ]
        }

    def test_eval(self, not_condition):
        assert not_condition.eval() == not_condition.id


class TestOr:
    def test_serialize(self, equal_condition, or_condition):
        assert or_condition.serialize() == {
            constant.ConditionFunction.OR: [
                equal_condition.serialize(),
                equal_condition.ref(),
            ]
        }

    def test_eval(self, or_condition):
        assert or_condition.eval() == or_condition.id


class TestIf:
    def test_serialize(self, equal_condition, if_condition):
        assert if_condition.serialize() == {
            constant.ConditionFunction.IF: [
                equal_condition.id,
                if_condition.value_if_true,
                if_condition.value_if_false.eval(),
            ]
        }

    def test_ref(self, if_condition):
        with pytest.raises(NotImplementedError):
            if_condition.ref()

    def test_eval(self, if_condition):
        assert if_condition.eval() == if_condition.serialize()


class TestTemplateWithCondition:
    def test(self):
        # --- declare template
        tpl = Template()

        param_git_branch = Parameter("GitBranch", Type=Parameter.TypeEnum.String)
        param_stage = Parameter("Stage", Type=Parameter.TypeEnum.String)
        tpl.add(param_git_branch)
        tpl.add(param_stage)

        condition_branch_is_master = Equals(
            "BranchIsMaster", param_git_branch, "master"
        )
        condition_stage_is_prod = Equals("StageIsProd", param_stage, "prod")
        condition_is_master_and_prod = And(
            "IsMasterAndProd",
            [condition_branch_is_master, condition_stage_is_prod],
        )
        condition_if_is_master_branch = If(
            "IfIsMasterBranch", condition_branch_is_master, "Y", "N"
        )

        tpl.add(condition_branch_is_master)
        tpl.add(condition_stage_is_prod)
        tpl.add(condition_is_master_and_prod)

        ssm_param_config = ssm.Parameter(
            "SSMParamConfig",
            rp_Type="Standard",
            rp_Value=Sub(
                '{"GitBranch": "${GitBranch}", "Stage": "${Stage}", "IsMasterBranch": "${IsMasterBranch}"}',
                dict(
                    GitBranch=param_git_branch,
                    Stage=param_stage,
                    IsMasterBranch=condition_if_is_master_branch,
                ),
            ),
            ra_Condition=condition_is_master_and_prod,
        )
        tpl.add(ssm_param_config)

        # --- validate template
        with pytest.raises(NotImplementedError):
            tpl.add(condition_if_is_master_branch)

        assert len(tpl.Conditions) == 3


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
