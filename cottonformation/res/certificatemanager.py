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
class PropAccountExpiryEventsConfiguration(Property):
    """
    AWS Object Type = "AWS::CertificateManager::Account.ExpiryEventsConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-certificatemanager-account-expiryeventsconfiguration.html

    Property Document:
    
    - ``p_DaysBeforeExpiry``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-certificatemanager-account-expiryeventsconfiguration.html#cfn-certificatemanager-account-expiryeventsconfiguration-daysbeforeexpiry
    """
    AWS_OBJECT_TYPE = "AWS::CertificateManager::Account.ExpiryEventsConfiguration"
    
    p_DaysBeforeExpiry: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "DaysBeforeExpiry"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-certificatemanager-account-expiryeventsconfiguration.html#cfn-certificatemanager-account-expiryeventsconfiguration-daysbeforeexpiry"""

@attr.s
class PropCertificateDomainValidationOption(Property):
    """
    AWS Object Type = "AWS::CertificateManager::Certificate.DomainValidationOption"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-certificatemanager-certificate-domainvalidationoption.html

    Property Document:
    
    - ``rp_DomainName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-certificatemanager-certificate-domainvalidationoption.html#cfn-certificatemanager-certificate-domainvalidationoptions-domainname
    - ``p_HostedZoneId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-certificatemanager-certificate-domainvalidationoption.html#cfn-certificatemanager-certificate-domainvalidationoption-hostedzoneid
    - ``p_ValidationDomain``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-certificatemanager-certificate-domainvalidationoption.html#cfn-certificatemanager-certificate-domainvalidationoption-validationdomain
    """
    AWS_OBJECT_TYPE = "AWS::CertificateManager::Certificate.DomainValidationOption"
    
    rp_DomainName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DomainName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-certificatemanager-certificate-domainvalidationoption.html#cfn-certificatemanager-certificate-domainvalidationoptions-domainname"""
    p_HostedZoneId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "HostedZoneId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-certificatemanager-certificate-domainvalidationoption.html#cfn-certificatemanager-certificate-domainvalidationoption-hostedzoneid"""
    p_ValidationDomain: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ValidationDomain"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-certificatemanager-certificate-domainvalidationoption.html#cfn-certificatemanager-certificate-domainvalidationoption-validationdomain"""


#--- Resource declaration ---

@attr.s
class Account(Resource):
    """
    AWS Object Type = "AWS::CertificateManager::Account"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-account.html

    Property Document:
    
    - ``rp_ExpiryEventsConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-account.html#cfn-certificatemanager-account-expiryeventsconfiguration
    """
    AWS_OBJECT_TYPE = "AWS::CertificateManager::Account"

    
    rp_ExpiryEventsConfiguration: typing.Union['PropAccountExpiryEventsConfiguration', dict] = attr.ib(
        default=None,
        converter=PropAccountExpiryEventsConfiguration.from_dict,
        validator=attr.validators.instance_of(PropAccountExpiryEventsConfiguration),
        metadata={AttrMeta.PROPERTY_NAME: "ExpiryEventsConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-account.html#cfn-certificatemanager-account-expiryeventsconfiguration"""

    
    @property
    def rv_AccountId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-account.html#aws-resource-certificatemanager-account-return-values"""
        return GetAtt(resource=self, attr_name="AccountId")
    

@attr.s
class Certificate(Resource):
    """
    AWS Object Type = "AWS::CertificateManager::Certificate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html

    Property Document:
    
    - ``rp_DomainName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-domainname
    - ``p_CertificateAuthorityArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-certificateauthorityarn
    - ``p_CertificateTransparencyLoggingPreference``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-certificatetransparencyloggingpreference
    - ``p_DomainValidationOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-domainvalidationoptions
    - ``p_SubjectAlternativeNames``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-subjectalternativenames
    - ``p_ValidationMethod``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-validationmethod
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-tags
    """
    AWS_OBJECT_TYPE = "AWS::CertificateManager::Certificate"

    
    rp_DomainName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DomainName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-domainname"""
    p_CertificateAuthorityArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CertificateAuthorityArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-certificateauthorityarn"""
    p_CertificateTransparencyLoggingPreference: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CertificateTransparencyLoggingPreference"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-certificatetransparencyloggingpreference"""
    p_DomainValidationOptions: typing.List[typing.Union['PropCertificateDomainValidationOption', dict]] = attr.ib(
        default=None,
        converter=PropCertificateDomainValidationOption.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropCertificateDomainValidationOption), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "DomainValidationOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-domainvalidationoptions"""
    p_SubjectAlternativeNames: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SubjectAlternativeNames"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-subjectalternativenames"""
    p_ValidationMethod: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ValidationMethod"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-validationmethod"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-tags"""

    
