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
class PropClusterCapacityProviderAssociationsCapacityProviderStrategy(Property):
    """
    AWS Object Type = "AWS::ECS::ClusterCapacityProviderAssociations.CapacityProviderStrategy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-clustercapacityproviderassociations-capacityproviderstrategy.html

    Property Document:
    
    - ``rp_CapacityProvider``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-clustercapacityproviderassociations-capacityproviderstrategy.html#cfn-ecs-clustercapacityproviderassociations-capacityproviderstrategy-capacityprovider
    - ``p_Base``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-clustercapacityproviderassociations-capacityproviderstrategy.html#cfn-ecs-clustercapacityproviderassociations-capacityproviderstrategy-base
    - ``p_Weight``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-clustercapacityproviderassociations-capacityproviderstrategy.html#cfn-ecs-clustercapacityproviderassociations-capacityproviderstrategy-weight
    """
    AWS_OBJECT_TYPE = "AWS::ECS::ClusterCapacityProviderAssociations.CapacityProviderStrategy"
    
    rp_CapacityProvider: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "CapacityProvider"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-clustercapacityproviderassociations-capacityproviderstrategy.html#cfn-ecs-clustercapacityproviderassociations-capacityproviderstrategy-capacityprovider"""
    p_Base: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Base"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-clustercapacityproviderassociations-capacityproviderstrategy.html#cfn-ecs-clustercapacityproviderassociations-capacityproviderstrategy-base"""
    p_Weight: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Weight"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-clustercapacityproviderassociations-capacityproviderstrategy.html#cfn-ecs-clustercapacityproviderassociations-capacityproviderstrategy-weight"""

@attr.s
class PropTaskDefinitionFirelensConfiguration(Property):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition.FirelensConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-firelensconfiguration.html

    Property Document:
    
    - ``p_Options``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-firelensconfiguration.html#cfn-ecs-taskdefinition-firelensconfiguration-options
    - ``p_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-firelensconfiguration.html#cfn-ecs-taskdefinition-firelensconfiguration-type
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition.FirelensConfiguration"
    
    p_Options: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type))),
        metadata={AttrMeta.PROPERTY_NAME: "Options"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-firelensconfiguration.html#cfn-ecs-taskdefinition-firelensconfiguration-options"""
    p_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-firelensconfiguration.html#cfn-ecs-taskdefinition-firelensconfiguration-type"""

@attr.s
class PropTaskDefinitionDevice(Property):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition.Device"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-device.html

    Property Document:
    
    - ``p_ContainerPath``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-device.html#cfn-ecs-taskdefinition-device-containerpath
    - ``p_HostPath``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-device.html#cfn-ecs-taskdefinition-device-hostpath
    - ``p_Permissions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-device.html#cfn-ecs-taskdefinition-device-permissions
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition.Device"
    
    p_ContainerPath: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ContainerPath"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-device.html#cfn-ecs-taskdefinition-device-containerpath"""
    p_HostPath: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "HostPath"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-device.html#cfn-ecs-taskdefinition-device-hostpath"""
    p_Permissions: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Permissions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-device.html#cfn-ecs-taskdefinition-device-permissions"""

@attr.s
class PropServicePlacementStrategy(Property):
    """
    AWS Object Type = "AWS::ECS::Service.PlacementStrategy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-placementstrategy.html

    Property Document:
    
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-placementstrategy.html#cfn-ecs-service-placementstrategy-type
    - ``p_Field``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-placementstrategy.html#cfn-ecs-service-placementstrategy-field
    """
    AWS_OBJECT_TYPE = "AWS::ECS::Service.PlacementStrategy"
    
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-placementstrategy.html#cfn-ecs-service-placementstrategy-type"""
    p_Field: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Field"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-placementstrategy.html#cfn-ecs-service-placementstrategy-field"""

@attr.s
class PropServiceDeploymentController(Property):
    """
    AWS Object Type = "AWS::ECS::Service.DeploymentController"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentcontroller.html

    Property Document:
    
    - ``p_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentcontroller.html#cfn-ecs-service-deploymentcontroller-type
    """
    AWS_OBJECT_TYPE = "AWS::ECS::Service.DeploymentController"
    
    p_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentcontroller.html#cfn-ecs-service-deploymentcontroller-type"""

@attr.s
class PropTaskDefinitionSystemControl(Property):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition.SystemControl"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-systemcontrol.html

    Property Document:
    
    - ``p_Namespace``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-systemcontrol.html#cfn-ecs-taskdefinition-systemcontrol-namespace
    - ``p_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-systemcontrol.html#cfn-ecs-taskdefinition-systemcontrol-value
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition.SystemControl"
    
    p_Namespace: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Namespace"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-systemcontrol.html#cfn-ecs-taskdefinition-systemcontrol-namespace"""
    p_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-systemcontrol.html#cfn-ecs-taskdefinition-systemcontrol-value"""

@attr.s
class PropClusterClusterSettings(Property):
    """
    AWS Object Type = "AWS::ECS::Cluster.ClusterSettings"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clustersettings.html

    Property Document:
    
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clustersettings.html#cfn-ecs-cluster-clustersettings-name
    - ``p_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clustersettings.html#cfn-ecs-cluster-clustersettings-value
    """
    AWS_OBJECT_TYPE = "AWS::ECS::Cluster.ClusterSettings"
    
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clustersettings.html#cfn-ecs-cluster-clustersettings-name"""
    p_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clustersettings.html#cfn-ecs-cluster-clustersettings-value"""

@attr.s
class PropServicePlacementConstraint(Property):
    """
    AWS Object Type = "AWS::ECS::Service.PlacementConstraint"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-placementconstraint.html

    Property Document:
    
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-placementconstraint.html#cfn-ecs-service-placementconstraint-type
    - ``p_Expression``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-placementconstraint.html#cfn-ecs-service-placementconstraint-expression
    """
    AWS_OBJECT_TYPE = "AWS::ECS::Service.PlacementConstraint"
    
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-placementconstraint.html#cfn-ecs-service-placementconstraint-type"""
    p_Expression: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Expression"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-placementconstraint.html#cfn-ecs-service-placementconstraint-expression"""

@attr.s
class PropTaskSetServiceRegistry(Property):
    """
    AWS Object Type = "AWS::ECS::TaskSet.ServiceRegistry"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-serviceregistry.html

    Property Document:
    
    - ``p_ContainerName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-serviceregistry.html#cfn-ecs-taskset-serviceregistry-containername
    - ``p_ContainerPort``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-serviceregistry.html#cfn-ecs-taskset-serviceregistry-containerport
    - ``p_Port``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-serviceregistry.html#cfn-ecs-taskset-serviceregistry-port
    - ``p_RegistryArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-serviceregistry.html#cfn-ecs-taskset-serviceregistry-registryarn
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskSet.ServiceRegistry"
    
    p_ContainerName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ContainerName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-serviceregistry.html#cfn-ecs-taskset-serviceregistry-containername"""
    p_ContainerPort: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ContainerPort"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-serviceregistry.html#cfn-ecs-taskset-serviceregistry-containerport"""
    p_Port: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Port"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-serviceregistry.html#cfn-ecs-taskset-serviceregistry-port"""
    p_RegistryArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RegistryArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-serviceregistry.html#cfn-ecs-taskset-serviceregistry-registryarn"""

@attr.s
class PropTaskDefinitionEphemeralStorage(Property):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition.EphemeralStorage"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-ephemeralstorage.html

    Property Document:
    
    - ``p_SizeInGiB``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-ephemeralstorage.html#cfn-ecs-taskdefinition-ephemeralstorage-sizeingib
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition.EphemeralStorage"
    
    p_SizeInGiB: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "SizeInGiB"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-ephemeralstorage.html#cfn-ecs-taskdefinition-ephemeralstorage-sizeingib"""

@attr.s
class PropTaskDefinitionResourceRequirement(Property):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition.ResourceRequirement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-resourcerequirement.html

    Property Document:
    
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-resourcerequirement.html#cfn-ecs-taskdefinition-resourcerequirement-type
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-resourcerequirement.html#cfn-ecs-taskdefinition-resourcerequirement-value
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition.ResourceRequirement"
    
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-resourcerequirement.html#cfn-ecs-taskdefinition-resourcerequirement-type"""
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-resourcerequirement.html#cfn-ecs-taskdefinition-resourcerequirement-value"""

@attr.s
class PropTaskDefinitionDockerVolumeConfiguration(Property):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition.DockerVolumeConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-dockervolumeconfiguration.html

    Property Document:
    
    - ``p_Autoprovision``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-dockervolumeconfiguration.html#cfn-ecs-taskdefinition-dockervolumeconfiguration-autoprovision
    - ``p_Driver``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-dockervolumeconfiguration.html#cfn-ecs-taskdefinition-dockervolumeconfiguration-driver
    - ``p_DriverOpts``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-dockervolumeconfiguration.html#cfn-ecs-taskdefinition-dockervolumeconfiguration-driveropts
    - ``p_Labels``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-dockervolumeconfiguration.html#cfn-ecs-taskdefinition-dockervolumeconfiguration-labels
    - ``p_Scope``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-dockervolumeconfiguration.html#cfn-ecs-taskdefinition-dockervolumeconfiguration-scope
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition.DockerVolumeConfiguration"
    
    p_Autoprovision: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Autoprovision"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-dockervolumeconfiguration.html#cfn-ecs-taskdefinition-dockervolumeconfiguration-autoprovision"""
    p_Driver: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Driver"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-dockervolumeconfiguration.html#cfn-ecs-taskdefinition-dockervolumeconfiguration-driver"""
    p_DriverOpts: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type))),
        metadata={AttrMeta.PROPERTY_NAME: "DriverOpts"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-dockervolumeconfiguration.html#cfn-ecs-taskdefinition-dockervolumeconfiguration-driveropts"""
    p_Labels: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type))),
        metadata={AttrMeta.PROPERTY_NAME: "Labels"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-dockervolumeconfiguration.html#cfn-ecs-taskdefinition-dockervolumeconfiguration-labels"""
    p_Scope: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Scope"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-dockervolumeconfiguration.html#cfn-ecs-taskdefinition-dockervolumeconfiguration-scope"""

@attr.s
class PropTaskDefinitionAuthorizationConfig(Property):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition.AuthorizationConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-authorizationconfig.html

    Property Document:
    
    - ``p_AccessPointId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-authorizationconfig.html#cfn-ecs-taskdefinition-authorizationconfig-accesspointid
    - ``p_IAM``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-authorizationconfig.html#cfn-ecs-taskdefinition-authorizationconfig-iam
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition.AuthorizationConfig"
    
    p_AccessPointId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AccessPointId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-authorizationconfig.html#cfn-ecs-taskdefinition-authorizationconfig-accesspointid"""
    p_IAM: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "IAM"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-authorizationconfig.html#cfn-ecs-taskdefinition-authorizationconfig-iam"""

@attr.s
class PropTaskDefinitionMountPoint(Property):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition.MountPoint"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-mountpoints.html

    Property Document:
    
    - ``p_ContainerPath``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-mountpoints.html#cfn-ecs-taskdefinition-containerdefinition-mountpoints-containerpath
    - ``p_ReadOnly``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-mountpoints.html#cfn-ecs-taskdefinition-containerdefinition-mountpoints-readonly
    - ``p_SourceVolume``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-mountpoints.html#cfn-ecs-taskdefinition-containerdefinition-mountpoints-sourcevolume
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition.MountPoint"
    
    p_ContainerPath: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ContainerPath"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-mountpoints.html#cfn-ecs-taskdefinition-containerdefinition-mountpoints-containerpath"""
    p_ReadOnly: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "ReadOnly"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-mountpoints.html#cfn-ecs-taskdefinition-containerdefinition-mountpoints-readonly"""
    p_SourceVolume: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SourceVolume"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-mountpoints.html#cfn-ecs-taskdefinition-containerdefinition-mountpoints-sourcevolume"""

@attr.s
class PropTaskDefinitionKernelCapabilities(Property):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition.KernelCapabilities"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-kernelcapabilities.html

    Property Document:
    
    - ``p_Add``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-kernelcapabilities.html#cfn-ecs-taskdefinition-kernelcapabilities-add
    - ``p_Drop``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-kernelcapabilities.html#cfn-ecs-taskdefinition-kernelcapabilities-drop
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition.KernelCapabilities"
    
    p_Add: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Add"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-kernelcapabilities.html#cfn-ecs-taskdefinition-kernelcapabilities-add"""
    p_Drop: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Drop"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-kernelcapabilities.html#cfn-ecs-taskdefinition-kernelcapabilities-drop"""

@attr.s
class PropTaskDefinitionPortMapping(Property):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition.PortMapping"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-portmappings.html

    Property Document:
    
    - ``p_ContainerPort``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-portmappings.html#cfn-ecs-taskdefinition-containerdefinition-portmappings-containerport
    - ``p_HostPort``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-portmappings.html#cfn-ecs-taskdefinition-containerdefinition-portmappings-readonly
    - ``p_Protocol``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-portmappings.html#cfn-ecs-taskdefinition-containerdefinition-portmappings-sourcevolume
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition.PortMapping"
    
    p_ContainerPort: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ContainerPort"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-portmappings.html#cfn-ecs-taskdefinition-containerdefinition-portmappings-containerport"""
    p_HostPort: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "HostPort"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-portmappings.html#cfn-ecs-taskdefinition-containerdefinition-portmappings-readonly"""
    p_Protocol: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Protocol"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-portmappings.html#cfn-ecs-taskdefinition-containerdefinition-portmappings-sourcevolume"""

@attr.s
class PropTaskDefinitionUlimit(Property):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition.Ulimit"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-ulimit.html

    Property Document:
    
    - ``rp_HardLimit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-ulimit.html#cfn-ecs-taskdefinition-containerdefinition-ulimit-hardlimit
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-ulimit.html#cfn-ecs-taskdefinition-containerdefinition-ulimit-name
    - ``rp_SoftLimit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-ulimit.html#cfn-ecs-taskdefinition-containerdefinition-ulimit-softlimit
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition.Ulimit"
    
    rp_HardLimit: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "HardLimit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-ulimit.html#cfn-ecs-taskdefinition-containerdefinition-ulimit-hardlimit"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-ulimit.html#cfn-ecs-taskdefinition-containerdefinition-ulimit-name"""
    rp_SoftLimit: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "SoftLimit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-ulimit.html#cfn-ecs-taskdefinition-containerdefinition-ulimit-softlimit"""

@attr.s
class PropTaskDefinitionContainerDependency(Property):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition.ContainerDependency"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdependency.html

    Property Document:
    
    - ``p_Condition``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdependency.html#cfn-ecs-taskdefinition-containerdependency-condition
    - ``p_ContainerName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdependency.html#cfn-ecs-taskdefinition-containerdependency-containername
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition.ContainerDependency"
    
    p_Condition: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Condition"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdependency.html#cfn-ecs-taskdefinition-containerdependency-condition"""
    p_ContainerName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ContainerName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdependency.html#cfn-ecs-taskdefinition-containerdependency-containername"""

@attr.s
class PropTaskDefinitionHostVolumeProperties(Property):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition.HostVolumeProperties"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-volumes-host.html

    Property Document:
    
    - ``p_SourcePath``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-volumes-host.html#cfn-ecs-taskdefinition-volumes-host-sourcepath
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition.HostVolumeProperties"
    
    p_SourcePath: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SourcePath"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-volumes-host.html#cfn-ecs-taskdefinition-volumes-host-sourcepath"""

@attr.s
class PropTaskDefinitionRepositoryCredentials(Property):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition.RepositoryCredentials"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-repositorycredentials.html

    Property Document:
    
    - ``p_CredentialsParameter``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-repositorycredentials.html#cfn-ecs-taskdefinition-repositorycredentials-credentialsparameter
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition.RepositoryCredentials"
    
    p_CredentialsParameter: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CredentialsParameter"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-repositorycredentials.html#cfn-ecs-taskdefinition-repositorycredentials-credentialsparameter"""

@attr.s
class PropTaskSetLoadBalancer(Property):
    """
    AWS Object Type = "AWS::ECS::TaskSet.LoadBalancer"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-loadbalancer.html

    Property Document:
    
    - ``p_ContainerName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-loadbalancer.html#cfn-ecs-taskset-loadbalancer-containername
    - ``p_ContainerPort``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-loadbalancer.html#cfn-ecs-taskset-loadbalancer-containerport
    - ``p_LoadBalancerName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-loadbalancer.html#cfn-ecs-taskset-loadbalancer-loadbalancername
    - ``p_TargetGroupArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-loadbalancer.html#cfn-ecs-taskset-loadbalancer-targetgrouparn
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskSet.LoadBalancer"
    
    p_ContainerName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ContainerName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-loadbalancer.html#cfn-ecs-taskset-loadbalancer-containername"""
    p_ContainerPort: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ContainerPort"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-loadbalancer.html#cfn-ecs-taskset-loadbalancer-containerport"""
    p_LoadBalancerName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LoadBalancerName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-loadbalancer.html#cfn-ecs-taskset-loadbalancer-loadbalancername"""
    p_TargetGroupArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TargetGroupArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-loadbalancer.html#cfn-ecs-taskset-loadbalancer-targetgrouparn"""

@attr.s
class PropClusterExecuteCommandLogConfiguration(Property):
    """
    AWS Object Type = "AWS::ECS::Cluster.ExecuteCommandLogConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandlogconfiguration.html

    Property Document:
    
    - ``p_CloudWatchEncryptionEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandlogconfiguration.html#cfn-ecs-cluster-executecommandlogconfiguration-cloudwatchencryptionenabled
    - ``p_CloudWatchLogGroupName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandlogconfiguration.html#cfn-ecs-cluster-executecommandlogconfiguration-cloudwatchloggroupname
    - ``p_S3BucketName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandlogconfiguration.html#cfn-ecs-cluster-executecommandlogconfiguration-s3bucketname
    - ``p_S3EncryptionEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandlogconfiguration.html#cfn-ecs-cluster-executecommandlogconfiguration-s3encryptionenabled
    - ``p_S3KeyPrefix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandlogconfiguration.html#cfn-ecs-cluster-executecommandlogconfiguration-s3keyprefix
    """
    AWS_OBJECT_TYPE = "AWS::ECS::Cluster.ExecuteCommandLogConfiguration"
    
    p_CloudWatchEncryptionEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "CloudWatchEncryptionEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandlogconfiguration.html#cfn-ecs-cluster-executecommandlogconfiguration-cloudwatchencryptionenabled"""
    p_CloudWatchLogGroupName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CloudWatchLogGroupName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandlogconfiguration.html#cfn-ecs-cluster-executecommandlogconfiguration-cloudwatchloggroupname"""
    p_S3BucketName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "S3BucketName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandlogconfiguration.html#cfn-ecs-cluster-executecommandlogconfiguration-s3bucketname"""
    p_S3EncryptionEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "S3EncryptionEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandlogconfiguration.html#cfn-ecs-cluster-executecommandlogconfiguration-s3encryptionenabled"""
    p_S3KeyPrefix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "S3KeyPrefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandlogconfiguration.html#cfn-ecs-cluster-executecommandlogconfiguration-s3keyprefix"""

@attr.s
class PropServiceLoadBalancer(Property):
    """
    AWS Object Type = "AWS::ECS::Service.LoadBalancer"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-loadbalancer.html

    Property Document:
    
    - ``p_ContainerName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-loadbalancer.html#cfn-ecs-service-loadbalancer-containername
    - ``p_ContainerPort``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-loadbalancer.html#cfn-ecs-service-loadbalancer-containerport
    - ``p_LoadBalancerName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-loadbalancer.html#cfn-ecs-service-loadbalancer-loadbalancername
    - ``p_TargetGroupArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-loadbalancer.html#cfn-ecs-service-loadbalancer-targetgrouparn
    """
    AWS_OBJECT_TYPE = "AWS::ECS::Service.LoadBalancer"
    
    p_ContainerName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ContainerName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-loadbalancer.html#cfn-ecs-service-loadbalancer-containername"""
    p_ContainerPort: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ContainerPort"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-loadbalancer.html#cfn-ecs-service-loadbalancer-containerport"""
    p_LoadBalancerName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LoadBalancerName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-loadbalancer.html#cfn-ecs-service-loadbalancer-loadbalancername"""
    p_TargetGroupArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TargetGroupArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-loadbalancer.html#cfn-ecs-service-loadbalancer-targetgrouparn"""

@attr.s
class PropTaskDefinitionInferenceAccelerator(Property):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition.InferenceAccelerator"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-inferenceaccelerator.html

    Property Document:
    
    - ``p_DeviceName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-inferenceaccelerator.html#cfn-ecs-taskdefinition-inferenceaccelerator-devicename
    - ``p_DeviceType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-inferenceaccelerator.html#cfn-ecs-taskdefinition-inferenceaccelerator-devicetype
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition.InferenceAccelerator"
    
    p_DeviceName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DeviceName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-inferenceaccelerator.html#cfn-ecs-taskdefinition-inferenceaccelerator-devicename"""
    p_DeviceType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DeviceType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-inferenceaccelerator.html#cfn-ecs-taskdefinition-inferenceaccelerator-devicetype"""

@attr.s
class PropTaskDefinitionRuntimePlatform(Property):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition.RuntimePlatform"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-runtimeplatform.html

    Property Document:
    
    - ``p_CpuArchitecture``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-runtimeplatform.html#cfn-ecs-taskdefinition-runtimeplatform-cpuarchitecture
    - ``p_OperatingSystemFamily``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-runtimeplatform.html#cfn-ecs-taskdefinition-runtimeplatform-operatingsystemfamily
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition.RuntimePlatform"
    
    p_CpuArchitecture: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CpuArchitecture"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-runtimeplatform.html#cfn-ecs-taskdefinition-runtimeplatform-cpuarchitecture"""
    p_OperatingSystemFamily: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "OperatingSystemFamily"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-runtimeplatform.html#cfn-ecs-taskdefinition-runtimeplatform-operatingsystemfamily"""

@attr.s
class PropTaskDefinitionSecret(Property):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition.Secret"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-secret.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-secret.html#cfn-ecs-taskdefinition-secret-name
    - ``rp_ValueFrom``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-secret.html#cfn-ecs-taskdefinition-secret-valuefrom
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition.Secret"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-secret.html#cfn-ecs-taskdefinition-secret-name"""
    rp_ValueFrom: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ValueFrom"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-secret.html#cfn-ecs-taskdefinition-secret-valuefrom"""

@attr.s
class PropClusterExecuteCommandConfiguration(Property):
    """
    AWS Object Type = "AWS::ECS::Cluster.ExecuteCommandConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandconfiguration.html

    Property Document:
    
    - ``p_KmsKeyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandconfiguration.html#cfn-ecs-cluster-executecommandconfiguration-kmskeyid
    - ``p_LogConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandconfiguration.html#cfn-ecs-cluster-executecommandconfiguration-logconfiguration
    - ``p_Logging``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandconfiguration.html#cfn-ecs-cluster-executecommandconfiguration-logging
    """
    AWS_OBJECT_TYPE = "AWS::ECS::Cluster.ExecuteCommandConfiguration"
    
    p_KmsKeyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "KmsKeyId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandconfiguration.html#cfn-ecs-cluster-executecommandconfiguration-kmskeyid"""
    p_LogConfiguration: typing.Union['PropClusterExecuteCommandLogConfiguration', dict] = attr.ib(
        default=None,
        converter=PropClusterExecuteCommandLogConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropClusterExecuteCommandLogConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "LogConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandconfiguration.html#cfn-ecs-cluster-executecommandconfiguration-logconfiguration"""
    p_Logging: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Logging"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandconfiguration.html#cfn-ecs-cluster-executecommandconfiguration-logging"""

@attr.s
class PropTaskSetAwsVpcConfiguration(Property):
    """
    AWS Object Type = "AWS::ECS::TaskSet.AwsVpcConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-awsvpcconfiguration.html

    Property Document:
    
    - ``rp_Subnets``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-awsvpcconfiguration.html#cfn-ecs-taskset-awsvpcconfiguration-subnets
    - ``p_AssignPublicIp``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-awsvpcconfiguration.html#cfn-ecs-taskset-awsvpcconfiguration-assignpublicip
    - ``p_SecurityGroups``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-awsvpcconfiguration.html#cfn-ecs-taskset-awsvpcconfiguration-securitygroups
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskSet.AwsVpcConfiguration"
    
    rp_Subnets: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Subnets"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-awsvpcconfiguration.html#cfn-ecs-taskset-awsvpcconfiguration-subnets"""
    p_AssignPublicIp: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AssignPublicIp"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-awsvpcconfiguration.html#cfn-ecs-taskset-awsvpcconfiguration-assignpublicip"""
    p_SecurityGroups: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SecurityGroups"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-awsvpcconfiguration.html#cfn-ecs-taskset-awsvpcconfiguration-securitygroups"""

@attr.s
class PropTaskDefinitionEnvironmentFile(Property):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition.EnvironmentFile"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-environmentfile.html

    Property Document:
    
    - ``p_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-environmentfile.html#cfn-ecs-taskdefinition-environmentfile-type
    - ``p_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-environmentfile.html#cfn-ecs-taskdefinition-environmentfile-value
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition.EnvironmentFile"
    
    p_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-environmentfile.html#cfn-ecs-taskdefinition-environmentfile-type"""
    p_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-environmentfile.html#cfn-ecs-taskdefinition-environmentfile-value"""

@attr.s
class PropTaskDefinitionVolumeFrom(Property):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition.VolumeFrom"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-volumesfrom.html

    Property Document:
    
    - ``p_ReadOnly``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-volumesfrom.html#cfn-ecs-taskdefinition-containerdefinition-volumesfrom-readonly
    - ``p_SourceContainer``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-volumesfrom.html#cfn-ecs-taskdefinition-containerdefinition-volumesfrom-sourcecontainer
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition.VolumeFrom"
    
    p_ReadOnly: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "ReadOnly"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-volumesfrom.html#cfn-ecs-taskdefinition-containerdefinition-volumesfrom-readonly"""
    p_SourceContainer: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SourceContainer"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-volumesfrom.html#cfn-ecs-taskdefinition-containerdefinition-volumesfrom-sourcecontainer"""

@attr.s
class PropTaskDefinitionHostEntry(Property):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition.HostEntry"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-hostentry.html

    Property Document:
    
    - ``p_Hostname``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-hostentry.html#cfn-ecs-taskdefinition-containerdefinition-hostentry-hostname
    - ``p_IpAddress``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-hostentry.html#cfn-ecs-taskdefinition-containerdefinition-hostentry-ipaddress
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition.HostEntry"
    
    p_Hostname: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Hostname"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-hostentry.html#cfn-ecs-taskdefinition-containerdefinition-hostentry-hostname"""
    p_IpAddress: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "IpAddress"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-hostentry.html#cfn-ecs-taskdefinition-containerdefinition-hostentry-ipaddress"""

@attr.s
class PropTaskDefinitionTaskDefinitionPlacementConstraint(Property):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition.TaskDefinitionPlacementConstraint"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-taskdefinitionplacementconstraint.html

    Property Document:
    
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-taskdefinitionplacementconstraint.html#cfn-ecs-taskdefinition-taskdefinitionplacementconstraint-type
    - ``p_Expression``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-taskdefinitionplacementconstraint.html#cfn-ecs-taskdefinition-taskdefinitionplacementconstraint-expression
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition.TaskDefinitionPlacementConstraint"
    
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-taskdefinitionplacementconstraint.html#cfn-ecs-taskdefinition-taskdefinitionplacementconstraint-type"""
    p_Expression: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Expression"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-taskdefinitionplacementconstraint.html#cfn-ecs-taskdefinition-taskdefinitionplacementconstraint-expression"""

@attr.s
class PropCapacityProviderManagedScaling(Property):
    """
    AWS Object Type = "AWS::ECS::CapacityProvider.ManagedScaling"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-managedscaling.html

    Property Document:
    
    - ``p_InstanceWarmupPeriod``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-managedscaling.html#cfn-ecs-capacityprovider-managedscaling-instancewarmupperiod
    - ``p_MaximumScalingStepSize``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-managedscaling.html#cfn-ecs-capacityprovider-managedscaling-maximumscalingstepsize
    - ``p_MinimumScalingStepSize``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-managedscaling.html#cfn-ecs-capacityprovider-managedscaling-minimumscalingstepsize
    - ``p_Status``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-managedscaling.html#cfn-ecs-capacityprovider-managedscaling-status
    - ``p_TargetCapacity``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-managedscaling.html#cfn-ecs-capacityprovider-managedscaling-targetcapacity
    """
    AWS_OBJECT_TYPE = "AWS::ECS::CapacityProvider.ManagedScaling"
    
    p_InstanceWarmupPeriod: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "InstanceWarmupPeriod"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-managedscaling.html#cfn-ecs-capacityprovider-managedscaling-instancewarmupperiod"""
    p_MaximumScalingStepSize: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MaximumScalingStepSize"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-managedscaling.html#cfn-ecs-capacityprovider-managedscaling-maximumscalingstepsize"""
    p_MinimumScalingStepSize: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MinimumScalingStepSize"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-managedscaling.html#cfn-ecs-capacityprovider-managedscaling-minimumscalingstepsize"""
    p_Status: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Status"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-managedscaling.html#cfn-ecs-capacityprovider-managedscaling-status"""
    p_TargetCapacity: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "TargetCapacity"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-managedscaling.html#cfn-ecs-capacityprovider-managedscaling-targetcapacity"""

@attr.s
class PropServiceAwsVpcConfiguration(Property):
    """
    AWS Object Type = "AWS::ECS::Service.AwsVpcConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-awsvpcconfiguration.html

    Property Document:
    
    - ``p_AssignPublicIp``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-awsvpcconfiguration.html#cfn-ecs-service-awsvpcconfiguration-assignpublicip
    - ``p_SecurityGroups``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-awsvpcconfiguration.html#cfn-ecs-service-awsvpcconfiguration-securitygroups
    - ``p_Subnets``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-awsvpcconfiguration.html#cfn-ecs-service-awsvpcconfiguration-subnets
    """
    AWS_OBJECT_TYPE = "AWS::ECS::Service.AwsVpcConfiguration"
    
    p_AssignPublicIp: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AssignPublicIp"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-awsvpcconfiguration.html#cfn-ecs-service-awsvpcconfiguration-assignpublicip"""
    p_SecurityGroups: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SecurityGroups"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-awsvpcconfiguration.html#cfn-ecs-service-awsvpcconfiguration-securitygroups"""
    p_Subnets: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Subnets"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-awsvpcconfiguration.html#cfn-ecs-service-awsvpcconfiguration-subnets"""

@attr.s
class PropServiceNetworkConfiguration(Property):
    """
    AWS Object Type = "AWS::ECS::Service.NetworkConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-networkconfiguration.html

    Property Document:
    
    - ``p_AwsvpcConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-networkconfiguration.html#cfn-ecs-service-networkconfiguration-awsvpcconfiguration
    """
    AWS_OBJECT_TYPE = "AWS::ECS::Service.NetworkConfiguration"
    
    p_AwsvpcConfiguration: typing.Union['PropServiceAwsVpcConfiguration', dict] = attr.ib(
        default=None,
        converter=PropServiceAwsVpcConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropServiceAwsVpcConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "AwsvpcConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-networkconfiguration.html#cfn-ecs-service-networkconfiguration-awsvpcconfiguration"""

@attr.s
class PropTaskDefinitionTmpfs(Property):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition.Tmpfs"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-tmpfs.html

    Property Document:
    
    - ``rp_Size``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-tmpfs.html#cfn-ecs-taskdefinition-tmpfs-size
    - ``p_ContainerPath``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-tmpfs.html#cfn-ecs-taskdefinition-tmpfs-containerpath
    - ``p_MountOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-tmpfs.html#cfn-ecs-taskdefinition-tmpfs-mountoptions
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition.Tmpfs"
    
    rp_Size: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Size"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-tmpfs.html#cfn-ecs-taskdefinition-tmpfs-size"""
    p_ContainerPath: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ContainerPath"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-tmpfs.html#cfn-ecs-taskdefinition-tmpfs-containerpath"""
    p_MountOptions: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "MountOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-tmpfs.html#cfn-ecs-taskdefinition-tmpfs-mountoptions"""

@attr.s
class PropServiceCapacityProviderStrategyItem(Property):
    """
    AWS Object Type = "AWS::ECS::Service.CapacityProviderStrategyItem"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-capacityproviderstrategyitem.html

    Property Document:
    
    - ``p_Base``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-capacityproviderstrategyitem.html#cfn-ecs-service-capacityproviderstrategyitem-base
    - ``p_CapacityProvider``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-capacityproviderstrategyitem.html#cfn-ecs-service-capacityproviderstrategyitem-capacityprovider
    - ``p_Weight``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-capacityproviderstrategyitem.html#cfn-ecs-service-capacityproviderstrategyitem-weight
    """
    AWS_OBJECT_TYPE = "AWS::ECS::Service.CapacityProviderStrategyItem"
    
    p_Base: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Base"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-capacityproviderstrategyitem.html#cfn-ecs-service-capacityproviderstrategyitem-base"""
    p_CapacityProvider: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CapacityProvider"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-capacityproviderstrategyitem.html#cfn-ecs-service-capacityproviderstrategyitem-capacityprovider"""
    p_Weight: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Weight"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-capacityproviderstrategyitem.html#cfn-ecs-service-capacityproviderstrategyitem-weight"""

@attr.s
class PropServiceDeploymentCircuitBreaker(Property):
    """
    AWS Object Type = "AWS::ECS::Service.DeploymentCircuitBreaker"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentcircuitbreaker.html

    Property Document:
    
    - ``rp_Enable``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentcircuitbreaker.html#cfn-ecs-service-deploymentcircuitbreaker-enable
    - ``rp_Rollback``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentcircuitbreaker.html#cfn-ecs-service-deploymentcircuitbreaker-rollback
    """
    AWS_OBJECT_TYPE = "AWS::ECS::Service.DeploymentCircuitBreaker"
    
    rp_Enable: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Enable"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentcircuitbreaker.html#cfn-ecs-service-deploymentcircuitbreaker-enable"""
    rp_Rollback: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Rollback"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentcircuitbreaker.html#cfn-ecs-service-deploymentcircuitbreaker-rollback"""

@attr.s
class PropTaskDefinitionKeyValuePair(Property):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition.KeyValuePair"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-environment.html

    Property Document:
    
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-environment.html#cfn-ecs-taskdefinition-containerdefinition-environment-name
    - ``p_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-environment.html#cfn-ecs-taskdefinition-containerdefinition-environment-value
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition.KeyValuePair"
    
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-environment.html#cfn-ecs-taskdefinition-containerdefinition-environment-name"""
    p_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-environment.html#cfn-ecs-taskdefinition-containerdefinition-environment-value"""

@attr.s
class PropClusterClusterConfiguration(Property):
    """
    AWS Object Type = "AWS::ECS::Cluster.ClusterConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clusterconfiguration.html

    Property Document:
    
    - ``p_ExecuteCommandConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clusterconfiguration.html#cfn-ecs-cluster-clusterconfiguration-executecommandconfiguration
    """
    AWS_OBJECT_TYPE = "AWS::ECS::Cluster.ClusterConfiguration"
    
    p_ExecuteCommandConfiguration: typing.Union['PropClusterExecuteCommandConfiguration', dict] = attr.ib(
        default=None,
        converter=PropClusterExecuteCommandConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropClusterExecuteCommandConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "ExecuteCommandConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clusterconfiguration.html#cfn-ecs-cluster-clusterconfiguration-executecommandconfiguration"""

@attr.s
class PropServiceServiceRegistry(Property):
    """
    AWS Object Type = "AWS::ECS::Service.ServiceRegistry"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceregistry.html

    Property Document:
    
    - ``p_ContainerName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceregistry.html#cfn-ecs-service-serviceregistry-containername
    - ``p_ContainerPort``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceregistry.html#cfn-ecs-service-serviceregistry-containerport
    - ``p_Port``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceregistry.html#cfn-ecs-service-serviceregistry-port
    - ``p_RegistryArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceregistry.html#cfn-ecs-service-serviceregistry-registryarn
    """
    AWS_OBJECT_TYPE = "AWS::ECS::Service.ServiceRegistry"
    
    p_ContainerName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ContainerName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceregistry.html#cfn-ecs-service-serviceregistry-containername"""
    p_ContainerPort: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ContainerPort"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceregistry.html#cfn-ecs-service-serviceregistry-containerport"""
    p_Port: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Port"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceregistry.html#cfn-ecs-service-serviceregistry-port"""
    p_RegistryArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RegistryArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceregistry.html#cfn-ecs-service-serviceregistry-registryarn"""

@attr.s
class PropTaskDefinitionHealthCheck(Property):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition.HealthCheck"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-healthcheck.html

    Property Document:
    
    - ``p_Command``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-healthcheck.html#cfn-ecs-taskdefinition-healthcheck-command
    - ``p_Interval``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-healthcheck.html#cfn-ecs-taskdefinition-healthcheck-interval
    - ``p_Retries``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-healthcheck.html#cfn-ecs-taskdefinition-healthcheck-retries
    - ``p_StartPeriod``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-healthcheck.html#cfn-ecs-taskdefinition-healthcheck-startperiod
    - ``p_Timeout``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-healthcheck.html#cfn-ecs-taskdefinition-healthcheck-timeout
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition.HealthCheck"
    
    p_Command: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Command"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-healthcheck.html#cfn-ecs-taskdefinition-healthcheck-command"""
    p_Interval: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Interval"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-healthcheck.html#cfn-ecs-taskdefinition-healthcheck-interval"""
    p_Retries: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Retries"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-healthcheck.html#cfn-ecs-taskdefinition-healthcheck-retries"""
    p_StartPeriod: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "StartPeriod"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-healthcheck.html#cfn-ecs-taskdefinition-healthcheck-startperiod"""
    p_Timeout: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Timeout"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-healthcheck.html#cfn-ecs-taskdefinition-healthcheck-timeout"""

@attr.s
class PropTaskDefinitionLinuxParameters(Property):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition.LinuxParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-linuxparameters.html

    Property Document:
    
    - ``p_Capabilities``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-linuxparameters.html#cfn-ecs-taskdefinition-linuxparameters-capabilities
    - ``p_Devices``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-linuxparameters.html#cfn-ecs-taskdefinition-linuxparameters-devices
    - ``p_InitProcessEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-linuxparameters.html#cfn-ecs-taskdefinition-linuxparameters-initprocessenabled
    - ``p_MaxSwap``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-linuxparameters.html#cfn-ecs-taskdefinition-linuxparameters-maxswap
    - ``p_SharedMemorySize``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-linuxparameters.html#cfn-ecs-taskdefinition-linuxparameters-sharedmemorysize
    - ``p_Swappiness``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-linuxparameters.html#cfn-ecs-taskdefinition-linuxparameters-swappiness
    - ``p_Tmpfs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-linuxparameters.html#cfn-ecs-taskdefinition-linuxparameters-tmpfs
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition.LinuxParameters"
    
    p_Capabilities: typing.Union['PropTaskDefinitionKernelCapabilities', dict] = attr.ib(
        default=None,
        converter=PropTaskDefinitionKernelCapabilities.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTaskDefinitionKernelCapabilities)),
        metadata={AttrMeta.PROPERTY_NAME: "Capabilities"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-linuxparameters.html#cfn-ecs-taskdefinition-linuxparameters-capabilities"""
    p_Devices: typing.List[typing.Union['PropTaskDefinitionDevice', dict]] = attr.ib(
        default=None,
        converter=PropTaskDefinitionDevice.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTaskDefinitionDevice), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Devices"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-linuxparameters.html#cfn-ecs-taskdefinition-linuxparameters-devices"""
    p_InitProcessEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "InitProcessEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-linuxparameters.html#cfn-ecs-taskdefinition-linuxparameters-initprocessenabled"""
    p_MaxSwap: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MaxSwap"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-linuxparameters.html#cfn-ecs-taskdefinition-linuxparameters-maxswap"""
    p_SharedMemorySize: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "SharedMemorySize"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-linuxparameters.html#cfn-ecs-taskdefinition-linuxparameters-sharedmemorysize"""
    p_Swappiness: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Swappiness"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-linuxparameters.html#cfn-ecs-taskdefinition-linuxparameters-swappiness"""
    p_Tmpfs: typing.List[typing.Union['PropTaskDefinitionTmpfs', dict]] = attr.ib(
        default=None,
        converter=PropTaskDefinitionTmpfs.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTaskDefinitionTmpfs), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tmpfs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-linuxparameters.html#cfn-ecs-taskdefinition-linuxparameters-tmpfs"""

@attr.s
class PropTaskDefinitionProxyConfiguration(Property):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition.ProxyConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-proxyconfiguration.html

    Property Document:
    
    - ``rp_ContainerName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-proxyconfiguration.html#cfn-ecs-taskdefinition-proxyconfiguration-containername
    - ``p_ProxyConfigurationProperties``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-proxyconfiguration.html#cfn-ecs-taskdefinition-proxyconfiguration-proxyconfigurationproperties
    - ``p_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-proxyconfiguration.html#cfn-ecs-taskdefinition-proxyconfiguration-type
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition.ProxyConfiguration"
    
    rp_ContainerName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ContainerName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-proxyconfiguration.html#cfn-ecs-taskdefinition-proxyconfiguration-containername"""
    p_ProxyConfigurationProperties: typing.List[typing.Union['PropTaskDefinitionKeyValuePair', dict]] = attr.ib(
        default=None,
        converter=PropTaskDefinitionKeyValuePair.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTaskDefinitionKeyValuePair), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ProxyConfigurationProperties"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-proxyconfiguration.html#cfn-ecs-taskdefinition-proxyconfiguration-proxyconfigurationproperties"""
    p_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-proxyconfiguration.html#cfn-ecs-taskdefinition-proxyconfiguration-type"""

@attr.s
class PropTaskSetScale(Property):
    """
    AWS Object Type = "AWS::ECS::TaskSet.Scale"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-scale.html

    Property Document:
    
    - ``p_Unit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-scale.html#cfn-ecs-taskset-scale-unit
    - ``p_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-scale.html#cfn-ecs-taskset-scale-value
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskSet.Scale"
    
    p_Unit: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Unit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-scale.html#cfn-ecs-taskset-scale-unit"""
    p_Value: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-scale.html#cfn-ecs-taskset-scale-value"""

@attr.s
class PropClusterCapacityProviderStrategyItem(Property):
    """
    AWS Object Type = "AWS::ECS::Cluster.CapacityProviderStrategyItem"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-capacityproviderstrategyitem.html

    Property Document:
    
    - ``p_Base``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-capacityproviderstrategyitem.html#cfn-ecs-cluster-capacityproviderstrategyitem-base
    - ``p_CapacityProvider``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-capacityproviderstrategyitem.html#cfn-ecs-cluster-capacityproviderstrategyitem-capacityprovider
    - ``p_Weight``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-capacityproviderstrategyitem.html#cfn-ecs-cluster-capacityproviderstrategyitem-weight
    """
    AWS_OBJECT_TYPE = "AWS::ECS::Cluster.CapacityProviderStrategyItem"
    
    p_Base: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Base"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-capacityproviderstrategyitem.html#cfn-ecs-cluster-capacityproviderstrategyitem-base"""
    p_CapacityProvider: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CapacityProvider"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-capacityproviderstrategyitem.html#cfn-ecs-cluster-capacityproviderstrategyitem-capacityprovider"""
    p_Weight: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Weight"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-capacityproviderstrategyitem.html#cfn-ecs-cluster-capacityproviderstrategyitem-weight"""

@attr.s
class PropTaskDefinitionLogConfiguration(Property):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition.LogConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-logconfiguration.html

    Property Document:
    
    - ``rp_LogDriver``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-logconfiguration.html#cfn-ecs-taskdefinition-containerdefinition-logconfiguration-logdriver
    - ``p_Options``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-logconfiguration.html#cfn-ecs-taskdefinition-containerdefinition-logconfiguration-options
    - ``p_SecretOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-logconfiguration.html#cfn-ecs-taskdefinition-logconfiguration-secretoptions
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition.LogConfiguration"
    
    rp_LogDriver: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "LogDriver"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-logconfiguration.html#cfn-ecs-taskdefinition-containerdefinition-logconfiguration-logdriver"""
    p_Options: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type))),
        metadata={AttrMeta.PROPERTY_NAME: "Options"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-logconfiguration.html#cfn-ecs-taskdefinition-containerdefinition-logconfiguration-options"""
    p_SecretOptions: typing.List[typing.Union['PropTaskDefinitionSecret', dict]] = attr.ib(
        default=None,
        converter=PropTaskDefinitionSecret.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTaskDefinitionSecret), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SecretOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions-logconfiguration.html#cfn-ecs-taskdefinition-logconfiguration-secretoptions"""

@attr.s
class PropTaskDefinitionEFSVolumeConfiguration(Property):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition.EFSVolumeConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-efsvolumeconfiguration.html

    Property Document:
    
    - ``rp_FilesystemId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-efsvolumeconfiguration.html#cfn-ecs-taskdefinition-efsvolumeconfiguration-filesystemid
    - ``p_AuthorizationConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-efsvolumeconfiguration.html#cfn-ecs-taskdefinition-efsvolumeconfiguration-authorizationconfig
    - ``p_RootDirectory``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-efsvolumeconfiguration.html#cfn-ecs-taskdefinition-efsvolumeconfiguration-rootdirectory
    - ``p_TransitEncryption``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-efsvolumeconfiguration.html#cfn-ecs-taskdefinition-efsvolumeconfiguration-transitencryption
    - ``p_TransitEncryptionPort``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-efsvolumeconfiguration.html#cfn-ecs-taskdefinition-efsvolumeconfiguration-transitencryptionport
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition.EFSVolumeConfiguration"
    
    rp_FilesystemId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "FilesystemId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-efsvolumeconfiguration.html#cfn-ecs-taskdefinition-efsvolumeconfiguration-filesystemid"""
    p_AuthorizationConfig: typing.Union['PropTaskDefinitionAuthorizationConfig', dict] = attr.ib(
        default=None,
        converter=PropTaskDefinitionAuthorizationConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTaskDefinitionAuthorizationConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "AuthorizationConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-efsvolumeconfiguration.html#cfn-ecs-taskdefinition-efsvolumeconfiguration-authorizationconfig"""
    p_RootDirectory: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RootDirectory"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-efsvolumeconfiguration.html#cfn-ecs-taskdefinition-efsvolumeconfiguration-rootdirectory"""
    p_TransitEncryption: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TransitEncryption"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-efsvolumeconfiguration.html#cfn-ecs-taskdefinition-efsvolumeconfiguration-transitencryption"""
    p_TransitEncryptionPort: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "TransitEncryptionPort"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-efsvolumeconfiguration.html#cfn-ecs-taskdefinition-efsvolumeconfiguration-transitencryptionport"""

@attr.s
class PropTaskSetNetworkConfiguration(Property):
    """
    AWS Object Type = "AWS::ECS::TaskSet.NetworkConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-networkconfiguration.html

    Property Document:
    
    - ``p_AwsVpcConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-networkconfiguration.html#cfn-ecs-taskset-networkconfiguration-awsvpcconfiguration
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskSet.NetworkConfiguration"
    
    p_AwsVpcConfiguration: typing.Union['PropTaskSetAwsVpcConfiguration', dict] = attr.ib(
        default=None,
        converter=PropTaskSetAwsVpcConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTaskSetAwsVpcConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "AwsVpcConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-networkconfiguration.html#cfn-ecs-taskset-networkconfiguration-awsvpcconfiguration"""

@attr.s
class PropCapacityProviderAutoScalingGroupProvider(Property):
    """
    AWS Object Type = "AWS::ECS::CapacityProvider.AutoScalingGroupProvider"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-autoscalinggroupprovider.html

    Property Document:
    
    - ``rp_AutoScalingGroupArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-autoscalinggroupprovider.html#cfn-ecs-capacityprovider-autoscalinggroupprovider-autoscalinggrouparn
    - ``p_ManagedScaling``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-autoscalinggroupprovider.html#cfn-ecs-capacityprovider-autoscalinggroupprovider-managedscaling
    - ``p_ManagedTerminationProtection``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-autoscalinggroupprovider.html#cfn-ecs-capacityprovider-autoscalinggroupprovider-managedterminationprotection
    """
    AWS_OBJECT_TYPE = "AWS::ECS::CapacityProvider.AutoScalingGroupProvider"
    
    rp_AutoScalingGroupArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AutoScalingGroupArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-autoscalinggroupprovider.html#cfn-ecs-capacityprovider-autoscalinggroupprovider-autoscalinggrouparn"""
    p_ManagedScaling: typing.Union['PropCapacityProviderManagedScaling', dict] = attr.ib(
        default=None,
        converter=PropCapacityProviderManagedScaling.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCapacityProviderManagedScaling)),
        metadata={AttrMeta.PROPERTY_NAME: "ManagedScaling"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-autoscalinggroupprovider.html#cfn-ecs-capacityprovider-autoscalinggroupprovider-managedscaling"""
    p_ManagedTerminationProtection: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ManagedTerminationProtection"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-autoscalinggroupprovider.html#cfn-ecs-capacityprovider-autoscalinggroupprovider-managedterminationprotection"""

@attr.s
class PropServiceDeploymentConfiguration(Property):
    """
    AWS Object Type = "AWS::ECS::Service.DeploymentConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentconfiguration.html

    Property Document:
    
    - ``p_DeploymentCircuitBreaker``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentconfiguration.html#cfn-ecs-service-deploymentconfiguration-deploymentcircuitbreaker
    - ``p_MaximumPercent``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentconfiguration.html#cfn-ecs-service-deploymentconfiguration-maximumpercent
    - ``p_MinimumHealthyPercent``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentconfiguration.html#cfn-ecs-service-deploymentconfiguration-minimumhealthypercent
    """
    AWS_OBJECT_TYPE = "AWS::ECS::Service.DeploymentConfiguration"
    
    p_DeploymentCircuitBreaker: typing.Union['PropServiceDeploymentCircuitBreaker', dict] = attr.ib(
        default=None,
        converter=PropServiceDeploymentCircuitBreaker.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropServiceDeploymentCircuitBreaker)),
        metadata={AttrMeta.PROPERTY_NAME: "DeploymentCircuitBreaker"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentconfiguration.html#cfn-ecs-service-deploymentconfiguration-deploymentcircuitbreaker"""
    p_MaximumPercent: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MaximumPercent"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentconfiguration.html#cfn-ecs-service-deploymentconfiguration-maximumpercent"""
    p_MinimumHealthyPercent: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MinimumHealthyPercent"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentconfiguration.html#cfn-ecs-service-deploymentconfiguration-minimumhealthypercent"""

@attr.s
class PropTaskDefinitionVolume(Property):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition.Volume"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-volumes.html

    Property Document:
    
    - ``p_DockerVolumeConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-volumes.html#cfn-ecs-taskdefinition-volume-dockervolumeconfiguration
    - ``p_EFSVolumeConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-volumes.html#cfn-ecs-taskdefinition-volume-efsvolumeconfiguration
    - ``p_Host``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-volumes.html#cfn-ecs-taskdefinition-volumes-host
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-volumes.html#cfn-ecs-taskdefinition-volumes-name
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition.Volume"
    
    p_DockerVolumeConfiguration: typing.Union['PropTaskDefinitionDockerVolumeConfiguration', dict] = attr.ib(
        default=None,
        converter=PropTaskDefinitionDockerVolumeConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTaskDefinitionDockerVolumeConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "DockerVolumeConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-volumes.html#cfn-ecs-taskdefinition-volume-dockervolumeconfiguration"""
    p_EFSVolumeConfiguration: typing.Union['PropTaskDefinitionEFSVolumeConfiguration', dict] = attr.ib(
        default=None,
        converter=PropTaskDefinitionEFSVolumeConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTaskDefinitionEFSVolumeConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "EFSVolumeConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-volumes.html#cfn-ecs-taskdefinition-volume-efsvolumeconfiguration"""
    p_Host: typing.Union['PropTaskDefinitionHostVolumeProperties', dict] = attr.ib(
        default=None,
        converter=PropTaskDefinitionHostVolumeProperties.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTaskDefinitionHostVolumeProperties)),
        metadata={AttrMeta.PROPERTY_NAME: "Host"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-volumes.html#cfn-ecs-taskdefinition-volumes-host"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-volumes.html#cfn-ecs-taskdefinition-volumes-name"""

@attr.s
class PropTaskDefinitionContainerDefinition(Property):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition.ContainerDefinition"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html

    Property Document:
    
    - ``p_Command``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-command
    - ``p_Cpu``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-cpu
    - ``p_DependsOn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-dependson
    - ``p_DisableNetworking``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-disablenetworking
    - ``p_DnsSearchDomains``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-dnssearchdomains
    - ``p_DnsServers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-dnsservers
    - ``p_DockerLabels``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-dockerlabels
    - ``p_DockerSecurityOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-dockersecurityoptions
    - ``p_EntryPoint``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-entrypoint
    - ``p_Environment``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-environment
    - ``p_EnvironmentFiles``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-environmentfiles
    - ``p_Essential``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-essential
    - ``p_ExtraHosts``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-extrahosts
    - ``p_FirelensConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-firelensconfiguration
    - ``p_HealthCheck``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-healthcheck
    - ``p_Hostname``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-hostname
    - ``p_Image``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-image
    - ``p_Interactive``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-interactive
    - ``p_Links``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-links
    - ``p_LinuxParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-linuxparameters
    - ``p_LogConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-logconfiguration
    - ``p_Memory``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-memory
    - ``p_MemoryReservation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-memoryreservation
    - ``p_MountPoints``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-mountpoints
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-name
    - ``p_PortMappings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-portmappings
    - ``p_Privileged``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-privileged
    - ``p_PseudoTerminal``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-pseudoterminal
    - ``p_ReadonlyRootFilesystem``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-readonlyrootfilesystem
    - ``p_RepositoryCredentials``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-repositorycredentials
    - ``p_ResourceRequirements``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-resourcerequirements
    - ``p_Secrets``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-secrets
    - ``p_StartTimeout``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-starttimeout
    - ``p_StopTimeout``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-stoptimeout
    - ``p_SystemControls``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-systemcontrols
    - ``p_Ulimits``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-ulimits
    - ``p_User``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-user
    - ``p_VolumesFrom``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-volumesfrom
    - ``p_WorkingDirectory``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-workingdirectory
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition.ContainerDefinition"
    
    p_Command: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Command"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-command"""
    p_Cpu: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Cpu"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-cpu"""
    p_DependsOn: typing.List[typing.Union['PropTaskDefinitionContainerDependency', dict]] = attr.ib(
        default=None,
        converter=PropTaskDefinitionContainerDependency.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTaskDefinitionContainerDependency), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "DependsOn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-dependson"""
    p_DisableNetworking: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "DisableNetworking"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-disablenetworking"""
    p_DnsSearchDomains: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "DnsSearchDomains"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-dnssearchdomains"""
    p_DnsServers: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "DnsServers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-dnsservers"""
    p_DockerLabels: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type))),
        metadata={AttrMeta.PROPERTY_NAME: "DockerLabels"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-dockerlabels"""
    p_DockerSecurityOptions: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "DockerSecurityOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-dockersecurityoptions"""
    p_EntryPoint: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "EntryPoint"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-entrypoint"""
    p_Environment: typing.List[typing.Union['PropTaskDefinitionKeyValuePair', dict]] = attr.ib(
        default=None,
        converter=PropTaskDefinitionKeyValuePair.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTaskDefinitionKeyValuePair), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Environment"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-environment"""
    p_EnvironmentFiles: typing.List[typing.Union['PropTaskDefinitionEnvironmentFile', dict]] = attr.ib(
        default=None,
        converter=PropTaskDefinitionEnvironmentFile.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTaskDefinitionEnvironmentFile), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "EnvironmentFiles"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-environmentfiles"""
    p_Essential: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Essential"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-essential"""
    p_ExtraHosts: typing.List[typing.Union['PropTaskDefinitionHostEntry', dict]] = attr.ib(
        default=None,
        converter=PropTaskDefinitionHostEntry.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTaskDefinitionHostEntry), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ExtraHosts"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-extrahosts"""
    p_FirelensConfiguration: typing.Union['PropTaskDefinitionFirelensConfiguration', dict] = attr.ib(
        default=None,
        converter=PropTaskDefinitionFirelensConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTaskDefinitionFirelensConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "FirelensConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-firelensconfiguration"""
    p_HealthCheck: typing.Union['PropTaskDefinitionHealthCheck', dict] = attr.ib(
        default=None,
        converter=PropTaskDefinitionHealthCheck.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTaskDefinitionHealthCheck)),
        metadata={AttrMeta.PROPERTY_NAME: "HealthCheck"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-healthcheck"""
    p_Hostname: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Hostname"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-hostname"""
    p_Image: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Image"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-image"""
    p_Interactive: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Interactive"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-interactive"""
    p_Links: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Links"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-links"""
    p_LinuxParameters: typing.Union['PropTaskDefinitionLinuxParameters', dict] = attr.ib(
        default=None,
        converter=PropTaskDefinitionLinuxParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTaskDefinitionLinuxParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "LinuxParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-linuxparameters"""
    p_LogConfiguration: typing.Union['PropTaskDefinitionLogConfiguration', dict] = attr.ib(
        default=None,
        converter=PropTaskDefinitionLogConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTaskDefinitionLogConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "LogConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-logconfiguration"""
    p_Memory: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Memory"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-memory"""
    p_MemoryReservation: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MemoryReservation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-memoryreservation"""
    p_MountPoints: typing.List[typing.Union['PropTaskDefinitionMountPoint', dict]] = attr.ib(
        default=None,
        converter=PropTaskDefinitionMountPoint.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTaskDefinitionMountPoint), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "MountPoints"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-mountpoints"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-name"""
    p_PortMappings: typing.List[typing.Union['PropTaskDefinitionPortMapping', dict]] = attr.ib(
        default=None,
        converter=PropTaskDefinitionPortMapping.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTaskDefinitionPortMapping), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "PortMappings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-portmappings"""
    p_Privileged: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Privileged"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-privileged"""
    p_PseudoTerminal: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "PseudoTerminal"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-pseudoterminal"""
    p_ReadonlyRootFilesystem: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "ReadonlyRootFilesystem"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-readonlyrootfilesystem"""
    p_RepositoryCredentials: typing.Union['PropTaskDefinitionRepositoryCredentials', dict] = attr.ib(
        default=None,
        converter=PropTaskDefinitionRepositoryCredentials.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTaskDefinitionRepositoryCredentials)),
        metadata={AttrMeta.PROPERTY_NAME: "RepositoryCredentials"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-repositorycredentials"""
    p_ResourceRequirements: typing.List[typing.Union['PropTaskDefinitionResourceRequirement', dict]] = attr.ib(
        default=None,
        converter=PropTaskDefinitionResourceRequirement.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTaskDefinitionResourceRequirement), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceRequirements"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-resourcerequirements"""
    p_Secrets: typing.List[typing.Union['PropTaskDefinitionSecret', dict]] = attr.ib(
        default=None,
        converter=PropTaskDefinitionSecret.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTaskDefinitionSecret), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Secrets"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-secrets"""
    p_StartTimeout: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "StartTimeout"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-starttimeout"""
    p_StopTimeout: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "StopTimeout"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-stoptimeout"""
    p_SystemControls: typing.List[typing.Union['PropTaskDefinitionSystemControl', dict]] = attr.ib(
        default=None,
        converter=PropTaskDefinitionSystemControl.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTaskDefinitionSystemControl), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SystemControls"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-systemcontrols"""
    p_Ulimits: typing.List[typing.Union['PropTaskDefinitionUlimit', dict]] = attr.ib(
        default=None,
        converter=PropTaskDefinitionUlimit.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTaskDefinitionUlimit), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Ulimits"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-ulimits"""
    p_User: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "User"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-user"""
    p_VolumesFrom: typing.List[typing.Union['PropTaskDefinitionVolumeFrom', dict]] = attr.ib(
        default=None,
        converter=PropTaskDefinitionVolumeFrom.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTaskDefinitionVolumeFrom), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "VolumesFrom"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-volumesfrom"""
    p_WorkingDirectory: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "WorkingDirectory"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-containerdefinitions.html#cfn-ecs-taskdefinition-containerdefinition-workingdirectory"""


#--- Resource declaration ---

@attr.s
class Cluster(Resource):
    """
    AWS Object Type = "AWS::ECS::Cluster"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html

    Property Document:
    
    - ``p_CapacityProviders``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html#cfn-ecs-cluster-capacityproviders
    - ``p_ClusterName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html#cfn-ecs-cluster-clustername
    - ``p_ClusterSettings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html#cfn-ecs-cluster-clustersettings
    - ``p_Configuration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html#cfn-ecs-cluster-configuration
    - ``p_DefaultCapacityProviderStrategy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html#cfn-ecs-cluster-defaultcapacityproviderstrategy
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html#cfn-ecs-cluster-tags
    """
    AWS_OBJECT_TYPE = "AWS::ECS::Cluster"

    
    p_CapacityProviders: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "CapacityProviders"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html#cfn-ecs-cluster-capacityproviders"""
    p_ClusterName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ClusterName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html#cfn-ecs-cluster-clustername"""
    p_ClusterSettings: typing.List[typing.Union['PropClusterClusterSettings', dict]] = attr.ib(
        default=None,
        converter=PropClusterClusterSettings.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropClusterClusterSettings), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ClusterSettings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html#cfn-ecs-cluster-clustersettings"""
    p_Configuration: typing.Union['PropClusterClusterConfiguration', dict] = attr.ib(
        default=None,
        converter=PropClusterClusterConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropClusterClusterConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "Configuration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html#cfn-ecs-cluster-configuration"""
    p_DefaultCapacityProviderStrategy: typing.List[typing.Union['PropClusterCapacityProviderStrategyItem', dict]] = attr.ib(
        default=None,
        converter=PropClusterCapacityProviderStrategyItem.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropClusterCapacityProviderStrategyItem), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultCapacityProviderStrategy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html#cfn-ecs-cluster-defaultcapacityproviderstrategy"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html#cfn-ecs-cluster-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html#aws-resource-ecs-cluster-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class Service(Resource):
    """
    AWS Object Type = "AWS::ECS::Service"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html

    Property Document:
    
    - ``p_CapacityProviderStrategy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-capacityproviderstrategy
    - ``p_Cluster``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-cluster
    - ``p_DeploymentConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-deploymentconfiguration
    - ``p_DeploymentController``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-deploymentcontroller
    - ``p_DesiredCount``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-desiredcount
    - ``p_EnableECSManagedTags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-enableecsmanagedtags
    - ``p_EnableExecuteCommand``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-enableexecutecommand
    - ``p_HealthCheckGracePeriodSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-healthcheckgraceperiodseconds
    - ``p_LaunchType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-launchtype
    - ``p_LoadBalancers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-loadbalancers
    - ``p_NetworkConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-networkconfiguration
    - ``p_PlacementConstraints``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-placementconstraints
    - ``p_PlacementStrategies``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-placementstrategies
    - ``p_PlatformVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-platformversion
    - ``p_PropagateTags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-propagatetags
    - ``p_Role``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-role
    - ``p_SchedulingStrategy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-schedulingstrategy
    - ``p_ServiceName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-servicename
    - ``p_ServiceRegistries``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-serviceregistries
    - ``p_TaskDefinition``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-taskdefinition
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-tags
    """
    AWS_OBJECT_TYPE = "AWS::ECS::Service"

    
    p_CapacityProviderStrategy: typing.List[typing.Union['PropServiceCapacityProviderStrategyItem', dict]] = attr.ib(
        default=None,
        converter=PropServiceCapacityProviderStrategyItem.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropServiceCapacityProviderStrategyItem), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "CapacityProviderStrategy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-capacityproviderstrategy"""
    p_Cluster: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Cluster"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-cluster"""
    p_DeploymentConfiguration: typing.Union['PropServiceDeploymentConfiguration', dict] = attr.ib(
        default=None,
        converter=PropServiceDeploymentConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropServiceDeploymentConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "DeploymentConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-deploymentconfiguration"""
    p_DeploymentController: typing.Union['PropServiceDeploymentController', dict] = attr.ib(
        default=None,
        converter=PropServiceDeploymentController.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropServiceDeploymentController)),
        metadata={AttrMeta.PROPERTY_NAME: "DeploymentController"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-deploymentcontroller"""
    p_DesiredCount: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "DesiredCount"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-desiredcount"""
    p_EnableECSManagedTags: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EnableECSManagedTags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-enableecsmanagedtags"""
    p_EnableExecuteCommand: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EnableExecuteCommand"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-enableexecutecommand"""
    p_HealthCheckGracePeriodSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "HealthCheckGracePeriodSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-healthcheckgraceperiodseconds"""
    p_LaunchType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LaunchType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-launchtype"""
    p_LoadBalancers: typing.List[typing.Union['PropServiceLoadBalancer', dict]] = attr.ib(
        default=None,
        converter=PropServiceLoadBalancer.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropServiceLoadBalancer), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "LoadBalancers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-loadbalancers"""
    p_NetworkConfiguration: typing.Union['PropServiceNetworkConfiguration', dict] = attr.ib(
        default=None,
        converter=PropServiceNetworkConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropServiceNetworkConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "NetworkConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-networkconfiguration"""
    p_PlacementConstraints: typing.List[typing.Union['PropServicePlacementConstraint', dict]] = attr.ib(
        default=None,
        converter=PropServicePlacementConstraint.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropServicePlacementConstraint), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "PlacementConstraints"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-placementconstraints"""
    p_PlacementStrategies: typing.List[typing.Union['PropServicePlacementStrategy', dict]] = attr.ib(
        default=None,
        converter=PropServicePlacementStrategy.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropServicePlacementStrategy), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "PlacementStrategies"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-placementstrategies"""
    p_PlatformVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PlatformVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-platformversion"""
    p_PropagateTags: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PropagateTags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-propagatetags"""
    p_Role: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Role"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-role"""
    p_SchedulingStrategy: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SchedulingStrategy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-schedulingstrategy"""
    p_ServiceName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ServiceName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-servicename"""
    p_ServiceRegistries: typing.List[typing.Union['PropServiceServiceRegistry', dict]] = attr.ib(
        default=None,
        converter=PropServiceServiceRegistry.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropServiceServiceRegistry), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ServiceRegistries"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-serviceregistries"""
    p_TaskDefinition: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TaskDefinition"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-taskdefinition"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-tags"""

    
    @property
    def rv_ServiceArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#aws-resource-ecs-service-return-values"""
        return GetAtt(resource=self, attr_name="ServiceArn")
    
    @property
    def rv_Name(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#aws-resource-ecs-service-return-values"""
        return GetAtt(resource=self, attr_name="Name")
    

@attr.s
class ClusterCapacityProviderAssociations(Resource):
    """
    AWS Object Type = "AWS::ECS::ClusterCapacityProviderAssociations"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-clustercapacityproviderassociations.html

    Property Document:
    
    - ``rp_CapacityProviders``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-clustercapacityproviderassociations.html#cfn-ecs-clustercapacityproviderassociations-capacityproviders
    - ``rp_Cluster``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-clustercapacityproviderassociations.html#cfn-ecs-clustercapacityproviderassociations-cluster
    - ``rp_DefaultCapacityProviderStrategy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-clustercapacityproviderassociations.html#cfn-ecs-clustercapacityproviderassociations-defaultcapacityproviderstrategy
    """
    AWS_OBJECT_TYPE = "AWS::ECS::ClusterCapacityProviderAssociations"

    
    rp_CapacityProviders: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "CapacityProviders"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-clustercapacityproviderassociations.html#cfn-ecs-clustercapacityproviderassociations-capacityproviders"""
    rp_Cluster: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Cluster"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-clustercapacityproviderassociations.html#cfn-ecs-clustercapacityproviderassociations-cluster"""
    rp_DefaultCapacityProviderStrategy: typing.List[typing.Union['PropClusterCapacityProviderAssociationsCapacityProviderStrategy', dict]] = attr.ib(
        default=None,
        converter=PropClusterCapacityProviderAssociationsCapacityProviderStrategy.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropClusterCapacityProviderAssociationsCapacityProviderStrategy), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultCapacityProviderStrategy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-clustercapacityproviderassociations.html#cfn-ecs-clustercapacityproviderassociations-defaultcapacityproviderstrategy"""

    

@attr.s
class TaskDefinition(Resource):
    """
    AWS Object Type = "AWS::ECS::TaskDefinition"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html

    Property Document:
    
    - ``p_ContainerDefinitions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-containerdefinitions
    - ``p_Cpu``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-cpu
    - ``p_EphemeralStorage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-ephemeralstorage
    - ``p_ExecutionRoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-executionrolearn
    - ``p_Family``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-family
    - ``p_InferenceAccelerators``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-inferenceaccelerators
    - ``p_IpcMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-ipcmode
    - ``p_Memory``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-memory
    - ``p_NetworkMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-networkmode
    - ``p_PidMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-pidmode
    - ``p_PlacementConstraints``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-placementconstraints
    - ``p_ProxyConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-proxyconfiguration
    - ``p_RequiresCompatibilities``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-requirescompatibilities
    - ``p_RuntimePlatform``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-runtimeplatform
    - ``p_TaskRoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-taskrolearn
    - ``p_Volumes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-volumes
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-tags
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskDefinition"

    
    p_ContainerDefinitions: typing.List[typing.Union['PropTaskDefinitionContainerDefinition', dict]] = attr.ib(
        default=None,
        converter=PropTaskDefinitionContainerDefinition.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTaskDefinitionContainerDefinition), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ContainerDefinitions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-containerdefinitions"""
    p_Cpu: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Cpu"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-cpu"""
    p_EphemeralStorage: typing.Union['PropTaskDefinitionEphemeralStorage', dict] = attr.ib(
        default=None,
        converter=PropTaskDefinitionEphemeralStorage.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTaskDefinitionEphemeralStorage)),
        metadata={AttrMeta.PROPERTY_NAME: "EphemeralStorage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-ephemeralstorage"""
    p_ExecutionRoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ExecutionRoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-executionrolearn"""
    p_Family: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Family"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-family"""
    p_InferenceAccelerators: typing.List[typing.Union['PropTaskDefinitionInferenceAccelerator', dict]] = attr.ib(
        default=None,
        converter=PropTaskDefinitionInferenceAccelerator.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTaskDefinitionInferenceAccelerator), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "InferenceAccelerators"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-inferenceaccelerators"""
    p_IpcMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "IpcMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-ipcmode"""
    p_Memory: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Memory"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-memory"""
    p_NetworkMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "NetworkMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-networkmode"""
    p_PidMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PidMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-pidmode"""
    p_PlacementConstraints: typing.List[typing.Union['PropTaskDefinitionTaskDefinitionPlacementConstraint', dict]] = attr.ib(
        default=None,
        converter=PropTaskDefinitionTaskDefinitionPlacementConstraint.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTaskDefinitionTaskDefinitionPlacementConstraint), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "PlacementConstraints"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-placementconstraints"""
    p_ProxyConfiguration: typing.Union['PropTaskDefinitionProxyConfiguration', dict] = attr.ib(
        default=None,
        converter=PropTaskDefinitionProxyConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTaskDefinitionProxyConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "ProxyConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-proxyconfiguration"""
    p_RequiresCompatibilities: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "RequiresCompatibilities"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-requirescompatibilities"""
    p_RuntimePlatform: typing.Union['PropTaskDefinitionRuntimePlatform', dict] = attr.ib(
        default=None,
        converter=PropTaskDefinitionRuntimePlatform.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTaskDefinitionRuntimePlatform)),
        metadata={AttrMeta.PROPERTY_NAME: "RuntimePlatform"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-runtimeplatform"""
    p_TaskRoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TaskRoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-taskrolearn"""
    p_Volumes: typing.List[typing.Union['PropTaskDefinitionVolume', dict]] = attr.ib(
        default=None,
        converter=PropTaskDefinitionVolume.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTaskDefinitionVolume), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Volumes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-volumes"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#cfn-ecs-taskdefinition-tags"""

    
    @property
    def rv_TaskDefinitionArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html#aws-resource-ecs-taskdefinition-return-values"""
        return GetAtt(resource=self, attr_name="TaskDefinitionArn")
    

@attr.s
class CapacityProvider(Resource):
    """
    AWS Object Type = "AWS::ECS::CapacityProvider"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-capacityprovider.html

    Property Document:
    
    - ``rp_AutoScalingGroupProvider``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-capacityprovider.html#cfn-ecs-capacityprovider-autoscalinggroupprovider
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-capacityprovider.html#cfn-ecs-capacityprovider-name
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-capacityprovider.html#cfn-ecs-capacityprovider-tags
    """
    AWS_OBJECT_TYPE = "AWS::ECS::CapacityProvider"

    
    rp_AutoScalingGroupProvider: typing.Union['PropCapacityProviderAutoScalingGroupProvider', dict] = attr.ib(
        default=None,
        converter=PropCapacityProviderAutoScalingGroupProvider.from_dict,
        validator=attr.validators.instance_of(PropCapacityProviderAutoScalingGroupProvider),
        metadata={AttrMeta.PROPERTY_NAME: "AutoScalingGroupProvider"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-capacityprovider.html#cfn-ecs-capacityprovider-autoscalinggroupprovider"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-capacityprovider.html#cfn-ecs-capacityprovider-name"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-capacityprovider.html#cfn-ecs-capacityprovider-tags"""

    

@attr.s
class PrimaryTaskSet(Resource):
    """
    AWS Object Type = "AWS::ECS::PrimaryTaskSet"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-primarytaskset.html

    Property Document:
    
    - ``rp_Cluster``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-primarytaskset.html#cfn-ecs-primarytaskset-cluster
    - ``rp_Service``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-primarytaskset.html#cfn-ecs-primarytaskset-service
    - ``rp_TaskSetId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-primarytaskset.html#cfn-ecs-primarytaskset-tasksetid
    """
    AWS_OBJECT_TYPE = "AWS::ECS::PrimaryTaskSet"

    
    rp_Cluster: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Cluster"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-primarytaskset.html#cfn-ecs-primarytaskset-cluster"""
    rp_Service: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Service"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-primarytaskset.html#cfn-ecs-primarytaskset-service"""
    rp_TaskSetId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TaskSetId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-primarytaskset.html#cfn-ecs-primarytaskset-tasksetid"""

    

@attr.s
class TaskSet(Resource):
    """
    AWS Object Type = "AWS::ECS::TaskSet"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html

    Property Document:
    
    - ``rp_Cluster``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#cfn-ecs-taskset-cluster
    - ``rp_Service``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#cfn-ecs-taskset-service
    - ``rp_TaskDefinition``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#cfn-ecs-taskset-taskdefinition
    - ``p_ExternalId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#cfn-ecs-taskset-externalid
    - ``p_LaunchType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#cfn-ecs-taskset-launchtype
    - ``p_LoadBalancers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#cfn-ecs-taskset-loadbalancers
    - ``p_NetworkConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#cfn-ecs-taskset-networkconfiguration
    - ``p_PlatformVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#cfn-ecs-taskset-platformversion
    - ``p_Scale``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#cfn-ecs-taskset-scale
    - ``p_ServiceRegistries``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#cfn-ecs-taskset-serviceregistries
    """
    AWS_OBJECT_TYPE = "AWS::ECS::TaskSet"

    
    rp_Cluster: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Cluster"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#cfn-ecs-taskset-cluster"""
    rp_Service: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Service"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#cfn-ecs-taskset-service"""
    rp_TaskDefinition: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TaskDefinition"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#cfn-ecs-taskset-taskdefinition"""
    p_ExternalId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ExternalId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#cfn-ecs-taskset-externalid"""
    p_LaunchType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LaunchType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#cfn-ecs-taskset-launchtype"""
    p_LoadBalancers: typing.List[typing.Union['PropTaskSetLoadBalancer', dict]] = attr.ib(
        default=None,
        converter=PropTaskSetLoadBalancer.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTaskSetLoadBalancer), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "LoadBalancers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#cfn-ecs-taskset-loadbalancers"""
    p_NetworkConfiguration: typing.Union['PropTaskSetNetworkConfiguration', dict] = attr.ib(
        default=None,
        converter=PropTaskSetNetworkConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTaskSetNetworkConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "NetworkConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#cfn-ecs-taskset-networkconfiguration"""
    p_PlatformVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PlatformVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#cfn-ecs-taskset-platformversion"""
    p_Scale: typing.Union['PropTaskSetScale', dict] = attr.ib(
        default=None,
        converter=PropTaskSetScale.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTaskSetScale)),
        metadata={AttrMeta.PROPERTY_NAME: "Scale"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#cfn-ecs-taskset-scale"""
    p_ServiceRegistries: typing.List[typing.Union['PropTaskSetServiceRegistry', dict]] = attr.ib(
        default=None,
        converter=PropTaskSetServiceRegistry.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTaskSetServiceRegistry), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ServiceRegistries"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#cfn-ecs-taskset-serviceregistries"""

    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html#aws-resource-ecs-taskset-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
