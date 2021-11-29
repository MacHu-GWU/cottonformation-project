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
class PropClusterEndpoint(Property):
    """
    AWS Object Type = "AWS::MemoryDB::Cluster.Endpoint"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-memorydb-cluster-endpoint.html

    Property Document:
    
    - ``p_Address``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-memorydb-cluster-endpoint.html#cfn-memorydb-cluster-endpoint-address
    - ``p_Port``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-memorydb-cluster-endpoint.html#cfn-memorydb-cluster-endpoint-port
    """
    AWS_OBJECT_TYPE = "AWS::MemoryDB::Cluster.Endpoint"
    
    p_Address: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Address"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-memorydb-cluster-endpoint.html#cfn-memorydb-cluster-endpoint-address"""
    p_Port: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Port"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-memorydb-cluster-endpoint.html#cfn-memorydb-cluster-endpoint-port"""


#--- Resource declaration ---

@attr.s
class ParameterGroup(Resource):
    """
    AWS Object Type = "AWS::MemoryDB::ParameterGroup"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-parametergroup.html

    Property Document:
    
    - ``rp_Family``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-parametergroup.html#cfn-memorydb-parametergroup-family
    - ``rp_ParameterGroupName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-parametergroup.html#cfn-memorydb-parametergroup-parametergroupname
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-parametergroup.html#cfn-memorydb-parametergroup-description
    - ``p_Parameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-parametergroup.html#cfn-memorydb-parametergroup-parameters
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-parametergroup.html#cfn-memorydb-parametergroup-tags
    """
    AWS_OBJECT_TYPE = "AWS::MemoryDB::ParameterGroup"

    
    rp_Family: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Family"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-parametergroup.html#cfn-memorydb-parametergroup-family"""
    rp_ParameterGroupName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ParameterGroupName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-parametergroup.html#cfn-memorydb-parametergroup-parametergroupname"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-parametergroup.html#cfn-memorydb-parametergroup-description"""
    p_Parameters: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Parameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-parametergroup.html#cfn-memorydb-parametergroup-parameters"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-parametergroup.html#cfn-memorydb-parametergroup-tags"""

    
    @property
    def rv_ARN(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-parametergroup.html#aws-resource-memorydb-parametergroup-return-values"""
        return GetAtt(resource=self, attr_name="ARN")
    

@attr.s
class ACL(Resource):
    """
    AWS Object Type = "AWS::MemoryDB::ACL"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-acl.html

    Property Document:
    
    - ``rp_ACLName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-acl.html#cfn-memorydb-acl-aclname
    - ``p_UserNames``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-acl.html#cfn-memorydb-acl-usernames
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-acl.html#cfn-memorydb-acl-tags
    """
    AWS_OBJECT_TYPE = "AWS::MemoryDB::ACL"

    
    rp_ACLName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ACLName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-acl.html#cfn-memorydb-acl-aclname"""
    p_UserNames: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "UserNames"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-acl.html#cfn-memorydb-acl-usernames"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-acl.html#cfn-memorydb-acl-tags"""

    
    @property
    def rv_Status(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-acl.html#aws-resource-memorydb-acl-return-values"""
        return GetAtt(resource=self, attr_name="Status")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-acl.html#aws-resource-memorydb-acl-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class User(Resource):
    """
    AWS Object Type = "AWS::MemoryDB::User"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-user.html

    Property Document:
    
    - ``rp_AccessString``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-user.html#cfn-memorydb-user-accessstring
    - ``rp_AuthenticationMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-user.html#cfn-memorydb-user-authenticationmode
    - ``rp_UserName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-user.html#cfn-memorydb-user-username
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-user.html#cfn-memorydb-user-tags
    """
    AWS_OBJECT_TYPE = "AWS::MemoryDB::User"

    
    rp_AccessString: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AccessString"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-user.html#cfn-memorydb-user-accessstring"""
    rp_AuthenticationMode: dict = attr.ib(
        default=None,
        validator=attr.validators.instance_of(dict),
        metadata={AttrMeta.PROPERTY_NAME: "AuthenticationMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-user.html#cfn-memorydb-user-authenticationmode"""
    rp_UserName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "UserName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-user.html#cfn-memorydb-user-username"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-user.html#cfn-memorydb-user-tags"""

    
    @property
    def rv_Status(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-user.html#aws-resource-memorydb-user-return-values"""
        return GetAtt(resource=self, attr_name="Status")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-user.html#aws-resource-memorydb-user-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class SubnetGroup(Resource):
    """
    AWS Object Type = "AWS::MemoryDB::SubnetGroup"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-subnetgroup.html

    Property Document:
    
    - ``rp_SubnetGroupName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-subnetgroup.html#cfn-memorydb-subnetgroup-subnetgroupname
    - ``rp_SubnetIds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-subnetgroup.html#cfn-memorydb-subnetgroup-subnetids
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-subnetgroup.html#cfn-memorydb-subnetgroup-description
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-subnetgroup.html#cfn-memorydb-subnetgroup-tags
    """
    AWS_OBJECT_TYPE = "AWS::MemoryDB::SubnetGroup"

    
    rp_SubnetGroupName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SubnetGroupName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-subnetgroup.html#cfn-memorydb-subnetgroup-subnetgroupname"""
    rp_SubnetIds: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "SubnetIds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-subnetgroup.html#cfn-memorydb-subnetgroup-subnetids"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-subnetgroup.html#cfn-memorydb-subnetgroup-description"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-subnetgroup.html#cfn-memorydb-subnetgroup-tags"""

    
    @property
    def rv_ARN(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-subnetgroup.html#aws-resource-memorydb-subnetgroup-return-values"""
        return GetAtt(resource=self, attr_name="ARN")
    

@attr.s
class Cluster(Resource):
    """
    AWS Object Type = "AWS::MemoryDB::Cluster"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html

    Property Document:
    
    - ``rp_ACLName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-aclname
    - ``rp_ClusterName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-clustername
    - ``rp_NodeType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-nodetype
    - ``p_AutoMinorVersionUpgrade``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-autominorversionupgrade
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-description
    - ``p_EngineVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-engineversion
    - ``p_FinalSnapshotName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-finalsnapshotname
    - ``p_KmsKeyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-kmskeyid
    - ``p_MaintenanceWindow``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-maintenancewindow
    - ``p_NumReplicasPerShard``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-numreplicaspershard
    - ``p_NumShards``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-numshards
    - ``p_ParameterGroupName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-parametergroupname
    - ``p_Port``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-port
    - ``p_SecurityGroupIds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-securitygroupids
    - ``p_SnapshotArns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-snapshotarns
    - ``p_SnapshotName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-snapshotname
    - ``p_SnapshotRetentionLimit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-snapshotretentionlimit
    - ``p_SnapshotWindow``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-snapshotwindow
    - ``p_SnsTopicArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-snstopicarn
    - ``p_SnsTopicStatus``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-snstopicstatus
    - ``p_SubnetGroupName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-subnetgroupname
    - ``p_TLSEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-tlsenabled
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-tags
    """
    AWS_OBJECT_TYPE = "AWS::MemoryDB::Cluster"

    
    rp_ACLName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ACLName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-aclname"""
    rp_ClusterName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ClusterName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-clustername"""
    rp_NodeType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "NodeType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-nodetype"""
    p_AutoMinorVersionUpgrade: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "AutoMinorVersionUpgrade"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-autominorversionupgrade"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-description"""
    p_EngineVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "EngineVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-engineversion"""
    p_FinalSnapshotName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "FinalSnapshotName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-finalsnapshotname"""
    p_KmsKeyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "KmsKeyId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-kmskeyid"""
    p_MaintenanceWindow: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MaintenanceWindow"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-maintenancewindow"""
    p_NumReplicasPerShard: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "NumReplicasPerShard"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-numreplicaspershard"""
    p_NumShards: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "NumShards"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-numshards"""
    p_ParameterGroupName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ParameterGroupName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-parametergroupname"""
    p_Port: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Port"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-port"""
    p_SecurityGroupIds: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SecurityGroupIds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-securitygroupids"""
    p_SnapshotArns: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SnapshotArns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-snapshotarns"""
    p_SnapshotName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SnapshotName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-snapshotname"""
    p_SnapshotRetentionLimit: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "SnapshotRetentionLimit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-snapshotretentionlimit"""
    p_SnapshotWindow: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SnapshotWindow"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-snapshotwindow"""
    p_SnsTopicArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SnsTopicArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-snstopicarn"""
    p_SnsTopicStatus: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SnsTopicStatus"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-snstopicstatus"""
    p_SubnetGroupName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SubnetGroupName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-subnetgroupname"""
    p_TLSEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "TLSEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-tlsenabled"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#cfn-memorydb-cluster-tags"""

    
    @property
    def rv_Status(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#aws-resource-memorydb-cluster-return-values"""
        return GetAtt(resource=self, attr_name="Status")
    
    @property
    def rv_ParameterGroupStatus(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#aws-resource-memorydb-cluster-return-values"""
        return GetAtt(resource=self, attr_name="ParameterGroupStatus")
    
    @property
    def rv_ARN(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#aws-resource-memorydb-cluster-return-values"""
        return GetAtt(resource=self, attr_name="ARN")
    
    @property
    def rv_ClusterEndpointAddress(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#aws-resource-memorydb-cluster-return-values"""
        return GetAtt(resource=self, attr_name="ClusterEndpoint.Address")
    
    @property
    def rv_ClusterEndpointPort(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html#aws-resource-memorydb-cluster-return-values"""
        return GetAtt(resource=self, attr_name="ClusterEndpoint.Port")
    
