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
class PropWebACLWafAction(Property):
    """
    AWS Object Type = "AWS::WAF::WebACL.WafAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-webacl-action.html

    Property Document:
    
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-webacl-action.html#cfn-waf-webacl-action-type
    """
    AWS_OBJECT_TYPE = "AWS::WAF::WebACL.WafAction"
    
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-webacl-action.html#cfn-waf-webacl-action-type"""

@attr.s
class PropIPSetIPSetDescriptor(Property):
    """
    AWS Object Type = "AWS::WAF::IPSet.IPSetDescriptor"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-ipset-ipsetdescriptors.html

    Property Document:
    
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-ipset-ipsetdescriptors.html#cfn-waf-ipset-ipsetdescriptors-type
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-ipset-ipsetdescriptors.html#cfn-waf-ipset-ipsetdescriptors-value
    """
    AWS_OBJECT_TYPE = "AWS::WAF::IPSet.IPSetDescriptor"
    
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-ipset-ipsetdescriptors.html#cfn-waf-ipset-ipsetdescriptors-type"""
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-ipset-ipsetdescriptors.html#cfn-waf-ipset-ipsetdescriptors-value"""

@attr.s
class PropByteMatchSetFieldToMatch(Property):
    """
    AWS Object Type = "AWS::WAF::ByteMatchSet.FieldToMatch"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples-fieldtomatch.html

    Property Document:
    
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples-fieldtomatch.html#cfn-waf-bytematchset-bytematchtuples-fieldtomatch-type
    - ``p_Data``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples-fieldtomatch.html#cfn-waf-bytematchset-bytematchtuples-fieldtomatch-data
    """
    AWS_OBJECT_TYPE = "AWS::WAF::ByteMatchSet.FieldToMatch"
    
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples-fieldtomatch.html#cfn-waf-bytematchset-bytematchtuples-fieldtomatch-type"""
    p_Data: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Data"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples-fieldtomatch.html#cfn-waf-bytematchset-bytematchtuples-fieldtomatch-data"""

@attr.s
class PropSqlInjectionMatchSetFieldToMatch(Property):
    """
    AWS Object Type = "AWS::WAF::SqlInjectionMatchSet.FieldToMatch"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples-fieldtomatch.html

    Property Document:
    
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples-fieldtomatch.html#cfn-waf-sizeconstraintset-sizeconstraint-fieldtomatch-type
    - ``p_Data``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples-fieldtomatch.html#cfn-waf-sizeconstraintset-sizeconstraint-fieldtomatch-data
    """
    AWS_OBJECT_TYPE = "AWS::WAF::SqlInjectionMatchSet.FieldToMatch"
    
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples-fieldtomatch.html#cfn-waf-sizeconstraintset-sizeconstraint-fieldtomatch-type"""
    p_Data: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Data"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples-fieldtomatch.html#cfn-waf-sizeconstraintset-sizeconstraint-fieldtomatch-data"""

@attr.s
class PropByteMatchSetByteMatchTuple(Property):
    """
    AWS Object Type = "AWS::WAF::ByteMatchSet.ByteMatchTuple"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples.html

    Property Document:
    
    - ``rp_FieldToMatch``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples.html#cfn-waf-bytematchset-bytematchtuples-fieldtomatch
    - ``rp_PositionalConstraint``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples.html#cfn-waf-bytematchset-bytematchtuples-positionalconstraint
    - ``rp_TextTransformation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples.html#cfn-waf-bytematchset-bytematchtuples-texttransformation
    - ``p_TargetString``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples.html#cfn-waf-bytematchset-bytematchtuples-targetstring
    - ``p_TargetStringBase64``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples.html#cfn-waf-bytematchset-bytematchtuples-targetstringbase64
    """
    AWS_OBJECT_TYPE = "AWS::WAF::ByteMatchSet.ByteMatchTuple"
    
    rp_FieldToMatch: typing.Union['PropByteMatchSetFieldToMatch', dict] = attr.ib(
        default=None,
        converter=PropByteMatchSetFieldToMatch.from_dict,
        validator=attr.validators.instance_of(PropByteMatchSetFieldToMatch),
        metadata={AttrMeta.PROPERTY_NAME: "FieldToMatch"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples.html#cfn-waf-bytematchset-bytematchtuples-fieldtomatch"""
    rp_PositionalConstraint: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PositionalConstraint"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples.html#cfn-waf-bytematchset-bytematchtuples-positionalconstraint"""
    rp_TextTransformation: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TextTransformation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples.html#cfn-waf-bytematchset-bytematchtuples-texttransformation"""
    p_TargetString: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TargetString"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples.html#cfn-waf-bytematchset-bytematchtuples-targetstring"""
    p_TargetStringBase64: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TargetStringBase64"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples.html#cfn-waf-bytematchset-bytematchtuples-targetstringbase64"""

@attr.s
class PropSqlInjectionMatchSetSqlInjectionMatchTuple(Property):
    """
    AWS Object Type = "AWS::WAF::SqlInjectionMatchSet.SqlInjectionMatchTuple"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sqlinjectionmatchset-sqlinjectionmatchtuples.html

    Property Document:
    
    - ``rp_FieldToMatch``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sqlinjectionmatchset-sqlinjectionmatchtuples.html#cfn-waf-sqlinjectionmatchset-sqlinjectionmatchtuples-fieldtomatch
    - ``rp_TextTransformation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sqlinjectionmatchset-sqlinjectionmatchtuples.html#cfn-waf-sqlinjectionmatchset-sqlinjectionmatchtuples-texttransformation
    """
    AWS_OBJECT_TYPE = "AWS::WAF::SqlInjectionMatchSet.SqlInjectionMatchTuple"
    
    rp_FieldToMatch: typing.Union['PropSqlInjectionMatchSetFieldToMatch', dict] = attr.ib(
        default=None,
        converter=PropSqlInjectionMatchSetFieldToMatch.from_dict,
        validator=attr.validators.instance_of(PropSqlInjectionMatchSetFieldToMatch),
        metadata={AttrMeta.PROPERTY_NAME: "FieldToMatch"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sqlinjectionmatchset-sqlinjectionmatchtuples.html#cfn-waf-sqlinjectionmatchset-sqlinjectionmatchtuples-fieldtomatch"""
    rp_TextTransformation: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TextTransformation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sqlinjectionmatchset-sqlinjectionmatchtuples.html#cfn-waf-sqlinjectionmatchset-sqlinjectionmatchtuples-texttransformation"""

@attr.s
class PropWebACLActivatedRule(Property):
    """
    AWS Object Type = "AWS::WAF::WebACL.ActivatedRule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-webacl-rules.html

    Property Document:
    
    - ``rp_Priority``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-webacl-rules.html#cfn-waf-webacl-rules-priority
    - ``rp_RuleId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-webacl-rules.html#cfn-waf-webacl-rules-ruleid
    - ``p_Action``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-webacl-rules.html#cfn-waf-webacl-rules-action
    """
    AWS_OBJECT_TYPE = "AWS::WAF::WebACL.ActivatedRule"
    
    rp_Priority: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Priority"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-webacl-rules.html#cfn-waf-webacl-rules-priority"""
    rp_RuleId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RuleId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-webacl-rules.html#cfn-waf-webacl-rules-ruleid"""
    p_Action: typing.Union['PropWebACLWafAction', dict] = attr.ib(
        default=None,
        converter=PropWebACLWafAction.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWebACLWafAction)),
        metadata={AttrMeta.PROPERTY_NAME: "Action"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-webacl-rules.html#cfn-waf-webacl-rules-action"""

@attr.s
class PropRulePredicate(Property):
    """
    AWS Object Type = "AWS::WAF::Rule.Predicate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-rule-predicates.html

    Property Document:
    
    - ``rp_DataId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-rule-predicates.html#cfn-waf-rule-predicates-dataid
    - ``rp_Negated``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-rule-predicates.html#cfn-waf-rule-predicates-negated
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-rule-predicates.html#cfn-waf-rule-predicates-type
    """
    AWS_OBJECT_TYPE = "AWS::WAF::Rule.Predicate"
    
    rp_DataId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DataId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-rule-predicates.html#cfn-waf-rule-predicates-dataid"""
    rp_Negated: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Negated"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-rule-predicates.html#cfn-waf-rule-predicates-negated"""
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-rule-predicates.html#cfn-waf-rule-predicates-type"""

@attr.s
class PropXssMatchSetFieldToMatch(Property):
    """
    AWS Object Type = "AWS::WAF::XssMatchSet.FieldToMatch"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-xssmatchset-xssmatchtuple-fieldtomatch.html

    Property Document:
    
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-xssmatchset-xssmatchtuple-fieldtomatch.html#cfn-waf-xssmatchset-xssmatchtuple-fieldtomatch-type
    - ``p_Data``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-xssmatchset-xssmatchtuple-fieldtomatch.html#cfn-waf-xssmatchset-xssmatchtuple-fieldtomatch-data
    """
    AWS_OBJECT_TYPE = "AWS::WAF::XssMatchSet.FieldToMatch"
    
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-xssmatchset-xssmatchtuple-fieldtomatch.html#cfn-waf-xssmatchset-xssmatchtuple-fieldtomatch-type"""
    p_Data: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Data"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-xssmatchset-xssmatchtuple-fieldtomatch.html#cfn-waf-xssmatchset-xssmatchtuple-fieldtomatch-data"""

@attr.s
class PropSizeConstraintSetFieldToMatch(Property):
    """
    AWS Object Type = "AWS::WAF::SizeConstraintSet.FieldToMatch"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint-fieldtomatch.html

    Property Document:
    
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint-fieldtomatch.html#cfn-waf-sizeconstraintset-sizeconstraint-fieldtomatch-type
    - ``p_Data``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint-fieldtomatch.html#cfn-waf-sizeconstraintset-sizeconstraint-fieldtomatch-data
    """
    AWS_OBJECT_TYPE = "AWS::WAF::SizeConstraintSet.FieldToMatch"
    
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint-fieldtomatch.html#cfn-waf-sizeconstraintset-sizeconstraint-fieldtomatch-type"""
    p_Data: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Data"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint-fieldtomatch.html#cfn-waf-sizeconstraintset-sizeconstraint-fieldtomatch-data"""

@attr.s
class PropSizeConstraintSetSizeConstraint(Property):
    """
    AWS Object Type = "AWS::WAF::SizeConstraintSet.SizeConstraint"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint.html

    Property Document:
    
    - ``rp_ComparisonOperator``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint.html#cfn-waf-sizeconstraintset-sizeconstraint-comparisonoperator
    - ``rp_FieldToMatch``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint.html#cfn-waf-sizeconstraintset-sizeconstraint-fieldtomatch
    - ``rp_Size``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint.html#cfn-waf-sizeconstraintset-sizeconstraint-size
    - ``rp_TextTransformation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint.html#cfn-waf-sizeconstraintset-sizeconstraint-texttransformation
    """
    AWS_OBJECT_TYPE = "AWS::WAF::SizeConstraintSet.SizeConstraint"
    
    rp_ComparisonOperator: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ComparisonOperator"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint.html#cfn-waf-sizeconstraintset-sizeconstraint-comparisonoperator"""
    rp_FieldToMatch: typing.Union['PropSizeConstraintSetFieldToMatch', dict] = attr.ib(
        default=None,
        converter=PropSizeConstraintSetFieldToMatch.from_dict,
        validator=attr.validators.instance_of(PropSizeConstraintSetFieldToMatch),
        metadata={AttrMeta.PROPERTY_NAME: "FieldToMatch"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint.html#cfn-waf-sizeconstraintset-sizeconstraint-fieldtomatch"""
    rp_Size: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Size"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint.html#cfn-waf-sizeconstraintset-sizeconstraint-size"""
    rp_TextTransformation: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TextTransformation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint.html#cfn-waf-sizeconstraintset-sizeconstraint-texttransformation"""

@attr.s
class PropXssMatchSetXssMatchTuple(Property):
    """
    AWS Object Type = "AWS::WAF::XssMatchSet.XssMatchTuple"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-xssmatchset-xssmatchtuple.html

    Property Document:
    
    - ``rp_FieldToMatch``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-xssmatchset-xssmatchtuple.html#cfn-waf-xssmatchset-xssmatchtuple-fieldtomatch
    - ``rp_TextTransformation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-xssmatchset-xssmatchtuple.html#cfn-waf-xssmatchset-xssmatchtuple-texttransformation
    """
    AWS_OBJECT_TYPE = "AWS::WAF::XssMatchSet.XssMatchTuple"
    
    rp_FieldToMatch: typing.Union['PropXssMatchSetFieldToMatch', dict] = attr.ib(
        default=None,
        converter=PropXssMatchSetFieldToMatch.from_dict,
        validator=attr.validators.instance_of(PropXssMatchSetFieldToMatch),
        metadata={AttrMeta.PROPERTY_NAME: "FieldToMatch"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-xssmatchset-xssmatchtuple.html#cfn-waf-xssmatchset-xssmatchtuple-fieldtomatch"""
    rp_TextTransformation: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TextTransformation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-xssmatchset-xssmatchtuple.html#cfn-waf-xssmatchset-xssmatchtuple-texttransformation"""


#--- Resource declaration ---

@attr.s
class IPSet(Resource):
    """
    AWS Object Type = "AWS::WAF::IPSet"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-ipset.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-ipset.html#cfn-waf-ipset-name
    - ``p_IPSetDescriptors``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-ipset.html#cfn-waf-ipset-ipsetdescriptors
    """
    AWS_OBJECT_TYPE = "AWS::WAF::IPSet"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-ipset.html#cfn-waf-ipset-name"""
    p_IPSetDescriptors: typing.List[typing.Union['PropIPSetIPSetDescriptor', dict]] = attr.ib(
        default=None,
        converter=PropIPSetIPSetDescriptor.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropIPSetIPSetDescriptor), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "IPSetDescriptors"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-ipset.html#cfn-waf-ipset-ipsetdescriptors"""

    

@attr.s
class SizeConstraintSet(Resource):
    """
    AWS Object Type = "AWS::WAF::SizeConstraintSet"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sizeconstraintset.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sizeconstraintset.html#cfn-waf-sizeconstraintset-name
    - ``rp_SizeConstraints``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sizeconstraintset.html#cfn-waf-sizeconstraintset-sizeconstraints
    """
    AWS_OBJECT_TYPE = "AWS::WAF::SizeConstraintSet"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sizeconstraintset.html#cfn-waf-sizeconstraintset-name"""
    rp_SizeConstraints: typing.List[typing.Union['PropSizeConstraintSetSizeConstraint', dict]] = attr.ib(
        default=None,
        converter=PropSizeConstraintSetSizeConstraint.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropSizeConstraintSetSizeConstraint), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "SizeConstraints"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sizeconstraintset.html#cfn-waf-sizeconstraintset-sizeconstraints"""

    

@attr.s
class XssMatchSet(Resource):
    """
    AWS Object Type = "AWS::WAF::XssMatchSet"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-xssmatchset.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-xssmatchset.html#cfn-waf-xssmatchset-name
    - ``rp_XssMatchTuples``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-xssmatchset.html#cfn-waf-xssmatchset-xssmatchtuples
    """
    AWS_OBJECT_TYPE = "AWS::WAF::XssMatchSet"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-xssmatchset.html#cfn-waf-xssmatchset-name"""
    rp_XssMatchTuples: typing.List[typing.Union['PropXssMatchSetXssMatchTuple', dict]] = attr.ib(
        default=None,
        converter=PropXssMatchSetXssMatchTuple.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropXssMatchSetXssMatchTuple), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "XssMatchTuples"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-xssmatchset.html#cfn-waf-xssmatchset-xssmatchtuples"""

    

@attr.s
class Rule(Resource):
    """
    AWS Object Type = "AWS::WAF::Rule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html

    Property Document:
    
    - ``rp_MetricName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html#cfn-waf-rule-metricname
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html#cfn-waf-rule-name
    - ``p_Predicates``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html#cfn-waf-rule-predicates
    """
    AWS_OBJECT_TYPE = "AWS::WAF::Rule"

    
    rp_MetricName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "MetricName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html#cfn-waf-rule-metricname"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html#cfn-waf-rule-name"""
    p_Predicates: typing.List[typing.Union['PropRulePredicate', dict]] = attr.ib(
        default=None,
        converter=PropRulePredicate.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropRulePredicate), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Predicates"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html#cfn-waf-rule-predicates"""

    

@attr.s
class SqlInjectionMatchSet(Resource):
    """
    AWS Object Type = "AWS::WAF::SqlInjectionMatchSet"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sqlinjectionmatchset.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sqlinjectionmatchset.html#cfn-waf-sqlinjectionmatchset-name
    - ``p_SqlInjectionMatchTuples``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sqlinjectionmatchset.html#cfn-waf-sqlinjectionmatchset-sqlinjectionmatchtuples
    """
    AWS_OBJECT_TYPE = "AWS::WAF::SqlInjectionMatchSet"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sqlinjectionmatchset.html#cfn-waf-sqlinjectionmatchset-name"""
    p_SqlInjectionMatchTuples: typing.List[typing.Union['PropSqlInjectionMatchSetSqlInjectionMatchTuple', dict]] = attr.ib(
        default=None,
        converter=PropSqlInjectionMatchSetSqlInjectionMatchTuple.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropSqlInjectionMatchSetSqlInjectionMatchTuple), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SqlInjectionMatchTuples"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sqlinjectionmatchset.html#cfn-waf-sqlinjectionmatchset-sqlinjectionmatchtuples"""

    

@attr.s
class WebACL(Resource):
    """
    AWS Object Type = "AWS::WAF::WebACL"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html

    Property Document:
    
    - ``rp_DefaultAction``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-defaultaction
    - ``rp_MetricName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-metricname
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-name
    - ``p_Rules``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-rules
    """
    AWS_OBJECT_TYPE = "AWS::WAF::WebACL"

    
    rp_DefaultAction: typing.Union['PropWebACLWafAction', dict] = attr.ib(
        default=None,
        converter=PropWebACLWafAction.from_dict,
        validator=attr.validators.instance_of(PropWebACLWafAction),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultAction"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-defaultaction"""
    rp_MetricName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "MetricName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-metricname"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-name"""
    p_Rules: typing.List[typing.Union['PropWebACLActivatedRule', dict]] = attr.ib(
        default=None,
        converter=PropWebACLActivatedRule.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropWebACLActivatedRule), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Rules"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-rules"""

    

@attr.s
class ByteMatchSet(Resource):
    """
    AWS Object Type = "AWS::WAF::ByteMatchSet"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-bytematchset.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-bytematchset.html#cfn-waf-bytematchset-name
    - ``p_ByteMatchTuples``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-bytematchset.html#cfn-waf-bytematchset-bytematchtuples
    """
    AWS_OBJECT_TYPE = "AWS::WAF::ByteMatchSet"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-bytematchset.html#cfn-waf-bytematchset-name"""
    p_ByteMatchTuples: typing.List[typing.Union['PropByteMatchSetByteMatchTuple', dict]] = attr.ib(
        default=None,
        converter=PropByteMatchSetByteMatchTuple.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropByteMatchSetByteMatchTuple), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ByteMatchTuples"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-bytematchset.html#cfn-waf-bytematchset-bytematchtuples"""

    
