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
class PropWorkspaceWorkspaceProperties(Property):
    """
    AWS Object Type = "AWS::WorkSpaces::Workspace.WorkspaceProperties"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html

    Property Document:
    
    - ``p_ComputeTypeName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html#cfn-workspaces-workspace-workspaceproperties-computetypename
    - ``p_RootVolumeSizeGib``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html#cfn-workspaces-workspace-workspaceproperties-rootvolumesizegib
    - ``p_RunningMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html#cfn-workspaces-workspace-workspaceproperties-runningmode
    - ``p_RunningModeAutoStopTimeoutInMinutes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html#cfn-workspaces-workspace-workspaceproperties-runningmodeautostoptimeoutinminutes
    - ``p_UserVolumeSizeGib``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html#cfn-workspaces-workspace-workspaceproperties-uservolumesizegib
    """
    AWS_OBJECT_TYPE = "AWS::WorkSpaces::Workspace.WorkspaceProperties"
    
    p_ComputeTypeName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ComputeTypeName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html#cfn-workspaces-workspace-workspaceproperties-computetypename"""
    p_RootVolumeSizeGib: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "RootVolumeSizeGib"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html#cfn-workspaces-workspace-workspaceproperties-rootvolumesizegib"""
    p_RunningMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RunningMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html#cfn-workspaces-workspace-workspaceproperties-runningmode"""
    p_RunningModeAutoStopTimeoutInMinutes: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "RunningModeAutoStopTimeoutInMinutes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html#cfn-workspaces-workspace-workspaceproperties-runningmodeautostoptimeoutinminutes"""
    p_UserVolumeSizeGib: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "UserVolumeSizeGib"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html#cfn-workspaces-workspace-workspaceproperties-uservolumesizegib"""

@attr.s
class PropConnectionAliasConnectionAliasAssociation(Property):
    """
    AWS Object Type = "AWS::WorkSpaces::ConnectionAlias.ConnectionAliasAssociation"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-connectionalias-connectionaliasassociation.html

    Property Document:
    
    - ``p_AssociatedAccountId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-connectionalias-connectionaliasassociation.html#cfn-workspaces-connectionalias-connectionaliasassociation-associatedaccountid
    - ``p_AssociationStatus``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-connectionalias-connectionaliasassociation.html#cfn-workspaces-connectionalias-connectionaliasassociation-associationstatus
    - ``p_ConnectionIdentifier``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-connectionalias-connectionaliasassociation.html#cfn-workspaces-connectionalias-connectionaliasassociation-connectionidentifier
    - ``p_ResourceId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-connectionalias-connectionaliasassociation.html#cfn-workspaces-connectionalias-connectionaliasassociation-resourceid
    """
    AWS_OBJECT_TYPE = "AWS::WorkSpaces::ConnectionAlias.ConnectionAliasAssociation"
    
    p_AssociatedAccountId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AssociatedAccountId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-connectionalias-connectionaliasassociation.html#cfn-workspaces-connectionalias-connectionaliasassociation-associatedaccountid"""
    p_AssociationStatus: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AssociationStatus"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-connectionalias-connectionaliasassociation.html#cfn-workspaces-connectionalias-connectionaliasassociation-associationstatus"""
    p_ConnectionIdentifier: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ConnectionIdentifier"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-connectionalias-connectionaliasassociation.html#cfn-workspaces-connectionalias-connectionaliasassociation-connectionidentifier"""
    p_ResourceId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-connectionalias-connectionaliasassociation.html#cfn-workspaces-connectionalias-connectionaliasassociation-resourceid"""


#--- Resource declaration ---

@attr.s
class ConnectionAlias(Resource):
    """
    AWS Object Type = "AWS::WorkSpaces::ConnectionAlias"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-connectionalias.html

    Property Document:
    
    - ``rp_ConnectionString``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-connectionalias.html#cfn-workspaces-connectionalias-connectionstring
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-connectionalias.html#cfn-workspaces-connectionalias-tags
    """
    AWS_OBJECT_TYPE = "AWS::WorkSpaces::ConnectionAlias"

    
    rp_ConnectionString: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ConnectionString"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-connectionalias.html#cfn-workspaces-connectionalias-connectionstring"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-connectionalias.html#cfn-workspaces-connectionalias-tags"""

    
    @property
    def rv_Associations(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-connectionalias.html#aws-resource-workspaces-connectionalias-return-values"""
        return GetAtt(resource=self, attr_name="Associations")
    
    @property
    def rv_AliasId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-connectionalias.html#aws-resource-workspaces-connectionalias-return-values"""
        return GetAtt(resource=self, attr_name="AliasId")
    
    @property
    def rv_ConnectionAliasState(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-connectionalias.html#aws-resource-workspaces-connectionalias-return-values"""
        return GetAtt(resource=self, attr_name="ConnectionAliasState")
    

@attr.s
class Workspace(Resource):
    """
    AWS Object Type = "AWS::WorkSpaces::Workspace"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html

    Property Document:
    
    - ``rp_BundleId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-bundleid
    - ``rp_DirectoryId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-directoryid
    - ``rp_UserName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-username
    - ``p_RootVolumeEncryptionEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-rootvolumeencryptionenabled
    - ``p_UserVolumeEncryptionEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-uservolumeencryptionenabled
    - ``p_VolumeEncryptionKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-volumeencryptionkey
    - ``p_WorkspaceProperties``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-workspaceproperties
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-tags
    """
    AWS_OBJECT_TYPE = "AWS::WorkSpaces::Workspace"

    
    rp_BundleId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "BundleId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-bundleid"""
    rp_DirectoryId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DirectoryId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-directoryid"""
    rp_UserName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "UserName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-username"""
    p_RootVolumeEncryptionEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "RootVolumeEncryptionEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-rootvolumeencryptionenabled"""
    p_UserVolumeEncryptionEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "UserVolumeEncryptionEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-uservolumeencryptionenabled"""
    p_VolumeEncryptionKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "VolumeEncryptionKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-volumeencryptionkey"""
    p_WorkspaceProperties: typing.Union['PropWorkspaceWorkspaceProperties', dict] = attr.ib(
        default=None,
        converter=PropWorkspaceWorkspaceProperties.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWorkspaceWorkspaceProperties)),
        metadata={AttrMeta.PROPERTY_NAME: "WorkspaceProperties"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-workspaceproperties"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-tags"""

    
