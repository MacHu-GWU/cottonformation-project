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
class PropResourceSetNLBResource(Property):
    """
    AWS Object Type = "AWS::Route53RecoveryReadiness::ResourceSet.NLBResource"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-nlbresource.html

    Property Document:
    
    - ``p_Arn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-nlbresource.html#cfn-route53recoveryreadiness-resourceset-nlbresource-arn
    """
    AWS_OBJECT_TYPE = "AWS::Route53RecoveryReadiness::ResourceSet.NLBResource"
    
    p_Arn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Arn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-nlbresource.html#cfn-route53recoveryreadiness-resourceset-nlbresource-arn"""

@attr.s
class PropResourceSetR53ResourceRecord(Property):
    """
    AWS Object Type = "AWS::Route53RecoveryReadiness::ResourceSet.R53ResourceRecord"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-r53resourcerecord.html

    Property Document:
    
    - ``p_DomainName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-r53resourcerecord.html#cfn-route53recoveryreadiness-resourceset-r53resourcerecord-domainname
    - ``p_RecordSetId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-r53resourcerecord.html#cfn-route53recoveryreadiness-resourceset-r53resourcerecord-recordsetid
    """
    AWS_OBJECT_TYPE = "AWS::Route53RecoveryReadiness::ResourceSet.R53ResourceRecord"
    
    p_DomainName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DomainName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-r53resourcerecord.html#cfn-route53recoveryreadiness-resourceset-r53resourcerecord-domainname"""
    p_RecordSetId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RecordSetId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-r53resourcerecord.html#cfn-route53recoveryreadiness-resourceset-r53resourcerecord-recordsetid"""

@attr.s
class PropResourceSetTargetResource(Property):
    """
    AWS Object Type = "AWS::Route53RecoveryReadiness::ResourceSet.TargetResource"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-targetresource.html

    Property Document:
    
    - ``p_NLBResource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-targetresource.html#cfn-route53recoveryreadiness-resourceset-targetresource-nlbresource
    - ``p_R53Resource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-targetresource.html#cfn-route53recoveryreadiness-resourceset-targetresource-r53resource
    """
    AWS_OBJECT_TYPE = "AWS::Route53RecoveryReadiness::ResourceSet.TargetResource"
    
    p_NLBResource: typing.Union['PropResourceSetNLBResource', dict] = attr.ib(
        default=None,
        converter=PropResourceSetNLBResource.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResourceSetNLBResource)),
        metadata={AttrMeta.PROPERTY_NAME: "NLBResource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-targetresource.html#cfn-route53recoveryreadiness-resourceset-targetresource-nlbresource"""
    p_R53Resource: typing.Union['PropResourceSetR53ResourceRecord', dict] = attr.ib(
        default=None,
        converter=PropResourceSetR53ResourceRecord.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResourceSetR53ResourceRecord)),
        metadata={AttrMeta.PROPERTY_NAME: "R53Resource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-targetresource.html#cfn-route53recoveryreadiness-resourceset-targetresource-r53resource"""

@attr.s
class PropResourceSetDNSTargetResource(Property):
    """
    AWS Object Type = "AWS::Route53RecoveryReadiness::ResourceSet.DNSTargetResource"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.html

    Property Document:
    
    - ``p_DomainName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.html#cfn-route53recoveryreadiness-resourceset-dnstargetresource-domainname
    - ``p_HostedZoneArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.html#cfn-route53recoveryreadiness-resourceset-dnstargetresource-hostedzonearn
    - ``p_RecordSetId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.html#cfn-route53recoveryreadiness-resourceset-dnstargetresource-recordsetid
    - ``p_RecordType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.html#cfn-route53recoveryreadiness-resourceset-dnstargetresource-recordtype
    - ``p_TargetResource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.html#cfn-route53recoveryreadiness-resourceset-dnstargetresource-targetresource
    """
    AWS_OBJECT_TYPE = "AWS::Route53RecoveryReadiness::ResourceSet.DNSTargetResource"
    
    p_DomainName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DomainName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.html#cfn-route53recoveryreadiness-resourceset-dnstargetresource-domainname"""
    p_HostedZoneArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "HostedZoneArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.html#cfn-route53recoveryreadiness-resourceset-dnstargetresource-hostedzonearn"""
    p_RecordSetId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RecordSetId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.html#cfn-route53recoveryreadiness-resourceset-dnstargetresource-recordsetid"""
    p_RecordType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RecordType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.html#cfn-route53recoveryreadiness-resourceset-dnstargetresource-recordtype"""
    p_TargetResource: typing.Union['PropResourceSetTargetResource', dict] = attr.ib(
        default=None,
        converter=PropResourceSetTargetResource.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResourceSetTargetResource)),
        metadata={AttrMeta.PROPERTY_NAME: "TargetResource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.html#cfn-route53recoveryreadiness-resourceset-dnstargetresource-targetresource"""

@attr.s
class PropResourceSetResource(Property):
    """
    AWS Object Type = "AWS::Route53RecoveryReadiness::ResourceSet.Resource"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-resource.html

    Property Document:
    
    - ``p_ComponentId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-resource.html#cfn-route53recoveryreadiness-resourceset-resource-componentid
    - ``p_DnsTargetResource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-resource.html#cfn-route53recoveryreadiness-resourceset-resource-dnstargetresource
    - ``p_ReadinessScopes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-resource.html#cfn-route53recoveryreadiness-resourceset-resource-readinessscopes
    - ``p_ResourceArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-resource.html#cfn-route53recoveryreadiness-resourceset-resource-resourcearn
    """
    AWS_OBJECT_TYPE = "AWS::Route53RecoveryReadiness::ResourceSet.Resource"
    
    p_ComponentId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ComponentId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-resource.html#cfn-route53recoveryreadiness-resourceset-resource-componentid"""
    p_DnsTargetResource: typing.Union['PropResourceSetDNSTargetResource', dict] = attr.ib(
        default=None,
        converter=PropResourceSetDNSTargetResource.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResourceSetDNSTargetResource)),
        metadata={AttrMeta.PROPERTY_NAME: "DnsTargetResource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-resource.html#cfn-route53recoveryreadiness-resourceset-resource-dnstargetresource"""
    p_ReadinessScopes: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ReadinessScopes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-resource.html#cfn-route53recoveryreadiness-resourceset-resource-readinessscopes"""
    p_ResourceArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-resource.html#cfn-route53recoveryreadiness-resourceset-resource-resourcearn"""


#--- Resource declaration ---

@attr.s
class ReadinessCheck(Resource):
    """
    AWS Object Type = "AWS::Route53RecoveryReadiness::ReadinessCheck"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html

    Property Document:
    
    - ``rp_ReadinessCheckName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html#cfn-route53recoveryreadiness-readinesscheck-readinesscheckname
    - ``p_ResourceSetName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html#cfn-route53recoveryreadiness-readinesscheck-resourcesetname
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html#cfn-route53recoveryreadiness-readinesscheck-tags
    """
    AWS_OBJECT_TYPE = "AWS::Route53RecoveryReadiness::ReadinessCheck"

    
    rp_ReadinessCheckName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ReadinessCheckName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html#cfn-route53recoveryreadiness-readinesscheck-readinesscheckname"""
    p_ResourceSetName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceSetName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html#cfn-route53recoveryreadiness-readinesscheck-resourcesetname"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html#cfn-route53recoveryreadiness-readinesscheck-tags"""

    
    @property
    def rv_ReadinessCheckArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html#aws-resource-route53recoveryreadiness-readinesscheck-return-values"""
        return GetAtt(resource=self, attr_name="ReadinessCheckArn")
    

@attr.s
class RecoveryGroup(Resource):
    """
    AWS Object Type = "AWS::Route53RecoveryReadiness::RecoveryGroup"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-recoverygroup.html

    Property Document:
    
    - ``rp_RecoveryGroupName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-recoverygroup.html#cfn-route53recoveryreadiness-recoverygroup-recoverygroupname
    - ``p_Cells``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-recoverygroup.html#cfn-route53recoveryreadiness-recoverygroup-cells
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-recoverygroup.html#cfn-route53recoveryreadiness-recoverygroup-tags
    """
    AWS_OBJECT_TYPE = "AWS::Route53RecoveryReadiness::RecoveryGroup"

    
    rp_RecoveryGroupName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RecoveryGroupName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-recoverygroup.html#cfn-route53recoveryreadiness-recoverygroup-recoverygroupname"""
    p_Cells: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Cells"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-recoverygroup.html#cfn-route53recoveryreadiness-recoverygroup-cells"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-recoverygroup.html#cfn-route53recoveryreadiness-recoverygroup-tags"""

    
    @property
    def rv_RecoveryGroupArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-recoverygroup.html#aws-resource-route53recoveryreadiness-recoverygroup-return-values"""
        return GetAtt(resource=self, attr_name="RecoveryGroupArn")
    

@attr.s
class Cell(Resource):
    """
    AWS Object Type = "AWS::Route53RecoveryReadiness::Cell"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-cell.html

    Property Document:
    
    - ``rp_CellName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-cell.html#cfn-route53recoveryreadiness-cell-cellname
    - ``p_Cells``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-cell.html#cfn-route53recoveryreadiness-cell-cells
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-cell.html#cfn-route53recoveryreadiness-cell-tags
    """
    AWS_OBJECT_TYPE = "AWS::Route53RecoveryReadiness::Cell"

    
    rp_CellName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "CellName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-cell.html#cfn-route53recoveryreadiness-cell-cellname"""
    p_Cells: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Cells"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-cell.html#cfn-route53recoveryreadiness-cell-cells"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-cell.html#cfn-route53recoveryreadiness-cell-tags"""

    
    @property
    def rv_CellArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-cell.html#aws-resource-route53recoveryreadiness-cell-return-values"""
        return GetAtt(resource=self, attr_name="CellArn")
    
    @property
    def rv_ParentReadinessScopes(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-cell.html#aws-resource-route53recoveryreadiness-cell-return-values"""
        return GetAtt(resource=self, attr_name="ParentReadinessScopes")
    

@attr.s
class ResourceSet(Resource):
    """
    AWS Object Type = "AWS::Route53RecoveryReadiness::ResourceSet"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html

    Property Document:
    
    - ``rp_ResourceSetName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html#cfn-route53recoveryreadiness-resourceset-resourcesetname
    - ``rp_ResourceSetType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html#cfn-route53recoveryreadiness-resourceset-resourcesettype
    - ``rp_Resources``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html#cfn-route53recoveryreadiness-resourceset-resources
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html#cfn-route53recoveryreadiness-resourceset-tags
    """
    AWS_OBJECT_TYPE = "AWS::Route53RecoveryReadiness::ResourceSet"

    
    rp_ResourceSetName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceSetName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html#cfn-route53recoveryreadiness-resourceset-resourcesetname"""
    rp_ResourceSetType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceSetType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html#cfn-route53recoveryreadiness-resourceset-resourcesettype"""
    rp_Resources: typing.List[typing.Union['PropResourceSetResource', dict]] = attr.ib(
        default=None,
        converter=PropResourceSetResource.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropResourceSetResource), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Resources"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html#cfn-route53recoveryreadiness-resourceset-resources"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html#cfn-route53recoveryreadiness-resourceset-tags"""

    
    @property
    def rv_ResourceSetArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html#aws-resource-route53recoveryreadiness-resourceset-return-values"""
        return GetAtt(resource=self, attr_name="ResourceSetArn")
    
