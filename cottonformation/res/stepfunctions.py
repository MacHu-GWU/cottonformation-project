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
class PropActivityTagsEntry(Property):
    """
    AWS Object Type = "AWS::StepFunctions::Activity.TagsEntry"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-activity-tagsentry.html

    Property Document:
    
    - ``rp_Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-activity-tagsentry.html#cfn-stepfunctions-activity-tagsentry-key
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-activity-tagsentry.html#cfn-stepfunctions-activity-tagsentry-value
    """
    AWS_OBJECT_TYPE = "AWS::StepFunctions::Activity.TagsEntry"
    
    rp_Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-activity-tagsentry.html#cfn-stepfunctions-activity-tagsentry-key"""
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-activity-tagsentry.html#cfn-stepfunctions-activity-tagsentry-value"""

@attr.s
class PropStateMachineDefinition(Property):
    """
    AWS Object Type = "AWS::StepFunctions::StateMachine.Definition"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-definition.html

    Property Document:
    
    """
    AWS_OBJECT_TYPE = "AWS::StepFunctions::StateMachine.Definition"
    

@attr.s
class PropStateMachineTagsEntry(Property):
    """
    AWS Object Type = "AWS::StepFunctions::StateMachine.TagsEntry"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tagsentry.html

    Property Document:
    
    - ``rp_Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tagsentry.html#cfn-stepfunctions-statemachine-tagsentry-key
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tagsentry.html#cfn-stepfunctions-statemachine-tagsentry-value
    """
    AWS_OBJECT_TYPE = "AWS::StepFunctions::StateMachine.TagsEntry"
    
    rp_Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tagsentry.html#cfn-stepfunctions-statemachine-tagsentry-key"""
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tagsentry.html#cfn-stepfunctions-statemachine-tagsentry-value"""

@attr.s
class PropStateMachineS3Location(Property):
    """
    AWS Object Type = "AWS::StepFunctions::StateMachine.S3Location"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-s3location.html

    Property Document:
    
    - ``rp_Bucket``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-s3location.html#cfn-stepfunctions-statemachine-s3location-bucket
    - ``rp_Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-s3location.html#cfn-stepfunctions-statemachine-s3location-key
    - ``p_Version``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-s3location.html#cfn-stepfunctions-statemachine-s3location-version
    """
    AWS_OBJECT_TYPE = "AWS::StepFunctions::StateMachine.S3Location"
    
    rp_Bucket: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Bucket"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-s3location.html#cfn-stepfunctions-statemachine-s3location-bucket"""
    rp_Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-s3location.html#cfn-stepfunctions-statemachine-s3location-key"""
    p_Version: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Version"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-s3location.html#cfn-stepfunctions-statemachine-s3location-version"""

@attr.s
class PropStateMachineCloudWatchLogsLogGroup(Property):
    """
    AWS Object Type = "AWS::StepFunctions::StateMachine.CloudWatchLogsLogGroup"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-cloudwatchlogsloggroup.html

    Property Document:
    
    - ``p_LogGroupArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-cloudwatchlogsloggroup.html#cfn-stepfunctions-statemachine-cloudwatchlogsloggroup-loggrouparn
    """
    AWS_OBJECT_TYPE = "AWS::StepFunctions::StateMachine.CloudWatchLogsLogGroup"
    
    p_LogGroupArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LogGroupArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-cloudwatchlogsloggroup.html#cfn-stepfunctions-statemachine-cloudwatchlogsloggroup-loggrouparn"""

@attr.s
class PropStateMachineTracingConfiguration(Property):
    """
    AWS Object Type = "AWS::StepFunctions::StateMachine.TracingConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tracingconfiguration.html

    Property Document:
    
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tracingconfiguration.html#cfn-stepfunctions-statemachine-tracingconfiguration-enabled
    """
    AWS_OBJECT_TYPE = "AWS::StepFunctions::StateMachine.TracingConfiguration"
    
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tracingconfiguration.html#cfn-stepfunctions-statemachine-tracingconfiguration-enabled"""

@attr.s
class PropStateMachineLogDestination(Property):
    """
    AWS Object Type = "AWS::StepFunctions::StateMachine.LogDestination"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-logdestination.html

    Property Document:
    
    - ``p_CloudWatchLogsLogGroup``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-logdestination.html#cfn-stepfunctions-statemachine-logdestination-cloudwatchlogsloggroup
    """
    AWS_OBJECT_TYPE = "AWS::StepFunctions::StateMachine.LogDestination"
    
    p_CloudWatchLogsLogGroup: typing.Union['PropStateMachineCloudWatchLogsLogGroup', dict] = attr.ib(
        default=None,
        converter=PropStateMachineCloudWatchLogsLogGroup.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropStateMachineCloudWatchLogsLogGroup)),
        metadata={AttrMeta.PROPERTY_NAME: "CloudWatchLogsLogGroup"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-logdestination.html#cfn-stepfunctions-statemachine-logdestination-cloudwatchlogsloggroup"""

@attr.s
class PropStateMachineLoggingConfiguration(Property):
    """
    AWS Object Type = "AWS::StepFunctions::StateMachine.LoggingConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html

    Property Document:
    
    - ``p_Destinations``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html#cfn-stepfunctions-statemachine-loggingconfiguration-destinations
    - ``p_IncludeExecutionData``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html#cfn-stepfunctions-statemachine-loggingconfiguration-includeexecutiondata
    - ``p_Level``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html#cfn-stepfunctions-statemachine-loggingconfiguration-level
    """
    AWS_OBJECT_TYPE = "AWS::StepFunctions::StateMachine.LoggingConfiguration"
    
    p_Destinations: typing.List[typing.Union['PropStateMachineLogDestination', dict]] = attr.ib(
        default=None,
        converter=PropStateMachineLogDestination.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropStateMachineLogDestination), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Destinations"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html#cfn-stepfunctions-statemachine-loggingconfiguration-destinations"""
    p_IncludeExecutionData: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IncludeExecutionData"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html#cfn-stepfunctions-statemachine-loggingconfiguration-includeexecutiondata"""
    p_Level: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Level"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html#cfn-stepfunctions-statemachine-loggingconfiguration-level"""


#--- Resource declaration ---

@attr.s
class StateMachine(Resource):
    """
    AWS Object Type = "AWS::StepFunctions::StateMachine"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html

    Property Document:
    
    - ``rp_RoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-rolearn
    - ``p_Definition``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definition
    - ``p_DefinitionS3Location``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definitions3location
    - ``p_DefinitionString``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definitionstring
    - ``p_DefinitionSubstitutions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definitionsubstitutions
    - ``p_LoggingConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-loggingconfiguration
    - ``p_StateMachineName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-statemachinename
    - ``p_StateMachineType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-statemachinetype
    - ``p_TracingConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-tracingconfiguration
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-tags
    """
    AWS_OBJECT_TYPE = "AWS::StepFunctions::StateMachine"

    
    rp_RoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-rolearn"""
    p_Definition: typing.Union['PropStateMachineDefinition', dict] = attr.ib(
        default=None,
        converter=PropStateMachineDefinition.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropStateMachineDefinition)),
        metadata={AttrMeta.PROPERTY_NAME: "Definition"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definition"""
    p_DefinitionS3Location: typing.Union['PropStateMachineS3Location', dict] = attr.ib(
        default=None,
        converter=PropStateMachineS3Location.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropStateMachineS3Location)),
        metadata={AttrMeta.PROPERTY_NAME: "DefinitionS3Location"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definitions3location"""
    p_DefinitionString: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DefinitionString"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definitionstring"""
    p_DefinitionSubstitutions: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type))),
        metadata={AttrMeta.PROPERTY_NAME: "DefinitionSubstitutions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definitionsubstitutions"""
    p_LoggingConfiguration: typing.Union['PropStateMachineLoggingConfiguration', dict] = attr.ib(
        default=None,
        converter=PropStateMachineLoggingConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropStateMachineLoggingConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "LoggingConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-loggingconfiguration"""
    p_StateMachineName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "StateMachineName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-statemachinename"""
    p_StateMachineType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "StateMachineType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-statemachinetype"""
    p_TracingConfiguration: typing.Union['PropStateMachineTracingConfiguration', dict] = attr.ib(
        default=None,
        converter=PropStateMachineTracingConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropStateMachineTracingConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "TracingConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-tracingconfiguration"""
    p_Tags: typing.List[typing.Union['PropStateMachineTagsEntry', dict]] = attr.ib(
        default=None,
        converter=PropStateMachineTagsEntry.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropStateMachineTagsEntry), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#aws-resource-stepfunctions-statemachine-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_Name(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#aws-resource-stepfunctions-statemachine-return-values"""
        return GetAtt(resource=self, attr_name="Name")
    

@attr.s
class Activity(Resource):
    """
    AWS Object Type = "AWS::StepFunctions::Activity"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-activity.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-activity.html#cfn-stepfunctions-activity-name
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-activity.html#cfn-stepfunctions-activity-tags
    """
    AWS_OBJECT_TYPE = "AWS::StepFunctions::Activity"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-activity.html#cfn-stepfunctions-activity-name"""
    p_Tags: typing.List[typing.Union['PropActivityTagsEntry', dict]] = attr.ib(
        default=None,
        converter=PropActivityTagsEntry.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropActivityTagsEntry), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-activity.html#cfn-stepfunctions-activity-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-activity.html#aws-resource-stepfunctions-activity-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_Name(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-activity.html#aws-resource-stepfunctions-activity-return-values"""
        return GetAtt(resource=self, attr_name="Name")
    
