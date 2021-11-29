# -*- coding: utf-8 -*-

"""
This module
"""

import attr
import typing

from ..core.model import (
    Property, Resource, Tag, GetAtt, TypeHint, TypeCheck,
)
from ..core.constant import AttrMeta

#--- Property declaration ---

@attr.s
class PropClusterClusterEndpoint(Property):
    """
    AWS Object Type = "AWS::Route53RecoveryControl::Cluster.ClusterEndpoint"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-cluster-clusterendpoint.html

    Property Document:
    
    - ``p_Endpoint``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-cluster-clusterendpoint.html#cfn-route53recoverycontrol-cluster-clusterendpoint-endpoint
    - ``p_Region``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-cluster-clusterendpoint.html#cfn-route53recoverycontrol-cluster-clusterendpoint-region
    """
    AWS_OBJECT_TYPE = "AWS::Route53RecoveryControl::Cluster.ClusterEndpoint"
    
    p_Endpoint: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Endpoint"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-cluster-clusterendpoint.html#cfn-route53recoverycontrol-cluster-clusterendpoint-endpoint"""
    p_Region: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Region"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-cluster-clusterendpoint.html#cfn-route53recoverycontrol-cluster-clusterendpoint-region"""

@attr.s
class PropSafetyRuleRuleConfig(Property):
    """
    AWS Object Type = "AWS::Route53RecoveryControl::SafetyRule.RuleConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-ruleconfig.html

    Property Document:
    
    - ``rp_Inverted``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-ruleconfig.html#cfn-route53recoverycontrol-safetyrule-ruleconfig-inverted
    - ``rp_Threshold``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-ruleconfig.html#cfn-route53recoverycontrol-safetyrule-ruleconfig-threshold
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-ruleconfig.html#cfn-route53recoverycontrol-safetyrule-ruleconfig-type
    """
    AWS_OBJECT_TYPE = "AWS::Route53RecoveryControl::SafetyRule.RuleConfig"
    
    rp_Inverted: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Inverted"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-ruleconfig.html#cfn-route53recoverycontrol-safetyrule-ruleconfig-inverted"""
    rp_Threshold: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Threshold"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-ruleconfig.html#cfn-route53recoverycontrol-safetyrule-ruleconfig-threshold"""
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-ruleconfig.html#cfn-route53recoverycontrol-safetyrule-ruleconfig-type"""

@attr.s
class PropSafetyRuleAssertionRule(Property):
    """
    AWS Object Type = "AWS::Route53RecoveryControl::SafetyRule.AssertionRule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-assertionrule.html

    Property Document:
    
    - ``rp_AssertedControls``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-assertionrule.html#cfn-route53recoverycontrol-safetyrule-assertionrule-assertedcontrols
    - ``rp_WaitPeriodMs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-assertionrule.html#cfn-route53recoverycontrol-safetyrule-assertionrule-waitperiodms
    """
    AWS_OBJECT_TYPE = "AWS::Route53RecoveryControl::SafetyRule.AssertionRule"
    
    rp_AssertedControls: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "AssertedControls"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-assertionrule.html#cfn-route53recoverycontrol-safetyrule-assertionrule-assertedcontrols"""
    rp_WaitPeriodMs: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "WaitPeriodMs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-assertionrule.html#cfn-route53recoverycontrol-safetyrule-assertionrule-waitperiodms"""

@attr.s
class PropSafetyRuleGatingRule(Property):
    """
    AWS Object Type = "AWS::Route53RecoveryControl::SafetyRule.GatingRule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-gatingrule.html

    Property Document:
    
    - ``rp_GatingControls``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-gatingrule.html#cfn-route53recoverycontrol-safetyrule-gatingrule-gatingcontrols
    - ``rp_TargetControls``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-gatingrule.html#cfn-route53recoverycontrol-safetyrule-gatingrule-targetcontrols
    - ``rp_WaitPeriodMs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-gatingrule.html#cfn-route53recoverycontrol-safetyrule-gatingrule-waitperiodms
    """
    AWS_OBJECT_TYPE = "AWS::Route53RecoveryControl::SafetyRule.GatingRule"
    
    rp_GatingControls: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "GatingControls"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-gatingrule.html#cfn-route53recoverycontrol-safetyrule-gatingrule-gatingcontrols"""
    rp_TargetControls: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "TargetControls"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-gatingrule.html#cfn-route53recoverycontrol-safetyrule-gatingrule-targetcontrols"""
    rp_WaitPeriodMs: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "WaitPeriodMs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-gatingrule.html#cfn-route53recoverycontrol-safetyrule-gatingrule-waitperiodms"""


#--- Resource declaration ---

@attr.s
class SafetyRule(Resource):
    """
    AWS Object Type = "AWS::Route53RecoveryControl::SafetyRule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html

    Property Document:
    
    - ``rp_ControlPanelArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-controlpanelarn
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-name
    - ``rp_RuleConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-ruleconfig
    - ``p_AssertionRule``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-assertionrule
    - ``p_GatingRule``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-gatingrule
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-tags
    """
    AWS_OBJECT_TYPE = "AWS::Route53RecoveryControl::SafetyRule"

    
    rp_ControlPanelArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ControlPanelArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-controlpanelarn"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-name"""
    rp_RuleConfig: typing.Union['PropSafetyRuleRuleConfig', dict] = attr.ib(
        default=None,
        converter=PropSafetyRuleRuleConfig.from_dict,
        validator=attr.validators.instance_of(PropSafetyRuleRuleConfig),
        metadata={AttrMeta.PROPERTY_NAME: "RuleConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-ruleconfig"""
    p_AssertionRule: typing.Union['PropSafetyRuleAssertionRule', dict] = attr.ib(
        default=None,
        converter=PropSafetyRuleAssertionRule.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropSafetyRuleAssertionRule)),
        metadata={AttrMeta.PROPERTY_NAME: "AssertionRule"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-assertionrule"""
    p_GatingRule: typing.Union['PropSafetyRuleGatingRule', dict] = attr.ib(
        default=None,
        converter=PropSafetyRuleGatingRule.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropSafetyRuleGatingRule)),
        metadata={AttrMeta.PROPERTY_NAME: "GatingRule"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-gatingrule"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#cfn-route53recoverycontrol-safetyrule-tags"""

    
    @property
    def rv_SafetyRuleArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#aws-resource-route53recoverycontrol-safetyrule-return-values"""
        return GetAtt(resource=self, attr_name="SafetyRuleArn")
    
    @property
    def rv_Status(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html#aws-resource-route53recoverycontrol-safetyrule-return-values"""
        return GetAtt(resource=self, attr_name="Status")
    

@attr.s
class Cluster(Resource):
    """
    AWS Object Type = "AWS::Route53RecoveryControl::Cluster"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-cluster.html

    Property Document:
    
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-cluster.html#cfn-route53recoverycontrol-cluster-name
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-cluster.html#cfn-route53recoverycontrol-cluster-tags
    """
    AWS_OBJECT_TYPE = "AWS::Route53RecoveryControl::Cluster"

    
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-cluster.html#cfn-route53recoverycontrol-cluster-name"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-cluster.html#cfn-route53recoverycontrol-cluster-tags"""

    
    @property
    def rv_ClusterArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-cluster.html#aws-resource-route53recoverycontrol-cluster-return-values"""
        return GetAtt(resource=self, attr_name="ClusterArn")
    
    @property
    def rv_Status(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-cluster.html#aws-resource-route53recoverycontrol-cluster-return-values"""
        return GetAtt(resource=self, attr_name="Status")
    
    @property
    def rv_ClusterEndpoints(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-cluster.html#aws-resource-route53recoverycontrol-cluster-return-values"""
        return GetAtt(resource=self, attr_name="ClusterEndpoints")
    

@attr.s
class RoutingControl(Resource):
    """
    AWS Object Type = "AWS::Route53RecoveryControl::RoutingControl"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-routingcontrol.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-routingcontrol.html#cfn-route53recoverycontrol-routingcontrol-name
    - ``p_ClusterArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-routingcontrol.html#cfn-route53recoverycontrol-routingcontrol-clusterarn
    - ``p_ControlPanelArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-routingcontrol.html#cfn-route53recoverycontrol-routingcontrol-controlpanelarn
    """
    AWS_OBJECT_TYPE = "AWS::Route53RecoveryControl::RoutingControl"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-routingcontrol.html#cfn-route53recoverycontrol-routingcontrol-name"""
    p_ClusterArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ClusterArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-routingcontrol.html#cfn-route53recoverycontrol-routingcontrol-clusterarn"""
    p_ControlPanelArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ControlPanelArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-routingcontrol.html#cfn-route53recoverycontrol-routingcontrol-controlpanelarn"""

    
    @property
    def rv_RoutingControlArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-routingcontrol.html#aws-resource-route53recoverycontrol-routingcontrol-return-values"""
        return GetAtt(resource=self, attr_name="RoutingControlArn")
    
    @property
    def rv_Status(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-routingcontrol.html#aws-resource-route53recoverycontrol-routingcontrol-return-values"""
        return GetAtt(resource=self, attr_name="Status")
    

@attr.s
class ControlPanel(Resource):
    """
    AWS Object Type = "AWS::Route53RecoveryControl::ControlPanel"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html#cfn-route53recoverycontrol-controlpanel-name
    - ``p_ClusterArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html#cfn-route53recoverycontrol-controlpanel-clusterarn
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html#cfn-route53recoverycontrol-controlpanel-tags
    """
    AWS_OBJECT_TYPE = "AWS::Route53RecoveryControl::ControlPanel"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html#cfn-route53recoverycontrol-controlpanel-name"""
    p_ClusterArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ClusterArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html#cfn-route53recoverycontrol-controlpanel-clusterarn"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html#cfn-route53recoverycontrol-controlpanel-tags"""

    
    @property
    def rv_ControlPanelArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html#aws-resource-route53recoverycontrol-controlpanel-return-values"""
        return GetAtt(resource=self, attr_name="ControlPanelArn")
    
    @property
    def rv_Status(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html#aws-resource-route53recoverycontrol-controlpanel-return-values"""
        return GetAtt(resource=self, attr_name="Status")
    
    @property
    def rv_DefaultControlPanel(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html#aws-resource-route53recoverycontrol-controlpanel-return-values"""
        return GetAtt(resource=self, attr_name="DefaultControlPanel")
    
    @property
    def rv_RoutingControlCount(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html#aws-resource-route53recoverycontrol-controlpanel-return-values"""
        return GetAtt(resource=self, attr_name="RoutingControlCount")
    
