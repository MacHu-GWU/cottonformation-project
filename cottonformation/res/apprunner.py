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
class PropServiceKeyValuePair(Property):
    """
    AWS Object Type = "AWS::AppRunner::Service.KeyValuePair"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-keyvaluepair.html

    Property Document:
    
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-keyvaluepair.html#cfn-apprunner-service-keyvaluepair-name
    - ``p_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-keyvaluepair.html#cfn-apprunner-service-keyvaluepair-value
    """
    AWS_OBJECT_TYPE = "AWS::AppRunner::Service.KeyValuePair"
    
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-keyvaluepair.html#cfn-apprunner-service-keyvaluepair-name"""
    p_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-keyvaluepair.html#cfn-apprunner-service-keyvaluepair-value"""

@attr.s
class PropServiceIngressConfiguration(Property):
    """
    AWS Object Type = "AWS::AppRunner::Service.IngressConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-ingressconfiguration.html

    Property Document:
    
    - ``rp_IsPubliclyAccessible``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-ingressconfiguration.html#cfn-apprunner-service-ingressconfiguration-ispubliclyaccessible
    """
    AWS_OBJECT_TYPE = "AWS::AppRunner::Service.IngressConfiguration"
    
    rp_IsPubliclyAccessible: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "IsPubliclyAccessible"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-ingressconfiguration.html#cfn-apprunner-service-ingressconfiguration-ispubliclyaccessible"""

@attr.s
class PropServiceHealthCheckConfiguration(Property):
    """
    AWS Object Type = "AWS::AppRunner::Service.HealthCheckConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html

    Property Document:
    
    - ``p_HealthyThreshold``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-healthythreshold
    - ``p_Interval``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-interval
    - ``p_Path``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-path
    - ``p_Protocol``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-protocol
    - ``p_Timeout``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-timeout
    - ``p_UnhealthyThreshold``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-unhealthythreshold
    """
    AWS_OBJECT_TYPE = "AWS::AppRunner::Service.HealthCheckConfiguration"
    
    p_HealthyThreshold: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "HealthyThreshold"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-healthythreshold"""
    p_Interval: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Interval"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-interval"""
    p_Path: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Path"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-path"""
    p_Protocol: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Protocol"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-protocol"""
    p_Timeout: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Timeout"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-timeout"""
    p_UnhealthyThreshold: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "UnhealthyThreshold"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-unhealthythreshold"""

@attr.s
class PropServiceServiceObservabilityConfiguration(Property):
    """
    AWS Object Type = "AWS::AppRunner::Service.ServiceObservabilityConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-serviceobservabilityconfiguration.html

    Property Document:
    
    - ``rp_ObservabilityEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-serviceobservabilityconfiguration.html#cfn-apprunner-service-serviceobservabilityconfiguration-observabilityenabled
    - ``p_ObservabilityConfigurationArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-serviceobservabilityconfiguration.html#cfn-apprunner-service-serviceobservabilityconfiguration-observabilityconfigurationarn
    """
    AWS_OBJECT_TYPE = "AWS::AppRunner::Service.ServiceObservabilityConfiguration"
    
    rp_ObservabilityEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "ObservabilityEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-serviceobservabilityconfiguration.html#cfn-apprunner-service-serviceobservabilityconfiguration-observabilityenabled"""
    p_ObservabilityConfigurationArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ObservabilityConfigurationArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-serviceobservabilityconfiguration.html#cfn-apprunner-service-serviceobservabilityconfiguration-observabilityconfigurationarn"""

@attr.s
class PropServiceSourceCodeVersion(Property):
    """
    AWS Object Type = "AWS::AppRunner::Service.SourceCodeVersion"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourcecodeversion.html

    Property Document:
    
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourcecodeversion.html#cfn-apprunner-service-sourcecodeversion-type
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourcecodeversion.html#cfn-apprunner-service-sourcecodeversion-value
    """
    AWS_OBJECT_TYPE = "AWS::AppRunner::Service.SourceCodeVersion"
    
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourcecodeversion.html#cfn-apprunner-service-sourcecodeversion-type"""
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourcecodeversion.html#cfn-apprunner-service-sourcecodeversion-value"""

@attr.s
class PropVpcIngressConnectionIngressVpcConfiguration(Property):
    """
    AWS Object Type = "AWS::AppRunner::VpcIngressConnection.IngressVpcConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-vpcingressconnection-ingressvpcconfiguration.html

    Property Document:
    
    - ``rp_VpcEndpointId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-vpcingressconnection-ingressvpcconfiguration.html#cfn-apprunner-vpcingressconnection-ingressvpcconfiguration-vpcendpointid
    - ``rp_VpcId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-vpcingressconnection-ingressvpcconfiguration.html#cfn-apprunner-vpcingressconnection-ingressvpcconfiguration-vpcid
    """
    AWS_OBJECT_TYPE = "AWS::AppRunner::VpcIngressConnection.IngressVpcConfiguration"
    
    rp_VpcEndpointId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "VpcEndpointId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-vpcingressconnection-ingressvpcconfiguration.html#cfn-apprunner-vpcingressconnection-ingressvpcconfiguration-vpcendpointid"""
    rp_VpcId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "VpcId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-vpcingressconnection-ingressvpcconfiguration.html#cfn-apprunner-vpcingressconnection-ingressvpcconfiguration-vpcid"""

@attr.s
class PropServiceInstanceConfiguration(Property):
    """
    AWS Object Type = "AWS::AppRunner::Service.InstanceConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html

    Property Document:
    
    - ``p_Cpu``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html#cfn-apprunner-service-instanceconfiguration-cpu
    - ``p_InstanceRoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html#cfn-apprunner-service-instanceconfiguration-instancerolearn
    - ``p_Memory``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html#cfn-apprunner-service-instanceconfiguration-memory
    """
    AWS_OBJECT_TYPE = "AWS::AppRunner::Service.InstanceConfiguration"
    
    p_Cpu: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Cpu"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html#cfn-apprunner-service-instanceconfiguration-cpu"""
    p_InstanceRoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "InstanceRoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html#cfn-apprunner-service-instanceconfiguration-instancerolearn"""
    p_Memory: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Memory"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html#cfn-apprunner-service-instanceconfiguration-memory"""

@attr.s
class PropServiceAuthenticationConfiguration(Property):
    """
    AWS Object Type = "AWS::AppRunner::Service.AuthenticationConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-authenticationconfiguration.html

    Property Document:
    
    - ``p_AccessRoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-authenticationconfiguration.html#cfn-apprunner-service-authenticationconfiguration-accessrolearn
    - ``p_ConnectionArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-authenticationconfiguration.html#cfn-apprunner-service-authenticationconfiguration-connectionarn
    """
    AWS_OBJECT_TYPE = "AWS::AppRunner::Service.AuthenticationConfiguration"
    
    p_AccessRoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AccessRoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-authenticationconfiguration.html#cfn-apprunner-service-authenticationconfiguration-accessrolearn"""
    p_ConnectionArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ConnectionArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-authenticationconfiguration.html#cfn-apprunner-service-authenticationconfiguration-connectionarn"""

@attr.s
class PropServiceEncryptionConfiguration(Property):
    """
    AWS Object Type = "AWS::AppRunner::Service.EncryptionConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-encryptionconfiguration.html

    Property Document:
    
    - ``rp_KmsKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-encryptionconfiguration.html#cfn-apprunner-service-encryptionconfiguration-kmskey
    """
    AWS_OBJECT_TYPE = "AWS::AppRunner::Service.EncryptionConfiguration"
    
    rp_KmsKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "KmsKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-encryptionconfiguration.html#cfn-apprunner-service-encryptionconfiguration-kmskey"""

@attr.s
class PropObservabilityConfigurationTraceConfiguration(Property):
    """
    AWS Object Type = "AWS::AppRunner::ObservabilityConfiguration.TraceConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-observabilityconfiguration-traceconfiguration.html

    Property Document:
    
    - ``rp_Vendor``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-observabilityconfiguration-traceconfiguration.html#cfn-apprunner-observabilityconfiguration-traceconfiguration-vendor
    """
    AWS_OBJECT_TYPE = "AWS::AppRunner::ObservabilityConfiguration.TraceConfiguration"
    
    rp_Vendor: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Vendor"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-observabilityconfiguration-traceconfiguration.html#cfn-apprunner-observabilityconfiguration-traceconfiguration-vendor"""

@attr.s
class PropServiceCodeConfigurationValues(Property):
    """
    AWS Object Type = "AWS::AppRunner::Service.CodeConfigurationValues"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html

    Property Document:
    
    - ``rp_Runtime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-runtime
    - ``p_BuildCommand``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-buildcommand
    - ``p_Port``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-port
    - ``p_RuntimeEnvironmentVariables``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-runtimeenvironmentvariables
    - ``p_StartCommand``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-startcommand
    """
    AWS_OBJECT_TYPE = "AWS::AppRunner::Service.CodeConfigurationValues"
    
    rp_Runtime: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Runtime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-runtime"""
    p_BuildCommand: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BuildCommand"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-buildcommand"""
    p_Port: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Port"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-port"""
    p_RuntimeEnvironmentVariables: typing.List[typing.Union['PropServiceKeyValuePair', dict]] = attr.ib(
        default=None,
        converter=PropServiceKeyValuePair.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropServiceKeyValuePair), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "RuntimeEnvironmentVariables"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-runtimeenvironmentvariables"""
    p_StartCommand: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "StartCommand"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-startcommand"""

@attr.s
class PropServiceEgressConfiguration(Property):
    """
    AWS Object Type = "AWS::AppRunner::Service.EgressConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-egressconfiguration.html

    Property Document:
    
    - ``rp_EgressType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-egressconfiguration.html#cfn-apprunner-service-egressconfiguration-egresstype
    - ``p_VpcConnectorArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-egressconfiguration.html#cfn-apprunner-service-egressconfiguration-vpcconnectorarn
    """
    AWS_OBJECT_TYPE = "AWS::AppRunner::Service.EgressConfiguration"
    
    rp_EgressType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "EgressType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-egressconfiguration.html#cfn-apprunner-service-egressconfiguration-egresstype"""
    p_VpcConnectorArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "VpcConnectorArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-egressconfiguration.html#cfn-apprunner-service-egressconfiguration-vpcconnectorarn"""

@attr.s
class PropServiceImageConfiguration(Property):
    """
    AWS Object Type = "AWS::AppRunner::Service.ImageConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html

    Property Document:
    
    - ``p_Port``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html#cfn-apprunner-service-imageconfiguration-port
    - ``p_RuntimeEnvironmentVariables``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html#cfn-apprunner-service-imageconfiguration-runtimeenvironmentvariables
    - ``p_StartCommand``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html#cfn-apprunner-service-imageconfiguration-startcommand
    """
    AWS_OBJECT_TYPE = "AWS::AppRunner::Service.ImageConfiguration"
    
    p_Port: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Port"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html#cfn-apprunner-service-imageconfiguration-port"""
    p_RuntimeEnvironmentVariables: typing.List[typing.Union['PropServiceKeyValuePair', dict]] = attr.ib(
        default=None,
        converter=PropServiceKeyValuePair.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropServiceKeyValuePair), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "RuntimeEnvironmentVariables"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html#cfn-apprunner-service-imageconfiguration-runtimeenvironmentvariables"""
    p_StartCommand: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "StartCommand"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html#cfn-apprunner-service-imageconfiguration-startcommand"""

@attr.s
class PropServiceCodeConfiguration(Property):
    """
    AWS Object Type = "AWS::AppRunner::Service.CodeConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfiguration.html

    Property Document:
    
    - ``rp_ConfigurationSource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfiguration.html#cfn-apprunner-service-codeconfiguration-configurationsource
    - ``p_CodeConfigurationValues``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfiguration.html#cfn-apprunner-service-codeconfiguration-codeconfigurationvalues
    """
    AWS_OBJECT_TYPE = "AWS::AppRunner::Service.CodeConfiguration"
    
    rp_ConfigurationSource: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ConfigurationSource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfiguration.html#cfn-apprunner-service-codeconfiguration-configurationsource"""
    p_CodeConfigurationValues: typing.Union['PropServiceCodeConfigurationValues', dict] = attr.ib(
        default=None,
        converter=PropServiceCodeConfigurationValues.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropServiceCodeConfigurationValues)),
        metadata={AttrMeta.PROPERTY_NAME: "CodeConfigurationValues"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfiguration.html#cfn-apprunner-service-codeconfiguration-codeconfigurationvalues"""

@attr.s
class PropServiceImageRepository(Property):
    """
    AWS Object Type = "AWS::AppRunner::Service.ImageRepository"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html

    Property Document:
    
    - ``rp_ImageIdentifier``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html#cfn-apprunner-service-imagerepository-imageidentifier
    - ``rp_ImageRepositoryType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html#cfn-apprunner-service-imagerepository-imagerepositorytype
    - ``p_ImageConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html#cfn-apprunner-service-imagerepository-imageconfiguration
    """
    AWS_OBJECT_TYPE = "AWS::AppRunner::Service.ImageRepository"
    
    rp_ImageIdentifier: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ImageIdentifier"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html#cfn-apprunner-service-imagerepository-imageidentifier"""
    rp_ImageRepositoryType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ImageRepositoryType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html#cfn-apprunner-service-imagerepository-imagerepositorytype"""
    p_ImageConfiguration: typing.Union['PropServiceImageConfiguration', dict] = attr.ib(
        default=None,
        converter=PropServiceImageConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropServiceImageConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "ImageConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html#cfn-apprunner-service-imagerepository-imageconfiguration"""

@attr.s
class PropServiceNetworkConfiguration(Property):
    """
    AWS Object Type = "AWS::AppRunner::Service.NetworkConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-networkconfiguration.html

    Property Document:
    
    - ``p_EgressConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-networkconfiguration.html#cfn-apprunner-service-networkconfiguration-egressconfiguration
    - ``p_IngressConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-networkconfiguration.html#cfn-apprunner-service-networkconfiguration-ingressconfiguration
    """
    AWS_OBJECT_TYPE = "AWS::AppRunner::Service.NetworkConfiguration"
    
    p_EgressConfiguration: typing.Union['PropServiceEgressConfiguration', dict] = attr.ib(
        default=None,
        converter=PropServiceEgressConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropServiceEgressConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "EgressConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-networkconfiguration.html#cfn-apprunner-service-networkconfiguration-egressconfiguration"""
    p_IngressConfiguration: typing.Union['PropServiceIngressConfiguration', dict] = attr.ib(
        default=None,
        converter=PropServiceIngressConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropServiceIngressConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "IngressConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-networkconfiguration.html#cfn-apprunner-service-networkconfiguration-ingressconfiguration"""

@attr.s
class PropServiceCodeRepository(Property):
    """
    AWS Object Type = "AWS::AppRunner::Service.CodeRepository"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-coderepository.html

    Property Document:
    
    - ``rp_RepositoryUrl``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-coderepository.html#cfn-apprunner-service-coderepository-repositoryurl
    - ``rp_SourceCodeVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-coderepository.html#cfn-apprunner-service-coderepository-sourcecodeversion
    - ``p_CodeConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-coderepository.html#cfn-apprunner-service-coderepository-codeconfiguration
    """
    AWS_OBJECT_TYPE = "AWS::AppRunner::Service.CodeRepository"
    
    rp_RepositoryUrl: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RepositoryUrl"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-coderepository.html#cfn-apprunner-service-coderepository-repositoryurl"""
    rp_SourceCodeVersion: typing.Union['PropServiceSourceCodeVersion', dict] = attr.ib(
        default=None,
        converter=PropServiceSourceCodeVersion.from_dict,
        validator=attr.validators.instance_of(PropServiceSourceCodeVersion),
        metadata={AttrMeta.PROPERTY_NAME: "SourceCodeVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-coderepository.html#cfn-apprunner-service-coderepository-sourcecodeversion"""
    p_CodeConfiguration: typing.Union['PropServiceCodeConfiguration', dict] = attr.ib(
        default=None,
        converter=PropServiceCodeConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropServiceCodeConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "CodeConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-coderepository.html#cfn-apprunner-service-coderepository-codeconfiguration"""

@attr.s
class PropServiceSourceConfiguration(Property):
    """
    AWS Object Type = "AWS::AppRunner::Service.SourceConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html

    Property Document:
    
    - ``p_AuthenticationConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html#cfn-apprunner-service-sourceconfiguration-authenticationconfiguration
    - ``p_AutoDeploymentsEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html#cfn-apprunner-service-sourceconfiguration-autodeploymentsenabled
    - ``p_CodeRepository``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html#cfn-apprunner-service-sourceconfiguration-coderepository
    - ``p_ImageRepository``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html#cfn-apprunner-service-sourceconfiguration-imagerepository
    """
    AWS_OBJECT_TYPE = "AWS::AppRunner::Service.SourceConfiguration"
    
    p_AuthenticationConfiguration: typing.Union['PropServiceAuthenticationConfiguration', dict] = attr.ib(
        default=None,
        converter=PropServiceAuthenticationConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropServiceAuthenticationConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "AuthenticationConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html#cfn-apprunner-service-sourceconfiguration-authenticationconfiguration"""
    p_AutoDeploymentsEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "AutoDeploymentsEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html#cfn-apprunner-service-sourceconfiguration-autodeploymentsenabled"""
    p_CodeRepository: typing.Union['PropServiceCodeRepository', dict] = attr.ib(
        default=None,
        converter=PropServiceCodeRepository.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropServiceCodeRepository)),
        metadata={AttrMeta.PROPERTY_NAME: "CodeRepository"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html#cfn-apprunner-service-sourceconfiguration-coderepository"""
    p_ImageRepository: typing.Union['PropServiceImageRepository', dict] = attr.ib(
        default=None,
        converter=PropServiceImageRepository.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropServiceImageRepository)),
        metadata={AttrMeta.PROPERTY_NAME: "ImageRepository"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html#cfn-apprunner-service-sourceconfiguration-imagerepository"""


#--- Resource declaration ---

@attr.s
class VpcConnector(Resource):
    """
    AWS Object Type = "AWS::AppRunner::VpcConnector"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html

    Property Document:
    
    - ``rp_Subnets``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html#cfn-apprunner-vpcconnector-subnets
    - ``p_SecurityGroups``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html#cfn-apprunner-vpcconnector-securitygroups
    - ``p_VpcConnectorName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html#cfn-apprunner-vpcconnector-vpcconnectorname
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html#cfn-apprunner-vpcconnector-tags
    """
    AWS_OBJECT_TYPE = "AWS::AppRunner::VpcConnector"

    
    rp_Subnets: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={
            AttrMeta.PROPERTY_NAME: "Subnets",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": True,
                "Type": 'List',
                "PrimitiveItemType": 'String',
                "DuplicatesAllowed": False,
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html#cfn-apprunner-vpcconnector-subnets"""
    p_SecurityGroups: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={
            AttrMeta.PROPERTY_NAME: "SecurityGroups",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "Type": 'List',
                "PrimitiveItemType": 'String',
                "DuplicatesAllowed": False,
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html#cfn-apprunner-vpcconnector-securitygroups"""
    p_VpcConnectorName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "VpcConnectorName",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html#cfn-apprunner-vpcconnector-vpcconnectorname"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={
            AttrMeta.PROPERTY_NAME: "Tags",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "Type": 'List',
                "ItemType": 'Tag',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html#cfn-apprunner-vpcconnector-tags"""

    
    @property
    def rv_VpcConnectorArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html#aws-resource-apprunner-vpcconnector-return-values"""
        return GetAtt(resource=self, attr_name="VpcConnectorArn")
    
    @property
    def rv_VpcConnectorRevision(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html#aws-resource-apprunner-vpcconnector-return-values"""
        return GetAtt(resource=self, attr_name="VpcConnectorRevision")
    

@attr.s
class ObservabilityConfiguration(Resource):
    """
    AWS Object Type = "AWS::AppRunner::ObservabilityConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-observabilityconfiguration.html

    Property Document:
    
    - ``p_ObservabilityConfigurationName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-observabilityconfiguration.html#cfn-apprunner-observabilityconfiguration-observabilityconfigurationname
    - ``p_TraceConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-observabilityconfiguration.html#cfn-apprunner-observabilityconfiguration-traceconfiguration
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-observabilityconfiguration.html#cfn-apprunner-observabilityconfiguration-tags
    """
    AWS_OBJECT_TYPE = "AWS::AppRunner::ObservabilityConfiguration"

    
    p_ObservabilityConfigurationName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "ObservabilityConfigurationName",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-observabilityconfiguration.html#cfn-apprunner-observabilityconfiguration-observabilityconfigurationname"""
    p_TraceConfiguration: typing.Union['PropObservabilityConfigurationTraceConfiguration', dict] = attr.ib(
        default=None,
        converter=PropObservabilityConfigurationTraceConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropObservabilityConfigurationTraceConfiguration)),
        metadata={
            AttrMeta.PROPERTY_NAME: "TraceConfiguration",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "Type": 'TraceConfiguration',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-observabilityconfiguration.html#cfn-apprunner-observabilityconfiguration-traceconfiguration"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={
            AttrMeta.PROPERTY_NAME: "Tags",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "Type": 'List',
                "ItemType": 'Tag',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-observabilityconfiguration.html#cfn-apprunner-observabilityconfiguration-tags"""

    
    @property
    def rv_ObservabilityConfigurationArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-observabilityconfiguration.html#aws-resource-apprunner-observabilityconfiguration-return-values"""
        return GetAtt(resource=self, attr_name="ObservabilityConfigurationArn")
    
    @property
    def rv_ObservabilityConfigurationRevision(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-observabilityconfiguration.html#aws-resource-apprunner-observabilityconfiguration-return-values"""
        return GetAtt(resource=self, attr_name="ObservabilityConfigurationRevision")
    
    @property
    def rv_Latest(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-observabilityconfiguration.html#aws-resource-apprunner-observabilityconfiguration-return-values"""
        return GetAtt(resource=self, attr_name="Latest")
    

@attr.s
class VpcIngressConnection(Resource):
    """
    AWS Object Type = "AWS::AppRunner::VpcIngressConnection"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcingressconnection.html

    Property Document:
    
    - ``rp_IngressVpcConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcingressconnection.html#cfn-apprunner-vpcingressconnection-ingressvpcconfiguration
    - ``rp_ServiceArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcingressconnection.html#cfn-apprunner-vpcingressconnection-servicearn
    - ``p_VpcIngressConnectionName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcingressconnection.html#cfn-apprunner-vpcingressconnection-vpcingressconnectionname
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcingressconnection.html#cfn-apprunner-vpcingressconnection-tags
    """
    AWS_OBJECT_TYPE = "AWS::AppRunner::VpcIngressConnection"

    
    rp_IngressVpcConfiguration: typing.Union['PropVpcIngressConnectionIngressVpcConfiguration', dict] = attr.ib(
        default=None,
        converter=PropVpcIngressConnectionIngressVpcConfiguration.from_dict,
        validator=attr.validators.instance_of(PropVpcIngressConnectionIngressVpcConfiguration),
        metadata={
            AttrMeta.PROPERTY_NAME: "IngressVpcConfiguration",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": True,
                "Type": 'IngressVpcConfiguration',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcingressconnection.html#cfn-apprunner-vpcingressconnection-ingressvpcconfiguration"""
    rp_ServiceArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={
            AttrMeta.PROPERTY_NAME: "ServiceArn",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": True,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcingressconnection.html#cfn-apprunner-vpcingressconnection-servicearn"""
    p_VpcIngressConnectionName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "VpcIngressConnectionName",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcingressconnection.html#cfn-apprunner-vpcingressconnection-vpcingressconnectionname"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={
            AttrMeta.PROPERTY_NAME: "Tags",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "Type": 'List',
                "ItemType": 'Tag',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcingressconnection.html#cfn-apprunner-vpcingressconnection-tags"""

    
    @property
    def rv_VpcIngressConnectionArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcingressconnection.html#aws-resource-apprunner-vpcingressconnection-return-values"""
        return GetAtt(resource=self, attr_name="VpcIngressConnectionArn")
    
    @property
    def rv_Status(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcingressconnection.html#aws-resource-apprunner-vpcingressconnection-return-values"""
        return GetAtt(resource=self, attr_name="Status")
    
    @property
    def rv_DomainName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcingressconnection.html#aws-resource-apprunner-vpcingressconnection-return-values"""
        return GetAtt(resource=self, attr_name="DomainName")
    

@attr.s
class Service(Resource):
    """
    AWS Object Type = "AWS::AppRunner::Service"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html

    Property Document:
    
    - ``rp_SourceConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-sourceconfiguration
    - ``p_AutoScalingConfigurationArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-autoscalingconfigurationarn
    - ``p_EncryptionConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-encryptionconfiguration
    - ``p_HealthCheckConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-healthcheckconfiguration
    - ``p_InstanceConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-instanceconfiguration
    - ``p_NetworkConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-networkconfiguration
    - ``p_ObservabilityConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-observabilityconfiguration
    - ``p_ServiceName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-servicename
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-tags
    """
    AWS_OBJECT_TYPE = "AWS::AppRunner::Service"

    
    rp_SourceConfiguration: typing.Union['PropServiceSourceConfiguration', dict] = attr.ib(
        default=None,
        converter=PropServiceSourceConfiguration.from_dict,
        validator=attr.validators.instance_of(PropServiceSourceConfiguration),
        metadata={
            AttrMeta.PROPERTY_NAME: "SourceConfiguration",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": True,
                "Type": 'SourceConfiguration',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-sourceconfiguration"""
    p_AutoScalingConfigurationArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "AutoScalingConfigurationArn",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-autoscalingconfigurationarn"""
    p_EncryptionConfiguration: typing.Union['PropServiceEncryptionConfiguration', dict] = attr.ib(
        default=None,
        converter=PropServiceEncryptionConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropServiceEncryptionConfiguration)),
        metadata={
            AttrMeta.PROPERTY_NAME: "EncryptionConfiguration",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "Type": 'EncryptionConfiguration',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-encryptionconfiguration"""
    p_HealthCheckConfiguration: typing.Union['PropServiceHealthCheckConfiguration', dict] = attr.ib(
        default=None,
        converter=PropServiceHealthCheckConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropServiceHealthCheckConfiguration)),
        metadata={
            AttrMeta.PROPERTY_NAME: "HealthCheckConfiguration",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'HealthCheckConfiguration',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-healthcheckconfiguration"""
    p_InstanceConfiguration: typing.Union['PropServiceInstanceConfiguration', dict] = attr.ib(
        default=None,
        converter=PropServiceInstanceConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropServiceInstanceConfiguration)),
        metadata={
            AttrMeta.PROPERTY_NAME: "InstanceConfiguration",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'InstanceConfiguration',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-instanceconfiguration"""
    p_NetworkConfiguration: typing.Union['PropServiceNetworkConfiguration', dict] = attr.ib(
        default=None,
        converter=PropServiceNetworkConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropServiceNetworkConfiguration)),
        metadata={
            AttrMeta.PROPERTY_NAME: "NetworkConfiguration",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'NetworkConfiguration',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-networkconfiguration"""
    p_ObservabilityConfiguration: typing.Union['PropServiceServiceObservabilityConfiguration', dict] = attr.ib(
        default=None,
        converter=PropServiceServiceObservabilityConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropServiceServiceObservabilityConfiguration)),
        metadata={
            AttrMeta.PROPERTY_NAME: "ObservabilityConfiguration",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'ServiceObservabilityConfiguration',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-observabilityconfiguration"""
    p_ServiceName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "ServiceName",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-servicename"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={
            AttrMeta.PROPERTY_NAME: "Tags",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "Type": 'List',
                "ItemType": 'Tag',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-tags"""

    
    @property
    def rv_ServiceId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#aws-resource-apprunner-service-return-values"""
        return GetAtt(resource=self, attr_name="ServiceId")
    
    @property
    def rv_ServiceArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#aws-resource-apprunner-service-return-values"""
        return GetAtt(resource=self, attr_name="ServiceArn")
    
    @property
    def rv_ServiceUrl(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#aws-resource-apprunner-service-return-values"""
        return GetAtt(resource=self, attr_name="ServiceUrl")
    
    @property
    def rv_Status(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#aws-resource-apprunner-service-return-values"""
        return GetAtt(resource=self, attr_name="Status")
    
