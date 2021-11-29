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
class PropDeploymentTags(Property):
    """
    AWS Object Type = "AWS::AppConfig::Deployment.Tags"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deployment-tags.html

    Property Document:
    
    - ``p_Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deployment-tags.html#cfn-appconfig-deployment-tags-key
    - ``p_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deployment-tags.html#cfn-appconfig-deployment-tags-value
    """
    AWS_OBJECT_TYPE = "AWS::AppConfig::Deployment.Tags"
    
    p_Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deployment-tags.html#cfn-appconfig-deployment-tags-key"""
    p_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deployment-tags.html#cfn-appconfig-deployment-tags-value"""

@attr.s
class PropDeploymentStrategyTags(Property):
    """
    AWS Object Type = "AWS::AppConfig::DeploymentStrategy.Tags"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deploymentstrategy-tags.html

    Property Document:
    
    - ``p_Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deploymentstrategy-tags.html#cfn-appconfig-deploymentstrategy-tags-key
    - ``p_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deploymentstrategy-tags.html#cfn-appconfig-deploymentstrategy-tags-value
    """
    AWS_OBJECT_TYPE = "AWS::AppConfig::DeploymentStrategy.Tags"
    
    p_Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deploymentstrategy-tags.html#cfn-appconfig-deploymentstrategy-tags-key"""
    p_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deploymentstrategy-tags.html#cfn-appconfig-deploymentstrategy-tags-value"""

@attr.s
class PropEnvironmentMonitors(Property):
    """
    AWS Object Type = "AWS::AppConfig::Environment.Monitors"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-monitors.html

    Property Document:
    
    - ``p_AlarmArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-monitors.html#cfn-appconfig-environment-monitors-alarmarn
    - ``p_AlarmRoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-monitors.html#cfn-appconfig-environment-monitors-alarmrolearn
    """
    AWS_OBJECT_TYPE = "AWS::AppConfig::Environment.Monitors"
    
    p_AlarmArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AlarmArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-monitors.html#cfn-appconfig-environment-monitors-alarmarn"""
    p_AlarmRoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AlarmRoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-monitors.html#cfn-appconfig-environment-monitors-alarmrolearn"""

@attr.s
class PropEnvironmentTags(Property):
    """
    AWS Object Type = "AWS::AppConfig::Environment.Tags"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-tags.html

    Property Document:
    
    - ``p_Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-tags.html#cfn-appconfig-environment-tags-key
    - ``p_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-tags.html#cfn-appconfig-environment-tags-value
    """
    AWS_OBJECT_TYPE = "AWS::AppConfig::Environment.Tags"
    
    p_Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-tags.html#cfn-appconfig-environment-tags-key"""
    p_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-tags.html#cfn-appconfig-environment-tags-value"""

@attr.s
class PropConfigurationProfileValidators(Property):
    """
    AWS Object Type = "AWS::AppConfig::ConfigurationProfile.Validators"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-validators.html

    Property Document:
    
    - ``p_Content``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-validators.html#cfn-appconfig-configurationprofile-validators-content
    - ``p_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-validators.html#cfn-appconfig-configurationprofile-validators-type
    """
    AWS_OBJECT_TYPE = "AWS::AppConfig::ConfigurationProfile.Validators"
    
    p_Content: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Content"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-validators.html#cfn-appconfig-configurationprofile-validators-content"""
    p_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-validators.html#cfn-appconfig-configurationprofile-validators-type"""

@attr.s
class PropApplicationTags(Property):
    """
    AWS Object Type = "AWS::AppConfig::Application.Tags"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-application-tags.html

    Property Document:
    
    - ``p_Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-application-tags.html#cfn-appconfig-application-tags-key
    - ``p_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-application-tags.html#cfn-appconfig-application-tags-value
    """
    AWS_OBJECT_TYPE = "AWS::AppConfig::Application.Tags"
    
    p_Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-application-tags.html#cfn-appconfig-application-tags-key"""
    p_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-application-tags.html#cfn-appconfig-application-tags-value"""

@attr.s
class PropConfigurationProfileTags(Property):
    """
    AWS Object Type = "AWS::AppConfig::ConfigurationProfile.Tags"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-tags.html

    Property Document:
    
    - ``p_Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-tags.html#cfn-appconfig-configurationprofile-tags-key
    - ``p_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-tags.html#cfn-appconfig-configurationprofile-tags-value
    """
    AWS_OBJECT_TYPE = "AWS::AppConfig::ConfigurationProfile.Tags"
    
    p_Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-tags.html#cfn-appconfig-configurationprofile-tags-key"""
    p_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-tags.html#cfn-appconfig-configurationprofile-tags-value"""


#--- Resource declaration ---

@attr.s
class Environment(Resource):
    """
    AWS Object Type = "AWS::AppConfig::Environment"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html

    Property Document:
    
    - ``rp_ApplicationId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-applicationid
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-name
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-description
    - ``p_Monitors``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-monitors
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-tags
    """
    AWS_OBJECT_TYPE = "AWS::AppConfig::Environment"

    
    rp_ApplicationId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-applicationid"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-name"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-description"""
    p_Monitors: typing.List[typing.Union['PropEnvironmentMonitors', dict]] = attr.ib(
        default=None,
        converter=PropEnvironmentMonitors.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropEnvironmentMonitors), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Monitors"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-monitors"""
    p_Tags: typing.List[typing.Union['PropEnvironmentTags', dict]] = attr.ib(
        default=None,
        converter=PropEnvironmentTags.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropEnvironmentTags), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-tags"""

    

@attr.s
class DeploymentStrategy(Resource):
    """
    AWS Object Type = "AWS::AppConfig::DeploymentStrategy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html

    Property Document:
    
    - ``rp_DeploymentDurationInMinutes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-deploymentdurationinminutes
    - ``rp_GrowthFactor``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-growthfactor
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-name
    - ``rp_ReplicateTo``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-replicateto
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-description
    - ``p_FinalBakeTimeInMinutes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-finalbaketimeinminutes
    - ``p_GrowthType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-growthtype
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-tags
    """
    AWS_OBJECT_TYPE = "AWS::AppConfig::DeploymentStrategy"

    
    rp_DeploymentDurationInMinutes: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "DeploymentDurationInMinutes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-deploymentdurationinminutes"""
    rp_GrowthFactor: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "GrowthFactor"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-growthfactor"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-name"""
    rp_ReplicateTo: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ReplicateTo"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-replicateto"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-description"""
    p_FinalBakeTimeInMinutes: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "FinalBakeTimeInMinutes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-finalbaketimeinminutes"""
    p_GrowthType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "GrowthType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-growthtype"""
    p_Tags: typing.List[typing.Union['PropDeploymentStrategyTags', dict]] = attr.ib(
        default=None,
        converter=PropDeploymentStrategyTags.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDeploymentStrategyTags), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-tags"""

    

@attr.s
class Deployment(Resource):
    """
    AWS Object Type = "AWS::AppConfig::Deployment"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html

    Property Document:
    
    - ``rp_ApplicationId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-applicationid
    - ``rp_ConfigurationProfileId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-configurationprofileid
    - ``rp_ConfigurationVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-configurationversion
    - ``rp_DeploymentStrategyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-deploymentstrategyid
    - ``rp_EnvironmentId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-environmentid
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-description
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-tags
    """
    AWS_OBJECT_TYPE = "AWS::AppConfig::Deployment"

    
    rp_ApplicationId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-applicationid"""
    rp_ConfigurationProfileId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ConfigurationProfileId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-configurationprofileid"""
    rp_ConfigurationVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ConfigurationVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-configurationversion"""
    rp_DeploymentStrategyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DeploymentStrategyId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-deploymentstrategyid"""
    rp_EnvironmentId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "EnvironmentId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-environmentid"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-description"""
    p_Tags: typing.List[typing.Union['PropDeploymentTags', dict]] = attr.ib(
        default=None,
        converter=PropDeploymentTags.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDeploymentTags), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-tags"""

    

@attr.s
class HostedConfigurationVersion(Resource):
    """
    AWS Object Type = "AWS::AppConfig::HostedConfigurationVersion"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html

    Property Document:
    
    - ``rp_ApplicationId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-applicationid
    - ``rp_ConfigurationProfileId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-configurationprofileid
    - ``rp_Content``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-content
    - ``rp_ContentType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-contenttype
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-description
    - ``p_LatestVersionNumber``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-latestversionnumber
    """
    AWS_OBJECT_TYPE = "AWS::AppConfig::HostedConfigurationVersion"

    
    rp_ApplicationId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-applicationid"""
    rp_ConfigurationProfileId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ConfigurationProfileId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-configurationprofileid"""
    rp_Content: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Content"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-content"""
    rp_ContentType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ContentType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-contenttype"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-description"""
    p_LatestVersionNumber: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "LatestVersionNumber"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-latestversionnumber"""

    

@attr.s
class ConfigurationProfile(Resource):
    """
    AWS Object Type = "AWS::AppConfig::ConfigurationProfile"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html

    Property Document:
    
    - ``rp_ApplicationId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-applicationid
    - ``rp_LocationUri``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-locationuri
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-name
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-description
    - ``p_RetrievalRoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-retrievalrolearn
    - ``p_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-type
    - ``p_Validators``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-validators
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-tags
    """
    AWS_OBJECT_TYPE = "AWS::AppConfig::ConfigurationProfile"

    
    rp_ApplicationId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-applicationid"""
    rp_LocationUri: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "LocationUri"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-locationuri"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-name"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-description"""
    p_RetrievalRoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RetrievalRoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-retrievalrolearn"""
    p_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-type"""
    p_Validators: typing.List[typing.Union['PropConfigurationProfileValidators', dict]] = attr.ib(
        default=None,
        converter=PropConfigurationProfileValidators.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropConfigurationProfileValidators), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Validators"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-validators"""
    p_Tags: typing.List[typing.Union['PropConfigurationProfileTags', dict]] = attr.ib(
        default=None,
        converter=PropConfigurationProfileTags.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropConfigurationProfileTags), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-tags"""

    

@attr.s
class Application(Resource):
    """
    AWS Object Type = "AWS::AppConfig::Application"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html#cfn-appconfig-application-name
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html#cfn-appconfig-application-description
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html#cfn-appconfig-application-tags
    """
    AWS_OBJECT_TYPE = "AWS::AppConfig::Application"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html#cfn-appconfig-application-name"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html#cfn-appconfig-application-description"""
    p_Tags: typing.List[typing.Union['PropApplicationTags', dict]] = attr.ib(
        default=None,
        converter=PropApplicationTags.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropApplicationTags), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html#cfn-appconfig-application-tags"""

    
