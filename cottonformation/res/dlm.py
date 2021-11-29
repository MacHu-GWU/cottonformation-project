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
class PropLifecyclePolicyFastRestoreRule(Property):
    """
    AWS Object Type = "AWS::DLM::LifecyclePolicy.FastRestoreRule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-fastrestorerule.html

    Property Document:
    
    - ``p_AvailabilityZones``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-fastrestorerule.html#cfn-dlm-lifecyclepolicy-fastrestorerule-availabilityzones
    - ``p_Count``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-fastrestorerule.html#cfn-dlm-lifecyclepolicy-fastrestorerule-count
    - ``p_Interval``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-fastrestorerule.html#cfn-dlm-lifecyclepolicy-fastrestorerule-interval
    - ``p_IntervalUnit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-fastrestorerule.html#cfn-dlm-lifecyclepolicy-fastrestorerule-intervalunit
    """
    AWS_OBJECT_TYPE = "AWS::DLM::LifecyclePolicy.FastRestoreRule"
    
    p_AvailabilityZones: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AvailabilityZones"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-fastrestorerule.html#cfn-dlm-lifecyclepolicy-fastrestorerule-availabilityzones"""
    p_Count: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Count"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-fastrestorerule.html#cfn-dlm-lifecyclepolicy-fastrestorerule-count"""
    p_Interval: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Interval"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-fastrestorerule.html#cfn-dlm-lifecyclepolicy-fastrestorerule-interval"""
    p_IntervalUnit: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "IntervalUnit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-fastrestorerule.html#cfn-dlm-lifecyclepolicy-fastrestorerule-intervalunit"""

@attr.s
class PropLifecyclePolicyEventParameters(Property):
    """
    AWS Object Type = "AWS::DLM::LifecyclePolicy.EventParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventparameters.html

    Property Document:
    
    - ``rp_EventType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventparameters.html#cfn-dlm-lifecyclepolicy-eventparameters-eventtype
    - ``rp_SnapshotOwner``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventparameters.html#cfn-dlm-lifecyclepolicy-eventparameters-snapshotowner
    - ``p_DescriptionRegex``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventparameters.html#cfn-dlm-lifecyclepolicy-eventparameters-descriptionregex
    """
    AWS_OBJECT_TYPE = "AWS::DLM::LifecyclePolicy.EventParameters"
    
    rp_EventType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "EventType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventparameters.html#cfn-dlm-lifecyclepolicy-eventparameters-eventtype"""
    rp_SnapshotOwner: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "SnapshotOwner"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventparameters.html#cfn-dlm-lifecyclepolicy-eventparameters-snapshotowner"""
    p_DescriptionRegex: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DescriptionRegex"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventparameters.html#cfn-dlm-lifecyclepolicy-eventparameters-descriptionregex"""

@attr.s
class PropLifecyclePolicyCreateRule(Property):
    """
    AWS Object Type = "AWS::DLM::LifecyclePolicy.CreateRule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html

    Property Document:
    
    - ``p_CronExpression``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html#cfn-dlm-lifecyclepolicy-createrule-cronexpression
    - ``p_Interval``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html#cfn-dlm-lifecyclepolicy-createrule-interval
    - ``p_IntervalUnit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html#cfn-dlm-lifecyclepolicy-createrule-intervalunit
    - ``p_Location``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html#cfn-dlm-lifecyclepolicy-createrule-location
    - ``p_Times``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html#cfn-dlm-lifecyclepolicy-createrule-times
    """
    AWS_OBJECT_TYPE = "AWS::DLM::LifecyclePolicy.CreateRule"
    
    p_CronExpression: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CronExpression"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html#cfn-dlm-lifecyclepolicy-createrule-cronexpression"""
    p_Interval: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Interval"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html#cfn-dlm-lifecyclepolicy-createrule-interval"""
    p_IntervalUnit: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "IntervalUnit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html#cfn-dlm-lifecyclepolicy-createrule-intervalunit"""
    p_Location: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Location"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html#cfn-dlm-lifecyclepolicy-createrule-location"""
    p_Times: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Times"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html#cfn-dlm-lifecyclepolicy-createrule-times"""

@attr.s
class PropLifecyclePolicyRetainRule(Property):
    """
    AWS Object Type = "AWS::DLM::LifecyclePolicy.RetainRule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-retainrule.html

    Property Document:
    
    - ``p_Count``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-retainrule.html#cfn-dlm-lifecyclepolicy-retainrule-count
    - ``p_Interval``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-retainrule.html#cfn-dlm-lifecyclepolicy-retainrule-interval
    - ``p_IntervalUnit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-retainrule.html#cfn-dlm-lifecyclepolicy-retainrule-intervalunit
    """
    AWS_OBJECT_TYPE = "AWS::DLM::LifecyclePolicy.RetainRule"
    
    p_Count: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Count"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-retainrule.html#cfn-dlm-lifecyclepolicy-retainrule-count"""
    p_Interval: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Interval"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-retainrule.html#cfn-dlm-lifecyclepolicy-retainrule-interval"""
    p_IntervalUnit: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "IntervalUnit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-retainrule.html#cfn-dlm-lifecyclepolicy-retainrule-intervalunit"""

@attr.s
class PropLifecyclePolicyParameters(Property):
    """
    AWS Object Type = "AWS::DLM::LifecyclePolicy.Parameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-parameters.html

    Property Document:
    
    - ``p_ExcludeBootVolume``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-parameters.html#cfn-dlm-lifecyclepolicy-parameters-excludebootvolume
    - ``p_NoReboot``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-parameters.html#cfn-dlm-lifecyclepolicy-parameters-noreboot
    """
    AWS_OBJECT_TYPE = "AWS::DLM::LifecyclePolicy.Parameters"
    
    p_ExcludeBootVolume: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "ExcludeBootVolume"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-parameters.html#cfn-dlm-lifecyclepolicy-parameters-excludebootvolume"""
    p_NoReboot: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "NoReboot"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-parameters.html#cfn-dlm-lifecyclepolicy-parameters-noreboot"""

@attr.s
class PropLifecyclePolicyEncryptionConfiguration(Property):
    """
    AWS Object Type = "AWS::DLM::LifecyclePolicy.EncryptionConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-encryptionconfiguration.html

    Property Document:
    
    - ``rp_Encrypted``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-encryptionconfiguration.html#cfn-dlm-lifecyclepolicy-encryptionconfiguration-encrypted
    - ``p_CmkArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-encryptionconfiguration.html#cfn-dlm-lifecyclepolicy-encryptionconfiguration-cmkarn
    """
    AWS_OBJECT_TYPE = "AWS::DLM::LifecyclePolicy.EncryptionConfiguration"
    
    rp_Encrypted: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Encrypted"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-encryptionconfiguration.html#cfn-dlm-lifecyclepolicy-encryptionconfiguration-encrypted"""
    p_CmkArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CmkArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-encryptionconfiguration.html#cfn-dlm-lifecyclepolicy-encryptionconfiguration-cmkarn"""

@attr.s
class PropLifecyclePolicyCrossRegionCopyRetainRule(Property):
    """
    AWS Object Type = "AWS::DLM::LifecyclePolicy.CrossRegionCopyRetainRule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyretainrule.html

    Property Document:
    
    - ``rp_Interval``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyretainrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyretainrule-interval
    - ``rp_IntervalUnit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyretainrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyretainrule-intervalunit
    """
    AWS_OBJECT_TYPE = "AWS::DLM::LifecyclePolicy.CrossRegionCopyRetainRule"
    
    rp_Interval: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Interval"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyretainrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyretainrule-interval"""
    rp_IntervalUnit: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "IntervalUnit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyretainrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyretainrule-intervalunit"""

@attr.s
class PropLifecyclePolicyCrossRegionCopyAction(Property):
    """
    AWS Object Type = "AWS::DLM::LifecyclePolicy.CrossRegionCopyAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyaction.html

    Property Document:
    
    - ``rp_EncryptionConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyaction.html#cfn-dlm-lifecyclepolicy-crossregioncopyaction-encryptionconfiguration
    - ``rp_Target``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyaction.html#cfn-dlm-lifecyclepolicy-crossregioncopyaction-target
    - ``p_RetainRule``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyaction.html#cfn-dlm-lifecyclepolicy-crossregioncopyaction-retainrule
    """
    AWS_OBJECT_TYPE = "AWS::DLM::LifecyclePolicy.CrossRegionCopyAction"
    
    rp_EncryptionConfiguration: typing.Union['PropLifecyclePolicyEncryptionConfiguration', dict] = attr.ib(
        default=None,
        converter=PropLifecyclePolicyEncryptionConfiguration.from_dict,
        validator=attr.validators.instance_of(PropLifecyclePolicyEncryptionConfiguration),
        metadata={AttrMeta.PROPERTY_NAME: "EncryptionConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyaction.html#cfn-dlm-lifecyclepolicy-crossregioncopyaction-encryptionconfiguration"""
    rp_Target: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Target"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyaction.html#cfn-dlm-lifecyclepolicy-crossregioncopyaction-target"""
    p_RetainRule: typing.Union['PropLifecyclePolicyCrossRegionCopyRetainRule', dict] = attr.ib(
        default=None,
        converter=PropLifecyclePolicyCrossRegionCopyRetainRule.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropLifecyclePolicyCrossRegionCopyRetainRule)),
        metadata={AttrMeta.PROPERTY_NAME: "RetainRule"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyaction.html#cfn-dlm-lifecyclepolicy-crossregioncopyaction-retainrule"""

@attr.s
class PropLifecyclePolicyDeprecateRule(Property):
    """
    AWS Object Type = "AWS::DLM::LifecyclePolicy.DeprecateRule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-deprecaterule.html

    Property Document:
    
    - ``p_Count``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-deprecaterule.html#cfn-dlm-lifecyclepolicy-deprecaterule-count
    - ``p_Interval``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-deprecaterule.html#cfn-dlm-lifecyclepolicy-deprecaterule-interval
    - ``p_IntervalUnit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-deprecaterule.html#cfn-dlm-lifecyclepolicy-deprecaterule-intervalunit
    """
    AWS_OBJECT_TYPE = "AWS::DLM::LifecyclePolicy.DeprecateRule"
    
    p_Count: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Count"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-deprecaterule.html#cfn-dlm-lifecyclepolicy-deprecaterule-count"""
    p_Interval: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Interval"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-deprecaterule.html#cfn-dlm-lifecyclepolicy-deprecaterule-interval"""
    p_IntervalUnit: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "IntervalUnit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-deprecaterule.html#cfn-dlm-lifecyclepolicy-deprecaterule-intervalunit"""

@attr.s
class PropLifecyclePolicyCrossRegionCopyDeprecateRule(Property):
    """
    AWS Object Type = "AWS::DLM::LifecyclePolicy.CrossRegionCopyDeprecateRule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopydeprecaterule.html

    Property Document:
    
    - ``rp_Interval``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopydeprecaterule.html#cfn-dlm-lifecyclepolicy-crossregioncopydeprecaterule-interval
    - ``rp_IntervalUnit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopydeprecaterule.html#cfn-dlm-lifecyclepolicy-crossregioncopydeprecaterule-intervalunit
    """
    AWS_OBJECT_TYPE = "AWS::DLM::LifecyclePolicy.CrossRegionCopyDeprecateRule"
    
    rp_Interval: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Interval"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopydeprecaterule.html#cfn-dlm-lifecyclepolicy-crossregioncopydeprecaterule-interval"""
    rp_IntervalUnit: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "IntervalUnit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopydeprecaterule.html#cfn-dlm-lifecyclepolicy-crossregioncopydeprecaterule-intervalunit"""

@attr.s
class PropLifecyclePolicyShareRule(Property):
    """
    AWS Object Type = "AWS::DLM::LifecyclePolicy.ShareRule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-sharerule.html

    Property Document:
    
    - ``p_TargetAccounts``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-sharerule.html#cfn-dlm-lifecyclepolicy-sharerule-targetaccounts
    - ``p_UnshareInterval``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-sharerule.html#cfn-dlm-lifecyclepolicy-sharerule-unshareinterval
    - ``p_UnshareIntervalUnit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-sharerule.html#cfn-dlm-lifecyclepolicy-sharerule-unshareintervalunit
    """
    AWS_OBJECT_TYPE = "AWS::DLM::LifecyclePolicy.ShareRule"
    
    p_TargetAccounts: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "TargetAccounts"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-sharerule.html#cfn-dlm-lifecyclepolicy-sharerule-targetaccounts"""
    p_UnshareInterval: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "UnshareInterval"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-sharerule.html#cfn-dlm-lifecyclepolicy-sharerule-unshareinterval"""
    p_UnshareIntervalUnit: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "UnshareIntervalUnit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-sharerule.html#cfn-dlm-lifecyclepolicy-sharerule-unshareintervalunit"""

@attr.s
class PropLifecyclePolicyEventSource(Property):
    """
    AWS Object Type = "AWS::DLM::LifecyclePolicy.EventSource"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventsource.html

    Property Document:
    
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventsource.html#cfn-dlm-lifecyclepolicy-eventsource-type
    - ``p_Parameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventsource.html#cfn-dlm-lifecyclepolicy-eventsource-parameters
    """
    AWS_OBJECT_TYPE = "AWS::DLM::LifecyclePolicy.EventSource"
    
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventsource.html#cfn-dlm-lifecyclepolicy-eventsource-type"""
    p_Parameters: typing.Union['PropLifecyclePolicyEventParameters', dict] = attr.ib(
        default=None,
        converter=PropLifecyclePolicyEventParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropLifecyclePolicyEventParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "Parameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventsource.html#cfn-dlm-lifecyclepolicy-eventsource-parameters"""

@attr.s
class PropLifecyclePolicyAction(Property):
    """
    AWS Object Type = "AWS::DLM::LifecyclePolicy.Action"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-action.html

    Property Document:
    
    - ``rp_CrossRegionCopy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-action.html#cfn-dlm-lifecyclepolicy-action-crossregioncopy
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-action.html#cfn-dlm-lifecyclepolicy-action-name
    """
    AWS_OBJECT_TYPE = "AWS::DLM::LifecyclePolicy.Action"
    
    rp_CrossRegionCopy: typing.List[typing.Union['PropLifecyclePolicyCrossRegionCopyAction', dict]] = attr.ib(
        default=None,
        converter=PropLifecyclePolicyCrossRegionCopyAction.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropLifecyclePolicyCrossRegionCopyAction), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "CrossRegionCopy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-action.html#cfn-dlm-lifecyclepolicy-action-crossregioncopy"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-action.html#cfn-dlm-lifecyclepolicy-action-name"""

@attr.s
class PropLifecyclePolicyCrossRegionCopyRule(Property):
    """
    AWS Object Type = "AWS::DLM::LifecyclePolicy.CrossRegionCopyRule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html

    Property Document:
    
    - ``rp_Encrypted``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-encrypted
    - ``p_CmkArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-cmkarn
    - ``p_CopyTags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-copytags
    - ``p_DeprecateRule``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-deprecaterule
    - ``p_RetainRule``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-retainrule
    - ``p_Target``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-target
    - ``p_TargetRegion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-targetregion
    """
    AWS_OBJECT_TYPE = "AWS::DLM::LifecyclePolicy.CrossRegionCopyRule"
    
    rp_Encrypted: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Encrypted"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-encrypted"""
    p_CmkArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CmkArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-cmkarn"""
    p_CopyTags: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "CopyTags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-copytags"""
    p_DeprecateRule: typing.Union['PropLifecyclePolicyCrossRegionCopyDeprecateRule', dict] = attr.ib(
        default=None,
        converter=PropLifecyclePolicyCrossRegionCopyDeprecateRule.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropLifecyclePolicyCrossRegionCopyDeprecateRule)),
        metadata={AttrMeta.PROPERTY_NAME: "DeprecateRule"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-deprecaterule"""
    p_RetainRule: typing.Union['PropLifecyclePolicyCrossRegionCopyRetainRule', dict] = attr.ib(
        default=None,
        converter=PropLifecyclePolicyCrossRegionCopyRetainRule.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropLifecyclePolicyCrossRegionCopyRetainRule)),
        metadata={AttrMeta.PROPERTY_NAME: "RetainRule"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-retainrule"""
    p_Target: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Target"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-target"""
    p_TargetRegion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TargetRegion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-targetregion"""

@attr.s
class PropLifecyclePolicySchedule(Property):
    """
    AWS Object Type = "AWS::DLM::LifecyclePolicy.Schedule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html

    Property Document:
    
    - ``p_CopyTags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-copytags
    - ``p_CreateRule``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-createrule
    - ``p_CrossRegionCopyRules``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-crossregioncopyrules
    - ``p_DeprecateRule``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-deprecaterule
    - ``p_FastRestoreRule``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-fastrestorerule
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-name
    - ``p_RetainRule``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-retainrule
    - ``p_ShareRules``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-sharerules
    - ``p_TagsToAdd``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-tagstoadd
    - ``p_VariableTags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-variabletags
    """
    AWS_OBJECT_TYPE = "AWS::DLM::LifecyclePolicy.Schedule"
    
    p_CopyTags: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "CopyTags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-copytags"""
    p_CreateRule: typing.Union['PropLifecyclePolicyCreateRule', dict] = attr.ib(
        default=None,
        converter=PropLifecyclePolicyCreateRule.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropLifecyclePolicyCreateRule)),
        metadata={AttrMeta.PROPERTY_NAME: "CreateRule"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-createrule"""
    p_CrossRegionCopyRules: typing.List[typing.Union['PropLifecyclePolicyCrossRegionCopyRule', dict]] = attr.ib(
        default=None,
        converter=PropLifecyclePolicyCrossRegionCopyRule.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropLifecyclePolicyCrossRegionCopyRule), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "CrossRegionCopyRules"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-crossregioncopyrules"""
    p_DeprecateRule: typing.Union['PropLifecyclePolicyDeprecateRule', dict] = attr.ib(
        default=None,
        converter=PropLifecyclePolicyDeprecateRule.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropLifecyclePolicyDeprecateRule)),
        metadata={AttrMeta.PROPERTY_NAME: "DeprecateRule"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-deprecaterule"""
    p_FastRestoreRule: typing.Union['PropLifecyclePolicyFastRestoreRule', dict] = attr.ib(
        default=None,
        converter=PropLifecyclePolicyFastRestoreRule.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropLifecyclePolicyFastRestoreRule)),
        metadata={AttrMeta.PROPERTY_NAME: "FastRestoreRule"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-fastrestorerule"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-name"""
    p_RetainRule: typing.Union['PropLifecyclePolicyRetainRule', dict] = attr.ib(
        default=None,
        converter=PropLifecyclePolicyRetainRule.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropLifecyclePolicyRetainRule)),
        metadata={AttrMeta.PROPERTY_NAME: "RetainRule"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-retainrule"""
    p_ShareRules: typing.List[typing.Union['PropLifecyclePolicyShareRule', dict]] = attr.ib(
        default=None,
        converter=PropLifecyclePolicyShareRule.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropLifecyclePolicyShareRule), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ShareRules"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-sharerules"""
    p_TagsToAdd: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "TagsToAdd"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-tagstoadd"""
    p_VariableTags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "VariableTags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-variabletags"""

@attr.s
class PropLifecyclePolicyPolicyDetails(Property):
    """
    AWS Object Type = "AWS::DLM::LifecyclePolicy.PolicyDetails"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html

    Property Document:
    
    - ``p_Actions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-actions
    - ``p_EventSource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-eventsource
    - ``p_Parameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-parameters
    - ``p_PolicyType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-policytype
    - ``p_ResourceLocations``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-resourcelocations
    - ``p_ResourceTypes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-resourcetypes
    - ``p_Schedules``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-schedules
    - ``p_TargetTags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-targettags
    """
    AWS_OBJECT_TYPE = "AWS::DLM::LifecyclePolicy.PolicyDetails"
    
    p_Actions: typing.List[typing.Union['PropLifecyclePolicyAction', dict]] = attr.ib(
        default=None,
        converter=PropLifecyclePolicyAction.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropLifecyclePolicyAction), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Actions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-actions"""
    p_EventSource: typing.Union['PropLifecyclePolicyEventSource', dict] = attr.ib(
        default=None,
        converter=PropLifecyclePolicyEventSource.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropLifecyclePolicyEventSource)),
        metadata={AttrMeta.PROPERTY_NAME: "EventSource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-eventsource"""
    p_Parameters: typing.Union['PropLifecyclePolicyParameters', dict] = attr.ib(
        default=None,
        converter=PropLifecyclePolicyParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropLifecyclePolicyParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "Parameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-parameters"""
    p_PolicyType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PolicyType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-policytype"""
    p_ResourceLocations: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceLocations"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-resourcelocations"""
    p_ResourceTypes: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceTypes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-resourcetypes"""
    p_Schedules: typing.List[typing.Union['PropLifecyclePolicySchedule', dict]] = attr.ib(
        default=None,
        converter=PropLifecyclePolicySchedule.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropLifecyclePolicySchedule), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Schedules"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-schedules"""
    p_TargetTags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "TargetTags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-targettags"""


#--- Resource declaration ---

@attr.s
class LifecyclePolicy(Resource):
    """
    AWS Object Type = "AWS::DLM::LifecyclePolicy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html

    Property Document:
    
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-description
    - ``p_ExecutionRoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-executionrolearn
    - ``p_PolicyDetails``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-policydetails
    - ``p_State``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-state
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-tags
    """
    AWS_OBJECT_TYPE = "AWS::DLM::LifecyclePolicy"

    
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-description"""
    p_ExecutionRoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ExecutionRoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-executionrolearn"""
    p_PolicyDetails: typing.Union['PropLifecyclePolicyPolicyDetails', dict] = attr.ib(
        default=None,
        converter=PropLifecyclePolicyPolicyDetails.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropLifecyclePolicyPolicyDetails)),
        metadata={AttrMeta.PROPERTY_NAME: "PolicyDetails"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-policydetails"""
    p_State: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "State"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-state"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#aws-resource-dlm-lifecyclepolicy-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
