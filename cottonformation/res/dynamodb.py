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
class PropGlobalTablePointInTimeRecoverySpecification(Property):
    """
    AWS Object Type = "AWS::DynamoDB::GlobalTable.PointInTimeRecoverySpecification"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-pointintimerecoveryspecification.html

    Property Document:
    
    - ``p_PointInTimeRecoveryEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-pointintimerecoveryspecification.html#cfn-dynamodb-globaltable-pointintimerecoveryspecification-pointintimerecoveryenabled
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::GlobalTable.PointInTimeRecoverySpecification"
    
    p_PointInTimeRecoveryEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "PointInTimeRecoveryEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-pointintimerecoveryspecification.html#cfn-dynamodb-globaltable-pointintimerecoveryspecification-pointintimerecoveryenabled"""

@attr.s
class PropTablePointInTimeRecoverySpecification(Property):
    """
    AWS Object Type = "AWS::DynamoDB::Table.PointInTimeRecoverySpecification"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-pointintimerecoveryspecification.html

    Property Document:
    
    - ``p_PointInTimeRecoveryEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-pointintimerecoveryspecification.html#cfn-dynamodb-table-pointintimerecoveryspecification-pointintimerecoveryenabled
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::Table.PointInTimeRecoverySpecification"
    
    p_PointInTimeRecoveryEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "PointInTimeRecoveryEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-pointintimerecoveryspecification.html#cfn-dynamodb-table-pointintimerecoveryspecification-pointintimerecoveryenabled"""

@attr.s
class PropTableKinesisStreamSpecification(Property):
    """
    AWS Object Type = "AWS::DynamoDB::Table.KinesisStreamSpecification"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-kinesisstreamspecification.html

    Property Document:
    
    - ``rp_StreamArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-kinesisstreamspecification.html#cfn-dynamodb-kinesisstreamspecification-streamarn
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::Table.KinesisStreamSpecification"
    
    rp_StreamArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "StreamArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-kinesisstreamspecification.html#cfn-dynamodb-kinesisstreamspecification-streamarn"""

@attr.s
class PropGlobalTableContributorInsightsSpecification(Property):
    """
    AWS Object Type = "AWS::DynamoDB::GlobalTable.ContributorInsightsSpecification"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-contributorinsightsspecification.html

    Property Document:
    
    - ``rp_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-contributorinsightsspecification.html#cfn-dynamodb-globaltable-contributorinsightsspecification-enabled
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::GlobalTable.ContributorInsightsSpecification"
    
    rp_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-contributorinsightsspecification.html#cfn-dynamodb-globaltable-contributorinsightsspecification-enabled"""

@attr.s
class PropTableAttributeDefinition(Property):
    """
    AWS Object Type = "AWS::DynamoDB::Table.AttributeDefinition"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-attributedef.html

    Property Document:
    
    - ``rp_AttributeName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-attributedef.html#cfn-dynamodb-attributedef-attributename
    - ``rp_AttributeType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-attributedef.html#cfn-dynamodb-attributedef-attributename-attributetype
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::Table.AttributeDefinition"
    
    rp_AttributeName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AttributeName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-attributedef.html#cfn-dynamodb-attributedef-attributename"""
    rp_AttributeType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AttributeType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-attributedef.html#cfn-dynamodb-attributedef-attributename-attributetype"""

@attr.s
class PropTableContributorInsightsSpecification(Property):
    """
    AWS Object Type = "AWS::DynamoDB::Table.ContributorInsightsSpecification"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-contributorinsightsspecification.html

    Property Document:
    
    - ``rp_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-contributorinsightsspecification.html#cfn-dynamodb-contributorinsightsspecification-enabled
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::Table.ContributorInsightsSpecification"
    
    rp_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-contributorinsightsspecification.html#cfn-dynamodb-contributorinsightsspecification-enabled"""

@attr.s
class PropTableKeySchema(Property):
    """
    AWS Object Type = "AWS::DynamoDB::Table.KeySchema"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-keyschema.html

    Property Document:
    
    - ``rp_AttributeName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-keyschema.html#aws-properties-dynamodb-keyschema-attributename
    - ``rp_KeyType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-keyschema.html#aws-properties-dynamodb-keyschema-keytype
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::Table.KeySchema"
    
    rp_AttributeName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AttributeName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-keyschema.html#aws-properties-dynamodb-keyschema-attributename"""
    rp_KeyType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "KeyType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-keyschema.html#aws-properties-dynamodb-keyschema-keytype"""

@attr.s
class PropGlobalTableTargetTrackingScalingPolicyConfiguration(Property):
    """
    AWS Object Type = "AWS::DynamoDB::GlobalTable.TargetTrackingScalingPolicyConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-targettrackingscalingpolicyconfiguration.html

    Property Document:
    
    - ``rp_TargetValue``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-targettrackingscalingpolicyconfiguration.html#cfn-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-targetvalue
    - ``p_DisableScaleIn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-targettrackingscalingpolicyconfiguration.html#cfn-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-disablescalein
    - ``p_ScaleInCooldown``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-targettrackingscalingpolicyconfiguration.html#cfn-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-scaleincooldown
    - ``p_ScaleOutCooldown``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-targettrackingscalingpolicyconfiguration.html#cfn-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-scaleoutcooldown
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::GlobalTable.TargetTrackingScalingPolicyConfiguration"
    
    rp_TargetValue: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "TargetValue"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-targettrackingscalingpolicyconfiguration.html#cfn-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-targetvalue"""
    p_DisableScaleIn: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "DisableScaleIn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-targettrackingscalingpolicyconfiguration.html#cfn-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-disablescalein"""
    p_ScaleInCooldown: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ScaleInCooldown"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-targettrackingscalingpolicyconfiguration.html#cfn-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-scaleincooldown"""
    p_ScaleOutCooldown: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ScaleOutCooldown"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-targettrackingscalingpolicyconfiguration.html#cfn-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-scaleoutcooldown"""

@attr.s
class PropGlobalTableKeySchema(Property):
    """
    AWS Object Type = "AWS::DynamoDB::GlobalTable.KeySchema"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-keyschema.html

    Property Document:
    
    - ``rp_AttributeName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-keyschema.html#cfn-dynamodb-globaltable-keyschema-attributename
    - ``rp_KeyType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-keyschema.html#cfn-dynamodb-globaltable-keyschema-keytype
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::GlobalTable.KeySchema"
    
    rp_AttributeName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AttributeName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-keyschema.html#cfn-dynamodb-globaltable-keyschema-attributename"""
    rp_KeyType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "KeyType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-keyschema.html#cfn-dynamodb-globaltable-keyschema-keytype"""

@attr.s
class PropGlobalTableStreamSpecification(Property):
    """
    AWS Object Type = "AWS::DynamoDB::GlobalTable.StreamSpecification"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-streamspecification.html

    Property Document:
    
    - ``rp_StreamViewType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-streamspecification.html#cfn-dynamodb-globaltable-streamspecification-streamviewtype
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::GlobalTable.StreamSpecification"
    
    rp_StreamViewType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "StreamViewType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-streamspecification.html#cfn-dynamodb-globaltable-streamspecification-streamviewtype"""

@attr.s
class PropGlobalTableProjection(Property):
    """
    AWS Object Type = "AWS::DynamoDB::GlobalTable.Projection"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-projection.html

    Property Document:
    
    - ``p_NonKeyAttributes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-projection.html#cfn-dynamodb-globaltable-projection-nonkeyattributes
    - ``p_ProjectionType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-projection.html#cfn-dynamodb-globaltable-projection-projectiontype
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::GlobalTable.Projection"
    
    p_NonKeyAttributes: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "NonKeyAttributes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-projection.html#cfn-dynamodb-globaltable-projection-nonkeyattributes"""
    p_ProjectionType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ProjectionType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-projection.html#cfn-dynamodb-globaltable-projection-projectiontype"""

@attr.s
class PropGlobalTableAttributeDefinition(Property):
    """
    AWS Object Type = "AWS::DynamoDB::GlobalTable.AttributeDefinition"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-attributedefinition.html

    Property Document:
    
    - ``rp_AttributeName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-attributedefinition.html#cfn-dynamodb-globaltable-attributedefinition-attributename
    - ``rp_AttributeType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-attributedefinition.html#cfn-dynamodb-globaltable-attributedefinition-attributetype
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::GlobalTable.AttributeDefinition"
    
    rp_AttributeName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AttributeName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-attributedefinition.html#cfn-dynamodb-globaltable-attributedefinition-attributename"""
    rp_AttributeType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AttributeType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-attributedefinition.html#cfn-dynamodb-globaltable-attributedefinition-attributetype"""

@attr.s
class PropGlobalTableSSESpecification(Property):
    """
    AWS Object Type = "AWS::DynamoDB::GlobalTable.SSESpecification"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-ssespecification.html

    Property Document:
    
    - ``rp_SSEEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-ssespecification.html#cfn-dynamodb-globaltable-ssespecification-sseenabled
    - ``p_SSEType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-ssespecification.html#cfn-dynamodb-globaltable-ssespecification-ssetype
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::GlobalTable.SSESpecification"
    
    rp_SSEEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "SSEEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-ssespecification.html#cfn-dynamodb-globaltable-ssespecification-sseenabled"""
    p_SSEType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SSEType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-ssespecification.html#cfn-dynamodb-globaltable-ssespecification-ssetype"""

@attr.s
class PropTableSSESpecification(Property):
    """
    AWS Object Type = "AWS::DynamoDB::Table.SSESpecification"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-ssespecification.html

    Property Document:
    
    - ``rp_SSEEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-ssespecification.html#cfn-dynamodb-table-ssespecification-sseenabled
    - ``p_KMSMasterKeyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-ssespecification.html#cfn-dynamodb-table-ssespecification-kmsmasterkeyid
    - ``p_SSEType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-ssespecification.html#cfn-dynamodb-table-ssespecification-ssetype
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::Table.SSESpecification"
    
    rp_SSEEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "SSEEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-ssespecification.html#cfn-dynamodb-table-ssespecification-sseenabled"""
    p_KMSMasterKeyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "KMSMasterKeyId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-ssespecification.html#cfn-dynamodb-table-ssespecification-kmsmasterkeyid"""
    p_SSEType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SSEType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-ssespecification.html#cfn-dynamodb-table-ssespecification-ssetype"""

@attr.s
class PropTableTimeToLiveSpecification(Property):
    """
    AWS Object Type = "AWS::DynamoDB::Table.TimeToLiveSpecification"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-timetolivespecification.html

    Property Document:
    
    - ``rp_AttributeName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-timetolivespecification.html#cfn-dynamodb-timetolivespecification-attributename
    - ``rp_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-timetolivespecification.html#cfn-dynamodb-timetolivespecification-enabled
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::Table.TimeToLiveSpecification"
    
    rp_AttributeName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AttributeName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-timetolivespecification.html#cfn-dynamodb-timetolivespecification-attributename"""
    rp_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-timetolivespecification.html#cfn-dynamodb-timetolivespecification-enabled"""

@attr.s
class PropTableProvisionedThroughput(Property):
    """
    AWS Object Type = "AWS::DynamoDB::Table.ProvisionedThroughput"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-provisionedthroughput.html

    Property Document:
    
    - ``rp_ReadCapacityUnits``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-provisionedthroughput.html#cfn-dynamodb-provisionedthroughput-readcapacityunits
    - ``rp_WriteCapacityUnits``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-provisionedthroughput.html#cfn-dynamodb-provisionedthroughput-writecapacityunits
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::Table.ProvisionedThroughput"
    
    rp_ReadCapacityUnits: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "ReadCapacityUnits"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-provisionedthroughput.html#cfn-dynamodb-provisionedthroughput-readcapacityunits"""
    rp_WriteCapacityUnits: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "WriteCapacityUnits"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-provisionedthroughput.html#cfn-dynamodb-provisionedthroughput-writecapacityunits"""

@attr.s
class PropTableProjection(Property):
    """
    AWS Object Type = "AWS::DynamoDB::Table.Projection"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-projectionobject.html

    Property Document:
    
    - ``p_NonKeyAttributes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-projectionobject.html#cfn-dynamodb-projectionobj-nonkeyatt
    - ``p_ProjectionType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-projectionobject.html#cfn-dynamodb-projectionobj-projtype
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::Table.Projection"
    
    p_NonKeyAttributes: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "NonKeyAttributes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-projectionobject.html#cfn-dynamodb-projectionobj-nonkeyatt"""
    p_ProjectionType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ProjectionType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-projectionobject.html#cfn-dynamodb-projectionobj-projtype"""

@attr.s
class PropGlobalTableTimeToLiveSpecification(Property):
    """
    AWS Object Type = "AWS::DynamoDB::GlobalTable.TimeToLiveSpecification"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-timetolivespecification.html

    Property Document:
    
    - ``rp_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-timetolivespecification.html#cfn-dynamodb-globaltable-timetolivespecification-enabled
    - ``p_AttributeName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-timetolivespecification.html#cfn-dynamodb-globaltable-timetolivespecification-attributename
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::GlobalTable.TimeToLiveSpecification"
    
    rp_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-timetolivespecification.html#cfn-dynamodb-globaltable-timetolivespecification-enabled"""
    p_AttributeName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AttributeName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-timetolivespecification.html#cfn-dynamodb-globaltable-timetolivespecification-attributename"""

@attr.s
class PropGlobalTableReplicaSSESpecification(Property):
    """
    AWS Object Type = "AWS::DynamoDB::GlobalTable.ReplicaSSESpecification"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicassespecification.html

    Property Document:
    
    - ``rp_KMSMasterKeyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicassespecification.html#cfn-dynamodb-globaltable-replicassespecification-kmsmasterkeyid
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::GlobalTable.ReplicaSSESpecification"
    
    rp_KMSMasterKeyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "KMSMasterKeyId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicassespecification.html#cfn-dynamodb-globaltable-replicassespecification-kmsmasterkeyid"""

@attr.s
class PropTableStreamSpecification(Property):
    """
    AWS Object Type = "AWS::DynamoDB::Table.StreamSpecification"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-streamspecification.html

    Property Document:
    
    - ``rp_StreamViewType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-streamspecification.html#cfn-dynamodb-streamspecification-streamviewtype
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::Table.StreamSpecification"
    
    rp_StreamViewType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "StreamViewType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-streamspecification.html#cfn-dynamodb-streamspecification-streamviewtype"""

@attr.s
class PropTableLocalSecondaryIndex(Property):
    """
    AWS Object Type = "AWS::DynamoDB::Table.LocalSecondaryIndex"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-lsi.html

    Property Document:
    
    - ``rp_IndexName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-lsi.html#cfn-dynamodb-lsi-indexname
    - ``rp_KeySchema``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-lsi.html#cfn-dynamodb-lsi-keyschema
    - ``rp_Projection``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-lsi.html#cfn-dynamodb-lsi-projection
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::Table.LocalSecondaryIndex"
    
    rp_IndexName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "IndexName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-lsi.html#cfn-dynamodb-lsi-indexname"""
    rp_KeySchema: typing.List[typing.Union['PropTableKeySchema', dict]] = attr.ib(
        default=None,
        converter=PropTableKeySchema.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTableKeySchema), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "KeySchema"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-lsi.html#cfn-dynamodb-lsi-keyschema"""
    rp_Projection: typing.Union['PropTableProjection', dict] = attr.ib(
        default=None,
        converter=PropTableProjection.from_dict,
        validator=attr.validators.instance_of(PropTableProjection),
        metadata={AttrMeta.PROPERTY_NAME: "Projection"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-lsi.html#cfn-dynamodb-lsi-projection"""

@attr.s
class PropGlobalTableCapacityAutoScalingSettings(Property):
    """
    AWS Object Type = "AWS::DynamoDB::GlobalTable.CapacityAutoScalingSettings"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-capacityautoscalingsettings.html

    Property Document:
    
    - ``rp_MaxCapacity``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-capacityautoscalingsettings.html#cfn-dynamodb-globaltable-capacityautoscalingsettings-maxcapacity
    - ``rp_MinCapacity``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-capacityautoscalingsettings.html#cfn-dynamodb-globaltable-capacityautoscalingsettings-mincapacity
    - ``rp_TargetTrackingScalingPolicyConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-capacityautoscalingsettings.html#cfn-dynamodb-globaltable-capacityautoscalingsettings-targettrackingscalingpolicyconfiguration
    - ``p_SeedCapacity``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-capacityautoscalingsettings.html#cfn-dynamodb-globaltable-capacityautoscalingsettings-seedcapacity
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::GlobalTable.CapacityAutoScalingSettings"
    
    rp_MaxCapacity: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "MaxCapacity"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-capacityautoscalingsettings.html#cfn-dynamodb-globaltable-capacityautoscalingsettings-maxcapacity"""
    rp_MinCapacity: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "MinCapacity"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-capacityautoscalingsettings.html#cfn-dynamodb-globaltable-capacityautoscalingsettings-mincapacity"""
    rp_TargetTrackingScalingPolicyConfiguration: typing.Union['PropGlobalTableTargetTrackingScalingPolicyConfiguration', dict] = attr.ib(
        default=None,
        converter=PropGlobalTableTargetTrackingScalingPolicyConfiguration.from_dict,
        validator=attr.validators.instance_of(PropGlobalTableTargetTrackingScalingPolicyConfiguration),
        metadata={AttrMeta.PROPERTY_NAME: "TargetTrackingScalingPolicyConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-capacityautoscalingsettings.html#cfn-dynamodb-globaltable-capacityautoscalingsettings-targettrackingscalingpolicyconfiguration"""
    p_SeedCapacity: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "SeedCapacity"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-capacityautoscalingsettings.html#cfn-dynamodb-globaltable-capacityautoscalingsettings-seedcapacity"""

@attr.s
class PropGlobalTableReadProvisionedThroughputSettings(Property):
    """
    AWS Object Type = "AWS::DynamoDB::GlobalTable.ReadProvisionedThroughputSettings"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-readprovisionedthroughputsettings.html

    Property Document:
    
    - ``p_ReadCapacityAutoScalingSettings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-readprovisionedthroughputsettings.html#cfn-dynamodb-globaltable-readprovisionedthroughputsettings-readcapacityautoscalingsettings
    - ``p_ReadCapacityUnits``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-readprovisionedthroughputsettings.html#cfn-dynamodb-globaltable-readprovisionedthroughputsettings-readcapacityunits
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::GlobalTable.ReadProvisionedThroughputSettings"
    
    p_ReadCapacityAutoScalingSettings: typing.Union['PropGlobalTableCapacityAutoScalingSettings', dict] = attr.ib(
        default=None,
        converter=PropGlobalTableCapacityAutoScalingSettings.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGlobalTableCapacityAutoScalingSettings)),
        metadata={AttrMeta.PROPERTY_NAME: "ReadCapacityAutoScalingSettings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-readprovisionedthroughputsettings.html#cfn-dynamodb-globaltable-readprovisionedthroughputsettings-readcapacityautoscalingsettings"""
    p_ReadCapacityUnits: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ReadCapacityUnits"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-readprovisionedthroughputsettings.html#cfn-dynamodb-globaltable-readprovisionedthroughputsettings-readcapacityunits"""

@attr.s
class PropGlobalTableLocalSecondaryIndex(Property):
    """
    AWS Object Type = "AWS::DynamoDB::GlobalTable.LocalSecondaryIndex"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-localsecondaryindex.html

    Property Document:
    
    - ``rp_IndexName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-localsecondaryindex.html#cfn-dynamodb-globaltable-localsecondaryindex-indexname
    - ``rp_KeySchema``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-localsecondaryindex.html#cfn-dynamodb-globaltable-localsecondaryindex-keyschema
    - ``rp_Projection``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-localsecondaryindex.html#cfn-dynamodb-globaltable-localsecondaryindex-projection
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::GlobalTable.LocalSecondaryIndex"
    
    rp_IndexName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "IndexName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-localsecondaryindex.html#cfn-dynamodb-globaltable-localsecondaryindex-indexname"""
    rp_KeySchema: typing.List[typing.Union['PropGlobalTableKeySchema', dict]] = attr.ib(
        default=None,
        converter=PropGlobalTableKeySchema.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropGlobalTableKeySchema), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "KeySchema"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-localsecondaryindex.html#cfn-dynamodb-globaltable-localsecondaryindex-keyschema"""
    rp_Projection: typing.Union['PropGlobalTableProjection', dict] = attr.ib(
        default=None,
        converter=PropGlobalTableProjection.from_dict,
        validator=attr.validators.instance_of(PropGlobalTableProjection),
        metadata={AttrMeta.PROPERTY_NAME: "Projection"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-localsecondaryindex.html#cfn-dynamodb-globaltable-localsecondaryindex-projection"""

@attr.s
class PropTableGlobalSecondaryIndex(Property):
    """
    AWS Object Type = "AWS::DynamoDB::Table.GlobalSecondaryIndex"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html

    Property Document:
    
    - ``rp_IndexName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html#cfn-dynamodb-gsi-indexname
    - ``rp_KeySchema``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html#cfn-dynamodb-gsi-keyschema
    - ``rp_Projection``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html#cfn-dynamodb-gsi-projection
    - ``p_ContributorInsightsSpecification``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html#cfn-dynamodb-contributorinsightsspecification-enabled
    - ``p_ProvisionedThroughput``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html#cfn-dynamodb-gsi-provisionedthroughput
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::Table.GlobalSecondaryIndex"
    
    rp_IndexName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "IndexName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html#cfn-dynamodb-gsi-indexname"""
    rp_KeySchema: typing.List[typing.Union['PropTableKeySchema', dict]] = attr.ib(
        default=None,
        converter=PropTableKeySchema.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTableKeySchema), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "KeySchema"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html#cfn-dynamodb-gsi-keyschema"""
    rp_Projection: typing.Union['PropTableProjection', dict] = attr.ib(
        default=None,
        converter=PropTableProjection.from_dict,
        validator=attr.validators.instance_of(PropTableProjection),
        metadata={AttrMeta.PROPERTY_NAME: "Projection"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html#cfn-dynamodb-gsi-projection"""
    p_ContributorInsightsSpecification: typing.Union['PropTableContributorInsightsSpecification', dict] = attr.ib(
        default=None,
        converter=PropTableContributorInsightsSpecification.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTableContributorInsightsSpecification)),
        metadata={AttrMeta.PROPERTY_NAME: "ContributorInsightsSpecification"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html#cfn-dynamodb-contributorinsightsspecification-enabled"""
    p_ProvisionedThroughput: typing.Union['PropTableProvisionedThroughput', dict] = attr.ib(
        default=None,
        converter=PropTableProvisionedThroughput.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTableProvisionedThroughput)),
        metadata={AttrMeta.PROPERTY_NAME: "ProvisionedThroughput"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html#cfn-dynamodb-gsi-provisionedthroughput"""

@attr.s
class PropGlobalTableReplicaGlobalSecondaryIndexSpecification(Property):
    """
    AWS Object Type = "AWS::DynamoDB::GlobalTable.ReplicaGlobalSecondaryIndexSpecification"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaglobalsecondaryindexspecification.html

    Property Document:
    
    - ``rp_IndexName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaglobalsecondaryindexspecification.html#cfn-dynamodb-globaltable-replicaglobalsecondaryindexspecification-indexname
    - ``p_ContributorInsightsSpecification``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaglobalsecondaryindexspecification.html#cfn-dynamodb-globaltable-replicaglobalsecondaryindexspecification-contributorinsightsspecification
    - ``p_ReadProvisionedThroughputSettings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaglobalsecondaryindexspecification.html#cfn-dynamodb-globaltable-replicaglobalsecondaryindexspecification-readprovisionedthroughputsettings
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::GlobalTable.ReplicaGlobalSecondaryIndexSpecification"
    
    rp_IndexName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "IndexName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaglobalsecondaryindexspecification.html#cfn-dynamodb-globaltable-replicaglobalsecondaryindexspecification-indexname"""
    p_ContributorInsightsSpecification: typing.Union['PropGlobalTableContributorInsightsSpecification', dict] = attr.ib(
        default=None,
        converter=PropGlobalTableContributorInsightsSpecification.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGlobalTableContributorInsightsSpecification)),
        metadata={AttrMeta.PROPERTY_NAME: "ContributorInsightsSpecification"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaglobalsecondaryindexspecification.html#cfn-dynamodb-globaltable-replicaglobalsecondaryindexspecification-contributorinsightsspecification"""
    p_ReadProvisionedThroughputSettings: typing.Union['PropGlobalTableReadProvisionedThroughputSettings', dict] = attr.ib(
        default=None,
        converter=PropGlobalTableReadProvisionedThroughputSettings.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGlobalTableReadProvisionedThroughputSettings)),
        metadata={AttrMeta.PROPERTY_NAME: "ReadProvisionedThroughputSettings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaglobalsecondaryindexspecification.html#cfn-dynamodb-globaltable-replicaglobalsecondaryindexspecification-readprovisionedthroughputsettings"""

@attr.s
class PropGlobalTableWriteProvisionedThroughputSettings(Property):
    """
    AWS Object Type = "AWS::DynamoDB::GlobalTable.WriteProvisionedThroughputSettings"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-writeprovisionedthroughputsettings.html

    Property Document:
    
    - ``p_WriteCapacityAutoScalingSettings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-writeprovisionedthroughputsettings.html#cfn-dynamodb-globaltable-writeprovisionedthroughputsettings-writecapacityautoscalingsettings
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::GlobalTable.WriteProvisionedThroughputSettings"
    
    p_WriteCapacityAutoScalingSettings: typing.Union['PropGlobalTableCapacityAutoScalingSettings', dict] = attr.ib(
        default=None,
        converter=PropGlobalTableCapacityAutoScalingSettings.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGlobalTableCapacityAutoScalingSettings)),
        metadata={AttrMeta.PROPERTY_NAME: "WriteCapacityAutoScalingSettings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-writeprovisionedthroughputsettings.html#cfn-dynamodb-globaltable-writeprovisionedthroughputsettings-writecapacityautoscalingsettings"""

@attr.s
class PropGlobalTableReplicaSpecification(Property):
    """
    AWS Object Type = "AWS::DynamoDB::GlobalTable.ReplicaSpecification"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html

    Property Document:
    
    - ``rp_Region``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-region
    - ``p_ContributorInsightsSpecification``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-contributorinsightsspecification
    - ``p_GlobalSecondaryIndexes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-globalsecondaryindexes
    - ``p_PointInTimeRecoverySpecification``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-pointintimerecoveryspecification
    - ``p_ReadProvisionedThroughputSettings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-readprovisionedthroughputsettings
    - ``p_SSESpecification``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-ssespecification
    - ``p_TableClass``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-tableclass
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-tags
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::GlobalTable.ReplicaSpecification"
    
    rp_Region: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Region"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-region"""
    p_ContributorInsightsSpecification: typing.Union['PropGlobalTableContributorInsightsSpecification', dict] = attr.ib(
        default=None,
        converter=PropGlobalTableContributorInsightsSpecification.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGlobalTableContributorInsightsSpecification)),
        metadata={AttrMeta.PROPERTY_NAME: "ContributorInsightsSpecification"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-contributorinsightsspecification"""
    p_GlobalSecondaryIndexes: typing.List[typing.Union['PropGlobalTableReplicaGlobalSecondaryIndexSpecification', dict]] = attr.ib(
        default=None,
        converter=PropGlobalTableReplicaGlobalSecondaryIndexSpecification.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropGlobalTableReplicaGlobalSecondaryIndexSpecification), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "GlobalSecondaryIndexes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-globalsecondaryindexes"""
    p_PointInTimeRecoverySpecification: typing.Union['PropGlobalTablePointInTimeRecoverySpecification', dict] = attr.ib(
        default=None,
        converter=PropGlobalTablePointInTimeRecoverySpecification.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGlobalTablePointInTimeRecoverySpecification)),
        metadata={AttrMeta.PROPERTY_NAME: "PointInTimeRecoverySpecification"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-pointintimerecoveryspecification"""
    p_ReadProvisionedThroughputSettings: typing.Union['PropGlobalTableReadProvisionedThroughputSettings', dict] = attr.ib(
        default=None,
        converter=PropGlobalTableReadProvisionedThroughputSettings.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGlobalTableReadProvisionedThroughputSettings)),
        metadata={AttrMeta.PROPERTY_NAME: "ReadProvisionedThroughputSettings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-readprovisionedthroughputsettings"""
    p_SSESpecification: typing.Union['PropGlobalTableReplicaSSESpecification', dict] = attr.ib(
        default=None,
        converter=PropGlobalTableReplicaSSESpecification.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGlobalTableReplicaSSESpecification)),
        metadata={AttrMeta.PROPERTY_NAME: "SSESpecification"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-ssespecification"""
    p_TableClass: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TableClass"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-tableclass"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html#cfn-dynamodb-globaltable-replicaspecification-tags"""

@attr.s
class PropGlobalTableGlobalSecondaryIndex(Property):
    """
    AWS Object Type = "AWS::DynamoDB::GlobalTable.GlobalSecondaryIndex"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-globalsecondaryindex.html

    Property Document:
    
    - ``rp_IndexName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-globalsecondaryindex.html#cfn-dynamodb-globaltable-globalsecondaryindex-indexname
    - ``rp_KeySchema``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-globalsecondaryindex.html#cfn-dynamodb-globaltable-globalsecondaryindex-keyschema
    - ``rp_Projection``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-globalsecondaryindex.html#cfn-dynamodb-globaltable-globalsecondaryindex-projection
    - ``p_WriteProvisionedThroughputSettings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-globalsecondaryindex.html#cfn-dynamodb-globaltable-globalsecondaryindex-writeprovisionedthroughputsettings
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::GlobalTable.GlobalSecondaryIndex"
    
    rp_IndexName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "IndexName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-globalsecondaryindex.html#cfn-dynamodb-globaltable-globalsecondaryindex-indexname"""
    rp_KeySchema: typing.List[typing.Union['PropGlobalTableKeySchema', dict]] = attr.ib(
        default=None,
        converter=PropGlobalTableKeySchema.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropGlobalTableKeySchema), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "KeySchema"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-globalsecondaryindex.html#cfn-dynamodb-globaltable-globalsecondaryindex-keyschema"""
    rp_Projection: typing.Union['PropGlobalTableProjection', dict] = attr.ib(
        default=None,
        converter=PropGlobalTableProjection.from_dict,
        validator=attr.validators.instance_of(PropGlobalTableProjection),
        metadata={AttrMeta.PROPERTY_NAME: "Projection"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-globalsecondaryindex.html#cfn-dynamodb-globaltable-globalsecondaryindex-projection"""
    p_WriteProvisionedThroughputSettings: typing.Union['PropGlobalTableWriteProvisionedThroughputSettings', dict] = attr.ib(
        default=None,
        converter=PropGlobalTableWriteProvisionedThroughputSettings.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGlobalTableWriteProvisionedThroughputSettings)),
        metadata={AttrMeta.PROPERTY_NAME: "WriteProvisionedThroughputSettings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-globalsecondaryindex.html#cfn-dynamodb-globaltable-globalsecondaryindex-writeprovisionedthroughputsettings"""


#--- Resource declaration ---

@attr.s
class Table(Resource):
    """
    AWS Object Type = "AWS::DynamoDB::Table"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html

    Property Document:
    
    - ``rp_KeySchema``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-keyschema
    - ``p_AttributeDefinitions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-attributedef
    - ``p_BillingMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-billingmode
    - ``p_ContributorInsightsSpecification``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-contributorinsightsspecification-enabled
    - ``p_GlobalSecondaryIndexes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-gsi
    - ``p_KinesisStreamSpecification``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-kinesisstreamspecification
    - ``p_LocalSecondaryIndexes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-lsi
    - ``p_PointInTimeRecoverySpecification``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-pointintimerecoveryspecification
    - ``p_ProvisionedThroughput``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-provisionedthroughput
    - ``p_SSESpecification``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-ssespecification
    - ``p_StreamSpecification``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-streamspecification
    - ``p_TableClass``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-tableclass
    - ``p_TableName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-tablename
    - ``p_TimeToLiveSpecification``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-timetolivespecification
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-tags
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::Table"

    
    rp_KeySchema: typing.List[typing.Union['PropTableKeySchema', dict]] = attr.ib(
        default=None,
        converter=PropTableKeySchema.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTableKeySchema), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "KeySchema"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-keyschema"""
    p_AttributeDefinitions: typing.List[typing.Union['PropTableAttributeDefinition', dict]] = attr.ib(
        default=None,
        converter=PropTableAttributeDefinition.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTableAttributeDefinition), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AttributeDefinitions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-attributedef"""
    p_BillingMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BillingMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-billingmode"""
    p_ContributorInsightsSpecification: typing.Union['PropTableContributorInsightsSpecification', dict] = attr.ib(
        default=None,
        converter=PropTableContributorInsightsSpecification.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTableContributorInsightsSpecification)),
        metadata={AttrMeta.PROPERTY_NAME: "ContributorInsightsSpecification"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-contributorinsightsspecification-enabled"""
    p_GlobalSecondaryIndexes: typing.List[typing.Union['PropTableGlobalSecondaryIndex', dict]] = attr.ib(
        default=None,
        converter=PropTableGlobalSecondaryIndex.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTableGlobalSecondaryIndex), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "GlobalSecondaryIndexes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-gsi"""
    p_KinesisStreamSpecification: typing.Union['PropTableKinesisStreamSpecification', dict] = attr.ib(
        default=None,
        converter=PropTableKinesisStreamSpecification.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTableKinesisStreamSpecification)),
        metadata={AttrMeta.PROPERTY_NAME: "KinesisStreamSpecification"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-kinesisstreamspecification"""
    p_LocalSecondaryIndexes: typing.List[typing.Union['PropTableLocalSecondaryIndex', dict]] = attr.ib(
        default=None,
        converter=PropTableLocalSecondaryIndex.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTableLocalSecondaryIndex), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "LocalSecondaryIndexes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-lsi"""
    p_PointInTimeRecoverySpecification: typing.Union['PropTablePointInTimeRecoverySpecification', dict] = attr.ib(
        default=None,
        converter=PropTablePointInTimeRecoverySpecification.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTablePointInTimeRecoverySpecification)),
        metadata={AttrMeta.PROPERTY_NAME: "PointInTimeRecoverySpecification"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-pointintimerecoveryspecification"""
    p_ProvisionedThroughput: typing.Union['PropTableProvisionedThroughput', dict] = attr.ib(
        default=None,
        converter=PropTableProvisionedThroughput.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTableProvisionedThroughput)),
        metadata={AttrMeta.PROPERTY_NAME: "ProvisionedThroughput"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-provisionedthroughput"""
    p_SSESpecification: typing.Union['PropTableSSESpecification', dict] = attr.ib(
        default=None,
        converter=PropTableSSESpecification.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTableSSESpecification)),
        metadata={AttrMeta.PROPERTY_NAME: "SSESpecification"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-ssespecification"""
    p_StreamSpecification: typing.Union['PropTableStreamSpecification', dict] = attr.ib(
        default=None,
        converter=PropTableStreamSpecification.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTableStreamSpecification)),
        metadata={AttrMeta.PROPERTY_NAME: "StreamSpecification"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-streamspecification"""
    p_TableClass: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TableClass"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-tableclass"""
    p_TableName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TableName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-tablename"""
    p_TimeToLiveSpecification: typing.Union['PropTableTimeToLiveSpecification', dict] = attr.ib(
        default=None,
        converter=PropTableTimeToLiveSpecification.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTableTimeToLiveSpecification)),
        metadata={AttrMeta.PROPERTY_NAME: "TimeToLiveSpecification"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-timetolivespecification"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#aws-resource-dynamodb-table-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_StreamArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#aws-resource-dynamodb-table-return-values"""
        return GetAtt(resource=self, attr_name="StreamArn")
    

@attr.s
class GlobalTable(Resource):
    """
    AWS Object Type = "AWS::DynamoDB::GlobalTable"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html

    Property Document:
    
    - ``rp_AttributeDefinitions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-attributedefinitions
    - ``rp_KeySchema``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-keyschema
    - ``rp_Replicas``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-replicas
    - ``p_BillingMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-billingmode
    - ``p_GlobalSecondaryIndexes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-globalsecondaryindexes
    - ``p_LocalSecondaryIndexes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-localsecondaryindexes
    - ``p_SSESpecification``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-ssespecification
    - ``p_StreamSpecification``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-streamspecification
    - ``p_TableName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-tablename
    - ``p_TimeToLiveSpecification``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-timetolivespecification
    - ``p_WriteProvisionedThroughputSettings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-writeprovisionedthroughputsettings
    """
    AWS_OBJECT_TYPE = "AWS::DynamoDB::GlobalTable"

    
    rp_AttributeDefinitions: typing.List[typing.Union['PropGlobalTableAttributeDefinition', dict]] = attr.ib(
        default=None,
        converter=PropGlobalTableAttributeDefinition.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropGlobalTableAttributeDefinition), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "AttributeDefinitions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-attributedefinitions"""
    rp_KeySchema: typing.List[typing.Union['PropGlobalTableKeySchema', dict]] = attr.ib(
        default=None,
        converter=PropGlobalTableKeySchema.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropGlobalTableKeySchema), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "KeySchema"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-keyschema"""
    rp_Replicas: typing.List[typing.Union['PropGlobalTableReplicaSpecification', dict]] = attr.ib(
        default=None,
        converter=PropGlobalTableReplicaSpecification.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropGlobalTableReplicaSpecification), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Replicas"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-replicas"""
    p_BillingMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BillingMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-billingmode"""
    p_GlobalSecondaryIndexes: typing.List[typing.Union['PropGlobalTableGlobalSecondaryIndex', dict]] = attr.ib(
        default=None,
        converter=PropGlobalTableGlobalSecondaryIndex.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropGlobalTableGlobalSecondaryIndex), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "GlobalSecondaryIndexes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-globalsecondaryindexes"""
    p_LocalSecondaryIndexes: typing.List[typing.Union['PropGlobalTableLocalSecondaryIndex', dict]] = attr.ib(
        default=None,
        converter=PropGlobalTableLocalSecondaryIndex.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropGlobalTableLocalSecondaryIndex), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "LocalSecondaryIndexes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-localsecondaryindexes"""
    p_SSESpecification: typing.Union['PropGlobalTableSSESpecification', dict] = attr.ib(
        default=None,
        converter=PropGlobalTableSSESpecification.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGlobalTableSSESpecification)),
        metadata={AttrMeta.PROPERTY_NAME: "SSESpecification"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-ssespecification"""
    p_StreamSpecification: typing.Union['PropGlobalTableStreamSpecification', dict] = attr.ib(
        default=None,
        converter=PropGlobalTableStreamSpecification.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGlobalTableStreamSpecification)),
        metadata={AttrMeta.PROPERTY_NAME: "StreamSpecification"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-streamspecification"""
    p_TableName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TableName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-tablename"""
    p_TimeToLiveSpecification: typing.Union['PropGlobalTableTimeToLiveSpecification', dict] = attr.ib(
        default=None,
        converter=PropGlobalTableTimeToLiveSpecification.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGlobalTableTimeToLiveSpecification)),
        metadata={AttrMeta.PROPERTY_NAME: "TimeToLiveSpecification"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-timetolivespecification"""
    p_WriteProvisionedThroughputSettings: typing.Union['PropGlobalTableWriteProvisionedThroughputSettings', dict] = attr.ib(
        default=None,
        converter=PropGlobalTableWriteProvisionedThroughputSettings.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGlobalTableWriteProvisionedThroughputSettings)),
        metadata={AttrMeta.PROPERTY_NAME: "WriteProvisionedThroughputSettings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#cfn-dynamodb-globaltable-writeprovisionedthroughputsettings"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#aws-resource-dynamodb-globaltable-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_StreamArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#aws-resource-dynamodb-globaltable-return-values"""
        return GetAtt(resource=self, attr_name="StreamArn")
    
    @property
    def rv_TableId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html#aws-resource-dynamodb-globaltable-return-values"""
        return GetAtt(resource=self, attr_name="TableId")
    
