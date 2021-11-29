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
class PropOriginEndpointStreamSelection(Property):
    """
    AWS Object Type = "AWS::MediaPackage::OriginEndpoint.StreamSelection"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-streamselection.html

    Property Document:
    
    - ``p_MaxVideoBitsPerSecond``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-streamselection.html#cfn-mediapackage-originendpoint-streamselection-maxvideobitspersecond
    - ``p_MinVideoBitsPerSecond``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-streamselection.html#cfn-mediapackage-originendpoint-streamselection-minvideobitspersecond
    - ``p_StreamOrder``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-streamselection.html#cfn-mediapackage-originendpoint-streamselection-streamorder
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::OriginEndpoint.StreamSelection"
    
    p_MaxVideoBitsPerSecond: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MaxVideoBitsPerSecond"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-streamselection.html#cfn-mediapackage-originendpoint-streamselection-maxvideobitspersecond"""
    p_MinVideoBitsPerSecond: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MinVideoBitsPerSecond"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-streamselection.html#cfn-mediapackage-originendpoint-streamselection-minvideobitspersecond"""
    p_StreamOrder: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "StreamOrder"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-streamselection.html#cfn-mediapackage-originendpoint-streamselection-streamorder"""

@attr.s
class PropPackagingGroupLogConfiguration(Property):
    """
    AWS Object Type = "AWS::MediaPackage::PackagingGroup.LogConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packaginggroup-logconfiguration.html

    Property Document:
    
    - ``p_LogGroupName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packaginggroup-logconfiguration.html#cfn-mediapackage-packaginggroup-logconfiguration-loggroupname
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::PackagingGroup.LogConfiguration"
    
    p_LogGroupName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LogGroupName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packaginggroup-logconfiguration.html#cfn-mediapackage-packaginggroup-logconfiguration-loggroupname"""

@attr.s
class PropOriginEndpointAuthorization(Property):
    """
    AWS Object Type = "AWS::MediaPackage::OriginEndpoint.Authorization"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-authorization.html

    Property Document:
    
    - ``rp_CdnIdentifierSecret``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-authorization.html#cfn-mediapackage-originendpoint-authorization-cdnidentifiersecret
    - ``rp_SecretsRoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-authorization.html#cfn-mediapackage-originendpoint-authorization-secretsrolearn
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::OriginEndpoint.Authorization"
    
    rp_CdnIdentifierSecret: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "CdnIdentifierSecret"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-authorization.html#cfn-mediapackage-originendpoint-authorization-cdnidentifiersecret"""
    rp_SecretsRoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SecretsRoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-authorization.html#cfn-mediapackage-originendpoint-authorization-secretsrolearn"""

@attr.s
class PropPackagingConfigurationSpekeKeyProvider(Property):
    """
    AWS Object Type = "AWS::MediaPackage::PackagingConfiguration.SpekeKeyProvider"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-spekekeyprovider.html

    Property Document:
    
    - ``rp_RoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-spekekeyprovider.html#cfn-mediapackage-packagingconfiguration-spekekeyprovider-rolearn
    - ``rp_SystemIds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-spekekeyprovider.html#cfn-mediapackage-packagingconfiguration-spekekeyprovider-systemids
    - ``rp_Url``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-spekekeyprovider.html#cfn-mediapackage-packagingconfiguration-spekekeyprovider-url
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::PackagingConfiguration.SpekeKeyProvider"
    
    rp_RoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-spekekeyprovider.html#cfn-mediapackage-packagingconfiguration-spekekeyprovider-rolearn"""
    rp_SystemIds: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "SystemIds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-spekekeyprovider.html#cfn-mediapackage-packagingconfiguration-spekekeyprovider-systemids"""
    rp_Url: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Url"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-spekekeyprovider.html#cfn-mediapackage-packagingconfiguration-spekekeyprovider-url"""

@attr.s
class PropChannelLogConfiguration(Property):
    """
    AWS Object Type = "AWS::MediaPackage::Channel.LogConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-channel-logconfiguration.html

    Property Document:
    
    - ``p_LogGroupName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-channel-logconfiguration.html#cfn-mediapackage-channel-logconfiguration-loggroupname
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::Channel.LogConfiguration"
    
    p_LogGroupName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LogGroupName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-channel-logconfiguration.html#cfn-mediapackage-channel-logconfiguration-loggroupname"""

@attr.s
class PropPackagingConfigurationHlsEncryption(Property):
    """
    AWS Object Type = "AWS::MediaPackage::PackagingConfiguration.HlsEncryption"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsencryption.html

    Property Document:
    
    - ``rp_SpekeKeyProvider``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsencryption.html#cfn-mediapackage-packagingconfiguration-hlsencryption-spekekeyprovider
    - ``p_ConstantInitializationVector``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsencryption.html#cfn-mediapackage-packagingconfiguration-hlsencryption-constantinitializationvector
    - ``p_EncryptionMethod``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsencryption.html#cfn-mediapackage-packagingconfiguration-hlsencryption-encryptionmethod
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::PackagingConfiguration.HlsEncryption"
    
    rp_SpekeKeyProvider: typing.Union['PropPackagingConfigurationSpekeKeyProvider', dict] = attr.ib(
        default=None,
        converter=PropPackagingConfigurationSpekeKeyProvider.from_dict,
        validator=attr.validators.instance_of(PropPackagingConfigurationSpekeKeyProvider),
        metadata={AttrMeta.PROPERTY_NAME: "SpekeKeyProvider"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsencryption.html#cfn-mediapackage-packagingconfiguration-hlsencryption-spekekeyprovider"""
    p_ConstantInitializationVector: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ConstantInitializationVector"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsencryption.html#cfn-mediapackage-packagingconfiguration-hlsencryption-constantinitializationvector"""
    p_EncryptionMethod: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "EncryptionMethod"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsencryption.html#cfn-mediapackage-packagingconfiguration-hlsencryption-encryptionmethod"""

@attr.s
class PropPackagingGroupAuthorization(Property):
    """
    AWS Object Type = "AWS::MediaPackage::PackagingGroup.Authorization"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packaginggroup-authorization.html

    Property Document:
    
    - ``rp_CdnIdentifierSecret``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packaginggroup-authorization.html#cfn-mediapackage-packaginggroup-authorization-cdnidentifiersecret
    - ``rp_SecretsRoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packaginggroup-authorization.html#cfn-mediapackage-packaginggroup-authorization-secretsrolearn
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::PackagingGroup.Authorization"
    
    rp_CdnIdentifierSecret: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "CdnIdentifierSecret"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packaginggroup-authorization.html#cfn-mediapackage-packaginggroup-authorization-cdnidentifiersecret"""
    rp_SecretsRoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SecretsRoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packaginggroup-authorization.html#cfn-mediapackage-packaginggroup-authorization-secretsrolearn"""

@attr.s
class PropOriginEndpointHlsManifest(Property):
    """
    AWS Object Type = "AWS::MediaPackage::OriginEndpoint.HlsManifest"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html

    Property Document:
    
    - ``rp_Id``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-id
    - ``p_AdMarkers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-admarkers
    - ``p_AdTriggers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-adtriggers
    - ``p_AdsOnDeliveryRestrictions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-adsondeliveryrestrictions
    - ``p_IncludeIframeOnlyStream``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-includeiframeonlystream
    - ``p_ManifestName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-manifestname
    - ``p_PlaylistType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-playlisttype
    - ``p_PlaylistWindowSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-playlistwindowseconds
    - ``p_ProgramDateTimeIntervalSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-programdatetimeintervalseconds
    - ``p_Url``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-url
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::OriginEndpoint.HlsManifest"
    
    rp_Id: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Id"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-id"""
    p_AdMarkers: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AdMarkers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-admarkers"""
    p_AdTriggers: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AdTriggers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-adtriggers"""
    p_AdsOnDeliveryRestrictions: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AdsOnDeliveryRestrictions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-adsondeliveryrestrictions"""
    p_IncludeIframeOnlyStream: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IncludeIframeOnlyStream"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-includeiframeonlystream"""
    p_ManifestName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ManifestName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-manifestname"""
    p_PlaylistType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PlaylistType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-playlisttype"""
    p_PlaylistWindowSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "PlaylistWindowSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-playlistwindowseconds"""
    p_ProgramDateTimeIntervalSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ProgramDateTimeIntervalSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-programdatetimeintervalseconds"""
    p_Url: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Url"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-url"""

@attr.s
class PropPackagingConfigurationCmafEncryption(Property):
    """
    AWS Object Type = "AWS::MediaPackage::PackagingConfiguration.CmafEncryption"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafencryption.html

    Property Document:
    
    - ``rp_SpekeKeyProvider``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafencryption.html#cfn-mediapackage-packagingconfiguration-cmafencryption-spekekeyprovider
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::PackagingConfiguration.CmafEncryption"
    
    rp_SpekeKeyProvider: typing.Union['PropPackagingConfigurationSpekeKeyProvider', dict] = attr.ib(
        default=None,
        converter=PropPackagingConfigurationSpekeKeyProvider.from_dict,
        validator=attr.validators.instance_of(PropPackagingConfigurationSpekeKeyProvider),
        metadata={AttrMeta.PROPERTY_NAME: "SpekeKeyProvider"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafencryption.html#cfn-mediapackage-packagingconfiguration-cmafencryption-spekekeyprovider"""

@attr.s
class PropPackagingConfigurationMssEncryption(Property):
    """
    AWS Object Type = "AWS::MediaPackage::PackagingConfiguration.MssEncryption"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-mssencryption.html

    Property Document:
    
    - ``rp_SpekeKeyProvider``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-mssencryption.html#cfn-mediapackage-packagingconfiguration-mssencryption-spekekeyprovider
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::PackagingConfiguration.MssEncryption"
    
    rp_SpekeKeyProvider: typing.Union['PropPackagingConfigurationSpekeKeyProvider', dict] = attr.ib(
        default=None,
        converter=PropPackagingConfigurationSpekeKeyProvider.from_dict,
        validator=attr.validators.instance_of(PropPackagingConfigurationSpekeKeyProvider),
        metadata={AttrMeta.PROPERTY_NAME: "SpekeKeyProvider"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-mssencryption.html#cfn-mediapackage-packagingconfiguration-mssencryption-spekekeyprovider"""

@attr.s
class PropPackagingConfigurationStreamSelection(Property):
    """
    AWS Object Type = "AWS::MediaPackage::PackagingConfiguration.StreamSelection"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-streamselection.html

    Property Document:
    
    - ``p_MaxVideoBitsPerSecond``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-streamselection.html#cfn-mediapackage-packagingconfiguration-streamselection-maxvideobitspersecond
    - ``p_MinVideoBitsPerSecond``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-streamselection.html#cfn-mediapackage-packagingconfiguration-streamselection-minvideobitspersecond
    - ``p_StreamOrder``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-streamselection.html#cfn-mediapackage-packagingconfiguration-streamselection-streamorder
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::PackagingConfiguration.StreamSelection"
    
    p_MaxVideoBitsPerSecond: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MaxVideoBitsPerSecond"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-streamselection.html#cfn-mediapackage-packagingconfiguration-streamselection-maxvideobitspersecond"""
    p_MinVideoBitsPerSecond: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MinVideoBitsPerSecond"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-streamselection.html#cfn-mediapackage-packagingconfiguration-streamselection-minvideobitspersecond"""
    p_StreamOrder: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "StreamOrder"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-streamselection.html#cfn-mediapackage-packagingconfiguration-streamselection-streamorder"""

@attr.s
class PropAssetEgressEndpoint(Property):
    """
    AWS Object Type = "AWS::MediaPackage::Asset.EgressEndpoint"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-asset-egressendpoint.html

    Property Document:
    
    - ``rp_PackagingConfigurationId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-asset-egressendpoint.html#cfn-mediapackage-asset-egressendpoint-packagingconfigurationid
    - ``rp_Url``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-asset-egressendpoint.html#cfn-mediapackage-asset-egressendpoint-url
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::Asset.EgressEndpoint"
    
    rp_PackagingConfigurationId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PackagingConfigurationId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-asset-egressendpoint.html#cfn-mediapackage-asset-egressendpoint-packagingconfigurationid"""
    rp_Url: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Url"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-asset-egressendpoint.html#cfn-mediapackage-asset-egressendpoint-url"""

@attr.s
class PropOriginEndpointSpekeKeyProvider(Property):
    """
    AWS Object Type = "AWS::MediaPackage::OriginEndpoint.SpekeKeyProvider"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html

    Property Document:
    
    - ``rp_ResourceId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html#cfn-mediapackage-originendpoint-spekekeyprovider-resourceid
    - ``rp_RoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html#cfn-mediapackage-originendpoint-spekekeyprovider-rolearn
    - ``rp_SystemIds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html#cfn-mediapackage-originendpoint-spekekeyprovider-systemids
    - ``rp_Url``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html#cfn-mediapackage-originendpoint-spekekeyprovider-url
    - ``p_CertificateArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html#cfn-mediapackage-originendpoint-spekekeyprovider-certificatearn
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::OriginEndpoint.SpekeKeyProvider"
    
    rp_ResourceId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html#cfn-mediapackage-originendpoint-spekekeyprovider-resourceid"""
    rp_RoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html#cfn-mediapackage-originendpoint-spekekeyprovider-rolearn"""
    rp_SystemIds: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "SystemIds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html#cfn-mediapackage-originendpoint-spekekeyprovider-systemids"""
    rp_Url: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Url"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html#cfn-mediapackage-originendpoint-spekekeyprovider-url"""
    p_CertificateArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CertificateArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html#cfn-mediapackage-originendpoint-spekekeyprovider-certificatearn"""

@attr.s
class PropOriginEndpointCmafEncryption(Property):
    """
    AWS Object Type = "AWS::MediaPackage::OriginEndpoint.CmafEncryption"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafencryption.html

    Property Document:
    
    - ``rp_SpekeKeyProvider``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafencryption.html#cfn-mediapackage-originendpoint-cmafencryption-spekekeyprovider
    - ``p_ConstantInitializationVector``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafencryption.html#cfn-mediapackage-originendpoint-cmafencryption-constantinitializationvector
    - ``p_KeyRotationIntervalSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafencryption.html#cfn-mediapackage-originendpoint-cmafencryption-keyrotationintervalseconds
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::OriginEndpoint.CmafEncryption"
    
    rp_SpekeKeyProvider: typing.Union['PropOriginEndpointSpekeKeyProvider', dict] = attr.ib(
        default=None,
        converter=PropOriginEndpointSpekeKeyProvider.from_dict,
        validator=attr.validators.instance_of(PropOriginEndpointSpekeKeyProvider),
        metadata={AttrMeta.PROPERTY_NAME: "SpekeKeyProvider"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafencryption.html#cfn-mediapackage-originendpoint-cmafencryption-spekekeyprovider"""
    p_ConstantInitializationVector: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ConstantInitializationVector"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafencryption.html#cfn-mediapackage-originendpoint-cmafencryption-constantinitializationvector"""
    p_KeyRotationIntervalSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "KeyRotationIntervalSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafencryption.html#cfn-mediapackage-originendpoint-cmafencryption-keyrotationintervalseconds"""

@attr.s
class PropOriginEndpointHlsEncryption(Property):
    """
    AWS Object Type = "AWS::MediaPackage::OriginEndpoint.HlsEncryption"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html

    Property Document:
    
    - ``rp_SpekeKeyProvider``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html#cfn-mediapackage-originendpoint-hlsencryption-spekekeyprovider
    - ``p_ConstantInitializationVector``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html#cfn-mediapackage-originendpoint-hlsencryption-constantinitializationvector
    - ``p_EncryptionMethod``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html#cfn-mediapackage-originendpoint-hlsencryption-encryptionmethod
    - ``p_KeyRotationIntervalSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html#cfn-mediapackage-originendpoint-hlsencryption-keyrotationintervalseconds
    - ``p_RepeatExtXKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html#cfn-mediapackage-originendpoint-hlsencryption-repeatextxkey
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::OriginEndpoint.HlsEncryption"
    
    rp_SpekeKeyProvider: typing.Union['PropOriginEndpointSpekeKeyProvider', dict] = attr.ib(
        default=None,
        converter=PropOriginEndpointSpekeKeyProvider.from_dict,
        validator=attr.validators.instance_of(PropOriginEndpointSpekeKeyProvider),
        metadata={AttrMeta.PROPERTY_NAME: "SpekeKeyProvider"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html#cfn-mediapackage-originendpoint-hlsencryption-spekekeyprovider"""
    p_ConstantInitializationVector: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ConstantInitializationVector"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html#cfn-mediapackage-originendpoint-hlsencryption-constantinitializationvector"""
    p_EncryptionMethod: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "EncryptionMethod"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html#cfn-mediapackage-originendpoint-hlsencryption-encryptionmethod"""
    p_KeyRotationIntervalSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "KeyRotationIntervalSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html#cfn-mediapackage-originendpoint-hlsencryption-keyrotationintervalseconds"""
    p_RepeatExtXKey: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "RepeatExtXKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html#cfn-mediapackage-originendpoint-hlsencryption-repeatextxkey"""

@attr.s
class PropOriginEndpointHlsPackage(Property):
    """
    AWS Object Type = "AWS::MediaPackage::OriginEndpoint.HlsPackage"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html

    Property Document:
    
    - ``p_AdMarkers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-admarkers
    - ``p_AdTriggers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-adtriggers
    - ``p_AdsOnDeliveryRestrictions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-adsondeliveryrestrictions
    - ``p_Encryption``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-encryption
    - ``p_IncludeIframeOnlyStream``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-includeiframeonlystream
    - ``p_PlaylistType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-playlisttype
    - ``p_PlaylistWindowSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-playlistwindowseconds
    - ``p_ProgramDateTimeIntervalSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-programdatetimeintervalseconds
    - ``p_SegmentDurationSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-segmentdurationseconds
    - ``p_StreamSelection``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-streamselection
    - ``p_UseAudioRenditionGroup``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-useaudiorenditiongroup
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::OriginEndpoint.HlsPackage"
    
    p_AdMarkers: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AdMarkers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-admarkers"""
    p_AdTriggers: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AdTriggers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-adtriggers"""
    p_AdsOnDeliveryRestrictions: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AdsOnDeliveryRestrictions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-adsondeliveryrestrictions"""
    p_Encryption: typing.Union['PropOriginEndpointHlsEncryption', dict] = attr.ib(
        default=None,
        converter=PropOriginEndpointHlsEncryption.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropOriginEndpointHlsEncryption)),
        metadata={AttrMeta.PROPERTY_NAME: "Encryption"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-encryption"""
    p_IncludeIframeOnlyStream: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IncludeIframeOnlyStream"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-includeiframeonlystream"""
    p_PlaylistType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PlaylistType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-playlisttype"""
    p_PlaylistWindowSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "PlaylistWindowSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-playlistwindowseconds"""
    p_ProgramDateTimeIntervalSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ProgramDateTimeIntervalSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-programdatetimeintervalseconds"""
    p_SegmentDurationSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "SegmentDurationSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-segmentdurationseconds"""
    p_StreamSelection: typing.Union['PropOriginEndpointStreamSelection', dict] = attr.ib(
        default=None,
        converter=PropOriginEndpointStreamSelection.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropOriginEndpointStreamSelection)),
        metadata={AttrMeta.PROPERTY_NAME: "StreamSelection"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-streamselection"""
    p_UseAudioRenditionGroup: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "UseAudioRenditionGroup"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-useaudiorenditiongroup"""

@attr.s
class PropPackagingConfigurationHlsManifest(Property):
    """
    AWS Object Type = "AWS::MediaPackage::PackagingConfiguration.HlsManifest"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html

    Property Document:
    
    - ``p_AdMarkers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html#cfn-mediapackage-packagingconfiguration-hlsmanifest-admarkers
    - ``p_IncludeIframeOnlyStream``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html#cfn-mediapackage-packagingconfiguration-hlsmanifest-includeiframeonlystream
    - ``p_ManifestName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html#cfn-mediapackage-packagingconfiguration-hlsmanifest-manifestname
    - ``p_ProgramDateTimeIntervalSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html#cfn-mediapackage-packagingconfiguration-hlsmanifest-programdatetimeintervalseconds
    - ``p_RepeatExtXKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html#cfn-mediapackage-packagingconfiguration-hlsmanifest-repeatextxkey
    - ``p_StreamSelection``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html#cfn-mediapackage-packagingconfiguration-hlsmanifest-streamselection
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::PackagingConfiguration.HlsManifest"
    
    p_AdMarkers: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AdMarkers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html#cfn-mediapackage-packagingconfiguration-hlsmanifest-admarkers"""
    p_IncludeIframeOnlyStream: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IncludeIframeOnlyStream"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html#cfn-mediapackage-packagingconfiguration-hlsmanifest-includeiframeonlystream"""
    p_ManifestName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ManifestName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html#cfn-mediapackage-packagingconfiguration-hlsmanifest-manifestname"""
    p_ProgramDateTimeIntervalSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ProgramDateTimeIntervalSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html#cfn-mediapackage-packagingconfiguration-hlsmanifest-programdatetimeintervalseconds"""
    p_RepeatExtXKey: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "RepeatExtXKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html#cfn-mediapackage-packagingconfiguration-hlsmanifest-repeatextxkey"""
    p_StreamSelection: typing.Union['PropPackagingConfigurationStreamSelection', dict] = attr.ib(
        default=None,
        converter=PropPackagingConfigurationStreamSelection.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropPackagingConfigurationStreamSelection)),
        metadata={AttrMeta.PROPERTY_NAME: "StreamSelection"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html#cfn-mediapackage-packagingconfiguration-hlsmanifest-streamselection"""

@attr.s
class PropOriginEndpointCmafPackage(Property):
    """
    AWS Object Type = "AWS::MediaPackage::OriginEndpoint.CmafPackage"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafpackage.html

    Property Document:
    
    - ``p_Encryption``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafpackage.html#cfn-mediapackage-originendpoint-cmafpackage-encryption
    - ``p_HlsManifests``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafpackage.html#cfn-mediapackage-originendpoint-cmafpackage-hlsmanifests
    - ``p_SegmentDurationSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafpackage.html#cfn-mediapackage-originendpoint-cmafpackage-segmentdurationseconds
    - ``p_SegmentPrefix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafpackage.html#cfn-mediapackage-originendpoint-cmafpackage-segmentprefix
    - ``p_StreamSelection``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafpackage.html#cfn-mediapackage-originendpoint-cmafpackage-streamselection
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::OriginEndpoint.CmafPackage"
    
    p_Encryption: typing.Union['PropOriginEndpointCmafEncryption', dict] = attr.ib(
        default=None,
        converter=PropOriginEndpointCmafEncryption.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropOriginEndpointCmafEncryption)),
        metadata={AttrMeta.PROPERTY_NAME: "Encryption"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafpackage.html#cfn-mediapackage-originendpoint-cmafpackage-encryption"""
    p_HlsManifests: typing.List[typing.Union['PropOriginEndpointHlsManifest', dict]] = attr.ib(
        default=None,
        converter=PropOriginEndpointHlsManifest.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropOriginEndpointHlsManifest), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "HlsManifests"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafpackage.html#cfn-mediapackage-originendpoint-cmafpackage-hlsmanifests"""
    p_SegmentDurationSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "SegmentDurationSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafpackage.html#cfn-mediapackage-originendpoint-cmafpackage-segmentdurationseconds"""
    p_SegmentPrefix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SegmentPrefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafpackage.html#cfn-mediapackage-originendpoint-cmafpackage-segmentprefix"""
    p_StreamSelection: typing.Union['PropOriginEndpointStreamSelection', dict] = attr.ib(
        default=None,
        converter=PropOriginEndpointStreamSelection.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropOriginEndpointStreamSelection)),
        metadata={AttrMeta.PROPERTY_NAME: "StreamSelection"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafpackage.html#cfn-mediapackage-originendpoint-cmafpackage-streamselection"""

@attr.s
class PropPackagingConfigurationDashEncryption(Property):
    """
    AWS Object Type = "AWS::MediaPackage::PackagingConfiguration.DashEncryption"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashencryption.html

    Property Document:
    
    - ``rp_SpekeKeyProvider``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashencryption.html#cfn-mediapackage-packagingconfiguration-dashencryption-spekekeyprovider
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::PackagingConfiguration.DashEncryption"
    
    rp_SpekeKeyProvider: typing.Union['PropPackagingConfigurationSpekeKeyProvider', dict] = attr.ib(
        default=None,
        converter=PropPackagingConfigurationSpekeKeyProvider.from_dict,
        validator=attr.validators.instance_of(PropPackagingConfigurationSpekeKeyProvider),
        metadata={AttrMeta.PROPERTY_NAME: "SpekeKeyProvider"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashencryption.html#cfn-mediapackage-packagingconfiguration-dashencryption-spekekeyprovider"""

@attr.s
class PropOriginEndpointMssEncryption(Property):
    """
    AWS Object Type = "AWS::MediaPackage::OriginEndpoint.MssEncryption"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-mssencryption.html

    Property Document:
    
    - ``rp_SpekeKeyProvider``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-mssencryption.html#cfn-mediapackage-originendpoint-mssencryption-spekekeyprovider
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::OriginEndpoint.MssEncryption"
    
    rp_SpekeKeyProvider: typing.Union['PropOriginEndpointSpekeKeyProvider', dict] = attr.ib(
        default=None,
        converter=PropOriginEndpointSpekeKeyProvider.from_dict,
        validator=attr.validators.instance_of(PropOriginEndpointSpekeKeyProvider),
        metadata={AttrMeta.PROPERTY_NAME: "SpekeKeyProvider"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-mssencryption.html#cfn-mediapackage-originendpoint-mssencryption-spekekeyprovider"""

@attr.s
class PropPackagingConfigurationCmafPackage(Property):
    """
    AWS Object Type = "AWS::MediaPackage::PackagingConfiguration.CmafPackage"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafpackage.html

    Property Document:
    
    - ``rp_HlsManifests``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafpackage.html#cfn-mediapackage-packagingconfiguration-cmafpackage-hlsmanifests
    - ``p_Encryption``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafpackage.html#cfn-mediapackage-packagingconfiguration-cmafpackage-encryption
    - ``p_IncludeEncoderConfigurationInSegments``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafpackage.html#cfn-mediapackage-packagingconfiguration-cmafpackage-includeencoderconfigurationinsegments
    - ``p_SegmentDurationSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafpackage.html#cfn-mediapackage-packagingconfiguration-cmafpackage-segmentdurationseconds
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::PackagingConfiguration.CmafPackage"
    
    rp_HlsManifests: typing.List[typing.Union['PropPackagingConfigurationHlsManifest', dict]] = attr.ib(
        default=None,
        converter=PropPackagingConfigurationHlsManifest.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropPackagingConfigurationHlsManifest), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "HlsManifests"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafpackage.html#cfn-mediapackage-packagingconfiguration-cmafpackage-hlsmanifests"""
    p_Encryption: typing.Union['PropPackagingConfigurationCmafEncryption', dict] = attr.ib(
        default=None,
        converter=PropPackagingConfigurationCmafEncryption.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropPackagingConfigurationCmafEncryption)),
        metadata={AttrMeta.PROPERTY_NAME: "Encryption"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafpackage.html#cfn-mediapackage-packagingconfiguration-cmafpackage-encryption"""
    p_IncludeEncoderConfigurationInSegments: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IncludeEncoderConfigurationInSegments"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafpackage.html#cfn-mediapackage-packagingconfiguration-cmafpackage-includeencoderconfigurationinsegments"""
    p_SegmentDurationSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "SegmentDurationSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafpackage.html#cfn-mediapackage-packagingconfiguration-cmafpackage-segmentdurationseconds"""

@attr.s
class PropPackagingConfigurationDashManifest(Property):
    """
    AWS Object Type = "AWS::MediaPackage::PackagingConfiguration.DashManifest"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html

    Property Document:
    
    - ``p_ManifestLayout``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html#cfn-mediapackage-packagingconfiguration-dashmanifest-manifestlayout
    - ``p_ManifestName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html#cfn-mediapackage-packagingconfiguration-dashmanifest-manifestname
    - ``p_MinBufferTimeSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html#cfn-mediapackage-packagingconfiguration-dashmanifest-minbuffertimeseconds
    - ``p_Profile``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html#cfn-mediapackage-packagingconfiguration-dashmanifest-profile
    - ``p_StreamSelection``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html#cfn-mediapackage-packagingconfiguration-dashmanifest-streamselection
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::PackagingConfiguration.DashManifest"
    
    p_ManifestLayout: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ManifestLayout"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html#cfn-mediapackage-packagingconfiguration-dashmanifest-manifestlayout"""
    p_ManifestName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ManifestName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html#cfn-mediapackage-packagingconfiguration-dashmanifest-manifestname"""
    p_MinBufferTimeSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MinBufferTimeSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html#cfn-mediapackage-packagingconfiguration-dashmanifest-minbuffertimeseconds"""
    p_Profile: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Profile"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html#cfn-mediapackage-packagingconfiguration-dashmanifest-profile"""
    p_StreamSelection: typing.Union['PropPackagingConfigurationStreamSelection', dict] = attr.ib(
        default=None,
        converter=PropPackagingConfigurationStreamSelection.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropPackagingConfigurationStreamSelection)),
        metadata={AttrMeta.PROPERTY_NAME: "StreamSelection"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html#cfn-mediapackage-packagingconfiguration-dashmanifest-streamselection"""

@attr.s
class PropOriginEndpointDashEncryption(Property):
    """
    AWS Object Type = "AWS::MediaPackage::OriginEndpoint.DashEncryption"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashencryption.html

    Property Document:
    
    - ``rp_SpekeKeyProvider``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashencryption.html#cfn-mediapackage-originendpoint-dashencryption-spekekeyprovider
    - ``p_KeyRotationIntervalSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashencryption.html#cfn-mediapackage-originendpoint-dashencryption-keyrotationintervalseconds
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::OriginEndpoint.DashEncryption"
    
    rp_SpekeKeyProvider: typing.Union['PropOriginEndpointSpekeKeyProvider', dict] = attr.ib(
        default=None,
        converter=PropOriginEndpointSpekeKeyProvider.from_dict,
        validator=attr.validators.instance_of(PropOriginEndpointSpekeKeyProvider),
        metadata={AttrMeta.PROPERTY_NAME: "SpekeKeyProvider"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashencryption.html#cfn-mediapackage-originendpoint-dashencryption-spekekeyprovider"""
    p_KeyRotationIntervalSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "KeyRotationIntervalSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashencryption.html#cfn-mediapackage-originendpoint-dashencryption-keyrotationintervalseconds"""

@attr.s
class PropPackagingConfigurationMssManifest(Property):
    """
    AWS Object Type = "AWS::MediaPackage::PackagingConfiguration.MssManifest"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-mssmanifest.html

    Property Document:
    
    - ``p_ManifestName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-mssmanifest.html#cfn-mediapackage-packagingconfiguration-mssmanifest-manifestname
    - ``p_StreamSelection``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-mssmanifest.html#cfn-mediapackage-packagingconfiguration-mssmanifest-streamselection
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::PackagingConfiguration.MssManifest"
    
    p_ManifestName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ManifestName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-mssmanifest.html#cfn-mediapackage-packagingconfiguration-mssmanifest-manifestname"""
    p_StreamSelection: typing.Union['PropPackagingConfigurationStreamSelection', dict] = attr.ib(
        default=None,
        converter=PropPackagingConfigurationStreamSelection.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropPackagingConfigurationStreamSelection)),
        metadata={AttrMeta.PROPERTY_NAME: "StreamSelection"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-mssmanifest.html#cfn-mediapackage-packagingconfiguration-mssmanifest-streamselection"""

@attr.s
class PropPackagingConfigurationMssPackage(Property):
    """
    AWS Object Type = "AWS::MediaPackage::PackagingConfiguration.MssPackage"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-msspackage.html

    Property Document:
    
    - ``rp_MssManifests``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-msspackage.html#cfn-mediapackage-packagingconfiguration-msspackage-mssmanifests
    - ``p_Encryption``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-msspackage.html#cfn-mediapackage-packagingconfiguration-msspackage-encryption
    - ``p_SegmentDurationSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-msspackage.html#cfn-mediapackage-packagingconfiguration-msspackage-segmentdurationseconds
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::PackagingConfiguration.MssPackage"
    
    rp_MssManifests: typing.List[typing.Union['PropPackagingConfigurationMssManifest', dict]] = attr.ib(
        default=None,
        converter=PropPackagingConfigurationMssManifest.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropPackagingConfigurationMssManifest), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "MssManifests"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-msspackage.html#cfn-mediapackage-packagingconfiguration-msspackage-mssmanifests"""
    p_Encryption: typing.Union['PropPackagingConfigurationMssEncryption', dict] = attr.ib(
        default=None,
        converter=PropPackagingConfigurationMssEncryption.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropPackagingConfigurationMssEncryption)),
        metadata={AttrMeta.PROPERTY_NAME: "Encryption"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-msspackage.html#cfn-mediapackage-packagingconfiguration-msspackage-encryption"""
    p_SegmentDurationSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "SegmentDurationSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-msspackage.html#cfn-mediapackage-packagingconfiguration-msspackage-segmentdurationseconds"""

@attr.s
class PropOriginEndpointMssPackage(Property):
    """
    AWS Object Type = "AWS::MediaPackage::OriginEndpoint.MssPackage"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-msspackage.html

    Property Document:
    
    - ``p_Encryption``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-msspackage.html#cfn-mediapackage-originendpoint-msspackage-encryption
    - ``p_ManifestWindowSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-msspackage.html#cfn-mediapackage-originendpoint-msspackage-manifestwindowseconds
    - ``p_SegmentDurationSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-msspackage.html#cfn-mediapackage-originendpoint-msspackage-segmentdurationseconds
    - ``p_StreamSelection``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-msspackage.html#cfn-mediapackage-originendpoint-msspackage-streamselection
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::OriginEndpoint.MssPackage"
    
    p_Encryption: typing.Union['PropOriginEndpointMssEncryption', dict] = attr.ib(
        default=None,
        converter=PropOriginEndpointMssEncryption.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropOriginEndpointMssEncryption)),
        metadata={AttrMeta.PROPERTY_NAME: "Encryption"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-msspackage.html#cfn-mediapackage-originendpoint-msspackage-encryption"""
    p_ManifestWindowSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ManifestWindowSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-msspackage.html#cfn-mediapackage-originendpoint-msspackage-manifestwindowseconds"""
    p_SegmentDurationSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "SegmentDurationSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-msspackage.html#cfn-mediapackage-originendpoint-msspackage-segmentdurationseconds"""
    p_StreamSelection: typing.Union['PropOriginEndpointStreamSelection', dict] = attr.ib(
        default=None,
        converter=PropOriginEndpointStreamSelection.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropOriginEndpointStreamSelection)),
        metadata={AttrMeta.PROPERTY_NAME: "StreamSelection"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-msspackage.html#cfn-mediapackage-originendpoint-msspackage-streamselection"""

@attr.s
class PropPackagingConfigurationHlsPackage(Property):
    """
    AWS Object Type = "AWS::MediaPackage::PackagingConfiguration.HlsPackage"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html

    Property Document:
    
    - ``rp_HlsManifests``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html#cfn-mediapackage-packagingconfiguration-hlspackage-hlsmanifests
    - ``p_Encryption``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html#cfn-mediapackage-packagingconfiguration-hlspackage-encryption
    - ``p_SegmentDurationSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html#cfn-mediapackage-packagingconfiguration-hlspackage-segmentdurationseconds
    - ``p_UseAudioRenditionGroup``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html#cfn-mediapackage-packagingconfiguration-hlspackage-useaudiorenditiongroup
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::PackagingConfiguration.HlsPackage"
    
    rp_HlsManifests: typing.List[typing.Union['PropPackagingConfigurationHlsManifest', dict]] = attr.ib(
        default=None,
        converter=PropPackagingConfigurationHlsManifest.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropPackagingConfigurationHlsManifest), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "HlsManifests"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html#cfn-mediapackage-packagingconfiguration-hlspackage-hlsmanifests"""
    p_Encryption: typing.Union['PropPackagingConfigurationHlsEncryption', dict] = attr.ib(
        default=None,
        converter=PropPackagingConfigurationHlsEncryption.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropPackagingConfigurationHlsEncryption)),
        metadata={AttrMeta.PROPERTY_NAME: "Encryption"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html#cfn-mediapackage-packagingconfiguration-hlspackage-encryption"""
    p_SegmentDurationSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "SegmentDurationSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html#cfn-mediapackage-packagingconfiguration-hlspackage-segmentdurationseconds"""
    p_UseAudioRenditionGroup: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "UseAudioRenditionGroup"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html#cfn-mediapackage-packagingconfiguration-hlspackage-useaudiorenditiongroup"""

@attr.s
class PropPackagingConfigurationDashPackage(Property):
    """
    AWS Object Type = "AWS::MediaPackage::PackagingConfiguration.DashPackage"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html

    Property Document:
    
    - ``rp_DashManifests``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-dashmanifests
    - ``p_Encryption``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-encryption
    - ``p_IncludeEncoderConfigurationInSegments``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-includeencoderconfigurationinsegments
    - ``p_PeriodTriggers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-periodtriggers
    - ``p_SegmentDurationSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-segmentdurationseconds
    - ``p_SegmentTemplateFormat``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-segmenttemplateformat
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::PackagingConfiguration.DashPackage"
    
    rp_DashManifests: typing.List[typing.Union['PropPackagingConfigurationDashManifest', dict]] = attr.ib(
        default=None,
        converter=PropPackagingConfigurationDashManifest.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropPackagingConfigurationDashManifest), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "DashManifests"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-dashmanifests"""
    p_Encryption: typing.Union['PropPackagingConfigurationDashEncryption', dict] = attr.ib(
        default=None,
        converter=PropPackagingConfigurationDashEncryption.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropPackagingConfigurationDashEncryption)),
        metadata={AttrMeta.PROPERTY_NAME: "Encryption"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-encryption"""
    p_IncludeEncoderConfigurationInSegments: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IncludeEncoderConfigurationInSegments"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-includeencoderconfigurationinsegments"""
    p_PeriodTriggers: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "PeriodTriggers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-periodtriggers"""
    p_SegmentDurationSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "SegmentDurationSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-segmentdurationseconds"""
    p_SegmentTemplateFormat: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SegmentTemplateFormat"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-segmenttemplateformat"""

@attr.s
class PropOriginEndpointDashPackage(Property):
    """
    AWS Object Type = "AWS::MediaPackage::OriginEndpoint.DashPackage"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html

    Property Document:
    
    - ``p_AdTriggers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-adtriggers
    - ``p_AdsOnDeliveryRestrictions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-adsondeliveryrestrictions
    - ``p_Encryption``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-encryption
    - ``p_ManifestLayout``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-manifestlayout
    - ``p_ManifestWindowSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-manifestwindowseconds
    - ``p_MinBufferTimeSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-minbuffertimeseconds
    - ``p_MinUpdatePeriodSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-minupdateperiodseconds
    - ``p_PeriodTriggers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-periodtriggers
    - ``p_Profile``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-profile
    - ``p_SegmentDurationSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-segmentdurationseconds
    - ``p_SegmentTemplateFormat``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-segmenttemplateformat
    - ``p_StreamSelection``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-streamselection
    - ``p_SuggestedPresentationDelaySeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-suggestedpresentationdelayseconds
    - ``p_UtcTiming``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-utctiming
    - ``p_UtcTimingUri``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-utctiminguri
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::OriginEndpoint.DashPackage"
    
    p_AdTriggers: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AdTriggers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-adtriggers"""
    p_AdsOnDeliveryRestrictions: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AdsOnDeliveryRestrictions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-adsondeliveryrestrictions"""
    p_Encryption: typing.Union['PropOriginEndpointDashEncryption', dict] = attr.ib(
        default=None,
        converter=PropOriginEndpointDashEncryption.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropOriginEndpointDashEncryption)),
        metadata={AttrMeta.PROPERTY_NAME: "Encryption"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-encryption"""
    p_ManifestLayout: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ManifestLayout"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-manifestlayout"""
    p_ManifestWindowSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ManifestWindowSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-manifestwindowseconds"""
    p_MinBufferTimeSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MinBufferTimeSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-minbuffertimeseconds"""
    p_MinUpdatePeriodSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MinUpdatePeriodSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-minupdateperiodseconds"""
    p_PeriodTriggers: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "PeriodTriggers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-periodtriggers"""
    p_Profile: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Profile"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-profile"""
    p_SegmentDurationSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "SegmentDurationSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-segmentdurationseconds"""
    p_SegmentTemplateFormat: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SegmentTemplateFormat"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-segmenttemplateformat"""
    p_StreamSelection: typing.Union['PropOriginEndpointStreamSelection', dict] = attr.ib(
        default=None,
        converter=PropOriginEndpointStreamSelection.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropOriginEndpointStreamSelection)),
        metadata={AttrMeta.PROPERTY_NAME: "StreamSelection"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-streamselection"""
    p_SuggestedPresentationDelaySeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "SuggestedPresentationDelaySeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-suggestedpresentationdelayseconds"""
    p_UtcTiming: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "UtcTiming"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-utctiming"""
    p_UtcTimingUri: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "UtcTimingUri"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-utctiminguri"""


#--- Resource declaration ---

@attr.s
class Channel(Resource):
    """
    AWS Object Type = "AWS::MediaPackage::Channel"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html

    Property Document:
    
    - ``rp_Id``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-id
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-description
    - ``p_EgressAccessLogs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-egressaccesslogs
    - ``p_IngressAccessLogs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-ingressaccesslogs
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-tags
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::Channel"

    
    rp_Id: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Id"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-id"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-description"""
    p_EgressAccessLogs: typing.Union['PropChannelLogConfiguration', dict] = attr.ib(
        default=None,
        converter=PropChannelLogConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropChannelLogConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "EgressAccessLogs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-egressaccesslogs"""
    p_IngressAccessLogs: typing.Union['PropChannelLogConfiguration', dict] = attr.ib(
        default=None,
        converter=PropChannelLogConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropChannelLogConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "IngressAccessLogs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-ingressaccesslogs"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#aws-resource-mediapackage-channel-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class PackagingConfiguration(Resource):
    """
    AWS Object Type = "AWS::MediaPackage::PackagingConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html

    Property Document:
    
    - ``rp_Id``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-id
    - ``rp_PackagingGroupId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-packaginggroupid
    - ``p_CmafPackage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-cmafpackage
    - ``p_DashPackage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-dashpackage
    - ``p_HlsPackage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-hlspackage
    - ``p_MssPackage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-msspackage
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-tags
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::PackagingConfiguration"

    
    rp_Id: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Id"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-id"""
    rp_PackagingGroupId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PackagingGroupId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-packaginggroupid"""
    p_CmafPackage: typing.Union['PropPackagingConfigurationCmafPackage', dict] = attr.ib(
        default=None,
        converter=PropPackagingConfigurationCmafPackage.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropPackagingConfigurationCmafPackage)),
        metadata={AttrMeta.PROPERTY_NAME: "CmafPackage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-cmafpackage"""
    p_DashPackage: typing.Union['PropPackagingConfigurationDashPackage', dict] = attr.ib(
        default=None,
        converter=PropPackagingConfigurationDashPackage.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropPackagingConfigurationDashPackage)),
        metadata={AttrMeta.PROPERTY_NAME: "DashPackage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-dashpackage"""
    p_HlsPackage: typing.Union['PropPackagingConfigurationHlsPackage', dict] = attr.ib(
        default=None,
        converter=PropPackagingConfigurationHlsPackage.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropPackagingConfigurationHlsPackage)),
        metadata={AttrMeta.PROPERTY_NAME: "HlsPackage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-hlspackage"""
    p_MssPackage: typing.Union['PropPackagingConfigurationMssPackage', dict] = attr.ib(
        default=None,
        converter=PropPackagingConfigurationMssPackage.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropPackagingConfigurationMssPackage)),
        metadata={AttrMeta.PROPERTY_NAME: "MssPackage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-msspackage"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#aws-resource-mediapackage-packagingconfiguration-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class Asset(Resource):
    """
    AWS Object Type = "AWS::MediaPackage::Asset"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html

    Property Document:
    
    - ``rp_Id``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-id
    - ``rp_PackagingGroupId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-packaginggroupid
    - ``rp_SourceArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-sourcearn
    - ``rp_SourceRoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-sourcerolearn
    - ``p_ResourceId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-resourceid
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-tags
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::Asset"

    
    rp_Id: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Id"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-id"""
    rp_PackagingGroupId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PackagingGroupId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-packaginggroupid"""
    rp_SourceArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SourceArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-sourcearn"""
    rp_SourceRoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SourceRoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-sourcerolearn"""
    p_ResourceId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-resourceid"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#aws-resource-mediapackage-asset-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_CreatedAt(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#aws-resource-mediapackage-asset-return-values"""
        return GetAtt(resource=self, attr_name="CreatedAt")
    
    @property
    def rv_EgressEndpoints(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#aws-resource-mediapackage-asset-return-values"""
        return GetAtt(resource=self, attr_name="EgressEndpoints")
    

@attr.s
class PackagingGroup(Resource):
    """
    AWS Object Type = "AWS::MediaPackage::PackagingGroup"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html

    Property Document:
    
    - ``rp_Id``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html#cfn-mediapackage-packaginggroup-id
    - ``p_Authorization``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html#cfn-mediapackage-packaginggroup-authorization
    - ``p_EgressAccessLogs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html#cfn-mediapackage-packaginggroup-egressaccesslogs
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html#cfn-mediapackage-packaginggroup-tags
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::PackagingGroup"

    
    rp_Id: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Id"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html#cfn-mediapackage-packaginggroup-id"""
    p_Authorization: typing.Union['PropPackagingGroupAuthorization', dict] = attr.ib(
        default=None,
        converter=PropPackagingGroupAuthorization.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropPackagingGroupAuthorization)),
        metadata={AttrMeta.PROPERTY_NAME: "Authorization"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html#cfn-mediapackage-packaginggroup-authorization"""
    p_EgressAccessLogs: typing.Union['PropPackagingGroupLogConfiguration', dict] = attr.ib(
        default=None,
        converter=PropPackagingGroupLogConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropPackagingGroupLogConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "EgressAccessLogs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html#cfn-mediapackage-packaginggroup-egressaccesslogs"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html#cfn-mediapackage-packaginggroup-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html#aws-resource-mediapackage-packaginggroup-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_DomainName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html#aws-resource-mediapackage-packaginggroup-return-values"""
        return GetAtt(resource=self, attr_name="DomainName")
    

@attr.s
class OriginEndpoint(Resource):
    """
    AWS Object Type = "AWS::MediaPackage::OriginEndpoint"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html

    Property Document:
    
    - ``rp_ChannelId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-channelid
    - ``rp_Id``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-id
    - ``p_Authorization``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-authorization
    - ``p_CmafPackage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-cmafpackage
    - ``p_DashPackage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-dashpackage
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-description
    - ``p_HlsPackage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-hlspackage
    - ``p_ManifestName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-manifestname
    - ``p_MssPackage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-msspackage
    - ``p_Origination``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-origination
    - ``p_StartoverWindowSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-startoverwindowseconds
    - ``p_TimeDelaySeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-timedelayseconds
    - ``p_Whitelist``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-whitelist
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-tags
    """
    AWS_OBJECT_TYPE = "AWS::MediaPackage::OriginEndpoint"

    
    rp_ChannelId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ChannelId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-channelid"""
    rp_Id: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Id"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-id"""
    p_Authorization: typing.Union['PropOriginEndpointAuthorization', dict] = attr.ib(
        default=None,
        converter=PropOriginEndpointAuthorization.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropOriginEndpointAuthorization)),
        metadata={AttrMeta.PROPERTY_NAME: "Authorization"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-authorization"""
    p_CmafPackage: typing.Union['PropOriginEndpointCmafPackage', dict] = attr.ib(
        default=None,
        converter=PropOriginEndpointCmafPackage.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropOriginEndpointCmafPackage)),
        metadata={AttrMeta.PROPERTY_NAME: "CmafPackage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-cmafpackage"""
    p_DashPackage: typing.Union['PropOriginEndpointDashPackage', dict] = attr.ib(
        default=None,
        converter=PropOriginEndpointDashPackage.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropOriginEndpointDashPackage)),
        metadata={AttrMeta.PROPERTY_NAME: "DashPackage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-dashpackage"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-description"""
    p_HlsPackage: typing.Union['PropOriginEndpointHlsPackage', dict] = attr.ib(
        default=None,
        converter=PropOriginEndpointHlsPackage.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropOriginEndpointHlsPackage)),
        metadata={AttrMeta.PROPERTY_NAME: "HlsPackage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-hlspackage"""
    p_ManifestName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ManifestName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-manifestname"""
    p_MssPackage: typing.Union['PropOriginEndpointMssPackage', dict] = attr.ib(
        default=None,
        converter=PropOriginEndpointMssPackage.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropOriginEndpointMssPackage)),
        metadata={AttrMeta.PROPERTY_NAME: "MssPackage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-msspackage"""
    p_Origination: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Origination"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-origination"""
    p_StartoverWindowSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "StartoverWindowSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-startoverwindowseconds"""
    p_TimeDelaySeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "TimeDelaySeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-timedelayseconds"""
    p_Whitelist: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Whitelist"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-whitelist"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#aws-resource-mediapackage-originendpoint-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_Url(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#aws-resource-mediapackage-originendpoint-return-values"""
        return GetAtt(resource=self, attr_name="Url")
    
