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
class PropDistributionCookies(Property):
    """
    AWS Object Type = "AWS::CloudFront::Distribution.Cookies"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cookies.html

    Property Document:
    
    - ``rp_Forward``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cookies.html#cfn-cloudfront-distribution-cookies-forward
    - ``p_WhitelistedNames``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cookies.html#cfn-cloudfront-distribution-cookies-whitelistednames
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::Distribution.Cookies"
    
    rp_Forward: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Forward"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cookies.html#cfn-cloudfront-distribution-cookies-forward"""
    p_WhitelistedNames: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "WhitelistedNames"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cookies.html#cfn-cloudfront-distribution-cookies-whitelistednames"""

@attr.s
class PropCachePolicyHeadersConfig(Property):
    """
    AWS Object Type = "AWS::CloudFront::CachePolicy.HeadersConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-headersconfig.html

    Property Document:
    
    - ``rp_HeaderBehavior``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-headersconfig.html#cfn-cloudfront-cachepolicy-headersconfig-headerbehavior
    - ``p_Headers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-headersconfig.html#cfn-cloudfront-cachepolicy-headersconfig-headers
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::CachePolicy.HeadersConfig"
    
    rp_HeaderBehavior: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "HeaderBehavior"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-headersconfig.html#cfn-cloudfront-cachepolicy-headersconfig-headerbehavior"""
    p_Headers: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Headers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-headersconfig.html#cfn-cloudfront-cachepolicy-headersconfig-headers"""

@attr.s
class PropKeyGroupKeyGroupConfig(Property):
    """
    AWS Object Type = "AWS::CloudFront::KeyGroup.KeyGroupConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-keygroup-keygroupconfig.html

    Property Document:
    
    - ``rp_Items``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-keygroup-keygroupconfig.html#cfn-cloudfront-keygroup-keygroupconfig-items
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-keygroup-keygroupconfig.html#cfn-cloudfront-keygroup-keygroupconfig-name
    - ``p_Comment``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-keygroup-keygroupconfig.html#cfn-cloudfront-keygroup-keygroupconfig-comment
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::KeyGroup.KeyGroupConfig"
    
    rp_Items: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Items"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-keygroup-keygroupconfig.html#cfn-cloudfront-keygroup-keygroupconfig-items"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-keygroup-keygroupconfig.html#cfn-cloudfront-keygroup-keygroupconfig-name"""
    p_Comment: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Comment"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-keygroup-keygroupconfig.html#cfn-cloudfront-keygroup-keygroupconfig-comment"""

@attr.s
class PropResponseHeadersPolicyXSSProtection(Property):
    """
    AWS Object Type = "AWS::CloudFront::ResponseHeadersPolicy.XSSProtection"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-xssprotection.html

    Property Document:
    
    - ``rp_Override``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-xssprotection.html#cfn-cloudfront-responseheaderspolicy-xssprotection-override
    - ``rp_Protection``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-xssprotection.html#cfn-cloudfront-responseheaderspolicy-xssprotection-protection
    - ``p_ModeBlock``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-xssprotection.html#cfn-cloudfront-responseheaderspolicy-xssprotection-modeblock
    - ``p_ReportUri``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-xssprotection.html#cfn-cloudfront-responseheaderspolicy-xssprotection-reporturi
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::ResponseHeadersPolicy.XSSProtection"
    
    rp_Override: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Override"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-xssprotection.html#cfn-cloudfront-responseheaderspolicy-xssprotection-override"""
    rp_Protection: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Protection"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-xssprotection.html#cfn-cloudfront-responseheaderspolicy-xssprotection-protection"""
    p_ModeBlock: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "ModeBlock"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-xssprotection.html#cfn-cloudfront-responseheaderspolicy-xssprotection-modeblock"""
    p_ReportUri: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ReportUri"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-xssprotection.html#cfn-cloudfront-responseheaderspolicy-xssprotection-reporturi"""

@attr.s
class PropStreamingDistributionS3Origin(Property):
    """
    AWS Object Type = "AWS::CloudFront::StreamingDistribution.S3Origin"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-s3origin.html

    Property Document:
    
    - ``rp_DomainName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-s3origin.html#cfn-cloudfront-streamingdistribution-s3origin-domainname
    - ``rp_OriginAccessIdentity``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-s3origin.html#cfn-cloudfront-streamingdistribution-s3origin-originaccessidentity
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::StreamingDistribution.S3Origin"
    
    rp_DomainName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DomainName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-s3origin.html#cfn-cloudfront-streamingdistribution-s3origin-domainname"""
    rp_OriginAccessIdentity: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "OriginAccessIdentity"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-s3origin.html#cfn-cloudfront-streamingdistribution-s3origin-originaccessidentity"""

@attr.s
class PropDistributionLegacyS3Origin(Property):
    """
    AWS Object Type = "AWS::CloudFront::Distribution.LegacyS3Origin"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacys3origin.html

    Property Document:
    
    - ``rp_DNSName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacys3origin.html#cfn-cloudfront-distribution-legacys3origin-dnsname
    - ``p_OriginAccessIdentity``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacys3origin.html#cfn-cloudfront-distribution-legacys3origin-originaccessidentity
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::Distribution.LegacyS3Origin"
    
    rp_DNSName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DNSName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacys3origin.html#cfn-cloudfront-distribution-legacys3origin-dnsname"""
    p_OriginAccessIdentity: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "OriginAccessIdentity"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacys3origin.html#cfn-cloudfront-distribution-legacys3origin-originaccessidentity"""

@attr.s
class PropDistributionOriginCustomHeader(Property):
    """
    AWS Object Type = "AWS::CloudFront::Distribution.OriginCustomHeader"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origincustomheader.html

    Property Document:
    
    - ``rp_HeaderName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origincustomheader.html#cfn-cloudfront-distribution-origincustomheader-headername
    - ``rp_HeaderValue``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origincustomheader.html#cfn-cloudfront-distribution-origincustomheader-headervalue
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::Distribution.OriginCustomHeader"
    
    rp_HeaderName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "HeaderName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origincustomheader.html#cfn-cloudfront-distribution-origincustomheader-headername"""
    rp_HeaderValue: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "HeaderValue"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origincustomheader.html#cfn-cloudfront-distribution-origincustomheader-headervalue"""

@attr.s
class PropDistributionCustomOriginConfig(Property):
    """
    AWS Object Type = "AWS::CloudFront::Distribution.CustomOriginConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html

    Property Document:
    
    - ``rp_OriginProtocolPolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html#cfn-cloudfront-distribution-customoriginconfig-originprotocolpolicy
    - ``p_HTTPPort``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html#cfn-cloudfront-distribution-customoriginconfig-httpport
    - ``p_HTTPSPort``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html#cfn-cloudfront-distribution-customoriginconfig-httpsport
    - ``p_OriginKeepaliveTimeout``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html#cfn-cloudfront-distribution-customoriginconfig-originkeepalivetimeout
    - ``p_OriginReadTimeout``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html#cfn-cloudfront-distribution-customoriginconfig-originreadtimeout
    - ``p_OriginSSLProtocols``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html#cfn-cloudfront-distribution-customoriginconfig-originsslprotocols
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::Distribution.CustomOriginConfig"
    
    rp_OriginProtocolPolicy: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "OriginProtocolPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html#cfn-cloudfront-distribution-customoriginconfig-originprotocolpolicy"""
    p_HTTPPort: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "HTTPPort"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html#cfn-cloudfront-distribution-customoriginconfig-httpport"""
    p_HTTPSPort: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "HTTPSPort"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html#cfn-cloudfront-distribution-customoriginconfig-httpsport"""
    p_OriginKeepaliveTimeout: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "OriginKeepaliveTimeout"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html#cfn-cloudfront-distribution-customoriginconfig-originkeepalivetimeout"""
    p_OriginReadTimeout: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "OriginReadTimeout"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html#cfn-cloudfront-distribution-customoriginconfig-originreadtimeout"""
    p_OriginSSLProtocols: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "OriginSSLProtocols"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html#cfn-cloudfront-distribution-customoriginconfig-originsslprotocols"""

@attr.s
class PropCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfig(Property):
    """
    AWS Object Type = "AWS::CloudFront::CloudFrontOriginAccessIdentity.CloudFrontOriginAccessIdentityConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cloudfrontoriginaccessidentity-cloudfrontoriginaccessidentityconfig.html

    Property Document:
    
    - ``rp_Comment``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cloudfrontoriginaccessidentity-cloudfrontoriginaccessidentityconfig.html#cfn-cloudfront-cloudfrontoriginaccessidentity-cloudfrontoriginaccessidentityconfig-comment
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::CloudFrontOriginAccessIdentity.CloudFrontOriginAccessIdentityConfig"
    
    rp_Comment: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Comment"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cloudfrontoriginaccessidentity-cloudfrontoriginaccessidentityconfig.html#cfn-cloudfront-cloudfrontoriginaccessidentity-cloudfrontoriginaccessidentityconfig-comment"""

@attr.s
class PropResponseHeadersPolicyAccessControlExposeHeaders(Property):
    """
    AWS Object Type = "AWS::CloudFront::ResponseHeadersPolicy.AccessControlExposeHeaders"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolexposeheaders.html

    Property Document:
    
    - ``rp_Items``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolexposeheaders.html#cfn-cloudfront-responseheaderspolicy-accesscontrolexposeheaders-items
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::ResponseHeadersPolicy.AccessControlExposeHeaders"
    
    rp_Items: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Items"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolexposeheaders.html#cfn-cloudfront-responseheaderspolicy-accesscontrolexposeheaders-items"""

@attr.s
class PropDistributionGeoRestriction(Property):
    """
    AWS Object Type = "AWS::CloudFront::Distribution.GeoRestriction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-georestriction.html

    Property Document:
    
    - ``rp_RestrictionType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-georestriction.html#cfn-cloudfront-distribution-georestriction-restrictiontype
    - ``p_Locations``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-georestriction.html#cfn-cloudfront-distribution-georestriction-locations
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::Distribution.GeoRestriction"
    
    rp_RestrictionType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RestrictionType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-georestriction.html#cfn-cloudfront-distribution-georestriction-restrictiontype"""
    p_Locations: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Locations"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-georestriction.html#cfn-cloudfront-distribution-georestriction-locations"""

@attr.s
class PropDistributionViewerCertificate(Property):
    """
    AWS Object Type = "AWS::CloudFront::Distribution.ViewerCertificate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html

    Property Document:
    
    - ``p_AcmCertificateArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html#cfn-cloudfront-distribution-viewercertificate-acmcertificatearn
    - ``p_CloudFrontDefaultCertificate``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html#cfn-cloudfront-distribution-viewercertificate-cloudfrontdefaultcertificate
    - ``p_IamCertificateId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html#cfn-cloudfront-distribution-viewercertificate-iamcertificateid
    - ``p_MinimumProtocolVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html#cfn-cloudfront-distribution-viewercertificate-minimumprotocolversion
    - ``p_SslSupportMethod``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html#cfn-cloudfront-distribution-viewercertificate-sslsupportmethod
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::Distribution.ViewerCertificate"
    
    p_AcmCertificateArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AcmCertificateArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html#cfn-cloudfront-distribution-viewercertificate-acmcertificatearn"""
    p_CloudFrontDefaultCertificate: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "CloudFrontDefaultCertificate"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html#cfn-cloudfront-distribution-viewercertificate-cloudfrontdefaultcertificate"""
    p_IamCertificateId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "IamCertificateId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html#cfn-cloudfront-distribution-viewercertificate-iamcertificateid"""
    p_MinimumProtocolVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MinimumProtocolVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html#cfn-cloudfront-distribution-viewercertificate-minimumprotocolversion"""
    p_SslSupportMethod: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SslSupportMethod"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html#cfn-cloudfront-distribution-viewercertificate-sslsupportmethod"""

@attr.s
class PropDistributionCustomErrorResponse(Property):
    """
    AWS Object Type = "AWS::CloudFront::Distribution.CustomErrorResponse"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customerrorresponse.html

    Property Document:
    
    - ``rp_ErrorCode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customerrorresponse.html#cfn-cloudfront-distribution-customerrorresponse-errorcode
    - ``p_ErrorCachingMinTTL``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customerrorresponse.html#cfn-cloudfront-distribution-customerrorresponse-errorcachingminttl
    - ``p_ResponseCode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customerrorresponse.html#cfn-cloudfront-distribution-customerrorresponse-responsecode
    - ``p_ResponsePagePath``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customerrorresponse.html#cfn-cloudfront-distribution-customerrorresponse-responsepagepath
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::Distribution.CustomErrorResponse"
    
    rp_ErrorCode: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "ErrorCode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customerrorresponse.html#cfn-cloudfront-distribution-customerrorresponse-errorcode"""
    p_ErrorCachingMinTTL: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "ErrorCachingMinTTL"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customerrorresponse.html#cfn-cloudfront-distribution-customerrorresponse-errorcachingminttl"""
    p_ResponseCode: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ResponseCode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customerrorresponse.html#cfn-cloudfront-distribution-customerrorresponse-responsecode"""
    p_ResponsePagePath: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ResponsePagePath"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customerrorresponse.html#cfn-cloudfront-distribution-customerrorresponse-responsepagepath"""

@attr.s
class PropResponseHeadersPolicyAccessControlAllowMethods(Property):
    """
    AWS Object Type = "AWS::CloudFront::ResponseHeadersPolicy.AccessControlAllowMethods"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolallowmethods.html

    Property Document:
    
    - ``rp_Items``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolallowmethods.html#cfn-cloudfront-responseheaderspolicy-accesscontrolallowmethods-items
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::ResponseHeadersPolicy.AccessControlAllowMethods"
    
    rp_Items: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Items"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolallowmethods.html#cfn-cloudfront-responseheaderspolicy-accesscontrolallowmethods-items"""

@attr.s
class PropStreamingDistributionLogging(Property):
    """
    AWS Object Type = "AWS::CloudFront::StreamingDistribution.Logging"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-logging.html

    Property Document:
    
    - ``rp_Bucket``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-logging.html#cfn-cloudfront-streamingdistribution-logging-bucket
    - ``rp_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-logging.html#cfn-cloudfront-streamingdistribution-logging-enabled
    - ``rp_Prefix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-logging.html#cfn-cloudfront-streamingdistribution-logging-prefix
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::StreamingDistribution.Logging"
    
    rp_Bucket: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Bucket"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-logging.html#cfn-cloudfront-streamingdistribution-logging-bucket"""
    rp_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-logging.html#cfn-cloudfront-streamingdistribution-logging-enabled"""
    rp_Prefix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Prefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-logging.html#cfn-cloudfront-streamingdistribution-logging-prefix"""

@attr.s
class PropResponseHeadersPolicyReferrerPolicy(Property):
    """
    AWS Object Type = "AWS::CloudFront::ResponseHeadersPolicy.ReferrerPolicy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-referrerpolicy.html

    Property Document:
    
    - ``rp_Override``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-referrerpolicy.html#cfn-cloudfront-responseheaderspolicy-referrerpolicy-override
    - ``rp_ReferrerPolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-referrerpolicy.html#cfn-cloudfront-responseheaderspolicy-referrerpolicy-referrerpolicy
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::ResponseHeadersPolicy.ReferrerPolicy"
    
    rp_Override: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Override"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-referrerpolicy.html#cfn-cloudfront-responseheaderspolicy-referrerpolicy-override"""
    rp_ReferrerPolicy: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ReferrerPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-referrerpolicy.html#cfn-cloudfront-responseheaderspolicy-referrerpolicy-referrerpolicy"""

@attr.s
class PropDistributionLambdaFunctionAssociation(Property):
    """
    AWS Object Type = "AWS::CloudFront::Distribution.LambdaFunctionAssociation"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-lambdafunctionassociation.html

    Property Document:
    
    - ``p_EventType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-lambdafunctionassociation.html#cfn-cloudfront-distribution-lambdafunctionassociation-eventtype
    - ``p_IncludeBody``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-lambdafunctionassociation.html#cfn-cloudfront-distribution-lambdafunctionassociation-includebody
    - ``p_LambdaFunctionARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-lambdafunctionassociation.html#cfn-cloudfront-distribution-lambdafunctionassociation-lambdafunctionarn
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::Distribution.LambdaFunctionAssociation"
    
    p_EventType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "EventType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-lambdafunctionassociation.html#cfn-cloudfront-distribution-lambdafunctionassociation-eventtype"""
    p_IncludeBody: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IncludeBody"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-lambdafunctionassociation.html#cfn-cloudfront-distribution-lambdafunctionassociation-includebody"""
    p_LambdaFunctionARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LambdaFunctionARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-lambdafunctionassociation.html#cfn-cloudfront-distribution-lambdafunctionassociation-lambdafunctionarn"""

@attr.s
class PropOriginRequestPolicyCookiesConfig(Property):
    """
    AWS Object Type = "AWS::CloudFront::OriginRequestPolicy.CookiesConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-cookiesconfig.html

    Property Document:
    
    - ``rp_CookieBehavior``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-cookiesconfig.html#cfn-cloudfront-originrequestpolicy-cookiesconfig-cookiebehavior
    - ``p_Cookies``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-cookiesconfig.html#cfn-cloudfront-originrequestpolicy-cookiesconfig-cookies
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::OriginRequestPolicy.CookiesConfig"
    
    rp_CookieBehavior: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "CookieBehavior"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-cookiesconfig.html#cfn-cloudfront-originrequestpolicy-cookiesconfig-cookiebehavior"""
    p_Cookies: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Cookies"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-cookiesconfig.html#cfn-cloudfront-originrequestpolicy-cookiesconfig-cookies"""

@attr.s
class PropDistributionOriginGroupMember(Property):
    """
    AWS Object Type = "AWS::CloudFront::Distribution.OriginGroupMember"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupmember.html

    Property Document:
    
    - ``rp_OriginId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupmember.html#cfn-cloudfront-distribution-origingroupmember-originid
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::Distribution.OriginGroupMember"
    
    rp_OriginId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "OriginId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupmember.html#cfn-cloudfront-distribution-origingroupmember-originid"""

@attr.s
class PropResponseHeadersPolicyAccessControlAllowHeaders(Property):
    """
    AWS Object Type = "AWS::CloudFront::ResponseHeadersPolicy.AccessControlAllowHeaders"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolallowheaders.html

    Property Document:
    
    - ``rp_Items``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolallowheaders.html#cfn-cloudfront-responseheaderspolicy-accesscontrolallowheaders-items
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::ResponseHeadersPolicy.AccessControlAllowHeaders"
    
    rp_Items: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Items"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolallowheaders.html#cfn-cloudfront-responseheaderspolicy-accesscontrolallowheaders-items"""

@attr.s
class PropStreamingDistributionTrustedSigners(Property):
    """
    AWS Object Type = "AWS::CloudFront::StreamingDistribution.TrustedSigners"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-trustedsigners.html

    Property Document:
    
    - ``rp_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-trustedsigners.html#cfn-cloudfront-streamingdistribution-trustedsigners-enabled
    - ``p_AwsAccountNumbers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-trustedsigners.html#cfn-cloudfront-streamingdistribution-trustedsigners-awsaccountnumbers
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::StreamingDistribution.TrustedSigners"
    
    rp_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-trustedsigners.html#cfn-cloudfront-streamingdistribution-trustedsigners-enabled"""
    p_AwsAccountNumbers: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AwsAccountNumbers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-trustedsigners.html#cfn-cloudfront-streamingdistribution-trustedsigners-awsaccountnumbers"""

@attr.s
class PropDistributionLegacyCustomOrigin(Property):
    """
    AWS Object Type = "AWS::CloudFront::Distribution.LegacyCustomOrigin"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacycustomorigin.html

    Property Document:
    
    - ``rp_DNSName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacycustomorigin.html#cfn-cloudfront-distribution-legacycustomorigin-dnsname
    - ``rp_OriginProtocolPolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacycustomorigin.html#cfn-cloudfront-distribution-legacycustomorigin-originprotocolpolicy
    - ``rp_OriginSSLProtocols``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacycustomorigin.html#cfn-cloudfront-distribution-legacycustomorigin-originsslprotocols
    - ``p_HTTPPort``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacycustomorigin.html#cfn-cloudfront-distribution-legacycustomorigin-httpport
    - ``p_HTTPSPort``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacycustomorigin.html#cfn-cloudfront-distribution-legacycustomorigin-httpsport
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::Distribution.LegacyCustomOrigin"
    
    rp_DNSName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DNSName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacycustomorigin.html#cfn-cloudfront-distribution-legacycustomorigin-dnsname"""
    rp_OriginProtocolPolicy: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "OriginProtocolPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacycustomorigin.html#cfn-cloudfront-distribution-legacycustomorigin-originprotocolpolicy"""
    rp_OriginSSLProtocols: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "OriginSSLProtocols"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacycustomorigin.html#cfn-cloudfront-distribution-legacycustomorigin-originsslprotocols"""
    p_HTTPPort: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "HTTPPort"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacycustomorigin.html#cfn-cloudfront-distribution-legacycustomorigin-httpport"""
    p_HTTPSPort: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "HTTPSPort"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacycustomorigin.html#cfn-cloudfront-distribution-legacycustomorigin-httpsport"""

@attr.s
class PropResponseHeadersPolicyFrameOptions(Property):
    """
    AWS Object Type = "AWS::CloudFront::ResponseHeadersPolicy.FrameOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-frameoptions.html

    Property Document:
    
    - ``rp_FrameOption``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-frameoptions.html#cfn-cloudfront-responseheaderspolicy-frameoptions-frameoption
    - ``rp_Override``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-frameoptions.html#cfn-cloudfront-responseheaderspolicy-frameoptions-override
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::ResponseHeadersPolicy.FrameOptions"
    
    rp_FrameOption: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "FrameOption"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-frameoptions.html#cfn-cloudfront-responseheaderspolicy-frameoptions-frameoption"""
    rp_Override: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Override"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-frameoptions.html#cfn-cloudfront-responseheaderspolicy-frameoptions-override"""

@attr.s
class PropDistributionRestrictions(Property):
    """
    AWS Object Type = "AWS::CloudFront::Distribution.Restrictions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-restrictions.html

    Property Document:
    
    - ``rp_GeoRestriction``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-restrictions.html#cfn-cloudfront-distribution-restrictions-georestriction
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::Distribution.Restrictions"
    
    rp_GeoRestriction: typing.Union['PropDistributionGeoRestriction', dict] = attr.ib(
        default=None,
        converter=PropDistributionGeoRestriction.from_dict,
        validator=attr.validators.instance_of(PropDistributionGeoRestriction),
        metadata={AttrMeta.PROPERTY_NAME: "GeoRestriction"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-restrictions.html#cfn-cloudfront-distribution-restrictions-georestriction"""

@attr.s
class PropResponseHeadersPolicyCustomHeader(Property):
    """
    AWS Object Type = "AWS::CloudFront::ResponseHeadersPolicy.CustomHeader"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-customheader.html

    Property Document:
    
    - ``rp_Header``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-customheader.html#cfn-cloudfront-responseheaderspolicy-customheader-header
    - ``rp_Override``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-customheader.html#cfn-cloudfront-responseheaderspolicy-customheader-override
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-customheader.html#cfn-cloudfront-responseheaderspolicy-customheader-value
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::ResponseHeadersPolicy.CustomHeader"
    
    rp_Header: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Header"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-customheader.html#cfn-cloudfront-responseheaderspolicy-customheader-header"""
    rp_Override: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Override"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-customheader.html#cfn-cloudfront-responseheaderspolicy-customheader-override"""
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-customheader.html#cfn-cloudfront-responseheaderspolicy-customheader-value"""

@attr.s
class PropResponseHeadersPolicyContentSecurityPolicy(Property):
    """
    AWS Object Type = "AWS::CloudFront::ResponseHeadersPolicy.ContentSecurityPolicy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-contentsecuritypolicy.html

    Property Document:
    
    - ``rp_ContentSecurityPolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-contentsecuritypolicy.html#cfn-cloudfront-responseheaderspolicy-contentsecuritypolicy-contentsecuritypolicy
    - ``rp_Override``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-contentsecuritypolicy.html#cfn-cloudfront-responseheaderspolicy-contentsecuritypolicy-override
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::ResponseHeadersPolicy.ContentSecurityPolicy"
    
    rp_ContentSecurityPolicy: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ContentSecurityPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-contentsecuritypolicy.html#cfn-cloudfront-responseheaderspolicy-contentsecuritypolicy-contentsecuritypolicy"""
    rp_Override: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Override"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-contentsecuritypolicy.html#cfn-cloudfront-responseheaderspolicy-contentsecuritypolicy-override"""

@attr.s
class PropPublicKeyPublicKeyConfig(Property):
    """
    AWS Object Type = "AWS::CloudFront::PublicKey.PublicKeyConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-publickey-publickeyconfig.html

    Property Document:
    
    - ``rp_CallerReference``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-publickey-publickeyconfig.html#cfn-cloudfront-publickey-publickeyconfig-callerreference
    - ``rp_EncodedKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-publickey-publickeyconfig.html#cfn-cloudfront-publickey-publickeyconfig-encodedkey
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-publickey-publickeyconfig.html#cfn-cloudfront-publickey-publickeyconfig-name
    - ``p_Comment``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-publickey-publickeyconfig.html#cfn-cloudfront-publickey-publickeyconfig-comment
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::PublicKey.PublicKeyConfig"
    
    rp_CallerReference: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "CallerReference"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-publickey-publickeyconfig.html#cfn-cloudfront-publickey-publickeyconfig-callerreference"""
    rp_EncodedKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "EncodedKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-publickey-publickeyconfig.html#cfn-cloudfront-publickey-publickeyconfig-encodedkey"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-publickey-publickeyconfig.html#cfn-cloudfront-publickey-publickeyconfig-name"""
    p_Comment: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Comment"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-publickey-publickeyconfig.html#cfn-cloudfront-publickey-publickeyconfig-comment"""

@attr.s
class PropDistributionStatusCodes(Property):
    """
    AWS Object Type = "AWS::CloudFront::Distribution.StatusCodes"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-statuscodes.html

    Property Document:
    
    - ``rp_Items``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-statuscodes.html#cfn-cloudfront-distribution-statuscodes-items
    - ``rp_Quantity``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-statuscodes.html#cfn-cloudfront-distribution-statuscodes-quantity
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::Distribution.StatusCodes"
    
    rp_Items: typing.List[int] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(int), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Items"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-statuscodes.html#cfn-cloudfront-distribution-statuscodes-items"""
    rp_Quantity: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Quantity"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-statuscodes.html#cfn-cloudfront-distribution-statuscodes-quantity"""

@attr.s
class PropFunctionFunctionConfig(Property):
    """
    AWS Object Type = "AWS::CloudFront::Function.FunctionConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-function-functionconfig.html

    Property Document:
    
    - ``rp_Comment``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-function-functionconfig.html#cfn-cloudfront-function-functionconfig-comment
    - ``rp_Runtime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-function-functionconfig.html#cfn-cloudfront-function-functionconfig-runtime
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::Function.FunctionConfig"
    
    rp_Comment: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Comment"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-function-functionconfig.html#cfn-cloudfront-function-functionconfig-comment"""
    rp_Runtime: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Runtime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-function-functionconfig.html#cfn-cloudfront-function-functionconfig-runtime"""

@attr.s
class PropOriginRequestPolicyQueryStringsConfig(Property):
    """
    AWS Object Type = "AWS::CloudFront::OriginRequestPolicy.QueryStringsConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-querystringsconfig.html

    Property Document:
    
    - ``rp_QueryStringBehavior``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-querystringsconfig.html#cfn-cloudfront-originrequestpolicy-querystringsconfig-querystringbehavior
    - ``p_QueryStrings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-querystringsconfig.html#cfn-cloudfront-originrequestpolicy-querystringsconfig-querystrings
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::OriginRequestPolicy.QueryStringsConfig"
    
    rp_QueryStringBehavior: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "QueryStringBehavior"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-querystringsconfig.html#cfn-cloudfront-originrequestpolicy-querystringsconfig-querystringbehavior"""
    p_QueryStrings: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "QueryStrings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-querystringsconfig.html#cfn-cloudfront-originrequestpolicy-querystringsconfig-querystrings"""

@attr.s
class PropDistributionOriginGroupFailoverCriteria(Property):
    """
    AWS Object Type = "AWS::CloudFront::Distribution.OriginGroupFailoverCriteria"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupfailovercriteria.html

    Property Document:
    
    - ``rp_StatusCodes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupfailovercriteria.html#cfn-cloudfront-distribution-origingroupfailovercriteria-statuscodes
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::Distribution.OriginGroupFailoverCriteria"
    
    rp_StatusCodes: typing.Union['PropDistributionStatusCodes', dict] = attr.ib(
        default=None,
        converter=PropDistributionStatusCodes.from_dict,
        validator=attr.validators.instance_of(PropDistributionStatusCodes),
        metadata={AttrMeta.PROPERTY_NAME: "StatusCodes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupfailovercriteria.html#cfn-cloudfront-distribution-origingroupfailovercriteria-statuscodes"""

@attr.s
class PropDistributionForwardedValues(Property):
    """
    AWS Object Type = "AWS::CloudFront::Distribution.ForwardedValues"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-forwardedvalues.html

    Property Document:
    
    - ``rp_QueryString``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-forwardedvalues.html#cfn-cloudfront-distribution-forwardedvalues-querystring
    - ``p_Cookies``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-forwardedvalues.html#cfn-cloudfront-distribution-forwardedvalues-cookies
    - ``p_Headers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-forwardedvalues.html#cfn-cloudfront-distribution-forwardedvalues-headers
    - ``p_QueryStringCacheKeys``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-forwardedvalues.html#cfn-cloudfront-distribution-forwardedvalues-querystringcachekeys
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::Distribution.ForwardedValues"
    
    rp_QueryString: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "QueryString"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-forwardedvalues.html#cfn-cloudfront-distribution-forwardedvalues-querystring"""
    p_Cookies: typing.Union['PropDistributionCookies', dict] = attr.ib(
        default=None,
        converter=PropDistributionCookies.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDistributionCookies)),
        metadata={AttrMeta.PROPERTY_NAME: "Cookies"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-forwardedvalues.html#cfn-cloudfront-distribution-forwardedvalues-cookies"""
    p_Headers: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Headers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-forwardedvalues.html#cfn-cloudfront-distribution-forwardedvalues-headers"""
    p_QueryStringCacheKeys: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "QueryStringCacheKeys"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-forwardedvalues.html#cfn-cloudfront-distribution-forwardedvalues-querystringcachekeys"""

@attr.s
class PropResponseHeadersPolicyStrictTransportSecurity(Property):
    """
    AWS Object Type = "AWS::CloudFront::ResponseHeadersPolicy.StrictTransportSecurity"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-stricttransportsecurity.html

    Property Document:
    
    - ``rp_AccessControlMaxAgeSec``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-stricttransportsecurity.html#cfn-cloudfront-responseheaderspolicy-stricttransportsecurity-accesscontrolmaxagesec
    - ``rp_Override``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-stricttransportsecurity.html#cfn-cloudfront-responseheaderspolicy-stricttransportsecurity-override
    - ``p_IncludeSubdomains``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-stricttransportsecurity.html#cfn-cloudfront-responseheaderspolicy-stricttransportsecurity-includesubdomains
    - ``p_Preload``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-stricttransportsecurity.html#cfn-cloudfront-responseheaderspolicy-stricttransportsecurity-preload
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::ResponseHeadersPolicy.StrictTransportSecurity"
    
    rp_AccessControlMaxAgeSec: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "AccessControlMaxAgeSec"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-stricttransportsecurity.html#cfn-cloudfront-responseheaderspolicy-stricttransportsecurity-accesscontrolmaxagesec"""
    rp_Override: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Override"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-stricttransportsecurity.html#cfn-cloudfront-responseheaderspolicy-stricttransportsecurity-override"""
    p_IncludeSubdomains: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IncludeSubdomains"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-stricttransportsecurity.html#cfn-cloudfront-responseheaderspolicy-stricttransportsecurity-includesubdomains"""
    p_Preload: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Preload"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-stricttransportsecurity.html#cfn-cloudfront-responseheaderspolicy-stricttransportsecurity-preload"""

@attr.s
class PropFunctionFunctionMetadata(Property):
    """
    AWS Object Type = "AWS::CloudFront::Function.FunctionMetadata"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-function-functionmetadata.html

    Property Document:
    
    - ``p_FunctionARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-function-functionmetadata.html#cfn-cloudfront-function-functionmetadata-functionarn
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::Function.FunctionMetadata"
    
    p_FunctionARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "FunctionARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-function-functionmetadata.html#cfn-cloudfront-function-functionmetadata-functionarn"""

@attr.s
class PropResponseHeadersPolicyAccessControlAllowOrigins(Property):
    """
    AWS Object Type = "AWS::CloudFront::ResponseHeadersPolicy.AccessControlAllowOrigins"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolalloworigins.html

    Property Document:
    
    - ``rp_Items``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolalloworigins.html#cfn-cloudfront-responseheaderspolicy-accesscontrolalloworigins-items
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::ResponseHeadersPolicy.AccessControlAllowOrigins"
    
    rp_Items: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Items"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolalloworigins.html#cfn-cloudfront-responseheaderspolicy-accesscontrolalloworigins-items"""

@attr.s
class PropResponseHeadersPolicyContentTypeOptions(Property):
    """
    AWS Object Type = "AWS::CloudFront::ResponseHeadersPolicy.ContentTypeOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-contenttypeoptions.html

    Property Document:
    
    - ``rp_Override``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-contenttypeoptions.html#cfn-cloudfront-responseheaderspolicy-contenttypeoptions-override
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::ResponseHeadersPolicy.ContentTypeOptions"
    
    rp_Override: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Override"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-contenttypeoptions.html#cfn-cloudfront-responseheaderspolicy-contenttypeoptions-override"""

@attr.s
class PropDistributionOriginShield(Property):
    """
    AWS Object Type = "AWS::CloudFront::Distribution.OriginShield"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-originshield.html

    Property Document:
    
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-originshield.html#cfn-cloudfront-distribution-originshield-enabled
    - ``p_OriginShieldRegion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-originshield.html#cfn-cloudfront-distribution-originshield-originshieldregion
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::Distribution.OriginShield"
    
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-originshield.html#cfn-cloudfront-distribution-originshield-enabled"""
    p_OriginShieldRegion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "OriginShieldRegion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-originshield.html#cfn-cloudfront-distribution-originshield-originshieldregion"""

@attr.s
class PropDistributionS3OriginConfig(Property):
    """
    AWS Object Type = "AWS::CloudFront::Distribution.S3OriginConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-s3originconfig.html

    Property Document:
    
    - ``p_OriginAccessIdentity``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-s3originconfig.html#cfn-cloudfront-distribution-s3originconfig-originaccessidentity
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::Distribution.S3OriginConfig"
    
    p_OriginAccessIdentity: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "OriginAccessIdentity"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-s3originconfig.html#cfn-cloudfront-distribution-s3originconfig-originaccessidentity"""

@attr.s
class PropRealtimeLogConfigKinesisStreamConfig(Property):
    """
    AWS Object Type = "AWS::CloudFront::RealtimeLogConfig.KinesisStreamConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-realtimelogconfig-kinesisstreamconfig.html

    Property Document:
    
    - ``rp_RoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-realtimelogconfig-kinesisstreamconfig.html#cfn-cloudfront-realtimelogconfig-kinesisstreamconfig-rolearn
    - ``rp_StreamArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-realtimelogconfig-kinesisstreamconfig.html#cfn-cloudfront-realtimelogconfig-kinesisstreamconfig-streamarn
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::RealtimeLogConfig.KinesisStreamConfig"
    
    rp_RoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-realtimelogconfig-kinesisstreamconfig.html#cfn-cloudfront-realtimelogconfig-kinesisstreamconfig-rolearn"""
    rp_StreamArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "StreamArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-realtimelogconfig-kinesisstreamconfig.html#cfn-cloudfront-realtimelogconfig-kinesisstreamconfig-streamarn"""

@attr.s
class PropResponseHeadersPolicyCustomHeadersConfig(Property):
    """
    AWS Object Type = "AWS::CloudFront::ResponseHeadersPolicy.CustomHeadersConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-customheadersconfig.html

    Property Document:
    
    - ``rp_Items``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-customheadersconfig.html#cfn-cloudfront-responseheaderspolicy-customheadersconfig-items
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::ResponseHeadersPolicy.CustomHeadersConfig"
    
    rp_Items: typing.List[typing.Union['PropResponseHeadersPolicyCustomHeader', dict]] = attr.ib(
        default=None,
        converter=PropResponseHeadersPolicyCustomHeader.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropResponseHeadersPolicyCustomHeader), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Items"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-customheadersconfig.html#cfn-cloudfront-responseheaderspolicy-customheadersconfig-items"""

@attr.s
class PropCachePolicyQueryStringsConfig(Property):
    """
    AWS Object Type = "AWS::CloudFront::CachePolicy.QueryStringsConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-querystringsconfig.html

    Property Document:
    
    - ``rp_QueryStringBehavior``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-querystringsconfig.html#cfn-cloudfront-cachepolicy-querystringsconfig-querystringbehavior
    - ``p_QueryStrings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-querystringsconfig.html#cfn-cloudfront-cachepolicy-querystringsconfig-querystrings
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::CachePolicy.QueryStringsConfig"
    
    rp_QueryStringBehavior: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "QueryStringBehavior"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-querystringsconfig.html#cfn-cloudfront-cachepolicy-querystringsconfig-querystringbehavior"""
    p_QueryStrings: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "QueryStrings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-querystringsconfig.html#cfn-cloudfront-cachepolicy-querystringsconfig-querystrings"""

@attr.s
class PropDistributionLogging(Property):
    """
    AWS Object Type = "AWS::CloudFront::Distribution.Logging"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-logging.html

    Property Document:
    
    - ``rp_Bucket``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-logging.html#cfn-cloudfront-distribution-logging-bucket
    - ``p_IncludeCookies``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-logging.html#cfn-cloudfront-distribution-logging-includecookies
    - ``p_Prefix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-logging.html#cfn-cloudfront-distribution-logging-prefix
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::Distribution.Logging"
    
    rp_Bucket: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Bucket"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-logging.html#cfn-cloudfront-distribution-logging-bucket"""
    p_IncludeCookies: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IncludeCookies"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-logging.html#cfn-cloudfront-distribution-logging-includecookies"""
    p_Prefix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Prefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-logging.html#cfn-cloudfront-distribution-logging-prefix"""

@attr.s
class PropOriginRequestPolicyHeadersConfig(Property):
    """
    AWS Object Type = "AWS::CloudFront::OriginRequestPolicy.HeadersConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-headersconfig.html

    Property Document:
    
    - ``rp_HeaderBehavior``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-headersconfig.html#cfn-cloudfront-originrequestpolicy-headersconfig-headerbehavior
    - ``p_Headers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-headersconfig.html#cfn-cloudfront-originrequestpolicy-headersconfig-headers
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::OriginRequestPolicy.HeadersConfig"
    
    rp_HeaderBehavior: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "HeaderBehavior"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-headersconfig.html#cfn-cloudfront-originrequestpolicy-headersconfig-headerbehavior"""
    p_Headers: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Headers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-headersconfig.html#cfn-cloudfront-originrequestpolicy-headersconfig-headers"""

@attr.s
class PropDistributionFunctionAssociation(Property):
    """
    AWS Object Type = "AWS::CloudFront::Distribution.FunctionAssociation"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-functionassociation.html

    Property Document:
    
    - ``p_EventType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-functionassociation.html#cfn-cloudfront-distribution-functionassociation-eventtype
    - ``p_FunctionARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-functionassociation.html#cfn-cloudfront-distribution-functionassociation-functionarn
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::Distribution.FunctionAssociation"
    
    p_EventType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "EventType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-functionassociation.html#cfn-cloudfront-distribution-functionassociation-eventtype"""
    p_FunctionARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "FunctionARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-functionassociation.html#cfn-cloudfront-distribution-functionassociation-functionarn"""

@attr.s
class PropCachePolicyCookiesConfig(Property):
    """
    AWS Object Type = "AWS::CloudFront::CachePolicy.CookiesConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cookiesconfig.html

    Property Document:
    
    - ``rp_CookieBehavior``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cookiesconfig.html#cfn-cloudfront-cachepolicy-cookiesconfig-cookiebehavior
    - ``p_Cookies``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cookiesconfig.html#cfn-cloudfront-cachepolicy-cookiesconfig-cookies
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::CachePolicy.CookiesConfig"
    
    rp_CookieBehavior: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "CookieBehavior"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cookiesconfig.html#cfn-cloudfront-cachepolicy-cookiesconfig-cookiebehavior"""
    p_Cookies: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Cookies"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cookiesconfig.html#cfn-cloudfront-cachepolicy-cookiesconfig-cookies"""

@attr.s
class PropOriginRequestPolicyOriginRequestPolicyConfig(Property):
    """
    AWS Object Type = "AWS::CloudFront::OriginRequestPolicy.OriginRequestPolicyConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-originrequestpolicyconfig.html

    Property Document:
    
    - ``rp_CookiesConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-originrequestpolicyconfig.html#cfn-cloudfront-originrequestpolicy-originrequestpolicyconfig-cookiesconfig
    - ``rp_HeadersConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-originrequestpolicyconfig.html#cfn-cloudfront-originrequestpolicy-originrequestpolicyconfig-headersconfig
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-originrequestpolicyconfig.html#cfn-cloudfront-originrequestpolicy-originrequestpolicyconfig-name
    - ``rp_QueryStringsConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-originrequestpolicyconfig.html#cfn-cloudfront-originrequestpolicy-originrequestpolicyconfig-querystringsconfig
    - ``p_Comment``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-originrequestpolicyconfig.html#cfn-cloudfront-originrequestpolicy-originrequestpolicyconfig-comment
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::OriginRequestPolicy.OriginRequestPolicyConfig"
    
    rp_CookiesConfig: typing.Union['PropOriginRequestPolicyCookiesConfig', dict] = attr.ib(
        default=None,
        converter=PropOriginRequestPolicyCookiesConfig.from_dict,
        validator=attr.validators.instance_of(PropOriginRequestPolicyCookiesConfig),
        metadata={AttrMeta.PROPERTY_NAME: "CookiesConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-originrequestpolicyconfig.html#cfn-cloudfront-originrequestpolicy-originrequestpolicyconfig-cookiesconfig"""
    rp_HeadersConfig: typing.Union['PropOriginRequestPolicyHeadersConfig', dict] = attr.ib(
        default=None,
        converter=PropOriginRequestPolicyHeadersConfig.from_dict,
        validator=attr.validators.instance_of(PropOriginRequestPolicyHeadersConfig),
        metadata={AttrMeta.PROPERTY_NAME: "HeadersConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-originrequestpolicyconfig.html#cfn-cloudfront-originrequestpolicy-originrequestpolicyconfig-headersconfig"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-originrequestpolicyconfig.html#cfn-cloudfront-originrequestpolicy-originrequestpolicyconfig-name"""
    rp_QueryStringsConfig: typing.Union['PropOriginRequestPolicyQueryStringsConfig', dict] = attr.ib(
        default=None,
        converter=PropOriginRequestPolicyQueryStringsConfig.from_dict,
        validator=attr.validators.instance_of(PropOriginRequestPolicyQueryStringsConfig),
        metadata={AttrMeta.PROPERTY_NAME: "QueryStringsConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-originrequestpolicyconfig.html#cfn-cloudfront-originrequestpolicy-originrequestpolicyconfig-querystringsconfig"""
    p_Comment: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Comment"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-originrequestpolicyconfig.html#cfn-cloudfront-originrequestpolicy-originrequestpolicyconfig-comment"""

@attr.s
class PropDistributionOriginGroupMembers(Property):
    """
    AWS Object Type = "AWS::CloudFront::Distribution.OriginGroupMembers"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupmembers.html

    Property Document:
    
    - ``rp_Items``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupmembers.html#cfn-cloudfront-distribution-origingroupmembers-items
    - ``rp_Quantity``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupmembers.html#cfn-cloudfront-distribution-origingroupmembers-quantity
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::Distribution.OriginGroupMembers"
    
    rp_Items: typing.List[typing.Union['PropDistributionOriginGroupMember', dict]] = attr.ib(
        default=None,
        converter=PropDistributionOriginGroupMember.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDistributionOriginGroupMember), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Items"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupmembers.html#cfn-cloudfront-distribution-origingroupmembers-items"""
    rp_Quantity: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Quantity"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupmembers.html#cfn-cloudfront-distribution-origingroupmembers-quantity"""

@attr.s
class PropCachePolicyParametersInCacheKeyAndForwardedToOrigin(Property):
    """
    AWS Object Type = "AWS::CloudFront::CachePolicy.ParametersInCacheKeyAndForwardedToOrigin"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin.html

    Property Document:
    
    - ``rp_CookiesConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin.html#cfn-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin-cookiesconfig
    - ``rp_EnableAcceptEncodingGzip``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin.html#cfn-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin-enableacceptencodinggzip
    - ``rp_HeadersConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin.html#cfn-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin-headersconfig
    - ``rp_QueryStringsConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin.html#cfn-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin-querystringsconfig
    - ``p_EnableAcceptEncodingBrotli``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin.html#cfn-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin-enableacceptencodingbrotli
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::CachePolicy.ParametersInCacheKeyAndForwardedToOrigin"
    
    rp_CookiesConfig: typing.Union['PropCachePolicyCookiesConfig', dict] = attr.ib(
        default=None,
        converter=PropCachePolicyCookiesConfig.from_dict,
        validator=attr.validators.instance_of(PropCachePolicyCookiesConfig),
        metadata={AttrMeta.PROPERTY_NAME: "CookiesConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin.html#cfn-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin-cookiesconfig"""
    rp_EnableAcceptEncodingGzip: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "EnableAcceptEncodingGzip"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin.html#cfn-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin-enableacceptencodinggzip"""
    rp_HeadersConfig: typing.Union['PropCachePolicyHeadersConfig', dict] = attr.ib(
        default=None,
        converter=PropCachePolicyHeadersConfig.from_dict,
        validator=attr.validators.instance_of(PropCachePolicyHeadersConfig),
        metadata={AttrMeta.PROPERTY_NAME: "HeadersConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin.html#cfn-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin-headersconfig"""
    rp_QueryStringsConfig: typing.Union['PropCachePolicyQueryStringsConfig', dict] = attr.ib(
        default=None,
        converter=PropCachePolicyQueryStringsConfig.from_dict,
        validator=attr.validators.instance_of(PropCachePolicyQueryStringsConfig),
        metadata={AttrMeta.PROPERTY_NAME: "QueryStringsConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin.html#cfn-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin-querystringsconfig"""
    p_EnableAcceptEncodingBrotli: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EnableAcceptEncodingBrotli"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin.html#cfn-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin-enableacceptencodingbrotli"""

@attr.s
class PropRealtimeLogConfigEndPoint(Property):
    """
    AWS Object Type = "AWS::CloudFront::RealtimeLogConfig.EndPoint"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-realtimelogconfig-endpoint.html

    Property Document:
    
    - ``rp_KinesisStreamConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-realtimelogconfig-endpoint.html#cfn-cloudfront-realtimelogconfig-endpoint-kinesisstreamconfig
    - ``rp_StreamType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-realtimelogconfig-endpoint.html#cfn-cloudfront-realtimelogconfig-endpoint-streamtype
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::RealtimeLogConfig.EndPoint"
    
    rp_KinesisStreamConfig: typing.Union['PropRealtimeLogConfigKinesisStreamConfig', dict] = attr.ib(
        default=None,
        converter=PropRealtimeLogConfigKinesisStreamConfig.from_dict,
        validator=attr.validators.instance_of(PropRealtimeLogConfigKinesisStreamConfig),
        metadata={AttrMeta.PROPERTY_NAME: "KinesisStreamConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-realtimelogconfig-endpoint.html#cfn-cloudfront-realtimelogconfig-endpoint-kinesisstreamconfig"""
    rp_StreamType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "StreamType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-realtimelogconfig-endpoint.html#cfn-cloudfront-realtimelogconfig-endpoint-streamtype"""

@attr.s
class PropResponseHeadersPolicyCorsConfig(Property):
    """
    AWS Object Type = "AWS::CloudFront::ResponseHeadersPolicy.CorsConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-corsconfig.html

    Property Document:
    
    - ``rp_AccessControlAllowCredentials``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-corsconfig.html#cfn-cloudfront-responseheaderspolicy-corsconfig-accesscontrolallowcredentials
    - ``rp_AccessControlAllowHeaders``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-corsconfig.html#cfn-cloudfront-responseheaderspolicy-corsconfig-accesscontrolallowheaders
    - ``rp_AccessControlAllowMethods``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-corsconfig.html#cfn-cloudfront-responseheaderspolicy-corsconfig-accesscontrolallowmethods
    - ``rp_AccessControlAllowOrigins``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-corsconfig.html#cfn-cloudfront-responseheaderspolicy-corsconfig-accesscontrolalloworigins
    - ``rp_OriginOverride``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-corsconfig.html#cfn-cloudfront-responseheaderspolicy-corsconfig-originoverride
    - ``p_AccessControlExposeHeaders``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-corsconfig.html#cfn-cloudfront-responseheaderspolicy-corsconfig-accesscontrolexposeheaders
    - ``p_AccessControlMaxAgeSec``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-corsconfig.html#cfn-cloudfront-responseheaderspolicy-corsconfig-accesscontrolmaxagesec
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::ResponseHeadersPolicy.CorsConfig"
    
    rp_AccessControlAllowCredentials: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "AccessControlAllowCredentials"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-corsconfig.html#cfn-cloudfront-responseheaderspolicy-corsconfig-accesscontrolallowcredentials"""
    rp_AccessControlAllowHeaders: typing.Union['PropResponseHeadersPolicyAccessControlAllowHeaders', dict] = attr.ib(
        default=None,
        converter=PropResponseHeadersPolicyAccessControlAllowHeaders.from_dict,
        validator=attr.validators.instance_of(PropResponseHeadersPolicyAccessControlAllowHeaders),
        metadata={AttrMeta.PROPERTY_NAME: "AccessControlAllowHeaders"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-corsconfig.html#cfn-cloudfront-responseheaderspolicy-corsconfig-accesscontrolallowheaders"""
    rp_AccessControlAllowMethods: typing.Union['PropResponseHeadersPolicyAccessControlAllowMethods', dict] = attr.ib(
        default=None,
        converter=PropResponseHeadersPolicyAccessControlAllowMethods.from_dict,
        validator=attr.validators.instance_of(PropResponseHeadersPolicyAccessControlAllowMethods),
        metadata={AttrMeta.PROPERTY_NAME: "AccessControlAllowMethods"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-corsconfig.html#cfn-cloudfront-responseheaderspolicy-corsconfig-accesscontrolallowmethods"""
    rp_AccessControlAllowOrigins: typing.Union['PropResponseHeadersPolicyAccessControlAllowOrigins', dict] = attr.ib(
        default=None,
        converter=PropResponseHeadersPolicyAccessControlAllowOrigins.from_dict,
        validator=attr.validators.instance_of(PropResponseHeadersPolicyAccessControlAllowOrigins),
        metadata={AttrMeta.PROPERTY_NAME: "AccessControlAllowOrigins"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-corsconfig.html#cfn-cloudfront-responseheaderspolicy-corsconfig-accesscontrolalloworigins"""
    rp_OriginOverride: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "OriginOverride"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-corsconfig.html#cfn-cloudfront-responseheaderspolicy-corsconfig-originoverride"""
    p_AccessControlExposeHeaders: typing.Union['PropResponseHeadersPolicyAccessControlExposeHeaders', dict] = attr.ib(
        default=None,
        converter=PropResponseHeadersPolicyAccessControlExposeHeaders.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResponseHeadersPolicyAccessControlExposeHeaders)),
        metadata={AttrMeta.PROPERTY_NAME: "AccessControlExposeHeaders"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-corsconfig.html#cfn-cloudfront-responseheaderspolicy-corsconfig-accesscontrolexposeheaders"""
    p_AccessControlMaxAgeSec: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "AccessControlMaxAgeSec"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-corsconfig.html#cfn-cloudfront-responseheaderspolicy-corsconfig-accesscontrolmaxagesec"""

@attr.s
class PropStreamingDistributionStreamingDistributionConfig(Property):
    """
    AWS Object Type = "AWS::CloudFront::StreamingDistribution.StreamingDistributionConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html

    Property Document:
    
    - ``rp_Comment``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig-comment
    - ``rp_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig-enabled
    - ``rp_S3Origin``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig-s3origin
    - ``rp_TrustedSigners``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig-trustedsigners
    - ``p_Aliases``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig-aliases
    - ``p_Logging``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig-logging
    - ``p_PriceClass``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig-priceclass
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::StreamingDistribution.StreamingDistributionConfig"
    
    rp_Comment: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Comment"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig-comment"""
    rp_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig-enabled"""
    rp_S3Origin: typing.Union['PropStreamingDistributionS3Origin', dict] = attr.ib(
        default=None,
        converter=PropStreamingDistributionS3Origin.from_dict,
        validator=attr.validators.instance_of(PropStreamingDistributionS3Origin),
        metadata={AttrMeta.PROPERTY_NAME: "S3Origin"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig-s3origin"""
    rp_TrustedSigners: typing.Union['PropStreamingDistributionTrustedSigners', dict] = attr.ib(
        default=None,
        converter=PropStreamingDistributionTrustedSigners.from_dict,
        validator=attr.validators.instance_of(PropStreamingDistributionTrustedSigners),
        metadata={AttrMeta.PROPERTY_NAME: "TrustedSigners"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig-trustedsigners"""
    p_Aliases: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Aliases"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig-aliases"""
    p_Logging: typing.Union['PropStreamingDistributionLogging', dict] = attr.ib(
        default=None,
        converter=PropStreamingDistributionLogging.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropStreamingDistributionLogging)),
        metadata={AttrMeta.PROPERTY_NAME: "Logging"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig-logging"""
    p_PriceClass: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PriceClass"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig-priceclass"""

@attr.s
class PropDistributionCacheBehavior(Property):
    """
    AWS Object Type = "AWS::CloudFront::Distribution.CacheBehavior"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html

    Property Document:
    
    - ``rp_PathPattern``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-pathpattern
    - ``rp_TargetOriginId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-targetoriginid
    - ``rp_ViewerProtocolPolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-viewerprotocolpolicy
    - ``p_AllowedMethods``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-allowedmethods
    - ``p_CachePolicyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-cachepolicyid
    - ``p_CachedMethods``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-cachedmethods
    - ``p_Compress``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-compress
    - ``p_DefaultTTL``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-defaultttl
    - ``p_FieldLevelEncryptionId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-fieldlevelencryptionid
    - ``p_ForwardedValues``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-forwardedvalues
    - ``p_FunctionAssociations``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-functionassociations
    - ``p_LambdaFunctionAssociations``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-lambdafunctionassociations
    - ``p_MaxTTL``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-maxttl
    - ``p_MinTTL``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-minttl
    - ``p_OriginRequestPolicyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-originrequestpolicyid
    - ``p_RealtimeLogConfigArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-realtimelogconfigarn
    - ``p_ResponseHeadersPolicyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-responseheaderspolicyid
    - ``p_SmoothStreaming``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-smoothstreaming
    - ``p_TrustedKeyGroups``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-trustedkeygroups
    - ``p_TrustedSigners``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-trustedsigners
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::Distribution.CacheBehavior"
    
    rp_PathPattern: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PathPattern"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-pathpattern"""
    rp_TargetOriginId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TargetOriginId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-targetoriginid"""
    rp_ViewerProtocolPolicy: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ViewerProtocolPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-viewerprotocolpolicy"""
    p_AllowedMethods: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AllowedMethods"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-allowedmethods"""
    p_CachePolicyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CachePolicyId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-cachepolicyid"""
    p_CachedMethods: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "CachedMethods"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-cachedmethods"""
    p_Compress: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Compress"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-compress"""
    p_DefaultTTL: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultTTL"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-defaultttl"""
    p_FieldLevelEncryptionId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "FieldLevelEncryptionId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-fieldlevelencryptionid"""
    p_ForwardedValues: typing.Union['PropDistributionForwardedValues', dict] = attr.ib(
        default=None,
        converter=PropDistributionForwardedValues.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDistributionForwardedValues)),
        metadata={AttrMeta.PROPERTY_NAME: "ForwardedValues"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-forwardedvalues"""
    p_FunctionAssociations: typing.List[typing.Union['PropDistributionFunctionAssociation', dict]] = attr.ib(
        default=None,
        converter=PropDistributionFunctionAssociation.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDistributionFunctionAssociation), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "FunctionAssociations"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-functionassociations"""
    p_LambdaFunctionAssociations: typing.List[typing.Union['PropDistributionLambdaFunctionAssociation', dict]] = attr.ib(
        default=None,
        converter=PropDistributionLambdaFunctionAssociation.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDistributionLambdaFunctionAssociation), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "LambdaFunctionAssociations"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-lambdafunctionassociations"""
    p_MaxTTL: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "MaxTTL"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-maxttl"""
    p_MinTTL: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "MinTTL"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-minttl"""
    p_OriginRequestPolicyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "OriginRequestPolicyId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-originrequestpolicyid"""
    p_RealtimeLogConfigArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RealtimeLogConfigArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-realtimelogconfigarn"""
    p_ResponseHeadersPolicyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ResponseHeadersPolicyId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-responseheaderspolicyid"""
    p_SmoothStreaming: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "SmoothStreaming"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-smoothstreaming"""
    p_TrustedKeyGroups: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "TrustedKeyGroups"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-trustedkeygroups"""
    p_TrustedSigners: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "TrustedSigners"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-trustedsigners"""

@attr.s
class PropDistributionDefaultCacheBehavior(Property):
    """
    AWS Object Type = "AWS::CloudFront::Distribution.DefaultCacheBehavior"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html

    Property Document:
    
    - ``rp_TargetOriginId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-targetoriginid
    - ``rp_ViewerProtocolPolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-viewerprotocolpolicy
    - ``p_AllowedMethods``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-allowedmethods
    - ``p_CachePolicyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-cachepolicyid
    - ``p_CachedMethods``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-cachedmethods
    - ``p_Compress``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-compress
    - ``p_DefaultTTL``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-defaultttl
    - ``p_FieldLevelEncryptionId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-fieldlevelencryptionid
    - ``p_ForwardedValues``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-forwardedvalues
    - ``p_FunctionAssociations``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-functionassociations
    - ``p_LambdaFunctionAssociations``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-lambdafunctionassociations
    - ``p_MaxTTL``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-maxttl
    - ``p_MinTTL``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-minttl
    - ``p_OriginRequestPolicyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-originrequestpolicyid
    - ``p_RealtimeLogConfigArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-realtimelogconfigarn
    - ``p_ResponseHeadersPolicyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-responseheaderspolicyid
    - ``p_SmoothStreaming``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-smoothstreaming
    - ``p_TrustedKeyGroups``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-trustedkeygroups
    - ``p_TrustedSigners``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-trustedsigners
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::Distribution.DefaultCacheBehavior"
    
    rp_TargetOriginId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TargetOriginId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-targetoriginid"""
    rp_ViewerProtocolPolicy: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ViewerProtocolPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-viewerprotocolpolicy"""
    p_AllowedMethods: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AllowedMethods"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-allowedmethods"""
    p_CachePolicyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CachePolicyId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-cachepolicyid"""
    p_CachedMethods: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "CachedMethods"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-cachedmethods"""
    p_Compress: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Compress"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-compress"""
    p_DefaultTTL: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultTTL"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-defaultttl"""
    p_FieldLevelEncryptionId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "FieldLevelEncryptionId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-fieldlevelencryptionid"""
    p_ForwardedValues: typing.Union['PropDistributionForwardedValues', dict] = attr.ib(
        default=None,
        converter=PropDistributionForwardedValues.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDistributionForwardedValues)),
        metadata={AttrMeta.PROPERTY_NAME: "ForwardedValues"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-forwardedvalues"""
    p_FunctionAssociations: typing.List[typing.Union['PropDistributionFunctionAssociation', dict]] = attr.ib(
        default=None,
        converter=PropDistributionFunctionAssociation.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDistributionFunctionAssociation), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "FunctionAssociations"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-functionassociations"""
    p_LambdaFunctionAssociations: typing.List[typing.Union['PropDistributionLambdaFunctionAssociation', dict]] = attr.ib(
        default=None,
        converter=PropDistributionLambdaFunctionAssociation.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDistributionLambdaFunctionAssociation), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "LambdaFunctionAssociations"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-lambdafunctionassociations"""
    p_MaxTTL: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "MaxTTL"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-maxttl"""
    p_MinTTL: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "MinTTL"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-minttl"""
    p_OriginRequestPolicyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "OriginRequestPolicyId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-originrequestpolicyid"""
    p_RealtimeLogConfigArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RealtimeLogConfigArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-realtimelogconfigarn"""
    p_ResponseHeadersPolicyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ResponseHeadersPolicyId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-responseheaderspolicyid"""
    p_SmoothStreaming: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "SmoothStreaming"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-smoothstreaming"""
    p_TrustedKeyGroups: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "TrustedKeyGroups"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-trustedkeygroups"""
    p_TrustedSigners: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "TrustedSigners"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html#cfn-cloudfront-distribution-defaultcachebehavior-trustedsigners"""

@attr.s
class PropDistributionOrigin(Property):
    """
    AWS Object Type = "AWS::CloudFront::Distribution.Origin"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html

    Property Document:
    
    - ``rp_DomainName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-domainname
    - ``rp_Id``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-id
    - ``p_ConnectionAttempts``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-connectionattempts
    - ``p_ConnectionTimeout``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-connectiontimeout
    - ``p_CustomOriginConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-customoriginconfig
    - ``p_OriginCustomHeaders``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-origincustomheaders
    - ``p_OriginPath``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-originpath
    - ``p_OriginShield``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-originshield
    - ``p_S3OriginConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-s3originconfig
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::Distribution.Origin"
    
    rp_DomainName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DomainName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-domainname"""
    rp_Id: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Id"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-id"""
    p_ConnectionAttempts: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ConnectionAttempts"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-connectionattempts"""
    p_ConnectionTimeout: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ConnectionTimeout"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-connectiontimeout"""
    p_CustomOriginConfig: typing.Union['PropDistributionCustomOriginConfig', dict] = attr.ib(
        default=None,
        converter=PropDistributionCustomOriginConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDistributionCustomOriginConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomOriginConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-customoriginconfig"""
    p_OriginCustomHeaders: typing.List[typing.Union['PropDistributionOriginCustomHeader', dict]] = attr.ib(
        default=None,
        converter=PropDistributionOriginCustomHeader.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDistributionOriginCustomHeader), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "OriginCustomHeaders"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-origincustomheaders"""
    p_OriginPath: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "OriginPath"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-originpath"""
    p_OriginShield: typing.Union['PropDistributionOriginShield', dict] = attr.ib(
        default=None,
        converter=PropDistributionOriginShield.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDistributionOriginShield)),
        metadata={AttrMeta.PROPERTY_NAME: "OriginShield"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-originshield"""
    p_S3OriginConfig: typing.Union['PropDistributionS3OriginConfig', dict] = attr.ib(
        default=None,
        converter=PropDistributionS3OriginConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDistributionS3OriginConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "S3OriginConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-s3originconfig"""

@attr.s
class PropResponseHeadersPolicySecurityHeadersConfig(Property):
    """
    AWS Object Type = "AWS::CloudFront::ResponseHeadersPolicy.SecurityHeadersConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-securityheadersconfig.html

    Property Document:
    
    - ``p_ContentSecurityPolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-securityheadersconfig.html#cfn-cloudfront-responseheaderspolicy-securityheadersconfig-contentsecuritypolicy
    - ``p_ContentTypeOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-securityheadersconfig.html#cfn-cloudfront-responseheaderspolicy-securityheadersconfig-contenttypeoptions
    - ``p_FrameOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-securityheadersconfig.html#cfn-cloudfront-responseheaderspolicy-securityheadersconfig-frameoptions
    - ``p_ReferrerPolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-securityheadersconfig.html#cfn-cloudfront-responseheaderspolicy-securityheadersconfig-referrerpolicy
    - ``p_StrictTransportSecurity``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-securityheadersconfig.html#cfn-cloudfront-responseheaderspolicy-securityheadersconfig-stricttransportsecurity
    - ``p_XSSProtection``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-securityheadersconfig.html#cfn-cloudfront-responseheaderspolicy-securityheadersconfig-xssprotection
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::ResponseHeadersPolicy.SecurityHeadersConfig"
    
    p_ContentSecurityPolicy: typing.Union['PropResponseHeadersPolicyContentSecurityPolicy', dict] = attr.ib(
        default=None,
        converter=PropResponseHeadersPolicyContentSecurityPolicy.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResponseHeadersPolicyContentSecurityPolicy)),
        metadata={AttrMeta.PROPERTY_NAME: "ContentSecurityPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-securityheadersconfig.html#cfn-cloudfront-responseheaderspolicy-securityheadersconfig-contentsecuritypolicy"""
    p_ContentTypeOptions: typing.Union['PropResponseHeadersPolicyContentTypeOptions', dict] = attr.ib(
        default=None,
        converter=PropResponseHeadersPolicyContentTypeOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResponseHeadersPolicyContentTypeOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "ContentTypeOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-securityheadersconfig.html#cfn-cloudfront-responseheaderspolicy-securityheadersconfig-contenttypeoptions"""
    p_FrameOptions: typing.Union['PropResponseHeadersPolicyFrameOptions', dict] = attr.ib(
        default=None,
        converter=PropResponseHeadersPolicyFrameOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResponseHeadersPolicyFrameOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "FrameOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-securityheadersconfig.html#cfn-cloudfront-responseheaderspolicy-securityheadersconfig-frameoptions"""
    p_ReferrerPolicy: typing.Union['PropResponseHeadersPolicyReferrerPolicy', dict] = attr.ib(
        default=None,
        converter=PropResponseHeadersPolicyReferrerPolicy.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResponseHeadersPolicyReferrerPolicy)),
        metadata={AttrMeta.PROPERTY_NAME: "ReferrerPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-securityheadersconfig.html#cfn-cloudfront-responseheaderspolicy-securityheadersconfig-referrerpolicy"""
    p_StrictTransportSecurity: typing.Union['PropResponseHeadersPolicyStrictTransportSecurity', dict] = attr.ib(
        default=None,
        converter=PropResponseHeadersPolicyStrictTransportSecurity.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResponseHeadersPolicyStrictTransportSecurity)),
        metadata={AttrMeta.PROPERTY_NAME: "StrictTransportSecurity"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-securityheadersconfig.html#cfn-cloudfront-responseheaderspolicy-securityheadersconfig-stricttransportsecurity"""
    p_XSSProtection: typing.Union['PropResponseHeadersPolicyXSSProtection', dict] = attr.ib(
        default=None,
        converter=PropResponseHeadersPolicyXSSProtection.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResponseHeadersPolicyXSSProtection)),
        metadata={AttrMeta.PROPERTY_NAME: "XSSProtection"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-securityheadersconfig.html#cfn-cloudfront-responseheaderspolicy-securityheadersconfig-xssprotection"""

@attr.s
class PropResponseHeadersPolicyResponseHeadersPolicyConfig(Property):
    """
    AWS Object Type = "AWS::CloudFront::ResponseHeadersPolicy.ResponseHeadersPolicyConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-responseheaderspolicyconfig.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-responseheaderspolicyconfig.html#cfn-cloudfront-responseheaderspolicy-responseheaderspolicyconfig-name
    - ``p_Comment``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-responseheaderspolicyconfig.html#cfn-cloudfront-responseheaderspolicy-responseheaderspolicyconfig-comment
    - ``p_CorsConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-responseheaderspolicyconfig.html#cfn-cloudfront-responseheaderspolicy-responseheaderspolicyconfig-corsconfig
    - ``p_CustomHeadersConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-responseheaderspolicyconfig.html#cfn-cloudfront-responseheaderspolicy-responseheaderspolicyconfig-customheadersconfig
    - ``p_SecurityHeadersConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-responseheaderspolicyconfig.html#cfn-cloudfront-responseheaderspolicy-responseheaderspolicyconfig-securityheadersconfig
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::ResponseHeadersPolicy.ResponseHeadersPolicyConfig"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-responseheaderspolicyconfig.html#cfn-cloudfront-responseheaderspolicy-responseheaderspolicyconfig-name"""
    p_Comment: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Comment"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-responseheaderspolicyconfig.html#cfn-cloudfront-responseheaderspolicy-responseheaderspolicyconfig-comment"""
    p_CorsConfig: typing.Union['PropResponseHeadersPolicyCorsConfig', dict] = attr.ib(
        default=None,
        converter=PropResponseHeadersPolicyCorsConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResponseHeadersPolicyCorsConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "CorsConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-responseheaderspolicyconfig.html#cfn-cloudfront-responseheaderspolicy-responseheaderspolicyconfig-corsconfig"""
    p_CustomHeadersConfig: typing.Union['PropResponseHeadersPolicyCustomHeadersConfig', dict] = attr.ib(
        default=None,
        converter=PropResponseHeadersPolicyCustomHeadersConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResponseHeadersPolicyCustomHeadersConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomHeadersConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-responseheaderspolicyconfig.html#cfn-cloudfront-responseheaderspolicy-responseheaderspolicyconfig-customheadersconfig"""
    p_SecurityHeadersConfig: typing.Union['PropResponseHeadersPolicySecurityHeadersConfig', dict] = attr.ib(
        default=None,
        converter=PropResponseHeadersPolicySecurityHeadersConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResponseHeadersPolicySecurityHeadersConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "SecurityHeadersConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-responseheaderspolicyconfig.html#cfn-cloudfront-responseheaderspolicy-responseheaderspolicyconfig-securityheadersconfig"""

@attr.s
class PropCachePolicyCachePolicyConfig(Property):
    """
    AWS Object Type = "AWS::CloudFront::CachePolicy.CachePolicyConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cachepolicyconfig.html

    Property Document:
    
    - ``rp_DefaultTTL``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cachepolicyconfig.html#cfn-cloudfront-cachepolicy-cachepolicyconfig-defaultttl
    - ``rp_MaxTTL``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cachepolicyconfig.html#cfn-cloudfront-cachepolicy-cachepolicyconfig-maxttl
    - ``rp_MinTTL``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cachepolicyconfig.html#cfn-cloudfront-cachepolicy-cachepolicyconfig-minttl
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cachepolicyconfig.html#cfn-cloudfront-cachepolicy-cachepolicyconfig-name
    - ``rp_ParametersInCacheKeyAndForwardedToOrigin``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cachepolicyconfig.html#cfn-cloudfront-cachepolicy-cachepolicyconfig-parametersincachekeyandforwardedtoorigin
    - ``p_Comment``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cachepolicyconfig.html#cfn-cloudfront-cachepolicy-cachepolicyconfig-comment
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::CachePolicy.CachePolicyConfig"
    
    rp_DefaultTTL: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultTTL"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cachepolicyconfig.html#cfn-cloudfront-cachepolicy-cachepolicyconfig-defaultttl"""
    rp_MaxTTL: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "MaxTTL"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cachepolicyconfig.html#cfn-cloudfront-cachepolicy-cachepolicyconfig-maxttl"""
    rp_MinTTL: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "MinTTL"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cachepolicyconfig.html#cfn-cloudfront-cachepolicy-cachepolicyconfig-minttl"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cachepolicyconfig.html#cfn-cloudfront-cachepolicy-cachepolicyconfig-name"""
    rp_ParametersInCacheKeyAndForwardedToOrigin: typing.Union['PropCachePolicyParametersInCacheKeyAndForwardedToOrigin', dict] = attr.ib(
        default=None,
        converter=PropCachePolicyParametersInCacheKeyAndForwardedToOrigin.from_dict,
        validator=attr.validators.instance_of(PropCachePolicyParametersInCacheKeyAndForwardedToOrigin),
        metadata={AttrMeta.PROPERTY_NAME: "ParametersInCacheKeyAndForwardedToOrigin"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cachepolicyconfig.html#cfn-cloudfront-cachepolicy-cachepolicyconfig-parametersincachekeyandforwardedtoorigin"""
    p_Comment: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Comment"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cachepolicyconfig.html#cfn-cloudfront-cachepolicy-cachepolicyconfig-comment"""

@attr.s
class PropDistributionOriginGroup(Property):
    """
    AWS Object Type = "AWS::CloudFront::Distribution.OriginGroup"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroup.html

    Property Document:
    
    - ``rp_FailoverCriteria``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroup.html#cfn-cloudfront-distribution-origingroup-failovercriteria
    - ``rp_Id``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroup.html#cfn-cloudfront-distribution-origingroup-id
    - ``rp_Members``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroup.html#cfn-cloudfront-distribution-origingroup-members
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::Distribution.OriginGroup"
    
    rp_FailoverCriteria: typing.Union['PropDistributionOriginGroupFailoverCriteria', dict] = attr.ib(
        default=None,
        converter=PropDistributionOriginGroupFailoverCriteria.from_dict,
        validator=attr.validators.instance_of(PropDistributionOriginGroupFailoverCriteria),
        metadata={AttrMeta.PROPERTY_NAME: "FailoverCriteria"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroup.html#cfn-cloudfront-distribution-origingroup-failovercriteria"""
    rp_Id: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Id"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroup.html#cfn-cloudfront-distribution-origingroup-id"""
    rp_Members: typing.Union['PropDistributionOriginGroupMembers', dict] = attr.ib(
        default=None,
        converter=PropDistributionOriginGroupMembers.from_dict,
        validator=attr.validators.instance_of(PropDistributionOriginGroupMembers),
        metadata={AttrMeta.PROPERTY_NAME: "Members"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroup.html#cfn-cloudfront-distribution-origingroup-members"""

@attr.s
class PropDistributionOriginGroups(Property):
    """
    AWS Object Type = "AWS::CloudFront::Distribution.OriginGroups"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroups.html

    Property Document:
    
    - ``rp_Quantity``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroups.html#cfn-cloudfront-distribution-origingroups-quantity
    - ``p_Items``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroups.html#cfn-cloudfront-distribution-origingroups-items
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::Distribution.OriginGroups"
    
    rp_Quantity: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Quantity"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroups.html#cfn-cloudfront-distribution-origingroups-quantity"""
    p_Items: typing.List[typing.Union['PropDistributionOriginGroup', dict]] = attr.ib(
        default=None,
        converter=PropDistributionOriginGroup.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDistributionOriginGroup), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Items"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroups.html#cfn-cloudfront-distribution-origingroups-items"""

@attr.s
class PropDistributionDistributionConfig(Property):
    """
    AWS Object Type = "AWS::CloudFront::Distribution.DistributionConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html

    Property Document:
    
    - ``rp_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-enabled
    - ``p_Aliases``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-aliases
    - ``p_CNAMEs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-cnames
    - ``p_CacheBehaviors``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-cachebehaviors
    - ``p_Comment``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-comment
    - ``p_CustomErrorResponses``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-customerrorresponses
    - ``p_CustomOrigin``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-customorigin
    - ``p_DefaultCacheBehavior``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-defaultcachebehavior
    - ``p_DefaultRootObject``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-defaultrootobject
    - ``p_HttpVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-httpversion
    - ``p_IPV6Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-ipv6enabled
    - ``p_Logging``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-logging
    - ``p_OriginGroups``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-origingroups
    - ``p_Origins``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-origins
    - ``p_PriceClass``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-priceclass
    - ``p_Restrictions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-restrictions
    - ``p_S3Origin``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-s3origin
    - ``p_ViewerCertificate``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-viewercertificate
    - ``p_WebACLId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-webaclid
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::Distribution.DistributionConfig"
    
    rp_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-enabled"""
    p_Aliases: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Aliases"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-aliases"""
    p_CNAMEs: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "CNAMEs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-cnames"""
    p_CacheBehaviors: typing.List[typing.Union['PropDistributionCacheBehavior', dict]] = attr.ib(
        default=None,
        converter=PropDistributionCacheBehavior.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDistributionCacheBehavior), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "CacheBehaviors"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-cachebehaviors"""
    p_Comment: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Comment"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-comment"""
    p_CustomErrorResponses: typing.List[typing.Union['PropDistributionCustomErrorResponse', dict]] = attr.ib(
        default=None,
        converter=PropDistributionCustomErrorResponse.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDistributionCustomErrorResponse), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "CustomErrorResponses"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-customerrorresponses"""
    p_CustomOrigin: typing.Union['PropDistributionLegacyCustomOrigin', dict] = attr.ib(
        default=None,
        converter=PropDistributionLegacyCustomOrigin.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDistributionLegacyCustomOrigin)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomOrigin"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-customorigin"""
    p_DefaultCacheBehavior: typing.Union['PropDistributionDefaultCacheBehavior', dict] = attr.ib(
        default=None,
        converter=PropDistributionDefaultCacheBehavior.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDistributionDefaultCacheBehavior)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultCacheBehavior"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-defaultcachebehavior"""
    p_DefaultRootObject: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultRootObject"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-defaultrootobject"""
    p_HttpVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "HttpVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-httpversion"""
    p_IPV6Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IPV6Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-ipv6enabled"""
    p_Logging: typing.Union['PropDistributionLogging', dict] = attr.ib(
        default=None,
        converter=PropDistributionLogging.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDistributionLogging)),
        metadata={AttrMeta.PROPERTY_NAME: "Logging"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-logging"""
    p_OriginGroups: typing.Union['PropDistributionOriginGroups', dict] = attr.ib(
        default=None,
        converter=PropDistributionOriginGroups.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDistributionOriginGroups)),
        metadata={AttrMeta.PROPERTY_NAME: "OriginGroups"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-origingroups"""
    p_Origins: typing.List[typing.Union['PropDistributionOrigin', dict]] = attr.ib(
        default=None,
        converter=PropDistributionOrigin.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDistributionOrigin), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Origins"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-origins"""
    p_PriceClass: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PriceClass"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-priceclass"""
    p_Restrictions: typing.Union['PropDistributionRestrictions', dict] = attr.ib(
        default=None,
        converter=PropDistributionRestrictions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDistributionRestrictions)),
        metadata={AttrMeta.PROPERTY_NAME: "Restrictions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-restrictions"""
    p_S3Origin: typing.Union['PropDistributionLegacyS3Origin', dict] = attr.ib(
        default=None,
        converter=PropDistributionLegacyS3Origin.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDistributionLegacyS3Origin)),
        metadata={AttrMeta.PROPERTY_NAME: "S3Origin"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-s3origin"""
    p_ViewerCertificate: typing.Union['PropDistributionViewerCertificate', dict] = attr.ib(
        default=None,
        converter=PropDistributionViewerCertificate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDistributionViewerCertificate)),
        metadata={AttrMeta.PROPERTY_NAME: "ViewerCertificate"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-viewercertificate"""
    p_WebACLId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "WebACLId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-webaclid"""


#--- Resource declaration ---

@attr.s
class StreamingDistribution(Resource):
    """
    AWS Object Type = "AWS::CloudFront::StreamingDistribution"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-streamingdistribution.html

    Property Document:
    
    - ``rp_StreamingDistributionConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-streamingdistribution.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig
    - ``rp_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-streamingdistribution.html#cfn-cloudfront-streamingdistribution-tags
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::StreamingDistribution"

    
    rp_StreamingDistributionConfig: typing.Union['PropStreamingDistributionStreamingDistributionConfig', dict] = attr.ib(
        default=None,
        converter=PropStreamingDistributionStreamingDistributionConfig.from_dict,
        validator=attr.validators.instance_of(PropStreamingDistributionStreamingDistributionConfig),
        metadata={AttrMeta.PROPERTY_NAME: "StreamingDistributionConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-streamingdistribution.html#cfn-cloudfront-streamingdistribution-streamingdistributionconfig"""
    rp_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-streamingdistribution.html#cfn-cloudfront-streamingdistribution-tags"""

    
    @property
    def rv_DomainName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-streamingdistribution.html#aws-resource-cloudfront-streamingdistribution-return-values"""
        return GetAtt(resource=self, attr_name="DomainName")
    

@attr.s
class CachePolicy(Resource):
    """
    AWS Object Type = "AWS::CloudFront::CachePolicy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cachepolicy.html

    Property Document:
    
    - ``rp_CachePolicyConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cachepolicy.html#cfn-cloudfront-cachepolicy-cachepolicyconfig
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::CachePolicy"

    
    rp_CachePolicyConfig: typing.Union['PropCachePolicyCachePolicyConfig', dict] = attr.ib(
        default=None,
        converter=PropCachePolicyCachePolicyConfig.from_dict,
        validator=attr.validators.instance_of(PropCachePolicyCachePolicyConfig),
        metadata={AttrMeta.PROPERTY_NAME: "CachePolicyConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cachepolicy.html#cfn-cloudfront-cachepolicy-cachepolicyconfig"""

    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cachepolicy.html#aws-resource-cloudfront-cachepolicy-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_LastModifiedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cachepolicy.html#aws-resource-cloudfront-cachepolicy-return-values"""
        return GetAtt(resource=self, attr_name="LastModifiedTime")
    

@attr.s
class Distribution(Resource):
    """
    AWS Object Type = "AWS::CloudFront::Distribution"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.html

    Property Document:
    
    - ``rp_DistributionConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.html#cfn-cloudfront-distribution-distributionconfig
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.html#cfn-cloudfront-distribution-tags
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::Distribution"

    
    rp_DistributionConfig: typing.Union['PropDistributionDistributionConfig', dict] = attr.ib(
        default=None,
        converter=PropDistributionDistributionConfig.from_dict,
        validator=attr.validators.instance_of(PropDistributionDistributionConfig),
        metadata={AttrMeta.PROPERTY_NAME: "DistributionConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.html#cfn-cloudfront-distribution-distributionconfig"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.html#cfn-cloudfront-distribution-tags"""

    
    @property
    def rv_DomainName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.html#aws-resource-cloudfront-distribution-return-values"""
        return GetAtt(resource=self, attr_name="DomainName")
    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.html#aws-resource-cloudfront-distribution-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    

@attr.s
class Function(Resource):
    """
    AWS Object Type = "AWS::CloudFront::Function"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-function.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-function.html#cfn-cloudfront-function-name
    - ``p_AutoPublish``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-function.html#cfn-cloudfront-function-autopublish
    - ``p_FunctionCode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-function.html#cfn-cloudfront-function-functioncode
    - ``p_FunctionConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-function.html#cfn-cloudfront-function-functionconfig
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::Function"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-function.html#cfn-cloudfront-function-name"""
    p_AutoPublish: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "AutoPublish"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-function.html#cfn-cloudfront-function-autopublish"""
    p_FunctionCode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "FunctionCode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-function.html#cfn-cloudfront-function-functioncode"""
    p_FunctionConfig: typing.Union['PropFunctionFunctionConfig', dict] = attr.ib(
        default=None,
        converter=PropFunctionFunctionConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropFunctionFunctionConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "FunctionConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-function.html#cfn-cloudfront-function-functionconfig"""

    
    @property
    def rv_FunctionARN(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-function.html#aws-resource-cloudfront-function-return-values"""
        return GetAtt(resource=self, attr_name="FunctionARN")
    
    @property
    def rv_FunctionMetadataFunctionARN(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-function.html#aws-resource-cloudfront-function-return-values"""
        return GetAtt(resource=self, attr_name="FunctionMetadata.FunctionARN")
    
    @property
    def rv_Stage(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-function.html#aws-resource-cloudfront-function-return-values"""
        return GetAtt(resource=self, attr_name="Stage")
    

@attr.s
class KeyGroup(Resource):
    """
    AWS Object Type = "AWS::CloudFront::KeyGroup"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-keygroup.html

    Property Document:
    
    - ``rp_KeyGroupConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-keygroup.html#cfn-cloudfront-keygroup-keygroupconfig
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::KeyGroup"

    
    rp_KeyGroupConfig: typing.Union['PropKeyGroupKeyGroupConfig', dict] = attr.ib(
        default=None,
        converter=PropKeyGroupKeyGroupConfig.from_dict,
        validator=attr.validators.instance_of(PropKeyGroupKeyGroupConfig),
        metadata={AttrMeta.PROPERTY_NAME: "KeyGroupConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-keygroup.html#cfn-cloudfront-keygroup-keygroupconfig"""

    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-keygroup.html#aws-resource-cloudfront-keygroup-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_LastModifiedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-keygroup.html#aws-resource-cloudfront-keygroup-return-values"""
        return GetAtt(resource=self, attr_name="LastModifiedTime")
    

@attr.s
class CloudFrontOriginAccessIdentity(Resource):
    """
    AWS Object Type = "AWS::CloudFront::CloudFrontOriginAccessIdentity"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cloudfrontoriginaccessidentity.html

    Property Document:
    
    - ``rp_CloudFrontOriginAccessIdentityConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cloudfrontoriginaccessidentity.html#cfn-cloudfront-cloudfrontoriginaccessidentity-cloudfrontoriginaccessidentityconfig
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::CloudFrontOriginAccessIdentity"

    
    rp_CloudFrontOriginAccessIdentityConfig: typing.Union['PropCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfig', dict] = attr.ib(
        default=None,
        converter=PropCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfig.from_dict,
        validator=attr.validators.instance_of(PropCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfig),
        metadata={AttrMeta.PROPERTY_NAME: "CloudFrontOriginAccessIdentityConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cloudfrontoriginaccessidentity.html#cfn-cloudfront-cloudfrontoriginaccessidentity-cloudfrontoriginaccessidentityconfig"""

    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cloudfrontoriginaccessidentity.html#aws-resource-cloudfront-cloudfrontoriginaccessidentity-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_S3CanonicalUserId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cloudfrontoriginaccessidentity.html#aws-resource-cloudfront-cloudfrontoriginaccessidentity-return-values"""
        return GetAtt(resource=self, attr_name="S3CanonicalUserId")
    

@attr.s
class RealtimeLogConfig(Resource):
    """
    AWS Object Type = "AWS::CloudFront::RealtimeLogConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-realtimelogconfig.html

    Property Document:
    
    - ``rp_EndPoints``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-realtimelogconfig.html#cfn-cloudfront-realtimelogconfig-endpoints
    - ``rp_Fields``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-realtimelogconfig.html#cfn-cloudfront-realtimelogconfig-fields
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-realtimelogconfig.html#cfn-cloudfront-realtimelogconfig-name
    - ``rp_SamplingRate``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-realtimelogconfig.html#cfn-cloudfront-realtimelogconfig-samplingrate
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::RealtimeLogConfig"

    
    rp_EndPoints: typing.List[typing.Union['PropRealtimeLogConfigEndPoint', dict]] = attr.ib(
        default=None,
        converter=PropRealtimeLogConfigEndPoint.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropRealtimeLogConfigEndPoint), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "EndPoints"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-realtimelogconfig.html#cfn-cloudfront-realtimelogconfig-endpoints"""
    rp_Fields: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Fields"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-realtimelogconfig.html#cfn-cloudfront-realtimelogconfig-fields"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-realtimelogconfig.html#cfn-cloudfront-realtimelogconfig-name"""
    rp_SamplingRate: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "SamplingRate"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-realtimelogconfig.html#cfn-cloudfront-realtimelogconfig-samplingrate"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-realtimelogconfig.html#aws-resource-cloudfront-realtimelogconfig-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class ResponseHeadersPolicy(Resource):
    """
    AWS Object Type = "AWS::CloudFront::ResponseHeadersPolicy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-responseheaderspolicy.html

    Property Document:
    
    - ``rp_ResponseHeadersPolicyConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-responseheaderspolicy.html#cfn-cloudfront-responseheaderspolicy-responseheaderspolicyconfig
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::ResponseHeadersPolicy"

    
    rp_ResponseHeadersPolicyConfig: typing.Union['PropResponseHeadersPolicyResponseHeadersPolicyConfig', dict] = attr.ib(
        default=None,
        converter=PropResponseHeadersPolicyResponseHeadersPolicyConfig.from_dict,
        validator=attr.validators.instance_of(PropResponseHeadersPolicyResponseHeadersPolicyConfig),
        metadata={AttrMeta.PROPERTY_NAME: "ResponseHeadersPolicyConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-responseheaderspolicy.html#cfn-cloudfront-responseheaderspolicy-responseheaderspolicyconfig"""

    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-responseheaderspolicy.html#aws-resource-cloudfront-responseheaderspolicy-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_LastModifiedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-responseheaderspolicy.html#aws-resource-cloudfront-responseheaderspolicy-return-values"""
        return GetAtt(resource=self, attr_name="LastModifiedTime")
    

@attr.s
class OriginRequestPolicy(Resource):
    """
    AWS Object Type = "AWS::CloudFront::OriginRequestPolicy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-originrequestpolicy.html

    Property Document:
    
    - ``rp_OriginRequestPolicyConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-originrequestpolicy.html#cfn-cloudfront-originrequestpolicy-originrequestpolicyconfig
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::OriginRequestPolicy"

    
    rp_OriginRequestPolicyConfig: typing.Union['PropOriginRequestPolicyOriginRequestPolicyConfig', dict] = attr.ib(
        default=None,
        converter=PropOriginRequestPolicyOriginRequestPolicyConfig.from_dict,
        validator=attr.validators.instance_of(PropOriginRequestPolicyOriginRequestPolicyConfig),
        metadata={AttrMeta.PROPERTY_NAME: "OriginRequestPolicyConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-originrequestpolicy.html#cfn-cloudfront-originrequestpolicy-originrequestpolicyconfig"""

    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-originrequestpolicy.html#aws-resource-cloudfront-originrequestpolicy-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_LastModifiedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-originrequestpolicy.html#aws-resource-cloudfront-originrequestpolicy-return-values"""
        return GetAtt(resource=self, attr_name="LastModifiedTime")
    

@attr.s
class PublicKey(Resource):
    """
    AWS Object Type = "AWS::CloudFront::PublicKey"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-publickey.html

    Property Document:
    
    - ``rp_PublicKeyConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-publickey.html#cfn-cloudfront-publickey-publickeyconfig
    """
    AWS_OBJECT_TYPE = "AWS::CloudFront::PublicKey"

    
    rp_PublicKeyConfig: typing.Union['PropPublicKeyPublicKeyConfig', dict] = attr.ib(
        default=None,
        converter=PropPublicKeyPublicKeyConfig.from_dict,
        validator=attr.validators.instance_of(PropPublicKeyPublicKeyConfig),
        metadata={AttrMeta.PROPERTY_NAME: "PublicKeyConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-publickey.html#cfn-cloudfront-publickey-publickeyconfig"""

    
    @property
    def rv_CreatedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-publickey.html#aws-resource-cloudfront-publickey-return-values"""
        return GetAtt(resource=self, attr_name="CreatedTime")
    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-publickey.html#aws-resource-cloudfront-publickey-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
