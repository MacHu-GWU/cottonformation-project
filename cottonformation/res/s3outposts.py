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
class PropBucketAbortIncompleteMultipartUpload(Property):
    """
    AWS Object Type = "AWS::S3Outposts::Bucket.AbortIncompleteMultipartUpload"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-abortincompletemultipartupload.html

    Property Document:
    
    - ``rp_DaysAfterInitiation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-abortincompletemultipartupload.html#cfn-s3outposts-bucket-abortincompletemultipartupload-daysafterinitiation
    """
    AWS_OBJECT_TYPE = "AWS::S3Outposts::Bucket.AbortIncompleteMultipartUpload"
    
    rp_DaysAfterInitiation: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "DaysAfterInitiation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-abortincompletemultipartupload.html#cfn-s3outposts-bucket-abortincompletemultipartupload-daysafterinitiation"""

@attr.s
class PropAccessPointVpcConfiguration(Property):
    """
    AWS Object Type = "AWS::S3Outposts::AccessPoint.VpcConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-accesspoint-vpcconfiguration.html

    Property Document:
    
    - ``p_VpcId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-accesspoint-vpcconfiguration.html#cfn-s3outposts-accesspoint-vpcconfiguration-vpcid
    """
    AWS_OBJECT_TYPE = "AWS::S3Outposts::AccessPoint.VpcConfiguration"
    
    p_VpcId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "VpcId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-accesspoint-vpcconfiguration.html#cfn-s3outposts-accesspoint-vpcconfiguration-vpcid"""

@attr.s
class PropBucketRule(Property):
    """
    AWS Object Type = "AWS::S3Outposts::Bucket.Rule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html

    Property Document:
    
    - ``p_AbortIncompleteMultipartUpload``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html#cfn-s3outposts-bucket-rule-abortincompletemultipartupload
    - ``p_ExpirationDate``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html#cfn-s3outposts-bucket-rule-expirationdate
    - ``p_ExpirationInDays``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html#cfn-s3outposts-bucket-rule-expirationindays
    - ``p_Filter``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html#cfn-s3outposts-bucket-rule-filter
    - ``p_Id``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html#cfn-s3outposts-bucket-rule-id
    - ``p_Status``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html#cfn-s3outposts-bucket-rule-status
    """
    AWS_OBJECT_TYPE = "AWS::S3Outposts::Bucket.Rule"
    
    p_AbortIncompleteMultipartUpload: typing.Union['PropBucketAbortIncompleteMultipartUpload', dict] = attr.ib(
        default=None,
        converter=PropBucketAbortIncompleteMultipartUpload.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBucketAbortIncompleteMultipartUpload)),
        metadata={AttrMeta.PROPERTY_NAME: "AbortIncompleteMultipartUpload"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html#cfn-s3outposts-bucket-rule-abortincompletemultipartupload"""
    p_ExpirationDate: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ExpirationDate"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html#cfn-s3outposts-bucket-rule-expirationdate"""
    p_ExpirationInDays: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ExpirationInDays"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html#cfn-s3outposts-bucket-rule-expirationindays"""
    p_Filter: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Filter"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html#cfn-s3outposts-bucket-rule-filter"""
    p_Id: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Id"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html#cfn-s3outposts-bucket-rule-id"""
    p_Status: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Status"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html#cfn-s3outposts-bucket-rule-status"""

@attr.s
class PropEndpointNetworkInterface(Property):
    """
    AWS Object Type = "AWS::S3Outposts::Endpoint.NetworkInterface"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-endpoint-networkinterface.html

    Property Document:
    
    - ``rp_NetworkInterfaceId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-endpoint-networkinterface.html#cfn-s3outposts-endpoint-networkinterface-networkinterfaceid
    """
    AWS_OBJECT_TYPE = "AWS::S3Outposts::Endpoint.NetworkInterface"
    
    rp_NetworkInterfaceId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "NetworkInterfaceId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-endpoint-networkinterface.html#cfn-s3outposts-endpoint-networkinterface-networkinterfaceid"""

@attr.s
class PropBucketLifecycleConfiguration(Property):
    """
    AWS Object Type = "AWS::S3Outposts::Bucket.LifecycleConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-lifecycleconfiguration.html

    Property Document:
    
    - ``rp_Rules``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-lifecycleconfiguration.html#cfn-s3outposts-bucket-lifecycleconfiguration-rules
    """
    AWS_OBJECT_TYPE = "AWS::S3Outposts::Bucket.LifecycleConfiguration"
    
    rp_Rules: typing.List[typing.Union['PropBucketRule', dict]] = attr.ib(
        default=None,
        converter=PropBucketRule.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBucketRule), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Rules"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-lifecycleconfiguration.html#cfn-s3outposts-bucket-lifecycleconfiguration-rules"""


#--- Resource declaration ---

@attr.s
class Endpoint(Resource):
    """
    AWS Object Type = "AWS::S3Outposts::Endpoint"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html

    Property Document:
    
    - ``rp_OutpostId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-outpostid
    - ``rp_SecurityGroupId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-securitygroupid
    - ``rp_SubnetId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-subnetid
    - ``p_AccessType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-accesstype
    - ``p_CustomerOwnedIpv4Pool``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-customerownedipv4pool
    """
    AWS_OBJECT_TYPE = "AWS::S3Outposts::Endpoint"

    
    rp_OutpostId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "OutpostId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-outpostid"""
    rp_SecurityGroupId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SecurityGroupId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-securitygroupid"""
    rp_SubnetId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SubnetId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-subnetid"""
    p_AccessType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AccessType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-accesstype"""
    p_CustomerOwnedIpv4Pool: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomerOwnedIpv4Pool"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-customerownedipv4pool"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#aws-resource-s3outposts-endpoint-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_CidrBlock(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#aws-resource-s3outposts-endpoint-return-values"""
        return GetAtt(resource=self, attr_name="CidrBlock")
    
    @property
    def rv_CreationTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#aws-resource-s3outposts-endpoint-return-values"""
        return GetAtt(resource=self, attr_name="CreationTime")
    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#aws-resource-s3outposts-endpoint-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_NetworkInterfaces(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#aws-resource-s3outposts-endpoint-return-values"""
        return GetAtt(resource=self, attr_name="NetworkInterfaces")
    
    @property
    def rv_Status(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#aws-resource-s3outposts-endpoint-return-values"""
        return GetAtt(resource=self, attr_name="Status")
    

@attr.s
class AccessPoint(Resource):
    """
    AWS Object Type = "AWS::S3Outposts::AccessPoint"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html

    Property Document:
    
    - ``rp_Bucket``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html#cfn-s3outposts-accesspoint-bucket
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html#cfn-s3outposts-accesspoint-name
    - ``rp_VpcConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html#cfn-s3outposts-accesspoint-vpcconfiguration
    - ``p_Policy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html#cfn-s3outposts-accesspoint-policy
    """
    AWS_OBJECT_TYPE = "AWS::S3Outposts::AccessPoint"

    
    rp_Bucket: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Bucket"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html#cfn-s3outposts-accesspoint-bucket"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html#cfn-s3outposts-accesspoint-name"""
    rp_VpcConfiguration: typing.Union['PropAccessPointVpcConfiguration', dict] = attr.ib(
        default=None,
        converter=PropAccessPointVpcConfiguration.from_dict,
        validator=attr.validators.instance_of(PropAccessPointVpcConfiguration),
        metadata={AttrMeta.PROPERTY_NAME: "VpcConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html#cfn-s3outposts-accesspoint-vpcconfiguration"""
    p_Policy: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Policy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html#cfn-s3outposts-accesspoint-policy"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html#aws-resource-s3outposts-accesspoint-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class Bucket(Resource):
    """
    AWS Object Type = "AWS::S3Outposts::Bucket"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html

    Property Document:
    
    - ``rp_BucketName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html#cfn-s3outposts-bucket-bucketname
    - ``rp_OutpostId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html#cfn-s3outposts-bucket-outpostid
    - ``p_LifecycleConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html#cfn-s3outposts-bucket-lifecycleconfiguration
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html#cfn-s3outposts-bucket-tags
    """
    AWS_OBJECT_TYPE = "AWS::S3Outposts::Bucket"

    
    rp_BucketName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "BucketName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html#cfn-s3outposts-bucket-bucketname"""
    rp_OutpostId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "OutpostId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html#cfn-s3outposts-bucket-outpostid"""
    p_LifecycleConfiguration: typing.Union['PropBucketLifecycleConfiguration', dict] = attr.ib(
        default=None,
        converter=PropBucketLifecycleConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBucketLifecycleConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "LifecycleConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html#cfn-s3outposts-bucket-lifecycleconfiguration"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html#cfn-s3outposts-bucket-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html#aws-resource-s3outposts-bucket-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class BucketPolicy(Resource):
    """
    AWS Object Type = "AWS::S3Outposts::BucketPolicy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucketpolicy.html

    Property Document:
    
    - ``rp_Bucket``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucketpolicy.html#cfn-s3outposts-bucketpolicy-bucket
    - ``rp_PolicyDocument``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucketpolicy.html#cfn-s3outposts-bucketpolicy-policydocument
    """
    AWS_OBJECT_TYPE = "AWS::S3Outposts::BucketPolicy"

    
    rp_Bucket: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Bucket"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucketpolicy.html#cfn-s3outposts-bucketpolicy-bucket"""
    rp_PolicyDocument: dict = attr.ib(
        default=None,
        validator=attr.validators.instance_of(dict),
        metadata={AttrMeta.PROPERTY_NAME: "PolicyDocument"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucketpolicy.html#cfn-s3outposts-bucketpolicy-policydocument"""

    
