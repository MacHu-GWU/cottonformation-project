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
class PropScalableTargetSuspendedState(Property):
    """
    AWS Object Type = "AWS::ApplicationAutoScaling::ScalableTarget.SuspendedState"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-suspendedstate.html

    Property Document:
    
    - ``p_DynamicScalingInSuspended``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-suspendedstate.html#cfn-applicationautoscaling-scalabletarget-suspendedstate-dynamicscalinginsuspended
    - ``p_DynamicScalingOutSuspended``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-suspendedstate.html#cfn-applicationautoscaling-scalabletarget-suspendedstate-dynamicscalingoutsuspended
    - ``p_ScheduledScalingSuspended``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-suspendedstate.html#cfn-applicationautoscaling-scalabletarget-suspendedstate-scheduledscalingsuspended
    """
    AWS_OBJECT_TYPE = "AWS::ApplicationAutoScaling::ScalableTarget.SuspendedState"
    
    p_DynamicScalingInSuspended: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "DynamicScalingInSuspended"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-suspendedstate.html#cfn-applicationautoscaling-scalabletarget-suspendedstate-dynamicscalinginsuspended"""
    p_DynamicScalingOutSuspended: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "DynamicScalingOutSuspended"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-suspendedstate.html#cfn-applicationautoscaling-scalabletarget-suspendedstate-dynamicscalingoutsuspended"""
    p_ScheduledScalingSuspended: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "ScheduledScalingSuspended"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-suspendedstate.html#cfn-applicationautoscaling-scalabletarget-suspendedstate-scheduledscalingsuspended"""

@attr.s
class PropScalingPolicyPredefinedMetricSpecification(Property):
    """
    AWS Object Type = "AWS::ApplicationAutoScaling::ScalingPolicy.PredefinedMetricSpecification"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-predefinedmetricspecification.html

    Property Document:
    
    - ``rp_PredefinedMetricType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-predefinedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-predefinedmetricspecification-predefinedmetrictype
    - ``p_ResourceLabel``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-predefinedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-predefinedmetricspecification-resourcelabel
    """
    AWS_OBJECT_TYPE = "AWS::ApplicationAutoScaling::ScalingPolicy.PredefinedMetricSpecification"
    
    rp_PredefinedMetricType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PredefinedMetricType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-predefinedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-predefinedmetricspecification-predefinedmetrictype"""
    p_ResourceLabel: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceLabel"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-predefinedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-predefinedmetricspecification-resourcelabel"""

@attr.s
class PropScalingPolicyMetricDimension(Property):
    """
    AWS Object Type = "AWS::ApplicationAutoScaling::ScalingPolicy.MetricDimension"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-metricdimension.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-metricdimension.html#cfn-applicationautoscaling-scalingpolicy-metricdimension-name
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-metricdimension.html#cfn-applicationautoscaling-scalingpolicy-metricdimension-value
    """
    AWS_OBJECT_TYPE = "AWS::ApplicationAutoScaling::ScalingPolicy.MetricDimension"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-metricdimension.html#cfn-applicationautoscaling-scalingpolicy-metricdimension-name"""
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-metricdimension.html#cfn-applicationautoscaling-scalingpolicy-metricdimension-value"""

@attr.s
class PropScalingPolicyStepAdjustment(Property):
    """
    AWS Object Type = "AWS::ApplicationAutoScaling::ScalingPolicy.StepAdjustment"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment.html

    Property Document:
    
    - ``rp_ScalingAdjustment``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment-scalingadjustment
    - ``p_MetricIntervalLowerBound``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment-metricintervallowerbound
    - ``p_MetricIntervalUpperBound``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment-metricintervalupperbound
    """
    AWS_OBJECT_TYPE = "AWS::ApplicationAutoScaling::ScalingPolicy.StepAdjustment"
    
    rp_ScalingAdjustment: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "ScalingAdjustment"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment-scalingadjustment"""
    p_MetricIntervalLowerBound: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "MetricIntervalLowerBound"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment-metricintervallowerbound"""
    p_MetricIntervalUpperBound: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "MetricIntervalUpperBound"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustment-metricintervalupperbound"""

@attr.s
class PropScalableTargetScalableTargetAction(Property):
    """
    AWS Object Type = "AWS::ApplicationAutoScaling::ScalableTarget.ScalableTargetAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scalabletargetaction.html

    Property Document:
    
    - ``p_MaxCapacity``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scalabletargetaction.html#cfn-applicationautoscaling-scalabletarget-scalabletargetaction-maxcapacity
    - ``p_MinCapacity``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scalabletargetaction.html#cfn-applicationautoscaling-scalabletarget-scalabletargetaction-mincapacity
    """
    AWS_OBJECT_TYPE = "AWS::ApplicationAutoScaling::ScalableTarget.ScalableTargetAction"
    
    p_MaxCapacity: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MaxCapacity"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scalabletargetaction.html#cfn-applicationautoscaling-scalabletarget-scalabletargetaction-maxcapacity"""
    p_MinCapacity: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MinCapacity"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scalabletargetaction.html#cfn-applicationautoscaling-scalabletarget-scalabletargetaction-mincapacity"""

@attr.s
class PropScalingPolicyStepScalingPolicyConfiguration(Property):
    """
    AWS Object Type = "AWS::ApplicationAutoScaling::ScalingPolicy.StepScalingPolicyConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html

    Property Document:
    
    - ``p_AdjustmentType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-adjustmenttype
    - ``p_Cooldown``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-cooldown
    - ``p_MetricAggregationType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-metricaggregationtype
    - ``p_MinAdjustmentMagnitude``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-minadjustmentmagnitude
    - ``p_StepAdjustments``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustments
    """
    AWS_OBJECT_TYPE = "AWS::ApplicationAutoScaling::ScalingPolicy.StepScalingPolicyConfiguration"
    
    p_AdjustmentType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AdjustmentType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-adjustmenttype"""
    p_Cooldown: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Cooldown"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-cooldown"""
    p_MetricAggregationType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MetricAggregationType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-metricaggregationtype"""
    p_MinAdjustmentMagnitude: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MinAdjustmentMagnitude"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-minadjustmentmagnitude"""
    p_StepAdjustments: typing.List[typing.Union['PropScalingPolicyStepAdjustment', dict]] = attr.ib(
        default=None,
        converter=PropScalingPolicyStepAdjustment.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropScalingPolicyStepAdjustment), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "StepAdjustments"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustments"""

@attr.s
class PropScalingPolicyCustomizedMetricSpecification(Property):
    """
    AWS Object Type = "AWS::ApplicationAutoScaling::ScalingPolicy.CustomizedMetricSpecification"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html

    Property Document:
    
    - ``rp_MetricName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-metricname
    - ``rp_Namespace``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-namespace
    - ``rp_Statistic``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-statistic
    - ``p_Dimensions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-dimensions
    - ``p_Unit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-unit
    """
    AWS_OBJECT_TYPE = "AWS::ApplicationAutoScaling::ScalingPolicy.CustomizedMetricSpecification"
    
    rp_MetricName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "MetricName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-metricname"""
    rp_Namespace: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Namespace"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-namespace"""
    rp_Statistic: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Statistic"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-statistic"""
    p_Dimensions: typing.List[typing.Union['PropScalingPolicyMetricDimension', dict]] = attr.ib(
        default=None,
        converter=PropScalingPolicyMetricDimension.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropScalingPolicyMetricDimension), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Dimensions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-dimensions"""
    p_Unit: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Unit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-unit"""

@attr.s
class PropScalableTargetScheduledAction(Property):
    """
    AWS Object Type = "AWS::ApplicationAutoScaling::ScalableTarget.ScheduledAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html

    Property Document:
    
    - ``rp_Schedule``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-schedule
    - ``rp_ScheduledActionName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-scheduledactionname
    - ``p_EndTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-endtime
    - ``p_ScalableTargetAction``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-scalabletargetaction
    - ``p_StartTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-starttime
    - ``p_Timezone``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-timezone
    """
    AWS_OBJECT_TYPE = "AWS::ApplicationAutoScaling::ScalableTarget.ScheduledAction"
    
    rp_Schedule: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Schedule"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-schedule"""
    rp_ScheduledActionName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ScheduledActionName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-scheduledactionname"""
    p_EndTime: str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
        metadata={AttrMeta.PROPERTY_NAME: "EndTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-endtime"""
    p_ScalableTargetAction: typing.Union['PropScalableTargetScalableTargetAction', dict] = attr.ib(
        default=None,
        converter=PropScalableTargetScalableTargetAction.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropScalableTargetScalableTargetAction)),
        metadata={AttrMeta.PROPERTY_NAME: "ScalableTargetAction"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-scalabletargetaction"""
    p_StartTime: str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(str)),
        metadata={AttrMeta.PROPERTY_NAME: "StartTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-starttime"""
    p_Timezone: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Timezone"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-timezone"""

@attr.s
class PropScalingPolicyTargetTrackingScalingPolicyConfiguration(Property):
    """
    AWS Object Type = "AWS::ApplicationAutoScaling::ScalingPolicy.TargetTrackingScalingPolicyConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html

    Property Document:
    
    - ``rp_TargetValue``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-targetvalue
    - ``p_CustomizedMetricSpecification``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-customizedmetricspecification
    - ``p_DisableScaleIn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-disablescalein
    - ``p_PredefinedMetricSpecification``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-predefinedmetricspecification
    - ``p_ScaleInCooldown``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-scaleincooldown
    - ``p_ScaleOutCooldown``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-scaleoutcooldown
    """
    AWS_OBJECT_TYPE = "AWS::ApplicationAutoScaling::ScalingPolicy.TargetTrackingScalingPolicyConfiguration"
    
    rp_TargetValue: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "TargetValue"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-targetvalue"""
    p_CustomizedMetricSpecification: typing.Union['PropScalingPolicyCustomizedMetricSpecification', dict] = attr.ib(
        default=None,
        converter=PropScalingPolicyCustomizedMetricSpecification.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropScalingPolicyCustomizedMetricSpecification)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomizedMetricSpecification"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-customizedmetricspecification"""
    p_DisableScaleIn: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "DisableScaleIn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-disablescalein"""
    p_PredefinedMetricSpecification: typing.Union['PropScalingPolicyPredefinedMetricSpecification', dict] = attr.ib(
        default=None,
        converter=PropScalingPolicyPredefinedMetricSpecification.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropScalingPolicyPredefinedMetricSpecification)),
        metadata={AttrMeta.PROPERTY_NAME: "PredefinedMetricSpecification"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-predefinedmetricspecification"""
    p_ScaleInCooldown: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ScaleInCooldown"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-scaleincooldown"""
    p_ScaleOutCooldown: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ScaleOutCooldown"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-scaleoutcooldown"""


#--- Resource declaration ---

@attr.s
class ScalableTarget(Resource):
    """
    AWS Object Type = "AWS::ApplicationAutoScaling::ScalableTarget"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html

    Property Document:
    
    - ``rp_MaxCapacity``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-maxcapacity
    - ``rp_MinCapacity``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-mincapacity
    - ``rp_ResourceId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-resourceid
    - ``rp_RoleARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-rolearn
    - ``rp_ScalableDimension``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-scalabledimension
    - ``rp_ServiceNamespace``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-servicenamespace
    - ``p_ScheduledActions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-scheduledactions
    - ``p_SuspendedState``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-suspendedstate
    """
    AWS_OBJECT_TYPE = "AWS::ApplicationAutoScaling::ScalableTarget"

    
    rp_MaxCapacity: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "MaxCapacity"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-maxcapacity"""
    rp_MinCapacity: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "MinCapacity"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-mincapacity"""
    rp_ResourceId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-resourceid"""
    rp_RoleARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-rolearn"""
    rp_ScalableDimension: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ScalableDimension"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-scalabledimension"""
    rp_ServiceNamespace: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ServiceNamespace"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-servicenamespace"""
    p_ScheduledActions: typing.List[typing.Union['PropScalableTargetScheduledAction', dict]] = attr.ib(
        default=None,
        converter=PropScalableTargetScheduledAction.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropScalableTargetScheduledAction), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ScheduledActions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-scheduledactions"""
    p_SuspendedState: typing.Union['PropScalableTargetSuspendedState', dict] = attr.ib(
        default=None,
        converter=PropScalableTargetSuspendedState.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropScalableTargetSuspendedState)),
        metadata={AttrMeta.PROPERTY_NAME: "SuspendedState"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-suspendedstate"""

    

@attr.s
class ScalingPolicy(Resource):
    """
    AWS Object Type = "AWS::ApplicationAutoScaling::ScalingPolicy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html

    Property Document:
    
    - ``rp_PolicyName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-policyname
    - ``rp_PolicyType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-policytype
    - ``p_ResourceId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-resourceid
    - ``p_ScalableDimension``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-scalabledimension
    - ``p_ScalingTargetId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-scalingtargetid
    - ``p_ServiceNamespace``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-servicenamespace
    - ``p_StepScalingPolicyConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration
    - ``p_TargetTrackingScalingPolicyConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration
    """
    AWS_OBJECT_TYPE = "AWS::ApplicationAutoScaling::ScalingPolicy"

    
    rp_PolicyName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PolicyName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-policyname"""
    rp_PolicyType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PolicyType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-policytype"""
    p_ResourceId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-resourceid"""
    p_ScalableDimension: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ScalableDimension"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-scalabledimension"""
    p_ScalingTargetId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ScalingTargetId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-scalingtargetid"""
    p_ServiceNamespace: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ServiceNamespace"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-servicenamespace"""
    p_StepScalingPolicyConfiguration: typing.Union['PropScalingPolicyStepScalingPolicyConfiguration', dict] = attr.ib(
        default=None,
        converter=PropScalingPolicyStepScalingPolicyConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropScalingPolicyStepScalingPolicyConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "StepScalingPolicyConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration"""
    p_TargetTrackingScalingPolicyConfiguration: typing.Union['PropScalingPolicyTargetTrackingScalingPolicyConfiguration', dict] = attr.ib(
        default=None,
        converter=PropScalingPolicyTargetTrackingScalingPolicyConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropScalingPolicyTargetTrackingScalingPolicyConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "TargetTrackingScalingPolicyConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration"""

    
