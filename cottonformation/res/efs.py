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
class PropAccessPointAccessPointTag(Property):
    """
    AWS Object Type = "AWS::EFS::AccessPoint.AccessPointTag"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-accesspointtag.html

    Property Document:
    
    - ``p_Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-accesspointtag.html#cfn-efs-accesspoint-accesspointtag-key
    - ``p_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-accesspointtag.html#cfn-efs-accesspoint-accesspointtag-value
    """
    AWS_OBJECT_TYPE = "AWS::EFS::AccessPoint.AccessPointTag"
    
    p_Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-accesspointtag.html#cfn-efs-accesspoint-accesspointtag-key"""
    p_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-accesspointtag.html#cfn-efs-accesspoint-accesspointtag-value"""

@attr.s
class PropFileSystemElasticFileSystemTag(Property):
    """
    AWS Object Type = "AWS::EFS::FileSystem.ElasticFileSystemTag"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-elasticfilesystemtag.html

    Property Document:
    
    - ``rp_Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-elasticfilesystemtag.html#cfn-efs-filesystem-elasticfilesystemtag-key
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-elasticfilesystemtag.html#cfn-efs-filesystem-elasticfilesystemtag-value
    """
    AWS_OBJECT_TYPE = "AWS::EFS::FileSystem.ElasticFileSystemTag"
    
    rp_Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-elasticfilesystemtag.html#cfn-efs-filesystem-elasticfilesystemtag-key"""
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-elasticfilesystemtag.html#cfn-efs-filesystem-elasticfilesystemtag-value"""

@attr.s
class PropFileSystemLifecyclePolicy(Property):
    """
    AWS Object Type = "AWS::EFS::FileSystem.LifecyclePolicy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-lifecyclepolicy.html

    Property Document:
    
    - ``p_TransitionToIA``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-lifecyclepolicy.html#cfn-efs-filesystem-lifecyclepolicy-transitiontoia
    - ``p_TransitionToPrimaryStorageClass``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-lifecyclepolicy.html#cfn-efs-filesystem-lifecyclepolicy-transitiontoprimarystorageclass
    """
    AWS_OBJECT_TYPE = "AWS::EFS::FileSystem.LifecyclePolicy"
    
    p_TransitionToIA: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TransitionToIA"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-lifecyclepolicy.html#cfn-efs-filesystem-lifecyclepolicy-transitiontoia"""
    p_TransitionToPrimaryStorageClass: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TransitionToPrimaryStorageClass"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-lifecyclepolicy.html#cfn-efs-filesystem-lifecyclepolicy-transitiontoprimarystorageclass"""

@attr.s
class PropFileSystemBackupPolicy(Property):
    """
    AWS Object Type = "AWS::EFS::FileSystem.BackupPolicy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-backuppolicy.html

    Property Document:
    
    - ``rp_Status``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-backuppolicy.html#cfn-efs-filesystem-backuppolicy-status
    """
    AWS_OBJECT_TYPE = "AWS::EFS::FileSystem.BackupPolicy"
    
    rp_Status: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Status"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-backuppolicy.html#cfn-efs-filesystem-backuppolicy-status"""

@attr.s
class PropAccessPointCreationInfo(Property):
    """
    AWS Object Type = "AWS::EFS::AccessPoint.CreationInfo"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-creationinfo.html

    Property Document:
    
    - ``rp_OwnerGid``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-creationinfo.html#cfn-efs-accesspoint-creationinfo-ownergid
    - ``rp_OwnerUid``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-creationinfo.html#cfn-efs-accesspoint-creationinfo-owneruid
    - ``rp_Permissions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-creationinfo.html#cfn-efs-accesspoint-creationinfo-permissions
    """
    AWS_OBJECT_TYPE = "AWS::EFS::AccessPoint.CreationInfo"
    
    rp_OwnerGid: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "OwnerGid"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-creationinfo.html#cfn-efs-accesspoint-creationinfo-ownergid"""
    rp_OwnerUid: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "OwnerUid"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-creationinfo.html#cfn-efs-accesspoint-creationinfo-owneruid"""
    rp_Permissions: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Permissions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-creationinfo.html#cfn-efs-accesspoint-creationinfo-permissions"""

@attr.s
class PropAccessPointPosixUser(Property):
    """
    AWS Object Type = "AWS::EFS::AccessPoint.PosixUser"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-posixuser.html

    Property Document:
    
    - ``rp_Gid``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-posixuser.html#cfn-efs-accesspoint-posixuser-gid
    - ``rp_Uid``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-posixuser.html#cfn-efs-accesspoint-posixuser-uid
    - ``p_SecondaryGids``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-posixuser.html#cfn-efs-accesspoint-posixuser-secondarygids
    """
    AWS_OBJECT_TYPE = "AWS::EFS::AccessPoint.PosixUser"
    
    rp_Gid: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Gid"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-posixuser.html#cfn-efs-accesspoint-posixuser-gid"""
    rp_Uid: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Uid"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-posixuser.html#cfn-efs-accesspoint-posixuser-uid"""
    p_SecondaryGids: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SecondaryGids"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-posixuser.html#cfn-efs-accesspoint-posixuser-secondarygids"""

@attr.s
class PropAccessPointRootDirectory(Property):
    """
    AWS Object Type = "AWS::EFS::AccessPoint.RootDirectory"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-rootdirectory.html

    Property Document:
    
    - ``p_CreationInfo``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-rootdirectory.html#cfn-efs-accesspoint-rootdirectory-creationinfo
    - ``p_Path``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-rootdirectory.html#cfn-efs-accesspoint-rootdirectory-path
    """
    AWS_OBJECT_TYPE = "AWS::EFS::AccessPoint.RootDirectory"
    
    p_CreationInfo: typing.Union['PropAccessPointCreationInfo', dict] = attr.ib(
        default=None,
        converter=PropAccessPointCreationInfo.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropAccessPointCreationInfo)),
        metadata={AttrMeta.PROPERTY_NAME: "CreationInfo"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-rootdirectory.html#cfn-efs-accesspoint-rootdirectory-creationinfo"""
    p_Path: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Path"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-rootdirectory.html#cfn-efs-accesspoint-rootdirectory-path"""


#--- Resource declaration ---

@attr.s
class MountTarget(Resource):
    """
    AWS Object Type = "AWS::EFS::MountTarget"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html

    Property Document:
    
    - ``rp_FileSystemId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html#cfn-efs-mounttarget-filesystemid
    - ``rp_SecurityGroups``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html#cfn-efs-mounttarget-securitygroups
    - ``rp_SubnetId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html#cfn-efs-mounttarget-subnetid
    - ``p_IpAddress``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html#cfn-efs-mounttarget-ipaddress
    """
    AWS_OBJECT_TYPE = "AWS::EFS::MountTarget"

    
    rp_FileSystemId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "FileSystemId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html#cfn-efs-mounttarget-filesystemid"""
    rp_SecurityGroups: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "SecurityGroups"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html#cfn-efs-mounttarget-securitygroups"""
    rp_SubnetId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SubnetId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html#cfn-efs-mounttarget-subnetid"""
    p_IpAddress: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "IpAddress"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html#cfn-efs-mounttarget-ipaddress"""

    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html#aws-resource-efs-mounttarget-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_IpAddress(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html#aws-resource-efs-mounttarget-return-values"""
        return GetAtt(resource=self, attr_name="IpAddress")
    

@attr.s
class FileSystem(Resource):
    """
    AWS Object Type = "AWS::EFS::FileSystem"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html

    Property Document:
    
    - ``p_AvailabilityZoneName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-availabilityzonename
    - ``p_BackupPolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-backuppolicy
    - ``p_BypassPolicyLockoutSafetyCheck``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-bypasspolicylockoutsafetycheck
    - ``p_Encrypted``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-encrypted
    - ``p_FileSystemPolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-filesystempolicy
    - ``p_FileSystemTags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-filesystemtags
    - ``p_KmsKeyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-kmskeyid
    - ``p_LifecyclePolicies``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-lifecyclepolicies
    - ``p_PerformanceMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-performancemode
    - ``p_ProvisionedThroughputInMibps``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-provisionedthroughputinmibps
    - ``p_ThroughputMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-throughputmode
    """
    AWS_OBJECT_TYPE = "AWS::EFS::FileSystem"

    
    p_AvailabilityZoneName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AvailabilityZoneName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-availabilityzonename"""
    p_BackupPolicy: typing.Union['PropFileSystemBackupPolicy', dict] = attr.ib(
        default=None,
        converter=PropFileSystemBackupPolicy.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropFileSystemBackupPolicy)),
        metadata={AttrMeta.PROPERTY_NAME: "BackupPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-backuppolicy"""
    p_BypassPolicyLockoutSafetyCheck: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "BypassPolicyLockoutSafetyCheck"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-bypasspolicylockoutsafetycheck"""
    p_Encrypted: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Encrypted"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-encrypted"""
    p_FileSystemPolicy: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "FileSystemPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-filesystempolicy"""
    p_FileSystemTags: typing.List[typing.Union['PropFileSystemElasticFileSystemTag', dict]] = attr.ib(
        default=None,
        converter=PropFileSystemElasticFileSystemTag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropFileSystemElasticFileSystemTag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "FileSystemTags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-filesystemtags"""
    p_KmsKeyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "KmsKeyId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-kmskeyid"""
    p_LifecyclePolicies: typing.List[typing.Union['PropFileSystemLifecyclePolicy', dict]] = attr.ib(
        default=None,
        converter=PropFileSystemLifecyclePolicy.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropFileSystemLifecyclePolicy), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "LifecyclePolicies"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-lifecyclepolicies"""
    p_PerformanceMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PerformanceMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-performancemode"""
    p_ProvisionedThroughputInMibps: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "ProvisionedThroughputInMibps"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-provisionedthroughputinmibps"""
    p_ThroughputMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ThroughputMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-throughputmode"""

    
    @property
    def rv_FileSystemId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#aws-resource-efs-filesystem-return-values"""
        return GetAtt(resource=self, attr_name="FileSystemId")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#aws-resource-efs-filesystem-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class AccessPoint(Resource):
    """
    AWS Object Type = "AWS::EFS::AccessPoint"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-accesspoint.html

    Property Document:
    
    - ``rp_FileSystemId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-accesspoint.html#cfn-efs-accesspoint-filesystemid
    - ``p_AccessPointTags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-accesspoint.html#cfn-efs-accesspoint-accesspointtags
    - ``p_ClientToken``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-accesspoint.html#cfn-efs-accesspoint-clienttoken
    - ``p_PosixUser``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-accesspoint.html#cfn-efs-accesspoint-posixuser
    - ``p_RootDirectory``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-accesspoint.html#cfn-efs-accesspoint-rootdirectory
    """
    AWS_OBJECT_TYPE = "AWS::EFS::AccessPoint"

    
    rp_FileSystemId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "FileSystemId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-accesspoint.html#cfn-efs-accesspoint-filesystemid"""
    p_AccessPointTags: typing.List[typing.Union['PropAccessPointAccessPointTag', dict]] = attr.ib(
        default=None,
        converter=PropAccessPointAccessPointTag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropAccessPointAccessPointTag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AccessPointTags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-accesspoint.html#cfn-efs-accesspoint-accesspointtags"""
    p_ClientToken: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ClientToken"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-accesspoint.html#cfn-efs-accesspoint-clienttoken"""
    p_PosixUser: typing.Union['PropAccessPointPosixUser', dict] = attr.ib(
        default=None,
        converter=PropAccessPointPosixUser.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropAccessPointPosixUser)),
        metadata={AttrMeta.PROPERTY_NAME: "PosixUser"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-accesspoint.html#cfn-efs-accesspoint-posixuser"""
    p_RootDirectory: typing.Union['PropAccessPointRootDirectory', dict] = attr.ib(
        default=None,
        converter=PropAccessPointRootDirectory.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropAccessPointRootDirectory)),
        metadata={AttrMeta.PROPERTY_NAME: "RootDirectory"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-accesspoint.html#cfn-efs-accesspoint-rootdirectory"""

    
    @property
    def rv_AccessPointId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-accesspoint.html#aws-resource-efs-accesspoint-return-values"""
        return GetAtt(resource=self, attr_name="AccessPointId")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-accesspoint.html#aws-resource-efs-accesspoint-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
