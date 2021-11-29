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
class PropRulePredicate(Property):
    """
    AWS Object Type = "AWS::WAFRegional::Rule.Predicate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-rule-predicate.html

    Property Document:
    
    - ``rp_DataId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-rule-predicate.html#cfn-wafregional-rule-predicate-dataid
    - ``rp_Negated``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-rule-predicate.html#cfn-wafregional-rule-predicate-negated
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-rule-predicate.html#cfn-wafregional-rule-predicate-type
    """
    AWS_OBJECT_TYPE = "AWS::WAFRegional::Rule.Predicate"
    
    rp_DataId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DataId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-rule-predicate.html#cfn-wafregional-rule-predicate-dataid"""
    rp_Negated: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Negated"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-rule-predicate.html#cfn-wafregional-rule-predicate-negated"""
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-rule-predicate.html#cfn-wafregional-rule-predicate-type"""

@attr.s
class PropByteMatchSetFieldToMatch(Property):
    """
    AWS Object Type = "AWS::WAFRegional::ByteMatchSet.FieldToMatch"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-fieldtomatch.html

    Property Document:
    
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-fieldtomatch.html#cfn-wafregional-bytematchset-fieldtomatch-type
    - ``p_Data``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-fieldtomatch.html#cfn-wafregional-bytematchset-fieldtomatch-data
    """
    AWS_OBJECT_TYPE = "AWS::WAFRegional::ByteMatchSet.FieldToMatch"
    
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-fieldtomatch.html#cfn-wafregional-bytematchset-fieldtomatch-type"""
    p_Data: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Data"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-fieldtomatch.html#cfn-wafregional-bytematchset-fieldtomatch-data"""

@attr.s
class PropSizeConstraintSetFieldToMatch(Property):
    """
    AWS Object Type = "AWS::WAFRegional::SizeConstraintSet.FieldToMatch"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-fieldtomatch.html

    Property Document:
    
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-fieldtomatch.html#cfn-wafregional-sizeconstraintset-fieldtomatch-type
    - ``p_Data``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-fieldtomatch.html#cfn-wafregional-sizeconstraintset-fieldtomatch-data
    """
    AWS_OBJECT_TYPE = "AWS::WAFRegional::SizeConstraintSet.FieldToMatch"
    
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-fieldtomatch.html#cfn-wafregional-sizeconstraintset-fieldtomatch-type"""
    p_Data: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Data"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-fieldtomatch.html#cfn-wafregional-sizeconstraintset-fieldtomatch-data"""

@attr.s
class PropGeoMatchSetGeoMatchConstraint(Property):
    """
    AWS Object Type = "AWS::WAFRegional::GeoMatchSet.GeoMatchConstraint"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-geomatchset-geomatchconstraint.html

    Property Document:
    
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-geomatchset-geomatchconstraint.html#cfn-wafregional-geomatchset-geomatchconstraint-type
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-geomatchset-geomatchconstraint.html#cfn-wafregional-geomatchset-geomatchconstraint-value
    """
    AWS_OBJECT_TYPE = "AWS::WAFRegional::GeoMatchSet.GeoMatchConstraint"
    
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-geomatchset-geomatchconstraint.html#cfn-wafregional-geomatchset-geomatchconstraint-type"""
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-geomatchset-geomatchconstraint.html#cfn-wafregional-geomatchset-geomatchconstraint-value"""

@attr.s
class PropSqlInjectionMatchSetFieldToMatch(Property):
    """
    AWS Object Type = "AWS::WAFRegional::SqlInjectionMatchSet.FieldToMatch"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-fieldtomatch.html

    Property Document:
    
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-fieldtomatch.html#cfn-wafregional-sqlinjectionmatchset-fieldtomatch-type
    - ``p_Data``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-fieldtomatch.html#cfn-wafregional-sqlinjectionmatchset-fieldtomatch-data
    """
    AWS_OBJECT_TYPE = "AWS::WAFRegional::SqlInjectionMatchSet.FieldToMatch"
    
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-fieldtomatch.html#cfn-wafregional-sqlinjectionmatchset-fieldtomatch-type"""
    p_Data: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Data"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-fieldtomatch.html#cfn-wafregional-sqlinjectionmatchset-fieldtomatch-data"""

@attr.s
class PropWebACLAction(Property):
    """
    AWS Object Type = "AWS::WAFRegional::WebACL.Action"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-action.html

    Property Document:
    
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-action.html#cfn-wafregional-webacl-action-type
    """
    AWS_OBJECT_TYPE = "AWS::WAFRegional::WebACL.Action"
    
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-action.html#cfn-wafregional-webacl-action-type"""

@attr.s
class PropSqlInjectionMatchSetSqlInjectionMatchTuple(Property):
    """
    AWS Object Type = "AWS::WAFRegional::SqlInjectionMatchSet.SqlInjectionMatchTuple"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple.html

    Property Document:
    
    - ``rp_FieldToMatch``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple.html#cfn-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple-fieldtomatch
    - ``rp_TextTransformation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple.html#cfn-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple-texttransformation
    """
    AWS_OBJECT_TYPE = "AWS::WAFRegional::SqlInjectionMatchSet.SqlInjectionMatchTuple"
    
    rp_FieldToMatch: typing.Union['PropSqlInjectionMatchSetFieldToMatch', dict] = attr.ib(
        default=None,
        converter=PropSqlInjectionMatchSetFieldToMatch.from_dict,
        validator=attr.validators.instance_of(PropSqlInjectionMatchSetFieldToMatch),
        metadata={AttrMeta.PROPERTY_NAME: "FieldToMatch"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple.html#cfn-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple-fieldtomatch"""
    rp_TextTransformation: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TextTransformation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple.html#cfn-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple-texttransformation"""

@attr.s
class PropWebACLRule(Property):
    """
    AWS Object Type = "AWS::WAFRegional::WebACL.Rule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-rule.html

    Property Document:
    
    - ``rp_Action``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-rule.html#cfn-wafregional-webacl-rule-action
    - ``rp_Priority``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-rule.html#cfn-wafregional-webacl-rule-priority
    - ``rp_RuleId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-rule.html#cfn-wafregional-webacl-rule-ruleid
    """
    AWS_OBJECT_TYPE = "AWS::WAFRegional::WebACL.Rule"
    
    rp_Action: typing.Union['PropWebACLAction', dict] = attr.ib(
        default=None,
        converter=PropWebACLAction.from_dict,
        validator=attr.validators.instance_of(PropWebACLAction),
        metadata={AttrMeta.PROPERTY_NAME: "Action"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-rule.html#cfn-wafregional-webacl-rule-action"""
    rp_Priority: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Priority"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-rule.html#cfn-wafregional-webacl-rule-priority"""
    rp_RuleId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RuleId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-rule.html#cfn-wafregional-webacl-rule-ruleid"""

@attr.s
class PropIPSetIPSetDescriptor(Property):
    """
    AWS Object Type = "AWS::WAFRegional::IPSet.IPSetDescriptor"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ipset-ipsetdescriptor.html

    Property Document:
    
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ipset-ipsetdescriptor.html#cfn-wafregional-ipset-ipsetdescriptor-type
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ipset-ipsetdescriptor.html#cfn-wafregional-ipset-ipsetdescriptor-value
    """
    AWS_OBJECT_TYPE = "AWS::WAFRegional::IPSet.IPSetDescriptor"
    
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ipset-ipsetdescriptor.html#cfn-wafregional-ipset-ipsetdescriptor-type"""
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ipset-ipsetdescriptor.html#cfn-wafregional-ipset-ipsetdescriptor-value"""

@attr.s
class PropXssMatchSetFieldToMatch(Property):
    """
    AWS Object Type = "AWS::WAFRegional::XssMatchSet.FieldToMatch"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-fieldtomatch.html

    Property Document:
    
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-fieldtomatch.html#cfn-wafregional-xssmatchset-fieldtomatch-type
    - ``p_Data``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-fieldtomatch.html#cfn-wafregional-xssmatchset-fieldtomatch-data
    """
    AWS_OBJECT_TYPE = "AWS::WAFRegional::XssMatchSet.FieldToMatch"
    
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-fieldtomatch.html#cfn-wafregional-xssmatchset-fieldtomatch-type"""
    p_Data: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Data"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-fieldtomatch.html#cfn-wafregional-xssmatchset-fieldtomatch-data"""

@attr.s
class PropRateBasedRulePredicate(Property):
    """
    AWS Object Type = "AWS::WAFRegional::RateBasedRule.Predicate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ratebasedrule-predicate.html

    Property Document:
    
    - ``rp_DataId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ratebasedrule-predicate.html#cfn-wafregional-ratebasedrule-predicate-dataid
    - ``rp_Negated``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ratebasedrule-predicate.html#cfn-wafregional-ratebasedrule-predicate-negated
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ratebasedrule-predicate.html#cfn-wafregional-ratebasedrule-predicate-type
    """
    AWS_OBJECT_TYPE = "AWS::WAFRegional::RateBasedRule.Predicate"
    
    rp_DataId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DataId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ratebasedrule-predicate.html#cfn-wafregional-ratebasedrule-predicate-dataid"""
    rp_Negated: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Negated"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ratebasedrule-predicate.html#cfn-wafregional-ratebasedrule-predicate-negated"""
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ratebasedrule-predicate.html#cfn-wafregional-ratebasedrule-predicate-type"""

@attr.s
class PropByteMatchSetByteMatchTuple(Property):
    """
    AWS Object Type = "AWS::WAFRegional::ByteMatchSet.ByteMatchTuple"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html

    Property Document:
    
    - ``rp_FieldToMatch``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html#cfn-wafregional-bytematchset-bytematchtuple-fieldtomatch
    - ``rp_PositionalConstraint``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html#cfn-wafregional-bytematchset-bytematchtuple-positionalconstraint
    - ``rp_TextTransformation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html#cfn-wafregional-bytematchset-bytematchtuple-texttransformation
    - ``p_TargetString``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html#cfn-wafregional-bytematchset-bytematchtuple-targetstring
    - ``p_TargetStringBase64``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html#cfn-wafregional-bytematchset-bytematchtuple-targetstringbase64
    """
    AWS_OBJECT_TYPE = "AWS::WAFRegional::ByteMatchSet.ByteMatchTuple"
    
    rp_FieldToMatch: typing.Union['PropByteMatchSetFieldToMatch', dict] = attr.ib(
        default=None,
        converter=PropByteMatchSetFieldToMatch.from_dict,
        validator=attr.validators.instance_of(PropByteMatchSetFieldToMatch),
        metadata={AttrMeta.PROPERTY_NAME: "FieldToMatch"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html#cfn-wafregional-bytematchset-bytematchtuple-fieldtomatch"""
    rp_PositionalConstraint: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PositionalConstraint"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html#cfn-wafregional-bytematchset-bytematchtuple-positionalconstraint"""
    rp_TextTransformation: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TextTransformation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html#cfn-wafregional-bytematchset-bytematchtuple-texttransformation"""
    p_TargetString: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TargetString"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html#cfn-wafregional-bytematchset-bytematchtuple-targetstring"""
    p_TargetStringBase64: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TargetStringBase64"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html#cfn-wafregional-bytematchset-bytematchtuple-targetstringbase64"""

@attr.s
class PropSizeConstraintSetSizeConstraint(Property):
    """
    AWS Object Type = "AWS::WAFRegional::SizeConstraintSet.SizeConstraint"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html

    Property Document:
    
    - ``rp_ComparisonOperator``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html#cfn-wafregional-sizeconstraintset-sizeconstraint-comparisonoperator
    - ``rp_FieldToMatch``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html#cfn-wafregional-sizeconstraintset-sizeconstraint-fieldtomatch
    - ``rp_Size``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html#cfn-wafregional-sizeconstraintset-sizeconstraint-size
    - ``rp_TextTransformation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html#cfn-wafregional-sizeconstraintset-sizeconstraint-texttransformation
    """
    AWS_OBJECT_TYPE = "AWS::WAFRegional::SizeConstraintSet.SizeConstraint"
    
    rp_ComparisonOperator: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ComparisonOperator"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html#cfn-wafregional-sizeconstraintset-sizeconstraint-comparisonoperator"""
    rp_FieldToMatch: typing.Union['PropSizeConstraintSetFieldToMatch', dict] = attr.ib(
        default=None,
        converter=PropSizeConstraintSetFieldToMatch.from_dict,
        validator=attr.validators.instance_of(PropSizeConstraintSetFieldToMatch),
        metadata={AttrMeta.PROPERTY_NAME: "FieldToMatch"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html#cfn-wafregional-sizeconstraintset-sizeconstraint-fieldtomatch"""
    rp_Size: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Size"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html#cfn-wafregional-sizeconstraintset-sizeconstraint-size"""
    rp_TextTransformation: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TextTransformation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html#cfn-wafregional-sizeconstraintset-sizeconstraint-texttransformation"""

@attr.s
class PropXssMatchSetXssMatchTuple(Property):
    """
    AWS Object Type = "AWS::WAFRegional::XssMatchSet.XssMatchTuple"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-xssmatchtuple.html

    Property Document:
    
    - ``rp_FieldToMatch``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-xssmatchtuple.html#cfn-wafregional-xssmatchset-xssmatchtuple-fieldtomatch
    - ``rp_TextTransformation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-xssmatchtuple.html#cfn-wafregional-xssmatchset-xssmatchtuple-texttransformation
    """
    AWS_OBJECT_TYPE = "AWS::WAFRegional::XssMatchSet.XssMatchTuple"
    
    rp_FieldToMatch: typing.Union['PropXssMatchSetFieldToMatch', dict] = attr.ib(
        default=None,
        converter=PropXssMatchSetFieldToMatch.from_dict,
        validator=attr.validators.instance_of(PropXssMatchSetFieldToMatch),
        metadata={AttrMeta.PROPERTY_NAME: "FieldToMatch"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-xssmatchtuple.html#cfn-wafregional-xssmatchset-xssmatchtuple-fieldtomatch"""
    rp_TextTransformation: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TextTransformation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-xssmatchtuple.html#cfn-wafregional-xssmatchset-xssmatchtuple-texttransformation"""


#--- Resource declaration ---

@attr.s
class SqlInjectionMatchSet(Resource):
    """
    AWS Object Type = "AWS::WAFRegional::SqlInjectionMatchSet"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sqlinjectionmatchset.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sqlinjectionmatchset.html#cfn-wafregional-sqlinjectionmatchset-name
    - ``p_SqlInjectionMatchTuples``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sqlinjectionmatchset.html#cfn-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuples
    """
    AWS_OBJECT_TYPE = "AWS::WAFRegional::SqlInjectionMatchSet"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sqlinjectionmatchset.html#cfn-wafregional-sqlinjectionmatchset-name"""
    p_SqlInjectionMatchTuples: typing.List[typing.Union['PropSqlInjectionMatchSetSqlInjectionMatchTuple', dict]] = attr.ib(
        default=None,
        converter=PropSqlInjectionMatchSetSqlInjectionMatchTuple.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropSqlInjectionMatchSetSqlInjectionMatchTuple), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SqlInjectionMatchTuples"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sqlinjectionmatchset.html#cfn-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuples"""

    

@attr.s
class RegexPatternSet(Resource):
    """
    AWS Object Type = "AWS::WAFRegional::RegexPatternSet"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-regexpatternset.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-regexpatternset.html#cfn-wafregional-regexpatternset-name
    - ``rp_RegexPatternStrings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-regexpatternset.html#cfn-wafregional-regexpatternset-regexpatternstrings
    """
    AWS_OBJECT_TYPE = "AWS::WAFRegional::RegexPatternSet"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-regexpatternset.html#cfn-wafregional-regexpatternset-name"""
    rp_RegexPatternStrings: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "RegexPatternStrings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-regexpatternset.html#cfn-wafregional-regexpatternset-regexpatternstrings"""

    

@attr.s
class WebACLAssociation(Resource):
    """
    AWS Object Type = "AWS::WAFRegional::WebACLAssociation"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webaclassociation.html

    Property Document:
    
    - ``rp_ResourceArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webaclassociation.html#cfn-wafregional-webaclassociation-resourcearn
    - ``rp_WebACLId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webaclassociation.html#cfn-wafregional-webaclassociation-webaclid
    """
    AWS_OBJECT_TYPE = "AWS::WAFRegional::WebACLAssociation"

    
    rp_ResourceArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webaclassociation.html#cfn-wafregional-webaclassociation-resourcearn"""
    rp_WebACLId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "WebACLId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webaclassociation.html#cfn-wafregional-webaclassociation-webaclid"""

    

@attr.s
class SizeConstraintSet(Resource):
    """
    AWS Object Type = "AWS::WAFRegional::SizeConstraintSet"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sizeconstraintset.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sizeconstraintset.html#cfn-wafregional-sizeconstraintset-name
    - ``p_SizeConstraints``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sizeconstraintset.html#cfn-wafregional-sizeconstraintset-sizeconstraints
    """
    AWS_OBJECT_TYPE = "AWS::WAFRegional::SizeConstraintSet"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sizeconstraintset.html#cfn-wafregional-sizeconstraintset-name"""
    p_SizeConstraints: typing.List[typing.Union['PropSizeConstraintSetSizeConstraint', dict]] = attr.ib(
        default=None,
        converter=PropSizeConstraintSetSizeConstraint.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropSizeConstraintSetSizeConstraint), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SizeConstraints"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sizeconstraintset.html#cfn-wafregional-sizeconstraintset-sizeconstraints"""

    

@attr.s
class XssMatchSet(Resource):
    """
    AWS Object Type = "AWS::WAFRegional::XssMatchSet"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-xssmatchset.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-xssmatchset.html#cfn-wafregional-xssmatchset-name
    - ``p_XssMatchTuples``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-xssmatchset.html#cfn-wafregional-xssmatchset-xssmatchtuples
    """
    AWS_OBJECT_TYPE = "AWS::WAFRegional::XssMatchSet"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-xssmatchset.html#cfn-wafregional-xssmatchset-name"""
    p_XssMatchTuples: typing.List[typing.Union['PropXssMatchSetXssMatchTuple', dict]] = attr.ib(
        default=None,
        converter=PropXssMatchSetXssMatchTuple.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropXssMatchSetXssMatchTuple), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "XssMatchTuples"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-xssmatchset.html#cfn-wafregional-xssmatchset-xssmatchtuples"""

    

@attr.s
class RateBasedRule(Resource):
    """
    AWS Object Type = "AWS::WAFRegional::RateBasedRule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ratebasedrule.html

    Property Document:
    
    - ``rp_MetricName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ratebasedrule.html#cfn-wafregional-ratebasedrule-metricname
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ratebasedrule.html#cfn-wafregional-ratebasedrule-name
    - ``rp_RateKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ratebasedrule.html#cfn-wafregional-ratebasedrule-ratekey
    - ``rp_RateLimit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ratebasedrule.html#cfn-wafregional-ratebasedrule-ratelimit
    - ``p_MatchPredicates``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ratebasedrule.html#cfn-wafregional-ratebasedrule-matchpredicates
    """
    AWS_OBJECT_TYPE = "AWS::WAFRegional::RateBasedRule"

    
    rp_MetricName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "MetricName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ratebasedrule.html#cfn-wafregional-ratebasedrule-metricname"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ratebasedrule.html#cfn-wafregional-ratebasedrule-name"""
    rp_RateKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RateKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ratebasedrule.html#cfn-wafregional-ratebasedrule-ratekey"""
    rp_RateLimit: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "RateLimit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ratebasedrule.html#cfn-wafregional-ratebasedrule-ratelimit"""
    p_MatchPredicates: typing.List[typing.Union['PropRateBasedRulePredicate', dict]] = attr.ib(
        default=None,
        converter=PropRateBasedRulePredicate.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropRateBasedRulePredicate), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "MatchPredicates"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ratebasedrule.html#cfn-wafregional-ratebasedrule-matchpredicates"""

    

@attr.s
class GeoMatchSet(Resource):
    """
    AWS Object Type = "AWS::WAFRegional::GeoMatchSet"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-geomatchset.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-geomatchset.html#cfn-wafregional-geomatchset-name
    - ``p_GeoMatchConstraints``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-geomatchset.html#cfn-wafregional-geomatchset-geomatchconstraints
    """
    AWS_OBJECT_TYPE = "AWS::WAFRegional::GeoMatchSet"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-geomatchset.html#cfn-wafregional-geomatchset-name"""
    p_GeoMatchConstraints: typing.List[typing.Union['PropGeoMatchSetGeoMatchConstraint', dict]] = attr.ib(
        default=None,
        converter=PropGeoMatchSetGeoMatchConstraint.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropGeoMatchSetGeoMatchConstraint), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "GeoMatchConstraints"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-geomatchset.html#cfn-wafregional-geomatchset-geomatchconstraints"""

    

@attr.s
class WebACL(Resource):
    """
    AWS Object Type = "AWS::WAFRegional::WebACL"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html

    Property Document:
    
    - ``rp_DefaultAction``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html#cfn-wafregional-webacl-defaultaction
    - ``rp_MetricName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html#cfn-wafregional-webacl-metricname
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html#cfn-wafregional-webacl-name
    - ``p_Rules``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html#cfn-wafregional-webacl-rules
    """
    AWS_OBJECT_TYPE = "AWS::WAFRegional::WebACL"

    
    rp_DefaultAction: typing.Union['PropWebACLAction', dict] = attr.ib(
        default=None,
        converter=PropWebACLAction.from_dict,
        validator=attr.validators.instance_of(PropWebACLAction),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultAction"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html#cfn-wafregional-webacl-defaultaction"""
    rp_MetricName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "MetricName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html#cfn-wafregional-webacl-metricname"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html#cfn-wafregional-webacl-name"""
    p_Rules: typing.List[typing.Union['PropWebACLRule', dict]] = attr.ib(
        default=None,
        converter=PropWebACLRule.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropWebACLRule), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Rules"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html#cfn-wafregional-webacl-rules"""

    

@attr.s
class IPSet(Resource):
    """
    AWS Object Type = "AWS::WAFRegional::IPSet"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ipset.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ipset.html#cfn-wafregional-ipset-name
    - ``p_IPSetDescriptors``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ipset.html#cfn-wafregional-ipset-ipsetdescriptors
    """
    AWS_OBJECT_TYPE = "AWS::WAFRegional::IPSet"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ipset.html#cfn-wafregional-ipset-name"""
    p_IPSetDescriptors: typing.List[typing.Union['PropIPSetIPSetDescriptor', dict]] = attr.ib(
        default=None,
        converter=PropIPSetIPSetDescriptor.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropIPSetIPSetDescriptor), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "IPSetDescriptors"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ipset.html#cfn-wafregional-ipset-ipsetdescriptors"""

    

@attr.s
class ByteMatchSet(Resource):
    """
    AWS Object Type = "AWS::WAFRegional::ByteMatchSet"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-bytematchset.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-bytematchset.html#cfn-wafregional-bytematchset-name
    - ``p_ByteMatchTuples``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-bytematchset.html#cfn-wafregional-bytematchset-bytematchtuples
    """
    AWS_OBJECT_TYPE = "AWS::WAFRegional::ByteMatchSet"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-bytematchset.html#cfn-wafregional-bytematchset-name"""
    p_ByteMatchTuples: typing.List[typing.Union['PropByteMatchSetByteMatchTuple', dict]] = attr.ib(
        default=None,
        converter=PropByteMatchSetByteMatchTuple.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropByteMatchSetByteMatchTuple), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ByteMatchTuples"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-bytematchset.html#cfn-wafregional-bytematchset-bytematchtuples"""

    

@attr.s
class Rule(Resource):
    """
    AWS Object Type = "AWS::WAFRegional::Rule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-rule.html

    Property Document:
    
    - ``rp_MetricName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-rule.html#cfn-wafregional-rule-metricname
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-rule.html#cfn-wafregional-rule-name
    - ``p_Predicates``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-rule.html#cfn-wafregional-rule-predicates
    """
    AWS_OBJECT_TYPE = "AWS::WAFRegional::Rule"

    
    rp_MetricName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "MetricName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-rule.html#cfn-wafregional-rule-metricname"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-rule.html#cfn-wafregional-rule-name"""
    p_Predicates: typing.List[typing.Union['PropRulePredicate', dict]] = attr.ib(
        default=None,
        converter=PropRulePredicate.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropRulePredicate), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Predicates"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-rule.html#cfn-wafregional-rule-predicates"""

    
