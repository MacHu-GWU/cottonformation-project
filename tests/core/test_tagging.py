# -*- coding: utf-8 -*-

import pytest

from cottonformation.res import (
    s3,
    xray,
    events,
    rds,
    autoscaling,
    appconfig,
    stepfunctions,
    fms,
    forecast,
    apigatewayv2,
    glue,
    cloudwatch,
)
from cottonformation.core.tagging import (
    get_tag_type_hash_key,
    get_tags_if_list_tag,
    put_tags_if_list_tag,
    get_tags_if_list_json,
    put_tags_if_list_json,
    get_tags_if_map,
    put_tags_if_map,
    get_tags_if_tags,
    put_tags_if_tags,
    get_tags,
    put_tags,
    update_tags,
)


def test_get_tag_type_hash_key():
    assert get_tag_type_hash_key(xray.Group) == "List-None-None-Json"
    assert get_tag_type_hash_key(events.EventBus) == "List-TagEntry-None-None"
    assert get_tag_type_hash_key(rds.DBProxy) == "List-TagFormat-None-None"
    assert (
        get_tag_type_hash_key(autoscaling.AutoScalingGroup)
        == "List-TagProperty-None-None"
    )
    assert get_tag_type_hash_key(appconfig.Application) == "List-Tags-None-None"
    assert (
        get_tag_type_hash_key(stepfunctions.StateMachine) == "List-TagsEntry-None-None"
    )
    assert get_tag_type_hash_key(fms.Policy) == "List-PolicyTag-None-None"

    assert get_tag_type_hash_key(xray.Group) == "List-None-None-Json"
    assert get_tag_type_hash_key(forecast.Dataset) == "List-None-None-Json"
    assert get_tag_type_hash_key(apigatewayv2.Api) == "Map-None-None-String"
    assert get_tag_type_hash_key(glue.DevEndpoint) == "None-None-Json-None"


def test_get_and_put_tags_if_list_tag_entry():
    obj = events.EventBus("", rp_Name="")
    assert get_tags_if_list_tag(obj) == {}

    obj_list = [
        # List-Tag-None-None
        s3.Bucket("", p_Tags=[s3.Tag(p_Key="name", p_Value="alice")]),
        # List-TagEntry-None-None
        events.EventBus(
            "",
            rp_Name="",
            p_Tags=[
                events.PropEventBusTagEntry(rp_Key="name", rp_Value="alice"),
            ],
        ),
        # List-TagFormat-None-None
        rds.DBProxy(
            "",
            rp_DBProxyName="",
            rp_Auth=[],
            rp_EngineFamily="",
            rp_VpcSubnetIds=[
                "",
            ],
            rp_RoleArn="",
            p_Tags=[rds.PropDBProxyTagFormat(p_Key="name", p_Value="alice")],
        ),
        # List-TagProperty-None-None
        autoscaling.AutoScalingGroup(
            "",
            rp_MinSize="",
            rp_MaxSize="",
            p_Tags=[
                autoscaling.PropAutoScalingGroupTagProperty(
                    rp_Key="name",
                    rp_Value="alice",
                    rp_PropagateAtLaunch=True,
                )
            ],
        ),
        # List-Tags-None-None
        appconfig.Application(
            "",
            rp_Name="",
            p_Tags=[appconfig.PropApplicationTags(p_Key="name", p_Value="alice")],
        ),
        # List-TagsEntry-None-None
        stepfunctions.StateMachine(
            "",
            rp_RoleArn="",
            p_Tags=[
                stepfunctions.PropStateMachineTagsEntry(rp_Key="name", rp_Value="alice")
            ],
        ),
        # List-PolicyTag-None-None
        fms.Policy(
            "",
            rp_PolicyName="",
            rp_ExcludeResourceTags=False,
            rp_RemediationEnabled=False,
            rp_SecurityServicePolicyData=fms.PropPolicySecurityServicePolicyData(
                rp_Type="",
            ),
            rp_ResourceType="",
            p_Tags=[fms.PropPolicyPolicyTag(rp_Key="name", rp_Value="alice")],
        ),
    ]
    for obj in obj_list:
        assert get_tags_if_list_tag(obj) == {"name": "alice"}
        assert get_tags(obj) == {"name": "alice"}

        obj.p_Tags = None
        put_tags_if_list_tag(obj, {"name": "bob"})
        assert len(obj.p_Tags) == 1
        assert obj.p_Tags[0].serialize()["Value"] == "bob"

        obj.p_Tags = None
        put_tags(obj, {"name": "bob"})
        assert len(obj.p_Tags) == 1
        assert obj.p_Tags[0].serialize()["Value"] == "bob"


def test_get_put_tags_if_list_json():
    obj_list = [
        xray.Group("", p_Tags=[{"Key": "name", "Value": "alice"}]),
        forecast.Dataset(
            "",
            rp_Domain="",
            rp_Schema=dict(),
            rp_DatasetName="",
            rp_DatasetType="",
            p_Tags=[{"Key": "name", "Value": "alice"}],
        ),
    ]
    for obj in obj_list:
        assert get_tags_if_list_json(obj) == {"name": "alice"}
        assert get_tags(obj) == {"name": "alice"}

        obj.p_Tags = None
        put_tags_if_list_json(obj, {"name": "bob"})
        assert len(obj.p_Tags) == 1
        assert obj.p_Tags[0]["Value"] == "bob"

        obj.p_Tags = None
        put_tags(obj, {"name": "bob"})
        assert len(obj.p_Tags) == 1
        assert obj.p_Tags[0]["Value"] == "bob"


def test_get_put_tags_if_map():
    obj_list = [
        # Map-None-None-String
        apigatewayv2.Api("", p_Tags={"name": "alice"}),
        # None-None-Json-None
        glue.DevEndpoint(
            "",
            rp_RoleArn="",
            p_Tags={"name": "alice"},
        ),
    ]
    for obj in obj_list:
        assert get_tags_if_map(obj) == {"name": "alice"}
        assert get_tags(obj) == {"name": "alice"}

        obj.p_Tags = None
        put_tags_if_map(obj, {"name": "bob"})
        assert len(obj.p_Tags) == 1
        assert obj.p_Tags["name"] == "bob"

        obj.p_Tags = None
        put_tags(obj, {"name": "bob"})
        assert len(obj.p_Tags) == 1
        assert obj.p_Tags["name"] == "bob"


def test_get_put_tags_if_tags():
    obj_list = [
        # Tags-None-None-None
        cloudwatch.InsightRule(
            "",
            rp_RuleName="",
            rp_RuleBody="",
            rp_RuleState="",
            p_Tags=cloudwatch.PropInsightRuleTags(),
        ),
    ]
    for obj in obj_list:
        assert get_tags_if_tags(obj) == {}
        assert get_tags(obj) == {}

        obj.p_Tags = None
        put_tags_if_tags(obj, {"name": "bob"})
        put_tags(obj, {"name": "bob"})


def test_update_tags():
    existing_tags = [s3.Tag(p_Key="a", p_Value="1"), s3.Tag(p_Key="b", p_Value="2")]
    to_update_tags = {"c": "3", "b": "22"}

    obj = s3.Bucket("", p_Tags=existing_tags)
    before, after = update_tags(obj, to_update_tags, mode_skip=True)
    assert get_tags(obj) == {"a": "1", "b": "2", "c": "3"}
    assert before == {"a": "1", "b": "2"}
    assert after == {"a": "1", "b": "2", "c": "3"}

    obj = s3.Bucket("", p_Tags=existing_tags)
    before, after = update_tags(obj, to_update_tags, mode_overwrite=True)
    assert get_tags(obj) == {"a": "1", "b": "22", "c": "3"}
    assert before == {"a": "1", "b": "2"}
    assert after == {"a": "1", "b": "22", "c": "3"}

    obj = s3.Bucket("", p_Tags=existing_tags)
    with pytest.raises(KeyError):
        update_tags(obj, to_update_tags)

    with pytest.raises(ValueError):
        update_tags(obj, to_update_tags, mode_skip=True, mode_overwrite=True)

    before, after = update_tags(obj, {})
    assert before == {"a": "1", "b": "2"}
    assert after == {"a": "1", "b": "2"}


if __name__ == "__main__":
    from cottonformation.tests import run_cov_test

    run_cov_test(__file__, "cottonformation.core.tagging")
