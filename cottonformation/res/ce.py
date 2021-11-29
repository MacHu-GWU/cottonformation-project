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
class PropAnomalySubscriptionSubscriber(Property):
    """
    AWS Object Type = "AWS::CE::AnomalySubscription.Subscriber"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalysubscription-subscriber.html

    Property Document:
    
    - ``rp_Address``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalysubscription-subscriber.html#cfn-ce-anomalysubscription-subscriber-address
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalysubscription-subscriber.html#cfn-ce-anomalysubscription-subscriber-type
    - ``p_Status``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalysubscription-subscriber.html#cfn-ce-anomalysubscription-subscriber-status
    """
    AWS_OBJECT_TYPE = "AWS::CE::AnomalySubscription.Subscriber"
    
    rp_Address: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Address"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalysubscription-subscriber.html#cfn-ce-anomalysubscription-subscriber-address"""
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalysubscription-subscriber.html#cfn-ce-anomalysubscription-subscriber-type"""
    p_Status: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Status"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalysubscription-subscriber.html#cfn-ce-anomalysubscription-subscriber-status"""


#--- Resource declaration ---

@attr.s
class CostCategory(Resource):
    """
    AWS Object Type = "AWS::CE::CostCategory"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-costcategory.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-costcategory.html#cfn-ce-costcategory-name
    - ``rp_RuleVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-costcategory.html#cfn-ce-costcategory-ruleversion
    - ``rp_Rules``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-costcategory.html#cfn-ce-costcategory-rules
    - ``p_DefaultValue``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-costcategory.html#cfn-ce-costcategory-defaultvalue
    - ``p_SplitChargeRules``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-costcategory.html#cfn-ce-costcategory-splitchargerules
    """
    AWS_OBJECT_TYPE = "AWS::CE::CostCategory"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-costcategory.html#cfn-ce-costcategory-name"""
    rp_RuleVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RuleVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-costcategory.html#cfn-ce-costcategory-ruleversion"""
    rp_Rules: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Rules"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-costcategory.html#cfn-ce-costcategory-rules"""
    p_DefaultValue: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultValue"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-costcategory.html#cfn-ce-costcategory-defaultvalue"""
    p_SplitChargeRules: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SplitChargeRules"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-costcategory.html#cfn-ce-costcategory-splitchargerules"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-costcategory.html#aws-resource-ce-costcategory-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_EffectiveStart(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-costcategory.html#aws-resource-ce-costcategory-return-values"""
        return GetAtt(resource=self, attr_name="EffectiveStart")
    

@attr.s
class AnomalyMonitor(Resource):
    """
    AWS Object Type = "AWS::CE::AnomalyMonitor"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html

    Property Document:
    
    - ``rp_MonitorName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html#cfn-ce-anomalymonitor-monitorname
    - ``rp_MonitorType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html#cfn-ce-anomalymonitor-monitortype
    - ``p_MonitorDimension``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html#cfn-ce-anomalymonitor-monitordimension
    - ``p_MonitorSpecification``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html#cfn-ce-anomalymonitor-monitorspecification
    """
    AWS_OBJECT_TYPE = "AWS::CE::AnomalyMonitor"

    
    rp_MonitorName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "MonitorName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html#cfn-ce-anomalymonitor-monitorname"""
    rp_MonitorType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "MonitorType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html#cfn-ce-anomalymonitor-monitortype"""
    p_MonitorDimension: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MonitorDimension"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html#cfn-ce-anomalymonitor-monitordimension"""
    p_MonitorSpecification: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MonitorSpecification"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html#cfn-ce-anomalymonitor-monitorspecification"""

    
    @property
    def rv_MonitorArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html#aws-resource-ce-anomalymonitor-return-values"""
        return GetAtt(resource=self, attr_name="MonitorArn")
    
    @property
    def rv_CreationDate(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html#aws-resource-ce-anomalymonitor-return-values"""
        return GetAtt(resource=self, attr_name="CreationDate")
    
    @property
    def rv_LastEvaluatedDate(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html#aws-resource-ce-anomalymonitor-return-values"""
        return GetAtt(resource=self, attr_name="LastEvaluatedDate")
    
    @property
    def rv_LastUpdatedDate(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html#aws-resource-ce-anomalymonitor-return-values"""
        return GetAtt(resource=self, attr_name="LastUpdatedDate")
    
    @property
    def rv_DimensionalValueCount(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html#aws-resource-ce-anomalymonitor-return-values"""
        return GetAtt(resource=self, attr_name="DimensionalValueCount")
    

@attr.s
class AnomalySubscription(Resource):
    """
    AWS Object Type = "AWS::CE::AnomalySubscription"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html

    Property Document:
    
    - ``rp_Frequency``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html#cfn-ce-anomalysubscription-frequency
    - ``rp_MonitorArnList``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html#cfn-ce-anomalysubscription-monitorarnlist
    - ``rp_Subscribers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html#cfn-ce-anomalysubscription-subscribers
    - ``rp_SubscriptionName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html#cfn-ce-anomalysubscription-subscriptionname
    - ``rp_Threshold``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html#cfn-ce-anomalysubscription-threshold
    """
    AWS_OBJECT_TYPE = "AWS::CE::AnomalySubscription"

    
    rp_Frequency: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Frequency"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html#cfn-ce-anomalysubscription-frequency"""
    rp_MonitorArnList: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "MonitorArnList"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html#cfn-ce-anomalysubscription-monitorarnlist"""
    rp_Subscribers: typing.List[typing.Union['PropAnomalySubscriptionSubscriber', dict]] = attr.ib(
        default=None,
        converter=PropAnomalySubscriptionSubscriber.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropAnomalySubscriptionSubscriber), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Subscribers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html#cfn-ce-anomalysubscription-subscribers"""
    rp_SubscriptionName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SubscriptionName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html#cfn-ce-anomalysubscription-subscriptionname"""
    rp_Threshold: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "Threshold"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html#cfn-ce-anomalysubscription-threshold"""

    
    @property
    def rv_SubscriptionArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html#aws-resource-ce-anomalysubscription-return-values"""
        return GetAtt(resource=self, attr_name="SubscriptionArn")
    
    @property
    def rv_AccountId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html#aws-resource-ce-anomalysubscription-return-values"""
        return GetAtt(resource=self, attr_name="AccountId")
    
