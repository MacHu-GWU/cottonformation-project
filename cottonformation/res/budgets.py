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
class PropBudgetsActionIamActionDefinition(Property):
    """
    AWS Object Type = "AWS::Budgets::BudgetsAction.IamActionDefinition"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-iamactiondefinition.html

    Property Document:
    
    - ``rp_PolicyArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-iamactiondefinition.html#cfn-budgets-budgetsaction-iamactiondefinition-policyarn
    - ``p_Groups``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-iamactiondefinition.html#cfn-budgets-budgetsaction-iamactiondefinition-groups
    - ``p_Roles``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-iamactiondefinition.html#cfn-budgets-budgetsaction-iamactiondefinition-roles
    - ``p_Users``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-iamactiondefinition.html#cfn-budgets-budgetsaction-iamactiondefinition-users
    """
    AWS_OBJECT_TYPE = "AWS::Budgets::BudgetsAction.IamActionDefinition"
    
    rp_PolicyArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PolicyArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-iamactiondefinition.html#cfn-budgets-budgetsaction-iamactiondefinition-policyarn"""
    p_Groups: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Groups"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-iamactiondefinition.html#cfn-budgets-budgetsaction-iamactiondefinition-groups"""
    p_Roles: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Roles"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-iamactiondefinition.html#cfn-budgets-budgetsaction-iamactiondefinition-roles"""
    p_Users: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Users"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-iamactiondefinition.html#cfn-budgets-budgetsaction-iamactiondefinition-users"""

@attr.s
class PropBudgetSubscriber(Property):
    """
    AWS Object Type = "AWS::Budgets::Budget.Subscriber"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-subscriber.html

    Property Document:
    
    - ``rp_Address``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-subscriber.html#cfn-budgets-budget-subscriber-address
    - ``rp_SubscriptionType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-subscriber.html#cfn-budgets-budget-subscriber-subscriptiontype
    """
    AWS_OBJECT_TYPE = "AWS::Budgets::Budget.Subscriber"
    
    rp_Address: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Address"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-subscriber.html#cfn-budgets-budget-subscriber-address"""
    rp_SubscriptionType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SubscriptionType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-subscriber.html#cfn-budgets-budget-subscriber-subscriptiontype"""

@attr.s
class PropBudgetTimePeriod(Property):
    """
    AWS Object Type = "AWS::Budgets::Budget.TimePeriod"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-timeperiod.html

    Property Document:
    
    - ``p_End``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-timeperiod.html#cfn-budgets-budget-timeperiod-end
    - ``p_Start``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-timeperiod.html#cfn-budgets-budget-timeperiod-start
    """
    AWS_OBJECT_TYPE = "AWS::Budgets::Budget.TimePeriod"
    
    p_End: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "End"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-timeperiod.html#cfn-budgets-budget-timeperiod-end"""
    p_Start: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Start"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-timeperiod.html#cfn-budgets-budget-timeperiod-start"""

@attr.s
class PropBudgetsActionScpActionDefinition(Property):
    """
    AWS Object Type = "AWS::Budgets::BudgetsAction.ScpActionDefinition"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-scpactiondefinition.html

    Property Document:
    
    - ``rp_PolicyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-scpactiondefinition.html#cfn-budgets-budgetsaction-scpactiondefinition-policyid
    - ``rp_TargetIds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-scpactiondefinition.html#cfn-budgets-budgetsaction-scpactiondefinition-targetids
    """
    AWS_OBJECT_TYPE = "AWS::Budgets::BudgetsAction.ScpActionDefinition"
    
    rp_PolicyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PolicyId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-scpactiondefinition.html#cfn-budgets-budgetsaction-scpactiondefinition-policyid"""
    rp_TargetIds: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "TargetIds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-scpactiondefinition.html#cfn-budgets-budgetsaction-scpactiondefinition-targetids"""

@attr.s
class PropBudgetsActionSsmActionDefinition(Property):
    """
    AWS Object Type = "AWS::Budgets::BudgetsAction.SsmActionDefinition"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-ssmactiondefinition.html

    Property Document:
    
    - ``rp_InstanceIds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-ssmactiondefinition.html#cfn-budgets-budgetsaction-ssmactiondefinition-instanceids
    - ``rp_Region``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-ssmactiondefinition.html#cfn-budgets-budgetsaction-ssmactiondefinition-region
    - ``rp_Subtype``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-ssmactiondefinition.html#cfn-budgets-budgetsaction-ssmactiondefinition-subtype
    """
    AWS_OBJECT_TYPE = "AWS::Budgets::BudgetsAction.SsmActionDefinition"
    
    rp_InstanceIds: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "InstanceIds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-ssmactiondefinition.html#cfn-budgets-budgetsaction-ssmactiondefinition-instanceids"""
    rp_Region: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Region"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-ssmactiondefinition.html#cfn-budgets-budgetsaction-ssmactiondefinition-region"""
    rp_Subtype: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Subtype"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-ssmactiondefinition.html#cfn-budgets-budgetsaction-ssmactiondefinition-subtype"""

@attr.s
class PropBudgetsActionActionThreshold(Property):
    """
    AWS Object Type = "AWS::Budgets::BudgetsAction.ActionThreshold"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-actionthreshold.html

    Property Document:
    
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-actionthreshold.html#cfn-budgets-budgetsaction-actionthreshold-type
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-actionthreshold.html#cfn-budgets-budgetsaction-actionthreshold-value
    """
    AWS_OBJECT_TYPE = "AWS::Budgets::BudgetsAction.ActionThreshold"
    
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-actionthreshold.html#cfn-budgets-budgetsaction-actionthreshold-type"""
    rp_Value: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-actionthreshold.html#cfn-budgets-budgetsaction-actionthreshold-value"""

@attr.s
class PropBudgetCostTypes(Property):
    """
    AWS Object Type = "AWS::Budgets::Budget.CostTypes"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html

    Property Document:
    
    - ``p_IncludeCredit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includecredit
    - ``p_IncludeDiscount``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includediscount
    - ``p_IncludeOtherSubscription``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includeothersubscription
    - ``p_IncludeRecurring``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includerecurring
    - ``p_IncludeRefund``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includerefund
    - ``p_IncludeSubscription``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includesubscription
    - ``p_IncludeSupport``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includesupport
    - ``p_IncludeTax``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includetax
    - ``p_IncludeUpfront``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includeupfront
    - ``p_UseAmortized``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-useamortized
    - ``p_UseBlended``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-useblended
    """
    AWS_OBJECT_TYPE = "AWS::Budgets::Budget.CostTypes"
    
    p_IncludeCredit: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IncludeCredit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includecredit"""
    p_IncludeDiscount: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IncludeDiscount"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includediscount"""
    p_IncludeOtherSubscription: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IncludeOtherSubscription"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includeothersubscription"""
    p_IncludeRecurring: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IncludeRecurring"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includerecurring"""
    p_IncludeRefund: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IncludeRefund"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includerefund"""
    p_IncludeSubscription: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IncludeSubscription"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includesubscription"""
    p_IncludeSupport: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IncludeSupport"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includesupport"""
    p_IncludeTax: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IncludeTax"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includetax"""
    p_IncludeUpfront: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IncludeUpfront"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includeupfront"""
    p_UseAmortized: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "UseAmortized"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-useamortized"""
    p_UseBlended: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "UseBlended"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-useblended"""

@attr.s
class PropBudgetNotification(Property):
    """
    AWS Object Type = "AWS::Budgets::Budget.Notification"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html

    Property Document:
    
    - ``rp_ComparisonOperator``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html#cfn-budgets-budget-notification-comparisonoperator
    - ``rp_NotificationType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html#cfn-budgets-budget-notification-notificationtype
    - ``rp_Threshold``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html#cfn-budgets-budget-notification-threshold
    - ``p_ThresholdType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html#cfn-budgets-budget-notification-thresholdtype
    """
    AWS_OBJECT_TYPE = "AWS::Budgets::Budget.Notification"
    
    rp_ComparisonOperator: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ComparisonOperator"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html#cfn-budgets-budget-notification-comparisonoperator"""
    rp_NotificationType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "NotificationType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html#cfn-budgets-budget-notification-notificationtype"""
    rp_Threshold: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "Threshold"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html#cfn-budgets-budget-notification-threshold"""
    p_ThresholdType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ThresholdType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html#cfn-budgets-budget-notification-thresholdtype"""

@attr.s
class PropBudgetsActionSubscriber(Property):
    """
    AWS Object Type = "AWS::Budgets::BudgetsAction.Subscriber"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-subscriber.html

    Property Document:
    
    - ``rp_Address``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-subscriber.html#cfn-budgets-budgetsaction-subscriber-address
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-subscriber.html#cfn-budgets-budgetsaction-subscriber-type
    """
    AWS_OBJECT_TYPE = "AWS::Budgets::BudgetsAction.Subscriber"
    
    rp_Address: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Address"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-subscriber.html#cfn-budgets-budgetsaction-subscriber-address"""
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-subscriber.html#cfn-budgets-budgetsaction-subscriber-type"""

@attr.s
class PropBudgetSpend(Property):
    """
    AWS Object Type = "AWS::Budgets::Budget.Spend"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-spend.html

    Property Document:
    
    - ``rp_Amount``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-spend.html#cfn-budgets-budget-spend-amount
    - ``rp_Unit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-spend.html#cfn-budgets-budget-spend-unit
    """
    AWS_OBJECT_TYPE = "AWS::Budgets::Budget.Spend"
    
    rp_Amount: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "Amount"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-spend.html#cfn-budgets-budget-spend-amount"""
    rp_Unit: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Unit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-spend.html#cfn-budgets-budget-spend-unit"""

@attr.s
class PropBudgetBudgetData(Property):
    """
    AWS Object Type = "AWS::Budgets::Budget.BudgetData"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html

    Property Document:
    
    - ``rp_BudgetType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-budgettype
    - ``rp_TimeUnit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-timeunit
    - ``p_BudgetLimit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-budgetlimit
    - ``p_BudgetName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-budgetname
    - ``p_CostFilters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-costfilters
    - ``p_CostTypes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-costtypes
    - ``p_PlannedBudgetLimits``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-plannedbudgetlimits
    - ``p_TimePeriod``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-timeperiod
    """
    AWS_OBJECT_TYPE = "AWS::Budgets::Budget.BudgetData"
    
    rp_BudgetType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "BudgetType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-budgettype"""
    rp_TimeUnit: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TimeUnit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-timeunit"""
    p_BudgetLimit: typing.Union['PropBudgetSpend', dict] = attr.ib(
        default=None,
        converter=PropBudgetSpend.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBudgetSpend)),
        metadata={AttrMeta.PROPERTY_NAME: "BudgetLimit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-budgetlimit"""
    p_BudgetName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BudgetName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-budgetname"""
    p_CostFilters: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "CostFilters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-costfilters"""
    p_CostTypes: typing.Union['PropBudgetCostTypes', dict] = attr.ib(
        default=None,
        converter=PropBudgetCostTypes.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBudgetCostTypes)),
        metadata={AttrMeta.PROPERTY_NAME: "CostTypes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-costtypes"""
    p_PlannedBudgetLimits: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "PlannedBudgetLimits"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-plannedbudgetlimits"""
    p_TimePeriod: typing.Union['PropBudgetTimePeriod', dict] = attr.ib(
        default=None,
        converter=PropBudgetTimePeriod.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBudgetTimePeriod)),
        metadata={AttrMeta.PROPERTY_NAME: "TimePeriod"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-timeperiod"""

@attr.s
class PropBudgetsActionDefinition(Property):
    """
    AWS Object Type = "AWS::Budgets::BudgetsAction.Definition"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-definition.html

    Property Document:
    
    - ``p_IamActionDefinition``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-definition.html#cfn-budgets-budgetsaction-definition-iamactiondefinition
    - ``p_ScpActionDefinition``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-definition.html#cfn-budgets-budgetsaction-definition-scpactiondefinition
    - ``p_SsmActionDefinition``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-definition.html#cfn-budgets-budgetsaction-definition-ssmactiondefinition
    """
    AWS_OBJECT_TYPE = "AWS::Budgets::BudgetsAction.Definition"
    
    p_IamActionDefinition: typing.Union['PropBudgetsActionIamActionDefinition', dict] = attr.ib(
        default=None,
        converter=PropBudgetsActionIamActionDefinition.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBudgetsActionIamActionDefinition)),
        metadata={AttrMeta.PROPERTY_NAME: "IamActionDefinition"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-definition.html#cfn-budgets-budgetsaction-definition-iamactiondefinition"""
    p_ScpActionDefinition: typing.Union['PropBudgetsActionScpActionDefinition', dict] = attr.ib(
        default=None,
        converter=PropBudgetsActionScpActionDefinition.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBudgetsActionScpActionDefinition)),
        metadata={AttrMeta.PROPERTY_NAME: "ScpActionDefinition"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-definition.html#cfn-budgets-budgetsaction-definition-scpactiondefinition"""
    p_SsmActionDefinition: typing.Union['PropBudgetsActionSsmActionDefinition', dict] = attr.ib(
        default=None,
        converter=PropBudgetsActionSsmActionDefinition.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBudgetsActionSsmActionDefinition)),
        metadata={AttrMeta.PROPERTY_NAME: "SsmActionDefinition"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-definition.html#cfn-budgets-budgetsaction-definition-ssmactiondefinition"""

@attr.s
class PropBudgetNotificationWithSubscribers(Property):
    """
    AWS Object Type = "AWS::Budgets::Budget.NotificationWithSubscribers"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notificationwithsubscribers.html

    Property Document:
    
    - ``rp_Notification``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notificationwithsubscribers.html#cfn-budgets-budget-notificationwithsubscribers-notification
    - ``rp_Subscribers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notificationwithsubscribers.html#cfn-budgets-budget-notificationwithsubscribers-subscribers
    """
    AWS_OBJECT_TYPE = "AWS::Budgets::Budget.NotificationWithSubscribers"
    
    rp_Notification: typing.Union['PropBudgetNotification', dict] = attr.ib(
        default=None,
        converter=PropBudgetNotification.from_dict,
        validator=attr.validators.instance_of(PropBudgetNotification),
        metadata={AttrMeta.PROPERTY_NAME: "Notification"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notificationwithsubscribers.html#cfn-budgets-budget-notificationwithsubscribers-notification"""
    rp_Subscribers: typing.List[typing.Union['PropBudgetSubscriber', dict]] = attr.ib(
        default=None,
        converter=PropBudgetSubscriber.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBudgetSubscriber), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Subscribers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notificationwithsubscribers.html#cfn-budgets-budget-notificationwithsubscribers-subscribers"""


#--- Resource declaration ---

@attr.s
class BudgetsAction(Resource):
    """
    AWS Object Type = "AWS::Budgets::BudgetsAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html

    Property Document:
    
    - ``rp_ActionThreshold``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-actionthreshold
    - ``rp_ActionType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-actiontype
    - ``rp_BudgetName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-budgetname
    - ``rp_Definition``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-definition
    - ``rp_ExecutionRoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-executionrolearn
    - ``rp_NotificationType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-notificationtype
    - ``rp_Subscribers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-subscribers
    - ``p_ApprovalModel``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-approvalmodel
    """
    AWS_OBJECT_TYPE = "AWS::Budgets::BudgetsAction"

    
    rp_ActionThreshold: typing.Union['PropBudgetsActionActionThreshold', dict] = attr.ib(
        default=None,
        converter=PropBudgetsActionActionThreshold.from_dict,
        validator=attr.validators.instance_of(PropBudgetsActionActionThreshold),
        metadata={AttrMeta.PROPERTY_NAME: "ActionThreshold"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-actionthreshold"""
    rp_ActionType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ActionType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-actiontype"""
    rp_BudgetName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "BudgetName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-budgetname"""
    rp_Definition: typing.Union['PropBudgetsActionDefinition', dict] = attr.ib(
        default=None,
        converter=PropBudgetsActionDefinition.from_dict,
        validator=attr.validators.instance_of(PropBudgetsActionDefinition),
        metadata={AttrMeta.PROPERTY_NAME: "Definition"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-definition"""
    rp_ExecutionRoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ExecutionRoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-executionrolearn"""
    rp_NotificationType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "NotificationType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-notificationtype"""
    rp_Subscribers: typing.List[typing.Union['PropBudgetsActionSubscriber', dict]] = attr.ib(
        default=None,
        converter=PropBudgetsActionSubscriber.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBudgetsActionSubscriber), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Subscribers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-subscribers"""
    p_ApprovalModel: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ApprovalModel"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-approvalmodel"""

    
    @property
    def rv_ActionId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#aws-resource-budgets-budgetsaction-return-values"""
        return GetAtt(resource=self, attr_name="ActionId")
    

@attr.s
class Budget(Resource):
    """
    AWS Object Type = "AWS::Budgets::Budget"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html

    Property Document:
    
    - ``rp_Budget``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html#cfn-budgets-budget-budget
    - ``p_NotificationsWithSubscribers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html#cfn-budgets-budget-notificationswithsubscribers
    """
    AWS_OBJECT_TYPE = "AWS::Budgets::Budget"

    
    rp_Budget: typing.Union['PropBudgetBudgetData', dict] = attr.ib(
        default=None,
        converter=PropBudgetBudgetData.from_dict,
        validator=attr.validators.instance_of(PropBudgetBudgetData),
        metadata={AttrMeta.PROPERTY_NAME: "Budget"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html#cfn-budgets-budget-budget"""
    p_NotificationsWithSubscribers: typing.List[typing.Union['PropBudgetNotificationWithSubscribers', dict]] = attr.ib(
        default=None,
        converter=PropBudgetNotificationWithSubscribers.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBudgetNotificationWithSubscribers), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "NotificationsWithSubscribers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html#cfn-budgets-budget-notificationswithsubscribers"""

    
