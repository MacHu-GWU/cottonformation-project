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
class PropAccessPointTransformationConfiguration(Property):
    """
    AWS Object Type = "AWS::S3ObjectLambda::AccessPoint.TransformationConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-transformationconfiguration.html

    Property Document:
    
    - ``rp_Actions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-transformationconfiguration.html#cfn-s3objectlambda-accesspoint-transformationconfiguration-actions
    - ``rp_ContentTransformation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-transformationconfiguration.html#cfn-s3objectlambda-accesspoint-transformationconfiguration-contenttransformation
    """
    AWS_OBJECT_TYPE = "AWS::S3ObjectLambda::AccessPoint.TransformationConfiguration"
    
    rp_Actions: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Actions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-transformationconfiguration.html#cfn-s3objectlambda-accesspoint-transformationconfiguration-actions"""
    rp_ContentTransformation: dict = attr.ib(
        default=None,
        validator=attr.validators.instance_of(dict),
        metadata={AttrMeta.PROPERTY_NAME: "ContentTransformation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-transformationconfiguration.html#cfn-s3objectlambda-accesspoint-transformationconfiguration-contenttransformation"""

@attr.s
class PropAccessPointObjectLambdaConfiguration(Property):
    """
    AWS Object Type = "AWS::S3ObjectLambda::AccessPoint.ObjectLambdaConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-objectlambdaconfiguration.html

    Property Document:
    
    - ``rp_SupportingAccessPoint``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-objectlambdaconfiguration.html#cfn-s3objectlambda-accesspoint-objectlambdaconfiguration-supportingaccesspoint
    - ``rp_TransformationConfigurations``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-objectlambdaconfiguration.html#cfn-s3objectlambda-accesspoint-objectlambdaconfiguration-transformationconfigurations
    - ``p_AllowedFeatures``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-objectlambdaconfiguration.html#cfn-s3objectlambda-accesspoint-objectlambdaconfiguration-allowedfeatures
    - ``p_CloudWatchMetricsEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-objectlambdaconfiguration.html#cfn-s3objectlambda-accesspoint-objectlambdaconfiguration-cloudwatchmetricsenabled
    """
    AWS_OBJECT_TYPE = "AWS::S3ObjectLambda::AccessPoint.ObjectLambdaConfiguration"
    
    rp_SupportingAccessPoint: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SupportingAccessPoint"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-objectlambdaconfiguration.html#cfn-s3objectlambda-accesspoint-objectlambdaconfiguration-supportingaccesspoint"""
    rp_TransformationConfigurations: typing.List[typing.Union['PropAccessPointTransformationConfiguration', dict]] = attr.ib(
        default=None,
        converter=PropAccessPointTransformationConfiguration.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropAccessPointTransformationConfiguration), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "TransformationConfigurations"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-objectlambdaconfiguration.html#cfn-s3objectlambda-accesspoint-objectlambdaconfiguration-transformationconfigurations"""
    p_AllowedFeatures: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AllowedFeatures"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-objectlambdaconfiguration.html#cfn-s3objectlambda-accesspoint-objectlambdaconfiguration-allowedfeatures"""
    p_CloudWatchMetricsEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "CloudWatchMetricsEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-objectlambdaconfiguration.html#cfn-s3objectlambda-accesspoint-objectlambdaconfiguration-cloudwatchmetricsenabled"""


#--- Resource declaration ---

@attr.s
class AccessPoint(Resource):
    """
    AWS Object Type = "AWS::S3ObjectLambda::AccessPoint"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspoint.html

    Property Document:
    
    - ``rp_ObjectLambdaConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspoint.html#cfn-s3objectlambda-accesspoint-objectlambdaconfiguration
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspoint.html#cfn-s3objectlambda-accesspoint-name
    """
    AWS_OBJECT_TYPE = "AWS::S3ObjectLambda::AccessPoint"

    
    rp_ObjectLambdaConfiguration: typing.Union['PropAccessPointObjectLambdaConfiguration', dict] = attr.ib(
        default=None,
        converter=PropAccessPointObjectLambdaConfiguration.from_dict,
        validator=attr.validators.instance_of(PropAccessPointObjectLambdaConfiguration),
        metadata={AttrMeta.PROPERTY_NAME: "ObjectLambdaConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspoint.html#cfn-s3objectlambda-accesspoint-objectlambdaconfiguration"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspoint.html#cfn-s3objectlambda-accesspoint-name"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspoint.html#aws-resource-s3objectlambda-accesspoint-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_CreationDate(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspoint.html#aws-resource-s3objectlambda-accesspoint-return-values"""
        return GetAtt(resource=self, attr_name="CreationDate")
    

@attr.s
class AccessPointPolicy(Resource):
    """
    AWS Object Type = "AWS::S3ObjectLambda::AccessPointPolicy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspointpolicy.html

    Property Document:
    
    - ``rp_ObjectLambdaAccessPoint``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspointpolicy.html#cfn-s3objectlambda-accesspointpolicy-objectlambdaaccesspoint
    - ``rp_PolicyDocument``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspointpolicy.html#cfn-s3objectlambda-accesspointpolicy-policydocument
    """
    AWS_OBJECT_TYPE = "AWS::S3ObjectLambda::AccessPointPolicy"

    
    rp_ObjectLambdaAccessPoint: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ObjectLambdaAccessPoint"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspointpolicy.html#cfn-s3objectlambda-accesspointpolicy-objectlambdaaccesspoint"""
    rp_PolicyDocument: dict = attr.ib(
        default=None,
        validator=attr.validators.instance_of(dict),
        metadata={AttrMeta.PROPERTY_NAME: "PolicyDocument"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspointpolicy.html#cfn-s3objectlambda-accesspointpolicy-policydocument"""

    
