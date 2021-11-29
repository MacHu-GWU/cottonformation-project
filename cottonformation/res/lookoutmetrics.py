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
class PropAnomalyDetectorCsvFormatDescriptor(Property):
    """
    AWS Object Type = "AWS::LookoutMetrics::AnomalyDetector.CsvFormatDescriptor"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html

    Property Document:
    
    - ``p_Charset``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-csvformatdescriptor-charset
    - ``p_ContainsHeader``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-csvformatdescriptor-containsheader
    - ``p_Delimiter``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-csvformatdescriptor-delimiter
    - ``p_FileCompression``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-csvformatdescriptor-filecompression
    - ``p_HeaderList``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-csvformatdescriptor-headerlist
    - ``p_QuoteSymbol``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-csvformatdescriptor-quotesymbol
    """
    AWS_OBJECT_TYPE = "AWS::LookoutMetrics::AnomalyDetector.CsvFormatDescriptor"
    
    p_Charset: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Charset"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-csvformatdescriptor-charset"""
    p_ContainsHeader: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "ContainsHeader"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-csvformatdescriptor-containsheader"""
    p_Delimiter: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Delimiter"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-csvformatdescriptor-delimiter"""
    p_FileCompression: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "FileCompression"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-csvformatdescriptor-filecompression"""
    p_HeaderList: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "HeaderList"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-csvformatdescriptor-headerlist"""
    p_QuoteSymbol: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "QuoteSymbol"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-csvformatdescriptor-quotesymbol"""

@attr.s
class PropAnomalyDetectorVpcConfiguration(Property):
    """
    AWS Object Type = "AWS::LookoutMetrics::AnomalyDetector.VpcConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-vpcconfiguration.html

    Property Document:
    
    - ``rp_SecurityGroupIdList``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-vpcconfiguration.html#cfn-lookoutmetrics-anomalydetector-vpcconfiguration-securitygroupidlist
    - ``rp_SubnetIdList``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-vpcconfiguration.html#cfn-lookoutmetrics-anomalydetector-vpcconfiguration-subnetidlist
    """
    AWS_OBJECT_TYPE = "AWS::LookoutMetrics::AnomalyDetector.VpcConfiguration"
    
    rp_SecurityGroupIdList: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "SecurityGroupIdList"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-vpcconfiguration.html#cfn-lookoutmetrics-anomalydetector-vpcconfiguration-securitygroupidlist"""
    rp_SubnetIdList: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "SubnetIdList"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-vpcconfiguration.html#cfn-lookoutmetrics-anomalydetector-vpcconfiguration-subnetidlist"""

@attr.s
class PropAlertSNSConfiguration(Property):
    """
    AWS Object Type = "AWS::LookoutMetrics::Alert.SNSConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-snsconfiguration.html

    Property Document:
    
    - ``rp_RoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-snsconfiguration.html#cfn-lookoutmetrics-alert-snsconfiguration-rolearn
    - ``rp_SnsTopicArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-snsconfiguration.html#cfn-lookoutmetrics-alert-snsconfiguration-snstopicarn
    """
    AWS_OBJECT_TYPE = "AWS::LookoutMetrics::Alert.SNSConfiguration"
    
    rp_RoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-snsconfiguration.html#cfn-lookoutmetrics-alert-snsconfiguration-rolearn"""
    rp_SnsTopicArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SnsTopicArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-snsconfiguration.html#cfn-lookoutmetrics-alert-snsconfiguration-snstopicarn"""

@attr.s
class PropAnomalyDetectorRDSSourceConfig(Property):
    """
    AWS Object Type = "AWS::LookoutMetrics::AnomalyDetector.RDSSourceConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html

    Property Document:
    
    - ``rp_DBInstanceIdentifier``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-dbinstanceidentifier
    - ``rp_DatabaseHost``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-databasehost
    - ``rp_DatabaseName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-databasename
    - ``rp_DatabasePort``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-databaseport
    - ``rp_RoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-rolearn
    - ``rp_SecretManagerArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-secretmanagerarn
    - ``rp_TableName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-tablename
    - ``rp_VpcConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-vpcconfiguration
    """
    AWS_OBJECT_TYPE = "AWS::LookoutMetrics::AnomalyDetector.RDSSourceConfig"
    
    rp_DBInstanceIdentifier: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DBInstanceIdentifier"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-dbinstanceidentifier"""
    rp_DatabaseHost: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DatabaseHost"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-databasehost"""
    rp_DatabaseName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DatabaseName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-databasename"""
    rp_DatabasePort: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "DatabasePort"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-databaseport"""
    rp_RoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-rolearn"""
    rp_SecretManagerArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SecretManagerArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-secretmanagerarn"""
    rp_TableName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TableName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-tablename"""
    rp_VpcConfiguration: typing.Union['PropAnomalyDetectorVpcConfiguration', dict] = attr.ib(
        default=None,
        converter=PropAnomalyDetectorVpcConfiguration.from_dict,
        validator=attr.validators.instance_of(PropAnomalyDetectorVpcConfiguration),
        metadata={AttrMeta.PROPERTY_NAME: "VpcConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-vpcconfiguration"""

@attr.s
class PropAnomalyDetectorTimestampColumn(Property):
    """
    AWS Object Type = "AWS::LookoutMetrics::AnomalyDetector.TimestampColumn"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-timestampcolumn.html

    Property Document:
    
    - ``p_ColumnFormat``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-timestampcolumn.html#cfn-lookoutmetrics-anomalydetector-timestampcolumn-columnformat
    - ``p_ColumnName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-timestampcolumn.html#cfn-lookoutmetrics-anomalydetector-timestampcolumn-columnname
    """
    AWS_OBJECT_TYPE = "AWS::LookoutMetrics::AnomalyDetector.TimestampColumn"
    
    p_ColumnFormat: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ColumnFormat"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-timestampcolumn.html#cfn-lookoutmetrics-anomalydetector-timestampcolumn-columnformat"""
    p_ColumnName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ColumnName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-timestampcolumn.html#cfn-lookoutmetrics-anomalydetector-timestampcolumn-columnname"""

@attr.s
class PropAnomalyDetectorJsonFormatDescriptor(Property):
    """
    AWS Object Type = "AWS::LookoutMetrics::AnomalyDetector.JsonFormatDescriptor"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-jsonformatdescriptor.html

    Property Document:
    
    - ``p_Charset``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-jsonformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-jsonformatdescriptor-charset
    - ``p_FileCompression``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-jsonformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-jsonformatdescriptor-filecompression
    """
    AWS_OBJECT_TYPE = "AWS::LookoutMetrics::AnomalyDetector.JsonFormatDescriptor"
    
    p_Charset: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Charset"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-jsonformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-jsonformatdescriptor-charset"""
    p_FileCompression: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "FileCompression"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-jsonformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-jsonformatdescriptor-filecompression"""

@attr.s
class PropAnomalyDetectorAnomalyDetectorConfig(Property):
    """
    AWS Object Type = "AWS::LookoutMetrics::AnomalyDetector.AnomalyDetectorConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-anomalydetectorconfig.html

    Property Document:
    
    - ``rp_AnomalyDetectorFrequency``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-anomalydetectorconfig.html#cfn-lookoutmetrics-anomalydetector-anomalydetectorconfig-anomalydetectorfrequency
    """
    AWS_OBJECT_TYPE = "AWS::LookoutMetrics::AnomalyDetector.AnomalyDetectorConfig"
    
    rp_AnomalyDetectorFrequency: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AnomalyDetectorFrequency"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-anomalydetectorconfig.html#cfn-lookoutmetrics-anomalydetector-anomalydetectorconfig-anomalydetectorfrequency"""

@attr.s
class PropAnomalyDetectorAppFlowConfig(Property):
    """
    AWS Object Type = "AWS::LookoutMetrics::AnomalyDetector.AppFlowConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-appflowconfig.html

    Property Document:
    
    - ``rp_FlowName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-appflowconfig.html#cfn-lookoutmetrics-anomalydetector-appflowconfig-flowname
    - ``rp_RoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-appflowconfig.html#cfn-lookoutmetrics-anomalydetector-appflowconfig-rolearn
    """
    AWS_OBJECT_TYPE = "AWS::LookoutMetrics::AnomalyDetector.AppFlowConfig"
    
    rp_FlowName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "FlowName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-appflowconfig.html#cfn-lookoutmetrics-anomalydetector-appflowconfig-flowname"""
    rp_RoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-appflowconfig.html#cfn-lookoutmetrics-anomalydetector-appflowconfig-rolearn"""

@attr.s
class PropAlertLambdaConfiguration(Property):
    """
    AWS Object Type = "AWS::LookoutMetrics::Alert.LambdaConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-lambdaconfiguration.html

    Property Document:
    
    - ``rp_LambdaArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-lambdaconfiguration.html#cfn-lookoutmetrics-alert-lambdaconfiguration-lambdaarn
    - ``rp_RoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-lambdaconfiguration.html#cfn-lookoutmetrics-alert-lambdaconfiguration-rolearn
    """
    AWS_OBJECT_TYPE = "AWS::LookoutMetrics::Alert.LambdaConfiguration"
    
    rp_LambdaArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "LambdaArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-lambdaconfiguration.html#cfn-lookoutmetrics-alert-lambdaconfiguration-lambdaarn"""
    rp_RoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-lambdaconfiguration.html#cfn-lookoutmetrics-alert-lambdaconfiguration-rolearn"""

@attr.s
class PropAnomalyDetectorRedshiftSourceConfig(Property):
    """
    AWS Object Type = "AWS::LookoutMetrics::AnomalyDetector.RedshiftSourceConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html

    Property Document:
    
    - ``rp_ClusterIdentifier``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-clusteridentifier
    - ``rp_DatabaseHost``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-databasehost
    - ``rp_DatabaseName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-databasename
    - ``rp_DatabasePort``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-databaseport
    - ``rp_RoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-rolearn
    - ``rp_SecretManagerArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-secretmanagerarn
    - ``rp_TableName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-tablename
    - ``rp_VpcConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-vpcconfiguration
    """
    AWS_OBJECT_TYPE = "AWS::LookoutMetrics::AnomalyDetector.RedshiftSourceConfig"
    
    rp_ClusterIdentifier: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ClusterIdentifier"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-clusteridentifier"""
    rp_DatabaseHost: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DatabaseHost"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-databasehost"""
    rp_DatabaseName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DatabaseName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-databasename"""
    rp_DatabasePort: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "DatabasePort"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-databaseport"""
    rp_RoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-rolearn"""
    rp_SecretManagerArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SecretManagerArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-secretmanagerarn"""
    rp_TableName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TableName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-tablename"""
    rp_VpcConfiguration: typing.Union['PropAnomalyDetectorVpcConfiguration', dict] = attr.ib(
        default=None,
        converter=PropAnomalyDetectorVpcConfiguration.from_dict,
        validator=attr.validators.instance_of(PropAnomalyDetectorVpcConfiguration),
        metadata={AttrMeta.PROPERTY_NAME: "VpcConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-vpcconfiguration"""

@attr.s
class PropAlertAction(Property):
    """
    AWS Object Type = "AWS::LookoutMetrics::Alert.Action"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-action.html

    Property Document:
    
    - ``p_LambdaConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-action.html#cfn-lookoutmetrics-alert-action-lambdaconfiguration
    - ``p_SNSConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-action.html#cfn-lookoutmetrics-alert-action-snsconfiguration
    """
    AWS_OBJECT_TYPE = "AWS::LookoutMetrics::Alert.Action"
    
    p_LambdaConfiguration: typing.Union['PropAlertLambdaConfiguration', dict] = attr.ib(
        default=None,
        converter=PropAlertLambdaConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropAlertLambdaConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "LambdaConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-action.html#cfn-lookoutmetrics-alert-action-lambdaconfiguration"""
    p_SNSConfiguration: typing.Union['PropAlertSNSConfiguration', dict] = attr.ib(
        default=None,
        converter=PropAlertSNSConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropAlertSNSConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "SNSConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-action.html#cfn-lookoutmetrics-alert-action-snsconfiguration"""

@attr.s
class PropAnomalyDetectorMetric(Property):
    """
    AWS Object Type = "AWS::LookoutMetrics::AnomalyDetector.Metric"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metric.html

    Property Document:
    
    - ``rp_AggregationFunction``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metric.html#cfn-lookoutmetrics-anomalydetector-metric-aggregationfunction
    - ``rp_MetricName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metric.html#cfn-lookoutmetrics-anomalydetector-metric-metricname
    - ``p_Namespace``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metric.html#cfn-lookoutmetrics-anomalydetector-metric-namespace
    """
    AWS_OBJECT_TYPE = "AWS::LookoutMetrics::AnomalyDetector.Metric"
    
    rp_AggregationFunction: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AggregationFunction"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metric.html#cfn-lookoutmetrics-anomalydetector-metric-aggregationfunction"""
    rp_MetricName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "MetricName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metric.html#cfn-lookoutmetrics-anomalydetector-metric-metricname"""
    p_Namespace: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Namespace"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metric.html#cfn-lookoutmetrics-anomalydetector-metric-namespace"""

@attr.s
class PropAnomalyDetectorCloudwatchConfig(Property):
    """
    AWS Object Type = "AWS::LookoutMetrics::AnomalyDetector.CloudwatchConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-cloudwatchconfig.html

    Property Document:
    
    - ``rp_RoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-cloudwatchconfig.html#cfn-lookoutmetrics-anomalydetector-cloudwatchconfig-rolearn
    """
    AWS_OBJECT_TYPE = "AWS::LookoutMetrics::AnomalyDetector.CloudwatchConfig"
    
    rp_RoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-cloudwatchconfig.html#cfn-lookoutmetrics-anomalydetector-cloudwatchconfig-rolearn"""

@attr.s
class PropAnomalyDetectorFileFormatDescriptor(Property):
    """
    AWS Object Type = "AWS::LookoutMetrics::AnomalyDetector.FileFormatDescriptor"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-fileformatdescriptor.html

    Property Document:
    
    - ``p_CsvFormatDescriptor``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-fileformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-fileformatdescriptor-csvformatdescriptor
    - ``p_JsonFormatDescriptor``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-fileformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-fileformatdescriptor-jsonformatdescriptor
    """
    AWS_OBJECT_TYPE = "AWS::LookoutMetrics::AnomalyDetector.FileFormatDescriptor"
    
    p_CsvFormatDescriptor: typing.Union['PropAnomalyDetectorCsvFormatDescriptor', dict] = attr.ib(
        default=None,
        converter=PropAnomalyDetectorCsvFormatDescriptor.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropAnomalyDetectorCsvFormatDescriptor)),
        metadata={AttrMeta.PROPERTY_NAME: "CsvFormatDescriptor"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-fileformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-fileformatdescriptor-csvformatdescriptor"""
    p_JsonFormatDescriptor: typing.Union['PropAnomalyDetectorJsonFormatDescriptor', dict] = attr.ib(
        default=None,
        converter=PropAnomalyDetectorJsonFormatDescriptor.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropAnomalyDetectorJsonFormatDescriptor)),
        metadata={AttrMeta.PROPERTY_NAME: "JsonFormatDescriptor"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-fileformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-fileformatdescriptor-jsonformatdescriptor"""

@attr.s
class PropAnomalyDetectorS3SourceConfig(Property):
    """
    AWS Object Type = "AWS::LookoutMetrics::AnomalyDetector.S3SourceConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-s3sourceconfig.html

    Property Document:
    
    - ``rp_FileFormatDescriptor``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-s3sourceconfig.html#cfn-lookoutmetrics-anomalydetector-s3sourceconfig-fileformatdescriptor
    - ``rp_RoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-s3sourceconfig.html#cfn-lookoutmetrics-anomalydetector-s3sourceconfig-rolearn
    - ``p_HistoricalDataPathList``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-s3sourceconfig.html#cfn-lookoutmetrics-anomalydetector-s3sourceconfig-historicaldatapathlist
    - ``p_TemplatedPathList``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-s3sourceconfig.html#cfn-lookoutmetrics-anomalydetector-s3sourceconfig-templatedpathlist
    """
    AWS_OBJECT_TYPE = "AWS::LookoutMetrics::AnomalyDetector.S3SourceConfig"
    
    rp_FileFormatDescriptor: typing.Union['PropAnomalyDetectorFileFormatDescriptor', dict] = attr.ib(
        default=None,
        converter=PropAnomalyDetectorFileFormatDescriptor.from_dict,
        validator=attr.validators.instance_of(PropAnomalyDetectorFileFormatDescriptor),
        metadata={AttrMeta.PROPERTY_NAME: "FileFormatDescriptor"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-s3sourceconfig.html#cfn-lookoutmetrics-anomalydetector-s3sourceconfig-fileformatdescriptor"""
    rp_RoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-s3sourceconfig.html#cfn-lookoutmetrics-anomalydetector-s3sourceconfig-rolearn"""
    p_HistoricalDataPathList: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "HistoricalDataPathList"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-s3sourceconfig.html#cfn-lookoutmetrics-anomalydetector-s3sourceconfig-historicaldatapathlist"""
    p_TemplatedPathList: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "TemplatedPathList"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-s3sourceconfig.html#cfn-lookoutmetrics-anomalydetector-s3sourceconfig-templatedpathlist"""

@attr.s
class PropAnomalyDetectorMetricSource(Property):
    """
    AWS Object Type = "AWS::LookoutMetrics::AnomalyDetector.MetricSource"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html

    Property Document:
    
    - ``p_AppFlowConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html#cfn-lookoutmetrics-anomalydetector-metricsource-appflowconfig
    - ``p_CloudwatchConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html#cfn-lookoutmetrics-anomalydetector-metricsource-cloudwatchconfig
    - ``p_RDSSourceConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html#cfn-lookoutmetrics-anomalydetector-metricsource-rdssourceconfig
    - ``p_RedshiftSourceConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html#cfn-lookoutmetrics-anomalydetector-metricsource-redshiftsourceconfig
    - ``p_S3SourceConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html#cfn-lookoutmetrics-anomalydetector-metricsource-s3sourceconfig
    """
    AWS_OBJECT_TYPE = "AWS::LookoutMetrics::AnomalyDetector.MetricSource"
    
    p_AppFlowConfig: typing.Union['PropAnomalyDetectorAppFlowConfig', dict] = attr.ib(
        default=None,
        converter=PropAnomalyDetectorAppFlowConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropAnomalyDetectorAppFlowConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "AppFlowConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html#cfn-lookoutmetrics-anomalydetector-metricsource-appflowconfig"""
    p_CloudwatchConfig: typing.Union['PropAnomalyDetectorCloudwatchConfig', dict] = attr.ib(
        default=None,
        converter=PropAnomalyDetectorCloudwatchConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropAnomalyDetectorCloudwatchConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "CloudwatchConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html#cfn-lookoutmetrics-anomalydetector-metricsource-cloudwatchconfig"""
    p_RDSSourceConfig: typing.Union['PropAnomalyDetectorRDSSourceConfig', dict] = attr.ib(
        default=None,
        converter=PropAnomalyDetectorRDSSourceConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropAnomalyDetectorRDSSourceConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "RDSSourceConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html#cfn-lookoutmetrics-anomalydetector-metricsource-rdssourceconfig"""
    p_RedshiftSourceConfig: typing.Union['PropAnomalyDetectorRedshiftSourceConfig', dict] = attr.ib(
        default=None,
        converter=PropAnomalyDetectorRedshiftSourceConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropAnomalyDetectorRedshiftSourceConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "RedshiftSourceConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html#cfn-lookoutmetrics-anomalydetector-metricsource-redshiftsourceconfig"""
    p_S3SourceConfig: typing.Union['PropAnomalyDetectorS3SourceConfig', dict] = attr.ib(
        default=None,
        converter=PropAnomalyDetectorS3SourceConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropAnomalyDetectorS3SourceConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "S3SourceConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html#cfn-lookoutmetrics-anomalydetector-metricsource-s3sourceconfig"""

@attr.s
class PropAnomalyDetectorMetricSet(Property):
    """
    AWS Object Type = "AWS::LookoutMetrics::AnomalyDetector.MetricSet"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html

    Property Document:
    
    - ``rp_MetricList``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-metriclist
    - ``rp_MetricSetName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-metricsetname
    - ``rp_MetricSource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-metricsource
    - ``p_DimensionList``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-dimensionlist
    - ``p_MetricSetDescription``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-metricsetdescription
    - ``p_MetricSetFrequency``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-metricsetfrequency
    - ``p_Offset``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-offset
    - ``p_TimestampColumn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-timestampcolumn
    - ``p_Timezone``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-timezone
    """
    AWS_OBJECT_TYPE = "AWS::LookoutMetrics::AnomalyDetector.MetricSet"
    
    rp_MetricList: typing.List[typing.Union['PropAnomalyDetectorMetric', dict]] = attr.ib(
        default=None,
        converter=PropAnomalyDetectorMetric.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropAnomalyDetectorMetric), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "MetricList"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-metriclist"""
    rp_MetricSetName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "MetricSetName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-metricsetname"""
    rp_MetricSource: typing.Union['PropAnomalyDetectorMetricSource', dict] = attr.ib(
        default=None,
        converter=PropAnomalyDetectorMetricSource.from_dict,
        validator=attr.validators.instance_of(PropAnomalyDetectorMetricSource),
        metadata={AttrMeta.PROPERTY_NAME: "MetricSource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-metricsource"""
    p_DimensionList: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "DimensionList"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-dimensionlist"""
    p_MetricSetDescription: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MetricSetDescription"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-metricsetdescription"""
    p_MetricSetFrequency: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MetricSetFrequency"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-metricsetfrequency"""
    p_Offset: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Offset"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-offset"""
    p_TimestampColumn: typing.Union['PropAnomalyDetectorTimestampColumn', dict] = attr.ib(
        default=None,
        converter=PropAnomalyDetectorTimestampColumn.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropAnomalyDetectorTimestampColumn)),
        metadata={AttrMeta.PROPERTY_NAME: "TimestampColumn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-timestampcolumn"""
    p_Timezone: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Timezone"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-timezone"""


#--- Resource declaration ---

@attr.s
class Alert(Resource):
    """
    AWS Object Type = "AWS::LookoutMetrics::Alert"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html

    Property Document:
    
    - ``rp_Action``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#cfn-lookoutmetrics-alert-action
    - ``rp_AlertSensitivityThreshold``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#cfn-lookoutmetrics-alert-alertsensitivitythreshold
    - ``rp_AnomalyDetectorArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#cfn-lookoutmetrics-alert-anomalydetectorarn
    - ``p_AlertDescription``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#cfn-lookoutmetrics-alert-alertdescription
    - ``p_AlertName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#cfn-lookoutmetrics-alert-alertname
    """
    AWS_OBJECT_TYPE = "AWS::LookoutMetrics::Alert"

    
    rp_Action: typing.Union['PropAlertAction', dict] = attr.ib(
        default=None,
        converter=PropAlertAction.from_dict,
        validator=attr.validators.instance_of(PropAlertAction),
        metadata={AttrMeta.PROPERTY_NAME: "Action"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#cfn-lookoutmetrics-alert-action"""
    rp_AlertSensitivityThreshold: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "AlertSensitivityThreshold"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#cfn-lookoutmetrics-alert-alertsensitivitythreshold"""
    rp_AnomalyDetectorArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AnomalyDetectorArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#cfn-lookoutmetrics-alert-anomalydetectorarn"""
    p_AlertDescription: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AlertDescription"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#cfn-lookoutmetrics-alert-alertdescription"""
    p_AlertName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AlertName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#cfn-lookoutmetrics-alert-alertname"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#aws-resource-lookoutmetrics-alert-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class AnomalyDetector(Resource):
    """
    AWS Object Type = "AWS::LookoutMetrics::AnomalyDetector"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html

    Property Document:
    
    - ``rp_AnomalyDetectorConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#cfn-lookoutmetrics-anomalydetector-anomalydetectorconfig
    - ``rp_MetricSetList``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#cfn-lookoutmetrics-anomalydetector-metricsetlist
    - ``p_AnomalyDetectorDescription``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#cfn-lookoutmetrics-anomalydetector-anomalydetectordescription
    - ``p_AnomalyDetectorName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#cfn-lookoutmetrics-anomalydetector-anomalydetectorname
    - ``p_KmsKeyArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#cfn-lookoutmetrics-anomalydetector-kmskeyarn
    """
    AWS_OBJECT_TYPE = "AWS::LookoutMetrics::AnomalyDetector"

    
    rp_AnomalyDetectorConfig: typing.Union['PropAnomalyDetectorAnomalyDetectorConfig', dict] = attr.ib(
        default=None,
        converter=PropAnomalyDetectorAnomalyDetectorConfig.from_dict,
        validator=attr.validators.instance_of(PropAnomalyDetectorAnomalyDetectorConfig),
        metadata={AttrMeta.PROPERTY_NAME: "AnomalyDetectorConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#cfn-lookoutmetrics-anomalydetector-anomalydetectorconfig"""
    rp_MetricSetList: typing.List[typing.Union['PropAnomalyDetectorMetricSet', dict]] = attr.ib(
        default=None,
        converter=PropAnomalyDetectorMetricSet.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropAnomalyDetectorMetricSet), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "MetricSetList"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#cfn-lookoutmetrics-anomalydetector-metricsetlist"""
    p_AnomalyDetectorDescription: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AnomalyDetectorDescription"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#cfn-lookoutmetrics-anomalydetector-anomalydetectordescription"""
    p_AnomalyDetectorName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AnomalyDetectorName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#cfn-lookoutmetrics-anomalydetector-anomalydetectorname"""
    p_KmsKeyArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "KmsKeyArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#cfn-lookoutmetrics-anomalydetector-kmskeyarn"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#aws-resource-lookoutmetrics-anomalydetector-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
