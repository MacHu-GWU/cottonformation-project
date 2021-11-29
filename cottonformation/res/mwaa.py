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
class PropEnvironmentNetworkConfiguration(Property):
    """
    AWS Object Type = "AWS::MWAA::Environment.NetworkConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-networkconfiguration.html

    Property Document:
    
    - ``p_SecurityGroupIds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-networkconfiguration.html#cfn-mwaa-environment-networkconfiguration-securitygroupids
    - ``p_SubnetIds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-networkconfiguration.html#cfn-mwaa-environment-networkconfiguration-subnetids
    """
    AWS_OBJECT_TYPE = "AWS::MWAA::Environment.NetworkConfiguration"
    
    p_SecurityGroupIds: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SecurityGroupIds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-networkconfiguration.html#cfn-mwaa-environment-networkconfiguration-securitygroupids"""
    p_SubnetIds: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SubnetIds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-networkconfiguration.html#cfn-mwaa-environment-networkconfiguration-subnetids"""

@attr.s
class PropEnvironmentModuleLoggingConfiguration(Property):
    """
    AWS Object Type = "AWS::MWAA::Environment.ModuleLoggingConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-moduleloggingconfiguration.html

    Property Document:
    
    - ``p_CloudWatchLogGroupArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-moduleloggingconfiguration.html#cfn-mwaa-environment-moduleloggingconfiguration-cloudwatchloggrouparn
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-moduleloggingconfiguration.html#cfn-mwaa-environment-moduleloggingconfiguration-enabled
    - ``p_LogLevel``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-moduleloggingconfiguration.html#cfn-mwaa-environment-moduleloggingconfiguration-loglevel
    """
    AWS_OBJECT_TYPE = "AWS::MWAA::Environment.ModuleLoggingConfiguration"
    
    p_CloudWatchLogGroupArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CloudWatchLogGroupArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-moduleloggingconfiguration.html#cfn-mwaa-environment-moduleloggingconfiguration-cloudwatchloggrouparn"""
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-moduleloggingconfiguration.html#cfn-mwaa-environment-moduleloggingconfiguration-enabled"""
    p_LogLevel: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LogLevel"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-moduleloggingconfiguration.html#cfn-mwaa-environment-moduleloggingconfiguration-loglevel"""

@attr.s
class PropEnvironmentLoggingConfiguration(Property):
    """
    AWS Object Type = "AWS::MWAA::Environment.LoggingConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html

    Property Document:
    
    - ``p_DagProcessingLogs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html#cfn-mwaa-environment-loggingconfiguration-dagprocessinglogs
    - ``p_SchedulerLogs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html#cfn-mwaa-environment-loggingconfiguration-schedulerlogs
    - ``p_TaskLogs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html#cfn-mwaa-environment-loggingconfiguration-tasklogs
    - ``p_WebserverLogs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html#cfn-mwaa-environment-loggingconfiguration-webserverlogs
    - ``p_WorkerLogs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html#cfn-mwaa-environment-loggingconfiguration-workerlogs
    """
    AWS_OBJECT_TYPE = "AWS::MWAA::Environment.LoggingConfiguration"
    
    p_DagProcessingLogs: typing.Union['PropEnvironmentModuleLoggingConfiguration', dict] = attr.ib(
        default=None,
        converter=PropEnvironmentModuleLoggingConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropEnvironmentModuleLoggingConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "DagProcessingLogs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html#cfn-mwaa-environment-loggingconfiguration-dagprocessinglogs"""
    p_SchedulerLogs: typing.Union['PropEnvironmentModuleLoggingConfiguration', dict] = attr.ib(
        default=None,
        converter=PropEnvironmentModuleLoggingConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropEnvironmentModuleLoggingConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "SchedulerLogs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html#cfn-mwaa-environment-loggingconfiguration-schedulerlogs"""
    p_TaskLogs: typing.Union['PropEnvironmentModuleLoggingConfiguration', dict] = attr.ib(
        default=None,
        converter=PropEnvironmentModuleLoggingConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropEnvironmentModuleLoggingConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "TaskLogs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html#cfn-mwaa-environment-loggingconfiguration-tasklogs"""
    p_WebserverLogs: typing.Union['PropEnvironmentModuleLoggingConfiguration', dict] = attr.ib(
        default=None,
        converter=PropEnvironmentModuleLoggingConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropEnvironmentModuleLoggingConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "WebserverLogs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html#cfn-mwaa-environment-loggingconfiguration-webserverlogs"""
    p_WorkerLogs: typing.Union['PropEnvironmentModuleLoggingConfiguration', dict] = attr.ib(
        default=None,
        converter=PropEnvironmentModuleLoggingConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropEnvironmentModuleLoggingConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "WorkerLogs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html#cfn-mwaa-environment-loggingconfiguration-workerlogs"""


#--- Resource declaration ---

@attr.s
class Environment(Resource):
    """
    AWS Object Type = "AWS::MWAA::Environment"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-name
    - ``p_AirflowConfigurationOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-airflowconfigurationoptions
    - ``p_AirflowVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-airflowversion
    - ``p_DagS3Path``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-dags3path
    - ``p_EnvironmentClass``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-environmentclass
    - ``p_ExecutionRoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-executionrolearn
    - ``p_KmsKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-kmskey
    - ``p_LoggingConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-loggingconfiguration
    - ``p_MaxWorkers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-maxworkers
    - ``p_MinWorkers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-minworkers
    - ``p_NetworkConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-networkconfiguration
    - ``p_PluginsS3ObjectVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-pluginss3objectversion
    - ``p_PluginsS3Path``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-pluginss3path
    - ``p_RequirementsS3ObjectVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-requirementss3objectversion
    - ``p_RequirementsS3Path``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-requirementss3path
    - ``p_Schedulers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-schedulers
    - ``p_SourceBucketArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-sourcebucketarn
    - ``p_WebserverAccessMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-webserveraccessmode
    - ``p_WeeklyMaintenanceWindowStart``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-weeklymaintenancewindowstart
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-tags
    """
    AWS_OBJECT_TYPE = "AWS::MWAA::Environment"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-name"""
    p_AirflowConfigurationOptions: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "AirflowConfigurationOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-airflowconfigurationoptions"""
    p_AirflowVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AirflowVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-airflowversion"""
    p_DagS3Path: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DagS3Path"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-dags3path"""
    p_EnvironmentClass: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "EnvironmentClass"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-environmentclass"""
    p_ExecutionRoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ExecutionRoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-executionrolearn"""
    p_KmsKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "KmsKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-kmskey"""
    p_LoggingConfiguration: typing.Union['PropEnvironmentLoggingConfiguration', dict] = attr.ib(
        default=None,
        converter=PropEnvironmentLoggingConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropEnvironmentLoggingConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "LoggingConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-loggingconfiguration"""
    p_MaxWorkers: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MaxWorkers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-maxworkers"""
    p_MinWorkers: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MinWorkers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-minworkers"""
    p_NetworkConfiguration: typing.Union['PropEnvironmentNetworkConfiguration', dict] = attr.ib(
        default=None,
        converter=PropEnvironmentNetworkConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropEnvironmentNetworkConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "NetworkConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-networkconfiguration"""
    p_PluginsS3ObjectVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PluginsS3ObjectVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-pluginss3objectversion"""
    p_PluginsS3Path: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PluginsS3Path"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-pluginss3path"""
    p_RequirementsS3ObjectVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RequirementsS3ObjectVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-requirementss3objectversion"""
    p_RequirementsS3Path: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RequirementsS3Path"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-requirementss3path"""
    p_Schedulers: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Schedulers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-schedulers"""
    p_SourceBucketArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SourceBucketArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-sourcebucketarn"""
    p_WebserverAccessMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "WebserverAccessMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-webserveraccessmode"""
    p_WeeklyMaintenanceWindowStart: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "WeeklyMaintenanceWindowStart"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-weeklymaintenancewindowstart"""
    p_Tags: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#aws-resource-mwaa-environment-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_WebserverUrl(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#aws-resource-mwaa-environment-return-values"""
        return GetAtt(resource=self, attr_name="WebserverUrl")
    
    @property
    def rv_LoggingConfigurationDagProcessingLogsCloudWatchLogGroupArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#aws-resource-mwaa-environment-return-values"""
        return GetAtt(resource=self, attr_name="LoggingConfiguration.DagProcessingLogs.CloudWatchLogGroupArn")
    
    @property
    def rv_LoggingConfigurationSchedulerLogsCloudWatchLogGroupArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#aws-resource-mwaa-environment-return-values"""
        return GetAtt(resource=self, attr_name="LoggingConfiguration.SchedulerLogs.CloudWatchLogGroupArn")
    
    @property
    def rv_LoggingConfigurationWebserverLogsCloudWatchLogGroupArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#aws-resource-mwaa-environment-return-values"""
        return GetAtt(resource=self, attr_name="LoggingConfiguration.WebserverLogs.CloudWatchLogGroupArn")
    
    @property
    def rv_LoggingConfigurationWorkerLogsCloudWatchLogGroupArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#aws-resource-mwaa-environment-return-values"""
        return GetAtt(resource=self, attr_name="LoggingConfiguration.WorkerLogs.CloudWatchLogGroupArn")
    
    @property
    def rv_LoggingConfigurationTaskLogsCloudWatchLogGroupArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#aws-resource-mwaa-environment-return-values"""
        return GetAtt(resource=self, attr_name="LoggingConfiguration.TaskLogs.CloudWatchLogGroupArn")
    
