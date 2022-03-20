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
class PropRuleGroupJsonMatchPattern(Property):
    """
    AWS Object Type = "AWS::WAFv2::RuleGroup.JsonMatchPattern"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-jsonmatchpattern.html

    Property Document:
    
    - ``p_All``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-jsonmatchpattern.html#cfn-wafv2-rulegroup-jsonmatchpattern-all
    - ``p_IncludedPaths``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-jsonmatchpattern.html#cfn-wafv2-rulegroup-jsonmatchpattern-includedpaths
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::RuleGroup.JsonMatchPattern"
    
    p_All: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "All"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-jsonmatchpattern.html#cfn-wafv2-rulegroup-jsonmatchpattern-all"""
    p_IncludedPaths: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "IncludedPaths"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-jsonmatchpattern.html#cfn-wafv2-rulegroup-jsonmatchpattern-includedpaths"""

@attr.s
class PropLoggingConfigurationFieldToMatch(Property):
    """
    AWS Object Type = "AWS::WAFv2::LoggingConfiguration.FieldToMatch"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-fieldtomatch.html

    Property Document:
    
    - ``p_JsonBody``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-fieldtomatch.html#cfn-wafv2-loggingconfiguration-fieldtomatch-jsonbody
    - ``p_Method``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-fieldtomatch.html#cfn-wafv2-loggingconfiguration-fieldtomatch-method
    - ``p_QueryString``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-fieldtomatch.html#cfn-wafv2-loggingconfiguration-fieldtomatch-querystring
    - ``p_SingleHeader``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-fieldtomatch.html#cfn-wafv2-loggingconfiguration-fieldtomatch-singleheader
    - ``p_UriPath``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-fieldtomatch.html#cfn-wafv2-loggingconfiguration-fieldtomatch-uripath
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::LoggingConfiguration.FieldToMatch"
    
    p_JsonBody: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "JsonBody"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-fieldtomatch.html#cfn-wafv2-loggingconfiguration-fieldtomatch-jsonbody"""
    p_Method: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Method"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-fieldtomatch.html#cfn-wafv2-loggingconfiguration-fieldtomatch-method"""
    p_QueryString: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "QueryString"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-fieldtomatch.html#cfn-wafv2-loggingconfiguration-fieldtomatch-querystring"""
    p_SingleHeader: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "SingleHeader"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-fieldtomatch.html#cfn-wafv2-loggingconfiguration-fieldtomatch-singleheader"""
    p_UriPath: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "UriPath"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-fieldtomatch.html#cfn-wafv2-loggingconfiguration-fieldtomatch-uripath"""

@attr.s
class PropWebACLFieldIdentifier(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.FieldIdentifier"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldidentifier.html

    Property Document:
    
    - ``rp_Identifier``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldidentifier.html#cfn-wafv2-webacl-fieldidentifier-identifier
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.FieldIdentifier"
    
    rp_Identifier: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Identifier"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldidentifier.html#cfn-wafv2-webacl-fieldidentifier-identifier"""

@attr.s
class PropWebACLTextTransformation(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.TextTransformation"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-texttransformation.html

    Property Document:
    
    - ``rp_Priority``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-texttransformation.html#cfn-wafv2-webacl-texttransformation-priority
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-texttransformation.html#cfn-wafv2-webacl-texttransformation-type
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.TextTransformation"
    
    rp_Priority: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Priority"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-texttransformation.html#cfn-wafv2-webacl-texttransformation-priority"""
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-texttransformation.html#cfn-wafv2-webacl-texttransformation-type"""

@attr.s
class PropRuleGroupLabelMatchStatement(Property):
    """
    AWS Object Type = "AWS::WAFv2::RuleGroup.LabelMatchStatement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-labelmatchstatement.html

    Property Document:
    
    - ``rp_Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-labelmatchstatement.html#cfn-wafv2-rulegroup-labelmatchstatement-key
    - ``rp_Scope``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-labelmatchstatement.html#cfn-wafv2-rulegroup-labelmatchstatement-scope
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::RuleGroup.LabelMatchStatement"
    
    rp_Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-labelmatchstatement.html#cfn-wafv2-rulegroup-labelmatchstatement-key"""
    rp_Scope: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Scope"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-labelmatchstatement.html#cfn-wafv2-rulegroup-labelmatchstatement-scope"""

@attr.s
class PropWebACLForwardedIPConfiguration(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.ForwardedIPConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-forwardedipconfiguration.html

    Property Document:
    
    - ``rp_FallbackBehavior``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-forwardedipconfiguration.html#cfn-wafv2-webacl-forwardedipconfiguration-fallbackbehavior
    - ``rp_HeaderName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-forwardedipconfiguration.html#cfn-wafv2-webacl-forwardedipconfiguration-headername
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.ForwardedIPConfiguration"
    
    rp_FallbackBehavior: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "FallbackBehavior"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-forwardedipconfiguration.html#cfn-wafv2-webacl-forwardedipconfiguration-fallbackbehavior"""
    rp_HeaderName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "HeaderName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-forwardedipconfiguration.html#cfn-wafv2-webacl-forwardedipconfiguration-headername"""

@attr.s
class PropRuleGroupRuleAction(Property):
    """
    AWS Object Type = "AWS::WAFv2::RuleGroup.RuleAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ruleaction.html

    Property Document:
    
    - ``p_Allow``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ruleaction.html#cfn-wafv2-rulegroup-ruleaction-allow
    - ``p_Block``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ruleaction.html#cfn-wafv2-rulegroup-ruleaction-block
    - ``p_Captcha``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ruleaction.html#cfn-wafv2-rulegroup-ruleaction-captcha
    - ``p_Count``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ruleaction.html#cfn-wafv2-rulegroup-ruleaction-count
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::RuleGroup.RuleAction"
    
    p_Allow: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Allow"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ruleaction.html#cfn-wafv2-rulegroup-ruleaction-allow"""
    p_Block: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Block"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ruleaction.html#cfn-wafv2-rulegroup-ruleaction-block"""
    p_Captcha: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Captcha"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ruleaction.html#cfn-wafv2-rulegroup-ruleaction-captcha"""
    p_Count: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Count"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ruleaction.html#cfn-wafv2-rulegroup-ruleaction-count"""

@attr.s
class PropWebACLLabel(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.Label"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-label.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-label.html#cfn-wafv2-webacl-label-name
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.Label"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-label.html#cfn-wafv2-webacl-label-name"""

@attr.s
class PropWebACLCustomHTTPHeader(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.CustomHTTPHeader"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customhttpheader.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customhttpheader.html#cfn-wafv2-webacl-customhttpheader-name
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customhttpheader.html#cfn-wafv2-webacl-customhttpheader-value
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.CustomHTTPHeader"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customhttpheader.html#cfn-wafv2-webacl-customhttpheader-name"""
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customhttpheader.html#cfn-wafv2-webacl-customhttpheader-value"""

@attr.s
class PropRuleGroupLabelSummary(Property):
    """
    AWS Object Type = "AWS::WAFv2::RuleGroup.LabelSummary"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-labelsummary.html

    Property Document:
    
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-labelsummary.html#cfn-wafv2-rulegroup-labelsummary-name
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::RuleGroup.LabelSummary"
    
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-labelsummary.html#cfn-wafv2-rulegroup-labelsummary-name"""

@attr.s
class PropWebACLIPSetForwardedIPConfiguration(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.IPSetForwardedIPConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetforwardedipconfiguration.html

    Property Document:
    
    - ``rp_FallbackBehavior``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetforwardedipconfiguration.html#cfn-wafv2-webacl-ipsetforwardedipconfiguration-fallbackbehavior
    - ``rp_HeaderName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetforwardedipconfiguration.html#cfn-wafv2-webacl-ipsetforwardedipconfiguration-headername
    - ``rp_Position``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetforwardedipconfiguration.html#cfn-wafv2-webacl-ipsetforwardedipconfiguration-position
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.IPSetForwardedIPConfiguration"
    
    rp_FallbackBehavior: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "FallbackBehavior"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetforwardedipconfiguration.html#cfn-wafv2-webacl-ipsetforwardedipconfiguration-fallbackbehavior"""
    rp_HeaderName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "HeaderName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetforwardedipconfiguration.html#cfn-wafv2-webacl-ipsetforwardedipconfiguration-headername"""
    rp_Position: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Position"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetforwardedipconfiguration.html#cfn-wafv2-webacl-ipsetforwardedipconfiguration-position"""

@attr.s
class PropWebACLCustomResponseBody(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.CustomResponseBody"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponsebody.html

    Property Document:
    
    - ``rp_Content``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponsebody.html#cfn-wafv2-webacl-customresponsebody-content
    - ``rp_ContentType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponsebody.html#cfn-wafv2-webacl-customresponsebody-contenttype
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.CustomResponseBody"
    
    rp_Content: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Content"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponsebody.html#cfn-wafv2-webacl-customresponsebody-content"""
    rp_ContentType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ContentType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponsebody.html#cfn-wafv2-webacl-customresponsebody-contenttype"""

@attr.s
class PropWebACLImmunityTimeProperty(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.ImmunityTimeProperty"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-immunitytimeproperty.html

    Property Document:
    
    - ``rp_ImmunityTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-immunitytimeproperty.html#cfn-wafv2-webacl-immunitytimeproperty-immunitytime
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.ImmunityTimeProperty"
    
    rp_ImmunityTime: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "ImmunityTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-immunitytimeproperty.html#cfn-wafv2-webacl-immunitytimeproperty-immunitytime"""

@attr.s
class PropWebACLLabelMatchStatement(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.LabelMatchStatement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-labelmatchstatement.html

    Property Document:
    
    - ``rp_Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-labelmatchstatement.html#cfn-wafv2-webacl-labelmatchstatement-key
    - ``rp_Scope``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-labelmatchstatement.html#cfn-wafv2-webacl-labelmatchstatement-scope
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.LabelMatchStatement"
    
    rp_Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-labelmatchstatement.html#cfn-wafv2-webacl-labelmatchstatement-key"""
    rp_Scope: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Scope"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-labelmatchstatement.html#cfn-wafv2-webacl-labelmatchstatement-scope"""

@attr.s
class PropWebACLJsonMatchPattern(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.JsonMatchPattern"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonmatchpattern.html

    Property Document:
    
    - ``p_All``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonmatchpattern.html#cfn-wafv2-webacl-jsonmatchpattern-all
    - ``p_IncludedPaths``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonmatchpattern.html#cfn-wafv2-webacl-jsonmatchpattern-includedpaths
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.JsonMatchPattern"
    
    p_All: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "All"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonmatchpattern.html#cfn-wafv2-webacl-jsonmatchpattern-all"""
    p_IncludedPaths: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "IncludedPaths"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonmatchpattern.html#cfn-wafv2-webacl-jsonmatchpattern-includedpaths"""

@attr.s
class PropWebACLCaptchaConfig(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.CaptchaConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-captchaconfig.html

    Property Document:
    
    - ``p_ImmunityTimeProperty``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-captchaconfig.html#cfn-wafv2-webacl-captchaconfig-immunitytimeproperty
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.CaptchaConfig"
    
    p_ImmunityTimeProperty: typing.Union['PropWebACLImmunityTimeProperty', dict] = attr.ib(
        default=None,
        converter=PropWebACLImmunityTimeProperty.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLImmunityTimeProperty)),
        metadata={AttrMeta.PROPERTY_NAME: "ImmunityTimeProperty"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-captchaconfig.html#cfn-wafv2-webacl-captchaconfig-immunitytimeproperty"""

@attr.s
class PropRuleGroupImmunityTimeProperty(Property):
    """
    AWS Object Type = "AWS::WAFv2::RuleGroup.ImmunityTimeProperty"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-immunitytimeproperty.html

    Property Document:
    
    - ``rp_ImmunityTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-immunitytimeproperty.html#cfn-wafv2-rulegroup-immunitytimeproperty-immunitytime
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::RuleGroup.ImmunityTimeProperty"
    
    rp_ImmunityTime: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "ImmunityTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-immunitytimeproperty.html#cfn-wafv2-rulegroup-immunitytimeproperty-immunitytime"""

@attr.s
class PropWebACLManagedRuleGroupConfig(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.ManagedRuleGroupConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupconfig.html

    Property Document:
    
    - ``p_LoginPath``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupconfig.html#cfn-wafv2-webacl-managedrulegroupconfig-loginpath
    - ``p_PasswordField``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupconfig.html#cfn-wafv2-webacl-managedrulegroupconfig-passwordfield
    - ``p_PayloadType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupconfig.html#cfn-wafv2-webacl-managedrulegroupconfig-payloadtype
    - ``p_UsernameField``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupconfig.html#cfn-wafv2-webacl-managedrulegroupconfig-usernamefield
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.ManagedRuleGroupConfig"
    
    p_LoginPath: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LoginPath"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupconfig.html#cfn-wafv2-webacl-managedrulegroupconfig-loginpath"""
    p_PasswordField: typing.Union['PropWebACLFieldIdentifier', dict] = attr.ib(
        default=None,
        converter=PropWebACLFieldIdentifier.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLFieldIdentifier)),
        metadata={AttrMeta.PROPERTY_NAME: "PasswordField"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupconfig.html#cfn-wafv2-webacl-managedrulegroupconfig-passwordfield"""
    p_PayloadType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PayloadType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupconfig.html#cfn-wafv2-webacl-managedrulegroupconfig-payloadtype"""
    p_UsernameField: typing.Union['PropWebACLFieldIdentifier', dict] = attr.ib(
        default=None,
        converter=PropWebACLFieldIdentifier.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLFieldIdentifier)),
        metadata={AttrMeta.PROPERTY_NAME: "UsernameField"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupconfig.html#cfn-wafv2-webacl-managedrulegroupconfig-usernamefield"""

@attr.s
class PropWebACLGeoMatchStatement(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.GeoMatchStatement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-geomatchstatement.html

    Property Document:
    
    - ``p_CountryCodes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-geomatchstatement.html#cfn-wafv2-webacl-geomatchstatement-countrycodes
    - ``p_ForwardedIPConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-geomatchstatement.html#cfn-wafv2-webacl-geomatchstatement-forwardedipconfig
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.GeoMatchStatement"
    
    p_CountryCodes: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "CountryCodes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-geomatchstatement.html#cfn-wafv2-webacl-geomatchstatement-countrycodes"""
    p_ForwardedIPConfig: typing.Union['PropWebACLForwardedIPConfiguration', dict] = attr.ib(
        default=None,
        converter=PropWebACLForwardedIPConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLForwardedIPConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "ForwardedIPConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-geomatchstatement.html#cfn-wafv2-webacl-geomatchstatement-forwardedipconfig"""

@attr.s
class PropRuleGroupVisibilityConfig(Property):
    """
    AWS Object Type = "AWS::WAFv2::RuleGroup.VisibilityConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-visibilityconfig.html

    Property Document:
    
    - ``rp_CloudWatchMetricsEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-visibilityconfig.html#cfn-wafv2-rulegroup-visibilityconfig-cloudwatchmetricsenabled
    - ``rp_MetricName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-visibilityconfig.html#cfn-wafv2-rulegroup-visibilityconfig-metricname
    - ``rp_SampledRequestsEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-visibilityconfig.html#cfn-wafv2-rulegroup-visibilityconfig-sampledrequestsenabled
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::RuleGroup.VisibilityConfig"
    
    rp_CloudWatchMetricsEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "CloudWatchMetricsEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-visibilityconfig.html#cfn-wafv2-rulegroup-visibilityconfig-cloudwatchmetricsenabled"""
    rp_MetricName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "MetricName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-visibilityconfig.html#cfn-wafv2-rulegroup-visibilityconfig-metricname"""
    rp_SampledRequestsEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "SampledRequestsEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-visibilityconfig.html#cfn-wafv2-rulegroup-visibilityconfig-sampledrequestsenabled"""

@attr.s
class PropRuleGroupIPSetForwardedIPConfiguration(Property):
    """
    AWS Object Type = "AWS::WAFv2::RuleGroup.IPSetForwardedIPConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetforwardedipconfiguration.html

    Property Document:
    
    - ``rp_FallbackBehavior``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetforwardedipconfiguration.html#cfn-wafv2-rulegroup-ipsetforwardedipconfiguration-fallbackbehavior
    - ``rp_HeaderName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetforwardedipconfiguration.html#cfn-wafv2-rulegroup-ipsetforwardedipconfiguration-headername
    - ``rp_Position``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetforwardedipconfiguration.html#cfn-wafv2-rulegroup-ipsetforwardedipconfiguration-position
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::RuleGroup.IPSetForwardedIPConfiguration"
    
    rp_FallbackBehavior: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "FallbackBehavior"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetforwardedipconfiguration.html#cfn-wafv2-rulegroup-ipsetforwardedipconfiguration-fallbackbehavior"""
    rp_HeaderName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "HeaderName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetforwardedipconfiguration.html#cfn-wafv2-rulegroup-ipsetforwardedipconfiguration-headername"""
    rp_Position: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Position"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetforwardedipconfiguration.html#cfn-wafv2-rulegroup-ipsetforwardedipconfiguration-position"""

@attr.s
class PropWebACLJsonBody(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.JsonBody"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonbody.html

    Property Document:
    
    - ``rp_MatchPattern``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonbody.html#cfn-wafv2-webacl-jsonbody-matchpattern
    - ``rp_MatchScope``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonbody.html#cfn-wafv2-webacl-jsonbody-matchscope
    - ``p_InvalidFallbackBehavior``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonbody.html#cfn-wafv2-webacl-jsonbody-invalidfallbackbehavior
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.JsonBody"
    
    rp_MatchPattern: typing.Union['PropWebACLJsonMatchPattern', dict] = attr.ib(
        default=None,
        converter=PropWebACLJsonMatchPattern.from_dict,
        validator=attr.validators.instance_of(PropWebACLJsonMatchPattern),
        metadata={AttrMeta.PROPERTY_NAME: "MatchPattern"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonbody.html#cfn-wafv2-webacl-jsonbody-matchpattern"""
    rp_MatchScope: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "MatchScope"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonbody.html#cfn-wafv2-webacl-jsonbody-matchscope"""
    p_InvalidFallbackBehavior: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "InvalidFallbackBehavior"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonbody.html#cfn-wafv2-webacl-jsonbody-invalidfallbackbehavior"""

@attr.s
class PropRuleGroupTextTransformation(Property):
    """
    AWS Object Type = "AWS::WAFv2::RuleGroup.TextTransformation"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-texttransformation.html

    Property Document:
    
    - ``rp_Priority``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-texttransformation.html#cfn-wafv2-rulegroup-texttransformation-priority
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-texttransformation.html#cfn-wafv2-rulegroup-texttransformation-type
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::RuleGroup.TextTransformation"
    
    rp_Priority: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Priority"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-texttransformation.html#cfn-wafv2-rulegroup-texttransformation-priority"""
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-texttransformation.html#cfn-wafv2-rulegroup-texttransformation-type"""

@attr.s
class PropWebACLOverrideAction(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.OverrideAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-overrideaction.html

    Property Document:
    
    - ``p_Count``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-overrideaction.html#cfn-wafv2-webacl-overrideaction-count
    - ``p_None``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-overrideaction.html#cfn-wafv2-webacl-overrideaction-none
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.OverrideAction"
    
    p_Count: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Count"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-overrideaction.html#cfn-wafv2-webacl-overrideaction-count"""
    p_None: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "None"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-overrideaction.html#cfn-wafv2-webacl-overrideaction-none"""

@attr.s
class PropRuleGroupJsonBody(Property):
    """
    AWS Object Type = "AWS::WAFv2::RuleGroup.JsonBody"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-jsonbody.html

    Property Document:
    
    - ``rp_MatchPattern``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-jsonbody.html#cfn-wafv2-rulegroup-jsonbody-matchpattern
    - ``rp_MatchScope``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-jsonbody.html#cfn-wafv2-rulegroup-jsonbody-matchscope
    - ``p_InvalidFallbackBehavior``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-jsonbody.html#cfn-wafv2-rulegroup-jsonbody-invalidfallbackbehavior
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::RuleGroup.JsonBody"
    
    rp_MatchPattern: typing.Union['PropRuleGroupJsonMatchPattern', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupJsonMatchPattern.from_dict,
        validator=attr.validators.instance_of(PropRuleGroupJsonMatchPattern),
        metadata={AttrMeta.PROPERTY_NAME: "MatchPattern"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-jsonbody.html#cfn-wafv2-rulegroup-jsonbody-matchpattern"""
    rp_MatchScope: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "MatchScope"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-jsonbody.html#cfn-wafv2-rulegroup-jsonbody-matchscope"""
    p_InvalidFallbackBehavior: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "InvalidFallbackBehavior"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-jsonbody.html#cfn-wafv2-rulegroup-jsonbody-invalidfallbackbehavior"""

@attr.s
class PropRuleGroupCustomResponseBody(Property):
    """
    AWS Object Type = "AWS::WAFv2::RuleGroup.CustomResponseBody"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-customresponsebody.html

    Property Document:
    
    - ``rp_Content``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-customresponsebody.html#cfn-wafv2-rulegroup-customresponsebody-content
    - ``rp_ContentType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-customresponsebody.html#cfn-wafv2-rulegroup-customresponsebody-contenttype
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::RuleGroup.CustomResponseBody"
    
    rp_Content: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Content"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-customresponsebody.html#cfn-wafv2-rulegroup-customresponsebody-content"""
    rp_ContentType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ContentType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-customresponsebody.html#cfn-wafv2-rulegroup-customresponsebody-contenttype"""

@attr.s
class PropWebACLCustomResponse(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.CustomResponse"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponse.html

    Property Document:
    
    - ``rp_ResponseCode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponse.html#cfn-wafv2-webacl-customresponse-responsecode
    - ``p_CustomResponseBodyKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponse.html#cfn-wafv2-webacl-customresponse-customresponsebodykey
    - ``p_ResponseHeaders``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponse.html#cfn-wafv2-webacl-customresponse-responseheaders
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.CustomResponse"
    
    rp_ResponseCode: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "ResponseCode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponse.html#cfn-wafv2-webacl-customresponse-responsecode"""
    p_CustomResponseBodyKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomResponseBodyKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponse.html#cfn-wafv2-webacl-customresponse-customresponsebodykey"""
    p_ResponseHeaders: typing.List[typing.Union['PropWebACLCustomHTTPHeader', dict]] = attr.ib(
        default=None,
        converter=PropWebACLCustomHTTPHeader.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropWebACLCustomHTTPHeader), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ResponseHeaders"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponse.html#cfn-wafv2-webacl-customresponse-responseheaders"""

@attr.s
class PropRuleGroupLabel(Property):
    """
    AWS Object Type = "AWS::WAFv2::RuleGroup.Label"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-label.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-label.html#cfn-wafv2-rulegroup-label-name
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::RuleGroup.Label"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-label.html#cfn-wafv2-rulegroup-label-name"""

@attr.s
class PropWebACLExcludedRule(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.ExcludedRule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-excludedrule.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-excludedrule.html#cfn-wafv2-webacl-excludedrule-name
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.ExcludedRule"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-excludedrule.html#cfn-wafv2-webacl-excludedrule-name"""

@attr.s
class PropWebACLVisibilityConfig(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.VisibilityConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-visibilityconfig.html

    Property Document:
    
    - ``rp_CloudWatchMetricsEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-visibilityconfig.html#cfn-wafv2-webacl-visibilityconfig-cloudwatchmetricsenabled
    - ``rp_MetricName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-visibilityconfig.html#cfn-wafv2-webacl-visibilityconfig-metricname
    - ``rp_SampledRequestsEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-visibilityconfig.html#cfn-wafv2-webacl-visibilityconfig-sampledrequestsenabled
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.VisibilityConfig"
    
    rp_CloudWatchMetricsEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "CloudWatchMetricsEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-visibilityconfig.html#cfn-wafv2-webacl-visibilityconfig-cloudwatchmetricsenabled"""
    rp_MetricName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "MetricName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-visibilityconfig.html#cfn-wafv2-webacl-visibilityconfig-metricname"""
    rp_SampledRequestsEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "SampledRequestsEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-visibilityconfig.html#cfn-wafv2-webacl-visibilityconfig-sampledrequestsenabled"""

@attr.s
class PropWebACLIPSetReferenceStatement(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.IPSetReferenceStatement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetreferencestatement.html

    Property Document:
    
    - ``rp_Arn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetreferencestatement.html#cfn-wafv2-webacl-ipsetreferencestatement-arn
    - ``p_IPSetForwardedIPConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetreferencestatement.html#cfn-wafv2-webacl-ipsetreferencestatement-ipsetforwardedipconfig
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.IPSetReferenceStatement"
    
    rp_Arn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Arn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetreferencestatement.html#cfn-wafv2-webacl-ipsetreferencestatement-arn"""
    p_IPSetForwardedIPConfig: typing.Union['PropWebACLIPSetForwardedIPConfiguration', dict] = attr.ib(
        default=None,
        converter=PropWebACLIPSetForwardedIPConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLIPSetForwardedIPConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "IPSetForwardedIPConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetreferencestatement.html#cfn-wafv2-webacl-ipsetreferencestatement-ipsetforwardedipconfig"""

@attr.s
class PropRuleGroupForwardedIPConfiguration(Property):
    """
    AWS Object Type = "AWS::WAFv2::RuleGroup.ForwardedIPConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-forwardedipconfiguration.html

    Property Document:
    
    - ``rp_FallbackBehavior``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-forwardedipconfiguration.html#cfn-wafv2-rulegroup-forwardedipconfiguration-fallbackbehavior
    - ``rp_HeaderName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-forwardedipconfiguration.html#cfn-wafv2-rulegroup-forwardedipconfiguration-headername
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::RuleGroup.ForwardedIPConfiguration"
    
    rp_FallbackBehavior: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "FallbackBehavior"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-forwardedipconfiguration.html#cfn-wafv2-rulegroup-forwardedipconfiguration-fallbackbehavior"""
    rp_HeaderName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "HeaderName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-forwardedipconfiguration.html#cfn-wafv2-rulegroup-forwardedipconfiguration-headername"""

@attr.s
class PropWebACLCustomRequestHandling(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.CustomRequestHandling"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customrequesthandling.html

    Property Document:
    
    - ``rp_InsertHeaders``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customrequesthandling.html#cfn-wafv2-webacl-customrequesthandling-insertheaders
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.CustomRequestHandling"
    
    rp_InsertHeaders: typing.List[typing.Union['PropWebACLCustomHTTPHeader', dict]] = attr.ib(
        default=None,
        converter=PropWebACLCustomHTTPHeader.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropWebACLCustomHTTPHeader), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "InsertHeaders"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customrequesthandling.html#cfn-wafv2-webacl-customrequesthandling-insertheaders"""

@attr.s
class PropWebACLAllowAction(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.AllowAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-allowaction.html

    Property Document:
    
    - ``p_CustomRequestHandling``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-allowaction.html#cfn-wafv2-webacl-allowaction-customrequesthandling
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.AllowAction"
    
    p_CustomRequestHandling: typing.Union['PropWebACLCustomRequestHandling', dict] = attr.ib(
        default=None,
        converter=PropWebACLCustomRequestHandling.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLCustomRequestHandling)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomRequestHandling"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-allowaction.html#cfn-wafv2-webacl-allowaction-customrequesthandling"""

@attr.s
class PropRuleGroupFieldToMatch(Property):
    """
    AWS Object Type = "AWS::WAFv2::RuleGroup.FieldToMatch"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html

    Property Document:
    
    - ``p_AllQueryArguments``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-allqueryarguments
    - ``p_Body``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-body
    - ``p_JsonBody``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-jsonbody
    - ``p_Method``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-method
    - ``p_QueryString``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-querystring
    - ``p_SingleHeader``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-singleheader
    - ``p_SingleQueryArgument``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-singlequeryargument
    - ``p_UriPath``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-uripath
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::RuleGroup.FieldToMatch"
    
    p_AllQueryArguments: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "AllQueryArguments"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-allqueryarguments"""
    p_Body: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Body"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-body"""
    p_JsonBody: typing.Union['PropRuleGroupJsonBody', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupJsonBody.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRuleGroupJsonBody)),
        metadata={AttrMeta.PROPERTY_NAME: "JsonBody"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-jsonbody"""
    p_Method: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Method"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-method"""
    p_QueryString: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "QueryString"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-querystring"""
    p_SingleHeader: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "SingleHeader"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-singleheader"""
    p_SingleQueryArgument: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "SingleQueryArgument"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-singlequeryargument"""
    p_UriPath: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "UriPath"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-uripath"""

@attr.s
class PropWebACLBlockAction(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.BlockAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-blockaction.html

    Property Document:
    
    - ``p_CustomResponse``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-blockaction.html#cfn-wafv2-webacl-blockaction-customresponse
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.BlockAction"
    
    p_CustomResponse: typing.Union['PropWebACLCustomResponse', dict] = attr.ib(
        default=None,
        converter=PropWebACLCustomResponse.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLCustomResponse)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomResponse"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-blockaction.html#cfn-wafv2-webacl-blockaction-customresponse"""

@attr.s
class PropRuleGroupIPSetReferenceStatement(Property):
    """
    AWS Object Type = "AWS::WAFv2::RuleGroup.IPSetReferenceStatement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetreferencestatement.html

    Property Document:
    
    - ``rp_Arn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetreferencestatement.html#cfn-wafv2-rulegroup-ipsetreferencestatement-arn
    - ``p_IPSetForwardedIPConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetreferencestatement.html#cfn-wafv2-rulegroup-ipsetreferencestatement-ipsetforwardedipconfig
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::RuleGroup.IPSetReferenceStatement"
    
    rp_Arn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Arn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetreferencestatement.html#cfn-wafv2-rulegroup-ipsetreferencestatement-arn"""
    p_IPSetForwardedIPConfig: typing.Union['PropRuleGroupIPSetForwardedIPConfiguration', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupIPSetForwardedIPConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRuleGroupIPSetForwardedIPConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "IPSetForwardedIPConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetreferencestatement.html#cfn-wafv2-rulegroup-ipsetreferencestatement-ipsetforwardedipconfig"""

@attr.s
class PropWebACLRuleGroupReferenceStatement(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.RuleGroupReferenceStatement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rulegroupreferencestatement.html

    Property Document:
    
    - ``rp_Arn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rulegroupreferencestatement.html#cfn-wafv2-webacl-rulegroupreferencestatement-arn
    - ``p_ExcludedRules``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rulegroupreferencestatement.html#cfn-wafv2-webacl-rulegroupreferencestatement-excludedrules
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.RuleGroupReferenceStatement"
    
    rp_Arn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Arn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rulegroupreferencestatement.html#cfn-wafv2-webacl-rulegroupreferencestatement-arn"""
    p_ExcludedRules: typing.List[typing.Union['PropWebACLExcludedRule', dict]] = attr.ib(
        default=None,
        converter=PropWebACLExcludedRule.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropWebACLExcludedRule), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ExcludedRules"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rulegroupreferencestatement.html#cfn-wafv2-webacl-rulegroupreferencestatement-excludedrules"""

@attr.s
class PropRuleGroupCaptchaConfig(Property):
    """
    AWS Object Type = "AWS::WAFv2::RuleGroup.CaptchaConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-captchaconfig.html

    Property Document:
    
    - ``p_ImmunityTimeProperty``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-captchaconfig.html#cfn-wafv2-rulegroup-captchaconfig-immunitytimeproperty
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::RuleGroup.CaptchaConfig"
    
    p_ImmunityTimeProperty: typing.Union['PropRuleGroupImmunityTimeProperty', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupImmunityTimeProperty.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRuleGroupImmunityTimeProperty)),
        metadata={AttrMeta.PROPERTY_NAME: "ImmunityTimeProperty"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-captchaconfig.html#cfn-wafv2-rulegroup-captchaconfig-immunitytimeproperty"""

@attr.s
class PropWebACLCountAction(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.CountAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-countaction.html

    Property Document:
    
    - ``p_CustomRequestHandling``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-countaction.html#cfn-wafv2-webacl-countaction-customrequesthandling
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.CountAction"
    
    p_CustomRequestHandling: typing.Union['PropWebACLCustomRequestHandling', dict] = attr.ib(
        default=None,
        converter=PropWebACLCustomRequestHandling.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLCustomRequestHandling)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomRequestHandling"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-countaction.html#cfn-wafv2-webacl-countaction-customrequesthandling"""

@attr.s
class PropWebACLFieldToMatch(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.FieldToMatch"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html

    Property Document:
    
    - ``p_AllQueryArguments``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-allqueryarguments
    - ``p_Body``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-body
    - ``p_JsonBody``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-jsonbody
    - ``p_Method``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-method
    - ``p_QueryString``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-querystring
    - ``p_SingleHeader``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-singleheader
    - ``p_SingleQueryArgument``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-singlequeryargument
    - ``p_UriPath``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-uripath
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.FieldToMatch"
    
    p_AllQueryArguments: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "AllQueryArguments"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-allqueryarguments"""
    p_Body: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Body"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-body"""
    p_JsonBody: typing.Union['PropWebACLJsonBody', dict] = attr.ib(
        default=None,
        converter=PropWebACLJsonBody.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLJsonBody)),
        metadata={AttrMeta.PROPERTY_NAME: "JsonBody"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-jsonbody"""
    p_Method: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Method"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-method"""
    p_QueryString: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "QueryString"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-querystring"""
    p_SingleHeader: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "SingleHeader"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-singleheader"""
    p_SingleQueryArgument: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "SingleQueryArgument"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-singlequeryargument"""
    p_UriPath: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "UriPath"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-uripath"""

@attr.s
class PropWebACLSqliMatchStatement(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.SqliMatchStatement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sqlimatchstatement.html

    Property Document:
    
    - ``rp_FieldToMatch``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sqlimatchstatement.html#cfn-wafv2-webacl-sqlimatchstatement-fieldtomatch
    - ``rp_TextTransformations``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sqlimatchstatement.html#cfn-wafv2-webacl-sqlimatchstatement-texttransformations
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.SqliMatchStatement"
    
    rp_FieldToMatch: typing.Union['PropWebACLFieldToMatch', dict] = attr.ib(
        default=None,
        converter=PropWebACLFieldToMatch.from_dict,
        validator=attr.validators.instance_of(PropWebACLFieldToMatch),
        metadata={AttrMeta.PROPERTY_NAME: "FieldToMatch"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sqlimatchstatement.html#cfn-wafv2-webacl-sqlimatchstatement-fieldtomatch"""
    rp_TextTransformations: typing.List[typing.Union['PropWebACLTextTransformation', dict]] = attr.ib(
        default=None,
        converter=PropWebACLTextTransformation.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropWebACLTextTransformation), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "TextTransformations"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sqlimatchstatement.html#cfn-wafv2-webacl-sqlimatchstatement-texttransformations"""

@attr.s
class PropRuleGroupGeoMatchStatement(Property):
    """
    AWS Object Type = "AWS::WAFv2::RuleGroup.GeoMatchStatement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-geomatchstatement.html

    Property Document:
    
    - ``p_CountryCodes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-geomatchstatement.html#cfn-wafv2-rulegroup-geomatchstatement-countrycodes
    - ``p_ForwardedIPConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-geomatchstatement.html#cfn-wafv2-rulegroup-geomatchstatement-forwardedipconfig
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::RuleGroup.GeoMatchStatement"
    
    p_CountryCodes: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "CountryCodes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-geomatchstatement.html#cfn-wafv2-rulegroup-geomatchstatement-countrycodes"""
    p_ForwardedIPConfig: typing.Union['PropRuleGroupForwardedIPConfiguration', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupForwardedIPConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRuleGroupForwardedIPConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "ForwardedIPConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-geomatchstatement.html#cfn-wafv2-rulegroup-geomatchstatement-forwardedipconfig"""

@attr.s
class PropRuleGroupRegexMatchStatement(Property):
    """
    AWS Object Type = "AWS::WAFv2::RuleGroup.RegexMatchStatement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexmatchstatement.html

    Property Document:
    
    - ``rp_FieldToMatch``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexmatchstatement.html#cfn-wafv2-rulegroup-regexmatchstatement-fieldtomatch
    - ``rp_RegexString``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexmatchstatement.html#cfn-wafv2-rulegroup-regexmatchstatement-regexstring
    - ``rp_TextTransformations``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexmatchstatement.html#cfn-wafv2-rulegroup-regexmatchstatement-texttransformations
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::RuleGroup.RegexMatchStatement"
    
    rp_FieldToMatch: typing.Union['PropRuleGroupFieldToMatch', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupFieldToMatch.from_dict,
        validator=attr.validators.instance_of(PropRuleGroupFieldToMatch),
        metadata={AttrMeta.PROPERTY_NAME: "FieldToMatch"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexmatchstatement.html#cfn-wafv2-rulegroup-regexmatchstatement-fieldtomatch"""
    rp_RegexString: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RegexString"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexmatchstatement.html#cfn-wafv2-rulegroup-regexmatchstatement-regexstring"""
    rp_TextTransformations: typing.List[typing.Union['PropRuleGroupTextTransformation', dict]] = attr.ib(
        default=None,
        converter=PropRuleGroupTextTransformation.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropRuleGroupTextTransformation), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "TextTransformations"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexmatchstatement.html#cfn-wafv2-rulegroup-regexmatchstatement-texttransformations"""

@attr.s
class PropRuleGroupByteMatchStatement(Property):
    """
    AWS Object Type = "AWS::WAFv2::RuleGroup.ByteMatchStatement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html

    Property Document:
    
    - ``rp_FieldToMatch``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html#cfn-wafv2-rulegroup-bytematchstatement-fieldtomatch
    - ``rp_PositionalConstraint``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html#cfn-wafv2-rulegroup-bytematchstatement-positionalconstraint
    - ``rp_TextTransformations``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html#cfn-wafv2-rulegroup-bytematchstatement-texttransformations
    - ``p_SearchString``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html#cfn-wafv2-rulegroup-bytematchstatement-searchstring
    - ``p_SearchStringBase64``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html#cfn-wafv2-rulegroup-bytematchstatement-searchstringbase64
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::RuleGroup.ByteMatchStatement"
    
    rp_FieldToMatch: typing.Union['PropRuleGroupFieldToMatch', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupFieldToMatch.from_dict,
        validator=attr.validators.instance_of(PropRuleGroupFieldToMatch),
        metadata={AttrMeta.PROPERTY_NAME: "FieldToMatch"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html#cfn-wafv2-rulegroup-bytematchstatement-fieldtomatch"""
    rp_PositionalConstraint: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PositionalConstraint"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html#cfn-wafv2-rulegroup-bytematchstatement-positionalconstraint"""
    rp_TextTransformations: typing.List[typing.Union['PropRuleGroupTextTransformation', dict]] = attr.ib(
        default=None,
        converter=PropRuleGroupTextTransformation.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropRuleGroupTextTransformation), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "TextTransformations"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html#cfn-wafv2-rulegroup-bytematchstatement-texttransformations"""
    p_SearchString: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SearchString"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html#cfn-wafv2-rulegroup-bytematchstatement-searchstring"""
    p_SearchStringBase64: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SearchStringBase64"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html#cfn-wafv2-rulegroup-bytematchstatement-searchstringbase64"""

@attr.s
class PropRuleGroupRegexPatternSetReferenceStatement(Property):
    """
    AWS Object Type = "AWS::WAFv2::RuleGroup.RegexPatternSetReferenceStatement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html

    Property Document:
    
    - ``rp_Arn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html#cfn-wafv2-rulegroup-regexpatternsetreferencestatement-arn
    - ``rp_FieldToMatch``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html#cfn-wafv2-rulegroup-regexpatternsetreferencestatement-fieldtomatch
    - ``rp_TextTransformations``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html#cfn-wafv2-rulegroup-regexpatternsetreferencestatement-texttransformations
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::RuleGroup.RegexPatternSetReferenceStatement"
    
    rp_Arn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Arn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html#cfn-wafv2-rulegroup-regexpatternsetreferencestatement-arn"""
    rp_FieldToMatch: typing.Union['PropRuleGroupFieldToMatch', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupFieldToMatch.from_dict,
        validator=attr.validators.instance_of(PropRuleGroupFieldToMatch),
        metadata={AttrMeta.PROPERTY_NAME: "FieldToMatch"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html#cfn-wafv2-rulegroup-regexpatternsetreferencestatement-fieldtomatch"""
    rp_TextTransformations: typing.List[typing.Union['PropRuleGroupTextTransformation', dict]] = attr.ib(
        default=None,
        converter=PropRuleGroupTextTransformation.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropRuleGroupTextTransformation), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "TextTransformations"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html#cfn-wafv2-rulegroup-regexpatternsetreferencestatement-texttransformations"""

@attr.s
class PropWebACLRegexMatchStatement(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.RegexMatchStatement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexmatchstatement.html

    Property Document:
    
    - ``rp_FieldToMatch``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexmatchstatement.html#cfn-wafv2-webacl-regexmatchstatement-fieldtomatch
    - ``rp_RegexString``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexmatchstatement.html#cfn-wafv2-webacl-regexmatchstatement-regexstring
    - ``rp_TextTransformations``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexmatchstatement.html#cfn-wafv2-webacl-regexmatchstatement-texttransformations
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.RegexMatchStatement"
    
    rp_FieldToMatch: typing.Union['PropWebACLFieldToMatch', dict] = attr.ib(
        default=None,
        converter=PropWebACLFieldToMatch.from_dict,
        validator=attr.validators.instance_of(PropWebACLFieldToMatch),
        metadata={AttrMeta.PROPERTY_NAME: "FieldToMatch"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexmatchstatement.html#cfn-wafv2-webacl-regexmatchstatement-fieldtomatch"""
    rp_RegexString: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RegexString"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexmatchstatement.html#cfn-wafv2-webacl-regexmatchstatement-regexstring"""
    rp_TextTransformations: typing.List[typing.Union['PropWebACLTextTransformation', dict]] = attr.ib(
        default=None,
        converter=PropWebACLTextTransformation.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropWebACLTextTransformation), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "TextTransformations"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexmatchstatement.html#cfn-wafv2-webacl-regexmatchstatement-texttransformations"""

@attr.s
class PropWebACLCaptchaAction(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.CaptchaAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-captchaaction.html

    Property Document:
    
    - ``p_CustomRequestHandling``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-captchaaction.html#cfn-wafv2-webacl-captchaaction-customrequesthandling
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.CaptchaAction"
    
    p_CustomRequestHandling: typing.Union['PropWebACLCustomRequestHandling', dict] = attr.ib(
        default=None,
        converter=PropWebACLCustomRequestHandling.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLCustomRequestHandling)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomRequestHandling"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-captchaaction.html#cfn-wafv2-webacl-captchaaction-customrequesthandling"""

@attr.s
class PropRuleGroupSqliMatchStatement(Property):
    """
    AWS Object Type = "AWS::WAFv2::RuleGroup.SqliMatchStatement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sqlimatchstatement.html

    Property Document:
    
    - ``rp_FieldToMatch``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sqlimatchstatement.html#cfn-wafv2-rulegroup-sqlimatchstatement-fieldtomatch
    - ``rp_TextTransformations``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sqlimatchstatement.html#cfn-wafv2-rulegroup-sqlimatchstatement-texttransformations
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::RuleGroup.SqliMatchStatement"
    
    rp_FieldToMatch: typing.Union['PropRuleGroupFieldToMatch', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupFieldToMatch.from_dict,
        validator=attr.validators.instance_of(PropRuleGroupFieldToMatch),
        metadata={AttrMeta.PROPERTY_NAME: "FieldToMatch"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sqlimatchstatement.html#cfn-wafv2-rulegroup-sqlimatchstatement-fieldtomatch"""
    rp_TextTransformations: typing.List[typing.Union['PropRuleGroupTextTransformation', dict]] = attr.ib(
        default=None,
        converter=PropRuleGroupTextTransformation.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropRuleGroupTextTransformation), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "TextTransformations"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sqlimatchstatement.html#cfn-wafv2-rulegroup-sqlimatchstatement-texttransformations"""

@attr.s
class PropRuleGroupSizeConstraintStatement(Property):
    """
    AWS Object Type = "AWS::WAFv2::RuleGroup.SizeConstraintStatement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sizeconstraintstatement.html

    Property Document:
    
    - ``rp_ComparisonOperator``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sizeconstraintstatement.html#cfn-wafv2-rulegroup-sizeconstraintstatement-comparisonoperator
    - ``rp_FieldToMatch``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sizeconstraintstatement.html#cfn-wafv2-rulegroup-sizeconstraintstatement-fieldtomatch
    - ``rp_Size``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sizeconstraintstatement.html#cfn-wafv2-rulegroup-sizeconstraintstatement-size
    - ``rp_TextTransformations``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sizeconstraintstatement.html#cfn-wafv2-rulegroup-sizeconstraintstatement-texttransformations
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::RuleGroup.SizeConstraintStatement"
    
    rp_ComparisonOperator: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ComparisonOperator"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sizeconstraintstatement.html#cfn-wafv2-rulegroup-sizeconstraintstatement-comparisonoperator"""
    rp_FieldToMatch: typing.Union['PropRuleGroupFieldToMatch', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupFieldToMatch.from_dict,
        validator=attr.validators.instance_of(PropRuleGroupFieldToMatch),
        metadata={AttrMeta.PROPERTY_NAME: "FieldToMatch"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sizeconstraintstatement.html#cfn-wafv2-rulegroup-sizeconstraintstatement-fieldtomatch"""
    rp_Size: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "Size"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sizeconstraintstatement.html#cfn-wafv2-rulegroup-sizeconstraintstatement-size"""
    rp_TextTransformations: typing.List[typing.Union['PropRuleGroupTextTransformation', dict]] = attr.ib(
        default=None,
        converter=PropRuleGroupTextTransformation.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropRuleGroupTextTransformation), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "TextTransformations"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sizeconstraintstatement.html#cfn-wafv2-rulegroup-sizeconstraintstatement-texttransformations"""

@attr.s
class PropRuleGroupXssMatchStatement(Property):
    """
    AWS Object Type = "AWS::WAFv2::RuleGroup.XssMatchStatement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-xssmatchstatement.html

    Property Document:
    
    - ``rp_FieldToMatch``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-xssmatchstatement.html#cfn-wafv2-rulegroup-xssmatchstatement-fieldtomatch
    - ``rp_TextTransformations``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-xssmatchstatement.html#cfn-wafv2-rulegroup-xssmatchstatement-texttransformations
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::RuleGroup.XssMatchStatement"
    
    rp_FieldToMatch: typing.Union['PropRuleGroupFieldToMatch', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupFieldToMatch.from_dict,
        validator=attr.validators.instance_of(PropRuleGroupFieldToMatch),
        metadata={AttrMeta.PROPERTY_NAME: "FieldToMatch"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-xssmatchstatement.html#cfn-wafv2-rulegroup-xssmatchstatement-fieldtomatch"""
    rp_TextTransformations: typing.List[typing.Union['PropRuleGroupTextTransformation', dict]] = attr.ib(
        default=None,
        converter=PropRuleGroupTextTransformation.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropRuleGroupTextTransformation), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "TextTransformations"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-xssmatchstatement.html#cfn-wafv2-rulegroup-xssmatchstatement-texttransformations"""

@attr.s
class PropWebACLDefaultAction(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.DefaultAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-defaultaction.html

    Property Document:
    
    - ``p_Allow``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-defaultaction.html#cfn-wafv2-webacl-defaultaction-allow
    - ``p_Block``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-defaultaction.html#cfn-wafv2-webacl-defaultaction-block
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.DefaultAction"
    
    p_Allow: typing.Union['PropWebACLAllowAction', dict] = attr.ib(
        default=None,
        converter=PropWebACLAllowAction.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLAllowAction)),
        metadata={AttrMeta.PROPERTY_NAME: "Allow"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-defaultaction.html#cfn-wafv2-webacl-defaultaction-allow"""
    p_Block: typing.Union['PropWebACLBlockAction', dict] = attr.ib(
        default=None,
        converter=PropWebACLBlockAction.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLBlockAction)),
        metadata={AttrMeta.PROPERTY_NAME: "Block"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-defaultaction.html#cfn-wafv2-webacl-defaultaction-block"""

@attr.s
class PropWebACLXssMatchStatement(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.XssMatchStatement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-xssmatchstatement.html

    Property Document:
    
    - ``rp_FieldToMatch``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-xssmatchstatement.html#cfn-wafv2-webacl-xssmatchstatement-fieldtomatch
    - ``rp_TextTransformations``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-xssmatchstatement.html#cfn-wafv2-webacl-xssmatchstatement-texttransformations
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.XssMatchStatement"
    
    rp_FieldToMatch: typing.Union['PropWebACLFieldToMatch', dict] = attr.ib(
        default=None,
        converter=PropWebACLFieldToMatch.from_dict,
        validator=attr.validators.instance_of(PropWebACLFieldToMatch),
        metadata={AttrMeta.PROPERTY_NAME: "FieldToMatch"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-xssmatchstatement.html#cfn-wafv2-webacl-xssmatchstatement-fieldtomatch"""
    rp_TextTransformations: typing.List[typing.Union['PropWebACLTextTransformation', dict]] = attr.ib(
        default=None,
        converter=PropWebACLTextTransformation.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropWebACLTextTransformation), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "TextTransformations"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-xssmatchstatement.html#cfn-wafv2-webacl-xssmatchstatement-texttransformations"""

@attr.s
class PropWebACLByteMatchStatement(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.ByteMatchStatement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html

    Property Document:
    
    - ``rp_FieldToMatch``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html#cfn-wafv2-webacl-bytematchstatement-fieldtomatch
    - ``rp_PositionalConstraint``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html#cfn-wafv2-webacl-bytematchstatement-positionalconstraint
    - ``rp_TextTransformations``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html#cfn-wafv2-webacl-bytematchstatement-texttransformations
    - ``p_SearchString``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html#cfn-wafv2-webacl-bytematchstatement-searchstring
    - ``p_SearchStringBase64``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html#cfn-wafv2-webacl-bytematchstatement-searchstringbase64
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.ByteMatchStatement"
    
    rp_FieldToMatch: typing.Union['PropWebACLFieldToMatch', dict] = attr.ib(
        default=None,
        converter=PropWebACLFieldToMatch.from_dict,
        validator=attr.validators.instance_of(PropWebACLFieldToMatch),
        metadata={AttrMeta.PROPERTY_NAME: "FieldToMatch"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html#cfn-wafv2-webacl-bytematchstatement-fieldtomatch"""
    rp_PositionalConstraint: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PositionalConstraint"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html#cfn-wafv2-webacl-bytematchstatement-positionalconstraint"""
    rp_TextTransformations: typing.List[typing.Union['PropWebACLTextTransformation', dict]] = attr.ib(
        default=None,
        converter=PropWebACLTextTransformation.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropWebACLTextTransformation), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "TextTransformations"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html#cfn-wafv2-webacl-bytematchstatement-texttransformations"""
    p_SearchString: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SearchString"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html#cfn-wafv2-webacl-bytematchstatement-searchstring"""
    p_SearchStringBase64: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SearchStringBase64"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html#cfn-wafv2-webacl-bytematchstatement-searchstringbase64"""

@attr.s
class PropWebACLRegexPatternSetReferenceStatement(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.RegexPatternSetReferenceStatement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexpatternsetreferencestatement.html

    Property Document:
    
    - ``rp_Arn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexpatternsetreferencestatement.html#cfn-wafv2-webacl-regexpatternsetreferencestatement-arn
    - ``rp_FieldToMatch``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexpatternsetreferencestatement.html#cfn-wafv2-webacl-regexpatternsetreferencestatement-fieldtomatch
    - ``rp_TextTransformations``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexpatternsetreferencestatement.html#cfn-wafv2-webacl-regexpatternsetreferencestatement-texttransformations
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.RegexPatternSetReferenceStatement"
    
    rp_Arn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Arn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexpatternsetreferencestatement.html#cfn-wafv2-webacl-regexpatternsetreferencestatement-arn"""
    rp_FieldToMatch: typing.Union['PropWebACLFieldToMatch', dict] = attr.ib(
        default=None,
        converter=PropWebACLFieldToMatch.from_dict,
        validator=attr.validators.instance_of(PropWebACLFieldToMatch),
        metadata={AttrMeta.PROPERTY_NAME: "FieldToMatch"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexpatternsetreferencestatement.html#cfn-wafv2-webacl-regexpatternsetreferencestatement-fieldtomatch"""
    rp_TextTransformations: typing.List[typing.Union['PropWebACLTextTransformation', dict]] = attr.ib(
        default=None,
        converter=PropWebACLTextTransformation.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropWebACLTextTransformation), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "TextTransformations"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexpatternsetreferencestatement.html#cfn-wafv2-webacl-regexpatternsetreferencestatement-texttransformations"""

@attr.s
class PropWebACLSizeConstraintStatement(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.SizeConstraintStatement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sizeconstraintstatement.html

    Property Document:
    
    - ``rp_ComparisonOperator``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sizeconstraintstatement.html#cfn-wafv2-webacl-sizeconstraintstatement-comparisonoperator
    - ``rp_FieldToMatch``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sizeconstraintstatement.html#cfn-wafv2-webacl-sizeconstraintstatement-fieldtomatch
    - ``rp_Size``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sizeconstraintstatement.html#cfn-wafv2-webacl-sizeconstraintstatement-size
    - ``rp_TextTransformations``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sizeconstraintstatement.html#cfn-wafv2-webacl-sizeconstraintstatement-texttransformations
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.SizeConstraintStatement"
    
    rp_ComparisonOperator: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ComparisonOperator"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sizeconstraintstatement.html#cfn-wafv2-webacl-sizeconstraintstatement-comparisonoperator"""
    rp_FieldToMatch: typing.Union['PropWebACLFieldToMatch', dict] = attr.ib(
        default=None,
        converter=PropWebACLFieldToMatch.from_dict,
        validator=attr.validators.instance_of(PropWebACLFieldToMatch),
        metadata={AttrMeta.PROPERTY_NAME: "FieldToMatch"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sizeconstraintstatement.html#cfn-wafv2-webacl-sizeconstraintstatement-fieldtomatch"""
    rp_Size: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "Size"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sizeconstraintstatement.html#cfn-wafv2-webacl-sizeconstraintstatement-size"""
    rp_TextTransformations: typing.List[typing.Union['PropWebACLTextTransformation', dict]] = attr.ib(
        default=None,
        converter=PropWebACLTextTransformation.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropWebACLTextTransformation), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "TextTransformations"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sizeconstraintstatement.html#cfn-wafv2-webacl-sizeconstraintstatement-texttransformations"""

@attr.s
class PropWebACLRuleAction(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.RuleAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ruleaction.html

    Property Document:
    
    - ``p_Allow``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ruleaction.html#cfn-wafv2-webacl-ruleaction-allow
    - ``p_Block``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ruleaction.html#cfn-wafv2-webacl-ruleaction-block
    - ``p_Captcha``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ruleaction.html#cfn-wafv2-webacl-ruleaction-captcha
    - ``p_Count``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ruleaction.html#cfn-wafv2-webacl-ruleaction-count
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.RuleAction"
    
    p_Allow: typing.Union['PropWebACLAllowAction', dict] = attr.ib(
        default=None,
        converter=PropWebACLAllowAction.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLAllowAction)),
        metadata={AttrMeta.PROPERTY_NAME: "Allow"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ruleaction.html#cfn-wafv2-webacl-ruleaction-allow"""
    p_Block: typing.Union['PropWebACLBlockAction', dict] = attr.ib(
        default=None,
        converter=PropWebACLBlockAction.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLBlockAction)),
        metadata={AttrMeta.PROPERTY_NAME: "Block"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ruleaction.html#cfn-wafv2-webacl-ruleaction-block"""
    p_Captcha: typing.Union['PropWebACLCaptchaAction', dict] = attr.ib(
        default=None,
        converter=PropWebACLCaptchaAction.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLCaptchaAction)),
        metadata={AttrMeta.PROPERTY_NAME: "Captcha"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ruleaction.html#cfn-wafv2-webacl-ruleaction-captcha"""
    p_Count: typing.Union['PropWebACLCountAction', dict] = attr.ib(
        default=None,
        converter=PropWebACLCountAction.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLCountAction)),
        metadata={AttrMeta.PROPERTY_NAME: "Count"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ruleaction.html#cfn-wafv2-webacl-ruleaction-count"""

@attr.s
class PropWebACLManagedRuleGroupStatement(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.ManagedRuleGroupStatement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html#cfn-wafv2-webacl-managedrulegroupstatement-name
    - ``rp_VendorName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html#cfn-wafv2-webacl-managedrulegroupstatement-vendorname
    - ``p_ExcludedRules``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html#cfn-wafv2-webacl-managedrulegroupstatement-excludedrules
    - ``p_ManagedRuleGroupConfigs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html#cfn-wafv2-webacl-managedrulegroupstatement-managedrulegroupconfigs
    - ``p_ScopeDownStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html#cfn-wafv2-webacl-managedrulegroupstatement-scopedownstatement
    - ``p_Version``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html#cfn-wafv2-webacl-managedrulegroupstatement-version
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.ManagedRuleGroupStatement"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html#cfn-wafv2-webacl-managedrulegroupstatement-name"""
    rp_VendorName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "VendorName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html#cfn-wafv2-webacl-managedrulegroupstatement-vendorname"""
    p_ExcludedRules: typing.List[typing.Union['PropWebACLExcludedRule', dict]] = attr.ib(
        default=None,
        converter=PropWebACLExcludedRule.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropWebACLExcludedRule), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ExcludedRules"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html#cfn-wafv2-webacl-managedrulegroupstatement-excludedrules"""
    p_ManagedRuleGroupConfigs: typing.List[typing.Union['PropWebACLManagedRuleGroupConfig', dict]] = attr.ib(
        default=None,
        converter=PropWebACLManagedRuleGroupConfig.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropWebACLManagedRuleGroupConfig), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ManagedRuleGroupConfigs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html#cfn-wafv2-webacl-managedrulegroupstatement-managedrulegroupconfigs"""
    p_ScopeDownStatement: typing.Union['PropWebACLStatement', dict] = attr.ib(
        default=None,
        validator=None,
        metadata={AttrMeta.PROPERTY_NAME: "ScopeDownStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html#cfn-wafv2-webacl-managedrulegroupstatement-scopedownstatement"""
    p_Version: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Version"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html#cfn-wafv2-webacl-managedrulegroupstatement-version"""

@attr.s
class PropWebACLOrStatement(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.OrStatement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-orstatement.html

    Property Document:
    
    - ``rp_Statements``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-orstatement.html#cfn-wafv2-webacl-orstatement-statements
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.OrStatement"
    
    rp_Statements: typing.List[typing.Union['PropWebACLStatement', dict]] = attr.ib(
        default=None,
        validator=attr.validators.instance_of(list),
        metadata={AttrMeta.PROPERTY_NAME: "Statements"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-orstatement.html#cfn-wafv2-webacl-orstatement-statements"""

@attr.s
class PropRuleGroupStatement(Property):
    """
    AWS Object Type = "AWS::WAFv2::RuleGroup.Statement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html

    Property Document:
    
    - ``p_AndStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-andstatement
    - ``p_ByteMatchStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-bytematchstatement
    - ``p_GeoMatchStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-geomatchstatement
    - ``p_IPSetReferenceStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-ipsetreferencestatement
    - ``p_LabelMatchStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-labelmatchstatement
    - ``p_NotStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-notstatement
    - ``p_OrStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-orstatement
    - ``p_RateBasedStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-ratebasedstatement
    - ``p_RegexMatchStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-regexmatchstatement
    - ``p_RegexPatternSetReferenceStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-regexpatternsetreferencestatement
    - ``p_SizeConstraintStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-sizeconstraintstatement
    - ``p_SqliMatchStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-sqlimatchstatement
    - ``p_XssMatchStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-xssmatchstatement
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::RuleGroup.Statement"
    
    p_AndStatement: typing.Union['PropRuleGroupAndStatement', dict] = attr.ib(
        default=None,
        validator=None,
        metadata={AttrMeta.PROPERTY_NAME: "AndStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-andstatement"""
    p_ByteMatchStatement: typing.Union['PropRuleGroupByteMatchStatement', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupByteMatchStatement.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRuleGroupByteMatchStatement)),
        metadata={AttrMeta.PROPERTY_NAME: "ByteMatchStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-bytematchstatement"""
    p_GeoMatchStatement: typing.Union['PropRuleGroupGeoMatchStatement', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupGeoMatchStatement.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRuleGroupGeoMatchStatement)),
        metadata={AttrMeta.PROPERTY_NAME: "GeoMatchStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-geomatchstatement"""
    p_IPSetReferenceStatement: typing.Union['PropRuleGroupIPSetReferenceStatement', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupIPSetReferenceStatement.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRuleGroupIPSetReferenceStatement)),
        metadata={AttrMeta.PROPERTY_NAME: "IPSetReferenceStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-ipsetreferencestatement"""
    p_LabelMatchStatement: typing.Union['PropRuleGroupLabelMatchStatement', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupLabelMatchStatement.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRuleGroupLabelMatchStatement)),
        metadata={AttrMeta.PROPERTY_NAME: "LabelMatchStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-labelmatchstatement"""
    p_NotStatement: typing.Union['PropRuleGroupNotStatement', dict] = attr.ib(
        default=None,
        validator=None,
        metadata={AttrMeta.PROPERTY_NAME: "NotStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-notstatement"""
    p_OrStatement: typing.Union['PropRuleGroupOrStatement', dict] = attr.ib(
        default=None,
        validator=None,
        metadata={AttrMeta.PROPERTY_NAME: "OrStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-orstatement"""
    p_RateBasedStatement: typing.Union['PropRuleGroupRateBasedStatement', dict] = attr.ib(
        default=None,
        validator=None,
        metadata={AttrMeta.PROPERTY_NAME: "RateBasedStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-ratebasedstatement"""
    p_RegexMatchStatement: typing.Union['PropRuleGroupRegexMatchStatement', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupRegexMatchStatement.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRuleGroupRegexMatchStatement)),
        metadata={AttrMeta.PROPERTY_NAME: "RegexMatchStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-regexmatchstatement"""
    p_RegexPatternSetReferenceStatement: typing.Union['PropRuleGroupRegexPatternSetReferenceStatement', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupRegexPatternSetReferenceStatement.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRuleGroupRegexPatternSetReferenceStatement)),
        metadata={AttrMeta.PROPERTY_NAME: "RegexPatternSetReferenceStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-regexpatternsetreferencestatement"""
    p_SizeConstraintStatement: typing.Union['PropRuleGroupSizeConstraintStatement', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupSizeConstraintStatement.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRuleGroupSizeConstraintStatement)),
        metadata={AttrMeta.PROPERTY_NAME: "SizeConstraintStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-sizeconstraintstatement"""
    p_SqliMatchStatement: typing.Union['PropRuleGroupSqliMatchStatement', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupSqliMatchStatement.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRuleGroupSqliMatchStatement)),
        metadata={AttrMeta.PROPERTY_NAME: "SqliMatchStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-sqlimatchstatement"""
    p_XssMatchStatement: typing.Union['PropRuleGroupXssMatchStatement', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupXssMatchStatement.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRuleGroupXssMatchStatement)),
        metadata={AttrMeta.PROPERTY_NAME: "XssMatchStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-xssmatchstatement"""

@attr.s
class PropWebACLStatement(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.Statement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html

    Property Document:
    
    - ``p_AndStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-andstatement
    - ``p_ByteMatchStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-bytematchstatement
    - ``p_GeoMatchStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-geomatchstatement
    - ``p_IPSetReferenceStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-ipsetreferencestatement
    - ``p_LabelMatchStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-labelmatchstatement
    - ``p_ManagedRuleGroupStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-managedrulegroupstatement
    - ``p_NotStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-notstatement
    - ``p_OrStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-orstatement
    - ``p_RateBasedStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-ratebasedstatement
    - ``p_RegexMatchStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-regexmatchstatement
    - ``p_RegexPatternSetReferenceStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-regexpatternsetreferencestatement
    - ``p_RuleGroupReferenceStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-rulegroupreferencestatement
    - ``p_SizeConstraintStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-sizeconstraintstatement
    - ``p_SqliMatchStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-sqlimatchstatement
    - ``p_XssMatchStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-xssmatchstatement
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.Statement"
    
    p_AndStatement: typing.Union['PropWebACLAndStatement', dict] = attr.ib(
        default=None,
        validator=None,
        metadata={AttrMeta.PROPERTY_NAME: "AndStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-andstatement"""
    p_ByteMatchStatement: typing.Union['PropWebACLByteMatchStatement', dict] = attr.ib(
        default=None,
        converter=PropWebACLByteMatchStatement.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLByteMatchStatement)),
        metadata={AttrMeta.PROPERTY_NAME: "ByteMatchStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-bytematchstatement"""
    p_GeoMatchStatement: typing.Union['PropWebACLGeoMatchStatement', dict] = attr.ib(
        default=None,
        converter=PropWebACLGeoMatchStatement.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLGeoMatchStatement)),
        metadata={AttrMeta.PROPERTY_NAME: "GeoMatchStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-geomatchstatement"""
    p_IPSetReferenceStatement: typing.Union['PropWebACLIPSetReferenceStatement', dict] = attr.ib(
        default=None,
        converter=PropWebACLIPSetReferenceStatement.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLIPSetReferenceStatement)),
        metadata={AttrMeta.PROPERTY_NAME: "IPSetReferenceStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-ipsetreferencestatement"""
    p_LabelMatchStatement: typing.Union['PropWebACLLabelMatchStatement', dict] = attr.ib(
        default=None,
        converter=PropWebACLLabelMatchStatement.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLLabelMatchStatement)),
        metadata={AttrMeta.PROPERTY_NAME: "LabelMatchStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-labelmatchstatement"""
    p_ManagedRuleGroupStatement: typing.Union['PropWebACLManagedRuleGroupStatement', dict] = attr.ib(
        default=None,
        validator=None,
        metadata={AttrMeta.PROPERTY_NAME: "ManagedRuleGroupStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-managedrulegroupstatement"""
    p_NotStatement: typing.Union['PropWebACLNotStatement', dict] = attr.ib(
        default=None,
        validator=None,
        metadata={AttrMeta.PROPERTY_NAME: "NotStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-notstatement"""
    p_OrStatement: typing.Union['PropWebACLOrStatement', dict] = attr.ib(
        default=None,
        validator=None,
        metadata={AttrMeta.PROPERTY_NAME: "OrStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-orstatement"""
    p_RateBasedStatement: typing.Union['PropWebACLRateBasedStatement', dict] = attr.ib(
        default=None,
        validator=None,
        metadata={AttrMeta.PROPERTY_NAME: "RateBasedStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-ratebasedstatement"""
    p_RegexMatchStatement: typing.Union['PropWebACLRegexMatchStatement', dict] = attr.ib(
        default=None,
        converter=PropWebACLRegexMatchStatement.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLRegexMatchStatement)),
        metadata={AttrMeta.PROPERTY_NAME: "RegexMatchStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-regexmatchstatement"""
    p_RegexPatternSetReferenceStatement: typing.Union['PropWebACLRegexPatternSetReferenceStatement', dict] = attr.ib(
        default=None,
        converter=PropWebACLRegexPatternSetReferenceStatement.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLRegexPatternSetReferenceStatement)),
        metadata={AttrMeta.PROPERTY_NAME: "RegexPatternSetReferenceStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-regexpatternsetreferencestatement"""
    p_RuleGroupReferenceStatement: typing.Union['PropWebACLRuleGroupReferenceStatement', dict] = attr.ib(
        default=None,
        converter=PropWebACLRuleGroupReferenceStatement.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLRuleGroupReferenceStatement)),
        metadata={AttrMeta.PROPERTY_NAME: "RuleGroupReferenceStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-rulegroupreferencestatement"""
    p_SizeConstraintStatement: typing.Union['PropWebACLSizeConstraintStatement', dict] = attr.ib(
        default=None,
        converter=PropWebACLSizeConstraintStatement.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLSizeConstraintStatement)),
        metadata={AttrMeta.PROPERTY_NAME: "SizeConstraintStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-sizeconstraintstatement"""
    p_SqliMatchStatement: typing.Union['PropWebACLSqliMatchStatement', dict] = attr.ib(
        default=None,
        converter=PropWebACLSqliMatchStatement.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLSqliMatchStatement)),
        metadata={AttrMeta.PROPERTY_NAME: "SqliMatchStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-sqlimatchstatement"""
    p_XssMatchStatement: typing.Union['PropWebACLXssMatchStatement', dict] = attr.ib(
        default=None,
        converter=PropWebACLXssMatchStatement.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLXssMatchStatement)),
        metadata={AttrMeta.PROPERTY_NAME: "XssMatchStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-xssmatchstatement"""

@attr.s
class PropWebACLAndStatement(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.AndStatement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-andstatement.html

    Property Document:
    
    - ``rp_Statements``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-andstatement.html#cfn-wafv2-webacl-andstatement-statements
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.AndStatement"
    
    rp_Statements: typing.List[typing.Union['PropWebACLStatement', dict]] = attr.ib(
        default=None,
        validator=attr.validators.instance_of(list),
        metadata={AttrMeta.PROPERTY_NAME: "Statements"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-andstatement.html#cfn-wafv2-webacl-andstatement-statements"""

@attr.s
class PropRuleGroupRateBasedStatement(Property):
    """
    AWS Object Type = "AWS::WAFv2::RuleGroup.RateBasedStatement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatement.html

    Property Document:
    
    - ``rp_AggregateKeyType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatement.html#cfn-wafv2-rulegroup-ratebasedstatement-aggregatekeytype
    - ``rp_Limit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatement.html#cfn-wafv2-rulegroup-ratebasedstatement-limit
    - ``p_ForwardedIPConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatement.html#cfn-wafv2-rulegroup-ratebasedstatement-forwardedipconfig
    - ``p_ScopeDownStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatement.html#cfn-wafv2-rulegroup-ratebasedstatement-scopedownstatement
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::RuleGroup.RateBasedStatement"
    
    rp_AggregateKeyType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AggregateKeyType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatement.html#cfn-wafv2-rulegroup-ratebasedstatement-aggregatekeytype"""
    rp_Limit: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Limit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatement.html#cfn-wafv2-rulegroup-ratebasedstatement-limit"""
    p_ForwardedIPConfig: typing.Union['PropRuleGroupForwardedIPConfiguration', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupForwardedIPConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRuleGroupForwardedIPConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "ForwardedIPConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatement.html#cfn-wafv2-rulegroup-ratebasedstatement-forwardedipconfig"""
    p_ScopeDownStatement: typing.Union['PropRuleGroupStatement', dict] = attr.ib(
        default=None,
        validator=None,
        metadata={AttrMeta.PROPERTY_NAME: "ScopeDownStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatement.html#cfn-wafv2-rulegroup-ratebasedstatement-scopedownstatement"""

@attr.s
class PropRuleGroupAndStatement(Property):
    """
    AWS Object Type = "AWS::WAFv2::RuleGroup.AndStatement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-andstatement.html

    Property Document:
    
    - ``rp_Statements``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-andstatement.html#cfn-wafv2-rulegroup-andstatement-statements
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::RuleGroup.AndStatement"
    
    rp_Statements: typing.List[typing.Union['PropRuleGroupStatement', dict]] = attr.ib(
        default=None,
        validator=attr.validators.instance_of(list),
        metadata={AttrMeta.PROPERTY_NAME: "Statements"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-andstatement.html#cfn-wafv2-rulegroup-andstatement-statements"""

@attr.s
class PropWebACLNotStatement(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.NotStatement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-notstatement.html

    Property Document:
    
    - ``rp_Statement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-notstatement.html#cfn-wafv2-webacl-notstatement-statement
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.NotStatement"
    
    rp_Statement: typing.Union['PropWebACLStatement', dict] = attr.ib(
        default=None,
        validator=None,
        metadata={AttrMeta.PROPERTY_NAME: "Statement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-notstatement.html#cfn-wafv2-webacl-notstatement-statement"""

@attr.s
class PropRuleGroupOrStatement(Property):
    """
    AWS Object Type = "AWS::WAFv2::RuleGroup.OrStatement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-orstatement.html

    Property Document:
    
    - ``rp_Statements``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-orstatement.html#cfn-wafv2-rulegroup-orstatement-statements
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::RuleGroup.OrStatement"
    
    rp_Statements: typing.List[typing.Union['PropRuleGroupStatement', dict]] = attr.ib(
        default=None,
        validator=attr.validators.instance_of(list),
        metadata={AttrMeta.PROPERTY_NAME: "Statements"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-orstatement.html#cfn-wafv2-rulegroup-orstatement-statements"""

@attr.s
class PropRuleGroupRule(Property):
    """
    AWS Object Type = "AWS::WAFv2::RuleGroup.Rule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-name
    - ``rp_Priority``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-priority
    - ``rp_Statement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-statement
    - ``rp_VisibilityConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-visibilityconfig
    - ``p_Action``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-action
    - ``p_CaptchaConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-captchaconfig
    - ``p_RuleLabels``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-rulelabels
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::RuleGroup.Rule"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-name"""
    rp_Priority: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Priority"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-priority"""
    rp_Statement: typing.Union['PropRuleGroupStatement', dict] = attr.ib(
        default=None,
        validator=None,
        metadata={AttrMeta.PROPERTY_NAME: "Statement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-statement"""
    rp_VisibilityConfig: typing.Union['PropRuleGroupVisibilityConfig', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupVisibilityConfig.from_dict,
        validator=attr.validators.instance_of(PropRuleGroupVisibilityConfig),
        metadata={AttrMeta.PROPERTY_NAME: "VisibilityConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-visibilityconfig"""
    p_Action: typing.Union['PropRuleGroupRuleAction', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupRuleAction.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRuleGroupRuleAction)),
        metadata={AttrMeta.PROPERTY_NAME: "Action"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-action"""
    p_CaptchaConfig: typing.Union['PropRuleGroupCaptchaConfig', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupCaptchaConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRuleGroupCaptchaConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "CaptchaConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-captchaconfig"""
    p_RuleLabels: typing.List[typing.Union['PropRuleGroupLabel', dict]] = attr.ib(
        default=None,
        converter=PropRuleGroupLabel.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropRuleGroupLabel), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "RuleLabels"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-rulelabels"""

@attr.s
class PropWebACLRule(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.Rule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-name
    - ``rp_Priority``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-priority
    - ``rp_Statement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-statement
    - ``rp_VisibilityConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-visibilityconfig
    - ``p_Action``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-action
    - ``p_CaptchaConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-captchaconfig
    - ``p_OverrideAction``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-overrideaction
    - ``p_RuleLabels``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-rulelabels
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.Rule"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-name"""
    rp_Priority: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Priority"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-priority"""
    rp_Statement: typing.Union['PropWebACLStatement', dict] = attr.ib(
        default=None,
        validator=None,
        metadata={AttrMeta.PROPERTY_NAME: "Statement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-statement"""
    rp_VisibilityConfig: typing.Union['PropWebACLVisibilityConfig', dict] = attr.ib(
        default=None,
        converter=PropWebACLVisibilityConfig.from_dict,
        validator=attr.validators.instance_of(PropWebACLVisibilityConfig),
        metadata={AttrMeta.PROPERTY_NAME: "VisibilityConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-visibilityconfig"""
    p_Action: typing.Union['PropWebACLRuleAction', dict] = attr.ib(
        default=None,
        converter=PropWebACLRuleAction.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLRuleAction)),
        metadata={AttrMeta.PROPERTY_NAME: "Action"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-action"""
    p_CaptchaConfig: typing.Union['PropWebACLCaptchaConfig', dict] = attr.ib(
        default=None,
        converter=PropWebACLCaptchaConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLCaptchaConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "CaptchaConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-captchaconfig"""
    p_OverrideAction: typing.Union['PropWebACLOverrideAction', dict] = attr.ib(
        default=None,
        converter=PropWebACLOverrideAction.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLOverrideAction)),
        metadata={AttrMeta.PROPERTY_NAME: "OverrideAction"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-overrideaction"""
    p_RuleLabels: typing.List[typing.Union['PropWebACLLabel', dict]] = attr.ib(
        default=None,
        converter=PropWebACLLabel.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropWebACLLabel), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "RuleLabels"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-rulelabels"""

@attr.s
class PropWebACLRateBasedStatement(Property):
    """
    AWS Object Type = "AWS::WAFv2::WebACL.RateBasedStatement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatement.html

    Property Document:
    
    - ``rp_AggregateKeyType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatement.html#cfn-wafv2-webacl-ratebasedstatement-aggregatekeytype
    - ``rp_Limit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatement.html#cfn-wafv2-webacl-ratebasedstatement-limit
    - ``p_ForwardedIPConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatement.html#cfn-wafv2-webacl-ratebasedstatement-forwardedipconfig
    - ``p_ScopeDownStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatement.html#cfn-wafv2-webacl-ratebasedstatement-scopedownstatement
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL.RateBasedStatement"
    
    rp_AggregateKeyType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AggregateKeyType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatement.html#cfn-wafv2-webacl-ratebasedstatement-aggregatekeytype"""
    rp_Limit: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Limit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatement.html#cfn-wafv2-webacl-ratebasedstatement-limit"""
    p_ForwardedIPConfig: typing.Union['PropWebACLForwardedIPConfiguration', dict] = attr.ib(
        default=None,
        converter=PropWebACLForwardedIPConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLForwardedIPConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "ForwardedIPConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatement.html#cfn-wafv2-webacl-ratebasedstatement-forwardedipconfig"""
    p_ScopeDownStatement: typing.Union['PropWebACLStatement', dict] = attr.ib(
        default=None,
        validator=None,
        metadata={AttrMeta.PROPERTY_NAME: "ScopeDownStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatement.html#cfn-wafv2-webacl-ratebasedstatement-scopedownstatement"""

@attr.s
class PropRuleGroupNotStatement(Property):
    """
    AWS Object Type = "AWS::WAFv2::RuleGroup.NotStatement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-notstatement.html

    Property Document:
    
    - ``rp_Statement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-notstatement.html#cfn-wafv2-rulegroup-notstatement-statement
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::RuleGroup.NotStatement"
    
    rp_Statement: typing.Union['PropRuleGroupStatement', dict] = attr.ib(
        default=None,
        validator=None,
        metadata={AttrMeta.PROPERTY_NAME: "Statement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-notstatement.html#cfn-wafv2-rulegroup-notstatement-statement"""


#--- Resource declaration ---

@attr.s
class LoggingConfiguration(Resource):
    """
    AWS Object Type = "AWS::WAFv2::LoggingConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html

    Property Document:
    
    - ``rp_LogDestinationConfigs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-logdestinationconfigs
    - ``rp_ResourceArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-resourcearn
    - ``p_LoggingFilter``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-loggingfilter
    - ``p_RedactedFields``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-redactedfields
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::LoggingConfiguration"

    
    rp_LogDestinationConfigs: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "LogDestinationConfigs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-logdestinationconfigs"""
    rp_ResourceArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-resourcearn"""
    p_LoggingFilter: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "LoggingFilter"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-loggingfilter"""
    p_RedactedFields: typing.List[typing.Union['PropLoggingConfigurationFieldToMatch', dict]] = attr.ib(
        default=None,
        converter=PropLoggingConfigurationFieldToMatch.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropLoggingConfigurationFieldToMatch), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "RedactedFields"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-redactedfields"""

    
    @property
    def rv_ManagedByFirewallManager(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#aws-resource-wafv2-loggingconfiguration-return-values"""
        return GetAtt(resource=self, attr_name="ManagedByFirewallManager")
    

@attr.s
class RegexPatternSet(Resource):
    """
    AWS Object Type = "AWS::WAFv2::RegexPatternSet"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html

    Property Document:
    
    - ``rp_RegularExpressionList``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-regularexpressionlist
    - ``rp_Scope``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-scope
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-description
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-name
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-tags
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::RegexPatternSet"

    
    rp_RegularExpressionList: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "RegularExpressionList"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-regularexpressionlist"""
    rp_Scope: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Scope"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-scope"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-description"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-name"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#aws-resource-wafv2-regexpatternset-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#aws-resource-wafv2-regexpatternset-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    

@attr.s
class IPSet(Resource):
    """
    AWS Object Type = "AWS::WAFv2::IPSet"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html

    Property Document:
    
    - ``rp_Addresses``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-addresses
    - ``rp_IPAddressVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-ipaddressversion
    - ``rp_Scope``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-scope
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-description
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-name
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-tags
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::IPSet"

    
    rp_Addresses: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Addresses"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-addresses"""
    rp_IPAddressVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "IPAddressVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-ipaddressversion"""
    rp_Scope: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Scope"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-scope"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-description"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-name"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#aws-resource-wafv2-ipset-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#aws-resource-wafv2-ipset-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    

@attr.s
class WebACLAssociation(Resource):
    """
    AWS Object Type = "AWS::WAFv2::WebACLAssociation"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webaclassociation.html

    Property Document:
    
    - ``rp_ResourceArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webaclassociation.html#cfn-wafv2-webaclassociation-resourcearn
    - ``rp_WebACLArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webaclassociation.html#cfn-wafv2-webaclassociation-webaclarn
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACLAssociation"

    
    rp_ResourceArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webaclassociation.html#cfn-wafv2-webaclassociation-resourcearn"""
    rp_WebACLArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "WebACLArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webaclassociation.html#cfn-wafv2-webaclassociation-webaclarn"""

    

@attr.s
class WebACL(Resource):
    """
    AWS Object Type = "AWS::WAFv2::WebACL"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html

    Property Document:
    
    - ``rp_DefaultAction``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-defaultaction
    - ``rp_Scope``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-scope
    - ``rp_VisibilityConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-visibilityconfig
    - ``p_CaptchaConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-captchaconfig
    - ``p_CustomResponseBodies``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-customresponsebodies
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-description
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-name
    - ``p_Rules``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-rules
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-tags
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::WebACL"

    
    rp_DefaultAction: typing.Union['PropWebACLDefaultAction', dict] = attr.ib(
        default=None,
        converter=PropWebACLDefaultAction.from_dict,
        validator=attr.validators.instance_of(PropWebACLDefaultAction),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultAction"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-defaultaction"""
    rp_Scope: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Scope"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-scope"""
    rp_VisibilityConfig: typing.Union['PropWebACLVisibilityConfig', dict] = attr.ib(
        default=None,
        converter=PropWebACLVisibilityConfig.from_dict,
        validator=attr.validators.instance_of(PropWebACLVisibilityConfig),
        metadata={AttrMeta.PROPERTY_NAME: "VisibilityConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-visibilityconfig"""
    p_CaptchaConfig: typing.Union['PropWebACLCaptchaConfig', dict] = attr.ib(
        default=None,
        converter=PropWebACLCaptchaConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLCaptchaConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "CaptchaConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-captchaconfig"""
    p_CustomResponseBodies: typing.Union['PropWebACLCustomResponseBody', dict] = attr.ib(
        default=None,
        converter=PropWebACLCustomResponseBody.from_list,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLCustomResponseBody)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomResponseBodies"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-customresponsebodies"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-description"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-name"""
    p_Rules: typing.List[typing.Union['PropWebACLRule', dict]] = attr.ib(
        default=None,
        converter=PropWebACLRule.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropWebACLRule), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Rules"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-rules"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#aws-resource-wafv2-webacl-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_Capacity(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#aws-resource-wafv2-webacl-return-values"""
        return GetAtt(resource=self, attr_name="Capacity")
    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#aws-resource-wafv2-webacl-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_LabelNamespace(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#aws-resource-wafv2-webacl-return-values"""
        return GetAtt(resource=self, attr_name="LabelNamespace")
    

@attr.s
class RuleGroup(Resource):
    """
    AWS Object Type = "AWS::WAFv2::RuleGroup"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html

    Property Document:
    
    - ``rp_Capacity``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-capacity
    - ``rp_Scope``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-scope
    - ``rp_VisibilityConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-visibilityconfig
    - ``p_CustomResponseBodies``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-customresponsebodies
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-description
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-name
    - ``p_Rules``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-rules
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-tags
    """
    AWS_OBJECT_TYPE = "AWS::WAFv2::RuleGroup"

    
    rp_Capacity: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Capacity"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-capacity"""
    rp_Scope: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Scope"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-scope"""
    rp_VisibilityConfig: typing.Union['PropRuleGroupVisibilityConfig', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupVisibilityConfig.from_dict,
        validator=attr.validators.instance_of(PropRuleGroupVisibilityConfig),
        metadata={AttrMeta.PROPERTY_NAME: "VisibilityConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-visibilityconfig"""
    p_CustomResponseBodies: typing.Union['PropRuleGroupCustomResponseBody', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupCustomResponseBody.from_list,
        validator=attr.validators.optional(attr.validators.instance_of(PropRuleGroupCustomResponseBody)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomResponseBodies"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-customresponsebodies"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-description"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-name"""
    p_Rules: typing.List[typing.Union['PropRuleGroupRule', dict]] = attr.ib(
        default=None,
        converter=PropRuleGroupRule.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropRuleGroupRule), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Rules"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-rules"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#aws-resource-wafv2-rulegroup-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#aws-resource-wafv2-rulegroup-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_LabelNamespace(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#aws-resource-wafv2-rulegroup-return-values"""
        return GetAtt(resource=self, attr_name="LabelNamespace")
    
    @property
    def rv_AvailableLabels(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#aws-resource-wafv2-rulegroup-return-values"""
        return GetAtt(resource=self, attr_name="AvailableLabels")
    
    @property
    def rv_ConsumedLabels(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#aws-resource-wafv2-rulegroup-return-values"""
        return GetAtt(resource=self, attr_name="ConsumedLabels")
    
