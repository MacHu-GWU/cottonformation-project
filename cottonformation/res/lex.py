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
class PropBotSlotValueRegexFilter(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.SlotValueRegexFilter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueregexfilter.html

    Property Document:
    
    - ``rp_Pattern``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueregexfilter.html#cfn-lex-bot-slotvalueregexfilter-pattern
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.SlotValueRegexFilter"
    
    rp_Pattern: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Pattern"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueregexfilter.html#cfn-lex-bot-slotvalueregexfilter-pattern"""

@attr.s
class PropBotInputContext(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.InputContext"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-inputcontext.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-inputcontext.html#cfn-lex-bot-inputcontext-name
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.InputContext"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-inputcontext.html#cfn-lex-bot-inputcontext-name"""

@attr.s
class PropBotVoiceSettings(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.VoiceSettings"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-voicesettings.html

    Property Document:
    
    - ``rp_VoiceId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-voicesettings.html#cfn-lex-bot-voicesettings-voiceid
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.VoiceSettings"
    
    rp_VoiceId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "VoiceId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-voicesettings.html#cfn-lex-bot-voicesettings-voiceid"""

@attr.s
class PropBotVersionBotVersionLocaleDetails(Property):
    """
    AWS Object Type = "AWS::Lex::BotVersion.BotVersionLocaleDetails"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botversion-botversionlocaledetails.html

    Property Document:
    
    - ``rp_SourceBotVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botversion-botversionlocaledetails.html#cfn-lex-botversion-botversionlocaledetails-sourcebotversion
    """
    AWS_OBJECT_TYPE = "AWS::Lex::BotVersion.BotVersionLocaleDetails"
    
    rp_SourceBotVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SourceBotVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botversion-botversionlocaledetails.html#cfn-lex-botversion-botversionlocaledetails-sourcebotversion"""

@attr.s
class PropBotMultipleValuesSetting(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.MultipleValuesSetting"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-multiplevaluessetting.html

    Property Document:
    
    - ``p_AllowMultipleValues``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-multiplevaluessetting.html#cfn-lex-bot-multiplevaluessetting-allowmultiplevalues
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.MultipleValuesSetting"
    
    p_AllowMultipleValues: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "AllowMultipleValues"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-multiplevaluessetting.html#cfn-lex-bot-multiplevaluessetting-allowmultiplevalues"""

@attr.s
class PropBotDialogCodeHookSetting(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.DialogCodeHookSetting"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogcodehooksetting.html

    Property Document:
    
    - ``rp_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogcodehooksetting.html#cfn-lex-bot-dialogcodehooksetting-enabled
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.DialogCodeHookSetting"
    
    rp_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogcodehooksetting.html#cfn-lex-bot-dialogcodehooksetting-enabled"""

@attr.s
class PropBotObfuscationSetting(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.ObfuscationSetting"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-obfuscationsetting.html

    Property Document:
    
    - ``rp_ObfuscationSettingType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-obfuscationsetting.html#cfn-lex-bot-obfuscationsetting-obfuscationsettingtype
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.ObfuscationSetting"
    
    rp_ObfuscationSettingType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ObfuscationSettingType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-obfuscationsetting.html#cfn-lex-bot-obfuscationsetting-obfuscationsettingtype"""

@attr.s
class PropBotAliasCloudWatchLogGroupLogDestination(Property):
    """
    AWS Object Type = "AWS::Lex::BotAlias.CloudWatchLogGroupLogDestination"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-cloudwatchloggrouplogdestination.html

    Property Document:
    
    - ``rp_CloudWatchLogGroupArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-cloudwatchloggrouplogdestination.html#cfn-lex-botalias-cloudwatchloggrouplogdestination-cloudwatchloggrouparn
    - ``rp_LogPrefix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-cloudwatchloggrouplogdestination.html#cfn-lex-botalias-cloudwatchloggrouplogdestination-logprefix
    """
    AWS_OBJECT_TYPE = "AWS::Lex::BotAlias.CloudWatchLogGroupLogDestination"
    
    rp_CloudWatchLogGroupArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "CloudWatchLogGroupArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-cloudwatchloggrouplogdestination.html#cfn-lex-botalias-cloudwatchloggrouplogdestination-cloudwatchloggrouparn"""
    rp_LogPrefix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "LogPrefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-cloudwatchloggrouplogdestination.html#cfn-lex-botalias-cloudwatchloggrouplogdestination-logprefix"""

@attr.s
class PropBotS3Location(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.S3Location"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-s3location.html

    Property Document:
    
    - ``rp_S3Bucket``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-s3location.html#cfn-lex-bot-s3location-s3bucket
    - ``rp_S3ObjectKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-s3location.html#cfn-lex-bot-s3location-s3objectkey
    - ``p_S3ObjectVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-s3location.html#cfn-lex-bot-s3location-s3objectversion
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.S3Location"
    
    rp_S3Bucket: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "S3Bucket"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-s3location.html#cfn-lex-bot-s3location-s3bucket"""
    rp_S3ObjectKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "S3ObjectKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-s3location.html#cfn-lex-bot-s3location-s3objectkey"""
    p_S3ObjectVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "S3ObjectVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-s3location.html#cfn-lex-bot-s3location-s3objectversion"""

@attr.s
class PropBotSlotDefaultValue(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.SlotDefaultValue"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotdefaultvalue.html

    Property Document:
    
    - ``rp_DefaultValue``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotdefaultvalue.html#cfn-lex-bot-slotdefaultvalue-defaultvalue
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.SlotDefaultValue"
    
    rp_DefaultValue: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultValue"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotdefaultvalue.html#cfn-lex-bot-slotdefaultvalue-defaultvalue"""

@attr.s
class PropBotSlotPriority(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.SlotPriority"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotpriority.html

    Property Document:
    
    - ``rp_Priority``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotpriority.html#cfn-lex-bot-slotpriority-priority
    - ``rp_SlotName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotpriority.html#cfn-lex-bot-slotpriority-slotname
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.SlotPriority"
    
    rp_Priority: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Priority"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotpriority.html#cfn-lex-bot-slotpriority-priority"""
    rp_SlotName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SlotName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotpriority.html#cfn-lex-bot-slotpriority-slotname"""

@attr.s
class PropBotAliasLambdaCodeHook(Property):
    """
    AWS Object Type = "AWS::Lex::BotAlias.LambdaCodeHook"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-lambdacodehook.html

    Property Document:
    
    - ``rp_CodeHookInterfaceVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-lambdacodehook.html#cfn-lex-botalias-lambdacodehook-codehookinterfaceversion
    - ``rp_LambdaArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-lambdacodehook.html#cfn-lex-botalias-lambdacodehook-lambdaarn
    """
    AWS_OBJECT_TYPE = "AWS::Lex::BotAlias.LambdaCodeHook"
    
    rp_CodeHookInterfaceVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "CodeHookInterfaceVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-lambdacodehook.html#cfn-lex-botalias-lambdacodehook-codehookinterfaceversion"""
    rp_LambdaArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "LambdaArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-lambdacodehook.html#cfn-lex-botalias-lambdacodehook-lambdaarn"""

@attr.s
class PropBotVersionBotVersionLocaleSpecification(Property):
    """
    AWS Object Type = "AWS::Lex::BotVersion.BotVersionLocaleSpecification"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botversion-botversionlocalespecification.html

    Property Document:
    
    - ``rp_BotVersionLocaleDetails``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botversion-botversionlocalespecification.html#cfn-lex-botversion-botversionlocalespecification-botversionlocaledetails
    - ``rp_LocaleId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botversion-botversionlocalespecification.html#cfn-lex-botversion-botversionlocalespecification-localeid
    """
    AWS_OBJECT_TYPE = "AWS::Lex::BotVersion.BotVersionLocaleSpecification"
    
    rp_BotVersionLocaleDetails: typing.Union['PropBotVersionBotVersionLocaleDetails', dict] = attr.ib(
        default=None,
        converter=PropBotVersionBotVersionLocaleDetails.from_dict,
        validator=attr.validators.instance_of(PropBotVersionBotVersionLocaleDetails),
        metadata={AttrMeta.PROPERTY_NAME: "BotVersionLocaleDetails"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botversion-botversionlocalespecification.html#cfn-lex-botversion-botversionlocalespecification-botversionlocaledetails"""
    rp_LocaleId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "LocaleId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botversion-botversionlocalespecification.html#cfn-lex-botversion-botversionlocalespecification-localeid"""

@attr.s
class PropBotSlotValueSelectionSetting(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.SlotValueSelectionSetting"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueselectionsetting.html

    Property Document:
    
    - ``rp_ResolutionStrategy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueselectionsetting.html#cfn-lex-bot-slotvalueselectionsetting-resolutionstrategy
    - ``p_RegexFilter``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueselectionsetting.html#cfn-lex-bot-slotvalueselectionsetting-regexfilter
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.SlotValueSelectionSetting"
    
    rp_ResolutionStrategy: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResolutionStrategy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueselectionsetting.html#cfn-lex-bot-slotvalueselectionsetting-resolutionstrategy"""
    p_RegexFilter: typing.Union['PropBotSlotValueRegexFilter', dict] = attr.ib(
        default=None,
        converter=PropBotSlotValueRegexFilter.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotSlotValueRegexFilter)),
        metadata={AttrMeta.PROPERTY_NAME: "RegexFilter"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueselectionsetting.html#cfn-lex-bot-slotvalueselectionsetting-regexfilter"""

@attr.s
class PropResourcePolicyPolicy(Property):
    """
    AWS Object Type = "AWS::Lex::ResourcePolicy.Policy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-resourcepolicy-policy.html

    Property Document:
    
    """
    AWS_OBJECT_TYPE = "AWS::Lex::ResourcePolicy.Policy"
    

@attr.s
class PropBotButton(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.Button"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-button.html

    Property Document:
    
    - ``rp_Text``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-button.html#cfn-lex-bot-button-text
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-button.html#cfn-lex-bot-button-value
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.Button"
    
    rp_Text: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Text"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-button.html#cfn-lex-bot-button-text"""
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-button.html#cfn-lex-bot-button-value"""

@attr.s
class PropBotPlainTextMessage(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.PlainTextMessage"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-plaintextmessage.html

    Property Document:
    
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-plaintextmessage.html#cfn-lex-bot-plaintextmessage-value
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.PlainTextMessage"
    
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-plaintextmessage.html#cfn-lex-bot-plaintextmessage-value"""

@attr.s
class PropBotSSMLMessage(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.SSMLMessage"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-ssmlmessage.html

    Property Document:
    
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-ssmlmessage.html#cfn-lex-bot-ssmlmessage-value
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.SSMLMessage"
    
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-ssmlmessage.html#cfn-lex-bot-ssmlmessage-value"""

@attr.s
class PropBotKendraConfiguration(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.KendraConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-kendraconfiguration.html

    Property Document:
    
    - ``rp_KendraIndex``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-kendraconfiguration.html#cfn-lex-bot-kendraconfiguration-kendraindex
    - ``p_QueryFilterString``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-kendraconfiguration.html#cfn-lex-bot-kendraconfiguration-queryfilterstring
    - ``p_QueryFilterStringEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-kendraconfiguration.html#cfn-lex-bot-kendraconfiguration-queryfilterstringenabled
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.KendraConfiguration"
    
    rp_KendraIndex: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "KendraIndex"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-kendraconfiguration.html#cfn-lex-bot-kendraconfiguration-kendraindex"""
    p_QueryFilterString: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "QueryFilterString"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-kendraconfiguration.html#cfn-lex-bot-kendraconfiguration-queryfilterstring"""
    p_QueryFilterStringEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "QueryFilterStringEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-kendraconfiguration.html#cfn-lex-bot-kendraconfiguration-queryfilterstringenabled"""

@attr.s
class PropBotGrammarSlotTypeSource(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.GrammarSlotTypeSource"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-grammarslottypesource.html

    Property Document:
    
    - ``rp_S3BucketName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-grammarslottypesource.html#cfn-lex-bot-grammarslottypesource-s3bucketname
    - ``rp_S3ObjectKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-grammarslottypesource.html#cfn-lex-bot-grammarslottypesource-s3objectkey
    - ``p_KmsKeyArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-grammarslottypesource.html#cfn-lex-bot-grammarslottypesource-kmskeyarn
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.GrammarSlotTypeSource"
    
    rp_S3BucketName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "S3BucketName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-grammarslottypesource.html#cfn-lex-bot-grammarslottypesource-s3bucketname"""
    rp_S3ObjectKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "S3ObjectKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-grammarslottypesource.html#cfn-lex-bot-grammarslottypesource-s3objectkey"""
    p_KmsKeyArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "KmsKeyArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-grammarslottypesource.html#cfn-lex-bot-grammarslottypesource-kmskeyarn"""

@attr.s
class PropBotAliasTextLogDestination(Property):
    """
    AWS Object Type = "AWS::Lex::BotAlias.TextLogDestination"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-textlogdestination.html

    Property Document:
    
    - ``rp_CloudWatch``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-textlogdestination.html#cfn-lex-botalias-textlogdestination-cloudwatch
    """
    AWS_OBJECT_TYPE = "AWS::Lex::BotAlias.TextLogDestination"
    
    rp_CloudWatch: typing.Union['PropBotAliasCloudWatchLogGroupLogDestination', dict] = attr.ib(
        default=None,
        converter=PropBotAliasCloudWatchLogGroupLogDestination.from_dict,
        validator=attr.validators.instance_of(PropBotAliasCloudWatchLogGroupLogDestination),
        metadata={AttrMeta.PROPERTY_NAME: "CloudWatch"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-textlogdestination.html#cfn-lex-botalias-textlogdestination-cloudwatch"""

@attr.s
class PropBotSampleUtterance(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.SampleUtterance"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-sampleutterance.html

    Property Document:
    
    - ``rp_Utterance``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-sampleutterance.html#cfn-lex-bot-sampleutterance-utterance
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.SampleUtterance"
    
    rp_Utterance: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Utterance"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-sampleutterance.html#cfn-lex-bot-sampleutterance-utterance"""

@attr.s
class PropBotGrammarSlotTypeSetting(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.GrammarSlotTypeSetting"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-grammarslottypesetting.html

    Property Document:
    
    - ``p_Source``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-grammarslottypesetting.html#cfn-lex-bot-grammarslottypesetting-source
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.GrammarSlotTypeSetting"
    
    p_Source: typing.Union['PropBotGrammarSlotTypeSource', dict] = attr.ib(
        default=None,
        converter=PropBotGrammarSlotTypeSource.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotGrammarSlotTypeSource)),
        metadata={AttrMeta.PROPERTY_NAME: "Source"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-grammarslottypesetting.html#cfn-lex-bot-grammarslottypesetting-source"""

@attr.s
class PropBotAliasS3BucketLogDestination(Property):
    """
    AWS Object Type = "AWS::Lex::BotAlias.S3BucketLogDestination"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-s3bucketlogdestination.html

    Property Document:
    
    - ``rp_LogPrefix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-s3bucketlogdestination.html#cfn-lex-botalias-s3bucketlogdestination-logprefix
    - ``rp_S3BucketArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-s3bucketlogdestination.html#cfn-lex-botalias-s3bucketlogdestination-s3bucketarn
    - ``p_KmsKeyArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-s3bucketlogdestination.html#cfn-lex-botalias-s3bucketlogdestination-kmskeyarn
    """
    AWS_OBJECT_TYPE = "AWS::Lex::BotAlias.S3BucketLogDestination"
    
    rp_LogPrefix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "LogPrefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-s3bucketlogdestination.html#cfn-lex-botalias-s3bucketlogdestination-logprefix"""
    rp_S3BucketArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "S3BucketArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-s3bucketlogdestination.html#cfn-lex-botalias-s3bucketlogdestination-s3bucketarn"""
    p_KmsKeyArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "KmsKeyArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-s3bucketlogdestination.html#cfn-lex-botalias-s3bucketlogdestination-kmskeyarn"""

@attr.s
class PropBotOutputContext(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.OutputContext"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-outputcontext.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-outputcontext.html#cfn-lex-bot-outputcontext-name
    - ``rp_TimeToLiveInSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-outputcontext.html#cfn-lex-bot-outputcontext-timetoliveinseconds
    - ``rp_TurnsToLive``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-outputcontext.html#cfn-lex-bot-outputcontext-turnstolive
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.OutputContext"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-outputcontext.html#cfn-lex-bot-outputcontext-name"""
    rp_TimeToLiveInSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "TimeToLiveInSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-outputcontext.html#cfn-lex-bot-outputcontext-timetoliveinseconds"""
    rp_TurnsToLive: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "TurnsToLive"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-outputcontext.html#cfn-lex-bot-outputcontext-turnstolive"""

@attr.s
class PropBotCustomPayload(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.CustomPayload"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-custompayload.html

    Property Document:
    
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-custompayload.html#cfn-lex-bot-custompayload-value
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.CustomPayload"
    
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-custompayload.html#cfn-lex-bot-custompayload-value"""

@attr.s
class PropBotSampleValue(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.SampleValue"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-samplevalue.html

    Property Document:
    
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-samplevalue.html#cfn-lex-bot-samplevalue-value
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.SampleValue"
    
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-samplevalue.html#cfn-lex-bot-samplevalue-value"""

@attr.s
class PropBotAliasCodeHookSpecification(Property):
    """
    AWS Object Type = "AWS::Lex::BotAlias.CodeHookSpecification"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-codehookspecification.html

    Property Document:
    
    - ``rp_LambdaCodeHook``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-codehookspecification.html#cfn-lex-botalias-codehookspecification-lambdacodehook
    """
    AWS_OBJECT_TYPE = "AWS::Lex::BotAlias.CodeHookSpecification"
    
    rp_LambdaCodeHook: typing.Union['PropBotAliasLambdaCodeHook', dict] = attr.ib(
        default=None,
        converter=PropBotAliasLambdaCodeHook.from_dict,
        validator=attr.validators.instance_of(PropBotAliasLambdaCodeHook),
        metadata={AttrMeta.PROPERTY_NAME: "LambdaCodeHook"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-codehookspecification.html#cfn-lex-botalias-codehookspecification-lambdacodehook"""

@attr.s
class PropBotAliasBotAliasLocaleSettings(Property):
    """
    AWS Object Type = "AWS::Lex::BotAlias.BotAliasLocaleSettings"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-botaliaslocalesettings.html

    Property Document:
    
    - ``rp_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-botaliaslocalesettings.html#cfn-lex-botalias-botaliaslocalesettings-enabled
    - ``p_CodeHookSpecification``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-botaliaslocalesettings.html#cfn-lex-botalias-botaliaslocalesettings-codehookspecification
    """
    AWS_OBJECT_TYPE = "AWS::Lex::BotAlias.BotAliasLocaleSettings"
    
    rp_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-botaliaslocalesettings.html#cfn-lex-botalias-botaliaslocalesettings-enabled"""
    p_CodeHookSpecification: typing.Union['PropBotAliasCodeHookSpecification', dict] = attr.ib(
        default=None,
        converter=PropBotAliasCodeHookSpecification.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotAliasCodeHookSpecification)),
        metadata={AttrMeta.PROPERTY_NAME: "CodeHookSpecification"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-botaliaslocalesettings.html#cfn-lex-botalias-botaliaslocalesettings-codehookspecification"""

@attr.s
class PropBotAliasAudioLogDestination(Property):
    """
    AWS Object Type = "AWS::Lex::BotAlias.AudioLogDestination"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-audiologdestination.html

    Property Document:
    
    - ``rp_S3Bucket``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-audiologdestination.html#cfn-lex-botalias-audiologdestination-s3bucket
    """
    AWS_OBJECT_TYPE = "AWS::Lex::BotAlias.AudioLogDestination"
    
    rp_S3Bucket: typing.Union['PropBotAliasS3BucketLogDestination', dict] = attr.ib(
        default=None,
        converter=PropBotAliasS3BucketLogDestination.from_dict,
        validator=attr.validators.instance_of(PropBotAliasS3BucketLogDestination),
        metadata={AttrMeta.PROPERTY_NAME: "S3Bucket"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-audiologdestination.html#cfn-lex-botalias-audiologdestination-s3bucket"""

@attr.s
class PropBotSlotDefaultValueSpecification(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.SlotDefaultValueSpecification"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotdefaultvaluespecification.html

    Property Document:
    
    - ``rp_DefaultValueList``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotdefaultvaluespecification.html#cfn-lex-bot-slotdefaultvaluespecification-defaultvaluelist
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.SlotDefaultValueSpecification"
    
    rp_DefaultValueList: typing.List[typing.Union['PropBotSlotDefaultValue', dict]] = attr.ib(
        default=None,
        converter=PropBotSlotDefaultValue.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBotSlotDefaultValue), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultValueList"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotdefaultvaluespecification.html#cfn-lex-bot-slotdefaultvaluespecification-defaultvaluelist"""

@attr.s
class PropBotExternalSourceSetting(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.ExternalSourceSetting"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-externalsourcesetting.html

    Property Document:
    
    - ``p_GrammarSlotTypeSetting``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-externalsourcesetting.html#cfn-lex-bot-externalsourcesetting-grammarslottypesetting
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.ExternalSourceSetting"
    
    p_GrammarSlotTypeSetting: typing.Union['PropBotGrammarSlotTypeSetting', dict] = attr.ib(
        default=None,
        converter=PropBotGrammarSlotTypeSetting.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotGrammarSlotTypeSetting)),
        metadata={AttrMeta.PROPERTY_NAME: "GrammarSlotTypeSetting"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-externalsourcesetting.html#cfn-lex-bot-externalsourcesetting-grammarslottypesetting"""

@attr.s
class PropBotImageResponseCard(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.ImageResponseCard"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-imageresponsecard.html

    Property Document:
    
    - ``rp_Title``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-imageresponsecard.html#cfn-lex-bot-imageresponsecard-title
    - ``p_Buttons``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-imageresponsecard.html#cfn-lex-bot-imageresponsecard-buttons
    - ``p_ImageUrl``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-imageresponsecard.html#cfn-lex-bot-imageresponsecard-imageurl
    - ``p_Subtitle``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-imageresponsecard.html#cfn-lex-bot-imageresponsecard-subtitle
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.ImageResponseCard"
    
    rp_Title: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Title"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-imageresponsecard.html#cfn-lex-bot-imageresponsecard-title"""
    p_Buttons: typing.List[typing.Union['PropBotButton', dict]] = attr.ib(
        default=None,
        converter=PropBotButton.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBotButton), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Buttons"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-imageresponsecard.html#cfn-lex-bot-imageresponsecard-buttons"""
    p_ImageUrl: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ImageUrl"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-imageresponsecard.html#cfn-lex-bot-imageresponsecard-imageurl"""
    p_Subtitle: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Subtitle"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-imageresponsecard.html#cfn-lex-bot-imageresponsecard-subtitle"""

@attr.s
class PropBotAliasAudioLogSetting(Property):
    """
    AWS Object Type = "AWS::Lex::BotAlias.AudioLogSetting"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-audiologsetting.html

    Property Document:
    
    - ``rp_Destination``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-audiologsetting.html#cfn-lex-botalias-audiologsetting-destination
    - ``rp_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-audiologsetting.html#cfn-lex-botalias-audiologsetting-enabled
    """
    AWS_OBJECT_TYPE = "AWS::Lex::BotAlias.AudioLogSetting"
    
    rp_Destination: typing.Union['PropBotAliasAudioLogDestination', dict] = attr.ib(
        default=None,
        converter=PropBotAliasAudioLogDestination.from_dict,
        validator=attr.validators.instance_of(PropBotAliasAudioLogDestination),
        metadata={AttrMeta.PROPERTY_NAME: "Destination"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-audiologsetting.html#cfn-lex-botalias-audiologsetting-destination"""
    rp_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-audiologsetting.html#cfn-lex-botalias-audiologsetting-enabled"""

@attr.s
class PropBotSlotTypeValue(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.SlotTypeValue"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottypevalue.html

    Property Document:
    
    - ``rp_SampleValue``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottypevalue.html#cfn-lex-bot-slottypevalue-samplevalue
    - ``p_Synonyms``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottypevalue.html#cfn-lex-bot-slottypevalue-synonyms
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.SlotTypeValue"
    
    rp_SampleValue: typing.Union['PropBotSampleValue', dict] = attr.ib(
        default=None,
        converter=PropBotSampleValue.from_dict,
        validator=attr.validators.instance_of(PropBotSampleValue),
        metadata={AttrMeta.PROPERTY_NAME: "SampleValue"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottypevalue.html#cfn-lex-bot-slottypevalue-samplevalue"""
    p_Synonyms: typing.List[typing.Union['PropBotSampleValue', dict]] = attr.ib(
        default=None,
        converter=PropBotSampleValue.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBotSampleValue), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Synonyms"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottypevalue.html#cfn-lex-bot-slottypevalue-synonyms"""

@attr.s
class PropBotAliasTextLogSetting(Property):
    """
    AWS Object Type = "AWS::Lex::BotAlias.TextLogSetting"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-textlogsetting.html

    Property Document:
    
    - ``rp_Destination``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-textlogsetting.html#cfn-lex-botalias-textlogsetting-destination
    - ``rp_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-textlogsetting.html#cfn-lex-botalias-textlogsetting-enabled
    """
    AWS_OBJECT_TYPE = "AWS::Lex::BotAlias.TextLogSetting"
    
    rp_Destination: typing.Union['PropBotAliasTextLogDestination', dict] = attr.ib(
        default=None,
        converter=PropBotAliasTextLogDestination.from_dict,
        validator=attr.validators.instance_of(PropBotAliasTextLogDestination),
        metadata={AttrMeta.PROPERTY_NAME: "Destination"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-textlogsetting.html#cfn-lex-botalias-textlogsetting-destination"""
    rp_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-textlogsetting.html#cfn-lex-botalias-textlogsetting-enabled"""

@attr.s
class PropBotAliasBotAliasLocaleSettingsItem(Property):
    """
    AWS Object Type = "AWS::Lex::BotAlias.BotAliasLocaleSettingsItem"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-botaliaslocalesettingsitem.html

    Property Document:
    
    - ``rp_BotAliasLocaleSetting``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-botaliaslocalesettingsitem.html#cfn-lex-botalias-botaliaslocalesettingsitem-botaliaslocalesetting
    - ``rp_LocaleId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-botaliaslocalesettingsitem.html#cfn-lex-botalias-botaliaslocalesettingsitem-localeid
    """
    AWS_OBJECT_TYPE = "AWS::Lex::BotAlias.BotAliasLocaleSettingsItem"
    
    rp_BotAliasLocaleSetting: typing.Union['PropBotAliasBotAliasLocaleSettings', dict] = attr.ib(
        default=None,
        converter=PropBotAliasBotAliasLocaleSettings.from_dict,
        validator=attr.validators.instance_of(PropBotAliasBotAliasLocaleSettings),
        metadata={AttrMeta.PROPERTY_NAME: "BotAliasLocaleSetting"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-botaliaslocalesettingsitem.html#cfn-lex-botalias-botaliaslocalesettingsitem-botaliaslocalesetting"""
    rp_LocaleId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "LocaleId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-botaliaslocalesettingsitem.html#cfn-lex-botalias-botaliaslocalesettingsitem-localeid"""

@attr.s
class PropBotSlotType(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.SlotType"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottype.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottype.html#cfn-lex-bot-slottype-name
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottype.html#cfn-lex-bot-slottype-description
    - ``p_ExternalSourceSetting``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottype.html#cfn-lex-bot-slottype-externalsourcesetting
    - ``p_ParentSlotTypeSignature``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottype.html#cfn-lex-bot-slottype-parentslottypesignature
    - ``p_SlotTypeValues``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottype.html#cfn-lex-bot-slottype-slottypevalues
    - ``p_ValueSelectionSetting``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottype.html#cfn-lex-bot-slottype-valueselectionsetting
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.SlotType"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottype.html#cfn-lex-bot-slottype-name"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottype.html#cfn-lex-bot-slottype-description"""
    p_ExternalSourceSetting: typing.Union['PropBotExternalSourceSetting', dict] = attr.ib(
        default=None,
        converter=PropBotExternalSourceSetting.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotExternalSourceSetting)),
        metadata={AttrMeta.PROPERTY_NAME: "ExternalSourceSetting"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottype.html#cfn-lex-bot-slottype-externalsourcesetting"""
    p_ParentSlotTypeSignature: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ParentSlotTypeSignature"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottype.html#cfn-lex-bot-slottype-parentslottypesignature"""
    p_SlotTypeValues: typing.List[typing.Union['PropBotSlotTypeValue', dict]] = attr.ib(
        default=None,
        converter=PropBotSlotTypeValue.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBotSlotTypeValue), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SlotTypeValues"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottype.html#cfn-lex-bot-slottype-slottypevalues"""
    p_ValueSelectionSetting: typing.Union['PropBotSlotValueSelectionSetting', dict] = attr.ib(
        default=None,
        converter=PropBotSlotValueSelectionSetting.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotSlotValueSelectionSetting)),
        metadata={AttrMeta.PROPERTY_NAME: "ValueSelectionSetting"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottype.html#cfn-lex-bot-slottype-valueselectionsetting"""

@attr.s
class PropBotMessage(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.Message"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-message.html

    Property Document:
    
    - ``p_CustomPayload``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-message.html#cfn-lex-bot-message-custompayload
    - ``p_ImageResponseCard``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-message.html#cfn-lex-bot-message-imageresponsecard
    - ``p_PlainTextMessage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-message.html#cfn-lex-bot-message-plaintextmessage
    - ``p_SSMLMessage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-message.html#cfn-lex-bot-message-ssmlmessage
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.Message"
    
    p_CustomPayload: typing.Union['PropBotCustomPayload', dict] = attr.ib(
        default=None,
        converter=PropBotCustomPayload.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotCustomPayload)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomPayload"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-message.html#cfn-lex-bot-message-custompayload"""
    p_ImageResponseCard: typing.Union['PropBotImageResponseCard', dict] = attr.ib(
        default=None,
        converter=PropBotImageResponseCard.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotImageResponseCard)),
        metadata={AttrMeta.PROPERTY_NAME: "ImageResponseCard"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-message.html#cfn-lex-bot-message-imageresponsecard"""
    p_PlainTextMessage: typing.Union['PropBotPlainTextMessage', dict] = attr.ib(
        default=None,
        converter=PropBotPlainTextMessage.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotPlainTextMessage)),
        metadata={AttrMeta.PROPERTY_NAME: "PlainTextMessage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-message.html#cfn-lex-bot-message-plaintextmessage"""
    p_SSMLMessage: typing.Union['PropBotSSMLMessage', dict] = attr.ib(
        default=None,
        converter=PropBotSSMLMessage.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotSSMLMessage)),
        metadata={AttrMeta.PROPERTY_NAME: "SSMLMessage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-message.html#cfn-lex-bot-message-ssmlmessage"""

@attr.s
class PropBotAliasConversationLogSettings(Property):
    """
    AWS Object Type = "AWS::Lex::BotAlias.ConversationLogSettings"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-conversationlogsettings.html

    Property Document:
    
    - ``p_AudioLogSettings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-conversationlogsettings.html#cfn-lex-botalias-conversationlogsettings-audiologsettings
    - ``p_TextLogSettings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-conversationlogsettings.html#cfn-lex-botalias-conversationlogsettings-textlogsettings
    """
    AWS_OBJECT_TYPE = "AWS::Lex::BotAlias.ConversationLogSettings"
    
    p_AudioLogSettings: typing.List[typing.Union['PropBotAliasAudioLogSetting', dict]] = attr.ib(
        default=None,
        converter=PropBotAliasAudioLogSetting.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBotAliasAudioLogSetting), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AudioLogSettings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-conversationlogsettings.html#cfn-lex-botalias-conversationlogsettings-audiologsettings"""
    p_TextLogSettings: typing.List[typing.Union['PropBotAliasTextLogSetting', dict]] = attr.ib(
        default=None,
        converter=PropBotAliasTextLogSetting.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBotAliasTextLogSetting), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "TextLogSettings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-conversationlogsettings.html#cfn-lex-botalias-conversationlogsettings-textlogsettings"""

@attr.s
class PropBotMessageGroup(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.MessageGroup"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-messagegroup.html

    Property Document:
    
    - ``rp_Message``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-messagegroup.html#cfn-lex-bot-messagegroup-message
    - ``p_Variations``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-messagegroup.html#cfn-lex-bot-messagegroup-variations
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.MessageGroup"
    
    rp_Message: typing.Union['PropBotMessage', dict] = attr.ib(
        default=None,
        converter=PropBotMessage.from_dict,
        validator=attr.validators.instance_of(PropBotMessage),
        metadata={AttrMeta.PROPERTY_NAME: "Message"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-messagegroup.html#cfn-lex-bot-messagegroup-message"""
    p_Variations: typing.List[typing.Union['PropBotMessage', dict]] = attr.ib(
        default=None,
        converter=PropBotMessage.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBotMessage), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Variations"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-messagegroup.html#cfn-lex-bot-messagegroup-variations"""

@attr.s
class PropBotFulfillmentUpdateResponseSpecification(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.FulfillmentUpdateResponseSpecification"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdateresponsespecification.html

    Property Document:
    
    - ``rp_FrequencyInSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdateresponsespecification.html#cfn-lex-bot-fulfillmentupdateresponsespecification-frequencyinseconds
    - ``rp_MessageGroups``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdateresponsespecification.html#cfn-lex-bot-fulfillmentupdateresponsespecification-messagegroups
    - ``p_AllowInterrupt``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdateresponsespecification.html#cfn-lex-bot-fulfillmentupdateresponsespecification-allowinterrupt
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.FulfillmentUpdateResponseSpecification"
    
    rp_FrequencyInSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "FrequencyInSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdateresponsespecification.html#cfn-lex-bot-fulfillmentupdateresponsespecification-frequencyinseconds"""
    rp_MessageGroups: typing.List[typing.Union['PropBotMessageGroup', dict]] = attr.ib(
        default=None,
        converter=PropBotMessageGroup.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBotMessageGroup), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "MessageGroups"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdateresponsespecification.html#cfn-lex-bot-fulfillmentupdateresponsespecification-messagegroups"""
    p_AllowInterrupt: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "AllowInterrupt"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdateresponsespecification.html#cfn-lex-bot-fulfillmentupdateresponsespecification-allowinterrupt"""

@attr.s
class PropBotStillWaitingResponseSpecification(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.StillWaitingResponseSpecification"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-stillwaitingresponsespecification.html

    Property Document:
    
    - ``rp_FrequencyInSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-stillwaitingresponsespecification.html#cfn-lex-bot-stillwaitingresponsespecification-frequencyinseconds
    - ``rp_MessageGroupsList``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-stillwaitingresponsespecification.html#cfn-lex-bot-stillwaitingresponsespecification-messagegroupslist
    - ``rp_TimeoutInSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-stillwaitingresponsespecification.html#cfn-lex-bot-stillwaitingresponsespecification-timeoutinseconds
    - ``p_AllowInterrupt``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-stillwaitingresponsespecification.html#cfn-lex-bot-stillwaitingresponsespecification-allowinterrupt
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.StillWaitingResponseSpecification"
    
    rp_FrequencyInSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "FrequencyInSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-stillwaitingresponsespecification.html#cfn-lex-bot-stillwaitingresponsespecification-frequencyinseconds"""
    rp_MessageGroupsList: typing.List[typing.Union['PropBotMessageGroup', dict]] = attr.ib(
        default=None,
        converter=PropBotMessageGroup.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBotMessageGroup), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "MessageGroupsList"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-stillwaitingresponsespecification.html#cfn-lex-bot-stillwaitingresponsespecification-messagegroupslist"""
    rp_TimeoutInSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "TimeoutInSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-stillwaitingresponsespecification.html#cfn-lex-bot-stillwaitingresponsespecification-timeoutinseconds"""
    p_AllowInterrupt: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "AllowInterrupt"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-stillwaitingresponsespecification.html#cfn-lex-bot-stillwaitingresponsespecification-allowinterrupt"""

@attr.s
class PropBotPromptSpecification(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.PromptSpecification"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptspecification.html

    Property Document:
    
    - ``rp_MaxRetries``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptspecification.html#cfn-lex-bot-promptspecification-maxretries
    - ``rp_MessageGroupsList``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptspecification.html#cfn-lex-bot-promptspecification-messagegroupslist
    - ``p_AllowInterrupt``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptspecification.html#cfn-lex-bot-promptspecification-allowinterrupt
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.PromptSpecification"
    
    rp_MaxRetries: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "MaxRetries"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptspecification.html#cfn-lex-bot-promptspecification-maxretries"""
    rp_MessageGroupsList: typing.List[typing.Union['PropBotMessageGroup', dict]] = attr.ib(
        default=None,
        converter=PropBotMessageGroup.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBotMessageGroup), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "MessageGroupsList"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptspecification.html#cfn-lex-bot-promptspecification-messagegroupslist"""
    p_AllowInterrupt: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "AllowInterrupt"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptspecification.html#cfn-lex-bot-promptspecification-allowinterrupt"""

@attr.s
class PropBotFulfillmentStartResponseSpecification(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.FulfillmentStartResponseSpecification"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentstartresponsespecification.html

    Property Document:
    
    - ``rp_DelayInSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentstartresponsespecification.html#cfn-lex-bot-fulfillmentstartresponsespecification-delayinseconds
    - ``rp_MessageGroups``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentstartresponsespecification.html#cfn-lex-bot-fulfillmentstartresponsespecification-messagegroups
    - ``p_AllowInterrupt``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentstartresponsespecification.html#cfn-lex-bot-fulfillmentstartresponsespecification-allowinterrupt
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.FulfillmentStartResponseSpecification"
    
    rp_DelayInSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "DelayInSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentstartresponsespecification.html#cfn-lex-bot-fulfillmentstartresponsespecification-delayinseconds"""
    rp_MessageGroups: typing.List[typing.Union['PropBotMessageGroup', dict]] = attr.ib(
        default=None,
        converter=PropBotMessageGroup.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBotMessageGroup), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "MessageGroups"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentstartresponsespecification.html#cfn-lex-bot-fulfillmentstartresponsespecification-messagegroups"""
    p_AllowInterrupt: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "AllowInterrupt"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentstartresponsespecification.html#cfn-lex-bot-fulfillmentstartresponsespecification-allowinterrupt"""

@attr.s
class PropBotResponseSpecification(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.ResponseSpecification"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-responsespecification.html

    Property Document:
    
    - ``rp_MessageGroupsList``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-responsespecification.html#cfn-lex-bot-responsespecification-messagegroupslist
    - ``p_AllowInterrupt``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-responsespecification.html#cfn-lex-bot-responsespecification-allowinterrupt
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.ResponseSpecification"
    
    rp_MessageGroupsList: typing.List[typing.Union['PropBotMessageGroup', dict]] = attr.ib(
        default=None,
        converter=PropBotMessageGroup.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBotMessageGroup), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "MessageGroupsList"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-responsespecification.html#cfn-lex-bot-responsespecification-messagegroupslist"""
    p_AllowInterrupt: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "AllowInterrupt"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-responsespecification.html#cfn-lex-bot-responsespecification-allowinterrupt"""

@attr.s
class PropBotPostFulfillmentStatusSpecification(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.PostFulfillmentStatusSpecification"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postfulfillmentstatusspecification.html

    Property Document:
    
    - ``p_FailureResponse``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postfulfillmentstatusspecification.html#cfn-lex-bot-postfulfillmentstatusspecification-failureresponse
    - ``p_SuccessResponse``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postfulfillmentstatusspecification.html#cfn-lex-bot-postfulfillmentstatusspecification-successresponse
    - ``p_TimeoutResponse``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postfulfillmentstatusspecification.html#cfn-lex-bot-postfulfillmentstatusspecification-timeoutresponse
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.PostFulfillmentStatusSpecification"
    
    p_FailureResponse: typing.Union['PropBotResponseSpecification', dict] = attr.ib(
        default=None,
        converter=PropBotResponseSpecification.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotResponseSpecification)),
        metadata={AttrMeta.PROPERTY_NAME: "FailureResponse"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postfulfillmentstatusspecification.html#cfn-lex-bot-postfulfillmentstatusspecification-failureresponse"""
    p_SuccessResponse: typing.Union['PropBotResponseSpecification', dict] = attr.ib(
        default=None,
        converter=PropBotResponseSpecification.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotResponseSpecification)),
        metadata={AttrMeta.PROPERTY_NAME: "SuccessResponse"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postfulfillmentstatusspecification.html#cfn-lex-bot-postfulfillmentstatusspecification-successresponse"""
    p_TimeoutResponse: typing.Union['PropBotResponseSpecification', dict] = attr.ib(
        default=None,
        converter=PropBotResponseSpecification.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotResponseSpecification)),
        metadata={AttrMeta.PROPERTY_NAME: "TimeoutResponse"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postfulfillmentstatusspecification.html#cfn-lex-bot-postfulfillmentstatusspecification-timeoutresponse"""

@attr.s
class PropBotIntentClosingSetting(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.IntentClosingSetting"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentclosingsetting.html

    Property Document:
    
    - ``rp_ClosingResponse``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentclosingsetting.html#cfn-lex-bot-intentclosingsetting-closingresponse
    - ``p_IsActive``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentclosingsetting.html#cfn-lex-bot-intentclosingsetting-isactive
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.IntentClosingSetting"
    
    rp_ClosingResponse: typing.Union['PropBotResponseSpecification', dict] = attr.ib(
        default=None,
        converter=PropBotResponseSpecification.from_dict,
        validator=attr.validators.instance_of(PropBotResponseSpecification),
        metadata={AttrMeta.PROPERTY_NAME: "ClosingResponse"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentclosingsetting.html#cfn-lex-bot-intentclosingsetting-closingresponse"""
    p_IsActive: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IsActive"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentclosingsetting.html#cfn-lex-bot-intentclosingsetting-isactive"""

@attr.s
class PropBotFulfillmentUpdatesSpecification(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.FulfillmentUpdatesSpecification"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdatesspecification.html

    Property Document:
    
    - ``rp_Active``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdatesspecification.html#cfn-lex-bot-fulfillmentupdatesspecification-active
    - ``p_StartResponse``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdatesspecification.html#cfn-lex-bot-fulfillmentupdatesspecification-startresponse
    - ``p_TimeoutInSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdatesspecification.html#cfn-lex-bot-fulfillmentupdatesspecification-timeoutinseconds
    - ``p_UpdateResponse``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdatesspecification.html#cfn-lex-bot-fulfillmentupdatesspecification-updateresponse
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.FulfillmentUpdatesSpecification"
    
    rp_Active: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Active"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdatesspecification.html#cfn-lex-bot-fulfillmentupdatesspecification-active"""
    p_StartResponse: typing.Union['PropBotFulfillmentStartResponseSpecification', dict] = attr.ib(
        default=None,
        converter=PropBotFulfillmentStartResponseSpecification.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotFulfillmentStartResponseSpecification)),
        metadata={AttrMeta.PROPERTY_NAME: "StartResponse"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdatesspecification.html#cfn-lex-bot-fulfillmentupdatesspecification-startresponse"""
    p_TimeoutInSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "TimeoutInSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdatesspecification.html#cfn-lex-bot-fulfillmentupdatesspecification-timeoutinseconds"""
    p_UpdateResponse: typing.Union['PropBotFulfillmentUpdateResponseSpecification', dict] = attr.ib(
        default=None,
        converter=PropBotFulfillmentUpdateResponseSpecification.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotFulfillmentUpdateResponseSpecification)),
        metadata={AttrMeta.PROPERTY_NAME: "UpdateResponse"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdatesspecification.html#cfn-lex-bot-fulfillmentupdatesspecification-updateresponse"""

@attr.s
class PropBotIntentConfirmationSetting(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.IntentConfirmationSetting"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html

    Property Document:
    
    - ``rp_DeclinationResponse``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-declinationresponse
    - ``rp_PromptSpecification``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-promptspecification
    - ``p_IsActive``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-isactive
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.IntentConfirmationSetting"
    
    rp_DeclinationResponse: typing.Union['PropBotResponseSpecification', dict] = attr.ib(
        default=None,
        converter=PropBotResponseSpecification.from_dict,
        validator=attr.validators.instance_of(PropBotResponseSpecification),
        metadata={AttrMeta.PROPERTY_NAME: "DeclinationResponse"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-declinationresponse"""
    rp_PromptSpecification: typing.Union['PropBotPromptSpecification', dict] = attr.ib(
        default=None,
        converter=PropBotPromptSpecification.from_dict,
        validator=attr.validators.instance_of(PropBotPromptSpecification),
        metadata={AttrMeta.PROPERTY_NAME: "PromptSpecification"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-promptspecification"""
    p_IsActive: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IsActive"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-isactive"""

@attr.s
class PropBotWaitAndContinueSpecification(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.WaitAndContinueSpecification"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-waitandcontinuespecification.html

    Property Document:
    
    - ``rp_ContinueResponse``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-waitandcontinuespecification.html#cfn-lex-bot-waitandcontinuespecification-continueresponse
    - ``rp_WaitingResponse``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-waitandcontinuespecification.html#cfn-lex-bot-waitandcontinuespecification-waitingresponse
    - ``p_IsActive``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-waitandcontinuespecification.html#cfn-lex-bot-waitandcontinuespecification-isactive
    - ``p_StillWaitingResponse``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-waitandcontinuespecification.html#cfn-lex-bot-waitandcontinuespecification-stillwaitingresponse
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.WaitAndContinueSpecification"
    
    rp_ContinueResponse: typing.Union['PropBotResponseSpecification', dict] = attr.ib(
        default=None,
        converter=PropBotResponseSpecification.from_dict,
        validator=attr.validators.instance_of(PropBotResponseSpecification),
        metadata={AttrMeta.PROPERTY_NAME: "ContinueResponse"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-waitandcontinuespecification.html#cfn-lex-bot-waitandcontinuespecification-continueresponse"""
    rp_WaitingResponse: typing.Union['PropBotResponseSpecification', dict] = attr.ib(
        default=None,
        converter=PropBotResponseSpecification.from_dict,
        validator=attr.validators.instance_of(PropBotResponseSpecification),
        metadata={AttrMeta.PROPERTY_NAME: "WaitingResponse"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-waitandcontinuespecification.html#cfn-lex-bot-waitandcontinuespecification-waitingresponse"""
    p_IsActive: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IsActive"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-waitandcontinuespecification.html#cfn-lex-bot-waitandcontinuespecification-isactive"""
    p_StillWaitingResponse: typing.Union['PropBotStillWaitingResponseSpecification', dict] = attr.ib(
        default=None,
        converter=PropBotStillWaitingResponseSpecification.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotStillWaitingResponseSpecification)),
        metadata={AttrMeta.PROPERTY_NAME: "StillWaitingResponse"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-waitandcontinuespecification.html#cfn-lex-bot-waitandcontinuespecification-stillwaitingresponse"""

@attr.s
class PropBotSlotValueElicitationSetting(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.SlotValueElicitationSetting"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueelicitationsetting.html

    Property Document:
    
    - ``rp_SlotConstraint``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueelicitationsetting.html#cfn-lex-bot-slotvalueelicitationsetting-slotconstraint
    - ``p_DefaultValueSpecification``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueelicitationsetting.html#cfn-lex-bot-slotvalueelicitationsetting-defaultvaluespecification
    - ``p_PromptSpecification``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueelicitationsetting.html#cfn-lex-bot-slotvalueelicitationsetting-promptspecification
    - ``p_SampleUtterances``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueelicitationsetting.html#cfn-lex-bot-slotvalueelicitationsetting-sampleutterances
    - ``p_WaitAndContinueSpecification``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueelicitationsetting.html#cfn-lex-bot-slotvalueelicitationsetting-waitandcontinuespecification
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.SlotValueElicitationSetting"
    
    rp_SlotConstraint: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SlotConstraint"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueelicitationsetting.html#cfn-lex-bot-slotvalueelicitationsetting-slotconstraint"""
    p_DefaultValueSpecification: typing.Union['PropBotSlotDefaultValueSpecification', dict] = attr.ib(
        default=None,
        converter=PropBotSlotDefaultValueSpecification.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotSlotDefaultValueSpecification)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultValueSpecification"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueelicitationsetting.html#cfn-lex-bot-slotvalueelicitationsetting-defaultvaluespecification"""
    p_PromptSpecification: typing.Union['PropBotPromptSpecification', dict] = attr.ib(
        default=None,
        converter=PropBotPromptSpecification.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotPromptSpecification)),
        metadata={AttrMeta.PROPERTY_NAME: "PromptSpecification"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueelicitationsetting.html#cfn-lex-bot-slotvalueelicitationsetting-promptspecification"""
    p_SampleUtterances: typing.List[typing.Union['PropBotSampleUtterance', dict]] = attr.ib(
        default=None,
        converter=PropBotSampleUtterance.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBotSampleUtterance), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SampleUtterances"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueelicitationsetting.html#cfn-lex-bot-slotvalueelicitationsetting-sampleutterances"""
    p_WaitAndContinueSpecification: typing.Union['PropBotWaitAndContinueSpecification', dict] = attr.ib(
        default=None,
        converter=PropBotWaitAndContinueSpecification.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotWaitAndContinueSpecification)),
        metadata={AttrMeta.PROPERTY_NAME: "WaitAndContinueSpecification"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueelicitationsetting.html#cfn-lex-bot-slotvalueelicitationsetting-waitandcontinuespecification"""

@attr.s
class PropBotSlot(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.Slot"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slot.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slot.html#cfn-lex-bot-slot-name
    - ``rp_SlotTypeName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slot.html#cfn-lex-bot-slot-slottypename
    - ``rp_ValueElicitationSetting``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slot.html#cfn-lex-bot-slot-valueelicitationsetting
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slot.html#cfn-lex-bot-slot-description
    - ``p_MultipleValuesSetting``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slot.html#cfn-lex-bot-slot-multiplevaluessetting
    - ``p_ObfuscationSetting``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slot.html#cfn-lex-bot-slot-obfuscationsetting
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.Slot"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slot.html#cfn-lex-bot-slot-name"""
    rp_SlotTypeName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SlotTypeName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slot.html#cfn-lex-bot-slot-slottypename"""
    rp_ValueElicitationSetting: typing.Union['PropBotSlotValueElicitationSetting', dict] = attr.ib(
        default=None,
        converter=PropBotSlotValueElicitationSetting.from_dict,
        validator=attr.validators.instance_of(PropBotSlotValueElicitationSetting),
        metadata={AttrMeta.PROPERTY_NAME: "ValueElicitationSetting"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slot.html#cfn-lex-bot-slot-valueelicitationsetting"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slot.html#cfn-lex-bot-slot-description"""
    p_MultipleValuesSetting: typing.Union['PropBotMultipleValuesSetting', dict] = attr.ib(
        default=None,
        converter=PropBotMultipleValuesSetting.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotMultipleValuesSetting)),
        metadata={AttrMeta.PROPERTY_NAME: "MultipleValuesSetting"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slot.html#cfn-lex-bot-slot-multiplevaluessetting"""
    p_ObfuscationSetting: typing.Union['PropBotObfuscationSetting', dict] = attr.ib(
        default=None,
        converter=PropBotObfuscationSetting.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotObfuscationSetting)),
        metadata={AttrMeta.PROPERTY_NAME: "ObfuscationSetting"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slot.html#cfn-lex-bot-slot-obfuscationsetting"""

@attr.s
class PropBotFulfillmentCodeHookSetting(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.FulfillmentCodeHookSetting"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentcodehooksetting.html

    Property Document:
    
    - ``rp_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentcodehooksetting.html#cfn-lex-bot-fulfillmentcodehooksetting-enabled
    - ``p_FulfillmentUpdatesSpecification``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentcodehooksetting.html#cfn-lex-bot-fulfillmentcodehooksetting-fulfillmentupdatesspecification
    - ``p_PostFulfillmentStatusSpecification``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentcodehooksetting.html#cfn-lex-bot-fulfillmentcodehooksetting-postfulfillmentstatusspecification
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.FulfillmentCodeHookSetting"
    
    rp_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentcodehooksetting.html#cfn-lex-bot-fulfillmentcodehooksetting-enabled"""
    p_FulfillmentUpdatesSpecification: typing.Union['PropBotFulfillmentUpdatesSpecification', dict] = attr.ib(
        default=None,
        converter=PropBotFulfillmentUpdatesSpecification.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotFulfillmentUpdatesSpecification)),
        metadata={AttrMeta.PROPERTY_NAME: "FulfillmentUpdatesSpecification"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentcodehooksetting.html#cfn-lex-bot-fulfillmentcodehooksetting-fulfillmentupdatesspecification"""
    p_PostFulfillmentStatusSpecification: typing.Union['PropBotPostFulfillmentStatusSpecification', dict] = attr.ib(
        default=None,
        converter=PropBotPostFulfillmentStatusSpecification.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotPostFulfillmentStatusSpecification)),
        metadata={AttrMeta.PROPERTY_NAME: "PostFulfillmentStatusSpecification"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentcodehooksetting.html#cfn-lex-bot-fulfillmentcodehooksetting-postfulfillmentstatusspecification"""

@attr.s
class PropBotIntent(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.Intent"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-name
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-description
    - ``p_DialogCodeHook``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-dialogcodehook
    - ``p_FulfillmentCodeHook``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-fulfillmentcodehook
    - ``p_InputContexts``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-inputcontexts
    - ``p_IntentClosingSetting``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-intentclosingsetting
    - ``p_IntentConfirmationSetting``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-intentconfirmationsetting
    - ``p_KendraConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-kendraconfiguration
    - ``p_OutputContexts``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-outputcontexts
    - ``p_ParentIntentSignature``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-parentintentsignature
    - ``p_SampleUtterances``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-sampleutterances
    - ``p_SlotPriorities``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-slotpriorities
    - ``p_Slots``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-slots
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.Intent"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-name"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-description"""
    p_DialogCodeHook: typing.Union['PropBotDialogCodeHookSetting', dict] = attr.ib(
        default=None,
        converter=PropBotDialogCodeHookSetting.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotDialogCodeHookSetting)),
        metadata={AttrMeta.PROPERTY_NAME: "DialogCodeHook"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-dialogcodehook"""
    p_FulfillmentCodeHook: typing.Union['PropBotFulfillmentCodeHookSetting', dict] = attr.ib(
        default=None,
        converter=PropBotFulfillmentCodeHookSetting.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotFulfillmentCodeHookSetting)),
        metadata={AttrMeta.PROPERTY_NAME: "FulfillmentCodeHook"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-fulfillmentcodehook"""
    p_InputContexts: typing.List[typing.Union['PropBotInputContext', dict]] = attr.ib(
        default=None,
        converter=PropBotInputContext.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBotInputContext), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "InputContexts"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-inputcontexts"""
    p_IntentClosingSetting: typing.Union['PropBotIntentClosingSetting', dict] = attr.ib(
        default=None,
        converter=PropBotIntentClosingSetting.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotIntentClosingSetting)),
        metadata={AttrMeta.PROPERTY_NAME: "IntentClosingSetting"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-intentclosingsetting"""
    p_IntentConfirmationSetting: typing.Union['PropBotIntentConfirmationSetting', dict] = attr.ib(
        default=None,
        converter=PropBotIntentConfirmationSetting.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotIntentConfirmationSetting)),
        metadata={AttrMeta.PROPERTY_NAME: "IntentConfirmationSetting"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-intentconfirmationsetting"""
    p_KendraConfiguration: typing.Union['PropBotKendraConfiguration', dict] = attr.ib(
        default=None,
        converter=PropBotKendraConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotKendraConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "KendraConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-kendraconfiguration"""
    p_OutputContexts: typing.List[typing.Union['PropBotOutputContext', dict]] = attr.ib(
        default=None,
        converter=PropBotOutputContext.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBotOutputContext), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "OutputContexts"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-outputcontexts"""
    p_ParentIntentSignature: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ParentIntentSignature"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-parentintentsignature"""
    p_SampleUtterances: typing.List[typing.Union['PropBotSampleUtterance', dict]] = attr.ib(
        default=None,
        converter=PropBotSampleUtterance.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBotSampleUtterance), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SampleUtterances"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-sampleutterances"""
    p_SlotPriorities: typing.List[typing.Union['PropBotSlotPriority', dict]] = attr.ib(
        default=None,
        converter=PropBotSlotPriority.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBotSlotPriority), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SlotPriorities"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-slotpriorities"""
    p_Slots: typing.List[typing.Union['PropBotSlot', dict]] = attr.ib(
        default=None,
        converter=PropBotSlot.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBotSlot), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Slots"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-slots"""

@attr.s
class PropBotBotLocale(Property):
    """
    AWS Object Type = "AWS::Lex::Bot.BotLocale"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botlocale.html

    Property Document:
    
    - ``rp_LocaleId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botlocale.html#cfn-lex-bot-botlocale-localeid
    - ``rp_NluConfidenceThreshold``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botlocale.html#cfn-lex-bot-botlocale-nluconfidencethreshold
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botlocale.html#cfn-lex-bot-botlocale-description
    - ``p_Intents``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botlocale.html#cfn-lex-bot-botlocale-intents
    - ``p_SlotTypes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botlocale.html#cfn-lex-bot-botlocale-slottypes
    - ``p_VoiceSettings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botlocale.html#cfn-lex-bot-botlocale-voicesettings
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot.BotLocale"
    
    rp_LocaleId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "LocaleId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botlocale.html#cfn-lex-bot-botlocale-localeid"""
    rp_NluConfidenceThreshold: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "NluConfidenceThreshold"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botlocale.html#cfn-lex-bot-botlocale-nluconfidencethreshold"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botlocale.html#cfn-lex-bot-botlocale-description"""
    p_Intents: typing.List[typing.Union['PropBotIntent', dict]] = attr.ib(
        default=None,
        converter=PropBotIntent.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBotIntent), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Intents"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botlocale.html#cfn-lex-bot-botlocale-intents"""
    p_SlotTypes: typing.List[typing.Union['PropBotSlotType', dict]] = attr.ib(
        default=None,
        converter=PropBotSlotType.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBotSlotType), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SlotTypes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botlocale.html#cfn-lex-bot-botlocale-slottypes"""
    p_VoiceSettings: typing.Union['PropBotVoiceSettings', dict] = attr.ib(
        default=None,
        converter=PropBotVoiceSettings.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotVoiceSettings)),
        metadata={AttrMeta.PROPERTY_NAME: "VoiceSettings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botlocale.html#cfn-lex-bot-botlocale-voicesettings"""


#--- Resource declaration ---

@attr.s
class Bot(Resource):
    """
    AWS Object Type = "AWS::Lex::Bot"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html

    Property Document:
    
    - ``rp_DataPrivacy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-dataprivacy
    - ``rp_IdleSessionTTLInSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-idlesessionttlinseconds
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-name
    - ``rp_RoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-rolearn
    - ``p_AutoBuildBotLocales``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-autobuildbotlocales
    - ``p_BotFileS3Location``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-botfiles3location
    - ``p_BotLocales``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-botlocales
    - ``p_BotTags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-bottags
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-description
    - ``p_TestBotAliasTags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-testbotaliastags
    """
    AWS_OBJECT_TYPE = "AWS::Lex::Bot"

    
    rp_DataPrivacy: dict = attr.ib(
        default=None,
        validator=attr.validators.instance_of(dict),
        metadata={AttrMeta.PROPERTY_NAME: "DataPrivacy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-dataprivacy"""
    rp_IdleSessionTTLInSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "IdleSessionTTLInSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-idlesessionttlinseconds"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-name"""
    rp_RoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-rolearn"""
    p_AutoBuildBotLocales: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "AutoBuildBotLocales"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-autobuildbotlocales"""
    p_BotFileS3Location: typing.Union['PropBotS3Location', dict] = attr.ib(
        default=None,
        converter=PropBotS3Location.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotS3Location)),
        metadata={AttrMeta.PROPERTY_NAME: "BotFileS3Location"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-botfiles3location"""
    p_BotLocales: typing.List[typing.Union['PropBotBotLocale', dict]] = attr.ib(
        default=None,
        converter=PropBotBotLocale.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBotBotLocale), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "BotLocales"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-botlocales"""
    p_BotTags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "BotTags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-bottags"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-description"""
    p_TestBotAliasTags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "TestBotAliasTags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-testbotaliastags"""

    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#aws-resource-lex-bot-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#aws-resource-lex-bot-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class BotAlias(Resource):
    """
    AWS Object Type = "AWS::Lex::BotAlias"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html

    Property Document:
    
    - ``rp_BotAliasName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-botaliasname
    - ``rp_BotId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-botid
    - ``p_BotAliasLocaleSettings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-botaliaslocalesettings
    - ``p_BotAliasTags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-botaliastags
    - ``p_BotVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-botversion
    - ``p_ConversationLogSettings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-conversationlogsettings
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-description
    - ``p_SentimentAnalysisSettings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-sentimentanalysissettings
    """
    AWS_OBJECT_TYPE = "AWS::Lex::BotAlias"

    
    rp_BotAliasName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "BotAliasName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-botaliasname"""
    rp_BotId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "BotId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-botid"""
    p_BotAliasLocaleSettings: typing.List[typing.Union['PropBotAliasBotAliasLocaleSettingsItem', dict]] = attr.ib(
        default=None,
        converter=PropBotAliasBotAliasLocaleSettingsItem.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBotAliasBotAliasLocaleSettingsItem), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "BotAliasLocaleSettings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-botaliaslocalesettings"""
    p_BotAliasTags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "BotAliasTags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-botaliastags"""
    p_BotVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BotVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-botversion"""
    p_ConversationLogSettings: typing.Union['PropBotAliasConversationLogSettings', dict] = attr.ib(
        default=None,
        converter=PropBotAliasConversationLogSettings.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBotAliasConversationLogSettings)),
        metadata={AttrMeta.PROPERTY_NAME: "ConversationLogSettings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-conversationlogsettings"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-description"""
    p_SentimentAnalysisSettings: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "SentimentAnalysisSettings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-sentimentanalysissettings"""

    
    @property
    def rv_BotAliasId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#aws-resource-lex-botalias-return-values"""
        return GetAtt(resource=self, attr_name="BotAliasId")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#aws-resource-lex-botalias-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_BotAliasStatus(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#aws-resource-lex-botalias-return-values"""
        return GetAtt(resource=self, attr_name="BotAliasStatus")
    

@attr.s
class ResourcePolicy(Resource):
    """
    AWS Object Type = "AWS::Lex::ResourcePolicy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-resourcepolicy.html

    Property Document:
    
    - ``rp_Policy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-resourcepolicy.html#cfn-lex-resourcepolicy-policy
    - ``rp_ResourceArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-resourcepolicy.html#cfn-lex-resourcepolicy-resourcearn
    """
    AWS_OBJECT_TYPE = "AWS::Lex::ResourcePolicy"

    
    rp_Policy: typing.Union['PropResourcePolicyPolicy', dict] = attr.ib(
        default=None,
        converter=PropResourcePolicyPolicy.from_dict,
        validator=attr.validators.instance_of(PropResourcePolicyPolicy),
        metadata={AttrMeta.PROPERTY_NAME: "Policy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-resourcepolicy.html#cfn-lex-resourcepolicy-policy"""
    rp_ResourceArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-resourcepolicy.html#cfn-lex-resourcepolicy-resourcearn"""

    
    @property
    def rv_RevisionId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-resourcepolicy.html#aws-resource-lex-resourcepolicy-return-values"""
        return GetAtt(resource=self, attr_name="RevisionId")
    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-resourcepolicy.html#aws-resource-lex-resourcepolicy-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    

@attr.s
class BotVersion(Resource):
    """
    AWS Object Type = "AWS::Lex::BotVersion"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botversion.html

    Property Document:
    
    - ``rp_BotId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botversion.html#cfn-lex-botversion-botid
    - ``rp_BotVersionLocaleSpecification``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botversion.html#cfn-lex-botversion-botversionlocalespecification
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botversion.html#cfn-lex-botversion-description
    """
    AWS_OBJECT_TYPE = "AWS::Lex::BotVersion"

    
    rp_BotId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "BotId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botversion.html#cfn-lex-botversion-botid"""
    rp_BotVersionLocaleSpecification: typing.List[typing.Union['PropBotVersionBotVersionLocaleSpecification', dict]] = attr.ib(
        default=None,
        converter=PropBotVersionBotVersionLocaleSpecification.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBotVersionBotVersionLocaleSpecification), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "BotVersionLocaleSpecification"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botversion.html#cfn-lex-botversion-botversionlocalespecification"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botversion.html#cfn-lex-botversion-description"""

    
    @property
    def rv_BotVersion(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botversion.html#aws-resource-lex-botversion-return-values"""
        return GetAtt(resource=self, attr_name="BotVersion")
    
