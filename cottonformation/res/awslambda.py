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
class PropFunctionVpcConfig(Property):
    """
    AWS Object Type = "AWS::Lambda::Function.VpcConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-vpcconfig.html

    Property Document:
    
    - ``p_SecurityGroupIds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-vpcconfig.html#cfn-lambda-function-vpcconfig-securitygroupids
    - ``p_SubnetIds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-vpcconfig.html#cfn-lambda-function-vpcconfig-subnetids
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::Function.VpcConfig"
    
    p_SecurityGroupIds: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SecurityGroupIds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-vpcconfig.html#cfn-lambda-function-vpcconfig-securitygroupids"""
    p_SubnetIds: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SubnetIds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-vpcconfig.html#cfn-lambda-function-vpcconfig-subnetids"""

@attr.s
class PropFunctionFileSystemConfig(Property):
    """
    AWS Object Type = "AWS::Lambda::Function.FileSystemConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-filesystemconfig.html

    Property Document:
    
    - ``rp_Arn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-filesystemconfig.html#cfn-lambda-function-filesystemconfig-arn
    - ``rp_LocalMountPath``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-filesystemconfig.html#cfn-lambda-function-filesystemconfig-localmountpath
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::Function.FileSystemConfig"
    
    rp_Arn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Arn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-filesystemconfig.html#cfn-lambda-function-filesystemconfig-arn"""
    rp_LocalMountPath: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "LocalMountPath"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-filesystemconfig.html#cfn-lambda-function-filesystemconfig-localmountpath"""

@attr.s
class PropEventInvokeConfigOnFailure(Property):
    """
    AWS Object Type = "AWS::Lambda::EventInvokeConfig.OnFailure"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig-onfailure.html

    Property Document:
    
    - ``rp_Destination``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig-onfailure.html#cfn-lambda-eventinvokeconfig-destinationconfig-onfailure-destination
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::EventInvokeConfig.OnFailure"
    
    rp_Destination: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Destination"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig-onfailure.html#cfn-lambda-eventinvokeconfig-destinationconfig-onfailure-destination"""

@attr.s
class PropEventInvokeConfigOnSuccess(Property):
    """
    AWS Object Type = "AWS::Lambda::EventInvokeConfig.OnSuccess"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig-onsuccess.html

    Property Document:
    
    - ``rp_Destination``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig-onsuccess.html#cfn-lambda-eventinvokeconfig-destinationconfig-onsuccess-destination
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::EventInvokeConfig.OnSuccess"
    
    rp_Destination: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Destination"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig-onsuccess.html#cfn-lambda-eventinvokeconfig-destinationconfig-onsuccess-destination"""

@attr.s
class PropEventSourceMappingFilter(Property):
    """
    AWS Object Type = "AWS::Lambda::EventSourceMapping.Filter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filter.html

    Property Document:
    
    - ``p_Pattern``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filter.html#cfn-lambda-eventsourcemapping-filter-pattern
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::EventSourceMapping.Filter"
    
    p_Pattern: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Pattern"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filter.html#cfn-lambda-eventsourcemapping-filter-pattern"""

@attr.s
class PropEventInvokeConfigDestinationConfig(Property):
    """
    AWS Object Type = "AWS::Lambda::EventInvokeConfig.DestinationConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig.html

    Property Document:
    
    - ``p_OnFailure``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig.html#cfn-lambda-eventinvokeconfig-destinationconfig-onfailure
    - ``p_OnSuccess``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig.html#cfn-lambda-eventinvokeconfig-destinationconfig-onsuccess
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::EventInvokeConfig.DestinationConfig"
    
    p_OnFailure: typing.Union['PropEventInvokeConfigOnFailure', dict] = attr.ib(
        default=None,
        converter=PropEventInvokeConfigOnFailure.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropEventInvokeConfigOnFailure)),
        metadata={AttrMeta.PROPERTY_NAME: "OnFailure"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig.html#cfn-lambda-eventinvokeconfig-destinationconfig-onfailure"""
    p_OnSuccess: typing.Union['PropEventInvokeConfigOnSuccess', dict] = attr.ib(
        default=None,
        converter=PropEventInvokeConfigOnSuccess.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropEventInvokeConfigOnSuccess)),
        metadata={AttrMeta.PROPERTY_NAME: "OnSuccess"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig.html#cfn-lambda-eventinvokeconfig-destinationconfig-onsuccess"""

@attr.s
class PropCodeSigningConfigCodeSigningPolicies(Property):
    """
    AWS Object Type = "AWS::Lambda::CodeSigningConfig.CodeSigningPolicies"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-codesigningconfig-codesigningpolicies.html

    Property Document:
    
    - ``rp_UntrustedArtifactOnDeployment``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-codesigningconfig-codesigningpolicies.html#cfn-lambda-codesigningconfig-codesigningpolicies-untrustedartifactondeployment
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::CodeSigningConfig.CodeSigningPolicies"
    
    rp_UntrustedArtifactOnDeployment: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "UntrustedArtifactOnDeployment"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-codesigningconfig-codesigningpolicies.html#cfn-lambda-codesigningconfig-codesigningpolicies-untrustedartifactondeployment"""

@attr.s
class PropAliasVersionWeight(Property):
    """
    AWS Object Type = "AWS::Lambda::Alias.VersionWeight"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-alias-versionweight.html

    Property Document:
    
    - ``rp_FunctionVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-alias-versionweight.html#cfn-lambda-alias-versionweight-functionversion
    - ``rp_FunctionWeight``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-alias-versionweight.html#cfn-lambda-alias-versionweight-functionweight
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::Alias.VersionWeight"
    
    rp_FunctionVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "FunctionVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-alias-versionweight.html#cfn-lambda-alias-versionweight-functionversion"""
    rp_FunctionWeight: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "FunctionWeight"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-alias-versionweight.html#cfn-lambda-alias-versionweight-functionweight"""

@attr.s
class PropVersionProvisionedConcurrencyConfiguration(Property):
    """
    AWS Object Type = "AWS::Lambda::Version.ProvisionedConcurrencyConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-version-provisionedconcurrencyconfiguration.html

    Property Document:
    
    - ``rp_ProvisionedConcurrentExecutions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-version-provisionedconcurrencyconfiguration.html#cfn-lambda-version-provisionedconcurrencyconfiguration-provisionedconcurrentexecutions
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::Version.ProvisionedConcurrencyConfiguration"
    
    rp_ProvisionedConcurrentExecutions: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "ProvisionedConcurrentExecutions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-version-provisionedconcurrencyconfiguration.html#cfn-lambda-version-provisionedconcurrencyconfiguration-provisionedconcurrentexecutions"""

@attr.s
class PropFunctionImageConfig(Property):
    """
    AWS Object Type = "AWS::Lambda::Function.ImageConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-imageconfig.html

    Property Document:
    
    - ``p_Command``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-imageconfig.html#cfn-lambda-function-imageconfig-command
    - ``p_EntryPoint``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-imageconfig.html#cfn-lambda-function-imageconfig-entrypoint
    - ``p_WorkingDirectory``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-imageconfig.html#cfn-lambda-function-imageconfig-workingdirectory
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::Function.ImageConfig"
    
    p_Command: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Command"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-imageconfig.html#cfn-lambda-function-imageconfig-command"""
    p_EntryPoint: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "EntryPoint"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-imageconfig.html#cfn-lambda-function-imageconfig-entrypoint"""
    p_WorkingDirectory: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "WorkingDirectory"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-imageconfig.html#cfn-lambda-function-imageconfig-workingdirectory"""

@attr.s
class PropEventSourceMappingOnFailure(Property):
    """
    AWS Object Type = "AWS::Lambda::EventSourceMapping.OnFailure"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-onfailure.html

    Property Document:
    
    - ``p_Destination``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-onfailure.html#cfn-lambda-eventsourcemapping-onfailure-destination
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::EventSourceMapping.OnFailure"
    
    p_Destination: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Destination"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-onfailure.html#cfn-lambda-eventsourcemapping-onfailure-destination"""

@attr.s
class PropEventSourceMappingSourceAccessConfiguration(Property):
    """
    AWS Object Type = "AWS::Lambda::EventSourceMapping.SourceAccessConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-sourceaccessconfiguration.html

    Property Document:
    
    - ``p_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-sourceaccessconfiguration.html#cfn-lambda-eventsourcemapping-sourceaccessconfiguration-type
    - ``p_URI``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-sourceaccessconfiguration.html#cfn-lambda-eventsourcemapping-sourceaccessconfiguration-uri
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::EventSourceMapping.SourceAccessConfiguration"
    
    p_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-sourceaccessconfiguration.html#cfn-lambda-eventsourcemapping-sourceaccessconfiguration-type"""
    p_URI: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "URI"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-sourceaccessconfiguration.html#cfn-lambda-eventsourcemapping-sourceaccessconfiguration-uri"""

@attr.s
class PropEventSourceMappingEndpoints(Property):
    """
    AWS Object Type = "AWS::Lambda::EventSourceMapping.Endpoints"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-endpoints.html

    Property Document:
    
    - ``p_KafkaBootstrapServers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-endpoints.html#cfn-lambda-eventsourcemapping-endpoints-kafkabootstrapservers
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::EventSourceMapping.Endpoints"
    
    p_KafkaBootstrapServers: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "KafkaBootstrapServers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-endpoints.html#cfn-lambda-eventsourcemapping-endpoints-kafkabootstrapservers"""

@attr.s
class PropUrlCors(Property):
    """
    AWS Object Type = "AWS::Lambda::Url.Cors"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-url-cors.html

    Property Document:
    
    - ``p_AllowCredentials``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-url-cors.html#cfn-lambda-url-cors-allowcredentials
    - ``p_AllowHeaders``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-url-cors.html#cfn-lambda-url-cors-allowheaders
    - ``p_AllowMethods``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-url-cors.html#cfn-lambda-url-cors-allowmethods
    - ``p_AllowOrigins``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-url-cors.html#cfn-lambda-url-cors-alloworigins
    - ``p_ExposeHeaders``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-url-cors.html#cfn-lambda-url-cors-exposeheaders
    - ``p_MaxAge``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-url-cors.html#cfn-lambda-url-cors-maxage
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::Url.Cors"
    
    p_AllowCredentials: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "AllowCredentials"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-url-cors.html#cfn-lambda-url-cors-allowcredentials"""
    p_AllowHeaders: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AllowHeaders"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-url-cors.html#cfn-lambda-url-cors-allowheaders"""
    p_AllowMethods: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AllowMethods"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-url-cors.html#cfn-lambda-url-cors-allowmethods"""
    p_AllowOrigins: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AllowOrigins"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-url-cors.html#cfn-lambda-url-cors-alloworigins"""
    p_ExposeHeaders: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ExposeHeaders"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-url-cors.html#cfn-lambda-url-cors-exposeheaders"""
    p_MaxAge: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MaxAge"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-url-cors.html#cfn-lambda-url-cors-maxage"""

@attr.s
class PropEventSourceMappingDestinationConfig(Property):
    """
    AWS Object Type = "AWS::Lambda::EventSourceMapping.DestinationConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-destinationconfig.html

    Property Document:
    
    - ``p_OnFailure``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-destinationconfig.html#cfn-lambda-eventsourcemapping-destinationconfig-onfailure
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::EventSourceMapping.DestinationConfig"
    
    p_OnFailure: typing.Union['PropEventSourceMappingOnFailure', dict] = attr.ib(
        default=None,
        converter=PropEventSourceMappingOnFailure.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropEventSourceMappingOnFailure)),
        metadata={AttrMeta.PROPERTY_NAME: "OnFailure"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-destinationconfig.html#cfn-lambda-eventsourcemapping-destinationconfig-onfailure"""

@attr.s
class PropAliasProvisionedConcurrencyConfiguration(Property):
    """
    AWS Object Type = "AWS::Lambda::Alias.ProvisionedConcurrencyConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-alias-provisionedconcurrencyconfiguration.html

    Property Document:
    
    - ``rp_ProvisionedConcurrentExecutions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-alias-provisionedconcurrencyconfiguration.html#cfn-lambda-alias-provisionedconcurrencyconfiguration-provisionedconcurrentexecutions
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::Alias.ProvisionedConcurrencyConfiguration"
    
    rp_ProvisionedConcurrentExecutions: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "ProvisionedConcurrentExecutions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-alias-provisionedconcurrencyconfiguration.html#cfn-lambda-alias-provisionedconcurrencyconfiguration-provisionedconcurrentexecutions"""

@attr.s
class PropFunctionDeadLetterConfig(Property):
    """
    AWS Object Type = "AWS::Lambda::Function.DeadLetterConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-deadletterconfig.html

    Property Document:
    
    - ``p_TargetArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-deadletterconfig.html#cfn-lambda-function-deadletterconfig-targetarn
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::Function.DeadLetterConfig"
    
    p_TargetArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TargetArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-deadletterconfig.html#cfn-lambda-function-deadletterconfig-targetarn"""

@attr.s
class PropFunctionCode(Property):
    """
    AWS Object Type = "AWS::Lambda::Function.Code"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html

    Property Document:
    
    - ``p_ImageUri``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-imageuri
    - ``p_S3Bucket``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-s3bucket
    - ``p_S3Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-s3key
    - ``p_S3ObjectVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-s3objectversion
    - ``p_ZipFile``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-zipfile
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::Function.Code"
    
    p_ImageUri: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ImageUri"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-imageuri"""
    p_S3Bucket: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "S3Bucket"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-s3bucket"""
    p_S3Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "S3Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-s3key"""
    p_S3ObjectVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "S3ObjectVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-s3objectversion"""
    p_ZipFile: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ZipFile"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-zipfile"""

@attr.s
class PropAliasAliasRoutingConfiguration(Property):
    """
    AWS Object Type = "AWS::Lambda::Alias.AliasRoutingConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-alias-aliasroutingconfiguration.html

    Property Document:
    
    - ``rp_AdditionalVersionWeights``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-alias-aliasroutingconfiguration.html#cfn-lambda-alias-aliasroutingconfiguration-additionalversionweights
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::Alias.AliasRoutingConfiguration"
    
    rp_AdditionalVersionWeights: typing.List[typing.Union['PropAliasVersionWeight', dict]] = attr.ib(
        default=None,
        converter=PropAliasVersionWeight.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropAliasVersionWeight), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "AdditionalVersionWeights"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-alias-aliasroutingconfiguration.html#cfn-lambda-alias-aliasroutingconfiguration-additionalversionweights"""

@attr.s
class PropEventSourceMappingSelfManagedKafkaEventSourceConfig(Property):
    """
    AWS Object Type = "AWS::Lambda::EventSourceMapping.SelfManagedKafkaEventSourceConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig.html

    Property Document:
    
    - ``p_ConsumerGroupId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig.html#cfn-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig-consumergroupid
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::EventSourceMapping.SelfManagedKafkaEventSourceConfig"
    
    p_ConsumerGroupId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ConsumerGroupId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig.html#cfn-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig-consumergroupid"""

@attr.s
class PropEventSourceMappingAmazonManagedKafkaEventSourceConfig(Property):
    """
    AWS Object Type = "AWS::Lambda::EventSourceMapping.AmazonManagedKafkaEventSourceConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig.html

    Property Document:
    
    - ``p_ConsumerGroupId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig.html#cfn-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig-consumergroupid
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::EventSourceMapping.AmazonManagedKafkaEventSourceConfig"
    
    p_ConsumerGroupId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ConsumerGroupId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig.html#cfn-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig-consumergroupid"""

@attr.s
class PropFunctionEphemeralStorage(Property):
    """
    AWS Object Type = "AWS::Lambda::Function.EphemeralStorage"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-ephemeralstorage.html

    Property Document:
    
    - ``rp_Size``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-ephemeralstorage.html#cfn-lambda-function-ephemeralstorage-size
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::Function.EphemeralStorage"
    
    rp_Size: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Size"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-ephemeralstorage.html#cfn-lambda-function-ephemeralstorage-size"""

@attr.s
class PropLayerVersionContent(Property):
    """
    AWS Object Type = "AWS::Lambda::LayerVersion.Content"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-layerversion-content.html

    Property Document:
    
    - ``rp_S3Bucket``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-layerversion-content.html#cfn-lambda-layerversion-content-s3bucket
    - ``rp_S3Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-layerversion-content.html#cfn-lambda-layerversion-content-s3key
    - ``p_S3ObjectVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-layerversion-content.html#cfn-lambda-layerversion-content-s3objectversion
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::LayerVersion.Content"
    
    rp_S3Bucket: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "S3Bucket"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-layerversion-content.html#cfn-lambda-layerversion-content-s3bucket"""
    rp_S3Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "S3Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-layerversion-content.html#cfn-lambda-layerversion-content-s3key"""
    p_S3ObjectVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "S3ObjectVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-layerversion-content.html#cfn-lambda-layerversion-content-s3objectversion"""

@attr.s
class PropFunctionTracingConfig(Property):
    """
    AWS Object Type = "AWS::Lambda::Function.TracingConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-tracingconfig.html

    Property Document:
    
    - ``p_Mode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-tracingconfig.html#cfn-lambda-function-tracingconfig-mode
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::Function.TracingConfig"
    
    p_Mode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Mode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-tracingconfig.html#cfn-lambda-function-tracingconfig-mode"""

@attr.s
class PropFunctionEnvironment(Property):
    """
    AWS Object Type = "AWS::Lambda::Function.Environment"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-environment.html

    Property Document:
    
    - ``p_Variables``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-environment.html#cfn-lambda-function-environment-variables
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::Function.Environment"
    
    p_Variables: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type))),
        metadata={AttrMeta.PROPERTY_NAME: "Variables"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-environment.html#cfn-lambda-function-environment-variables"""

@attr.s
class PropEventSourceMappingFilterCriteria(Property):
    """
    AWS Object Type = "AWS::Lambda::EventSourceMapping.FilterCriteria"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filtercriteria.html

    Property Document:
    
    - ``p_Filters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filtercriteria.html#cfn-lambda-eventsourcemapping-filtercriteria-filters
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::EventSourceMapping.FilterCriteria"
    
    p_Filters: typing.List[typing.Union['PropEventSourceMappingFilter', dict]] = attr.ib(
        default=None,
        converter=PropEventSourceMappingFilter.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropEventSourceMappingFilter), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Filters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filtercriteria.html#cfn-lambda-eventsourcemapping-filtercriteria-filters"""

@attr.s
class PropFunctionSnapStart(Property):
    """
    AWS Object Type = "AWS::Lambda::Function.SnapStart"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-snapstart.html

    Property Document:
    
    - ``rp_ApplyOn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-snapstart.html#cfn-lambda-function-snapstart-applyon
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::Function.SnapStart"
    
    rp_ApplyOn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApplyOn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-snapstart.html#cfn-lambda-function-snapstart-applyon"""

@attr.s
class PropCodeSigningConfigAllowedPublishers(Property):
    """
    AWS Object Type = "AWS::Lambda::CodeSigningConfig.AllowedPublishers"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-codesigningconfig-allowedpublishers.html

    Property Document:
    
    - ``rp_SigningProfileVersionArns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-codesigningconfig-allowedpublishers.html#cfn-lambda-codesigningconfig-allowedpublishers-signingprofileversionarns
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::CodeSigningConfig.AllowedPublishers"
    
    rp_SigningProfileVersionArns: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "SigningProfileVersionArns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-codesigningconfig-allowedpublishers.html#cfn-lambda-codesigningconfig-allowedpublishers-signingprofileversionarns"""

@attr.s
class PropEventSourceMappingSelfManagedEventSource(Property):
    """
    AWS Object Type = "AWS::Lambda::EventSourceMapping.SelfManagedEventSource"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-selfmanagedeventsource.html

    Property Document:
    
    - ``p_Endpoints``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-selfmanagedeventsource.html#cfn-lambda-eventsourcemapping-selfmanagedeventsource-endpoints
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::EventSourceMapping.SelfManagedEventSource"
    
    p_Endpoints: typing.Union['PropEventSourceMappingEndpoints', dict] = attr.ib(
        default=None,
        converter=PropEventSourceMappingEndpoints.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropEventSourceMappingEndpoints)),
        metadata={AttrMeta.PROPERTY_NAME: "Endpoints"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-selfmanagedeventsource.html#cfn-lambda-eventsourcemapping-selfmanagedeventsource-endpoints"""


#--- Resource declaration ---

@attr.s
class LayerVersion(Resource):
    """
    AWS Object Type = "AWS::Lambda::LayerVersion"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html

    Property Document:
    
    - ``rp_Content``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-content
    - ``p_CompatibleArchitectures``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-compatiblearchitectures
    - ``p_CompatibleRuntimes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-compatibleruntimes
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-description
    - ``p_LayerName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-layername
    - ``p_LicenseInfo``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-licenseinfo
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::LayerVersion"

    
    rp_Content: typing.Union['PropLayerVersionContent', dict] = attr.ib(
        default=None,
        converter=PropLayerVersionContent.from_dict,
        validator=attr.validators.instance_of(PropLayerVersionContent),
        metadata={
            AttrMeta.PROPERTY_NAME: "Content",
            AttrMeta.DATA: {
                "Type": 'Content',
                "Required": True,
                "UpdateType": 'Immutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-content"""
    p_CompatibleArchitectures: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={
            AttrMeta.PROPERTY_NAME: "CompatibleArchitectures",
            AttrMeta.DATA: {
                "PrimitiveItemType": 'String',
                "Type": 'List',
                "Required": False,
                "UpdateType": 'Immutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-compatiblearchitectures"""
    p_CompatibleRuntimes: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={
            AttrMeta.PROPERTY_NAME: "CompatibleRuntimes",
            AttrMeta.DATA: {
                "PrimitiveItemType": 'String',
                "Type": 'List',
                "Required": False,
                "UpdateType": 'Immutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-compatibleruntimes"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "Description",
            AttrMeta.DATA: {
                "Required": False,
                "PrimitiveType": 'String',
                "UpdateType": 'Immutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-description"""
    p_LayerName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "LayerName",
            AttrMeta.DATA: {
                "Required": False,
                "PrimitiveType": 'String',
                "UpdateType": 'Immutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-layername"""
    p_LicenseInfo: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "LicenseInfo",
            AttrMeta.DATA: {
                "Required": False,
                "PrimitiveType": 'String',
                "UpdateType": 'Immutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-licenseinfo"""

    

@attr.s
class Alias(Resource):
    """
    AWS Object Type = "AWS::Lambda::Alias"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html

    Property Document:
    
    - ``rp_FunctionName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-functionname
    - ``rp_FunctionVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-functionversion
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-name
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-description
    - ``p_ProvisionedConcurrencyConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-provisionedconcurrencyconfig
    - ``p_RoutingConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-routingconfig
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::Alias"

    
    rp_FunctionName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={
            AttrMeta.PROPERTY_NAME: "FunctionName",
            AttrMeta.DATA: {
                "PrimitiveType": 'String',
                "Required": True,
                "UpdateType": 'Immutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-functionname"""
    rp_FunctionVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={
            AttrMeta.PROPERTY_NAME: "FunctionVersion",
            AttrMeta.DATA: {
                "PrimitiveType": 'String',
                "Required": True,
                "UpdateType": 'Mutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-functionversion"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={
            AttrMeta.PROPERTY_NAME: "Name",
            AttrMeta.DATA: {
                "PrimitiveType": 'String',
                "Required": True,
                "UpdateType": 'Immutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-name"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "Description",
            AttrMeta.DATA: {
                "PrimitiveType": 'String',
                "Required": False,
                "UpdateType": 'Mutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-description"""
    p_ProvisionedConcurrencyConfig: typing.Union['PropAliasProvisionedConcurrencyConfiguration', dict] = attr.ib(
        default=None,
        converter=PropAliasProvisionedConcurrencyConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropAliasProvisionedConcurrencyConfiguration)),
        metadata={
            AttrMeta.PROPERTY_NAME: "ProvisionedConcurrencyConfig",
            AttrMeta.DATA: {
                "Required": False,
                "Type": 'ProvisionedConcurrencyConfiguration',
                "UpdateType": 'Mutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-provisionedconcurrencyconfig"""
    p_RoutingConfig: typing.Union['PropAliasAliasRoutingConfiguration', dict] = attr.ib(
        default=None,
        converter=PropAliasAliasRoutingConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropAliasAliasRoutingConfiguration)),
        metadata={
            AttrMeta.PROPERTY_NAME: "RoutingConfig",
            AttrMeta.DATA: {
                "Required": False,
                "Type": 'AliasRoutingConfiguration',
                "UpdateType": 'Mutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-routingconfig"""

    

@attr.s
class LayerVersionPermission(Resource):
    """
    AWS Object Type = "AWS::Lambda::LayerVersionPermission"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.html

    Property Document:
    
    - ``rp_Action``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.html#cfn-lambda-layerversionpermission-action
    - ``rp_LayerVersionArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.html#cfn-lambda-layerversionpermission-layerversionarn
    - ``rp_Principal``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.html#cfn-lambda-layerversionpermission-principal
    - ``p_OrganizationId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.html#cfn-lambda-layerversionpermission-organizationid
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::LayerVersionPermission"

    
    rp_Action: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={
            AttrMeta.PROPERTY_NAME: "Action",
            AttrMeta.DATA: {
                "Required": True,
                "PrimitiveType": 'String',
                "UpdateType": 'Immutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.html#cfn-lambda-layerversionpermission-action"""
    rp_LayerVersionArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={
            AttrMeta.PROPERTY_NAME: "LayerVersionArn",
            AttrMeta.DATA: {
                "Required": True,
                "PrimitiveType": 'String',
                "UpdateType": 'Immutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.html#cfn-lambda-layerversionpermission-layerversionarn"""
    rp_Principal: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={
            AttrMeta.PROPERTY_NAME: "Principal",
            AttrMeta.DATA: {
                "Required": True,
                "PrimitiveType": 'String',
                "UpdateType": 'Immutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.html#cfn-lambda-layerversionpermission-principal"""
    p_OrganizationId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "OrganizationId",
            AttrMeta.DATA: {
                "Required": False,
                "PrimitiveType": 'String',
                "UpdateType": 'Immutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.html#cfn-lambda-layerversionpermission-organizationid"""

    

@attr.s
class Url(Resource):
    """
    AWS Object Type = "AWS::Lambda::Url"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-url.html

    Property Document:
    
    - ``rp_AuthType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-url.html#cfn-lambda-url-authtype
    - ``rp_TargetFunctionArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-url.html#cfn-lambda-url-targetfunctionarn
    - ``p_Cors``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-url.html#cfn-lambda-url-cors
    - ``p_InvokeMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-url.html#cfn-lambda-url-invokemode
    - ``p_Qualifier``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-url.html#cfn-lambda-url-qualifier
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::Url"

    
    rp_AuthType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={
            AttrMeta.PROPERTY_NAME: "AuthType",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": True,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-url.html#cfn-lambda-url-authtype"""
    rp_TargetFunctionArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={
            AttrMeta.PROPERTY_NAME: "TargetFunctionArn",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": True,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-url.html#cfn-lambda-url-targetfunctionarn"""
    p_Cors: typing.Union['PropUrlCors', dict] = attr.ib(
        default=None,
        converter=PropUrlCors.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropUrlCors)),
        metadata={
            AttrMeta.PROPERTY_NAME: "Cors",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'Cors',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-url.html#cfn-lambda-url-cors"""
    p_InvokeMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "InvokeMode",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-url.html#cfn-lambda-url-invokemode"""
    p_Qualifier: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "Qualifier",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-url.html#cfn-lambda-url-qualifier"""

    
    @property
    def rv_FunctionArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-url.html#aws-resource-lambda-url-return-values"""
        return GetAtt(resource=self, attr_name="FunctionArn")
    
    @property
    def rv_FunctionUrl(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-url.html#aws-resource-lambda-url-return-values"""
        return GetAtt(resource=self, attr_name="FunctionUrl")
    

@attr.s
class EventInvokeConfig(Resource):
    """
    AWS Object Type = "AWS::Lambda::EventInvokeConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html

    Property Document:
    
    - ``rp_FunctionName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html#cfn-lambda-eventinvokeconfig-functionname
    - ``rp_Qualifier``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html#cfn-lambda-eventinvokeconfig-qualifier
    - ``p_DestinationConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html#cfn-lambda-eventinvokeconfig-destinationconfig
    - ``p_MaximumEventAgeInSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html#cfn-lambda-eventinvokeconfig-maximumeventageinseconds
    - ``p_MaximumRetryAttempts``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html#cfn-lambda-eventinvokeconfig-maximumretryattempts
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::EventInvokeConfig"

    
    rp_FunctionName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={
            AttrMeta.PROPERTY_NAME: "FunctionName",
            AttrMeta.DATA: {
                "Required": True,
                "PrimitiveType": 'String',
                "UpdateType": 'Immutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html#cfn-lambda-eventinvokeconfig-functionname"""
    rp_Qualifier: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={
            AttrMeta.PROPERTY_NAME: "Qualifier",
            AttrMeta.DATA: {
                "Required": True,
                "PrimitiveType": 'String',
                "UpdateType": 'Immutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html#cfn-lambda-eventinvokeconfig-qualifier"""
    p_DestinationConfig: typing.Union['PropEventInvokeConfigDestinationConfig', dict] = attr.ib(
        default=None,
        converter=PropEventInvokeConfigDestinationConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropEventInvokeConfigDestinationConfig)),
        metadata={
            AttrMeta.PROPERTY_NAME: "DestinationConfig",
            AttrMeta.DATA: {
                "Type": 'DestinationConfig',
                "Required": False,
                "UpdateType": 'Mutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html#cfn-lambda-eventinvokeconfig-destinationconfig"""
    p_MaximumEventAgeInSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={
            AttrMeta.PROPERTY_NAME: "MaximumEventAgeInSeconds",
            AttrMeta.DATA: {
                "Required": False,
                "PrimitiveType": 'Integer',
                "UpdateType": 'Mutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html#cfn-lambda-eventinvokeconfig-maximumeventageinseconds"""
    p_MaximumRetryAttempts: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={
            AttrMeta.PROPERTY_NAME: "MaximumRetryAttempts",
            AttrMeta.DATA: {
                "Required": False,
                "PrimitiveType": 'Integer',
                "UpdateType": 'Mutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html#cfn-lambda-eventinvokeconfig-maximumretryattempts"""

    

@attr.s
class Function(Resource):
    """
    AWS Object Type = "AWS::Lambda::Function"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html

    Property Document:
    
    - ``rp_Code``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-code
    - ``rp_Role``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-role
    - ``p_Architectures``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-architectures
    - ``p_CodeSigningConfigArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-codesigningconfigarn
    - ``p_DeadLetterConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-deadletterconfig
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-description
    - ``p_Environment``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-environment
    - ``p_EphemeralStorage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-ephemeralstorage
    - ``p_FileSystemConfigs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-filesystemconfigs
    - ``p_FunctionName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-functionname
    - ``p_Handler``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-handler
    - ``p_ImageConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-imageconfig
    - ``p_KmsKeyArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-kmskeyarn
    - ``p_Layers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-layers
    - ``p_MemorySize``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-memorysize
    - ``p_PackageType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-packagetype
    - ``p_ReservedConcurrentExecutions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-reservedconcurrentexecutions
    - ``p_Runtime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-runtime
    - ``p_SnapStart``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-snapstart
    - ``p_Timeout``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-timeout
    - ``p_TracingConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-tracingconfig
    - ``p_VpcConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-vpcconfig
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-tags
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::Function"

    
    rp_Code: typing.Union['PropFunctionCode', dict] = attr.ib(
        default=None,
        converter=PropFunctionCode.from_dict,
        validator=attr.validators.instance_of(PropFunctionCode),
        metadata={
            AttrMeta.PROPERTY_NAME: "Code",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": True,
                "Type": 'Code',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-code"""
    rp_Role: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={
            AttrMeta.PROPERTY_NAME: "Role",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": True,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-role"""
    p_Architectures: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={
            AttrMeta.PROPERTY_NAME: "Architectures",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'List',
                "PrimitiveItemType": 'String',
                "DuplicatesAllowed": False,
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-architectures"""
    p_CodeSigningConfigArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "CodeSigningConfigArn",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-codesigningconfigarn"""
    p_DeadLetterConfig: typing.Union['PropFunctionDeadLetterConfig', dict] = attr.ib(
        default=None,
        converter=PropFunctionDeadLetterConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropFunctionDeadLetterConfig)),
        metadata={
            AttrMeta.PROPERTY_NAME: "DeadLetterConfig",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'DeadLetterConfig',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-deadletterconfig"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "Description",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-description"""
    p_Environment: typing.Union['PropFunctionEnvironment', dict] = attr.ib(
        default=None,
        converter=PropFunctionEnvironment.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropFunctionEnvironment)),
        metadata={
            AttrMeta.PROPERTY_NAME: "Environment",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'Environment',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-environment"""
    p_EphemeralStorage: typing.Union['PropFunctionEphemeralStorage', dict] = attr.ib(
        default=None,
        converter=PropFunctionEphemeralStorage.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropFunctionEphemeralStorage)),
        metadata={
            AttrMeta.PROPERTY_NAME: "EphemeralStorage",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'EphemeralStorage',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-ephemeralstorage"""
    p_FileSystemConfigs: typing.List[typing.Union['PropFunctionFileSystemConfig', dict]] = attr.ib(
        default=None,
        converter=PropFunctionFileSystemConfig.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropFunctionFileSystemConfig), iterable_validator=attr.validators.instance_of(list))),
        metadata={
            AttrMeta.PROPERTY_NAME: "FileSystemConfigs",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'List',
                "ItemType": 'FileSystemConfig',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-filesystemconfigs"""
    p_FunctionName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "FunctionName",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-functionname"""
    p_Handler: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "Handler",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-handler"""
    p_ImageConfig: typing.Union['PropFunctionImageConfig', dict] = attr.ib(
        default=None,
        converter=PropFunctionImageConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropFunctionImageConfig)),
        metadata={
            AttrMeta.PROPERTY_NAME: "ImageConfig",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'ImageConfig',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-imageconfig"""
    p_KmsKeyArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "KmsKeyArn",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-kmskeyarn"""
    p_Layers: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={
            AttrMeta.PROPERTY_NAME: "Layers",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'List',
                "PrimitiveItemType": 'String',
                "DuplicatesAllowed": True,
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-layers"""
    p_MemorySize: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={
            AttrMeta.PROPERTY_NAME: "MemorySize",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "PrimitiveType": 'Integer',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-memorysize"""
    p_PackageType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "PackageType",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-packagetype"""
    p_ReservedConcurrentExecutions: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={
            AttrMeta.PROPERTY_NAME: "ReservedConcurrentExecutions",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "PrimitiveType": 'Integer',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-reservedconcurrentexecutions"""
    p_Runtime: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "Runtime",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-runtime"""
    p_SnapStart: typing.Union['PropFunctionSnapStart', dict] = attr.ib(
        default=None,
        converter=PropFunctionSnapStart.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropFunctionSnapStart)),
        metadata={
            AttrMeta.PROPERTY_NAME: "SnapStart",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'SnapStart',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-snapstart"""
    p_Timeout: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={
            AttrMeta.PROPERTY_NAME: "Timeout",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "PrimitiveType": 'Integer',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-timeout"""
    p_TracingConfig: typing.Union['PropFunctionTracingConfig', dict] = attr.ib(
        default=None,
        converter=PropFunctionTracingConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropFunctionTracingConfig)),
        metadata={
            AttrMeta.PROPERTY_NAME: "TracingConfig",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'TracingConfig',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-tracingconfig"""
    p_VpcConfig: typing.Union['PropFunctionVpcConfig', dict] = attr.ib(
        default=None,
        converter=PropFunctionVpcConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropFunctionVpcConfig)),
        metadata={
            AttrMeta.PROPERTY_NAME: "VpcConfig",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'VpcConfig',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-vpcconfig"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={
            AttrMeta.PROPERTY_NAME: "Tags",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'List',
                "ItemType": 'Tag',
                "DuplicatesAllowed": False,
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#aws-resource-lambda-function-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class Permission(Resource):
    """
    AWS Object Type = "AWS::Lambda::Permission"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html

    Property Document:
    
    - ``rp_Action``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-action
    - ``rp_FunctionName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-functionname
    - ``rp_Principal``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-principal
    - ``p_EventSourceToken``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-eventsourcetoken
    - ``p_FunctionUrlAuthType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-functionurlauthtype
    - ``p_PrincipalOrgID``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-principalorgid
    - ``p_SourceAccount``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-sourceaccount
    - ``p_SourceArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-sourcearn
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::Permission"

    
    rp_Action: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={
            AttrMeta.PROPERTY_NAME: "Action",
            AttrMeta.DATA: {
                "PrimitiveType": 'String',
                "Required": True,
                "UpdateType": 'Immutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-action"""
    rp_FunctionName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={
            AttrMeta.PROPERTY_NAME: "FunctionName",
            AttrMeta.DATA: {
                "PrimitiveType": 'String',
                "Required": True,
                "UpdateType": 'Immutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-functionname"""
    rp_Principal: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={
            AttrMeta.PROPERTY_NAME: "Principal",
            AttrMeta.DATA: {
                "PrimitiveType": 'String',
                "Required": True,
                "UpdateType": 'Immutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-principal"""
    p_EventSourceToken: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "EventSourceToken",
            AttrMeta.DATA: {
                "PrimitiveType": 'String',
                "Required": False,
                "UpdateType": 'Immutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-eventsourcetoken"""
    p_FunctionUrlAuthType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "FunctionUrlAuthType",
            AttrMeta.DATA: {
                "PrimitiveType": 'String',
                "Required": False,
                "UpdateType": 'Immutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-functionurlauthtype"""
    p_PrincipalOrgID: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "PrincipalOrgID",
            AttrMeta.DATA: {
                "PrimitiveType": 'String',
                "Required": False,
                "UpdateType": 'Immutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-principalorgid"""
    p_SourceAccount: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "SourceAccount",
            AttrMeta.DATA: {
                "PrimitiveType": 'String',
                "Required": False,
                "UpdateType": 'Immutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-sourceaccount"""
    p_SourceArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "SourceArn",
            AttrMeta.DATA: {
                "PrimitiveType": 'String',
                "Required": False,
                "UpdateType": 'Immutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html#cfn-lambda-permission-sourcearn"""

    

@attr.s
class EventSourceMapping(Resource):
    """
    AWS Object Type = "AWS::Lambda::EventSourceMapping"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html

    Property Document:
    
    - ``rp_FunctionName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-functionname
    - ``p_AmazonManagedKafkaEventSourceConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig
    - ``p_BatchSize``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-batchsize
    - ``p_BisectBatchOnFunctionError``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-bisectbatchonfunctionerror
    - ``p_DestinationConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-destinationconfig
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-enabled
    - ``p_EventSourceArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-eventsourcearn
    - ``p_FilterCriteria``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-filtercriteria
    - ``p_FunctionResponseTypes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-functionresponsetypes
    - ``p_MaximumBatchingWindowInSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumbatchingwindowinseconds
    - ``p_MaximumRecordAgeInSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumrecordageinseconds
    - ``p_MaximumRetryAttempts``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumretryattempts
    - ``p_ParallelizationFactor``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-parallelizationfactor
    - ``p_Queues``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-queues
    - ``p_SelfManagedEventSource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-selfmanagedeventsource
    - ``p_SelfManagedKafkaEventSourceConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig
    - ``p_SourceAccessConfigurations``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-sourceaccessconfigurations
    - ``p_StartingPosition``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-startingposition
    - ``p_StartingPositionTimestamp``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-startingpositiontimestamp
    - ``p_Topics``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-topics
    - ``p_TumblingWindowInSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-tumblingwindowinseconds
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::EventSourceMapping"

    
    rp_FunctionName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={
            AttrMeta.PROPERTY_NAME: "FunctionName",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": True,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-functionname"""
    p_AmazonManagedKafkaEventSourceConfig: typing.Union['PropEventSourceMappingAmazonManagedKafkaEventSourceConfig', dict] = attr.ib(
        default=None,
        converter=PropEventSourceMappingAmazonManagedKafkaEventSourceConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropEventSourceMappingAmazonManagedKafkaEventSourceConfig)),
        metadata={
            AttrMeta.PROPERTY_NAME: "AmazonManagedKafkaEventSourceConfig",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "Type": 'AmazonManagedKafkaEventSourceConfig',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig"""
    p_BatchSize: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={
            AttrMeta.PROPERTY_NAME: "BatchSize",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "PrimitiveType": 'Integer',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-batchsize"""
    p_BisectBatchOnFunctionError: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={
            AttrMeta.PROPERTY_NAME: "BisectBatchOnFunctionError",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "PrimitiveType": 'Boolean',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-bisectbatchonfunctionerror"""
    p_DestinationConfig: typing.Union['PropEventSourceMappingDestinationConfig', dict] = attr.ib(
        default=None,
        converter=PropEventSourceMappingDestinationConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropEventSourceMappingDestinationConfig)),
        metadata={
            AttrMeta.PROPERTY_NAME: "DestinationConfig",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'DestinationConfig',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-destinationconfig"""
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={
            AttrMeta.PROPERTY_NAME: "Enabled",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "PrimitiveType": 'Boolean',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-enabled"""
    p_EventSourceArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "EventSourceArn",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-eventsourcearn"""
    p_FilterCriteria: typing.Union['PropEventSourceMappingFilterCriteria', dict] = attr.ib(
        default=None,
        converter=PropEventSourceMappingFilterCriteria.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropEventSourceMappingFilterCriteria)),
        metadata={
            AttrMeta.PROPERTY_NAME: "FilterCriteria",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'FilterCriteria',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-filtercriteria"""
    p_FunctionResponseTypes: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={
            AttrMeta.PROPERTY_NAME: "FunctionResponseTypes",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'List',
                "PrimitiveItemType": 'String',
                "DuplicatesAllowed": False,
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-functionresponsetypes"""
    p_MaximumBatchingWindowInSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={
            AttrMeta.PROPERTY_NAME: "MaximumBatchingWindowInSeconds",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "PrimitiveType": 'Integer',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumbatchingwindowinseconds"""
    p_MaximumRecordAgeInSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={
            AttrMeta.PROPERTY_NAME: "MaximumRecordAgeInSeconds",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "PrimitiveType": 'Integer',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumrecordageinseconds"""
    p_MaximumRetryAttempts: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={
            AttrMeta.PROPERTY_NAME: "MaximumRetryAttempts",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "PrimitiveType": 'Integer',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumretryattempts"""
    p_ParallelizationFactor: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={
            AttrMeta.PROPERTY_NAME: "ParallelizationFactor",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "PrimitiveType": 'Integer',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-parallelizationfactor"""
    p_Queues: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={
            AttrMeta.PROPERTY_NAME: "Queues",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'List',
                "PrimitiveItemType": 'String',
                "DuplicatesAllowed": False,
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-queues"""
    p_SelfManagedEventSource: typing.Union['PropEventSourceMappingSelfManagedEventSource', dict] = attr.ib(
        default=None,
        converter=PropEventSourceMappingSelfManagedEventSource.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropEventSourceMappingSelfManagedEventSource)),
        metadata={
            AttrMeta.PROPERTY_NAME: "SelfManagedEventSource",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "Type": 'SelfManagedEventSource',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-selfmanagedeventsource"""
    p_SelfManagedKafkaEventSourceConfig: typing.Union['PropEventSourceMappingSelfManagedKafkaEventSourceConfig', dict] = attr.ib(
        default=None,
        converter=PropEventSourceMappingSelfManagedKafkaEventSourceConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropEventSourceMappingSelfManagedKafkaEventSourceConfig)),
        metadata={
            AttrMeta.PROPERTY_NAME: "SelfManagedKafkaEventSourceConfig",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "Type": 'SelfManagedKafkaEventSourceConfig',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig"""
    p_SourceAccessConfigurations: typing.List[typing.Union['PropEventSourceMappingSourceAccessConfiguration', dict]] = attr.ib(
        default=None,
        converter=PropEventSourceMappingSourceAccessConfiguration.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropEventSourceMappingSourceAccessConfiguration), iterable_validator=attr.validators.instance_of(list))),
        metadata={
            AttrMeta.PROPERTY_NAME: "SourceAccessConfigurations",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'List',
                "ItemType": 'SourceAccessConfiguration',
                "DuplicatesAllowed": False,
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-sourceaccessconfigurations"""
    p_StartingPosition: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "StartingPosition",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-startingposition"""
    p_StartingPositionTimestamp: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={
            AttrMeta.PROPERTY_NAME: "StartingPositionTimestamp",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "PrimitiveType": 'Double',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-startingpositiontimestamp"""
    p_Topics: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={
            AttrMeta.PROPERTY_NAME: "Topics",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'List',
                "PrimitiveItemType": 'String',
                "DuplicatesAllowed": False,
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-topics"""
    p_TumblingWindowInSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={
            AttrMeta.PROPERTY_NAME: "TumblingWindowInSeconds",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "PrimitiveType": 'Integer',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-tumblingwindowinseconds"""

    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#aws-resource-lambda-eventsourcemapping-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    

@attr.s
class Version(Resource):
    """
    AWS Object Type = "AWS::Lambda::Version"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html

    Property Document:
    
    - ``rp_FunctionName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html#cfn-lambda-version-functionname
    - ``p_CodeSha256``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html#cfn-lambda-version-codesha256
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html#cfn-lambda-version-description
    - ``p_ProvisionedConcurrencyConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html#cfn-lambda-version-provisionedconcurrencyconfig
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::Version"

    
    rp_FunctionName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={
            AttrMeta.PROPERTY_NAME: "FunctionName",
            AttrMeta.DATA: {
                "PrimitiveType": 'String',
                "Required": True,
                "UpdateType": 'Immutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html#cfn-lambda-version-functionname"""
    p_CodeSha256: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "CodeSha256",
            AttrMeta.DATA: {
                "PrimitiveType": 'String',
                "Required": False,
                "UpdateType": 'Mutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html#cfn-lambda-version-codesha256"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "Description",
            AttrMeta.DATA: {
                "PrimitiveType": 'String',
                "Required": False,
                "UpdateType": 'Mutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html#cfn-lambda-version-description"""
    p_ProvisionedConcurrencyConfig: typing.Union['PropVersionProvisionedConcurrencyConfiguration', dict] = attr.ib(
        default=None,
        converter=PropVersionProvisionedConcurrencyConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVersionProvisionedConcurrencyConfiguration)),
        metadata={
            AttrMeta.PROPERTY_NAME: "ProvisionedConcurrencyConfig",
            AttrMeta.DATA: {
                "Required": False,
                "Type": 'ProvisionedConcurrencyConfiguration',
                "UpdateType": 'Mutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html#cfn-lambda-version-provisionedconcurrencyconfig"""

    
    @property
    def rv_Version(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html#aws-resource-lambda-version-return-values"""
        return GetAtt(resource=self, attr_name="Version")
    

@attr.s
class CodeSigningConfig(Resource):
    """
    AWS Object Type = "AWS::Lambda::CodeSigningConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html

    Property Document:
    
    - ``rp_AllowedPublishers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html#cfn-lambda-codesigningconfig-allowedpublishers
    - ``p_CodeSigningPolicies``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html#cfn-lambda-codesigningconfig-codesigningpolicies
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html#cfn-lambda-codesigningconfig-description
    """
    AWS_OBJECT_TYPE = "AWS::Lambda::CodeSigningConfig"

    
    rp_AllowedPublishers: typing.Union['PropCodeSigningConfigAllowedPublishers', dict] = attr.ib(
        default=None,
        converter=PropCodeSigningConfigAllowedPublishers.from_dict,
        validator=attr.validators.instance_of(PropCodeSigningConfigAllowedPublishers),
        metadata={
            AttrMeta.PROPERTY_NAME: "AllowedPublishers",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": True,
                "Type": 'AllowedPublishers',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html#cfn-lambda-codesigningconfig-allowedpublishers"""
    p_CodeSigningPolicies: typing.Union['PropCodeSigningConfigCodeSigningPolicies', dict] = attr.ib(
        default=None,
        converter=PropCodeSigningConfigCodeSigningPolicies.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCodeSigningConfigCodeSigningPolicies)),
        metadata={
            AttrMeta.PROPERTY_NAME: "CodeSigningPolicies",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'CodeSigningPolicies',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html#cfn-lambda-codesigningconfig-codesigningpolicies"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "Description",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html#cfn-lambda-codesigningconfig-description"""

    
    @property
    def rv_CodeSigningConfigId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html#aws-resource-lambda-codesigningconfig-return-values"""
        return GetAtt(resource=self, attr_name="CodeSigningConfigId")
    
    @property
    def rv_CodeSigningConfigArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html#aws-resource-lambda-codesigningconfig-return-values"""
        return GetAtt(resource=self, attr_name="CodeSigningConfigArn")
    
