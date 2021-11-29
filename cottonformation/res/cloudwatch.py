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
class PropAnomalyDetectorMetricDataQueries(Property):
    """
    AWS Object Type = "AWS::CloudWatch::AnomalyDetector.MetricDataQueries"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataqueries.html

    Property Document:
    
    """
    AWS_OBJECT_TYPE = "AWS::CloudWatch::AnomalyDetector.MetricDataQueries"
    

@attr.s
class PropMetricStreamMetricStreamFilter(Property):
    """
    AWS Object Type = "AWS::CloudWatch::MetricStream.MetricStreamFilter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-metricstream-metricstreamfilter.html

    Property Document:
    
    - ``rp_Namespace``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-metricstream-metricstreamfilter.html#cfn-cloudwatch-metricstream-metricstreamfilter-namespace
    """
    AWS_OBJECT_TYPE = "AWS::CloudWatch::MetricStream.MetricStreamFilter"
    
    rp_Namespace: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Namespace"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-metricstream-metricstreamfilter.html#cfn-cloudwatch-metricstream-metricstreamfilter-namespace"""

@attr.s
class PropAnomalyDetectorRange(Property):
    """
    AWS Object Type = "AWS::CloudWatch::AnomalyDetector.Range"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-range.html

    Property Document:
    
    - ``rp_EndTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-range.html#cfn-cloudwatch-anomalydetector-range-endtime
    - ``rp_StartTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-range.html#cfn-cloudwatch-anomalydetector-range-starttime
    """
    AWS_OBJECT_TYPE = "AWS::CloudWatch::AnomalyDetector.Range"
    
    rp_EndTime: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "EndTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-range.html#cfn-cloudwatch-anomalydetector-range-endtime"""
    rp_StartTime: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "StartTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-range.html#cfn-cloudwatch-anomalydetector-range-starttime"""

@attr.s
class PropInsightRuleTags(Property):
    """
    AWS Object Type = "AWS::CloudWatch::InsightRule.Tags"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-insightrule-tags.html

    Property Document:
    
    """
    AWS_OBJECT_TYPE = "AWS::CloudWatch::InsightRule.Tags"
    

@attr.s
class PropAnomalyDetectorDimension(Property):
    """
    AWS Object Type = "AWS::CloudWatch::AnomalyDetector.Dimension"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-dimension.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-dimension.html#cfn-cloudwatch-anomalydetector-dimension-name
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-dimension.html#cfn-cloudwatch-anomalydetector-dimension-value
    """
    AWS_OBJECT_TYPE = "AWS::CloudWatch::AnomalyDetector.Dimension"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-dimension.html#cfn-cloudwatch-anomalydetector-dimension-name"""
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-dimension.html#cfn-cloudwatch-anomalydetector-dimension-value"""

@attr.s
class PropAnomalyDetectorMetric(Property):
    """
    AWS Object Type = "AWS::CloudWatch::AnomalyDetector.Metric"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metric.html

    Property Document:
    
    - ``rp_MetricName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metric.html#cfn-cloudwatch-anomalydetector-metric-metricname
    - ``rp_Namespace``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metric.html#cfn-cloudwatch-anomalydetector-metric-namespace
    - ``p_Dimensions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metric.html#cfn-cloudwatch-anomalydetector-metric-dimensions
    """
    AWS_OBJECT_TYPE = "AWS::CloudWatch::AnomalyDetector.Metric"
    
    rp_MetricName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "MetricName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metric.html#cfn-cloudwatch-anomalydetector-metric-metricname"""
    rp_Namespace: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Namespace"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metric.html#cfn-cloudwatch-anomalydetector-metric-namespace"""
    p_Dimensions: typing.List[typing.Union['PropAnomalyDetectorDimension', dict]] = attr.ib(
        default=None,
        converter=PropAnomalyDetectorDimension.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropAnomalyDetectorDimension), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Dimensions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metric.html#cfn-cloudwatch-anomalydetector-metric-dimensions"""

@attr.s
class PropAnomalyDetectorMetricStat(Property):
    """
    AWS Object Type = "AWS::CloudWatch::AnomalyDetector.MetricStat"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricstat.html

    Property Document:
    
    - ``rp_Metric``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricstat.html#cfn-cloudwatch-anomalydetector-metricstat-metric
    - ``rp_Period``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricstat.html#cfn-cloudwatch-anomalydetector-metricstat-period
    - ``rp_Stat``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricstat.html#cfn-cloudwatch-anomalydetector-metricstat-stat
    - ``p_Unit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricstat.html#cfn-cloudwatch-anomalydetector-metricstat-unit
    """
    AWS_OBJECT_TYPE = "AWS::CloudWatch::AnomalyDetector.MetricStat"
    
    rp_Metric: typing.Union['PropAnomalyDetectorMetric', dict] = attr.ib(
        default=None,
        converter=PropAnomalyDetectorMetric.from_dict,
        validator=attr.validators.instance_of(PropAnomalyDetectorMetric),
        metadata={AttrMeta.PROPERTY_NAME: "Metric"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricstat.html#cfn-cloudwatch-anomalydetector-metricstat-metric"""
    rp_Period: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Period"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricstat.html#cfn-cloudwatch-anomalydetector-metricstat-period"""
    rp_Stat: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Stat"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricstat.html#cfn-cloudwatch-anomalydetector-metricstat-stat"""
    p_Unit: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Unit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricstat.html#cfn-cloudwatch-anomalydetector-metricstat-unit"""

@attr.s
class PropAlarmDimension(Property):
    """
    AWS Object Type = "AWS::CloudWatch::Alarm.Dimension"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-dimension.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-dimension.html#cfn-cloudwatch-alarm-dimension-name
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-dimension.html#cfn-cloudwatch-alarm-dimension-value
    """
    AWS_OBJECT_TYPE = "AWS::CloudWatch::Alarm.Dimension"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-dimension.html#cfn-cloudwatch-alarm-dimension-name"""
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-dimension.html#cfn-cloudwatch-alarm-dimension-value"""

@attr.s
class PropAlarmMetric(Property):
    """
    AWS Object Type = "AWS::CloudWatch::Alarm.Metric"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metric.html

    Property Document:
    
    - ``p_Dimensions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metric.html#cfn-cloudwatch-alarm-metric-dimensions
    - ``p_MetricName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metric.html#cfn-cloudwatch-alarm-metric-metricname
    - ``p_Namespace``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metric.html#cfn-cloudwatch-alarm-metric-namespace
    """
    AWS_OBJECT_TYPE = "AWS::CloudWatch::Alarm.Metric"
    
    p_Dimensions: typing.List[typing.Union['PropAlarmDimension', dict]] = attr.ib(
        default=None,
        converter=PropAlarmDimension.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropAlarmDimension), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Dimensions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metric.html#cfn-cloudwatch-alarm-metric-dimensions"""
    p_MetricName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MetricName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metric.html#cfn-cloudwatch-alarm-metric-metricname"""
    p_Namespace: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Namespace"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metric.html#cfn-cloudwatch-alarm-metric-namespace"""

@attr.s
class PropAnomalyDetectorConfiguration(Property):
    """
    AWS Object Type = "AWS::CloudWatch::AnomalyDetector.Configuration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-configuration.html

    Property Document:
    
    - ``p_ExcludedTimeRanges``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-configuration.html#cfn-cloudwatch-anomalydetector-configuration-excludedtimeranges
    - ``p_MetricTimeZone``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-configuration.html#cfn-cloudwatch-anomalydetector-configuration-metrictimezone
    """
    AWS_OBJECT_TYPE = "AWS::CloudWatch::AnomalyDetector.Configuration"
    
    p_ExcludedTimeRanges: typing.List[typing.Union['PropAnomalyDetectorRange', dict]] = attr.ib(
        default=None,
        converter=PropAnomalyDetectorRange.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropAnomalyDetectorRange), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ExcludedTimeRanges"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-configuration.html#cfn-cloudwatch-anomalydetector-configuration-excludedtimeranges"""
    p_MetricTimeZone: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MetricTimeZone"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-configuration.html#cfn-cloudwatch-anomalydetector-configuration-metrictimezone"""

@attr.s
class PropAlarmMetricStat(Property):
    """
    AWS Object Type = "AWS::CloudWatch::Alarm.MetricStat"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html

    Property Document:
    
    - ``rp_Metric``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html#cfn-cloudwatch-alarm-metricstat-metric
    - ``rp_Period``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html#cfn-cloudwatch-alarm-metricstat-period
    - ``rp_Stat``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html#cfn-cloudwatch-alarm-metricstat-stat
    - ``p_Unit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html#cfn-cloudwatch-alarm-metricstat-unit
    """
    AWS_OBJECT_TYPE = "AWS::CloudWatch::Alarm.MetricStat"
    
    rp_Metric: typing.Union['PropAlarmMetric', dict] = attr.ib(
        default=None,
        converter=PropAlarmMetric.from_dict,
        validator=attr.validators.instance_of(PropAlarmMetric),
        metadata={AttrMeta.PROPERTY_NAME: "Metric"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html#cfn-cloudwatch-alarm-metricstat-metric"""
    rp_Period: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Period"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html#cfn-cloudwatch-alarm-metricstat-period"""
    rp_Stat: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Stat"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html#cfn-cloudwatch-alarm-metricstat-stat"""
    p_Unit: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Unit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html#cfn-cloudwatch-alarm-metricstat-unit"""

@attr.s
class PropAnomalyDetectorMetricDataQuery(Property):
    """
    AWS Object Type = "AWS::CloudWatch::AnomalyDetector.MetricDataQuery"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html

    Property Document:
    
    - ``rp_Id``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-id
    - ``p_AccountId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-accountid
    - ``p_Expression``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-expression
    - ``p_Label``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-label
    - ``p_MetricStat``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-metricstat
    - ``p_Period``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-period
    - ``p_ReturnData``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-returndata
    """
    AWS_OBJECT_TYPE = "AWS::CloudWatch::AnomalyDetector.MetricDataQuery"
    
    rp_Id: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Id"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-id"""
    p_AccountId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AccountId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-accountid"""
    p_Expression: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Expression"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-expression"""
    p_Label: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Label"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-label"""
    p_MetricStat: typing.Union['PropAnomalyDetectorMetricStat', dict] = attr.ib(
        default=None,
        converter=PropAnomalyDetectorMetricStat.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropAnomalyDetectorMetricStat)),
        metadata={AttrMeta.PROPERTY_NAME: "MetricStat"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-metricstat"""
    p_Period: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Period"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-period"""
    p_ReturnData: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "ReturnData"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-returndata"""

@attr.s
class PropAnomalyDetectorSingleMetricAnomalyDetector(Property):
    """
    AWS Object Type = "AWS::CloudWatch::AnomalyDetector.SingleMetricAnomalyDetector"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector.html

    Property Document:
    
    - ``p_Dimensions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector.html#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-dimensions
    - ``p_MetricName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector.html#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-metricname
    - ``p_Namespace``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector.html#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-namespace
    - ``p_Stat``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector.html#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-stat
    """
    AWS_OBJECT_TYPE = "AWS::CloudWatch::AnomalyDetector.SingleMetricAnomalyDetector"
    
    p_Dimensions: typing.List[typing.Union['PropAnomalyDetectorDimension', dict]] = attr.ib(
        default=None,
        converter=PropAnomalyDetectorDimension.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropAnomalyDetectorDimension), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Dimensions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector.html#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-dimensions"""
    p_MetricName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MetricName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector.html#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-metricname"""
    p_Namespace: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Namespace"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector.html#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-namespace"""
    p_Stat: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Stat"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector.html#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-stat"""

@attr.s
class PropAlarmMetricDataQuery(Property):
    """
    AWS Object Type = "AWS::CloudWatch::Alarm.MetricDataQuery"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html

    Property Document:
    
    - ``rp_Id``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-id
    - ``p_AccountId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-accountid
    - ``p_Expression``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-expression
    - ``p_Label``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-label
    - ``p_MetricStat``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-metricstat
    - ``p_Period``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-period
    - ``p_ReturnData``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-returndata
    """
    AWS_OBJECT_TYPE = "AWS::CloudWatch::Alarm.MetricDataQuery"
    
    rp_Id: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Id"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-id"""
    p_AccountId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AccountId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-accountid"""
    p_Expression: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Expression"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-expression"""
    p_Label: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Label"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-label"""
    p_MetricStat: typing.Union['PropAlarmMetricStat', dict] = attr.ib(
        default=None,
        converter=PropAlarmMetricStat.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropAlarmMetricStat)),
        metadata={AttrMeta.PROPERTY_NAME: "MetricStat"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-metricstat"""
    p_Period: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Period"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-period"""
    p_ReturnData: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "ReturnData"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-returndata"""

@attr.s
class PropAnomalyDetectorMetricMathAnomalyDetector(Property):
    """
    AWS Object Type = "AWS::CloudWatch::AnomalyDetector.MetricMathAnomalyDetector"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricmathanomalydetector.html

    Property Document:
    
    - ``p_MetricDataQueries``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricmathanomalydetector.html#cfn-cloudwatch-anomalydetector-metricmathanomalydetector-metricdataqueries
    """
    AWS_OBJECT_TYPE = "AWS::CloudWatch::AnomalyDetector.MetricMathAnomalyDetector"
    
    p_MetricDataQueries: typing.List[typing.Union['PropAnomalyDetectorMetricDataQuery', dict]] = attr.ib(
        default=None,
        converter=PropAnomalyDetectorMetricDataQuery.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropAnomalyDetectorMetricDataQuery), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "MetricDataQueries"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricmathanomalydetector.html#cfn-cloudwatch-anomalydetector-metricmathanomalydetector-metricdataqueries"""


#--- Resource declaration ---

@attr.s
class AnomalyDetector(Resource):
    """
    AWS Object Type = "AWS::CloudWatch::AnomalyDetector"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html

    Property Document:
    
    - ``p_Configuration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-configuration
    - ``p_Dimensions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-dimensions
    - ``p_MetricMathAnomalyDetector``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-metricmathanomalydetector
    - ``p_MetricName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-metricname
    - ``p_Namespace``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-namespace
    - ``p_SingleMetricAnomalyDetector``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector
    - ``p_Stat``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-stat
    """
    AWS_OBJECT_TYPE = "AWS::CloudWatch::AnomalyDetector"

    
    p_Configuration: typing.Union['PropAnomalyDetectorConfiguration', dict] = attr.ib(
        default=None,
        converter=PropAnomalyDetectorConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropAnomalyDetectorConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "Configuration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-configuration"""
    p_Dimensions: typing.List[typing.Union['PropAnomalyDetectorDimension', dict]] = attr.ib(
        default=None,
        converter=PropAnomalyDetectorDimension.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropAnomalyDetectorDimension), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Dimensions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-dimensions"""
    p_MetricMathAnomalyDetector: typing.Union['PropAnomalyDetectorMetricMathAnomalyDetector', dict] = attr.ib(
        default=None,
        converter=PropAnomalyDetectorMetricMathAnomalyDetector.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropAnomalyDetectorMetricMathAnomalyDetector)),
        metadata={AttrMeta.PROPERTY_NAME: "MetricMathAnomalyDetector"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-metricmathanomalydetector"""
    p_MetricName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MetricName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-metricname"""
    p_Namespace: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Namespace"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-namespace"""
    p_SingleMetricAnomalyDetector: typing.Union['PropAnomalyDetectorSingleMetricAnomalyDetector', dict] = attr.ib(
        default=None,
        converter=PropAnomalyDetectorSingleMetricAnomalyDetector.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropAnomalyDetectorSingleMetricAnomalyDetector)),
        metadata={AttrMeta.PROPERTY_NAME: "SingleMetricAnomalyDetector"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector"""
    p_Stat: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Stat"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-stat"""

    

@attr.s
class CompositeAlarm(Resource):
    """
    AWS Object Type = "AWS::CloudWatch::CompositeAlarm"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html

    Property Document:
    
    - ``rp_AlarmName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-alarmname
    - ``rp_AlarmRule``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-alarmrule
    - ``p_ActionsEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-actionsenabled
    - ``p_AlarmActions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-alarmactions
    - ``p_AlarmDescription``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-alarmdescription
    - ``p_InsufficientDataActions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-insufficientdataactions
    - ``p_OKActions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-okactions
    """
    AWS_OBJECT_TYPE = "AWS::CloudWatch::CompositeAlarm"

    
    rp_AlarmName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AlarmName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-alarmname"""
    rp_AlarmRule: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AlarmRule"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-alarmrule"""
    p_ActionsEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "ActionsEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-actionsenabled"""
    p_AlarmActions: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AlarmActions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-alarmactions"""
    p_AlarmDescription: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AlarmDescription"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-alarmdescription"""
    p_InsufficientDataActions: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "InsufficientDataActions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-insufficientdataactions"""
    p_OKActions: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "OKActions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-okactions"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#aws-resource-cloudwatch-compositealarm-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class InsightRule(Resource):
    """
    AWS Object Type = "AWS::CloudWatch::InsightRule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html

    Property Document:
    
    - ``rp_RuleBody``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html#cfn-cloudwatch-insightrule-rulebody
    - ``rp_RuleName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html#cfn-cloudwatch-insightrule-rulename
    - ``rp_RuleState``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html#cfn-cloudwatch-insightrule-rulestate
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html#cfn-cloudwatch-insightrule-tags
    """
    AWS_OBJECT_TYPE = "AWS::CloudWatch::InsightRule"

    
    rp_RuleBody: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RuleBody"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html#cfn-cloudwatch-insightrule-rulebody"""
    rp_RuleName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RuleName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html#cfn-cloudwatch-insightrule-rulename"""
    rp_RuleState: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RuleState"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html#cfn-cloudwatch-insightrule-rulestate"""
    p_Tags: typing.Union['PropInsightRuleTags', dict] = attr.ib(
        default=None,
        converter=PropInsightRuleTags.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropInsightRuleTags)),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html#cfn-cloudwatch-insightrule-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html#aws-resource-cloudwatch-insightrule-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_RuleName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html#aws-resource-cloudwatch-insightrule-return-values"""
        return GetAtt(resource=self, attr_name="RuleName")
    

@attr.s
class Dashboard(Resource):
    """
    AWS Object Type = "AWS::CloudWatch::Dashboard"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-dashboard.html

    Property Document:
    
    - ``rp_DashboardBody``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-dashboard.html#cfn-cloudwatch-dashboard-dashboardbody
    - ``p_DashboardName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-dashboard.html#cfn-cloudwatch-dashboard-dashboardname
    """
    AWS_OBJECT_TYPE = "AWS::CloudWatch::Dashboard"

    
    rp_DashboardBody: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DashboardBody"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-dashboard.html#cfn-cloudwatch-dashboard-dashboardbody"""
    p_DashboardName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DashboardName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-dashboard.html#cfn-cloudwatch-dashboard-dashboardname"""

    

@attr.s
class MetricStream(Resource):
    """
    AWS Object Type = "AWS::CloudWatch::MetricStream"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html

    Property Document:
    
    - ``rp_FirehoseArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-firehosearn
    - ``rp_OutputFormat``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-outputformat
    - ``rp_RoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-rolearn
    - ``p_ExcludeFilters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-excludefilters
    - ``p_IncludeFilters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-includefilters
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-name
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-tags
    """
    AWS_OBJECT_TYPE = "AWS::CloudWatch::MetricStream"

    
    rp_FirehoseArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "FirehoseArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-firehosearn"""
    rp_OutputFormat: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "OutputFormat"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-outputformat"""
    rp_RoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-rolearn"""
    p_ExcludeFilters: typing.List[typing.Union['PropMetricStreamMetricStreamFilter', dict]] = attr.ib(
        default=None,
        converter=PropMetricStreamMetricStreamFilter.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropMetricStreamMetricStreamFilter), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ExcludeFilters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-excludefilters"""
    p_IncludeFilters: typing.List[typing.Union['PropMetricStreamMetricStreamFilter', dict]] = attr.ib(
        default=None,
        converter=PropMetricStreamMetricStreamFilter.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropMetricStreamMetricStreamFilter), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "IncludeFilters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-includefilters"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-name"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#aws-resource-cloudwatch-metricstream-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_CreationDate(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#aws-resource-cloudwatch-metricstream-return-values"""
        return GetAtt(resource=self, attr_name="CreationDate")
    
    @property
    def rv_LastUpdateDate(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#aws-resource-cloudwatch-metricstream-return-values"""
        return GetAtt(resource=self, attr_name="LastUpdateDate")
    
    @property
    def rv_State(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#aws-resource-cloudwatch-metricstream-return-values"""
        return GetAtt(resource=self, attr_name="State")
    

@attr.s
class Alarm(Resource):
    """
    AWS Object Type = "AWS::CloudWatch::Alarm"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html

    Property Document:
    
    - ``rp_ComparisonOperator``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-comparisonoperator
    - ``rp_EvaluationPeriods``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-evaluationperiods
    - ``p_ActionsEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-actionsenabled
    - ``p_AlarmActions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-alarmactions
    - ``p_AlarmDescription``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-alarmdescription
    - ``p_AlarmName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-alarmname
    - ``p_DatapointsToAlarm``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarm-datapointstoalarm
    - ``p_Dimensions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-dimension
    - ``p_EvaluateLowSampleCountPercentile``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-evaluatelowsamplecountpercentile
    - ``p_ExtendedStatistic``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-extendedstatistic
    - ``p_InsufficientDataActions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-insufficientdataactions
    - ``p_MetricName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-metricname
    - ``p_Metrics``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarm-metrics
    - ``p_Namespace``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-namespace
    - ``p_OKActions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-okactions
    - ``p_Period``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-period
    - ``p_Statistic``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-statistic
    - ``p_Threshold``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-threshold
    - ``p_ThresholdMetricId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-dynamic-threshold
    - ``p_TreatMissingData``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-treatmissingdata
    - ``p_Unit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-unit
    """
    AWS_OBJECT_TYPE = "AWS::CloudWatch::Alarm"

    
    rp_ComparisonOperator: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ComparisonOperator"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-comparisonoperator"""
    rp_EvaluationPeriods: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "EvaluationPeriods"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-evaluationperiods"""
    p_ActionsEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "ActionsEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-actionsenabled"""
    p_AlarmActions: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AlarmActions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-alarmactions"""
    p_AlarmDescription: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AlarmDescription"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-alarmdescription"""
    p_AlarmName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AlarmName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-alarmname"""
    p_DatapointsToAlarm: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "DatapointsToAlarm"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarm-datapointstoalarm"""
    p_Dimensions: typing.List[typing.Union['PropAlarmDimension', dict]] = attr.ib(
        default=None,
        converter=PropAlarmDimension.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropAlarmDimension), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Dimensions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-dimension"""
    p_EvaluateLowSampleCountPercentile: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "EvaluateLowSampleCountPercentile"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-evaluatelowsamplecountpercentile"""
    p_ExtendedStatistic: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ExtendedStatistic"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-extendedstatistic"""
    p_InsufficientDataActions: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "InsufficientDataActions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-insufficientdataactions"""
    p_MetricName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MetricName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-metricname"""
    p_Metrics: typing.List[typing.Union['PropAlarmMetricDataQuery', dict]] = attr.ib(
        default=None,
        converter=PropAlarmMetricDataQuery.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropAlarmMetricDataQuery), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Metrics"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarm-metrics"""
    p_Namespace: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Namespace"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-namespace"""
    p_OKActions: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "OKActions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-okactions"""
    p_Period: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Period"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-period"""
    p_Statistic: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Statistic"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-statistic"""
    p_Threshold: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "Threshold"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-threshold"""
    p_ThresholdMetricId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ThresholdMetricId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-dynamic-threshold"""
    p_TreatMissingData: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TreatMissingData"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-treatmissingdata"""
    p_Unit: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Unit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#cfn-cloudwatch-alarms-unit"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html#aws-properties-cw-alarm-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
