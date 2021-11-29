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
class PropCampaignMetricDimension(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Campaign.MetricDimension"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-metricdimension.html

    Property Document:
    
    - ``p_ComparisonOperator``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-metricdimension.html#cfn-pinpoint-campaign-metricdimension-comparisonoperator
    - ``p_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-metricdimension.html#cfn-pinpoint-campaign-metricdimension-value
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Campaign.MetricDimension"
    
    p_ComparisonOperator: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ComparisonOperator"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-metricdimension.html#cfn-pinpoint-campaign-metricdimension-comparisonoperator"""
    p_Value: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-metricdimension.html#cfn-pinpoint-campaign-metricdimension-value"""

@attr.s
class PropCampaignInAppMessageBodyConfig(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Campaign.InAppMessageBodyConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebodyconfig.html

    Property Document:
    
    - ``p_Alignment``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebodyconfig.html#cfn-pinpoint-campaign-inappmessagebodyconfig-alignment
    - ``p_Body``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebodyconfig.html#cfn-pinpoint-campaign-inappmessagebodyconfig-body
    - ``p_TextColor``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebodyconfig.html#cfn-pinpoint-campaign-inappmessagebodyconfig-textcolor
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Campaign.InAppMessageBodyConfig"
    
    p_Alignment: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Alignment"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebodyconfig.html#cfn-pinpoint-campaign-inappmessagebodyconfig-alignment"""
    p_Body: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Body"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebodyconfig.html#cfn-pinpoint-campaign-inappmessagebodyconfig-body"""
    p_TextColor: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TextColor"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebodyconfig.html#cfn-pinpoint-campaign-inappmessagebodyconfig-textcolor"""

@attr.s
class PropSegmentAttributeDimension(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Segment.AttributeDimension"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-attributedimension.html

    Property Document:
    
    - ``p_AttributeType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-attributedimension.html#cfn-pinpoint-segment-attributedimension-attributetype
    - ``p_Values``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-attributedimension.html#cfn-pinpoint-segment-attributedimension-values
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Segment.AttributeDimension"
    
    p_AttributeType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AttributeType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-attributedimension.html#cfn-pinpoint-segment-attributedimension-attributetype"""
    p_Values: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Values"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-attributedimension.html#cfn-pinpoint-segment-attributedimension-values"""

@attr.s
class PropCampaignDefaultButtonConfiguration(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Campaign.DefaultButtonConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html

    Property Document:
    
    - ``p_BackgroundColor``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html#cfn-pinpoint-campaign-defaultbuttonconfiguration-backgroundcolor
    - ``p_BorderRadius``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html#cfn-pinpoint-campaign-defaultbuttonconfiguration-borderradius
    - ``p_ButtonAction``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html#cfn-pinpoint-campaign-defaultbuttonconfiguration-buttonaction
    - ``p_Link``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html#cfn-pinpoint-campaign-defaultbuttonconfiguration-link
    - ``p_Text``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html#cfn-pinpoint-campaign-defaultbuttonconfiguration-text
    - ``p_TextColor``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html#cfn-pinpoint-campaign-defaultbuttonconfiguration-textcolor
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Campaign.DefaultButtonConfiguration"
    
    p_BackgroundColor: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BackgroundColor"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html#cfn-pinpoint-campaign-defaultbuttonconfiguration-backgroundcolor"""
    p_BorderRadius: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "BorderRadius"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html#cfn-pinpoint-campaign-defaultbuttonconfiguration-borderradius"""
    p_ButtonAction: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ButtonAction"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html#cfn-pinpoint-campaign-defaultbuttonconfiguration-buttonaction"""
    p_Link: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Link"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html#cfn-pinpoint-campaign-defaultbuttonconfiguration-link"""
    p_Text: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Text"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html#cfn-pinpoint-campaign-defaultbuttonconfiguration-text"""
    p_TextColor: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TextColor"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html#cfn-pinpoint-campaign-defaultbuttonconfiguration-textcolor"""

@attr.s
class PropSegmentRecency(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Segment.Recency"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-behavior-recency.html

    Property Document:
    
    - ``rp_Duration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-behavior-recency.html#cfn-pinpoint-segment-segmentdimensions-behavior-recency-duration
    - ``rp_RecencyType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-behavior-recency.html#cfn-pinpoint-segment-segmentdimensions-behavior-recency-recencytype
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Segment.Recency"
    
    rp_Duration: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Duration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-behavior-recency.html#cfn-pinpoint-segment-segmentdimensions-behavior-recency-duration"""
    rp_RecencyType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RecencyType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-behavior-recency.html#cfn-pinpoint-segment-segmentdimensions-behavior-recency-recencytype"""

@attr.s
class PropCampaignInAppMessageHeaderConfig(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Campaign.InAppMessageHeaderConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessageheaderconfig.html

    Property Document:
    
    - ``p_Alignment``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessageheaderconfig.html#cfn-pinpoint-campaign-inappmessageheaderconfig-alignment
    - ``p_Header``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessageheaderconfig.html#cfn-pinpoint-campaign-inappmessageheaderconfig-header
    - ``p_TextColor``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessageheaderconfig.html#cfn-pinpoint-campaign-inappmessageheaderconfig-textcolor
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Campaign.InAppMessageHeaderConfig"
    
    p_Alignment: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Alignment"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessageheaderconfig.html#cfn-pinpoint-campaign-inappmessageheaderconfig-alignment"""
    p_Header: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Header"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessageheaderconfig.html#cfn-pinpoint-campaign-inappmessageheaderconfig-header"""
    p_TextColor: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TextColor"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessageheaderconfig.html#cfn-pinpoint-campaign-inappmessageheaderconfig-textcolor"""

@attr.s
class PropInAppTemplateDefaultButtonConfiguration(Property):
    """
    AWS Object Type = "AWS::Pinpoint::InAppTemplate.DefaultButtonConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-defaultbuttonconfiguration.html

    Property Document:
    
    - ``p_BackgroundColor``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-defaultbuttonconfiguration.html#cfn-pinpoint-inapptemplate-defaultbuttonconfiguration-backgroundcolor
    - ``p_BorderRadius``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-defaultbuttonconfiguration.html#cfn-pinpoint-inapptemplate-defaultbuttonconfiguration-borderradius
    - ``p_ButtonAction``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-defaultbuttonconfiguration.html#cfn-pinpoint-inapptemplate-defaultbuttonconfiguration-buttonaction
    - ``p_Link``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-defaultbuttonconfiguration.html#cfn-pinpoint-inapptemplate-defaultbuttonconfiguration-link
    - ``p_Text``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-defaultbuttonconfiguration.html#cfn-pinpoint-inapptemplate-defaultbuttonconfiguration-text
    - ``p_TextColor``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-defaultbuttonconfiguration.html#cfn-pinpoint-inapptemplate-defaultbuttonconfiguration-textcolor
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::InAppTemplate.DefaultButtonConfiguration"
    
    p_BackgroundColor: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BackgroundColor"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-defaultbuttonconfiguration.html#cfn-pinpoint-inapptemplate-defaultbuttonconfiguration-backgroundcolor"""
    p_BorderRadius: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "BorderRadius"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-defaultbuttonconfiguration.html#cfn-pinpoint-inapptemplate-defaultbuttonconfiguration-borderradius"""
    p_ButtonAction: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ButtonAction"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-defaultbuttonconfiguration.html#cfn-pinpoint-inapptemplate-defaultbuttonconfiguration-buttonaction"""
    p_Link: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Link"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-defaultbuttonconfiguration.html#cfn-pinpoint-inapptemplate-defaultbuttonconfiguration-link"""
    p_Text: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Text"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-defaultbuttonconfiguration.html#cfn-pinpoint-inapptemplate-defaultbuttonconfiguration-text"""
    p_TextColor: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TextColor"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-defaultbuttonconfiguration.html#cfn-pinpoint-inapptemplate-defaultbuttonconfiguration-textcolor"""

@attr.s
class PropCampaignQuietTime(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Campaign.QuietTime"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule-quiettime.html

    Property Document:
    
    - ``rp_End``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule-quiettime.html#cfn-pinpoint-campaign-schedule-quiettime-end
    - ``rp_Start``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule-quiettime.html#cfn-pinpoint-campaign-schedule-quiettime-start
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Campaign.QuietTime"
    
    rp_End: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "End"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule-quiettime.html#cfn-pinpoint-campaign-schedule-quiettime-end"""
    rp_Start: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Start"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule-quiettime.html#cfn-pinpoint-campaign-schedule-quiettime-start"""

@attr.s
class PropApplicationSettingsCampaignHook(Property):
    """
    AWS Object Type = "AWS::Pinpoint::ApplicationSettings.CampaignHook"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-campaignhook.html

    Property Document:
    
    - ``p_LambdaFunctionName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-campaignhook.html#cfn-pinpoint-applicationsettings-campaignhook-lambdafunctionname
    - ``p_Mode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-campaignhook.html#cfn-pinpoint-applicationsettings-campaignhook-mode
    - ``p_WebUrl``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-campaignhook.html#cfn-pinpoint-applicationsettings-campaignhook-weburl
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::ApplicationSettings.CampaignHook"
    
    p_LambdaFunctionName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LambdaFunctionName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-campaignhook.html#cfn-pinpoint-applicationsettings-campaignhook-lambdafunctionname"""
    p_Mode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Mode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-campaignhook.html#cfn-pinpoint-applicationsettings-campaignhook-mode"""
    p_WebUrl: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "WebUrl"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-campaignhook.html#cfn-pinpoint-applicationsettings-campaignhook-weburl"""

@attr.s
class PropPushTemplateDefaultPushNotificationTemplate(Property):
    """
    AWS Object Type = "AWS::Pinpoint::PushTemplate.DefaultPushNotificationTemplate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html

    Property Document:
    
    - ``p_Action``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-defaultpushnotificationtemplate-action
    - ``p_Body``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-defaultpushnotificationtemplate-body
    - ``p_Sound``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-defaultpushnotificationtemplate-sound
    - ``p_Title``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-defaultpushnotificationtemplate-title
    - ``p_Url``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-defaultpushnotificationtemplate-url
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::PushTemplate.DefaultPushNotificationTemplate"
    
    p_Action: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Action"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-defaultpushnotificationtemplate-action"""
    p_Body: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Body"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-defaultpushnotificationtemplate-body"""
    p_Sound: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Sound"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-defaultpushnotificationtemplate-sound"""
    p_Title: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Title"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-defaultpushnotificationtemplate-title"""
    p_Url: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Url"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-defaultpushnotificationtemplate-url"""

@attr.s
class PropCampaignMessage(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Campaign.Message"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html

    Property Document:
    
    - ``p_Action``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-action
    - ``p_Body``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-body
    - ``p_ImageIconUrl``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-imageiconurl
    - ``p_ImageSmallIconUrl``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-imagesmalliconurl
    - ``p_ImageUrl``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-imageurl
    - ``p_JsonBody``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-jsonbody
    - ``p_MediaUrl``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-mediaurl
    - ``p_RawContent``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-rawcontent
    - ``p_SilentPush``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-silentpush
    - ``p_TimeToLive``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-timetolive
    - ``p_Title``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-title
    - ``p_Url``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-url
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Campaign.Message"
    
    p_Action: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Action"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-action"""
    p_Body: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Body"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-body"""
    p_ImageIconUrl: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ImageIconUrl"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-imageiconurl"""
    p_ImageSmallIconUrl: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ImageSmallIconUrl"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-imagesmalliconurl"""
    p_ImageUrl: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ImageUrl"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-imageurl"""
    p_JsonBody: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "JsonBody"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-jsonbody"""
    p_MediaUrl: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MediaUrl"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-mediaurl"""
    p_RawContent: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RawContent"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-rawcontent"""
    p_SilentPush: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "SilentPush"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-silentpush"""
    p_TimeToLive: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "TimeToLive"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-timetolive"""
    p_Title: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Title"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-title"""
    p_Url: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Url"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-url"""

@attr.s
class PropCampaignCampaignSmsMessage(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Campaign.CampaignSmsMessage"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html

    Property Document:
    
    - ``p_Body``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html#cfn-pinpoint-campaign-campaignsmsmessage-body
    - ``p_EntityId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html#cfn-pinpoint-campaign-campaignsmsmessage-entityid
    - ``p_MessageType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html#cfn-pinpoint-campaign-campaignsmsmessage-messagetype
    - ``p_OriginationNumber``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html#cfn-pinpoint-campaign-campaignsmsmessage-originationnumber
    - ``p_SenderId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html#cfn-pinpoint-campaign-campaignsmsmessage-senderid
    - ``p_TemplateId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html#cfn-pinpoint-campaign-campaignsmsmessage-templateid
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Campaign.CampaignSmsMessage"
    
    p_Body: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Body"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html#cfn-pinpoint-campaign-campaignsmsmessage-body"""
    p_EntityId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "EntityId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html#cfn-pinpoint-campaign-campaignsmsmessage-entityid"""
    p_MessageType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MessageType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html#cfn-pinpoint-campaign-campaignsmsmessage-messagetype"""
    p_OriginationNumber: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "OriginationNumber"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html#cfn-pinpoint-campaign-campaignsmsmessage-originationnumber"""
    p_SenderId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SenderId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html#cfn-pinpoint-campaign-campaignsmsmessage-senderid"""
    p_TemplateId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TemplateId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html#cfn-pinpoint-campaign-campaignsmsmessage-templateid"""

@attr.s
class PropSegmentCoordinates(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Segment.Coordinates"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location-gpspoint-coordinates.html

    Property Document:
    
    - ``rp_Latitude``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location-gpspoint-coordinates.html#cfn-pinpoint-segment-segmentdimensions-location-gpspoint-coordinates-latitude
    - ``rp_Longitude``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location-gpspoint-coordinates.html#cfn-pinpoint-segment-segmentdimensions-location-gpspoint-coordinates-longitude
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Segment.Coordinates"
    
    rp_Latitude: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "Latitude"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location-gpspoint-coordinates.html#cfn-pinpoint-segment-segmentdimensions-location-gpspoint-coordinates-latitude"""
    rp_Longitude: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "Longitude"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location-gpspoint-coordinates.html#cfn-pinpoint-segment-segmentdimensions-location-gpspoint-coordinates-longitude"""

@attr.s
class PropInAppTemplateBodyConfig(Property):
    """
    AWS Object Type = "AWS::Pinpoint::InAppTemplate.BodyConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-bodyconfig.html

    Property Document:
    
    - ``p_Alignment``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-bodyconfig.html#cfn-pinpoint-inapptemplate-bodyconfig-alignment
    - ``p_Body``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-bodyconfig.html#cfn-pinpoint-inapptemplate-bodyconfig-body
    - ``p_TextColor``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-bodyconfig.html#cfn-pinpoint-inapptemplate-bodyconfig-textcolor
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::InAppTemplate.BodyConfig"
    
    p_Alignment: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Alignment"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-bodyconfig.html#cfn-pinpoint-inapptemplate-bodyconfig-alignment"""
    p_Body: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Body"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-bodyconfig.html#cfn-pinpoint-inapptemplate-bodyconfig-body"""
    p_TextColor: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TextColor"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-bodyconfig.html#cfn-pinpoint-inapptemplate-bodyconfig-textcolor"""

@attr.s
class PropCampaignSetDimension(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Campaign.SetDimension"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-setdimension.html

    Property Document:
    
    - ``p_DimensionType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-setdimension.html#cfn-pinpoint-campaign-setdimension-dimensiontype
    - ``p_Values``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-setdimension.html#cfn-pinpoint-campaign-setdimension-values
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Campaign.SetDimension"
    
    p_DimensionType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DimensionType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-setdimension.html#cfn-pinpoint-campaign-setdimension-dimensiontype"""
    p_Values: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Values"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-setdimension.html#cfn-pinpoint-campaign-setdimension-values"""

@attr.s
class PropPushTemplateAndroidPushNotificationTemplate(Property):
    """
    AWS Object Type = "AWS::Pinpoint::PushTemplate.AndroidPushNotificationTemplate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html

    Property Document:
    
    - ``p_Action``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-action
    - ``p_Body``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-body
    - ``p_ImageIconUrl``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-imageiconurl
    - ``p_ImageUrl``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-imageurl
    - ``p_SmallImageIconUrl``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-smallimageiconurl
    - ``p_Sound``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-sound
    - ``p_Title``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-title
    - ``p_Url``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-url
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::PushTemplate.AndroidPushNotificationTemplate"
    
    p_Action: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Action"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-action"""
    p_Body: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Body"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-body"""
    p_ImageIconUrl: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ImageIconUrl"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-imageiconurl"""
    p_ImageUrl: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ImageUrl"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-imageurl"""
    p_SmallImageIconUrl: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SmallImageIconUrl"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-smallimageiconurl"""
    p_Sound: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Sound"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-sound"""
    p_Title: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Title"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-title"""
    p_Url: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Url"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-url"""

@attr.s
class PropCampaignEventDimensions(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Campaign.EventDimensions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-eventdimensions.html

    Property Document:
    
    - ``p_Attributes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-eventdimensions.html#cfn-pinpoint-campaign-eventdimensions-attributes
    - ``p_EventType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-eventdimensions.html#cfn-pinpoint-campaign-eventdimensions-eventtype
    - ``p_Metrics``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-eventdimensions.html#cfn-pinpoint-campaign-eventdimensions-metrics
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Campaign.EventDimensions"
    
    p_Attributes: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Attributes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-eventdimensions.html#cfn-pinpoint-campaign-eventdimensions-attributes"""
    p_EventType: typing.Union['PropCampaignSetDimension', dict] = attr.ib(
        default=None,
        converter=PropCampaignSetDimension.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCampaignSetDimension)),
        metadata={AttrMeta.PROPERTY_NAME: "EventType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-eventdimensions.html#cfn-pinpoint-campaign-eventdimensions-eventtype"""
    p_Metrics: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Metrics"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-eventdimensions.html#cfn-pinpoint-campaign-eventdimensions-metrics"""

@attr.s
class PropSegmentSourceSegments(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Segment.SourceSegments"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups-sourcesegments.html

    Property Document:
    
    - ``rp_Id``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups-sourcesegments.html#cfn-pinpoint-segment-segmentgroups-groups-sourcesegments-id
    - ``p_Version``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups-sourcesegments.html#cfn-pinpoint-segment-segmentgroups-groups-sourcesegments-version
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Segment.SourceSegments"
    
    rp_Id: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Id"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups-sourcesegments.html#cfn-pinpoint-segment-segmentgroups-groups-sourcesegments-id"""
    p_Version: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Version"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups-sourcesegments.html#cfn-pinpoint-segment-segmentgroups-groups-sourcesegments-version"""

@attr.s
class PropSegmentGPSPoint(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Segment.GPSPoint"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location-gpspoint.html

    Property Document:
    
    - ``rp_Coordinates``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location-gpspoint.html#cfn-pinpoint-segment-segmentdimensions-location-gpspoint-coordinates
    - ``rp_RangeInKilometers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location-gpspoint.html#cfn-pinpoint-segment-segmentdimensions-location-gpspoint-rangeinkilometers
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Segment.GPSPoint"
    
    rp_Coordinates: typing.Union['PropSegmentCoordinates', dict] = attr.ib(
        default=None,
        converter=PropSegmentCoordinates.from_dict,
        validator=attr.validators.instance_of(PropSegmentCoordinates),
        metadata={AttrMeta.PROPERTY_NAME: "Coordinates"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location-gpspoint.html#cfn-pinpoint-segment-segmentdimensions-location-gpspoint-coordinates"""
    rp_RangeInKilometers: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "RangeInKilometers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location-gpspoint.html#cfn-pinpoint-segment-segmentdimensions-location-gpspoint-rangeinkilometers"""

@attr.s
class PropApplicationSettingsLimits(Property):
    """
    AWS Object Type = "AWS::Pinpoint::ApplicationSettings.Limits"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-limits.html

    Property Document:
    
    - ``p_Daily``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-limits.html#cfn-pinpoint-applicationsettings-limits-daily
    - ``p_MaximumDuration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-limits.html#cfn-pinpoint-applicationsettings-limits-maximumduration
    - ``p_MessagesPerSecond``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-limits.html#cfn-pinpoint-applicationsettings-limits-messagespersecond
    - ``p_Total``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-limits.html#cfn-pinpoint-applicationsettings-limits-total
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::ApplicationSettings.Limits"
    
    p_Daily: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Daily"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-limits.html#cfn-pinpoint-applicationsettings-limits-daily"""
    p_MaximumDuration: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MaximumDuration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-limits.html#cfn-pinpoint-applicationsettings-limits-maximumduration"""
    p_MessagesPerSecond: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MessagesPerSecond"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-limits.html#cfn-pinpoint-applicationsettings-limits-messagespersecond"""
    p_Total: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Total"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-limits.html#cfn-pinpoint-applicationsettings-limits-total"""

@attr.s
class PropCampaignOverrideButtonConfiguration(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Campaign.OverrideButtonConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-overridebuttonconfiguration.html

    Property Document:
    
    - ``p_ButtonAction``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-overridebuttonconfiguration.html#cfn-pinpoint-campaign-overridebuttonconfiguration-buttonaction
    - ``p_Link``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-overridebuttonconfiguration.html#cfn-pinpoint-campaign-overridebuttonconfiguration-link
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Campaign.OverrideButtonConfiguration"
    
    p_ButtonAction: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ButtonAction"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-overridebuttonconfiguration.html#cfn-pinpoint-campaign-overridebuttonconfiguration-buttonaction"""
    p_Link: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Link"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-overridebuttonconfiguration.html#cfn-pinpoint-campaign-overridebuttonconfiguration-link"""

@attr.s
class PropCampaignLimits(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Campaign.Limits"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html

    Property Document:
    
    - ``p_Daily``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html#cfn-pinpoint-campaign-limits-daily
    - ``p_MaximumDuration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html#cfn-pinpoint-campaign-limits-maximumduration
    - ``p_MessagesPerSecond``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html#cfn-pinpoint-campaign-limits-messagespersecond
    - ``p_Session``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html#cfn-pinpoint-campaign-limits-session
    - ``p_Total``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html#cfn-pinpoint-campaign-limits-total
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Campaign.Limits"
    
    p_Daily: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Daily"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html#cfn-pinpoint-campaign-limits-daily"""
    p_MaximumDuration: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MaximumDuration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html#cfn-pinpoint-campaign-limits-maximumduration"""
    p_MessagesPerSecond: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MessagesPerSecond"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html#cfn-pinpoint-campaign-limits-messagespersecond"""
    p_Session: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Session"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html#cfn-pinpoint-campaign-limits-session"""
    p_Total: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Total"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html#cfn-pinpoint-campaign-limits-total"""

@attr.s
class PropSegmentSetDimension(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Segment.SetDimension"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-setdimension.html

    Property Document:
    
    - ``p_DimensionType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-setdimension.html#cfn-pinpoint-segment-setdimension-dimensiontype
    - ``p_Values``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-setdimension.html#cfn-pinpoint-segment-setdimension-values
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Segment.SetDimension"
    
    p_DimensionType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DimensionType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-setdimension.html#cfn-pinpoint-segment-setdimension-dimensiontype"""
    p_Values: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Values"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-setdimension.html#cfn-pinpoint-segment-setdimension-values"""

@attr.s
class PropInAppTemplateHeaderConfig(Property):
    """
    AWS Object Type = "AWS::Pinpoint::InAppTemplate.HeaderConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-headerconfig.html

    Property Document:
    
    - ``p_Alignment``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-headerconfig.html#cfn-pinpoint-inapptemplate-headerconfig-alignment
    - ``p_Header``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-headerconfig.html#cfn-pinpoint-inapptemplate-headerconfig-header
    - ``p_TextColor``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-headerconfig.html#cfn-pinpoint-inapptemplate-headerconfig-textcolor
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::InAppTemplate.HeaderConfig"
    
    p_Alignment: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Alignment"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-headerconfig.html#cfn-pinpoint-inapptemplate-headerconfig-alignment"""
    p_Header: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Header"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-headerconfig.html#cfn-pinpoint-inapptemplate-headerconfig-header"""
    p_TextColor: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TextColor"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-headerconfig.html#cfn-pinpoint-inapptemplate-headerconfig-textcolor"""

@attr.s
class PropInAppTemplateOverrideButtonConfiguration(Property):
    """
    AWS Object Type = "AWS::Pinpoint::InAppTemplate.OverrideButtonConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-overridebuttonconfiguration.html

    Property Document:
    
    - ``p_ButtonAction``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-overridebuttonconfiguration.html#cfn-pinpoint-inapptemplate-overridebuttonconfiguration-buttonaction
    - ``p_Link``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-overridebuttonconfiguration.html#cfn-pinpoint-inapptemplate-overridebuttonconfiguration-link
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::InAppTemplate.OverrideButtonConfiguration"
    
    p_ButtonAction: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ButtonAction"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-overridebuttonconfiguration.html#cfn-pinpoint-inapptemplate-overridebuttonconfiguration-buttonaction"""
    p_Link: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Link"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-overridebuttonconfiguration.html#cfn-pinpoint-inapptemplate-overridebuttonconfiguration-link"""

@attr.s
class PropCampaignAttributeDimension(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Campaign.AttributeDimension"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-attributedimension.html

    Property Document:
    
    - ``p_AttributeType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-attributedimension.html#cfn-pinpoint-campaign-attributedimension-attributetype
    - ``p_Values``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-attributedimension.html#cfn-pinpoint-campaign-attributedimension-values
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Campaign.AttributeDimension"
    
    p_AttributeType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AttributeType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-attributedimension.html#cfn-pinpoint-campaign-attributedimension-attributetype"""
    p_Values: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Values"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-attributedimension.html#cfn-pinpoint-campaign-attributedimension-values"""

@attr.s
class PropSegmentBehavior(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Segment.Behavior"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-behavior.html

    Property Document:
    
    - ``p_Recency``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-behavior.html#cfn-pinpoint-segment-segmentdimensions-behavior-recency
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Segment.Behavior"
    
    p_Recency: typing.Union['PropSegmentRecency', dict] = attr.ib(
        default=None,
        converter=PropSegmentRecency.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropSegmentRecency)),
        metadata={AttrMeta.PROPERTY_NAME: "Recency"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-behavior.html#cfn-pinpoint-segment-segmentdimensions-behavior-recency"""

@attr.s
class PropCampaignCampaignHook(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Campaign.CampaignHook"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignhook.html

    Property Document:
    
    - ``p_LambdaFunctionName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignhook.html#cfn-pinpoint-campaign-campaignhook-lambdafunctionname
    - ``p_Mode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignhook.html#cfn-pinpoint-campaign-campaignhook-mode
    - ``p_WebUrl``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignhook.html#cfn-pinpoint-campaign-campaignhook-weburl
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Campaign.CampaignHook"
    
    p_LambdaFunctionName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LambdaFunctionName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignhook.html#cfn-pinpoint-campaign-campaignhook-lambdafunctionname"""
    p_Mode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Mode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignhook.html#cfn-pinpoint-campaign-campaignhook-mode"""
    p_WebUrl: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "WebUrl"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignhook.html#cfn-pinpoint-campaign-campaignhook-weburl"""

@attr.s
class PropPushTemplateAPNSPushNotificationTemplate(Property):
    """
    AWS Object Type = "AWS::Pinpoint::PushTemplate.APNSPushNotificationTemplate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html

    Property Document:
    
    - ``p_Action``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html#cfn-pinpoint-pushtemplate-apnspushnotificationtemplate-action
    - ``p_Body``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html#cfn-pinpoint-pushtemplate-apnspushnotificationtemplate-body
    - ``p_MediaUrl``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html#cfn-pinpoint-pushtemplate-apnspushnotificationtemplate-mediaurl
    - ``p_Sound``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html#cfn-pinpoint-pushtemplate-apnspushnotificationtemplate-sound
    - ``p_Title``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html#cfn-pinpoint-pushtemplate-apnspushnotificationtemplate-title
    - ``p_Url``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html#cfn-pinpoint-pushtemplate-apnspushnotificationtemplate-url
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::PushTemplate.APNSPushNotificationTemplate"
    
    p_Action: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Action"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html#cfn-pinpoint-pushtemplate-apnspushnotificationtemplate-action"""
    p_Body: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Body"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html#cfn-pinpoint-pushtemplate-apnspushnotificationtemplate-body"""
    p_MediaUrl: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MediaUrl"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html#cfn-pinpoint-pushtemplate-apnspushnotificationtemplate-mediaurl"""
    p_Sound: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Sound"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html#cfn-pinpoint-pushtemplate-apnspushnotificationtemplate-sound"""
    p_Title: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Title"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html#cfn-pinpoint-pushtemplate-apnspushnotificationtemplate-title"""
    p_Url: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Url"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html#cfn-pinpoint-pushtemplate-apnspushnotificationtemplate-url"""

@attr.s
class PropCampaignCampaignEmailMessage(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Campaign.CampaignEmailMessage"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignemailmessage.html

    Property Document:
    
    - ``p_Body``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignemailmessage.html#cfn-pinpoint-campaign-campaignemailmessage-body
    - ``p_FromAddress``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignemailmessage.html#cfn-pinpoint-campaign-campaignemailmessage-fromaddress
    - ``p_HtmlBody``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignemailmessage.html#cfn-pinpoint-campaign-campaignemailmessage-htmlbody
    - ``p_Title``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignemailmessage.html#cfn-pinpoint-campaign-campaignemailmessage-title
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Campaign.CampaignEmailMessage"
    
    p_Body: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Body"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignemailmessage.html#cfn-pinpoint-campaign-campaignemailmessage-body"""
    p_FromAddress: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "FromAddress"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignemailmessage.html#cfn-pinpoint-campaign-campaignemailmessage-fromaddress"""
    p_HtmlBody: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "HtmlBody"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignemailmessage.html#cfn-pinpoint-campaign-campaignemailmessage-htmlbody"""
    p_Title: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Title"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignemailmessage.html#cfn-pinpoint-campaign-campaignemailmessage-title"""

@attr.s
class PropApplicationSettingsQuietTime(Property):
    """
    AWS Object Type = "AWS::Pinpoint::ApplicationSettings.QuietTime"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-quiettime.html

    Property Document:
    
    - ``rp_End``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-quiettime.html#cfn-pinpoint-applicationsettings-quiettime-end
    - ``rp_Start``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-quiettime.html#cfn-pinpoint-applicationsettings-quiettime-start
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::ApplicationSettings.QuietTime"
    
    rp_End: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "End"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-quiettime.html#cfn-pinpoint-applicationsettings-quiettime-end"""
    rp_Start: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Start"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-quiettime.html#cfn-pinpoint-applicationsettings-quiettime-start"""

@attr.s
class PropCampaignInAppMessageButton(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Campaign.InAppMessageButton"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebutton.html

    Property Document:
    
    - ``p_Android``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebutton.html#cfn-pinpoint-campaign-inappmessagebutton-android
    - ``p_DefaultConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebutton.html#cfn-pinpoint-campaign-inappmessagebutton-defaultconfig
    - ``p_IOS``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebutton.html#cfn-pinpoint-campaign-inappmessagebutton-ios
    - ``p_Web``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebutton.html#cfn-pinpoint-campaign-inappmessagebutton-web
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Campaign.InAppMessageButton"
    
    p_Android: typing.Union['PropCampaignOverrideButtonConfiguration', dict] = attr.ib(
        default=None,
        converter=PropCampaignOverrideButtonConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCampaignOverrideButtonConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "Android"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebutton.html#cfn-pinpoint-campaign-inappmessagebutton-android"""
    p_DefaultConfig: typing.Union['PropCampaignDefaultButtonConfiguration', dict] = attr.ib(
        default=None,
        converter=PropCampaignDefaultButtonConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCampaignDefaultButtonConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebutton.html#cfn-pinpoint-campaign-inappmessagebutton-defaultconfig"""
    p_IOS: typing.Union['PropCampaignOverrideButtonConfiguration', dict] = attr.ib(
        default=None,
        converter=PropCampaignOverrideButtonConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCampaignOverrideButtonConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "IOS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebutton.html#cfn-pinpoint-campaign-inappmessagebutton-ios"""
    p_Web: typing.Union['PropCampaignOverrideButtonConfiguration', dict] = attr.ib(
        default=None,
        converter=PropCampaignOverrideButtonConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCampaignOverrideButtonConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "Web"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebutton.html#cfn-pinpoint-campaign-inappmessagebutton-web"""

@attr.s
class PropCampaignInAppMessageContent(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Campaign.InAppMessageContent"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagecontent.html

    Property Document:
    
    - ``p_BackgroundColor``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagecontent.html#cfn-pinpoint-campaign-inappmessagecontent-backgroundcolor
    - ``p_BodyConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagecontent.html#cfn-pinpoint-campaign-inappmessagecontent-bodyconfig
    - ``p_HeaderConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagecontent.html#cfn-pinpoint-campaign-inappmessagecontent-headerconfig
    - ``p_ImageUrl``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagecontent.html#cfn-pinpoint-campaign-inappmessagecontent-imageurl
    - ``p_PrimaryBtn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagecontent.html#cfn-pinpoint-campaign-inappmessagecontent-primarybtn
    - ``p_SecondaryBtn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagecontent.html#cfn-pinpoint-campaign-inappmessagecontent-secondarybtn
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Campaign.InAppMessageContent"
    
    p_BackgroundColor: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BackgroundColor"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagecontent.html#cfn-pinpoint-campaign-inappmessagecontent-backgroundcolor"""
    p_BodyConfig: typing.Union['PropCampaignInAppMessageBodyConfig', dict] = attr.ib(
        default=None,
        converter=PropCampaignInAppMessageBodyConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCampaignInAppMessageBodyConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "BodyConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagecontent.html#cfn-pinpoint-campaign-inappmessagecontent-bodyconfig"""
    p_HeaderConfig: typing.Union['PropCampaignInAppMessageHeaderConfig', dict] = attr.ib(
        default=None,
        converter=PropCampaignInAppMessageHeaderConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCampaignInAppMessageHeaderConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "HeaderConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagecontent.html#cfn-pinpoint-campaign-inappmessagecontent-headerconfig"""
    p_ImageUrl: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ImageUrl"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagecontent.html#cfn-pinpoint-campaign-inappmessagecontent-imageurl"""
    p_PrimaryBtn: typing.Union['PropCampaignInAppMessageButton', dict] = attr.ib(
        default=None,
        converter=PropCampaignInAppMessageButton.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCampaignInAppMessageButton)),
        metadata={AttrMeta.PROPERTY_NAME: "PrimaryBtn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagecontent.html#cfn-pinpoint-campaign-inappmessagecontent-primarybtn"""
    p_SecondaryBtn: typing.Union['PropCampaignInAppMessageButton', dict] = attr.ib(
        default=None,
        converter=PropCampaignInAppMessageButton.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCampaignInAppMessageButton)),
        metadata={AttrMeta.PROPERTY_NAME: "SecondaryBtn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagecontent.html#cfn-pinpoint-campaign-inappmessagecontent-secondarybtn"""

@attr.s
class PropSegmentLocation(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Segment.Location"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location.html

    Property Document:
    
    - ``p_Country``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location.html#cfn-pinpoint-segment-segmentdimensions-location-country
    - ``p_GPSPoint``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location.html#cfn-pinpoint-segment-segmentdimensions-location-gpspoint
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Segment.Location"
    
    p_Country: typing.Union['PropSegmentSetDimension', dict] = attr.ib(
        default=None,
        converter=PropSegmentSetDimension.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropSegmentSetDimension)),
        metadata={AttrMeta.PROPERTY_NAME: "Country"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location.html#cfn-pinpoint-segment-segmentdimensions-location-country"""
    p_GPSPoint: typing.Union['PropSegmentGPSPoint', dict] = attr.ib(
        default=None,
        converter=PropSegmentGPSPoint.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropSegmentGPSPoint)),
        metadata={AttrMeta.PROPERTY_NAME: "GPSPoint"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location.html#cfn-pinpoint-segment-segmentdimensions-location-gpspoint"""

@attr.s
class PropCampaignCampaignInAppMessage(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Campaign.CampaignInAppMessage"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigninappmessage.html

    Property Document:
    
    - ``p_Content``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigninappmessage.html#cfn-pinpoint-campaign-campaigninappmessage-content
    - ``p_CustomConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigninappmessage.html#cfn-pinpoint-campaign-campaigninappmessage-customconfig
    - ``p_Layout``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigninappmessage.html#cfn-pinpoint-campaign-campaigninappmessage-layout
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Campaign.CampaignInAppMessage"
    
    p_Content: typing.List[typing.Union['PropCampaignInAppMessageContent', dict]] = attr.ib(
        default=None,
        converter=PropCampaignInAppMessageContent.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropCampaignInAppMessageContent), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Content"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigninappmessage.html#cfn-pinpoint-campaign-campaigninappmessage-content"""
    p_CustomConfig: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigninappmessage.html#cfn-pinpoint-campaign-campaigninappmessage-customconfig"""
    p_Layout: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Layout"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigninappmessage.html#cfn-pinpoint-campaign-campaigninappmessage-layout"""

@attr.s
class PropCampaignCampaignEventFilter(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Campaign.CampaignEventFilter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigneventfilter.html

    Property Document:
    
    - ``p_Dimensions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigneventfilter.html#cfn-pinpoint-campaign-campaigneventfilter-dimensions
    - ``p_FilterType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigneventfilter.html#cfn-pinpoint-campaign-campaigneventfilter-filtertype
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Campaign.CampaignEventFilter"
    
    p_Dimensions: typing.Union['PropCampaignEventDimensions', dict] = attr.ib(
        default=None,
        converter=PropCampaignEventDimensions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCampaignEventDimensions)),
        metadata={AttrMeta.PROPERTY_NAME: "Dimensions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigneventfilter.html#cfn-pinpoint-campaign-campaigneventfilter-dimensions"""
    p_FilterType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "FilterType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigneventfilter.html#cfn-pinpoint-campaign-campaigneventfilter-filtertype"""

@attr.s
class PropInAppTemplateButtonConfig(Property):
    """
    AWS Object Type = "AWS::Pinpoint::InAppTemplate.ButtonConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-buttonconfig.html

    Property Document:
    
    - ``p_Android``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-buttonconfig.html#cfn-pinpoint-inapptemplate-buttonconfig-android
    - ``p_DefaultConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-buttonconfig.html#cfn-pinpoint-inapptemplate-buttonconfig-defaultconfig
    - ``p_IOS``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-buttonconfig.html#cfn-pinpoint-inapptemplate-buttonconfig-ios
    - ``p_Web``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-buttonconfig.html#cfn-pinpoint-inapptemplate-buttonconfig-web
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::InAppTemplate.ButtonConfig"
    
    p_Android: typing.Union['PropInAppTemplateOverrideButtonConfiguration', dict] = attr.ib(
        default=None,
        converter=PropInAppTemplateOverrideButtonConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropInAppTemplateOverrideButtonConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "Android"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-buttonconfig.html#cfn-pinpoint-inapptemplate-buttonconfig-android"""
    p_DefaultConfig: typing.Union['PropInAppTemplateDefaultButtonConfiguration', dict] = attr.ib(
        default=None,
        converter=PropInAppTemplateDefaultButtonConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropInAppTemplateDefaultButtonConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-buttonconfig.html#cfn-pinpoint-inapptemplate-buttonconfig-defaultconfig"""
    p_IOS: typing.Union['PropInAppTemplateOverrideButtonConfiguration', dict] = attr.ib(
        default=None,
        converter=PropInAppTemplateOverrideButtonConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropInAppTemplateOverrideButtonConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "IOS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-buttonconfig.html#cfn-pinpoint-inapptemplate-buttonconfig-ios"""
    p_Web: typing.Union['PropInAppTemplateOverrideButtonConfiguration', dict] = attr.ib(
        default=None,
        converter=PropInAppTemplateOverrideButtonConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropInAppTemplateOverrideButtonConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "Web"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-buttonconfig.html#cfn-pinpoint-inapptemplate-buttonconfig-web"""

@attr.s
class PropInAppTemplateInAppMessageContent(Property):
    """
    AWS Object Type = "AWS::Pinpoint::InAppTemplate.InAppMessageContent"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-inappmessagecontent.html

    Property Document:
    
    - ``p_BackgroundColor``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-inappmessagecontent.html#cfn-pinpoint-inapptemplate-inappmessagecontent-backgroundcolor
    - ``p_BodyConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-inappmessagecontent.html#cfn-pinpoint-inapptemplate-inappmessagecontent-bodyconfig
    - ``p_HeaderConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-inappmessagecontent.html#cfn-pinpoint-inapptemplate-inappmessagecontent-headerconfig
    - ``p_ImageUrl``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-inappmessagecontent.html#cfn-pinpoint-inapptemplate-inappmessagecontent-imageurl
    - ``p_PrimaryBtn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-inappmessagecontent.html#cfn-pinpoint-inapptemplate-inappmessagecontent-primarybtn
    - ``p_SecondaryBtn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-inappmessagecontent.html#cfn-pinpoint-inapptemplate-inappmessagecontent-secondarybtn
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::InAppTemplate.InAppMessageContent"
    
    p_BackgroundColor: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BackgroundColor"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-inappmessagecontent.html#cfn-pinpoint-inapptemplate-inappmessagecontent-backgroundcolor"""
    p_BodyConfig: typing.Union['PropInAppTemplateBodyConfig', dict] = attr.ib(
        default=None,
        converter=PropInAppTemplateBodyConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropInAppTemplateBodyConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "BodyConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-inappmessagecontent.html#cfn-pinpoint-inapptemplate-inappmessagecontent-bodyconfig"""
    p_HeaderConfig: typing.Union['PropInAppTemplateHeaderConfig', dict] = attr.ib(
        default=None,
        converter=PropInAppTemplateHeaderConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropInAppTemplateHeaderConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "HeaderConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-inappmessagecontent.html#cfn-pinpoint-inapptemplate-inappmessagecontent-headerconfig"""
    p_ImageUrl: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ImageUrl"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-inappmessagecontent.html#cfn-pinpoint-inapptemplate-inappmessagecontent-imageurl"""
    p_PrimaryBtn: typing.Union['PropInAppTemplateButtonConfig', dict] = attr.ib(
        default=None,
        converter=PropInAppTemplateButtonConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropInAppTemplateButtonConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "PrimaryBtn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-inappmessagecontent.html#cfn-pinpoint-inapptemplate-inappmessagecontent-primarybtn"""
    p_SecondaryBtn: typing.Union['PropInAppTemplateButtonConfig', dict] = attr.ib(
        default=None,
        converter=PropInAppTemplateButtonConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropInAppTemplateButtonConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "SecondaryBtn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-inapptemplate-inappmessagecontent.html#cfn-pinpoint-inapptemplate-inappmessagecontent-secondarybtn"""

@attr.s
class PropSegmentDemographic(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Segment.Demographic"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-demographic.html

    Property Document:
    
    - ``p_AppVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-demographic.html#cfn-pinpoint-segment-segmentdimensions-demographic-appversion
    - ``p_Channel``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-demographic.html#cfn-pinpoint-segment-segmentdimensions-demographic-channel
    - ``p_DeviceType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-demographic.html#cfn-pinpoint-segment-segmentdimensions-demographic-devicetype
    - ``p_Make``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-demographic.html#cfn-pinpoint-segment-segmentdimensions-demographic-make
    - ``p_Model``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-demographic.html#cfn-pinpoint-segment-segmentdimensions-demographic-model
    - ``p_Platform``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-demographic.html#cfn-pinpoint-segment-segmentdimensions-demographic-platform
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Segment.Demographic"
    
    p_AppVersion: typing.Union['PropSegmentSetDimension', dict] = attr.ib(
        default=None,
        converter=PropSegmentSetDimension.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropSegmentSetDimension)),
        metadata={AttrMeta.PROPERTY_NAME: "AppVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-demographic.html#cfn-pinpoint-segment-segmentdimensions-demographic-appversion"""
    p_Channel: typing.Union['PropSegmentSetDimension', dict] = attr.ib(
        default=None,
        converter=PropSegmentSetDimension.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropSegmentSetDimension)),
        metadata={AttrMeta.PROPERTY_NAME: "Channel"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-demographic.html#cfn-pinpoint-segment-segmentdimensions-demographic-channel"""
    p_DeviceType: typing.Union['PropSegmentSetDimension', dict] = attr.ib(
        default=None,
        converter=PropSegmentSetDimension.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropSegmentSetDimension)),
        metadata={AttrMeta.PROPERTY_NAME: "DeviceType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-demographic.html#cfn-pinpoint-segment-segmentdimensions-demographic-devicetype"""
    p_Make: typing.Union['PropSegmentSetDimension', dict] = attr.ib(
        default=None,
        converter=PropSegmentSetDimension.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropSegmentSetDimension)),
        metadata={AttrMeta.PROPERTY_NAME: "Make"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-demographic.html#cfn-pinpoint-segment-segmentdimensions-demographic-make"""
    p_Model: typing.Union['PropSegmentSetDimension', dict] = attr.ib(
        default=None,
        converter=PropSegmentSetDimension.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropSegmentSetDimension)),
        metadata={AttrMeta.PROPERTY_NAME: "Model"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-demographic.html#cfn-pinpoint-segment-segmentdimensions-demographic-model"""
    p_Platform: typing.Union['PropSegmentSetDimension', dict] = attr.ib(
        default=None,
        converter=PropSegmentSetDimension.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropSegmentSetDimension)),
        metadata={AttrMeta.PROPERTY_NAME: "Platform"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-demographic.html#cfn-pinpoint-segment-segmentdimensions-demographic-platform"""

@attr.s
class PropCampaignMessageConfiguration(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Campaign.MessageConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html

    Property Document:
    
    - ``p_ADMMessage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-admmessage
    - ``p_APNSMessage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-apnsmessage
    - ``p_BaiduMessage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-baidumessage
    - ``p_DefaultMessage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-defaultmessage
    - ``p_EmailMessage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-emailmessage
    - ``p_GCMMessage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-gcmmessage
    - ``p_InAppMessage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-inappmessage
    - ``p_SMSMessage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-smsmessage
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Campaign.MessageConfiguration"
    
    p_ADMMessage: typing.Union['PropCampaignMessage', dict] = attr.ib(
        default=None,
        converter=PropCampaignMessage.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCampaignMessage)),
        metadata={AttrMeta.PROPERTY_NAME: "ADMMessage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-admmessage"""
    p_APNSMessage: typing.Union['PropCampaignMessage', dict] = attr.ib(
        default=None,
        converter=PropCampaignMessage.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCampaignMessage)),
        metadata={AttrMeta.PROPERTY_NAME: "APNSMessage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-apnsmessage"""
    p_BaiduMessage: typing.Union['PropCampaignMessage', dict] = attr.ib(
        default=None,
        converter=PropCampaignMessage.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCampaignMessage)),
        metadata={AttrMeta.PROPERTY_NAME: "BaiduMessage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-baidumessage"""
    p_DefaultMessage: typing.Union['PropCampaignMessage', dict] = attr.ib(
        default=None,
        converter=PropCampaignMessage.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCampaignMessage)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultMessage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-defaultmessage"""
    p_EmailMessage: typing.Union['PropCampaignCampaignEmailMessage', dict] = attr.ib(
        default=None,
        converter=PropCampaignCampaignEmailMessage.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCampaignCampaignEmailMessage)),
        metadata={AttrMeta.PROPERTY_NAME: "EmailMessage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-emailmessage"""
    p_GCMMessage: typing.Union['PropCampaignMessage', dict] = attr.ib(
        default=None,
        converter=PropCampaignMessage.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCampaignMessage)),
        metadata={AttrMeta.PROPERTY_NAME: "GCMMessage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-gcmmessage"""
    p_InAppMessage: typing.Union['PropCampaignCampaignInAppMessage', dict] = attr.ib(
        default=None,
        converter=PropCampaignCampaignInAppMessage.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCampaignCampaignInAppMessage)),
        metadata={AttrMeta.PROPERTY_NAME: "InAppMessage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-inappmessage"""
    p_SMSMessage: typing.Union['PropCampaignCampaignSmsMessage', dict] = attr.ib(
        default=None,
        converter=PropCampaignCampaignSmsMessage.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCampaignCampaignSmsMessage)),
        metadata={AttrMeta.PROPERTY_NAME: "SMSMessage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-smsmessage"""

@attr.s
class PropCampaignSchedule(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Campaign.Schedule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html

    Property Document:
    
    - ``p_EndTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-endtime
    - ``p_EventFilter``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-eventfilter
    - ``p_Frequency``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-frequency
    - ``p_IsLocalTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-islocaltime
    - ``p_QuietTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-quiettime
    - ``p_StartTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-starttime
    - ``p_TimeZone``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-timezone
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Campaign.Schedule"
    
    p_EndTime: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "EndTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-endtime"""
    p_EventFilter: typing.Union['PropCampaignCampaignEventFilter', dict] = attr.ib(
        default=None,
        converter=PropCampaignCampaignEventFilter.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCampaignCampaignEventFilter)),
        metadata={AttrMeta.PROPERTY_NAME: "EventFilter"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-eventfilter"""
    p_Frequency: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Frequency"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-frequency"""
    p_IsLocalTime: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IsLocalTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-islocaltime"""
    p_QuietTime: typing.Union['PropCampaignQuietTime', dict] = attr.ib(
        default=None,
        converter=PropCampaignQuietTime.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCampaignQuietTime)),
        metadata={AttrMeta.PROPERTY_NAME: "QuietTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-quiettime"""
    p_StartTime: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "StartTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-starttime"""
    p_TimeZone: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TimeZone"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-timezone"""

@attr.s
class PropCampaignWriteTreatmentResource(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Campaign.WriteTreatmentResource"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html

    Property Document:
    
    - ``p_MessageConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html#cfn-pinpoint-campaign-writetreatmentresource-messageconfiguration
    - ``p_Schedule``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html#cfn-pinpoint-campaign-writetreatmentresource-schedule
    - ``p_SizePercent``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html#cfn-pinpoint-campaign-writetreatmentresource-sizepercent
    - ``p_TreatmentDescription``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html#cfn-pinpoint-campaign-writetreatmentresource-treatmentdescription
    - ``p_TreatmentName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html#cfn-pinpoint-campaign-writetreatmentresource-treatmentname
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Campaign.WriteTreatmentResource"
    
    p_MessageConfiguration: typing.Union['PropCampaignMessageConfiguration', dict] = attr.ib(
        default=None,
        converter=PropCampaignMessageConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCampaignMessageConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "MessageConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html#cfn-pinpoint-campaign-writetreatmentresource-messageconfiguration"""
    p_Schedule: typing.Union['PropCampaignSchedule', dict] = attr.ib(
        default=None,
        converter=PropCampaignSchedule.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCampaignSchedule)),
        metadata={AttrMeta.PROPERTY_NAME: "Schedule"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html#cfn-pinpoint-campaign-writetreatmentresource-schedule"""
    p_SizePercent: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "SizePercent"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html#cfn-pinpoint-campaign-writetreatmentresource-sizepercent"""
    p_TreatmentDescription: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TreatmentDescription"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html#cfn-pinpoint-campaign-writetreatmentresource-treatmentdescription"""
    p_TreatmentName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TreatmentName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html#cfn-pinpoint-campaign-writetreatmentresource-treatmentname"""

@attr.s
class PropSegmentSegmentDimensions(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Segment.SegmentDimensions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html

    Property Document:
    
    - ``p_Attributes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html#cfn-pinpoint-segment-segmentdimensions-attributes
    - ``p_Behavior``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html#cfn-pinpoint-segment-segmentdimensions-behavior
    - ``p_Demographic``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html#cfn-pinpoint-segment-segmentdimensions-demographic
    - ``p_Location``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html#cfn-pinpoint-segment-segmentdimensions-location
    - ``p_Metrics``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html#cfn-pinpoint-segment-segmentdimensions-metrics
    - ``p_UserAttributes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html#cfn-pinpoint-segment-segmentdimensions-userattributes
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Segment.SegmentDimensions"
    
    p_Attributes: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Attributes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html#cfn-pinpoint-segment-segmentdimensions-attributes"""
    p_Behavior: typing.Union['PropSegmentBehavior', dict] = attr.ib(
        default=None,
        converter=PropSegmentBehavior.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropSegmentBehavior)),
        metadata={AttrMeta.PROPERTY_NAME: "Behavior"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html#cfn-pinpoint-segment-segmentdimensions-behavior"""
    p_Demographic: typing.Union['PropSegmentDemographic', dict] = attr.ib(
        default=None,
        converter=PropSegmentDemographic.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropSegmentDemographic)),
        metadata={AttrMeta.PROPERTY_NAME: "Demographic"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html#cfn-pinpoint-segment-segmentdimensions-demographic"""
    p_Location: typing.Union['PropSegmentLocation', dict] = attr.ib(
        default=None,
        converter=PropSegmentLocation.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropSegmentLocation)),
        metadata={AttrMeta.PROPERTY_NAME: "Location"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html#cfn-pinpoint-segment-segmentdimensions-location"""
    p_Metrics: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Metrics"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html#cfn-pinpoint-segment-segmentdimensions-metrics"""
    p_UserAttributes: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "UserAttributes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html#cfn-pinpoint-segment-segmentdimensions-userattributes"""

@attr.s
class PropSegmentGroups(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Segment.Groups"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups.html

    Property Document:
    
    - ``p_Dimensions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups.html#cfn-pinpoint-segment-segmentgroups-groups-dimensions
    - ``p_SourceSegments``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups.html#cfn-pinpoint-segment-segmentgroups-groups-sourcesegments
    - ``p_SourceType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups.html#cfn-pinpoint-segment-segmentgroups-groups-sourcetype
    - ``p_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups.html#cfn-pinpoint-segment-segmentgroups-groups-type
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Segment.Groups"
    
    p_Dimensions: typing.List[typing.Union['PropSegmentSegmentDimensions', dict]] = attr.ib(
        default=None,
        converter=PropSegmentSegmentDimensions.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropSegmentSegmentDimensions), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Dimensions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups.html#cfn-pinpoint-segment-segmentgroups-groups-dimensions"""
    p_SourceSegments: typing.List[typing.Union['PropSegmentSourceSegments', dict]] = attr.ib(
        default=None,
        converter=PropSegmentSourceSegments.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropSegmentSourceSegments), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SourceSegments"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups.html#cfn-pinpoint-segment-segmentgroups-groups-sourcesegments"""
    p_SourceType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SourceType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups.html#cfn-pinpoint-segment-segmentgroups-groups-sourcetype"""
    p_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups.html#cfn-pinpoint-segment-segmentgroups-groups-type"""

@attr.s
class PropSegmentSegmentGroups(Property):
    """
    AWS Object Type = "AWS::Pinpoint::Segment.SegmentGroups"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups.html

    Property Document:
    
    - ``p_Groups``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups.html#cfn-pinpoint-segment-segmentgroups-groups
    - ``p_Include``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups.html#cfn-pinpoint-segment-segmentgroups-include
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Segment.SegmentGroups"
    
    p_Groups: typing.List[typing.Union['PropSegmentGroups', dict]] = attr.ib(
        default=None,
        converter=PropSegmentGroups.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropSegmentGroups), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Groups"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups.html#cfn-pinpoint-segment-segmentgroups-groups"""
    p_Include: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Include"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups.html#cfn-pinpoint-segment-segmentgroups-include"""


#--- Resource declaration ---

@attr.s
class VoiceChannel(Resource):
    """
    AWS Object Type = "AWS::Pinpoint::VoiceChannel"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-voicechannel.html

    Property Document:
    
    - ``rp_ApplicationId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-voicechannel.html#cfn-pinpoint-voicechannel-applicationid
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-voicechannel.html#cfn-pinpoint-voicechannel-enabled
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::VoiceChannel"

    
    rp_ApplicationId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-voicechannel.html#cfn-pinpoint-voicechannel-applicationid"""
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-voicechannel.html#cfn-pinpoint-voicechannel-enabled"""

    

@attr.s
class EventStream(Resource):
    """
    AWS Object Type = "AWS::Pinpoint::EventStream"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-eventstream.html

    Property Document:
    
    - ``rp_ApplicationId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-eventstream.html#cfn-pinpoint-eventstream-applicationid
    - ``rp_DestinationStreamArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-eventstream.html#cfn-pinpoint-eventstream-destinationstreamarn
    - ``rp_RoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-eventstream.html#cfn-pinpoint-eventstream-rolearn
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::EventStream"

    
    rp_ApplicationId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-eventstream.html#cfn-pinpoint-eventstream-applicationid"""
    rp_DestinationStreamArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DestinationStreamArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-eventstream.html#cfn-pinpoint-eventstream-destinationstreamarn"""
    rp_RoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-eventstream.html#cfn-pinpoint-eventstream-rolearn"""

    

@attr.s
class EmailTemplate(Resource):
    """
    AWS Object Type = "AWS::Pinpoint::EmailTemplate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html

    Property Document:
    
    - ``rp_Subject``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-subject
    - ``rp_TemplateName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-templatename
    - ``p_DefaultSubstitutions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-defaultsubstitutions
    - ``p_HtmlPart``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-htmlpart
    - ``p_TemplateDescription``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-templatedescription
    - ``p_TextPart``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-textpart
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-tags
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::EmailTemplate"

    
    rp_Subject: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Subject"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-subject"""
    rp_TemplateName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TemplateName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-templatename"""
    p_DefaultSubstitutions: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultSubstitutions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-defaultsubstitutions"""
    p_HtmlPart: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "HtmlPart"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-htmlpart"""
    p_TemplateDescription: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TemplateDescription"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-templatedescription"""
    p_TextPart: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TextPart"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-textpart"""
    p_Tags: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#aws-resource-pinpoint-emailtemplate-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class BaiduChannel(Resource):
    """
    AWS Object Type = "AWS::Pinpoint::BaiduChannel"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html

    Property Document:
    
    - ``rp_ApiKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html#cfn-pinpoint-baiduchannel-apikey
    - ``rp_ApplicationId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html#cfn-pinpoint-baiduchannel-applicationid
    - ``rp_SecretKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html#cfn-pinpoint-baiduchannel-secretkey
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html#cfn-pinpoint-baiduchannel-enabled
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::BaiduChannel"

    
    rp_ApiKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApiKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html#cfn-pinpoint-baiduchannel-apikey"""
    rp_ApplicationId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html#cfn-pinpoint-baiduchannel-applicationid"""
    rp_SecretKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SecretKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html#cfn-pinpoint-baiduchannel-secretkey"""
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html#cfn-pinpoint-baiduchannel-enabled"""

    

@attr.s
class GCMChannel(Resource):
    """
    AWS Object Type = "AWS::Pinpoint::GCMChannel"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-gcmchannel.html

    Property Document:
    
    - ``rp_ApiKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-gcmchannel.html#cfn-pinpoint-gcmchannel-apikey
    - ``rp_ApplicationId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-gcmchannel.html#cfn-pinpoint-gcmchannel-applicationid
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-gcmchannel.html#cfn-pinpoint-gcmchannel-enabled
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::GCMChannel"

    
    rp_ApiKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApiKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-gcmchannel.html#cfn-pinpoint-gcmchannel-apikey"""
    rp_ApplicationId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-gcmchannel.html#cfn-pinpoint-gcmchannel-applicationid"""
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-gcmchannel.html#cfn-pinpoint-gcmchannel-enabled"""

    

@attr.s
class APNSChannel(Resource):
    """
    AWS Object Type = "AWS::Pinpoint::APNSChannel"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html

    Property Document:
    
    - ``rp_ApplicationId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-applicationid
    - ``p_BundleId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-bundleid
    - ``p_Certificate``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-certificate
    - ``p_DefaultAuthenticationMethod``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-defaultauthenticationmethod
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-enabled
    - ``p_PrivateKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-privatekey
    - ``p_TeamId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-teamid
    - ``p_TokenKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-tokenkey
    - ``p_TokenKeyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-tokenkeyid
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::APNSChannel"

    
    rp_ApplicationId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-applicationid"""
    p_BundleId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BundleId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-bundleid"""
    p_Certificate: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Certificate"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-certificate"""
    p_DefaultAuthenticationMethod: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultAuthenticationMethod"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-defaultauthenticationmethod"""
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-enabled"""
    p_PrivateKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PrivateKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-privatekey"""
    p_TeamId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TeamId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-teamid"""
    p_TokenKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TokenKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-tokenkey"""
    p_TokenKeyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TokenKeyId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-tokenkeyid"""

    

@attr.s
class InAppTemplate(Resource):
    """
    AWS Object Type = "AWS::Pinpoint::InAppTemplate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.html

    Property Document:
    
    - ``rp_TemplateName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.html#cfn-pinpoint-inapptemplate-templatename
    - ``p_Content``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.html#cfn-pinpoint-inapptemplate-content
    - ``p_CustomConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.html#cfn-pinpoint-inapptemplate-customconfig
    - ``p_Layout``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.html#cfn-pinpoint-inapptemplate-layout
    - ``p_TemplateDescription``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.html#cfn-pinpoint-inapptemplate-templatedescription
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.html#cfn-pinpoint-inapptemplate-tags
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::InAppTemplate"

    
    rp_TemplateName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TemplateName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.html#cfn-pinpoint-inapptemplate-templatename"""
    p_Content: typing.List[typing.Union['PropInAppTemplateInAppMessageContent', dict]] = attr.ib(
        default=None,
        converter=PropInAppTemplateInAppMessageContent.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropInAppTemplateInAppMessageContent), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Content"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.html#cfn-pinpoint-inapptemplate-content"""
    p_CustomConfig: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.html#cfn-pinpoint-inapptemplate-customconfig"""
    p_Layout: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Layout"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.html#cfn-pinpoint-inapptemplate-layout"""
    p_TemplateDescription: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TemplateDescription"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.html#cfn-pinpoint-inapptemplate-templatedescription"""
    p_Tags: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.html#cfn-pinpoint-inapptemplate-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.html#aws-resource-pinpoint-inapptemplate-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class Campaign(Resource):
    """
    AWS Object Type = "AWS::Pinpoint::Campaign"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html

    Property Document:
    
    - ``rp_ApplicationId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-applicationid
    - ``rp_MessageConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-messageconfiguration
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-name
    - ``rp_Schedule``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-schedule
    - ``rp_SegmentId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-segmentid
    - ``p_AdditionalTreatments``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-additionaltreatments
    - ``p_CampaignHook``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-campaignhook
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-description
    - ``p_HoldoutPercent``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-holdoutpercent
    - ``p_IsPaused``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-ispaused
    - ``p_Limits``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-limits
    - ``p_Priority``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-priority
    - ``p_SegmentVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-segmentversion
    - ``p_TreatmentDescription``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-treatmentdescription
    - ``p_TreatmentName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-treatmentname
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-tags
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Campaign"

    
    rp_ApplicationId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-applicationid"""
    rp_MessageConfiguration: typing.Union['PropCampaignMessageConfiguration', dict] = attr.ib(
        default=None,
        converter=PropCampaignMessageConfiguration.from_dict,
        validator=attr.validators.instance_of(PropCampaignMessageConfiguration),
        metadata={AttrMeta.PROPERTY_NAME: "MessageConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-messageconfiguration"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-name"""
    rp_Schedule: typing.Union['PropCampaignSchedule', dict] = attr.ib(
        default=None,
        converter=PropCampaignSchedule.from_dict,
        validator=attr.validators.instance_of(PropCampaignSchedule),
        metadata={AttrMeta.PROPERTY_NAME: "Schedule"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-schedule"""
    rp_SegmentId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SegmentId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-segmentid"""
    p_AdditionalTreatments: typing.List[typing.Union['PropCampaignWriteTreatmentResource', dict]] = attr.ib(
        default=None,
        converter=PropCampaignWriteTreatmentResource.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropCampaignWriteTreatmentResource), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AdditionalTreatments"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-additionaltreatments"""
    p_CampaignHook: typing.Union['PropCampaignCampaignHook', dict] = attr.ib(
        default=None,
        converter=PropCampaignCampaignHook.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCampaignCampaignHook)),
        metadata={AttrMeta.PROPERTY_NAME: "CampaignHook"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-campaignhook"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-description"""
    p_HoldoutPercent: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "HoldoutPercent"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-holdoutpercent"""
    p_IsPaused: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IsPaused"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-ispaused"""
    p_Limits: typing.Union['PropCampaignLimits', dict] = attr.ib(
        default=None,
        converter=PropCampaignLimits.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCampaignLimits)),
        metadata={AttrMeta.PROPERTY_NAME: "Limits"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-limits"""
    p_Priority: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Priority"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-priority"""
    p_SegmentVersion: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "SegmentVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-segmentversion"""
    p_TreatmentDescription: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TreatmentDescription"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-treatmentdescription"""
    p_TreatmentName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TreatmentName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-treatmentname"""
    p_Tags: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-tags"""

    
    @property
    def rv_CampaignId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#aws-resource-pinpoint-campaign-return-values"""
        return GetAtt(resource=self, attr_name="CampaignId")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#aws-resource-pinpoint-campaign-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class APNSVoipSandboxChannel(Resource):
    """
    AWS Object Type = "AWS::Pinpoint::APNSVoipSandboxChannel"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html

    Property Document:
    
    - ``rp_ApplicationId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-applicationid
    - ``p_BundleId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-bundleid
    - ``p_Certificate``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-certificate
    - ``p_DefaultAuthenticationMethod``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-defaultauthenticationmethod
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-enabled
    - ``p_PrivateKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-privatekey
    - ``p_TeamId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-teamid
    - ``p_TokenKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-tokenkey
    - ``p_TokenKeyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-tokenkeyid
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::APNSVoipSandboxChannel"

    
    rp_ApplicationId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-applicationid"""
    p_BundleId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BundleId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-bundleid"""
    p_Certificate: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Certificate"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-certificate"""
    p_DefaultAuthenticationMethod: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultAuthenticationMethod"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-defaultauthenticationmethod"""
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-enabled"""
    p_PrivateKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PrivateKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-privatekey"""
    p_TeamId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TeamId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-teamid"""
    p_TokenKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TokenKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-tokenkey"""
    p_TokenKeyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TokenKeyId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-tokenkeyid"""

    

@attr.s
class APNSVoipChannel(Resource):
    """
    AWS Object Type = "AWS::Pinpoint::APNSVoipChannel"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html

    Property Document:
    
    - ``rp_ApplicationId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-applicationid
    - ``p_BundleId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-bundleid
    - ``p_Certificate``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-certificate
    - ``p_DefaultAuthenticationMethod``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-defaultauthenticationmethod
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-enabled
    - ``p_PrivateKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-privatekey
    - ``p_TeamId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-teamid
    - ``p_TokenKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-tokenkey
    - ``p_TokenKeyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-tokenkeyid
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::APNSVoipChannel"

    
    rp_ApplicationId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-applicationid"""
    p_BundleId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BundleId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-bundleid"""
    p_Certificate: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Certificate"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-certificate"""
    p_DefaultAuthenticationMethod: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultAuthenticationMethod"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-defaultauthenticationmethod"""
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-enabled"""
    p_PrivateKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PrivateKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-privatekey"""
    p_TeamId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TeamId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-teamid"""
    p_TokenKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TokenKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-tokenkey"""
    p_TokenKeyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TokenKeyId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-tokenkeyid"""

    

@attr.s
class EmailChannel(Resource):
    """
    AWS Object Type = "AWS::Pinpoint::EmailChannel"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html

    Property Document:
    
    - ``rp_ApplicationId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-applicationid
    - ``rp_FromAddress``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-fromaddress
    - ``rp_Identity``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-identity
    - ``p_ConfigurationSet``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-configurationset
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-enabled
    - ``p_RoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-rolearn
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::EmailChannel"

    
    rp_ApplicationId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-applicationid"""
    rp_FromAddress: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "FromAddress"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-fromaddress"""
    rp_Identity: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Identity"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-identity"""
    p_ConfigurationSet: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ConfigurationSet"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-configurationset"""
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-enabled"""
    p_RoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-rolearn"""

    

@attr.s
class SMSChannel(Resource):
    """
    AWS Object Type = "AWS::Pinpoint::SMSChannel"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html

    Property Document:
    
    - ``rp_ApplicationId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html#cfn-pinpoint-smschannel-applicationid
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html#cfn-pinpoint-smschannel-enabled
    - ``p_SenderId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html#cfn-pinpoint-smschannel-senderid
    - ``p_ShortCode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html#cfn-pinpoint-smschannel-shortcode
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::SMSChannel"

    
    rp_ApplicationId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html#cfn-pinpoint-smschannel-applicationid"""
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html#cfn-pinpoint-smschannel-enabled"""
    p_SenderId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SenderId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html#cfn-pinpoint-smschannel-senderid"""
    p_ShortCode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ShortCode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html#cfn-pinpoint-smschannel-shortcode"""

    

@attr.s
class SmsTemplate(Resource):
    """
    AWS Object Type = "AWS::Pinpoint::SmsTemplate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html

    Property Document:
    
    - ``rp_Body``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#cfn-pinpoint-smstemplate-body
    - ``rp_TemplateName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#cfn-pinpoint-smstemplate-templatename
    - ``p_DefaultSubstitutions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#cfn-pinpoint-smstemplate-defaultsubstitutions
    - ``p_TemplateDescription``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#cfn-pinpoint-smstemplate-templatedescription
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#cfn-pinpoint-smstemplate-tags
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::SmsTemplate"

    
    rp_Body: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Body"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#cfn-pinpoint-smstemplate-body"""
    rp_TemplateName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TemplateName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#cfn-pinpoint-smstemplate-templatename"""
    p_DefaultSubstitutions: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultSubstitutions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#cfn-pinpoint-smstemplate-defaultsubstitutions"""
    p_TemplateDescription: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TemplateDescription"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#cfn-pinpoint-smstemplate-templatedescription"""
    p_Tags: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#cfn-pinpoint-smstemplate-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#aws-resource-pinpoint-smstemplate-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class Segment(Resource):
    """
    AWS Object Type = "AWS::Pinpoint::Segment"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html

    Property Document:
    
    - ``rp_ApplicationId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#cfn-pinpoint-segment-applicationid
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#cfn-pinpoint-segment-name
    - ``p_Dimensions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#cfn-pinpoint-segment-dimensions
    - ``p_SegmentGroups``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#cfn-pinpoint-segment-segmentgroups
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#cfn-pinpoint-segment-tags
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::Segment"

    
    rp_ApplicationId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#cfn-pinpoint-segment-applicationid"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#cfn-pinpoint-segment-name"""
    p_Dimensions: typing.Union['PropSegmentSegmentDimensions', dict] = attr.ib(
        default=None,
        converter=PropSegmentSegmentDimensions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropSegmentSegmentDimensions)),
        metadata={AttrMeta.PROPERTY_NAME: "Dimensions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#cfn-pinpoint-segment-dimensions"""
    p_SegmentGroups: typing.Union['PropSegmentSegmentGroups', dict] = attr.ib(
        default=None,
        converter=PropSegmentSegmentGroups.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropSegmentSegmentGroups)),
        metadata={AttrMeta.PROPERTY_NAME: "SegmentGroups"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#cfn-pinpoint-segment-segmentgroups"""
    p_Tags: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#cfn-pinpoint-segment-tags"""

    
    @property
    def rv_SegmentId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#aws-resource-pinpoint-segment-return-values"""
        return GetAtt(resource=self, attr_name="SegmentId")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#aws-resource-pinpoint-segment-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class APNSSandboxChannel(Resource):
    """
    AWS Object Type = "AWS::Pinpoint::APNSSandboxChannel"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html

    Property Document:
    
    - ``rp_ApplicationId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-applicationid
    - ``p_BundleId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-bundleid
    - ``p_Certificate``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-certificate
    - ``p_DefaultAuthenticationMethod``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-defaultauthenticationmethod
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-enabled
    - ``p_PrivateKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-privatekey
    - ``p_TeamId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-teamid
    - ``p_TokenKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-tokenkey
    - ``p_TokenKeyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-tokenkeyid
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::APNSSandboxChannel"

    
    rp_ApplicationId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-applicationid"""
    p_BundleId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BundleId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-bundleid"""
    p_Certificate: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Certificate"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-certificate"""
    p_DefaultAuthenticationMethod: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultAuthenticationMethod"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-defaultauthenticationmethod"""
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-enabled"""
    p_PrivateKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PrivateKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-privatekey"""
    p_TeamId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TeamId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-teamid"""
    p_TokenKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TokenKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-tokenkey"""
    p_TokenKeyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TokenKeyId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-tokenkeyid"""

    

@attr.s
class ADMChannel(Resource):
    """
    AWS Object Type = "AWS::Pinpoint::ADMChannel"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html

    Property Document:
    
    - ``rp_ApplicationId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html#cfn-pinpoint-admchannel-applicationid
    - ``rp_ClientId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html#cfn-pinpoint-admchannel-clientid
    - ``rp_ClientSecret``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html#cfn-pinpoint-admchannel-clientsecret
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html#cfn-pinpoint-admchannel-enabled
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::ADMChannel"

    
    rp_ApplicationId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html#cfn-pinpoint-admchannel-applicationid"""
    rp_ClientId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ClientId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html#cfn-pinpoint-admchannel-clientid"""
    rp_ClientSecret: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ClientSecret"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html#cfn-pinpoint-admchannel-clientsecret"""
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html#cfn-pinpoint-admchannel-enabled"""

    

@attr.s
class ApplicationSettings(Resource):
    """
    AWS Object Type = "AWS::Pinpoint::ApplicationSettings"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html

    Property Document:
    
    - ``rp_ApplicationId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html#cfn-pinpoint-applicationsettings-applicationid
    - ``p_CampaignHook``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html#cfn-pinpoint-applicationsettings-campaignhook
    - ``p_CloudWatchMetricsEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html#cfn-pinpoint-applicationsettings-cloudwatchmetricsenabled
    - ``p_Limits``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html#cfn-pinpoint-applicationsettings-limits
    - ``p_QuietTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html#cfn-pinpoint-applicationsettings-quiettime
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::ApplicationSettings"

    
    rp_ApplicationId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html#cfn-pinpoint-applicationsettings-applicationid"""
    p_CampaignHook: typing.Union['PropApplicationSettingsCampaignHook', dict] = attr.ib(
        default=None,
        converter=PropApplicationSettingsCampaignHook.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationSettingsCampaignHook)),
        metadata={AttrMeta.PROPERTY_NAME: "CampaignHook"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html#cfn-pinpoint-applicationsettings-campaignhook"""
    p_CloudWatchMetricsEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "CloudWatchMetricsEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html#cfn-pinpoint-applicationsettings-cloudwatchmetricsenabled"""
    p_Limits: typing.Union['PropApplicationSettingsLimits', dict] = attr.ib(
        default=None,
        converter=PropApplicationSettingsLimits.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationSettingsLimits)),
        metadata={AttrMeta.PROPERTY_NAME: "Limits"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html#cfn-pinpoint-applicationsettings-limits"""
    p_QuietTime: typing.Union['PropApplicationSettingsQuietTime', dict] = attr.ib(
        default=None,
        converter=PropApplicationSettingsQuietTime.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationSettingsQuietTime)),
        metadata={AttrMeta.PROPERTY_NAME: "QuietTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html#cfn-pinpoint-applicationsettings-quiettime"""

    

@attr.s
class PushTemplate(Resource):
    """
    AWS Object Type = "AWS::Pinpoint::PushTemplate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html

    Property Document:
    
    - ``rp_TemplateName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-templatename
    - ``p_ADM``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-adm
    - ``p_APNS``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-apns
    - ``p_Baidu``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-baidu
    - ``p_Default``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-default
    - ``p_DefaultSubstitutions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-defaultsubstitutions
    - ``p_GCM``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-gcm
    - ``p_TemplateDescription``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-templatedescription
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-tags
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::PushTemplate"

    
    rp_TemplateName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TemplateName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-templatename"""
    p_ADM: typing.Union['PropPushTemplateAndroidPushNotificationTemplate', dict] = attr.ib(
        default=None,
        converter=PropPushTemplateAndroidPushNotificationTemplate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropPushTemplateAndroidPushNotificationTemplate)),
        metadata={AttrMeta.PROPERTY_NAME: "ADM"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-adm"""
    p_APNS: typing.Union['PropPushTemplateAPNSPushNotificationTemplate', dict] = attr.ib(
        default=None,
        converter=PropPushTemplateAPNSPushNotificationTemplate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropPushTemplateAPNSPushNotificationTemplate)),
        metadata={AttrMeta.PROPERTY_NAME: "APNS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-apns"""
    p_Baidu: typing.Union['PropPushTemplateAndroidPushNotificationTemplate', dict] = attr.ib(
        default=None,
        converter=PropPushTemplateAndroidPushNotificationTemplate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropPushTemplateAndroidPushNotificationTemplate)),
        metadata={AttrMeta.PROPERTY_NAME: "Baidu"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-baidu"""
    p_Default: typing.Union['PropPushTemplateDefaultPushNotificationTemplate', dict] = attr.ib(
        default=None,
        converter=PropPushTemplateDefaultPushNotificationTemplate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropPushTemplateDefaultPushNotificationTemplate)),
        metadata={AttrMeta.PROPERTY_NAME: "Default"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-default"""
    p_DefaultSubstitutions: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultSubstitutions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-defaultsubstitutions"""
    p_GCM: typing.Union['PropPushTemplateAndroidPushNotificationTemplate', dict] = attr.ib(
        default=None,
        converter=PropPushTemplateAndroidPushNotificationTemplate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropPushTemplateAndroidPushNotificationTemplate)),
        metadata={AttrMeta.PROPERTY_NAME: "GCM"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-gcm"""
    p_TemplateDescription: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TemplateDescription"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-templatedescription"""
    p_Tags: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#aws-resource-pinpoint-pushtemplate-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class App(Resource):
    """
    AWS Object Type = "AWS::Pinpoint::App"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-app.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-app.html#cfn-pinpoint-app-name
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-app.html#cfn-pinpoint-app-tags
    """
    AWS_OBJECT_TYPE = "AWS::Pinpoint::App"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-app.html#cfn-pinpoint-app-name"""
    p_Tags: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-app.html#cfn-pinpoint-app-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-app.html#aws-resource-pinpoint-app-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
