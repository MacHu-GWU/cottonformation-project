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
class PropFindingsFilterFindingsFilterListItem(Property):
    """
    AWS Object Type = "AWS::Macie::FindingsFilter.FindingsFilterListItem"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingsfilterlistitem.html

    Property Document:
    
    - ``p_Id``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingsfilterlistitem.html#cfn-macie-findingsfilter-findingsfilterlistitem-id
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingsfilterlistitem.html#cfn-macie-findingsfilter-findingsfilterlistitem-name
    """
    AWS_OBJECT_TYPE = "AWS::Macie::FindingsFilter.FindingsFilterListItem"
    
    p_Id: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Id"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingsfilterlistitem.html#cfn-macie-findingsfilter-findingsfilterlistitem-id"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingsfilterlistitem.html#cfn-macie-findingsfilter-findingsfilterlistitem-name"""

@attr.s
class PropFindingsFilterCriterion(Property):
    """
    AWS Object Type = "AWS::Macie::FindingsFilter.Criterion"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-criterion.html

    Property Document:
    
    """
    AWS_OBJECT_TYPE = "AWS::Macie::FindingsFilter.Criterion"
    

@attr.s
class PropFindingsFilterFindingCriteria(Property):
    """
    AWS Object Type = "AWS::Macie::FindingsFilter.FindingCriteria"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingcriteria.html

    Property Document:
    
    - ``p_Criterion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingcriteria.html#cfn-macie-findingsfilter-findingcriteria-criterion
    """
    AWS_OBJECT_TYPE = "AWS::Macie::FindingsFilter.FindingCriteria"
    
    p_Criterion: typing.Union['PropFindingsFilterCriterion', dict] = attr.ib(
        default=None,
        converter=PropFindingsFilterCriterion.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropFindingsFilterCriterion)),
        metadata={AttrMeta.PROPERTY_NAME: "Criterion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingcriteria.html#cfn-macie-findingsfilter-findingcriteria-criterion"""


#--- Resource declaration ---

@attr.s
class Session(Resource):
    """
    AWS Object Type = "AWS::Macie::Session"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html

    Property Document:
    
    - ``p_FindingPublishingFrequency``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html#cfn-macie-session-findingpublishingfrequency
    - ``p_Status``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html#cfn-macie-session-status
    """
    AWS_OBJECT_TYPE = "AWS::Macie::Session"

    
    p_FindingPublishingFrequency: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "FindingPublishingFrequency"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html#cfn-macie-session-findingpublishingfrequency"""
    p_Status: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Status"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html#cfn-macie-session-status"""

    
    @property
    def rv_AwsAccountId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html#aws-resource-macie-session-return-values"""
        return GetAtt(resource=self, attr_name="AwsAccountId")
    
    @property
    def rv_ServiceRole(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html#aws-resource-macie-session-return-values"""
        return GetAtt(resource=self, attr_name="ServiceRole")
    

@attr.s
class FindingsFilter(Resource):
    """
    AWS Object Type = "AWS::Macie::FindingsFilter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html

    Property Document:
    
    - ``rp_FindingCriteria``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-findingcriteria
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-name
    - ``p_Action``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-action
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-description
    - ``p_Position``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-position
    """
    AWS_OBJECT_TYPE = "AWS::Macie::FindingsFilter"

    
    rp_FindingCriteria: typing.Union['PropFindingsFilterFindingCriteria', dict] = attr.ib(
        default=None,
        converter=PropFindingsFilterFindingCriteria.from_dict,
        validator=attr.validators.instance_of(PropFindingsFilterFindingCriteria),
        metadata={AttrMeta.PROPERTY_NAME: "FindingCriteria"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-findingcriteria"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-name"""
    p_Action: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Action"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-action"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-description"""
    p_Position: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Position"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-position"""

    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#aws-resource-macie-findingsfilter-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#aws-resource-macie-findingsfilter-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_FindingsFilterListItems(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#aws-resource-macie-findingsfilter-return-values"""
        return GetAtt(resource=self, attr_name="FindingsFilterListItems")
    

@attr.s
class CustomDataIdentifier(Resource):
    """
    AWS Object Type = "AWS::Macie::CustomDataIdentifier"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-name
    - ``rp_Regex``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-regex
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-description
    - ``p_IgnoreWords``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-ignorewords
    - ``p_Keywords``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-keywords
    - ``p_MaximumMatchDistance``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-maximummatchdistance
    """
    AWS_OBJECT_TYPE = "AWS::Macie::CustomDataIdentifier"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-name"""
    rp_Regex: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Regex"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-regex"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-description"""
    p_IgnoreWords: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "IgnoreWords"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-ignorewords"""
    p_Keywords: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Keywords"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-keywords"""
    p_MaximumMatchDistance: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MaximumMatchDistance"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-maximummatchdistance"""

    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#aws-resource-macie-customdataidentifier-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#aws-resource-macie-customdataidentifier-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
