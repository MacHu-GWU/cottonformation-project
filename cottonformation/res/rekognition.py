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
class PropStreamProcessorPoint(Property):
    """
    AWS Object Type = "AWS::Rekognition::StreamProcessor.Point"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-point.html

    Property Document:
    
    - ``rp_X``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-point.html#cfn-rekognition-streamprocessor-x
    - ``rp_Y``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-point.html#cfn-rekognition-streamprocessor-y
    """
    AWS_OBJECT_TYPE = "AWS::Rekognition::StreamProcessor.Point"
    
    rp_X: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "X"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-point.html#cfn-rekognition-streamprocessor-x"""
    rp_Y: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Y"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-point.html#cfn-rekognition-streamprocessor-y"""

@attr.s
class PropStreamProcessorKinesisDataStream(Property):
    """
    AWS Object Type = "AWS::Rekognition::StreamProcessor.KinesisDataStream"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-kinesisdatastream.html

    Property Document:
    
    - ``rp_Arn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-kinesisdatastream.html#cfn-rekognition-streamprocessor-kinesisdatastream-arn
    """
    AWS_OBJECT_TYPE = "AWS::Rekognition::StreamProcessor.KinesisDataStream"
    
    rp_Arn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Arn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-kinesisdatastream.html#cfn-rekognition-streamprocessor-kinesisdatastream-arn"""

@attr.s
class PropStreamProcessorFaceSearchSettings(Property):
    """
    AWS Object Type = "AWS::Rekognition::StreamProcessor.FaceSearchSettings"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-facesearchsettings.html

    Property Document:
    
    - ``rp_CollectionId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-facesearchsettings.html#cfn-rekognition-streamprocessor-facesearchsettings-collectionid
    - ``p_FaceMatchThreshold``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-facesearchsettings.html#cfn-rekognition-streamprocessor-facesearchsettings-facematchthreshold
    """
    AWS_OBJECT_TYPE = "AWS::Rekognition::StreamProcessor.FaceSearchSettings"
    
    rp_CollectionId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "CollectionId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-facesearchsettings.html#cfn-rekognition-streamprocessor-facesearchsettings-collectionid"""
    p_FaceMatchThreshold: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "FaceMatchThreshold"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-facesearchsettings.html#cfn-rekognition-streamprocessor-facesearchsettings-facematchthreshold"""

@attr.s
class PropStreamProcessorDataSharingPreference(Property):
    """
    AWS Object Type = "AWS::Rekognition::StreamProcessor.DataSharingPreference"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-datasharingpreference.html

    Property Document:
    
    - ``rp_OptIn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-datasharingpreference.html#cfn-rekognition-streamprocessor-datasharingpreference-optin
    """
    AWS_OBJECT_TYPE = "AWS::Rekognition::StreamProcessor.DataSharingPreference"
    
    rp_OptIn: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "OptIn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-datasharingpreference.html#cfn-rekognition-streamprocessor-datasharingpreference-optin"""

@attr.s
class PropStreamProcessorBoundingBox(Property):
    """
    AWS Object Type = "AWS::Rekognition::StreamProcessor.BoundingBox"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-boundingbox.html

    Property Document:
    
    - ``rp_Height``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-boundingbox.html#cfn-rekognition-streamprocessor-boundingbox-height
    - ``rp_Left``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-boundingbox.html#cfn-rekognition-streamprocessor-boundingbox-left
    - ``rp_Top``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-boundingbox.html#cfn-rekognition-streamprocessor-boundingbox-top
    - ``rp_Width``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-boundingbox.html#cfn-rekognition-streamprocessor-boundingbox-width
    """
    AWS_OBJECT_TYPE = "AWS::Rekognition::StreamProcessor.BoundingBox"
    
    rp_Height: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "Height"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-boundingbox.html#cfn-rekognition-streamprocessor-boundingbox-height"""
    rp_Left: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "Left"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-boundingbox.html#cfn-rekognition-streamprocessor-boundingbox-left"""
    rp_Top: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "Top"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-boundingbox.html#cfn-rekognition-streamprocessor-boundingbox-top"""
    rp_Width: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "Width"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-boundingbox.html#cfn-rekognition-streamprocessor-boundingbox-width"""

@attr.s
class PropStreamProcessorPolygon(Property):
    """
    AWS Object Type = "AWS::Rekognition::StreamProcessor.Polygon"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-polygon.html

    Property Document:
    
    - ``rp_Polygon``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-polygon.html#cfn-rekognition-streamprocessor-polygon
    """
    AWS_OBJECT_TYPE = "AWS::Rekognition::StreamProcessor.Polygon"
    
    rp_Polygon: typing.List[typing.Union['PropStreamProcessorPoint', dict]] = attr.ib(
        default=None,
        converter=PropStreamProcessorPoint.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropStreamProcessorPoint), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Polygon"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-polygon.html#cfn-rekognition-streamprocessor-polygon"""

@attr.s
class PropStreamProcessorConnectedHomeSettings(Property):
    """
    AWS Object Type = "AWS::Rekognition::StreamProcessor.ConnectedHomeSettings"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-connectedhomesettings.html

    Property Document:
    
    - ``rp_Labels``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-connectedhomesettings.html#cfn-rekognition-streamprocessor-connectedhomesettings-labels
    - ``p_MinConfidence``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-connectedhomesettings.html#cfn-rekognition-streamprocessor-connectedhomesettings-minconfidence
    """
    AWS_OBJECT_TYPE = "AWS::Rekognition::StreamProcessor.ConnectedHomeSettings"
    
    rp_Labels: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Labels"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-connectedhomesettings.html#cfn-rekognition-streamprocessor-connectedhomesettings-labels"""
    p_MinConfidence: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "MinConfidence"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-connectedhomesettings.html#cfn-rekognition-streamprocessor-connectedhomesettings-minconfidence"""

@attr.s
class PropStreamProcessorS3Destination(Property):
    """
    AWS Object Type = "AWS::Rekognition::StreamProcessor.S3Destination"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-s3destination.html

    Property Document:
    
    - ``rp_BucketName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-s3destination.html#cfn-rekognition-streamprocessor-s3destination-bucketname
    - ``p_ObjectKeyPrefix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-s3destination.html#cfn-rekognition-streamprocessor-s3destination-objectkeyprefix
    """
    AWS_OBJECT_TYPE = "AWS::Rekognition::StreamProcessor.S3Destination"
    
    rp_BucketName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "BucketName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-s3destination.html#cfn-rekognition-streamprocessor-s3destination-bucketname"""
    p_ObjectKeyPrefix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ObjectKeyPrefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-s3destination.html#cfn-rekognition-streamprocessor-s3destination-objectkeyprefix"""

@attr.s
class PropStreamProcessorNotificationChannel(Property):
    """
    AWS Object Type = "AWS::Rekognition::StreamProcessor.NotificationChannel"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-notificationchannel.html

    Property Document:
    
    - ``rp_Arn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-notificationchannel.html#cfn-rekognition-streamprocessor-notificationchannel-arn
    """
    AWS_OBJECT_TYPE = "AWS::Rekognition::StreamProcessor.NotificationChannel"
    
    rp_Arn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Arn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-notificationchannel.html#cfn-rekognition-streamprocessor-notificationchannel-arn"""

@attr.s
class PropStreamProcessorKinesisVideoStream(Property):
    """
    AWS Object Type = "AWS::Rekognition::StreamProcessor.KinesisVideoStream"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-kinesisvideostream.html

    Property Document:
    
    - ``rp_Arn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-kinesisvideostream.html#cfn-rekognition-streamprocessor-kinesisvideostream-arn
    """
    AWS_OBJECT_TYPE = "AWS::Rekognition::StreamProcessor.KinesisVideoStream"
    
    rp_Arn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Arn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-kinesisvideostream.html#cfn-rekognition-streamprocessor-kinesisvideostream-arn"""


#--- Resource declaration ---

@attr.s
class Collection(Resource):
    """
    AWS Object Type = "AWS::Rekognition::Collection"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-collection.html

    Property Document:
    
    - ``rp_CollectionId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-collection.html#cfn-rekognition-collection-collectionid
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-collection.html#cfn-rekognition-collection-tags
    """
    AWS_OBJECT_TYPE = "AWS::Rekognition::Collection"

    
    rp_CollectionId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={
            AttrMeta.PROPERTY_NAME: "CollectionId",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": True,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-collection.html#cfn-rekognition-collection-collectionid"""
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
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-collection.html#cfn-rekognition-collection-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-collection.html#aws-resource-rekognition-collection-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class Project(Resource):
    """
    AWS Object Type = "AWS::Rekognition::Project"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-project.html

    Property Document:
    
    - ``rp_ProjectName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-project.html#cfn-rekognition-project-projectname
    """
    AWS_OBJECT_TYPE = "AWS::Rekognition::Project"

    
    rp_ProjectName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={
            AttrMeta.PROPERTY_NAME: "ProjectName",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": True,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-project.html#cfn-rekognition-project-projectname"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-project.html#aws-resource-rekognition-project-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class StreamProcessor(Resource):
    """
    AWS Object Type = "AWS::Rekognition::StreamProcessor"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html

    Property Document:
    
    - ``rp_KinesisVideoStream``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-kinesisvideostream
    - ``rp_RoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-rolearn
    - ``p_BoundingBoxRegionsOfInterest``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-boundingboxregionsofinterest
    - ``p_ConnectedHomeSettings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-connectedhomesettings
    - ``p_DataSharingPreference``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-datasharingpreference
    - ``p_FaceSearchSettings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-facesearchsettings
    - ``p_KinesisDataStream``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-kinesisdatastream
    - ``p_KmsKeyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-kmskeyid
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-name
    - ``p_NotificationChannel``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-notificationchannel
    - ``p_PolygonRegionsOfInterest``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-polygonregionsofinterest
    - ``p_S3Destination``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-s3destination
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-tags
    """
    AWS_OBJECT_TYPE = "AWS::Rekognition::StreamProcessor"

    
    rp_KinesisVideoStream: typing.Union['PropStreamProcessorKinesisVideoStream', dict] = attr.ib(
        default=None,
        converter=PropStreamProcessorKinesisVideoStream.from_dict,
        validator=attr.validators.instance_of(PropStreamProcessorKinesisVideoStream),
        metadata={
            AttrMeta.PROPERTY_NAME: "KinesisVideoStream",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": True,
                "Type": 'KinesisVideoStream',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-kinesisvideostream"""
    rp_RoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={
            AttrMeta.PROPERTY_NAME: "RoleArn",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": True,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-rolearn"""
    p_BoundingBoxRegionsOfInterest: typing.List[typing.Union['PropStreamProcessorBoundingBox', dict]] = attr.ib(
        default=None,
        converter=PropStreamProcessorBoundingBox.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropStreamProcessorBoundingBox), iterable_validator=attr.validators.instance_of(list))),
        metadata={
            AttrMeta.PROPERTY_NAME: "BoundingBoxRegionsOfInterest",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "Type": 'List',
                "ItemType": 'BoundingBox',
                "DuplicatesAllowed": False,
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-boundingboxregionsofinterest"""
    p_ConnectedHomeSettings: typing.Union['PropStreamProcessorConnectedHomeSettings', dict] = attr.ib(
        default=None,
        converter=PropStreamProcessorConnectedHomeSettings.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropStreamProcessorConnectedHomeSettings)),
        metadata={
            AttrMeta.PROPERTY_NAME: "ConnectedHomeSettings",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "Type": 'ConnectedHomeSettings',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-connectedhomesettings"""
    p_DataSharingPreference: typing.Union['PropStreamProcessorDataSharingPreference', dict] = attr.ib(
        default=None,
        converter=PropStreamProcessorDataSharingPreference.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropStreamProcessorDataSharingPreference)),
        metadata={
            AttrMeta.PROPERTY_NAME: "DataSharingPreference",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "Type": 'DataSharingPreference',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-datasharingpreference"""
    p_FaceSearchSettings: typing.Union['PropStreamProcessorFaceSearchSettings', dict] = attr.ib(
        default=None,
        converter=PropStreamProcessorFaceSearchSettings.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropStreamProcessorFaceSearchSettings)),
        metadata={
            AttrMeta.PROPERTY_NAME: "FaceSearchSettings",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "Type": 'FaceSearchSettings',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-facesearchsettings"""
    p_KinesisDataStream: typing.Union['PropStreamProcessorKinesisDataStream', dict] = attr.ib(
        default=None,
        converter=PropStreamProcessorKinesisDataStream.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropStreamProcessorKinesisDataStream)),
        metadata={
            AttrMeta.PROPERTY_NAME: "KinesisDataStream",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "Type": 'KinesisDataStream',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-kinesisdatastream"""
    p_KmsKeyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "KmsKeyId",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-kmskeyid"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "Name",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-name"""
    p_NotificationChannel: typing.Union['PropStreamProcessorNotificationChannel', dict] = attr.ib(
        default=None,
        converter=PropStreamProcessorNotificationChannel.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropStreamProcessorNotificationChannel)),
        metadata={
            AttrMeta.PROPERTY_NAME: "NotificationChannel",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "Type": 'NotificationChannel',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-notificationchannel"""
    p_PolygonRegionsOfInterest: typing.List[typing.Union['PropStreamProcessorPolygon', dict]] = attr.ib(
        default=None,
        converter=PropStreamProcessorPolygon.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropStreamProcessorPolygon), iterable_validator=attr.validators.instance_of(list))),
        metadata={
            AttrMeta.PROPERTY_NAME: "PolygonRegionsOfInterest",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "Type": 'List',
                "ItemType": 'Polygon',
                "DuplicatesAllowed": False,
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-polygonregionsofinterest"""
    p_S3Destination: typing.Union['PropStreamProcessorS3Destination', dict] = attr.ib(
        default=None,
        converter=PropStreamProcessorS3Destination.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropStreamProcessorS3Destination)),
        metadata={
            AttrMeta.PROPERTY_NAME: "S3Destination",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "Type": 'S3Destination',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-s3destination"""
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
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#aws-resource-rekognition-streamprocessor-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_Status(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#aws-resource-rekognition-streamprocessor-return-values"""
        return GetAtt(resource=self, attr_name="Status")
    
    @property
    def rv_StatusMessage(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#aws-resource-rekognition-streamprocessor-return-values"""
        return GetAtt(resource=self, attr_name="StatusMessage")
    
