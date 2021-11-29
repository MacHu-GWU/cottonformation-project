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
class PropApiGatewayManagedOverridesAccessLogSettings(Property):
    """
    AWS Object Type = "AWS::ApiGatewayV2::ApiGatewayManagedOverrides.AccessLogSettings"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings.html

    Property Document:
    
    - ``p_DestinationArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings.html#cfn-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings-destinationarn
    - ``p_Format``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings.html#cfn-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings-format
    """
    AWS_OBJECT_TYPE = "AWS::ApiGatewayV2::ApiGatewayManagedOverrides.AccessLogSettings"
    
    p_DestinationArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DestinationArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings.html#cfn-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings-destinationarn"""
    p_Format: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Format"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings.html#cfn-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings-format"""

@attr.s
class PropApiGatewayManagedOverridesRouteOverrides(Property):
    """
    AWS Object Type = "AWS::ApiGatewayV2::ApiGatewayManagedOverrides.RouteOverrides"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routeoverrides.html

    Property Document:
    
    - ``p_AuthorizationScopes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routeoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routeoverrides-authorizationscopes
    - ``p_AuthorizationType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routeoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routeoverrides-authorizationtype
    - ``p_AuthorizerId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routeoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routeoverrides-authorizerid
    - ``p_OperationName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routeoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routeoverrides-operationname
    - ``p_Target``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routeoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routeoverrides-target
    """
    AWS_OBJECT_TYPE = "AWS::ApiGatewayV2::ApiGatewayManagedOverrides.RouteOverrides"
    
    p_AuthorizationScopes: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AuthorizationScopes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routeoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routeoverrides-authorizationscopes"""
    p_AuthorizationType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AuthorizationType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routeoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routeoverrides-authorizationtype"""
    p_AuthorizerId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AuthorizerId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routeoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routeoverrides-authorizerid"""
    p_OperationName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "OperationName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routeoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routeoverrides-operationname"""
    p_Target: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Target"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routeoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routeoverrides-target"""

@attr.s
class PropRouteParameterConstraints(Property):
    """
    AWS Object Type = "AWS::ApiGatewayV2::Route.ParameterConstraints"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-route-parameterconstraints.html

    Property Document:
    
    - ``rp_Required``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-route-parameterconstraints.html#cfn-apigatewayv2-route-parameterconstraints-required
    """
    AWS_OBJECT_TYPE = "AWS::ApiGatewayV2::Route.ParameterConstraints"
    
    rp_Required: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Required"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-route-parameterconstraints.html#cfn-apigatewayv2-route-parameterconstraints-required"""

@attr.s
class PropIntegrationTlsConfig(Property):
    """
    AWS Object Type = "AWS::ApiGatewayV2::Integration.TlsConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-tlsconfig.html

    Property Document:
    
    - ``p_ServerNameToVerify``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-tlsconfig.html#cfn-apigatewayv2-integration-tlsconfig-servernametoverify
    """
    AWS_OBJECT_TYPE = "AWS::ApiGatewayV2::Integration.TlsConfig"
    
    p_ServerNameToVerify: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ServerNameToVerify"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-tlsconfig.html#cfn-apigatewayv2-integration-tlsconfig-servernametoverify"""

@attr.s
class PropStageAccessLogSettings(Property):
    """
    AWS Object Type = "AWS::ApiGatewayV2::Stage.AccessLogSettings"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-accesslogsettings.html

    Property Document:
    
    - ``p_DestinationArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-accesslogsettings.html#cfn-apigatewayv2-stage-accesslogsettings-destinationarn
    - ``p_Format``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-accesslogsettings.html#cfn-apigatewayv2-stage-accesslogsettings-format
    """
    AWS_OBJECT_TYPE = "AWS::ApiGatewayV2::Stage.AccessLogSettings"
    
    p_DestinationArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DestinationArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-accesslogsettings.html#cfn-apigatewayv2-stage-accesslogsettings-destinationarn"""
    p_Format: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Format"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-accesslogsettings.html#cfn-apigatewayv2-stage-accesslogsettings-format"""

@attr.s
class PropDomainNameMutualTlsAuthentication(Property):
    """
    AWS Object Type = "AWS::ApiGatewayV2::DomainName.MutualTlsAuthentication"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-mutualtlsauthentication.html

    Property Document:
    
    - ``p_TruststoreUri``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-mutualtlsauthentication.html#cfn-apigatewayv2-domainname-mutualtlsauthentication-truststoreuri
    - ``p_TruststoreVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-mutualtlsauthentication.html#cfn-apigatewayv2-domainname-mutualtlsauthentication-truststoreversion
    """
    AWS_OBJECT_TYPE = "AWS::ApiGatewayV2::DomainName.MutualTlsAuthentication"
    
    p_TruststoreUri: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TruststoreUri"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-mutualtlsauthentication.html#cfn-apigatewayv2-domainname-mutualtlsauthentication-truststoreuri"""
    p_TruststoreVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TruststoreVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-mutualtlsauthentication.html#cfn-apigatewayv2-domainname-mutualtlsauthentication-truststoreversion"""

@attr.s
class PropApiGatewayManagedOverridesRouteSettings(Property):
    """
    AWS Object Type = "AWS::ApiGatewayV2::ApiGatewayManagedOverrides.RouteSettings"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings.html

    Property Document:
    
    - ``p_DataTraceEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routesettings-datatraceenabled
    - ``p_DetailedMetricsEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routesettings-detailedmetricsenabled
    - ``p_LoggingLevel``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routesettings-logginglevel
    - ``p_ThrottlingBurstLimit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routesettings-throttlingburstlimit
    - ``p_ThrottlingRateLimit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routesettings-throttlingratelimit
    """
    AWS_OBJECT_TYPE = "AWS::ApiGatewayV2::ApiGatewayManagedOverrides.RouteSettings"
    
    p_DataTraceEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "DataTraceEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routesettings-datatraceenabled"""
    p_DetailedMetricsEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "DetailedMetricsEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routesettings-detailedmetricsenabled"""
    p_LoggingLevel: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LoggingLevel"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routesettings-logginglevel"""
    p_ThrottlingBurstLimit: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ThrottlingBurstLimit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routesettings-throttlingburstlimit"""
    p_ThrottlingRateLimit: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "ThrottlingRateLimit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routesettings-throttlingratelimit"""

@attr.s
class PropIntegrationResponseParameter(Property):
    """
    AWS Object Type = "AWS::ApiGatewayV2::Integration.ResponseParameter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-responseparameter.html

    Property Document:
    
    - ``rp_Destination``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-responseparameter.html#cfn-apigatewayv2-integration-responseparameter-destination
    - ``rp_Source``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-responseparameter.html#cfn-apigatewayv2-integration-responseparameter-source
    """
    AWS_OBJECT_TYPE = "AWS::ApiGatewayV2::Integration.ResponseParameter"
    
    rp_Destination: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Destination"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-responseparameter.html#cfn-apigatewayv2-integration-responseparameter-destination"""
    rp_Source: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Source"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-responseparameter.html#cfn-apigatewayv2-integration-responseparameter-source"""

@attr.s
class PropApiGatewayManagedOverridesIntegrationOverrides(Property):
    """
    AWS Object Type = "AWS::ApiGatewayV2::ApiGatewayManagedOverrides.IntegrationOverrides"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides.html

    Property Document:
    
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides-description
    - ``p_IntegrationMethod``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides-integrationmethod
    - ``p_PayloadFormatVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides-payloadformatversion
    - ``p_TimeoutInMillis``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides-timeoutinmillis
    """
    AWS_OBJECT_TYPE = "AWS::ApiGatewayV2::ApiGatewayManagedOverrides.IntegrationOverrides"
    
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides-description"""
    p_IntegrationMethod: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "IntegrationMethod"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides-integrationmethod"""
    p_PayloadFormatVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PayloadFormatVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides-payloadformatversion"""
    p_TimeoutInMillis: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "TimeoutInMillis"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides-timeoutinmillis"""

@attr.s
class PropAuthorizerJWTConfiguration(Property):
    """
    AWS Object Type = "AWS::ApiGatewayV2::Authorizer.JWTConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-authorizer-jwtconfiguration.html

    Property Document:
    
    - ``p_Audience``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-authorizer-jwtconfiguration.html#cfn-apigatewayv2-authorizer-jwtconfiguration-audience
    - ``p_Issuer``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-authorizer-jwtconfiguration.html#cfn-apigatewayv2-authorizer-jwtconfiguration-issuer
    """
    AWS_OBJECT_TYPE = "AWS::ApiGatewayV2::Authorizer.JWTConfiguration"
    
    p_Audience: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Audience"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-authorizer-jwtconfiguration.html#cfn-apigatewayv2-authorizer-jwtconfiguration-audience"""
    p_Issuer: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Issuer"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-authorizer-jwtconfiguration.html#cfn-apigatewayv2-authorizer-jwtconfiguration-issuer"""

@attr.s
class PropDomainNameDomainNameConfiguration(Property):
    """
    AWS Object Type = "AWS::ApiGatewayV2::DomainName.DomainNameConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html

    Property Document:
    
    - ``p_CertificateArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html#cfn-apigatewayv2-domainname-domainnameconfiguration-certificatearn
    - ``p_CertificateName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html#cfn-apigatewayv2-domainname-domainnameconfiguration-certificatename
    - ``p_EndpointType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html#cfn-apigatewayv2-domainname-domainnameconfiguration-endpointtype
    - ``p_OwnershipVerificationCertificateArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html#cfn-apigatewayv2-domainname-domainnameconfiguration-ownershipverificationcertificatearn
    - ``p_SecurityPolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html#cfn-apigatewayv2-domainname-domainnameconfiguration-securitypolicy
    """
    AWS_OBJECT_TYPE = "AWS::ApiGatewayV2::DomainName.DomainNameConfiguration"
    
    p_CertificateArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CertificateArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html#cfn-apigatewayv2-domainname-domainnameconfiguration-certificatearn"""
    p_CertificateName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CertificateName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html#cfn-apigatewayv2-domainname-domainnameconfiguration-certificatename"""
    p_EndpointType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "EndpointType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html#cfn-apigatewayv2-domainname-domainnameconfiguration-endpointtype"""
    p_OwnershipVerificationCertificateArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "OwnershipVerificationCertificateArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html#cfn-apigatewayv2-domainname-domainnameconfiguration-ownershipverificationcertificatearn"""
    p_SecurityPolicy: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SecurityPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html#cfn-apigatewayv2-domainname-domainnameconfiguration-securitypolicy"""

@attr.s
class PropRouteResponseParameterConstraints(Property):
    """
    AWS Object Type = "AWS::ApiGatewayV2::RouteResponse.ParameterConstraints"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-routeresponse-parameterconstraints.html

    Property Document:
    
    - ``rp_Required``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-routeresponse-parameterconstraints.html#cfn-apigatewayv2-routeresponse-parameterconstraints-required
    """
    AWS_OBJECT_TYPE = "AWS::ApiGatewayV2::RouteResponse.ParameterConstraints"
    
    rp_Required: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Required"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-routeresponse-parameterconstraints.html#cfn-apigatewayv2-routeresponse-parameterconstraints-required"""

@attr.s
class PropApiCors(Property):
    """
    AWS Object Type = "AWS::ApiGatewayV2::Api.Cors"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html

    Property Document:
    
    - ``p_AllowCredentials``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html#cfn-apigatewayv2-api-cors-allowcredentials
    - ``p_AllowHeaders``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html#cfn-apigatewayv2-api-cors-allowheaders
    - ``p_AllowMethods``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html#cfn-apigatewayv2-api-cors-allowmethods
    - ``p_AllowOrigins``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html#cfn-apigatewayv2-api-cors-alloworigins
    - ``p_ExposeHeaders``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html#cfn-apigatewayv2-api-cors-exposeheaders
    - ``p_MaxAge``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html#cfn-apigatewayv2-api-cors-maxage
    """
    AWS_OBJECT_TYPE = "AWS::ApiGatewayV2::Api.Cors"
    
    p_AllowCredentials: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "AllowCredentials"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html#cfn-apigatewayv2-api-cors-allowcredentials"""
    p_AllowHeaders: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AllowHeaders"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html#cfn-apigatewayv2-api-cors-allowheaders"""
    p_AllowMethods: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AllowMethods"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html#cfn-apigatewayv2-api-cors-allowmethods"""
    p_AllowOrigins: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AllowOrigins"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html#cfn-apigatewayv2-api-cors-alloworigins"""
    p_ExposeHeaders: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ExposeHeaders"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html#cfn-apigatewayv2-api-cors-exposeheaders"""
    p_MaxAge: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MaxAge"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html#cfn-apigatewayv2-api-cors-maxage"""

@attr.s
class PropApiBodyS3Location(Property):
    """
    AWS Object Type = "AWS::ApiGatewayV2::Api.BodyS3Location"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html

    Property Document:
    
    - ``p_Bucket``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html#cfn-apigatewayv2-api-bodys3location-bucket
    - ``p_Etag``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html#cfn-apigatewayv2-api-bodys3location-etag
    - ``p_Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html#cfn-apigatewayv2-api-bodys3location-key
    - ``p_Version``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html#cfn-apigatewayv2-api-bodys3location-version
    """
    AWS_OBJECT_TYPE = "AWS::ApiGatewayV2::Api.BodyS3Location"
    
    p_Bucket: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Bucket"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html#cfn-apigatewayv2-api-bodys3location-bucket"""
    p_Etag: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Etag"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html#cfn-apigatewayv2-api-bodys3location-etag"""
    p_Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html#cfn-apigatewayv2-api-bodys3location-key"""
    p_Version: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Version"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html#cfn-apigatewayv2-api-bodys3location-version"""

@attr.s
class PropStageRouteSettings(Property):
    """
    AWS Object Type = "AWS::ApiGatewayV2::Stage.RouteSettings"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html

    Property Document:
    
    - ``p_DataTraceEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html#cfn-apigatewayv2-stage-routesettings-datatraceenabled
    - ``p_DetailedMetricsEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html#cfn-apigatewayv2-stage-routesettings-detailedmetricsenabled
    - ``p_LoggingLevel``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html#cfn-apigatewayv2-stage-routesettings-logginglevel
    - ``p_ThrottlingBurstLimit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html#cfn-apigatewayv2-stage-routesettings-throttlingburstlimit
    - ``p_ThrottlingRateLimit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html#cfn-apigatewayv2-stage-routesettings-throttlingratelimit
    """
    AWS_OBJECT_TYPE = "AWS::ApiGatewayV2::Stage.RouteSettings"
    
    p_DataTraceEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "DataTraceEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html#cfn-apigatewayv2-stage-routesettings-datatraceenabled"""
    p_DetailedMetricsEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "DetailedMetricsEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html#cfn-apigatewayv2-stage-routesettings-detailedmetricsenabled"""
    p_LoggingLevel: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LoggingLevel"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html#cfn-apigatewayv2-stage-routesettings-logginglevel"""
    p_ThrottlingBurstLimit: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ThrottlingBurstLimit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html#cfn-apigatewayv2-stage-routesettings-throttlingburstlimit"""
    p_ThrottlingRateLimit: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "ThrottlingRateLimit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html#cfn-apigatewayv2-stage-routesettings-throttlingratelimit"""

@attr.s
class PropIntegrationResponseParameterList(Property):
    """
    AWS Object Type = "AWS::ApiGatewayV2::Integration.ResponseParameterList"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-responseparameterlist.html

    Property Document:
    
    - ``p_ResponseParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-responseparameterlist.html#cfn-apigatewayv2-integration-responseparameterlist-responseparameters
    """
    AWS_OBJECT_TYPE = "AWS::ApiGatewayV2::Integration.ResponseParameterList"
    
    p_ResponseParameters: typing.List[typing.Union['PropIntegrationResponseParameter', dict]] = attr.ib(
        default=None,
        converter=PropIntegrationResponseParameter.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropIntegrationResponseParameter), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ResponseParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-responseparameterlist.html#cfn-apigatewayv2-integration-responseparameterlist-responseparameters"""

@attr.s
class PropApiGatewayManagedOverridesStageOverrides(Property):
    """
    AWS Object Type = "AWS::ApiGatewayV2::ApiGatewayManagedOverrides.StageOverrides"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-stageoverrides.html

    Property Document:
    
    - ``p_AccessLogSettings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-stageoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-stageoverrides-accesslogsettings
    - ``p_AutoDeploy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-stageoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-stageoverrides-autodeploy
    - ``p_DefaultRouteSettings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-stageoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-stageoverrides-defaultroutesettings
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-stageoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-stageoverrides-description
    - ``p_RouteSettings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-stageoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-stageoverrides-routesettings
    - ``p_StageVariables``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-stageoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-stageoverrides-stagevariables
    """
    AWS_OBJECT_TYPE = "AWS::ApiGatewayV2::ApiGatewayManagedOverrides.StageOverrides"
    
    p_AccessLogSettings: typing.Union['PropApiGatewayManagedOverridesAccessLogSettings', dict] = attr.ib(
        default=None,
        converter=PropApiGatewayManagedOverridesAccessLogSettings.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApiGatewayManagedOverridesAccessLogSettings)),
        metadata={AttrMeta.PROPERTY_NAME: "AccessLogSettings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-stageoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-stageoverrides-accesslogsettings"""
    p_AutoDeploy: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "AutoDeploy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-stageoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-stageoverrides-autodeploy"""
    p_DefaultRouteSettings: typing.Union['PropApiGatewayManagedOverridesRouteSettings', dict] = attr.ib(
        default=None,
        converter=PropApiGatewayManagedOverridesRouteSettings.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApiGatewayManagedOverridesRouteSettings)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultRouteSettings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-stageoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-stageoverrides-defaultroutesettings"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-stageoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-stageoverrides-description"""
    p_RouteSettings: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "RouteSettings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-stageoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-stageoverrides-routesettings"""
    p_StageVariables: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "StageVariables"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-stageoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-stageoverrides-stagevariables"""


#--- Resource declaration ---

@attr.s
class Api(Resource):
    """
    AWS Object Type = "AWS::ApiGatewayV2::Api"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html

    Property Document:
    
    - ``p_ApiKeySelectionExpression``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-apikeyselectionexpression
    - ``p_BasePath``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-basepath
    - ``p_Body``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-body
    - ``p_BodyS3Location``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-bodys3location
    - ``p_CorsConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-corsconfiguration
    - ``p_CredentialsArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-credentialsarn
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-description
    - ``p_DisableExecuteApiEndpoint``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-disableexecuteapiendpoint
    - ``p_DisableSchemaValidation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-disableschemavalidation
    - ``p_FailOnWarnings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-failonwarnings
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-name
    - ``p_ProtocolType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-protocoltype
    - ``p_RouteKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-routekey
    - ``p_RouteSelectionExpression``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-routeselectionexpression
    - ``p_Target``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-target
    - ``p_Version``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-version
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-tags
    """
    AWS_OBJECT_TYPE = "AWS::ApiGatewayV2::Api"

    
    p_ApiKeySelectionExpression: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ApiKeySelectionExpression"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-apikeyselectionexpression"""
    p_BasePath: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BasePath"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-basepath"""
    p_Body: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Body"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-body"""
    p_BodyS3Location: typing.Union['PropApiBodyS3Location', dict] = attr.ib(
        default=None,
        converter=PropApiBodyS3Location.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApiBodyS3Location)),
        metadata={AttrMeta.PROPERTY_NAME: "BodyS3Location"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-bodys3location"""
    p_CorsConfiguration: typing.Union['PropApiCors', dict] = attr.ib(
        default=None,
        converter=PropApiCors.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApiCors)),
        metadata={AttrMeta.PROPERTY_NAME: "CorsConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-corsconfiguration"""
    p_CredentialsArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CredentialsArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-credentialsarn"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-description"""
    p_DisableExecuteApiEndpoint: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "DisableExecuteApiEndpoint"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-disableexecuteapiendpoint"""
    p_DisableSchemaValidation: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "DisableSchemaValidation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-disableschemavalidation"""
    p_FailOnWarnings: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "FailOnWarnings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-failonwarnings"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-name"""
    p_ProtocolType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ProtocolType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-protocoltype"""
    p_RouteKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RouteKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-routekey"""
    p_RouteSelectionExpression: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RouteSelectionExpression"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-routeselectionexpression"""
    p_Target: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Target"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-target"""
    p_Version: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Version"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-version"""
    p_Tags: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-tags"""

    
    @property
    def rv_ApiEndpoint(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#aws-resource-apigatewayv2-api-return-values"""
        return GetAtt(resource=self, attr_name="ApiEndpoint")
    

@attr.s
class RouteResponse(Resource):
    """
    AWS Object Type = "AWS::ApiGatewayV2::RouteResponse"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html

    Property Document:
    
    - ``rp_ApiId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-apiid
    - ``rp_RouteId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-routeid
    - ``rp_RouteResponseKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-routeresponsekey
    - ``p_ModelSelectionExpression``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-modelselectionexpression
    - ``p_ResponseModels``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-responsemodels
    - ``p_ResponseParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-responseparameters
    """
    AWS_OBJECT_TYPE = "AWS::ApiGatewayV2::RouteResponse"

    
    rp_ApiId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApiId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-apiid"""
    rp_RouteId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RouteId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-routeid"""
    rp_RouteResponseKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RouteResponseKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-routeresponsekey"""
    p_ModelSelectionExpression: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ModelSelectionExpression"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-modelselectionexpression"""
    p_ResponseModels: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "ResponseModels"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-responsemodels"""
    p_ResponseParameters: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "ResponseParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-responseparameters"""

    

@attr.s
class DomainName(Resource):
    """
    AWS Object Type = "AWS::ApiGatewayV2::DomainName"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html

    Property Document:
    
    - ``rp_DomainName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html#cfn-apigatewayv2-domainname-domainname
    - ``p_DomainNameConfigurations``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html#cfn-apigatewayv2-domainname-domainnameconfigurations
    - ``p_MutualTlsAuthentication``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html#cfn-apigatewayv2-domainname-mutualtlsauthentication
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html#cfn-apigatewayv2-domainname-tags
    """
    AWS_OBJECT_TYPE = "AWS::ApiGatewayV2::DomainName"

    
    rp_DomainName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DomainName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html#cfn-apigatewayv2-domainname-domainname"""
    p_DomainNameConfigurations: typing.List[typing.Union['PropDomainNameDomainNameConfiguration', dict]] = attr.ib(
        default=None,
        converter=PropDomainNameDomainNameConfiguration.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDomainNameDomainNameConfiguration), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "DomainNameConfigurations"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html#cfn-apigatewayv2-domainname-domainnameconfigurations"""
    p_MutualTlsAuthentication: typing.Union['PropDomainNameMutualTlsAuthentication', dict] = attr.ib(
        default=None,
        converter=PropDomainNameMutualTlsAuthentication.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDomainNameMutualTlsAuthentication)),
        metadata={AttrMeta.PROPERTY_NAME: "MutualTlsAuthentication"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html#cfn-apigatewayv2-domainname-mutualtlsauthentication"""
    p_Tags: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html#cfn-apigatewayv2-domainname-tags"""

    
    @property
    def rv_RegionalHostedZoneId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html#aws-resource-apigatewayv2-domainname-return-values"""
        return GetAtt(resource=self, attr_name="RegionalHostedZoneId")
    
    @property
    def rv_RegionalDomainName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html#aws-resource-apigatewayv2-domainname-return-values"""
        return GetAtt(resource=self, attr_name="RegionalDomainName")
    

@attr.s
class Integration(Resource):
    """
    AWS Object Type = "AWS::ApiGatewayV2::Integration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html

    Property Document:
    
    - ``rp_ApiId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-apiid
    - ``rp_IntegrationType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-integrationtype
    - ``p_ConnectionId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-connectionid
    - ``p_ConnectionType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-connectiontype
    - ``p_ContentHandlingStrategy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-contenthandlingstrategy
    - ``p_CredentialsArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-credentialsarn
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-description
    - ``p_IntegrationMethod``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-integrationmethod
    - ``p_IntegrationSubtype``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-integrationsubtype
    - ``p_IntegrationUri``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-integrationuri
    - ``p_PassthroughBehavior``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-passthroughbehavior
    - ``p_PayloadFormatVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-payloadformatversion
    - ``p_RequestParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-requestparameters
    - ``p_RequestTemplates``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-requesttemplates
    - ``p_ResponseParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-responseparameters
    - ``p_TemplateSelectionExpression``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-templateselectionexpression
    - ``p_TimeoutInMillis``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-timeoutinmillis
    - ``p_TlsConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-tlsconfig
    """
    AWS_OBJECT_TYPE = "AWS::ApiGatewayV2::Integration"

    
    rp_ApiId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApiId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-apiid"""
    rp_IntegrationType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "IntegrationType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-integrationtype"""
    p_ConnectionId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ConnectionId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-connectionid"""
    p_ConnectionType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ConnectionType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-connectiontype"""
    p_ContentHandlingStrategy: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ContentHandlingStrategy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-contenthandlingstrategy"""
    p_CredentialsArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CredentialsArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-credentialsarn"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-description"""
    p_IntegrationMethod: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "IntegrationMethod"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-integrationmethod"""
    p_IntegrationSubtype: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "IntegrationSubtype"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-integrationsubtype"""
    p_IntegrationUri: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "IntegrationUri"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-integrationuri"""
    p_PassthroughBehavior: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PassthroughBehavior"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-passthroughbehavior"""
    p_PayloadFormatVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PayloadFormatVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-payloadformatversion"""
    p_RequestParameters: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "RequestParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-requestparameters"""
    p_RequestTemplates: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "RequestTemplates"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-requesttemplates"""
    p_ResponseParameters: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "ResponseParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-responseparameters"""
    p_TemplateSelectionExpression: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TemplateSelectionExpression"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-templateselectionexpression"""
    p_TimeoutInMillis: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "TimeoutInMillis"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-timeoutinmillis"""
    p_TlsConfig: typing.Union['PropIntegrationTlsConfig', dict] = attr.ib(
        default=None,
        converter=PropIntegrationTlsConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropIntegrationTlsConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "TlsConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-tlsconfig"""

    

@attr.s
class Deployment(Resource):
    """
    AWS Object Type = "AWS::ApiGatewayV2::Deployment"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-deployment.html

    Property Document:
    
    - ``rp_ApiId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-deployment.html#cfn-apigatewayv2-deployment-apiid
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-deployment.html#cfn-apigatewayv2-deployment-description
    - ``p_StageName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-deployment.html#cfn-apigatewayv2-deployment-stagename
    """
    AWS_OBJECT_TYPE = "AWS::ApiGatewayV2::Deployment"

    
    rp_ApiId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApiId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-deployment.html#cfn-apigatewayv2-deployment-apiid"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-deployment.html#cfn-apigatewayv2-deployment-description"""
    p_StageName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "StageName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-deployment.html#cfn-apigatewayv2-deployment-stagename"""

    

@attr.s
class Model(Resource):
    """
    AWS Object Type = "AWS::ApiGatewayV2::Model"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html

    Property Document:
    
    - ``rp_ApiId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html#cfn-apigatewayv2-model-apiid
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html#cfn-apigatewayv2-model-name
    - ``rp_Schema``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html#cfn-apigatewayv2-model-schema
    - ``p_ContentType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html#cfn-apigatewayv2-model-contenttype
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html#cfn-apigatewayv2-model-description
    """
    AWS_OBJECT_TYPE = "AWS::ApiGatewayV2::Model"

    
    rp_ApiId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApiId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html#cfn-apigatewayv2-model-apiid"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html#cfn-apigatewayv2-model-name"""
    rp_Schema: dict = attr.ib(
        default=None,
        validator=attr.validators.instance_of(dict),
        metadata={AttrMeta.PROPERTY_NAME: "Schema"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html#cfn-apigatewayv2-model-schema"""
    p_ContentType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ContentType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html#cfn-apigatewayv2-model-contenttype"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html#cfn-apigatewayv2-model-description"""

    

@attr.s
class IntegrationResponse(Resource):
    """
    AWS Object Type = "AWS::ApiGatewayV2::IntegrationResponse"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html

    Property Document:
    
    - ``rp_ApiId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-apiid
    - ``rp_IntegrationId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-integrationid
    - ``rp_IntegrationResponseKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-integrationresponsekey
    - ``p_ContentHandlingStrategy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-contenthandlingstrategy
    - ``p_ResponseParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-responseparameters
    - ``p_ResponseTemplates``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-responsetemplates
    - ``p_TemplateSelectionExpression``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-templateselectionexpression
    """
    AWS_OBJECT_TYPE = "AWS::ApiGatewayV2::IntegrationResponse"

    
    rp_ApiId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApiId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-apiid"""
    rp_IntegrationId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "IntegrationId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-integrationid"""
    rp_IntegrationResponseKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "IntegrationResponseKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-integrationresponsekey"""
    p_ContentHandlingStrategy: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ContentHandlingStrategy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-contenthandlingstrategy"""
    p_ResponseParameters: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "ResponseParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-responseparameters"""
    p_ResponseTemplates: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "ResponseTemplates"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-responsetemplates"""
    p_TemplateSelectionExpression: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TemplateSelectionExpression"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-templateselectionexpression"""

    

@attr.s
class Route(Resource):
    """
    AWS Object Type = "AWS::ApiGatewayV2::Route"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html

    Property Document:
    
    - ``rp_ApiId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-apiid
    - ``rp_RouteKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-routekey
    - ``p_ApiKeyRequired``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-apikeyrequired
    - ``p_AuthorizationScopes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-authorizationscopes
    - ``p_AuthorizationType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-authorizationtype
    - ``p_AuthorizerId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-authorizerid
    - ``p_ModelSelectionExpression``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-modelselectionexpression
    - ``p_OperationName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-operationname
    - ``p_RequestModels``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-requestmodels
    - ``p_RequestParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-requestparameters
    - ``p_RouteResponseSelectionExpression``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-routeresponseselectionexpression
    - ``p_Target``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-target
    """
    AWS_OBJECT_TYPE = "AWS::ApiGatewayV2::Route"

    
    rp_ApiId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApiId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-apiid"""
    rp_RouteKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RouteKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-routekey"""
    p_ApiKeyRequired: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "ApiKeyRequired"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-apikeyrequired"""
    p_AuthorizationScopes: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AuthorizationScopes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-authorizationscopes"""
    p_AuthorizationType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AuthorizationType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-authorizationtype"""
    p_AuthorizerId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AuthorizerId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-authorizerid"""
    p_ModelSelectionExpression: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ModelSelectionExpression"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-modelselectionexpression"""
    p_OperationName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "OperationName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-operationname"""
    p_RequestModels: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "RequestModels"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-requestmodels"""
    p_RequestParameters: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "RequestParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-requestparameters"""
    p_RouteResponseSelectionExpression: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RouteResponseSelectionExpression"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-routeresponseselectionexpression"""
    p_Target: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Target"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-target"""

    

@attr.s
class ApiGatewayManagedOverrides(Resource):
    """
    AWS Object Type = "AWS::ApiGatewayV2::ApiGatewayManagedOverrides"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apigatewaymanagedoverrides.html

    Property Document:
    
    - ``rp_ApiId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apigatewaymanagedoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-apiid
    - ``p_Integration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apigatewaymanagedoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-integration
    - ``p_Route``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apigatewaymanagedoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-route
    - ``p_Stage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apigatewaymanagedoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-stage
    """
    AWS_OBJECT_TYPE = "AWS::ApiGatewayV2::ApiGatewayManagedOverrides"

    
    rp_ApiId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApiId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apigatewaymanagedoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-apiid"""
    p_Integration: typing.Union['PropApiGatewayManagedOverridesIntegrationOverrides', dict] = attr.ib(
        default=None,
        converter=PropApiGatewayManagedOverridesIntegrationOverrides.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApiGatewayManagedOverridesIntegrationOverrides)),
        metadata={AttrMeta.PROPERTY_NAME: "Integration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apigatewaymanagedoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-integration"""
    p_Route: typing.Union['PropApiGatewayManagedOverridesRouteOverrides', dict] = attr.ib(
        default=None,
        converter=PropApiGatewayManagedOverridesRouteOverrides.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApiGatewayManagedOverridesRouteOverrides)),
        metadata={AttrMeta.PROPERTY_NAME: "Route"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apigatewaymanagedoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-route"""
    p_Stage: typing.Union['PropApiGatewayManagedOverridesStageOverrides', dict] = attr.ib(
        default=None,
        converter=PropApiGatewayManagedOverridesStageOverrides.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApiGatewayManagedOverridesStageOverrides)),
        metadata={AttrMeta.PROPERTY_NAME: "Stage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apigatewaymanagedoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-stage"""

    

@attr.s
class Stage(Resource):
    """
    AWS Object Type = "AWS::ApiGatewayV2::Stage"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html

    Property Document:
    
    - ``rp_ApiId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-apiid
    - ``rp_StageName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-stagename
    - ``p_AccessLogSettings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-accesslogsettings
    - ``p_AccessPolicyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-accesspolicyid
    - ``p_AutoDeploy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-autodeploy
    - ``p_ClientCertificateId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-clientcertificateid
    - ``p_DefaultRouteSettings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-defaultroutesettings
    - ``p_DeploymentId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-deploymentid
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-description
    - ``p_RouteSettings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-routesettings
    - ``p_StageVariables``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-stagevariables
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-tags
    """
    AWS_OBJECT_TYPE = "AWS::ApiGatewayV2::Stage"

    
    rp_ApiId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApiId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-apiid"""
    rp_StageName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "StageName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-stagename"""
    p_AccessLogSettings: typing.Union['PropStageAccessLogSettings', dict] = attr.ib(
        default=None,
        converter=PropStageAccessLogSettings.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropStageAccessLogSettings)),
        metadata={AttrMeta.PROPERTY_NAME: "AccessLogSettings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-accesslogsettings"""
    p_AccessPolicyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AccessPolicyId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-accesspolicyid"""
    p_AutoDeploy: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "AutoDeploy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-autodeploy"""
    p_ClientCertificateId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ClientCertificateId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-clientcertificateid"""
    p_DefaultRouteSettings: typing.Union['PropStageRouteSettings', dict] = attr.ib(
        default=None,
        converter=PropStageRouteSettings.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropStageRouteSettings)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultRouteSettings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-defaultroutesettings"""
    p_DeploymentId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DeploymentId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-deploymentid"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-description"""
    p_RouteSettings: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "RouteSettings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-routesettings"""
    p_StageVariables: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "StageVariables"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-stagevariables"""
    p_Tags: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-tags"""

    

@attr.s
class VpcLink(Resource):
    """
    AWS Object Type = "AWS::ApiGatewayV2::VpcLink"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-vpclink.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-vpclink.html#cfn-apigatewayv2-vpclink-name
    - ``rp_SubnetIds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-vpclink.html#cfn-apigatewayv2-vpclink-subnetids
    - ``p_SecurityGroupIds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-vpclink.html#cfn-apigatewayv2-vpclink-securitygroupids
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-vpclink.html#cfn-apigatewayv2-vpclink-tags
    """
    AWS_OBJECT_TYPE = "AWS::ApiGatewayV2::VpcLink"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-vpclink.html#cfn-apigatewayv2-vpclink-name"""
    rp_SubnetIds: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "SubnetIds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-vpclink.html#cfn-apigatewayv2-vpclink-subnetids"""
    p_SecurityGroupIds: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SecurityGroupIds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-vpclink.html#cfn-apigatewayv2-vpclink-securitygroupids"""
    p_Tags: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-vpclink.html#cfn-apigatewayv2-vpclink-tags"""

    

@attr.s
class Authorizer(Resource):
    """
    AWS Object Type = "AWS::ApiGatewayV2::Authorizer"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html

    Property Document:
    
    - ``rp_ApiId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-apiid
    - ``rp_AuthorizerType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-authorizertype
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-name
    - ``p_AuthorizerCredentialsArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-authorizercredentialsarn
    - ``p_AuthorizerPayloadFormatVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-authorizerpayloadformatversion
    - ``p_AuthorizerResultTtlInSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-authorizerresultttlinseconds
    - ``p_AuthorizerUri``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-authorizeruri
    - ``p_EnableSimpleResponses``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-enablesimpleresponses
    - ``p_IdentitySource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-identitysource
    - ``p_IdentityValidationExpression``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-identityvalidationexpression
    - ``p_JwtConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-jwtconfiguration
    """
    AWS_OBJECT_TYPE = "AWS::ApiGatewayV2::Authorizer"

    
    rp_ApiId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApiId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-apiid"""
    rp_AuthorizerType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AuthorizerType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-authorizertype"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-name"""
    p_AuthorizerCredentialsArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AuthorizerCredentialsArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-authorizercredentialsarn"""
    p_AuthorizerPayloadFormatVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AuthorizerPayloadFormatVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-authorizerpayloadformatversion"""
    p_AuthorizerResultTtlInSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "AuthorizerResultTtlInSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-authorizerresultttlinseconds"""
    p_AuthorizerUri: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AuthorizerUri"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-authorizeruri"""
    p_EnableSimpleResponses: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EnableSimpleResponses"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-enablesimpleresponses"""
    p_IdentitySource: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "IdentitySource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-identitysource"""
    p_IdentityValidationExpression: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "IdentityValidationExpression"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-identityvalidationexpression"""
    p_JwtConfiguration: typing.Union['PropAuthorizerJWTConfiguration', dict] = attr.ib(
        default=None,
        converter=PropAuthorizerJWTConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropAuthorizerJWTConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "JwtConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-jwtconfiguration"""

    

@attr.s
class ApiMapping(Resource):
    """
    AWS Object Type = "AWS::ApiGatewayV2::ApiMapping"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html

    Property Document:
    
    - ``rp_ApiId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html#cfn-apigatewayv2-apimapping-apiid
    - ``rp_DomainName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html#cfn-apigatewayv2-apimapping-domainname
    - ``rp_Stage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html#cfn-apigatewayv2-apimapping-stage
    - ``p_ApiMappingKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html#cfn-apigatewayv2-apimapping-apimappingkey
    """
    AWS_OBJECT_TYPE = "AWS::ApiGatewayV2::ApiMapping"

    
    rp_ApiId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApiId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html#cfn-apigatewayv2-apimapping-apiid"""
    rp_DomainName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DomainName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html#cfn-apigatewayv2-apimapping-domainname"""
    rp_Stage: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Stage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html#cfn-apigatewayv2-apimapping-stage"""
    p_ApiMappingKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ApiMappingKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html#cfn-apigatewayv2-apimapping-apimappingkey"""

    
