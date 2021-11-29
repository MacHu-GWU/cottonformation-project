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
class PropDetectorLabel(Property):
    """
    AWS Object Type = "AWS::FraudDetector::Detector.Label"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html

    Property Document:
    
    - ``p_Arn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html#cfn-frauddetector-detector-label-arn
    - ``p_CreatedTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html#cfn-frauddetector-detector-label-createdtime
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html#cfn-frauddetector-detector-label-description
    - ``p_Inline``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html#cfn-frauddetector-detector-label-inline
    - ``p_LastUpdatedTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html#cfn-frauddetector-detector-label-lastupdatedtime
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html#cfn-frauddetector-detector-label-name
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html#cfn-frauddetector-detector-label-tags
    """
    AWS_OBJECT_TYPE = "AWS::FraudDetector::Detector.Label"
    
    p_Arn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Arn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html#cfn-frauddetector-detector-label-arn"""
    p_CreatedTime: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CreatedTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html#cfn-frauddetector-detector-label-createdtime"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html#cfn-frauddetector-detector-label-description"""
    p_Inline: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Inline"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html#cfn-frauddetector-detector-label-inline"""
    p_LastUpdatedTime: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LastUpdatedTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html#cfn-frauddetector-detector-label-lastupdatedtime"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html#cfn-frauddetector-detector-label-name"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html#cfn-frauddetector-detector-label-tags"""

@attr.s
class PropDetectorEntityType(Property):
    """
    AWS Object Type = "AWS::FraudDetector::Detector.EntityType"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html

    Property Document:
    
    - ``p_Arn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html#cfn-frauddetector-detector-entitytype-arn
    - ``p_CreatedTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html#cfn-frauddetector-detector-entitytype-createdtime
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html#cfn-frauddetector-detector-entitytype-description
    - ``p_Inline``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html#cfn-frauddetector-detector-entitytype-inline
    - ``p_LastUpdatedTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html#cfn-frauddetector-detector-entitytype-lastupdatedtime
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html#cfn-frauddetector-detector-entitytype-name
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html#cfn-frauddetector-detector-entitytype-tags
    """
    AWS_OBJECT_TYPE = "AWS::FraudDetector::Detector.EntityType"
    
    p_Arn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Arn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html#cfn-frauddetector-detector-entitytype-arn"""
    p_CreatedTime: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CreatedTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html#cfn-frauddetector-detector-entitytype-createdtime"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html#cfn-frauddetector-detector-entitytype-description"""
    p_Inline: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Inline"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html#cfn-frauddetector-detector-entitytype-inline"""
    p_LastUpdatedTime: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LastUpdatedTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html#cfn-frauddetector-detector-entitytype-lastupdatedtime"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html#cfn-frauddetector-detector-entitytype-name"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html#cfn-frauddetector-detector-entitytype-tags"""

@attr.s
class PropDetectorModel(Property):
    """
    AWS Object Type = "AWS::FraudDetector::Detector.Model"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-model.html

    Property Document:
    
    - ``p_Arn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-model.html#cfn-frauddetector-detector-model-arn
    """
    AWS_OBJECT_TYPE = "AWS::FraudDetector::Detector.Model"
    
    p_Arn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Arn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-model.html#cfn-frauddetector-detector-model-arn"""

@attr.s
class PropDetectorOutcome(Property):
    """
    AWS Object Type = "AWS::FraudDetector::Detector.Outcome"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html

    Property Document:
    
    - ``p_Arn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html#cfn-frauddetector-detector-outcome-arn
    - ``p_CreatedTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html#cfn-frauddetector-detector-outcome-createdtime
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html#cfn-frauddetector-detector-outcome-description
    - ``p_Inline``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html#cfn-frauddetector-detector-outcome-inline
    - ``p_LastUpdatedTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html#cfn-frauddetector-detector-outcome-lastupdatedtime
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html#cfn-frauddetector-detector-outcome-name
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html#cfn-frauddetector-detector-outcome-tags
    """
    AWS_OBJECT_TYPE = "AWS::FraudDetector::Detector.Outcome"
    
    p_Arn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Arn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html#cfn-frauddetector-detector-outcome-arn"""
    p_CreatedTime: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CreatedTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html#cfn-frauddetector-detector-outcome-createdtime"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html#cfn-frauddetector-detector-outcome-description"""
    p_Inline: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Inline"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html#cfn-frauddetector-detector-outcome-inline"""
    p_LastUpdatedTime: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LastUpdatedTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html#cfn-frauddetector-detector-outcome-lastupdatedtime"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html#cfn-frauddetector-detector-outcome-name"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html#cfn-frauddetector-detector-outcome-tags"""

@attr.s
class PropEventTypeEntityType(Property):
    """
    AWS Object Type = "AWS::FraudDetector::EventType.EntityType"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html

    Property Document:
    
    - ``p_Arn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html#cfn-frauddetector-eventtype-entitytype-arn
    - ``p_CreatedTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html#cfn-frauddetector-eventtype-entitytype-createdtime
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html#cfn-frauddetector-eventtype-entitytype-description
    - ``p_Inline``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html#cfn-frauddetector-eventtype-entitytype-inline
    - ``p_LastUpdatedTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html#cfn-frauddetector-eventtype-entitytype-lastupdatedtime
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html#cfn-frauddetector-eventtype-entitytype-name
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html#cfn-frauddetector-eventtype-entitytype-tags
    """
    AWS_OBJECT_TYPE = "AWS::FraudDetector::EventType.EntityType"
    
    p_Arn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Arn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html#cfn-frauddetector-eventtype-entitytype-arn"""
    p_CreatedTime: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CreatedTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html#cfn-frauddetector-eventtype-entitytype-createdtime"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html#cfn-frauddetector-eventtype-entitytype-description"""
    p_Inline: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Inline"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html#cfn-frauddetector-eventtype-entitytype-inline"""
    p_LastUpdatedTime: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LastUpdatedTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html#cfn-frauddetector-eventtype-entitytype-lastupdatedtime"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html#cfn-frauddetector-eventtype-entitytype-name"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html#cfn-frauddetector-eventtype-entitytype-tags"""

@attr.s
class PropDetectorEventVariable(Property):
    """
    AWS Object Type = "AWS::FraudDetector::Detector.EventVariable"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html

    Property Document:
    
    - ``p_Arn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-arn
    - ``p_CreatedTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-createdtime
    - ``p_DataSource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-datasource
    - ``p_DataType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-datatype
    - ``p_DefaultValue``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-defaultvalue
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-description
    - ``p_Inline``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-inline
    - ``p_LastUpdatedTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-lastupdatedtime
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-name
    - ``p_VariableType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-variabletype
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-tags
    """
    AWS_OBJECT_TYPE = "AWS::FraudDetector::Detector.EventVariable"
    
    p_Arn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Arn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-arn"""
    p_CreatedTime: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CreatedTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-createdtime"""
    p_DataSource: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DataSource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-datasource"""
    p_DataType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DataType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-datatype"""
    p_DefaultValue: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultValue"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-defaultvalue"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-description"""
    p_Inline: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Inline"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-inline"""
    p_LastUpdatedTime: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LastUpdatedTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-lastupdatedtime"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-name"""
    p_VariableType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "VariableType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-variabletype"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-tags"""

@attr.s
class PropEventTypeEventVariable(Property):
    """
    AWS Object Type = "AWS::FraudDetector::EventType.EventVariable"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html

    Property Document:
    
    - ``p_Arn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-arn
    - ``p_CreatedTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-createdtime
    - ``p_DataSource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-datasource
    - ``p_DataType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-datatype
    - ``p_DefaultValue``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-defaultvalue
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-description
    - ``p_Inline``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-inline
    - ``p_LastUpdatedTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-lastupdatedtime
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-name
    - ``p_VariableType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-variabletype
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-tags
    """
    AWS_OBJECT_TYPE = "AWS::FraudDetector::EventType.EventVariable"
    
    p_Arn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Arn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-arn"""
    p_CreatedTime: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CreatedTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-createdtime"""
    p_DataSource: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DataSource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-datasource"""
    p_DataType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DataType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-datatype"""
    p_DefaultValue: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultValue"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-defaultvalue"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-description"""
    p_Inline: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Inline"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-inline"""
    p_LastUpdatedTime: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LastUpdatedTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-lastupdatedtime"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-name"""
    p_VariableType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "VariableType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-variabletype"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-tags"""

@attr.s
class PropEventTypeLabel(Property):
    """
    AWS Object Type = "AWS::FraudDetector::EventType.Label"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html

    Property Document:
    
    - ``p_Arn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html#cfn-frauddetector-eventtype-label-arn
    - ``p_CreatedTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html#cfn-frauddetector-eventtype-label-createdtime
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html#cfn-frauddetector-eventtype-label-description
    - ``p_Inline``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html#cfn-frauddetector-eventtype-label-inline
    - ``p_LastUpdatedTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html#cfn-frauddetector-eventtype-label-lastupdatedtime
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html#cfn-frauddetector-eventtype-label-name
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html#cfn-frauddetector-eventtype-label-tags
    """
    AWS_OBJECT_TYPE = "AWS::FraudDetector::EventType.Label"
    
    p_Arn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Arn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html#cfn-frauddetector-eventtype-label-arn"""
    p_CreatedTime: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CreatedTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html#cfn-frauddetector-eventtype-label-createdtime"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html#cfn-frauddetector-eventtype-label-description"""
    p_Inline: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Inline"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html#cfn-frauddetector-eventtype-label-inline"""
    p_LastUpdatedTime: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LastUpdatedTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html#cfn-frauddetector-eventtype-label-lastupdatedtime"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html#cfn-frauddetector-eventtype-label-name"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html#cfn-frauddetector-eventtype-label-tags"""

@attr.s
class PropDetectorRule(Property):
    """
    AWS Object Type = "AWS::FraudDetector::Detector.Rule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html

    Property Document:
    
    - ``p_Arn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-arn
    - ``p_CreatedTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-createdtime
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-description
    - ``p_DetectorId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-detectorid
    - ``p_Expression``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-expression
    - ``p_Language``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-language
    - ``p_LastUpdatedTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-lastupdatedtime
    - ``p_Outcomes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-outcomes
    - ``p_RuleId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-ruleid
    - ``p_RuleVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-ruleversion
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-tags
    """
    AWS_OBJECT_TYPE = "AWS::FraudDetector::Detector.Rule"
    
    p_Arn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Arn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-arn"""
    p_CreatedTime: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CreatedTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-createdtime"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-description"""
    p_DetectorId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DetectorId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-detectorid"""
    p_Expression: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Expression"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-expression"""
    p_Language: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Language"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-language"""
    p_LastUpdatedTime: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LastUpdatedTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-lastupdatedtime"""
    p_Outcomes: typing.List[typing.Union['PropDetectorOutcome', dict]] = attr.ib(
        default=None,
        converter=PropDetectorOutcome.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDetectorOutcome), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Outcomes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-outcomes"""
    p_RuleId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RuleId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-ruleid"""
    p_RuleVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RuleVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-ruleversion"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-tags"""

@attr.s
class PropDetectorEventType(Property):
    """
    AWS Object Type = "AWS::FraudDetector::Detector.EventType"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html

    Property Document:
    
    - ``p_Arn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-arn
    - ``p_CreatedTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-createdtime
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-description
    - ``p_EntityTypes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-entitytypes
    - ``p_EventVariables``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-eventvariables
    - ``p_Inline``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-inline
    - ``p_Labels``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-labels
    - ``p_LastUpdatedTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-lastupdatedtime
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-name
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-tags
    """
    AWS_OBJECT_TYPE = "AWS::FraudDetector::Detector.EventType"
    
    p_Arn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Arn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-arn"""
    p_CreatedTime: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CreatedTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-createdtime"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-description"""
    p_EntityTypes: typing.List[typing.Union['PropDetectorEntityType', dict]] = attr.ib(
        default=None,
        converter=PropDetectorEntityType.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDetectorEntityType), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "EntityTypes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-entitytypes"""
    p_EventVariables: typing.List[typing.Union['PropDetectorEventVariable', dict]] = attr.ib(
        default=None,
        converter=PropDetectorEventVariable.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDetectorEventVariable), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "EventVariables"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-eventvariables"""
    p_Inline: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Inline"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-inline"""
    p_Labels: typing.List[typing.Union['PropDetectorLabel', dict]] = attr.ib(
        default=None,
        converter=PropDetectorLabel.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDetectorLabel), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Labels"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-labels"""
    p_LastUpdatedTime: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LastUpdatedTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-lastupdatedtime"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-name"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-tags"""


#--- Resource declaration ---

@attr.s
class EntityType(Resource):
    """
    AWS Object Type = "AWS::FraudDetector::EntityType"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-entitytype.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-entitytype.html#cfn-frauddetector-entitytype-name
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-entitytype.html#cfn-frauddetector-entitytype-description
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-entitytype.html#cfn-frauddetector-entitytype-tags
    """
    AWS_OBJECT_TYPE = "AWS::FraudDetector::EntityType"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-entitytype.html#cfn-frauddetector-entitytype-name"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-entitytype.html#cfn-frauddetector-entitytype-description"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-entitytype.html#cfn-frauddetector-entitytype-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-entitytype.html#aws-resource-frauddetector-entitytype-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_CreatedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-entitytype.html#aws-resource-frauddetector-entitytype-return-values"""
        return GetAtt(resource=self, attr_name="CreatedTime")
    
    @property
    def rv_LastUpdatedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-entitytype.html#aws-resource-frauddetector-entitytype-return-values"""
        return GetAtt(resource=self, attr_name="LastUpdatedTime")
    

@attr.s
class Outcome(Resource):
    """
    AWS Object Type = "AWS::FraudDetector::Outcome"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-outcome.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-outcome.html#cfn-frauddetector-outcome-name
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-outcome.html#cfn-frauddetector-outcome-description
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-outcome.html#cfn-frauddetector-outcome-tags
    """
    AWS_OBJECT_TYPE = "AWS::FraudDetector::Outcome"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-outcome.html#cfn-frauddetector-outcome-name"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-outcome.html#cfn-frauddetector-outcome-description"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-outcome.html#cfn-frauddetector-outcome-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-outcome.html#aws-resource-frauddetector-outcome-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_CreatedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-outcome.html#aws-resource-frauddetector-outcome-return-values"""
        return GetAtt(resource=self, attr_name="CreatedTime")
    
    @property
    def rv_LastUpdatedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-outcome.html#aws-resource-frauddetector-outcome-return-values"""
        return GetAtt(resource=self, attr_name="LastUpdatedTime")
    

@attr.s
class Detector(Resource):
    """
    AWS Object Type = "AWS::FraudDetector::Detector"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html

    Property Document:
    
    - ``rp_DetectorId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-detectorid
    - ``rp_EventType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-eventtype
    - ``rp_Rules``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-rules
    - ``p_AssociatedModels``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-associatedmodels
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-description
    - ``p_DetectorVersionStatus``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-detectorversionstatus
    - ``p_RuleExecutionMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-ruleexecutionmode
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-tags
    """
    AWS_OBJECT_TYPE = "AWS::FraudDetector::Detector"

    
    rp_DetectorId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DetectorId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-detectorid"""
    rp_EventType: typing.Union['PropDetectorEventType', dict] = attr.ib(
        default=None,
        converter=PropDetectorEventType.from_dict,
        validator=attr.validators.instance_of(PropDetectorEventType),
        metadata={AttrMeta.PROPERTY_NAME: "EventType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-eventtype"""
    rp_Rules: typing.List[typing.Union['PropDetectorRule', dict]] = attr.ib(
        default=None,
        converter=PropDetectorRule.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDetectorRule), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Rules"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-rules"""
    p_AssociatedModels: typing.List[typing.Union['PropDetectorModel', dict]] = attr.ib(
        default=None,
        converter=PropDetectorModel.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDetectorModel), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AssociatedModels"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-associatedmodels"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-description"""
    p_DetectorVersionStatus: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DetectorVersionStatus"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-detectorversionstatus"""
    p_RuleExecutionMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RuleExecutionMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-ruleexecutionmode"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-tags"""

    
    @property
    def rv_DetectorVersionId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#aws-resource-frauddetector-detector-return-values"""
        return GetAtt(resource=self, attr_name="DetectorVersionId")
    
    @property
    def rv_EventTypeArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#aws-resource-frauddetector-detector-return-values"""
        return GetAtt(resource=self, attr_name="EventType.Arn")
    
    @property
    def rv_EventTypeCreatedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#aws-resource-frauddetector-detector-return-values"""
        return GetAtt(resource=self, attr_name="EventType.CreatedTime")
    
    @property
    def rv_EventTypeLastUpdatedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#aws-resource-frauddetector-detector-return-values"""
        return GetAtt(resource=self, attr_name="EventType.LastUpdatedTime")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#aws-resource-frauddetector-detector-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_CreatedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#aws-resource-frauddetector-detector-return-values"""
        return GetAtt(resource=self, attr_name="CreatedTime")
    
    @property
    def rv_LastUpdatedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#aws-resource-frauddetector-detector-return-values"""
        return GetAtt(resource=self, attr_name="LastUpdatedTime")
    

@attr.s
class Label(Resource):
    """
    AWS Object Type = "AWS::FraudDetector::Label"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html#cfn-frauddetector-label-name
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html#cfn-frauddetector-label-description
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html#cfn-frauddetector-label-tags
    """
    AWS_OBJECT_TYPE = "AWS::FraudDetector::Label"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html#cfn-frauddetector-label-name"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html#cfn-frauddetector-label-description"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html#cfn-frauddetector-label-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html#aws-resource-frauddetector-label-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_CreatedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html#aws-resource-frauddetector-label-return-values"""
        return GetAtt(resource=self, attr_name="CreatedTime")
    
    @property
    def rv_LastUpdatedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html#aws-resource-frauddetector-label-return-values"""
        return GetAtt(resource=self, attr_name="LastUpdatedTime")
    

@attr.s
class Variable(Resource):
    """
    AWS Object Type = "AWS::FraudDetector::Variable"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html

    Property Document:
    
    - ``rp_DataSource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-datasource
    - ``rp_DataType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-datatype
    - ``rp_DefaultValue``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-defaultvalue
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-name
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-description
    - ``p_VariableType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-variabletype
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-tags
    """
    AWS_OBJECT_TYPE = "AWS::FraudDetector::Variable"

    
    rp_DataSource: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DataSource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-datasource"""
    rp_DataType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DataType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-datatype"""
    rp_DefaultValue: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultValue"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-defaultvalue"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-name"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-description"""
    p_VariableType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "VariableType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-variabletype"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#aws-resource-frauddetector-variable-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_CreatedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#aws-resource-frauddetector-variable-return-values"""
        return GetAtt(resource=self, attr_name="CreatedTime")
    
    @property
    def rv_LastUpdatedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#aws-resource-frauddetector-variable-return-values"""
        return GetAtt(resource=self, attr_name="LastUpdatedTime")
    

@attr.s
class EventType(Resource):
    """
    AWS Object Type = "AWS::FraudDetector::EventType"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html

    Property Document:
    
    - ``rp_EntityTypes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#cfn-frauddetector-eventtype-entitytypes
    - ``rp_EventVariables``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#cfn-frauddetector-eventtype-eventvariables
    - ``rp_Labels``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#cfn-frauddetector-eventtype-labels
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#cfn-frauddetector-eventtype-name
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#cfn-frauddetector-eventtype-description
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#cfn-frauddetector-eventtype-tags
    """
    AWS_OBJECT_TYPE = "AWS::FraudDetector::EventType"

    
    rp_EntityTypes: typing.List[typing.Union['PropEventTypeEntityType', dict]] = attr.ib(
        default=None,
        converter=PropEventTypeEntityType.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropEventTypeEntityType), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "EntityTypes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#cfn-frauddetector-eventtype-entitytypes"""
    rp_EventVariables: typing.List[typing.Union['PropEventTypeEventVariable', dict]] = attr.ib(
        default=None,
        converter=PropEventTypeEventVariable.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropEventTypeEventVariable), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "EventVariables"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#cfn-frauddetector-eventtype-eventvariables"""
    rp_Labels: typing.List[typing.Union['PropEventTypeLabel', dict]] = attr.ib(
        default=None,
        converter=PropEventTypeLabel.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropEventTypeLabel), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Labels"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#cfn-frauddetector-eventtype-labels"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#cfn-frauddetector-eventtype-name"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#cfn-frauddetector-eventtype-description"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#cfn-frauddetector-eventtype-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#aws-resource-frauddetector-eventtype-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_CreatedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#aws-resource-frauddetector-eventtype-return-values"""
        return GetAtt(resource=self, attr_name="CreatedTime")
    
    @property
    def rv_LastUpdatedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#aws-resource-frauddetector-eventtype-return-values"""
        return GetAtt(resource=self, attr_name="LastUpdatedTime")
    
