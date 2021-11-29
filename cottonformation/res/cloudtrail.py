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
class PropTrailDataResource(Property):
    """
    AWS Object Type = "AWS::CloudTrail::Trail.DataResource"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-dataresource.html

    Property Document:
    
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-dataresource.html#cfn-cloudtrail-trail-dataresource-type
    - ``p_Values``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-dataresource.html#cfn-cloudtrail-trail-dataresource-values
    """
    AWS_OBJECT_TYPE = "AWS::CloudTrail::Trail.DataResource"
    
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-dataresource.html#cfn-cloudtrail-trail-dataresource-type"""
    p_Values: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Values"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-dataresource.html#cfn-cloudtrail-trail-dataresource-values"""

@attr.s
class PropTrailInsightSelector(Property):
    """
    AWS Object Type = "AWS::CloudTrail::Trail.InsightSelector"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-insightselector.html

    Property Document:
    
    - ``p_InsightType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-insightselector.html#cfn-cloudtrail-trail-insightselector-insighttype
    """
    AWS_OBJECT_TYPE = "AWS::CloudTrail::Trail.InsightSelector"
    
    p_InsightType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "InsightType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-insightselector.html#cfn-cloudtrail-trail-insightselector-insighttype"""

@attr.s
class PropTrailEventSelector(Property):
    """
    AWS Object Type = "AWS::CloudTrail::Trail.EventSelector"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-eventselector.html

    Property Document:
    
    - ``p_DataResources``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-eventselector.html#cfn-cloudtrail-trail-eventselector-dataresources
    - ``p_ExcludeManagementEventSources``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-eventselector.html#cfn-cloudtrail-trail-eventselector-excludemanagementeventsources
    - ``p_IncludeManagementEvents``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-eventselector.html#cfn-cloudtrail-trail-eventselector-includemanagementevents
    - ``p_ReadWriteType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-eventselector.html#cfn-cloudtrail-trail-eventselector-readwritetype
    """
    AWS_OBJECT_TYPE = "AWS::CloudTrail::Trail.EventSelector"
    
    p_DataResources: typing.List[typing.Union['PropTrailDataResource', dict]] = attr.ib(
        default=None,
        converter=PropTrailDataResource.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTrailDataResource), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "DataResources"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-eventselector.html#cfn-cloudtrail-trail-eventselector-dataresources"""
    p_ExcludeManagementEventSources: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ExcludeManagementEventSources"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-eventselector.html#cfn-cloudtrail-trail-eventselector-excludemanagementeventsources"""
    p_IncludeManagementEvents: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IncludeManagementEvents"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-eventselector.html#cfn-cloudtrail-trail-eventselector-includemanagementevents"""
    p_ReadWriteType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ReadWriteType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-eventselector.html#cfn-cloudtrail-trail-eventselector-readwritetype"""


#--- Resource declaration ---

@attr.s
class Trail(Resource):
    """
    AWS Object Type = "AWS::CloudTrail::Trail"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html

    Property Document:
    
    - ``rp_IsLogging``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-islogging
    - ``rp_S3BucketName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-s3bucketname
    - ``p_CloudWatchLogsLogGroupArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-cloudwatchlogsloggrouparn
    - ``p_CloudWatchLogsRoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-cloudwatchlogsrolearn
    - ``p_EnableLogFileValidation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-enablelogfilevalidation
    - ``p_EventSelectors``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-eventselectors
    - ``p_IncludeGlobalServiceEvents``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-includeglobalserviceevents
    - ``p_InsightSelectors``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-insightselectors
    - ``p_IsMultiRegionTrail``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-ismultiregiontrail
    - ``p_IsOrganizationTrail``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-isorganizationtrail
    - ``p_KMSKeyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-kmskeyid
    - ``p_S3KeyPrefix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-s3keyprefix
    - ``p_SnsTopicName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-snstopicname
    - ``p_TrailName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-trailname
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-tags
    """
    AWS_OBJECT_TYPE = "AWS::CloudTrail::Trail"

    
    rp_IsLogging: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "IsLogging"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-islogging"""
    rp_S3BucketName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "S3BucketName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-s3bucketname"""
    p_CloudWatchLogsLogGroupArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CloudWatchLogsLogGroupArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-cloudwatchlogsloggrouparn"""
    p_CloudWatchLogsRoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CloudWatchLogsRoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-cloudwatchlogsrolearn"""
    p_EnableLogFileValidation: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EnableLogFileValidation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-enablelogfilevalidation"""
    p_EventSelectors: typing.List[typing.Union['PropTrailEventSelector', dict]] = attr.ib(
        default=None,
        converter=PropTrailEventSelector.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTrailEventSelector), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "EventSelectors"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-eventselectors"""
    p_IncludeGlobalServiceEvents: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IncludeGlobalServiceEvents"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-includeglobalserviceevents"""
    p_InsightSelectors: typing.List[typing.Union['PropTrailInsightSelector', dict]] = attr.ib(
        default=None,
        converter=PropTrailInsightSelector.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTrailInsightSelector), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "InsightSelectors"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-insightselectors"""
    p_IsMultiRegionTrail: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IsMultiRegionTrail"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-ismultiregiontrail"""
    p_IsOrganizationTrail: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IsOrganizationTrail"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-isorganizationtrail"""
    p_KMSKeyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "KMSKeyId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-kmskeyid"""
    p_S3KeyPrefix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "S3KeyPrefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-s3keyprefix"""
    p_SnsTopicName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SnsTopicName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-snstopicname"""
    p_TrailName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TrailName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-trailname"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#aws-resource-cloudtrail-trail-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_SnsTopicArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#aws-resource-cloudtrail-trail-return-values"""
        return GetAtt(resource=self, attr_name="SnsTopicArn")
    
