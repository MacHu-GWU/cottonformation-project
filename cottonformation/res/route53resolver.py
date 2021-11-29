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
class PropFirewallRuleGroupFirewallRule(Property):
    """
    AWS Object Type = "AWS::Route53Resolver::FirewallRuleGroup.FirewallRule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html

    Property Document:
    
    - ``rp_Action``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-action
    - ``rp_FirewallDomainListId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-firewalldomainlistid
    - ``rp_Priority``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-priority
    - ``p_BlockOverrideDnsType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-blockoverridednstype
    - ``p_BlockOverrideDomain``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-blockoverridedomain
    - ``p_BlockOverrideTtl``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-blockoverridettl
    - ``p_BlockResponse``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-blockresponse
    """
    AWS_OBJECT_TYPE = "AWS::Route53Resolver::FirewallRuleGroup.FirewallRule"
    
    rp_Action: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Action"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-action"""
    rp_FirewallDomainListId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "FirewallDomainListId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-firewalldomainlistid"""
    rp_Priority: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Priority"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-priority"""
    p_BlockOverrideDnsType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BlockOverrideDnsType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-blockoverridednstype"""
    p_BlockOverrideDomain: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BlockOverrideDomain"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-blockoverridedomain"""
    p_BlockOverrideTtl: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "BlockOverrideTtl"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-blockoverridettl"""
    p_BlockResponse: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BlockResponse"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-blockresponse"""

@attr.s
class PropResolverRuleTargetAddress(Property):
    """
    AWS Object Type = "AWS::Route53Resolver::ResolverRule.TargetAddress"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverrule-targetaddress.html

    Property Document:
    
    - ``rp_Ip``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverrule-targetaddress.html#cfn-route53resolver-resolverrule-targetaddress-ip
    - ``p_Port``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverrule-targetaddress.html#cfn-route53resolver-resolverrule-targetaddress-port
    """
    AWS_OBJECT_TYPE = "AWS::Route53Resolver::ResolverRule.TargetAddress"
    
    rp_Ip: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Ip"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverrule-targetaddress.html#cfn-route53resolver-resolverrule-targetaddress-ip"""
    p_Port: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Port"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverrule-targetaddress.html#cfn-route53resolver-resolverrule-targetaddress-port"""

@attr.s
class PropResolverEndpointIpAddressRequest(Property):
    """
    AWS Object Type = "AWS::Route53Resolver::ResolverEndpoint.IpAddressRequest"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverendpoint-ipaddressrequest.html

    Property Document:
    
    - ``rp_SubnetId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverendpoint-ipaddressrequest.html#cfn-route53resolver-resolverendpoint-ipaddressrequest-subnetid
    - ``p_Ip``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverendpoint-ipaddressrequest.html#cfn-route53resolver-resolverendpoint-ipaddressrequest-ip
    """
    AWS_OBJECT_TYPE = "AWS::Route53Resolver::ResolverEndpoint.IpAddressRequest"
    
    rp_SubnetId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SubnetId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverendpoint-ipaddressrequest.html#cfn-route53resolver-resolverendpoint-ipaddressrequest-subnetid"""
    p_Ip: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Ip"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverendpoint-ipaddressrequest.html#cfn-route53resolver-resolverendpoint-ipaddressrequest-ip"""


#--- Resource declaration ---

@attr.s
class ResolverQueryLoggingConfig(Resource):
    """
    AWS Object Type = "AWS::Route53Resolver::ResolverQueryLoggingConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html

    Property Document:
    
    - ``p_DestinationArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html#cfn-route53resolver-resolverqueryloggingconfig-destinationarn
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html#cfn-route53resolver-resolverqueryloggingconfig-name
    """
    AWS_OBJECT_TYPE = "AWS::Route53Resolver::ResolverQueryLoggingConfig"

    
    p_DestinationArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DestinationArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html#cfn-route53resolver-resolverqueryloggingconfig-destinationarn"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html#cfn-route53resolver-resolverqueryloggingconfig-name"""

    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html#aws-resource-route53resolver-resolverqueryloggingconfig-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_OwnerId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html#aws-resource-route53resolver-resolverqueryloggingconfig-return-values"""
        return GetAtt(resource=self, attr_name="OwnerId")
    
    @property
    def rv_Status(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html#aws-resource-route53resolver-resolverqueryloggingconfig-return-values"""
        return GetAtt(resource=self, attr_name="Status")
    
    @property
    def rv_ShareStatus(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html#aws-resource-route53resolver-resolverqueryloggingconfig-return-values"""
        return GetAtt(resource=self, attr_name="ShareStatus")
    
    @property
    def rv_AssociationCount(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html#aws-resource-route53resolver-resolverqueryloggingconfig-return-values"""
        return GetAtt(resource=self, attr_name="AssociationCount")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html#aws-resource-route53resolver-resolverqueryloggingconfig-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_CreatorRequestId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html#aws-resource-route53resolver-resolverqueryloggingconfig-return-values"""
        return GetAtt(resource=self, attr_name="CreatorRequestId")
    
    @property
    def rv_CreationTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html#aws-resource-route53resolver-resolverqueryloggingconfig-return-values"""
        return GetAtt(resource=self, attr_name="CreationTime")
    

@attr.s
class FirewallRuleGroupAssociation(Resource):
    """
    AWS Object Type = "AWS::Route53Resolver::FirewallRuleGroupAssociation"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html

    Property Document:
    
    - ``rp_FirewallRuleGroupId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-firewallrulegroupid
    - ``rp_Priority``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-priority
    - ``rp_VpcId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-vpcid
    - ``p_MutationProtection``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-mutationprotection
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-name
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-tags
    """
    AWS_OBJECT_TYPE = "AWS::Route53Resolver::FirewallRuleGroupAssociation"

    
    rp_FirewallRuleGroupId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "FirewallRuleGroupId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-firewallrulegroupid"""
    rp_Priority: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Priority"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-priority"""
    rp_VpcId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "VpcId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-vpcid"""
    p_MutationProtection: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MutationProtection"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-mutationprotection"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-name"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-tags"""

    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#aws-resource-route53resolver-firewallrulegroupassociation-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#aws-resource-route53resolver-firewallrulegroupassociation-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_ManagedOwnerName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#aws-resource-route53resolver-firewallrulegroupassociation-return-values"""
        return GetAtt(resource=self, attr_name="ManagedOwnerName")
    
    @property
    def rv_Status(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#aws-resource-route53resolver-firewallrulegroupassociation-return-values"""
        return GetAtt(resource=self, attr_name="Status")
    
    @property
    def rv_StatusMessage(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#aws-resource-route53resolver-firewallrulegroupassociation-return-values"""
        return GetAtt(resource=self, attr_name="StatusMessage")
    
    @property
    def rv_CreatorRequestId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#aws-resource-route53resolver-firewallrulegroupassociation-return-values"""
        return GetAtt(resource=self, attr_name="CreatorRequestId")
    
    @property
    def rv_CreationTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#aws-resource-route53resolver-firewallrulegroupassociation-return-values"""
        return GetAtt(resource=self, attr_name="CreationTime")
    
    @property
    def rv_ModificationTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#aws-resource-route53resolver-firewallrulegroupassociation-return-values"""
        return GetAtt(resource=self, attr_name="ModificationTime")
    

@attr.s
class ResolverQueryLoggingConfigAssociation(Resource):
    """
    AWS Object Type = "AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfigassociation.html

    Property Document:
    
    - ``p_ResolverQueryLogConfigId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfigassociation.html#cfn-route53resolver-resolverqueryloggingconfigassociation-resolverquerylogconfigid
    - ``p_ResourceId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfigassociation.html#cfn-route53resolver-resolverqueryloggingconfigassociation-resourceid
    """
    AWS_OBJECT_TYPE = "AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation"

    
    p_ResolverQueryLogConfigId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ResolverQueryLogConfigId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfigassociation.html#cfn-route53resolver-resolverqueryloggingconfigassociation-resolverquerylogconfigid"""
    p_ResourceId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfigassociation.html#cfn-route53resolver-resolverqueryloggingconfigassociation-resourceid"""

    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfigassociation.html#aws-resource-route53resolver-resolverqueryloggingconfigassociation-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_Status(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfigassociation.html#aws-resource-route53resolver-resolverqueryloggingconfigassociation-return-values"""
        return GetAtt(resource=self, attr_name="Status")
    
    @property
    def rv_Error(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfigassociation.html#aws-resource-route53resolver-resolverqueryloggingconfigassociation-return-values"""
        return GetAtt(resource=self, attr_name="Error")
    
    @property
    def rv_ErrorMessage(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfigassociation.html#aws-resource-route53resolver-resolverqueryloggingconfigassociation-return-values"""
        return GetAtt(resource=self, attr_name="ErrorMessage")
    
    @property
    def rv_CreationTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfigassociation.html#aws-resource-route53resolver-resolverqueryloggingconfigassociation-return-values"""
        return GetAtt(resource=self, attr_name="CreationTime")
    

@attr.s
class ResolverConfig(Resource):
    """
    AWS Object Type = "AWS::Route53Resolver::ResolverConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverconfig.html

    Property Document:
    
    - ``rp_AutodefinedReverseFlag``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverconfig.html#cfn-route53resolver-resolverconfig-autodefinedreverseflag
    - ``rp_ResourceId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverconfig.html#cfn-route53resolver-resolverconfig-resourceid
    """
    AWS_OBJECT_TYPE = "AWS::Route53Resolver::ResolverConfig"

    
    rp_AutodefinedReverseFlag: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AutodefinedReverseFlag"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverconfig.html#cfn-route53resolver-resolverconfig-autodefinedreverseflag"""
    rp_ResourceId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverconfig.html#cfn-route53resolver-resolverconfig-resourceid"""

    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverconfig.html#aws-resource-route53resolver-resolverconfig-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_OwnerId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverconfig.html#aws-resource-route53resolver-resolverconfig-return-values"""
        return GetAtt(resource=self, attr_name="OwnerId")
    
    @property
    def rv_AutodefinedReverse(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverconfig.html#aws-resource-route53resolver-resolverconfig-return-values"""
        return GetAtt(resource=self, attr_name="AutodefinedReverse")
    

@attr.s
class ResolverDNSSECConfig(Resource):
    """
    AWS Object Type = "AWS::Route53Resolver::ResolverDNSSECConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverdnssecconfig.html

    Property Document:
    
    - ``p_ResourceId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverdnssecconfig.html#cfn-route53resolver-resolverdnssecconfig-resourceid
    """
    AWS_OBJECT_TYPE = "AWS::Route53Resolver::ResolverDNSSECConfig"

    
    p_ResourceId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverdnssecconfig.html#cfn-route53resolver-resolverdnssecconfig-resourceid"""

    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverdnssecconfig.html#aws-resource-route53resolver-resolverdnssecconfig-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_OwnerId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverdnssecconfig.html#aws-resource-route53resolver-resolverdnssecconfig-return-values"""
        return GetAtt(resource=self, attr_name="OwnerId")
    
    @property
    def rv_ValidationStatus(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverdnssecconfig.html#aws-resource-route53resolver-resolverdnssecconfig-return-values"""
        return GetAtt(resource=self, attr_name="ValidationStatus")
    

@attr.s
class FirewallDomainList(Resource):
    """
    AWS Object Type = "AWS::Route53Resolver::FirewallDomainList"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html

    Property Document:
    
    - ``p_DomainFileUrl``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#cfn-route53resolver-firewalldomainlist-domainfileurl
    - ``p_Domains``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#cfn-route53resolver-firewalldomainlist-domains
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#cfn-route53resolver-firewalldomainlist-name
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#cfn-route53resolver-firewalldomainlist-tags
    """
    AWS_OBJECT_TYPE = "AWS::Route53Resolver::FirewallDomainList"

    
    p_DomainFileUrl: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DomainFileUrl"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#cfn-route53resolver-firewalldomainlist-domainfileurl"""
    p_Domains: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Domains"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#cfn-route53resolver-firewalldomainlist-domains"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#cfn-route53resolver-firewalldomainlist-name"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#cfn-route53resolver-firewalldomainlist-tags"""

    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#aws-resource-route53resolver-firewalldomainlist-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#aws-resource-route53resolver-firewalldomainlist-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_DomainCount(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#aws-resource-route53resolver-firewalldomainlist-return-values"""
        return GetAtt(resource=self, attr_name="DomainCount")
    
    @property
    def rv_Status(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#aws-resource-route53resolver-firewalldomainlist-return-values"""
        return GetAtt(resource=self, attr_name="Status")
    
    @property
    def rv_StatusMessage(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#aws-resource-route53resolver-firewalldomainlist-return-values"""
        return GetAtt(resource=self, attr_name="StatusMessage")
    
    @property
    def rv_ManagedOwnerName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#aws-resource-route53resolver-firewalldomainlist-return-values"""
        return GetAtt(resource=self, attr_name="ManagedOwnerName")
    
    @property
    def rv_CreatorRequestId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#aws-resource-route53resolver-firewalldomainlist-return-values"""
        return GetAtt(resource=self, attr_name="CreatorRequestId")
    
    @property
    def rv_CreationTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#aws-resource-route53resolver-firewalldomainlist-return-values"""
        return GetAtt(resource=self, attr_name="CreationTime")
    
    @property
    def rv_ModificationTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#aws-resource-route53resolver-firewalldomainlist-return-values"""
        return GetAtt(resource=self, attr_name="ModificationTime")
    

@attr.s
class ResolverRule(Resource):
    """
    AWS Object Type = "AWS::Route53Resolver::ResolverRule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html

    Property Document:
    
    - ``rp_DomainName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-domainname
    - ``rp_RuleType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-ruletype
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-name
    - ``p_ResolverEndpointId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-resolverendpointid
    - ``p_TargetIps``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-targetips
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-tags
    """
    AWS_OBJECT_TYPE = "AWS::Route53Resolver::ResolverRule"

    
    rp_DomainName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DomainName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-domainname"""
    rp_RuleType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RuleType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-ruletype"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-name"""
    p_ResolverEndpointId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ResolverEndpointId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-resolverendpointid"""
    p_TargetIps: typing.List[typing.Union['PropResolverRuleTargetAddress', dict]] = attr.ib(
        default=None,
        converter=PropResolverRuleTargetAddress.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropResolverRuleTargetAddress), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "TargetIps"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-targetips"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-tags"""

    
    @property
    def rv_ResolverEndpointId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#aws-resource-route53resolver-resolverrule-return-values"""
        return GetAtt(resource=self, attr_name="ResolverEndpointId")
    
    @property
    def rv_DomainName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#aws-resource-route53resolver-resolverrule-return-values"""
        return GetAtt(resource=self, attr_name="DomainName")
    
    @property
    def rv_Name(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#aws-resource-route53resolver-resolverrule-return-values"""
        return GetAtt(resource=self, attr_name="Name")
    
    @property
    def rv_TargetIps(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#aws-resource-route53resolver-resolverrule-return-values"""
        return GetAtt(resource=self, attr_name="TargetIps")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#aws-resource-route53resolver-resolverrule-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_ResolverRuleId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#aws-resource-route53resolver-resolverrule-return-values"""
        return GetAtt(resource=self, attr_name="ResolverRuleId")
    

@attr.s
class FirewallRuleGroup(Resource):
    """
    AWS Object Type = "AWS::Route53Resolver::FirewallRuleGroup"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html

    Property Document:
    
    - ``p_FirewallRules``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html#cfn-route53resolver-firewallrulegroup-firewallrules
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html#cfn-route53resolver-firewallrulegroup-name
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html#cfn-route53resolver-firewallrulegroup-tags
    """
    AWS_OBJECT_TYPE = "AWS::Route53Resolver::FirewallRuleGroup"

    
    p_FirewallRules: typing.List[typing.Union['PropFirewallRuleGroupFirewallRule', dict]] = attr.ib(
        default=None,
        converter=PropFirewallRuleGroupFirewallRule.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropFirewallRuleGroupFirewallRule), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "FirewallRules"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html#cfn-route53resolver-firewallrulegroup-firewallrules"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html#cfn-route53resolver-firewallrulegroup-name"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html#cfn-route53resolver-firewallrulegroup-tags"""

    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html#aws-resource-route53resolver-firewallrulegroup-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html#aws-resource-route53resolver-firewallrulegroup-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_RuleCount(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html#aws-resource-route53resolver-firewallrulegroup-return-values"""
        return GetAtt(resource=self, attr_name="RuleCount")
    
    @property
    def rv_Status(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html#aws-resource-route53resolver-firewallrulegroup-return-values"""
        return GetAtt(resource=self, attr_name="Status")
    
    @property
    def rv_StatusMessage(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html#aws-resource-route53resolver-firewallrulegroup-return-values"""
        return GetAtt(resource=self, attr_name="StatusMessage")
    
    @property
    def rv_OwnerId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html#aws-resource-route53resolver-firewallrulegroup-return-values"""
        return GetAtt(resource=self, attr_name="OwnerId")
    
    @property
    def rv_ShareStatus(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html#aws-resource-route53resolver-firewallrulegroup-return-values"""
        return GetAtt(resource=self, attr_name="ShareStatus")
    
    @property
    def rv_CreatorRequestId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html#aws-resource-route53resolver-firewallrulegroup-return-values"""
        return GetAtt(resource=self, attr_name="CreatorRequestId")
    
    @property
    def rv_CreationTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html#aws-resource-route53resolver-firewallrulegroup-return-values"""
        return GetAtt(resource=self, attr_name="CreationTime")
    
    @property
    def rv_ModificationTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html#aws-resource-route53resolver-firewallrulegroup-return-values"""
        return GetAtt(resource=self, attr_name="ModificationTime")
    

@attr.s
class ResolverRuleAssociation(Resource):
    """
    AWS Object Type = "AWS::Route53Resolver::ResolverRuleAssociation"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html

    Property Document:
    
    - ``rp_ResolverRuleId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html#cfn-route53resolver-resolverruleassociation-resolverruleid
    - ``rp_VPCId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html#cfn-route53resolver-resolverruleassociation-vpcid
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html#cfn-route53resolver-resolverruleassociation-name
    """
    AWS_OBJECT_TYPE = "AWS::Route53Resolver::ResolverRuleAssociation"

    
    rp_ResolverRuleId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResolverRuleId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html#cfn-route53resolver-resolverruleassociation-resolverruleid"""
    rp_VPCId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "VPCId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html#cfn-route53resolver-resolverruleassociation-vpcid"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html#cfn-route53resolver-resolverruleassociation-name"""

    
    @property
    def rv_VPCId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html#aws-resource-route53resolver-resolverruleassociation-return-values"""
        return GetAtt(resource=self, attr_name="VPCId")
    
    @property
    def rv_ResolverRuleId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html#aws-resource-route53resolver-resolverruleassociation-return-values"""
        return GetAtt(resource=self, attr_name="ResolverRuleId")
    
    @property
    def rv_ResolverRuleAssociationId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html#aws-resource-route53resolver-resolverruleassociation-return-values"""
        return GetAtt(resource=self, attr_name="ResolverRuleAssociationId")
    
    @property
    def rv_Name(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html#aws-resource-route53resolver-resolverruleassociation-return-values"""
        return GetAtt(resource=self, attr_name="Name")
    

@attr.s
class ResolverEndpoint(Resource):
    """
    AWS Object Type = "AWS::Route53Resolver::ResolverEndpoint"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html

    Property Document:
    
    - ``rp_Direction``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-direction
    - ``rp_IpAddresses``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-ipaddresses
    - ``rp_SecurityGroupIds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-securitygroupids
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-name
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-tags
    """
    AWS_OBJECT_TYPE = "AWS::Route53Resolver::ResolverEndpoint"

    
    rp_Direction: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Direction"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-direction"""
    rp_IpAddresses: typing.List[typing.Union['PropResolverEndpointIpAddressRequest', dict]] = attr.ib(
        default=None,
        converter=PropResolverEndpointIpAddressRequest.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropResolverEndpointIpAddressRequest), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "IpAddresses"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-ipaddresses"""
    rp_SecurityGroupIds: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "SecurityGroupIds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-securitygroupids"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-name"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-tags"""

    
    @property
    def rv_ResolverEndpointId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#aws-resource-route53resolver-resolverendpoint-return-values"""
        return GetAtt(resource=self, attr_name="ResolverEndpointId")
    
    @property
    def rv_IpAddressCount(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#aws-resource-route53resolver-resolverendpoint-return-values"""
        return GetAtt(resource=self, attr_name="IpAddressCount")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#aws-resource-route53resolver-resolverendpoint-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_Direction(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#aws-resource-route53resolver-resolverendpoint-return-values"""
        return GetAtt(resource=self, attr_name="Direction")
    
    @property
    def rv_HostVPCId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#aws-resource-route53resolver-resolverendpoint-return-values"""
        return GetAtt(resource=self, attr_name="HostVPCId")
    
    @property
    def rv_Name(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#aws-resource-route53resolver-resolverendpoint-return-values"""
        return GetAtt(resource=self, attr_name="Name")
    
