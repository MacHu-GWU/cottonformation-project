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
class PropDataSetJoinKeyProperties(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSet.JoinKeyProperties"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-joinkeyproperties.html

    Property Document:
    
    - ``p_UniqueKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-joinkeyproperties.html#cfn-quicksight-dataset-joinkeyproperties-uniquekey
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSet.JoinKeyProperties"
    
    p_UniqueKey: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "UniqueKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-joinkeyproperties.html#cfn-quicksight-dataset-joinkeyproperties-uniquekey"""

@attr.s
class PropDataSourceAuroraPostgreSqlParameters(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSource.AuroraPostgreSqlParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-aurorapostgresqlparameters.html

    Property Document:
    
    - ``rp_Database``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-aurorapostgresqlparameters.html#cfn-quicksight-datasource-aurorapostgresqlparameters-database
    - ``rp_Host``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-aurorapostgresqlparameters.html#cfn-quicksight-datasource-aurorapostgresqlparameters-host
    - ``rp_Port``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-aurorapostgresqlparameters.html#cfn-quicksight-datasource-aurorapostgresqlparameters-port
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSource.AuroraPostgreSqlParameters"
    
    rp_Database: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Database"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-aurorapostgresqlparameters.html#cfn-quicksight-datasource-aurorapostgresqlparameters-database"""
    rp_Host: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Host"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-aurorapostgresqlparameters.html#cfn-quicksight-datasource-aurorapostgresqlparameters-host"""
    rp_Port: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "Port"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-aurorapostgresqlparameters.html#cfn-quicksight-datasource-aurorapostgresqlparameters-port"""

@attr.s
class PropDataSetUploadSettings(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSet.UploadSettings"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-uploadsettings.html

    Property Document:
    
    - ``p_ContainsHeader``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-uploadsettings.html#cfn-quicksight-dataset-uploadsettings-containsheader
    - ``p_Delimiter``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-uploadsettings.html#cfn-quicksight-dataset-uploadsettings-delimiter
    - ``p_Format``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-uploadsettings.html#cfn-quicksight-dataset-uploadsettings-format
    - ``p_StartFromRow``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-uploadsettings.html#cfn-quicksight-dataset-uploadsettings-startfromrow
    - ``p_TextQualifier``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-uploadsettings.html#cfn-quicksight-dataset-uploadsettings-textqualifier
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSet.UploadSettings"
    
    p_ContainsHeader: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "ContainsHeader"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-uploadsettings.html#cfn-quicksight-dataset-uploadsettings-containsheader"""
    p_Delimiter: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Delimiter"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-uploadsettings.html#cfn-quicksight-dataset-uploadsettings-delimiter"""
    p_Format: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Format"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-uploadsettings.html#cfn-quicksight-dataset-uploadsettings-format"""
    p_StartFromRow: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "StartFromRow"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-uploadsettings.html#cfn-quicksight-dataset-uploadsettings-startfromrow"""
    p_TextQualifier: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TextQualifier"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-uploadsettings.html#cfn-quicksight-dataset-uploadsettings-textqualifier"""

@attr.s
class PropDashboardSheetControlsOption(Property):
    """
    AWS Object Type = "AWS::QuickSight::Dashboard.SheetControlsOption"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-sheetcontrolsoption.html

    Property Document:
    
    - ``p_VisibilityState``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-sheetcontrolsoption.html#cfn-quicksight-dashboard-sheetcontrolsoption-visibilitystate
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Dashboard.SheetControlsOption"
    
    p_VisibilityState: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "VisibilityState"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-sheetcontrolsoption.html#cfn-quicksight-dashboard-sheetcontrolsoption-visibilitystate"""

@attr.s
class PropAnalysisDecimalParameter(Property):
    """
    AWS Object Type = "AWS::QuickSight::Analysis.DecimalParameter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-decimalparameter.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-decimalparameter.html#cfn-quicksight-analysis-decimalparameter-name
    - ``rp_Values``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-decimalparameter.html#cfn-quicksight-analysis-decimalparameter-values
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Analysis.DecimalParameter"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-decimalparameter.html#cfn-quicksight-analysis-decimalparameter-name"""
    rp_Values: typing.List[float] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(float), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Values"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-decimalparameter.html#cfn-quicksight-analysis-decimalparameter-values"""

@attr.s
class PropAnalysisResourcePermission(Property):
    """
    AWS Object Type = "AWS::QuickSight::Analysis.ResourcePermission"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-resourcepermission.html

    Property Document:
    
    - ``rp_Actions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-resourcepermission.html#cfn-quicksight-analysis-resourcepermission-actions
    - ``rp_Principal``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-resourcepermission.html#cfn-quicksight-analysis-resourcepermission-principal
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Analysis.ResourcePermission"
    
    rp_Actions: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Actions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-resourcepermission.html#cfn-quicksight-analysis-resourcepermission-actions"""
    rp_Principal: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Principal"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-resourcepermission.html#cfn-quicksight-analysis-resourcepermission-principal"""

@attr.s
class PropThemeFont(Property):
    """
    AWS Object Type = "AWS::QuickSight::Theme.Font"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-font.html

    Property Document:
    
    - ``p_FontFamily``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-font.html#cfn-quicksight-theme-font-fontfamily
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Theme.Font"
    
    p_FontFamily: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "FontFamily"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-font.html#cfn-quicksight-theme-font-fontfamily"""

@attr.s
class PropThemeBorderStyle(Property):
    """
    AWS Object Type = "AWS::QuickSight::Theme.BorderStyle"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-borderstyle.html

    Property Document:
    
    - ``p_Show``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-borderstyle.html#cfn-quicksight-theme-borderstyle-show
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Theme.BorderStyle"
    
    p_Show: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Show"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-borderstyle.html#cfn-quicksight-theme-borderstyle-show"""

@attr.s
class PropDataSetProjectOperation(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSet.ProjectOperation"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-projectoperation.html

    Property Document:
    
    - ``rp_ProjectedColumns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-projectoperation.html#cfn-quicksight-dataset-projectoperation-projectedcolumns
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSet.ProjectOperation"
    
    rp_ProjectedColumns: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "ProjectedColumns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-projectoperation.html#cfn-quicksight-dataset-projectoperation-projectedcolumns"""

@attr.s
class PropDataSetColumnLevelPermissionRule(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSet.ColumnLevelPermissionRule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-columnlevelpermissionrule.html

    Property Document:
    
    - ``p_ColumnNames``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-columnlevelpermissionrule.html#cfn-quicksight-dataset-columnlevelpermissionrule-columnnames
    - ``p_Principals``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-columnlevelpermissionrule.html#cfn-quicksight-dataset-columnlevelpermissionrule-principals
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSet.ColumnLevelPermissionRule"
    
    p_ColumnNames: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ColumnNames"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-columnlevelpermissionrule.html#cfn-quicksight-dataset-columnlevelpermissionrule-columnnames"""
    p_Principals: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Principals"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-columnlevelpermissionrule.html#cfn-quicksight-dataset-columnlevelpermissionrule-principals"""

@attr.s
class PropDashboardResourcePermission(Property):
    """
    AWS Object Type = "AWS::QuickSight::Dashboard.ResourcePermission"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-resourcepermission.html

    Property Document:
    
    - ``rp_Actions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-resourcepermission.html#cfn-quicksight-dashboard-resourcepermission-actions
    - ``rp_Principal``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-resourcepermission.html#cfn-quicksight-dashboard-resourcepermission-principal
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Dashboard.ResourcePermission"
    
    rp_Actions: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Actions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-resourcepermission.html#cfn-quicksight-dashboard-resourcepermission-actions"""
    rp_Principal: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Principal"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-resourcepermission.html#cfn-quicksight-dashboard-resourcepermission-principal"""

@attr.s
class PropDataSourceSnowflakeParameters(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSource.SnowflakeParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-snowflakeparameters.html

    Property Document:
    
    - ``rp_Database``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-snowflakeparameters.html#cfn-quicksight-datasource-snowflakeparameters-database
    - ``rp_Host``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-snowflakeparameters.html#cfn-quicksight-datasource-snowflakeparameters-host
    - ``rp_Warehouse``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-snowflakeparameters.html#cfn-quicksight-datasource-snowflakeparameters-warehouse
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSource.SnowflakeParameters"
    
    rp_Database: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Database"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-snowflakeparameters.html#cfn-quicksight-datasource-snowflakeparameters-database"""
    rp_Host: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Host"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-snowflakeparameters.html#cfn-quicksight-datasource-snowflakeparameters-host"""
    rp_Warehouse: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Warehouse"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-snowflakeparameters.html#cfn-quicksight-datasource-snowflakeparameters-warehouse"""

@attr.s
class PropDataSourceSslProperties(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSource.SslProperties"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-sslproperties.html

    Property Document:
    
    - ``p_DisableSsl``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-sslproperties.html#cfn-quicksight-datasource-sslproperties-disablessl
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSource.SslProperties"
    
    p_DisableSsl: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "DisableSsl"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-sslproperties.html#cfn-quicksight-datasource-sslproperties-disablessl"""

@attr.s
class PropDataSetColumnDescription(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSet.ColumnDescription"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-columndescription.html

    Property Document:
    
    - ``p_Text``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-columndescription.html#cfn-quicksight-dataset-columndescription-text
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSet.ColumnDescription"
    
    p_Text: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Text"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-columndescription.html#cfn-quicksight-dataset-columndescription-text"""

@attr.s
class PropAnalysisSheet(Property):
    """
    AWS Object Type = "AWS::QuickSight::Analysis.Sheet"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-sheet.html

    Property Document:
    
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-sheet.html#cfn-quicksight-analysis-sheet-name
    - ``p_SheetId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-sheet.html#cfn-quicksight-analysis-sheet-sheetid
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Analysis.Sheet"
    
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-sheet.html#cfn-quicksight-analysis-sheet-name"""
    p_SheetId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SheetId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-sheet.html#cfn-quicksight-analysis-sheet-sheetid"""

@attr.s
class PropDataSetRenameColumnOperation(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSet.RenameColumnOperation"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-renamecolumnoperation.html

    Property Document:
    
    - ``rp_ColumnName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-renamecolumnoperation.html#cfn-quicksight-dataset-renamecolumnoperation-columnname
    - ``rp_NewColumnName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-renamecolumnoperation.html#cfn-quicksight-dataset-renamecolumnoperation-newcolumnname
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSet.RenameColumnOperation"
    
    rp_ColumnName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ColumnName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-renamecolumnoperation.html#cfn-quicksight-dataset-renamecolumnoperation-columnname"""
    rp_NewColumnName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "NewColumnName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-renamecolumnoperation.html#cfn-quicksight-dataset-renamecolumnoperation-newcolumnname"""

@attr.s
class PropDataSourceAmazonOpenSearchParameters(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSource.AmazonOpenSearchParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-amazonopensearchparameters.html

    Property Document:
    
    - ``rp_Domain``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-amazonopensearchparameters.html#cfn-quicksight-datasource-amazonopensearchparameters-domain
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSource.AmazonOpenSearchParameters"
    
    rp_Domain: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Domain"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-amazonopensearchparameters.html#cfn-quicksight-datasource-amazonopensearchparameters-domain"""

@attr.s
class PropTemplateResourcePermission(Property):
    """
    AWS Object Type = "AWS::QuickSight::Template.ResourcePermission"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-resourcepermission.html

    Property Document:
    
    - ``rp_Actions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-resourcepermission.html#cfn-quicksight-template-resourcepermission-actions
    - ``rp_Principal``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-resourcepermission.html#cfn-quicksight-template-resourcepermission-principal
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Template.ResourcePermission"
    
    rp_Actions: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Actions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-resourcepermission.html#cfn-quicksight-template-resourcepermission-actions"""
    rp_Principal: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Principal"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-resourcepermission.html#cfn-quicksight-template-resourcepermission-principal"""

@attr.s
class PropDataSourcePrestoParameters(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSource.PrestoParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-prestoparameters.html

    Property Document:
    
    - ``rp_Catalog``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-prestoparameters.html#cfn-quicksight-datasource-prestoparameters-catalog
    - ``rp_Host``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-prestoparameters.html#cfn-quicksight-datasource-prestoparameters-host
    - ``rp_Port``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-prestoparameters.html#cfn-quicksight-datasource-prestoparameters-port
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSource.PrestoParameters"
    
    rp_Catalog: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Catalog"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-prestoparameters.html#cfn-quicksight-datasource-prestoparameters-catalog"""
    rp_Host: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Host"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-prestoparameters.html#cfn-quicksight-datasource-prestoparameters-host"""
    rp_Port: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "Port"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-prestoparameters.html#cfn-quicksight-datasource-prestoparameters-port"""

@attr.s
class PropDataSetGeoSpatialColumnGroup(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSet.GeoSpatialColumnGroup"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-geospatialcolumngroup.html

    Property Document:
    
    - ``rp_Columns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-geospatialcolumngroup.html#cfn-quicksight-dataset-geospatialcolumngroup-columns
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-geospatialcolumngroup.html#cfn-quicksight-dataset-geospatialcolumngroup-name
    - ``p_CountryCode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-geospatialcolumngroup.html#cfn-quicksight-dataset-geospatialcolumngroup-countrycode
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSet.GeoSpatialColumnGroup"
    
    rp_Columns: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Columns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-geospatialcolumngroup.html#cfn-quicksight-dataset-geospatialcolumngroup-columns"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-geospatialcolumngroup.html#cfn-quicksight-dataset-geospatialcolumngroup-name"""
    p_CountryCode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CountryCode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-geospatialcolumngroup.html#cfn-quicksight-dataset-geospatialcolumngroup-countrycode"""

@attr.s
class PropDataSourceResourcePermission(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSource.ResourcePermission"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-resourcepermission.html

    Property Document:
    
    - ``rp_Actions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-resourcepermission.html#cfn-quicksight-datasource-resourcepermission-actions
    - ``rp_Principal``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-resourcepermission.html#cfn-quicksight-datasource-resourcepermission-principal
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSource.ResourcePermission"
    
    rp_Actions: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Actions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-resourcepermission.html#cfn-quicksight-datasource-resourcepermission-actions"""
    rp_Principal: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Principal"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-resourcepermission.html#cfn-quicksight-datasource-resourcepermission-principal"""

@attr.s
class PropDataSetInputColumn(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSet.InputColumn"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-inputcolumn.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-inputcolumn.html#cfn-quicksight-dataset-inputcolumn-name
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-inputcolumn.html#cfn-quicksight-dataset-inputcolumn-type
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSet.InputColumn"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-inputcolumn.html#cfn-quicksight-dataset-inputcolumn-name"""
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-inputcolumn.html#cfn-quicksight-dataset-inputcolumn-type"""

@attr.s
class PropAnalysisDataSetReference(Property):
    """
    AWS Object Type = "AWS::QuickSight::Analysis.DataSetReference"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-datasetreference.html

    Property Document:
    
    - ``rp_DataSetArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-datasetreference.html#cfn-quicksight-analysis-datasetreference-datasetarn
    - ``rp_DataSetPlaceholder``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-datasetreference.html#cfn-quicksight-analysis-datasetreference-datasetplaceholder
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Analysis.DataSetReference"
    
    rp_DataSetArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DataSetArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-datasetreference.html#cfn-quicksight-analysis-datasetreference-datasetarn"""
    rp_DataSetPlaceholder: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DataSetPlaceholder"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-datasetreference.html#cfn-quicksight-analysis-datasetreference-datasetplaceholder"""

@attr.s
class PropDataSourceSparkParameters(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSource.SparkParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-sparkparameters.html

    Property Document:
    
    - ``rp_Host``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-sparkparameters.html#cfn-quicksight-datasource-sparkparameters-host
    - ``rp_Port``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-sparkparameters.html#cfn-quicksight-datasource-sparkparameters-port
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSource.SparkParameters"
    
    rp_Host: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Host"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-sparkparameters.html#cfn-quicksight-datasource-sparkparameters-host"""
    rp_Port: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "Port"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-sparkparameters.html#cfn-quicksight-datasource-sparkparameters-port"""

@attr.s
class PropDataSourceAuroraParameters(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSource.AuroraParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-auroraparameters.html

    Property Document:
    
    - ``rp_Database``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-auroraparameters.html#cfn-quicksight-datasource-auroraparameters-database
    - ``rp_Host``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-auroraparameters.html#cfn-quicksight-datasource-auroraparameters-host
    - ``rp_Port``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-auroraparameters.html#cfn-quicksight-datasource-auroraparameters-port
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSource.AuroraParameters"
    
    rp_Database: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Database"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-auroraparameters.html#cfn-quicksight-datasource-auroraparameters-database"""
    rp_Host: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Host"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-auroraparameters.html#cfn-quicksight-datasource-auroraparameters-host"""
    rp_Port: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "Port"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-auroraparameters.html#cfn-quicksight-datasource-auroraparameters-port"""

@attr.s
class PropDataSetRowLevelPermissionDataSet(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSet.RowLevelPermissionDataSet"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-rowlevelpermissiondataset.html

    Property Document:
    
    - ``rp_Arn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-rowlevelpermissiondataset.html#cfn-quicksight-dataset-rowlevelpermissiondataset-arn
    - ``rp_PermissionPolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-rowlevelpermissiondataset.html#cfn-quicksight-dataset-rowlevelpermissiondataset-permissionpolicy
    - ``p_FormatVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-rowlevelpermissiondataset.html#cfn-quicksight-dataset-rowlevelpermissiondataset-formatversion
    - ``p_Namespace``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-rowlevelpermissiondataset.html#cfn-quicksight-dataset-rowlevelpermissiondataset-namespace
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSet.RowLevelPermissionDataSet"
    
    rp_Arn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Arn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-rowlevelpermissiondataset.html#cfn-quicksight-dataset-rowlevelpermissiondataset-arn"""
    rp_PermissionPolicy: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PermissionPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-rowlevelpermissiondataset.html#cfn-quicksight-dataset-rowlevelpermissiondataset-permissionpolicy"""
    p_FormatVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "FormatVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-rowlevelpermissiondataset.html#cfn-quicksight-dataset-rowlevelpermissiondataset-formatversion"""
    p_Namespace: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Namespace"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-rowlevelpermissiondataset.html#cfn-quicksight-dataset-rowlevelpermissiondataset-namespace"""

@attr.s
class PropDataSourceMariaDbParameters(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSource.MariaDbParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-mariadbparameters.html

    Property Document:
    
    - ``rp_Database``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-mariadbparameters.html#cfn-quicksight-datasource-mariadbparameters-database
    - ``rp_Host``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-mariadbparameters.html#cfn-quicksight-datasource-mariadbparameters-host
    - ``rp_Port``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-mariadbparameters.html#cfn-quicksight-datasource-mariadbparameters-port
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSource.MariaDbParameters"
    
    rp_Database: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Database"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-mariadbparameters.html#cfn-quicksight-datasource-mariadbparameters-database"""
    rp_Host: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Host"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-mariadbparameters.html#cfn-quicksight-datasource-mariadbparameters-host"""
    rp_Port: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "Port"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-mariadbparameters.html#cfn-quicksight-datasource-mariadbparameters-port"""

@attr.s
class PropDashboardDataSetReference(Property):
    """
    AWS Object Type = "AWS::QuickSight::Dashboard.DataSetReference"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-datasetreference.html

    Property Document:
    
    - ``rp_DataSetArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-datasetreference.html#cfn-quicksight-dashboard-datasetreference-datasetarn
    - ``rp_DataSetPlaceholder``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-datasetreference.html#cfn-quicksight-dashboard-datasetreference-datasetplaceholder
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Dashboard.DataSetReference"
    
    rp_DataSetArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DataSetArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-datasetreference.html#cfn-quicksight-dashboard-datasetreference-datasetarn"""
    rp_DataSetPlaceholder: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DataSetPlaceholder"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-datasetreference.html#cfn-quicksight-dashboard-datasetreference-datasetplaceholder"""

@attr.s
class PropThemeTileStyle(Property):
    """
    AWS Object Type = "AWS::QuickSight::Theme.TileStyle"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-tilestyle.html

    Property Document:
    
    - ``p_Border``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-tilestyle.html#cfn-quicksight-theme-tilestyle-border
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Theme.TileStyle"
    
    p_Border: typing.Union['PropThemeBorderStyle', dict] = attr.ib(
        default=None,
        converter=PropThemeBorderStyle.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropThemeBorderStyle)),
        metadata={AttrMeta.PROPERTY_NAME: "Border"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-tilestyle.html#cfn-quicksight-theme-tilestyle-border"""

@attr.s
class PropDashboardStringParameter(Property):
    """
    AWS Object Type = "AWS::QuickSight::Dashboard.StringParameter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-stringparameter.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-stringparameter.html#cfn-quicksight-dashboard-stringparameter-name
    - ``rp_Values``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-stringparameter.html#cfn-quicksight-dashboard-stringparameter-values
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Dashboard.StringParameter"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-stringparameter.html#cfn-quicksight-dashboard-stringparameter-name"""
    rp_Values: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Values"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-stringparameter.html#cfn-quicksight-dashboard-stringparameter-values"""

@attr.s
class PropAnalysisDateTimeParameter(Property):
    """
    AWS Object Type = "AWS::QuickSight::Analysis.DateTimeParameter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-datetimeparameter.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-datetimeparameter.html#cfn-quicksight-analysis-datetimeparameter-name
    - ``rp_Values``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-datetimeparameter.html#cfn-quicksight-analysis-datetimeparameter-values
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Analysis.DateTimeParameter"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-datetimeparameter.html#cfn-quicksight-analysis-datetimeparameter-name"""
    rp_Values: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Values"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-datetimeparameter.html#cfn-quicksight-analysis-datetimeparameter-values"""

@attr.s
class PropDashboardIntegerParameter(Property):
    """
    AWS Object Type = "AWS::QuickSight::Dashboard.IntegerParameter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-integerparameter.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-integerparameter.html#cfn-quicksight-dashboard-integerparameter-name
    - ``rp_Values``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-integerparameter.html#cfn-quicksight-dashboard-integerparameter-values
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Dashboard.IntegerParameter"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-integerparameter.html#cfn-quicksight-dashboard-integerparameter-name"""
    rp_Values: typing.List[float] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(float), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Values"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-integerparameter.html#cfn-quicksight-dashboard-integerparameter-values"""

@attr.s
class PropDataSourceTeradataParameters(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSource.TeradataParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-teradataparameters.html

    Property Document:
    
    - ``rp_Database``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-teradataparameters.html#cfn-quicksight-datasource-teradataparameters-database
    - ``rp_Host``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-teradataparameters.html#cfn-quicksight-datasource-teradataparameters-host
    - ``rp_Port``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-teradataparameters.html#cfn-quicksight-datasource-teradataparameters-port
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSource.TeradataParameters"
    
    rp_Database: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Database"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-teradataparameters.html#cfn-quicksight-datasource-teradataparameters-database"""
    rp_Host: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Host"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-teradataparameters.html#cfn-quicksight-datasource-teradataparameters-host"""
    rp_Port: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "Port"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-teradataparameters.html#cfn-quicksight-datasource-teradataparameters-port"""

@attr.s
class PropThemeResourcePermission(Property):
    """
    AWS Object Type = "AWS::QuickSight::Theme.ResourcePermission"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-resourcepermission.html

    Property Document:
    
    - ``rp_Actions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-resourcepermission.html#cfn-quicksight-theme-resourcepermission-actions
    - ``rp_Principal``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-resourcepermission.html#cfn-quicksight-theme-resourcepermission-principal
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Theme.ResourcePermission"
    
    rp_Actions: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Actions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-resourcepermission.html#cfn-quicksight-theme-resourcepermission-actions"""
    rp_Principal: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Principal"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-resourcepermission.html#cfn-quicksight-theme-resourcepermission-principal"""

@attr.s
class PropTemplateTemplateSourceTemplate(Property):
    """
    AWS Object Type = "AWS::QuickSight::Template.TemplateSourceTemplate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourcetemplate.html

    Property Document:
    
    - ``rp_Arn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourcetemplate.html#cfn-quicksight-template-templatesourcetemplate-arn
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Template.TemplateSourceTemplate"
    
    rp_Arn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Arn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourcetemplate.html#cfn-quicksight-template-templatesourcetemplate-arn"""

@attr.s
class PropThemeMarginStyle(Property):
    """
    AWS Object Type = "AWS::QuickSight::Theme.MarginStyle"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-marginstyle.html

    Property Document:
    
    - ``p_Show``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-marginstyle.html#cfn-quicksight-theme-marginstyle-show
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Theme.MarginStyle"
    
    p_Show: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Show"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-marginstyle.html#cfn-quicksight-theme-marginstyle-show"""

@attr.s
class PropDashboardExportToCSVOption(Property):
    """
    AWS Object Type = "AWS::QuickSight::Dashboard.ExportToCSVOption"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-exporttocsvoption.html

    Property Document:
    
    - ``p_AvailabilityStatus``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-exporttocsvoption.html#cfn-quicksight-dashboard-exporttocsvoption-availabilitystatus
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Dashboard.ExportToCSVOption"
    
    p_AvailabilityStatus: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AvailabilityStatus"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-exporttocsvoption.html#cfn-quicksight-dashboard-exporttocsvoption-availabilitystatus"""

@attr.s
class PropDataSourceAthenaParameters(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSource.AthenaParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-athenaparameters.html

    Property Document:
    
    - ``p_WorkGroup``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-athenaparameters.html#cfn-quicksight-datasource-athenaparameters-workgroup
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSource.AthenaParameters"
    
    p_WorkGroup: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "WorkGroup"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-athenaparameters.html#cfn-quicksight-datasource-athenaparameters-workgroup"""

@attr.s
class PropThemeGutterStyle(Property):
    """
    AWS Object Type = "AWS::QuickSight::Theme.GutterStyle"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-gutterstyle.html

    Property Document:
    
    - ``p_Show``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-gutterstyle.html#cfn-quicksight-theme-gutterstyle-show
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Theme.GutterStyle"
    
    p_Show: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Show"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-gutterstyle.html#cfn-quicksight-theme-gutterstyle-show"""

@attr.s
class PropDataSourceManifestFileLocation(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSource.ManifestFileLocation"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-manifestfilelocation.html

    Property Document:
    
    - ``rp_Bucket``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-manifestfilelocation.html#cfn-quicksight-datasource-manifestfilelocation-bucket
    - ``rp_Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-manifestfilelocation.html#cfn-quicksight-datasource-manifestfilelocation-key
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSource.ManifestFileLocation"
    
    rp_Bucket: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Bucket"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-manifestfilelocation.html#cfn-quicksight-datasource-manifestfilelocation-bucket"""
    rp_Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-manifestfilelocation.html#cfn-quicksight-datasource-manifestfilelocation-key"""

@attr.s
class PropDataSetFilterOperation(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSet.FilterOperation"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-filteroperation.html

    Property Document:
    
    - ``rp_ConditionExpression``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-filteroperation.html#cfn-quicksight-dataset-filteroperation-conditionexpression
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSet.FilterOperation"
    
    rp_ConditionExpression: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ConditionExpression"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-filteroperation.html#cfn-quicksight-dataset-filteroperation-conditionexpression"""

@attr.s
class PropThemeDataColorPalette(Property):
    """
    AWS Object Type = "AWS::QuickSight::Theme.DataColorPalette"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-datacolorpalette.html

    Property Document:
    
    - ``p_Colors``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-datacolorpalette.html#cfn-quicksight-theme-datacolorpalette-colors
    - ``p_EmptyFillColor``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-datacolorpalette.html#cfn-quicksight-theme-datacolorpalette-emptyfillcolor
    - ``p_MinMaxGradient``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-datacolorpalette.html#cfn-quicksight-theme-datacolorpalette-minmaxgradient
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Theme.DataColorPalette"
    
    p_Colors: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Colors"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-datacolorpalette.html#cfn-quicksight-theme-datacolorpalette-colors"""
    p_EmptyFillColor: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "EmptyFillColor"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-datacolorpalette.html#cfn-quicksight-theme-datacolorpalette-emptyfillcolor"""
    p_MinMaxGradient: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "MinMaxGradient"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-datacolorpalette.html#cfn-quicksight-theme-datacolorpalette-minmaxgradient"""

@attr.s
class PropDataSetCustomSql(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSet.CustomSql"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-customsql.html

    Property Document:
    
    - ``rp_Columns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-customsql.html#cfn-quicksight-dataset-customsql-columns
    - ``rp_DataSourceArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-customsql.html#cfn-quicksight-dataset-customsql-datasourcearn
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-customsql.html#cfn-quicksight-dataset-customsql-name
    - ``rp_SqlQuery``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-customsql.html#cfn-quicksight-dataset-customsql-sqlquery
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSet.CustomSql"
    
    rp_Columns: typing.List[typing.Union['PropDataSetInputColumn', dict]] = attr.ib(
        default=None,
        converter=PropDataSetInputColumn.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDataSetInputColumn), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Columns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-customsql.html#cfn-quicksight-dataset-customsql-columns"""
    rp_DataSourceArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DataSourceArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-customsql.html#cfn-quicksight-dataset-customsql-datasourcearn"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-customsql.html#cfn-quicksight-dataset-customsql-name"""
    rp_SqlQuery: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SqlQuery"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-customsql.html#cfn-quicksight-dataset-customsql-sqlquery"""

@attr.s
class PropTemplateDataSetReference(Property):
    """
    AWS Object Type = "AWS::QuickSight::Template.DataSetReference"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-datasetreference.html

    Property Document:
    
    - ``rp_DataSetArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-datasetreference.html#cfn-quicksight-template-datasetreference-datasetarn
    - ``rp_DataSetPlaceholder``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-datasetreference.html#cfn-quicksight-template-datasetreference-datasetplaceholder
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Template.DataSetReference"
    
    rp_DataSetArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DataSetArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-datasetreference.html#cfn-quicksight-template-datasetreference-datasetarn"""
    rp_DataSetPlaceholder: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DataSetPlaceholder"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-datasetreference.html#cfn-quicksight-template-datasetreference-datasetplaceholder"""

@attr.s
class PropDataSourceMySqlParameters(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSource.MySqlParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-mysqlparameters.html

    Property Document:
    
    - ``rp_Database``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-mysqlparameters.html#cfn-quicksight-datasource-mysqlparameters-database
    - ``rp_Host``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-mysqlparameters.html#cfn-quicksight-datasource-mysqlparameters-host
    - ``rp_Port``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-mysqlparameters.html#cfn-quicksight-datasource-mysqlparameters-port
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSource.MySqlParameters"
    
    rp_Database: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Database"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-mysqlparameters.html#cfn-quicksight-datasource-mysqlparameters-database"""
    rp_Host: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Host"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-mysqlparameters.html#cfn-quicksight-datasource-mysqlparameters-host"""
    rp_Port: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "Port"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-mysqlparameters.html#cfn-quicksight-datasource-mysqlparameters-port"""

@attr.s
class PropAnalysisIntegerParameter(Property):
    """
    AWS Object Type = "AWS::QuickSight::Analysis.IntegerParameter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-integerparameter.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-integerparameter.html#cfn-quicksight-analysis-integerparameter-name
    - ``rp_Values``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-integerparameter.html#cfn-quicksight-analysis-integerparameter-values
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Analysis.IntegerParameter"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-integerparameter.html#cfn-quicksight-analysis-integerparameter-name"""
    rp_Values: typing.List[float] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(float), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Values"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-integerparameter.html#cfn-quicksight-analysis-integerparameter-values"""

@attr.s
class PropDataSourceOracleParameters(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSource.OracleParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-oracleparameters.html

    Property Document:
    
    - ``rp_Database``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-oracleparameters.html#cfn-quicksight-datasource-oracleparameters-database
    - ``rp_Host``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-oracleparameters.html#cfn-quicksight-datasource-oracleparameters-host
    - ``rp_Port``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-oracleparameters.html#cfn-quicksight-datasource-oracleparameters-port
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSource.OracleParameters"
    
    rp_Database: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Database"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-oracleparameters.html#cfn-quicksight-datasource-oracleparameters-database"""
    rp_Host: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Host"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-oracleparameters.html#cfn-quicksight-datasource-oracleparameters-host"""
    rp_Port: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "Port"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-oracleparameters.html#cfn-quicksight-datasource-oracleparameters-port"""

@attr.s
class PropDashboardDecimalParameter(Property):
    """
    AWS Object Type = "AWS::QuickSight::Dashboard.DecimalParameter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-decimalparameter.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-decimalparameter.html#cfn-quicksight-dashboard-decimalparameter-name
    - ``rp_Values``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-decimalparameter.html#cfn-quicksight-dashboard-decimalparameter-values
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Dashboard.DecimalParameter"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-decimalparameter.html#cfn-quicksight-dashboard-decimalparameter-name"""
    rp_Values: typing.List[float] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(float), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Values"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-decimalparameter.html#cfn-quicksight-dashboard-decimalparameter-values"""

@attr.s
class PropDataSourceAmazonElasticsearchParameters(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSource.AmazonElasticsearchParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-amazonelasticsearchparameters.html

    Property Document:
    
    - ``rp_Domain``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-amazonelasticsearchparameters.html#cfn-quicksight-datasource-amazonelasticsearchparameters-domain
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSource.AmazonElasticsearchParameters"
    
    rp_Domain: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Domain"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-amazonelasticsearchparameters.html#cfn-quicksight-datasource-amazonelasticsearchparameters-domain"""

@attr.s
class PropAnalysisStringParameter(Property):
    """
    AWS Object Type = "AWS::QuickSight::Analysis.StringParameter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-stringparameter.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-stringparameter.html#cfn-quicksight-analysis-stringparameter-name
    - ``rp_Values``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-stringparameter.html#cfn-quicksight-analysis-stringparameter-values
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Analysis.StringParameter"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-stringparameter.html#cfn-quicksight-analysis-stringparameter-name"""
    rp_Values: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Values"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-stringparameter.html#cfn-quicksight-analysis-stringparameter-values"""

@attr.s
class PropDataSetResourcePermission(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSet.ResourcePermission"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-resourcepermission.html

    Property Document:
    
    - ``rp_Actions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-resourcepermission.html#cfn-quicksight-dataset-resourcepermission-actions
    - ``rp_Principal``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-resourcepermission.html#cfn-quicksight-dataset-resourcepermission-principal
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSet.ResourcePermission"
    
    rp_Actions: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Actions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-resourcepermission.html#cfn-quicksight-dataset-resourcepermission-actions"""
    rp_Principal: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Principal"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-resourcepermission.html#cfn-quicksight-dataset-resourcepermission-principal"""

@attr.s
class PropDataSetFieldFolder(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSet.FieldFolder"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-fieldfolder.html

    Property Document:
    
    - ``p_Columns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-fieldfolder.html#cfn-quicksight-dataset-fieldfolder-columns
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-fieldfolder.html#cfn-quicksight-dataset-fieldfolder-description
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSet.FieldFolder"
    
    p_Columns: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Columns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-fieldfolder.html#cfn-quicksight-dataset-fieldfolder-columns"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-fieldfolder.html#cfn-quicksight-dataset-fieldfolder-description"""

@attr.s
class PropDataSetS3Source(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSet.S3Source"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-s3source.html

    Property Document:
    
    - ``rp_DataSourceArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-s3source.html#cfn-quicksight-dataset-s3source-datasourcearn
    - ``rp_InputColumns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-s3source.html#cfn-quicksight-dataset-s3source-inputcolumns
    - ``p_UploadSettings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-s3source.html#cfn-quicksight-dataset-s3source-uploadsettings
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSet.S3Source"
    
    rp_DataSourceArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DataSourceArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-s3source.html#cfn-quicksight-dataset-s3source-datasourcearn"""
    rp_InputColumns: typing.List[typing.Union['PropDataSetInputColumn', dict]] = attr.ib(
        default=None,
        converter=PropDataSetInputColumn.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDataSetInputColumn), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "InputColumns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-s3source.html#cfn-quicksight-dataset-s3source-inputcolumns"""
    p_UploadSettings: typing.Union['PropDataSetUploadSettings', dict] = attr.ib(
        default=None,
        converter=PropDataSetUploadSettings.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSetUploadSettings)),
        metadata={AttrMeta.PROPERTY_NAME: "UploadSettings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-s3source.html#cfn-quicksight-dataset-s3source-uploadsettings"""

@attr.s
class PropDataSourceDataSourceErrorInfo(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSource.DataSourceErrorInfo"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceerrorinfo.html

    Property Document:
    
    - ``p_Message``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceerrorinfo.html#cfn-quicksight-datasource-datasourceerrorinfo-message
    - ``p_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceerrorinfo.html#cfn-quicksight-datasource-datasourceerrorinfo-type
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSource.DataSourceErrorInfo"
    
    p_Message: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Message"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceerrorinfo.html#cfn-quicksight-datasource-datasourceerrorinfo-message"""
    p_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceerrorinfo.html#cfn-quicksight-datasource-datasourceerrorinfo-type"""

@attr.s
class PropDataSourceVpcConnectionProperties(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSource.VpcConnectionProperties"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-vpcconnectionproperties.html

    Property Document:
    
    - ``rp_VpcConnectionArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-vpcconnectionproperties.html#cfn-quicksight-datasource-vpcconnectionproperties-vpcconnectionarn
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSource.VpcConnectionProperties"
    
    rp_VpcConnectionArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "VpcConnectionArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-vpcconnectionproperties.html#cfn-quicksight-datasource-vpcconnectionproperties-vpcconnectionarn"""

@attr.s
class PropDataSourceRedshiftParameters(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSource.RedshiftParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-redshiftparameters.html

    Property Document:
    
    - ``rp_Database``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-redshiftparameters.html#cfn-quicksight-datasource-redshiftparameters-database
    - ``p_ClusterId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-redshiftparameters.html#cfn-quicksight-datasource-redshiftparameters-clusterid
    - ``p_Host``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-redshiftparameters.html#cfn-quicksight-datasource-redshiftparameters-host
    - ``p_Port``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-redshiftparameters.html#cfn-quicksight-datasource-redshiftparameters-port
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSource.RedshiftParameters"
    
    rp_Database: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Database"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-redshiftparameters.html#cfn-quicksight-datasource-redshiftparameters-database"""
    p_ClusterId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ClusterId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-redshiftparameters.html#cfn-quicksight-datasource-redshiftparameters-clusterid"""
    p_Host: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Host"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-redshiftparameters.html#cfn-quicksight-datasource-redshiftparameters-host"""
    p_Port: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "Port"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-redshiftparameters.html#cfn-quicksight-datasource-redshiftparameters-port"""

@attr.s
class PropAnalysisAnalysisError(Property):
    """
    AWS Object Type = "AWS::QuickSight::Analysis.AnalysisError"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysiserror.html

    Property Document:
    
    - ``p_Message``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysiserror.html#cfn-quicksight-analysis-analysiserror-message
    - ``p_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysiserror.html#cfn-quicksight-analysis-analysiserror-type
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Analysis.AnalysisError"
    
    p_Message: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Message"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysiserror.html#cfn-quicksight-analysis-analysiserror-message"""
    p_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysiserror.html#cfn-quicksight-analysis-analysiserror-type"""

@attr.s
class PropDashboardDateTimeParameter(Property):
    """
    AWS Object Type = "AWS::QuickSight::Dashboard.DateTimeParameter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-datetimeparameter.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-datetimeparameter.html#cfn-quicksight-dashboard-datetimeparameter-name
    - ``rp_Values``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-datetimeparameter.html#cfn-quicksight-dashboard-datetimeparameter-values
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Dashboard.DateTimeParameter"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-datetimeparameter.html#cfn-quicksight-dashboard-datetimeparameter-name"""
    rp_Values: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Values"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-datetimeparameter.html#cfn-quicksight-dashboard-datetimeparameter-values"""

@attr.s
class PropThemeUIColorPalette(Property):
    """
    AWS Object Type = "AWS::QuickSight::Theme.UIColorPalette"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html

    Property Document:
    
    - ``p_Accent``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-accent
    - ``p_AccentForeground``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-accentforeground
    - ``p_Danger``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-danger
    - ``p_DangerForeground``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-dangerforeground
    - ``p_Dimension``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-dimension
    - ``p_DimensionForeground``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-dimensionforeground
    - ``p_Measure``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-measure
    - ``p_MeasureForeground``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-measureforeground
    - ``p_PrimaryBackground``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-primarybackground
    - ``p_PrimaryForeground``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-primaryforeground
    - ``p_SecondaryBackground``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-secondarybackground
    - ``p_SecondaryForeground``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-secondaryforeground
    - ``p_Success``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-success
    - ``p_SuccessForeground``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-successforeground
    - ``p_Warning``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-warning
    - ``p_WarningForeground``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-warningforeground
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Theme.UIColorPalette"
    
    p_Accent: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Accent"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-accent"""
    p_AccentForeground: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AccentForeground"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-accentforeground"""
    p_Danger: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Danger"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-danger"""
    p_DangerForeground: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DangerForeground"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-dangerforeground"""
    p_Dimension: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Dimension"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-dimension"""
    p_DimensionForeground: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DimensionForeground"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-dimensionforeground"""
    p_Measure: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Measure"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-measure"""
    p_MeasureForeground: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MeasureForeground"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-measureforeground"""
    p_PrimaryBackground: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PrimaryBackground"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-primarybackground"""
    p_PrimaryForeground: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PrimaryForeground"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-primaryforeground"""
    p_SecondaryBackground: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SecondaryBackground"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-secondarybackground"""
    p_SecondaryForeground: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SecondaryForeground"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-secondaryforeground"""
    p_Success: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Success"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-success"""
    p_SuccessForeground: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SuccessForeground"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-successforeground"""
    p_Warning: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Warning"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-warning"""
    p_WarningForeground: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "WarningForeground"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html#cfn-quicksight-theme-uicolorpalette-warningforeground"""

@attr.s
class PropDataSetJoinInstruction(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSet.JoinInstruction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-joininstruction.html

    Property Document:
    
    - ``rp_LeftOperand``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-joininstruction.html#cfn-quicksight-dataset-joininstruction-leftoperand
    - ``rp_OnClause``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-joininstruction.html#cfn-quicksight-dataset-joininstruction-onclause
    - ``rp_RightOperand``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-joininstruction.html#cfn-quicksight-dataset-joininstruction-rightoperand
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-joininstruction.html#cfn-quicksight-dataset-joininstruction-type
    - ``p_LeftJoinKeyProperties``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-joininstruction.html#cfn-quicksight-dataset-joininstruction-leftjoinkeyproperties
    - ``p_RightJoinKeyProperties``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-joininstruction.html#cfn-quicksight-dataset-joininstruction-rightjoinkeyproperties
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSet.JoinInstruction"
    
    rp_LeftOperand: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "LeftOperand"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-joininstruction.html#cfn-quicksight-dataset-joininstruction-leftoperand"""
    rp_OnClause: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "OnClause"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-joininstruction.html#cfn-quicksight-dataset-joininstruction-onclause"""
    rp_RightOperand: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RightOperand"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-joininstruction.html#cfn-quicksight-dataset-joininstruction-rightoperand"""
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-joininstruction.html#cfn-quicksight-dataset-joininstruction-type"""
    p_LeftJoinKeyProperties: typing.Union['PropDataSetJoinKeyProperties', dict] = attr.ib(
        default=None,
        converter=PropDataSetJoinKeyProperties.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSetJoinKeyProperties)),
        metadata={AttrMeta.PROPERTY_NAME: "LeftJoinKeyProperties"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-joininstruction.html#cfn-quicksight-dataset-joininstruction-leftjoinkeyproperties"""
    p_RightJoinKeyProperties: typing.Union['PropDataSetJoinKeyProperties', dict] = attr.ib(
        default=None,
        converter=PropDataSetJoinKeyProperties.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSetJoinKeyProperties)),
        metadata={AttrMeta.PROPERTY_NAME: "RightJoinKeyProperties"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-joininstruction.html#cfn-quicksight-dataset-joininstruction-rightjoinkeyproperties"""

@attr.s
class PropDataSetOutputColumn(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSet.OutputColumn"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-outputcolumn.html

    Property Document:
    
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-outputcolumn.html#cfn-quicksight-dataset-outputcolumn-description
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-outputcolumn.html#cfn-quicksight-dataset-outputcolumn-name
    - ``p_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-outputcolumn.html#cfn-quicksight-dataset-outputcolumn-type
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSet.OutputColumn"
    
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-outputcolumn.html#cfn-quicksight-dataset-outputcolumn-description"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-outputcolumn.html#cfn-quicksight-dataset-outputcolumn-name"""
    p_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-outputcolumn.html#cfn-quicksight-dataset-outputcolumn-type"""

@attr.s
class PropDataSetColumnTag(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSet.ColumnTag"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-columntag.html

    Property Document:
    
    - ``p_ColumnDescription``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-columntag.html#cfn-quicksight-dataset-columntag-columndescription
    - ``p_ColumnGeographicRole``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-columntag.html#cfn-quicksight-dataset-columntag-columngeographicrole
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSet.ColumnTag"
    
    p_ColumnDescription: typing.Union['PropDataSetColumnDescription', dict] = attr.ib(
        default=None,
        converter=PropDataSetColumnDescription.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSetColumnDescription)),
        metadata={AttrMeta.PROPERTY_NAME: "ColumnDescription"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-columntag.html#cfn-quicksight-dataset-columntag-columndescription"""
    p_ColumnGeographicRole: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ColumnGeographicRole"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-columntag.html#cfn-quicksight-dataset-columntag-columngeographicrole"""

@attr.s
class PropDataSetTagColumnOperation(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSet.TagColumnOperation"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-tagcolumnoperation.html

    Property Document:
    
    - ``rp_ColumnName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-tagcolumnoperation.html#cfn-quicksight-dataset-tagcolumnoperation-columnname
    - ``rp_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-tagcolumnoperation.html#cfn-quicksight-dataset-tagcolumnoperation-tags
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSet.TagColumnOperation"
    
    rp_ColumnName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ColumnName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-tagcolumnoperation.html#cfn-quicksight-dataset-tagcolumnoperation-columnname"""
    rp_Tags: typing.List[typing.Union['PropDataSetColumnTag', dict]] = attr.ib(
        default=None,
        converter=PropDataSetColumnTag.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDataSetColumnTag), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-tagcolumnoperation.html#cfn-quicksight-dataset-tagcolumnoperation-tags"""

@attr.s
class PropThemeTileLayoutStyle(Property):
    """
    AWS Object Type = "AWS::QuickSight::Theme.TileLayoutStyle"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-tilelayoutstyle.html

    Property Document:
    
    - ``p_Gutter``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-tilelayoutstyle.html#cfn-quicksight-theme-tilelayoutstyle-gutter
    - ``p_Margin``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-tilelayoutstyle.html#cfn-quicksight-theme-tilelayoutstyle-margin
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Theme.TileLayoutStyle"
    
    p_Gutter: typing.Union['PropThemeGutterStyle', dict] = attr.ib(
        default=None,
        converter=PropThemeGutterStyle.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropThemeGutterStyle)),
        metadata={AttrMeta.PROPERTY_NAME: "Gutter"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-tilelayoutstyle.html#cfn-quicksight-theme-tilelayoutstyle-gutter"""
    p_Margin: typing.Union['PropThemeMarginStyle', dict] = attr.ib(
        default=None,
        converter=PropThemeMarginStyle.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropThemeMarginStyle)),
        metadata={AttrMeta.PROPERTY_NAME: "Margin"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-tilelayoutstyle.html#cfn-quicksight-theme-tilelayoutstyle-margin"""

@attr.s
class PropDataSourcePostgreSqlParameters(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSource.PostgreSqlParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-postgresqlparameters.html

    Property Document:
    
    - ``rp_Database``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-postgresqlparameters.html#cfn-quicksight-datasource-postgresqlparameters-database
    - ``rp_Host``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-postgresqlparameters.html#cfn-quicksight-datasource-postgresqlparameters-host
    - ``rp_Port``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-postgresqlparameters.html#cfn-quicksight-datasource-postgresqlparameters-port
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSource.PostgreSqlParameters"
    
    rp_Database: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Database"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-postgresqlparameters.html#cfn-quicksight-datasource-postgresqlparameters-database"""
    rp_Host: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Host"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-postgresqlparameters.html#cfn-quicksight-datasource-postgresqlparameters-host"""
    rp_Port: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "Port"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-postgresqlparameters.html#cfn-quicksight-datasource-postgresqlparameters-port"""

@attr.s
class PropDataSourceRdsParameters(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSource.RdsParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-rdsparameters.html

    Property Document:
    
    - ``rp_Database``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-rdsparameters.html#cfn-quicksight-datasource-rdsparameters-database
    - ``rp_InstanceId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-rdsparameters.html#cfn-quicksight-datasource-rdsparameters-instanceid
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSource.RdsParameters"
    
    rp_Database: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Database"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-rdsparameters.html#cfn-quicksight-datasource-rdsparameters-database"""
    rp_InstanceId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "InstanceId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-rdsparameters.html#cfn-quicksight-datasource-rdsparameters-instanceid"""

@attr.s
class PropDashboardAdHocFilteringOption(Property):
    """
    AWS Object Type = "AWS::QuickSight::Dashboard.AdHocFilteringOption"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-adhocfilteringoption.html

    Property Document:
    
    - ``p_AvailabilityStatus``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-adhocfilteringoption.html#cfn-quicksight-dashboard-adhocfilteringoption-availabilitystatus
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Dashboard.AdHocFilteringOption"
    
    p_AvailabilityStatus: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AvailabilityStatus"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-adhocfilteringoption.html#cfn-quicksight-dashboard-adhocfilteringoption-availabilitystatus"""

@attr.s
class PropThemeTypography(Property):
    """
    AWS Object Type = "AWS::QuickSight::Theme.Typography"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-typography.html

    Property Document:
    
    - ``p_FontFamilies``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-typography.html#cfn-quicksight-theme-typography-fontfamilies
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Theme.Typography"
    
    p_FontFamilies: typing.List[typing.Union['PropThemeFont', dict]] = attr.ib(
        default=None,
        converter=PropThemeFont.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropThemeFont), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "FontFamilies"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-typography.html#cfn-quicksight-theme-typography-fontfamilies"""

@attr.s
class PropDataSetIngestionWaitPolicy(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSet.IngestionWaitPolicy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-ingestionwaitpolicy.html

    Property Document:
    
    - ``p_IngestionWaitTimeInHours``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-ingestionwaitpolicy.html#cfn-quicksight-dataset-ingestionwaitpolicy-ingestionwaittimeinhours
    - ``p_WaitForSpiceIngestion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-ingestionwaitpolicy.html#cfn-quicksight-dataset-ingestionwaitpolicy-waitforspiceingestion
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSet.IngestionWaitPolicy"
    
    p_IngestionWaitTimeInHours: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "IngestionWaitTimeInHours"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-ingestionwaitpolicy.html#cfn-quicksight-dataset-ingestionwaitpolicy-ingestionwaittimeinhours"""
    p_WaitForSpiceIngestion: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "WaitForSpiceIngestion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-ingestionwaitpolicy.html#cfn-quicksight-dataset-ingestionwaitpolicy-waitforspiceingestion"""

@attr.s
class PropDataSetCalculatedColumn(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSet.CalculatedColumn"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-calculatedcolumn.html

    Property Document:
    
    - ``rp_ColumnId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-calculatedcolumn.html#cfn-quicksight-dataset-calculatedcolumn-columnid
    - ``rp_ColumnName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-calculatedcolumn.html#cfn-quicksight-dataset-calculatedcolumn-columnname
    - ``rp_Expression``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-calculatedcolumn.html#cfn-quicksight-dataset-calculatedcolumn-expression
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSet.CalculatedColumn"
    
    rp_ColumnId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ColumnId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-calculatedcolumn.html#cfn-quicksight-dataset-calculatedcolumn-columnid"""
    rp_ColumnName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ColumnName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-calculatedcolumn.html#cfn-quicksight-dataset-calculatedcolumn-columnname"""
    rp_Expression: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Expression"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-calculatedcolumn.html#cfn-quicksight-dataset-calculatedcolumn-expression"""

@attr.s
class PropDataSetCastColumnTypeOperation(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSet.CastColumnTypeOperation"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-castcolumntypeoperation.html

    Property Document:
    
    - ``rp_ColumnName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-castcolumntypeoperation.html#cfn-quicksight-dataset-castcolumntypeoperation-columnname
    - ``rp_NewColumnType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-castcolumntypeoperation.html#cfn-quicksight-dataset-castcolumntypeoperation-newcolumntype
    - ``p_Format``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-castcolumntypeoperation.html#cfn-quicksight-dataset-castcolumntypeoperation-format
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSet.CastColumnTypeOperation"
    
    rp_ColumnName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ColumnName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-castcolumntypeoperation.html#cfn-quicksight-dataset-castcolumntypeoperation-columnname"""
    rp_NewColumnType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "NewColumnType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-castcolumntypeoperation.html#cfn-quicksight-dataset-castcolumntypeoperation-newcolumntype"""
    p_Format: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Format"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-castcolumntypeoperation.html#cfn-quicksight-dataset-castcolumntypeoperation-format"""

@attr.s
class PropDataSetLogicalTableSource(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSet.LogicalTableSource"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-logicaltablesource.html

    Property Document:
    
    - ``p_JoinInstruction``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-logicaltablesource.html#cfn-quicksight-dataset-logicaltablesource-joininstruction
    - ``p_PhysicalTableId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-logicaltablesource.html#cfn-quicksight-dataset-logicaltablesource-physicaltableid
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSet.LogicalTableSource"
    
    p_JoinInstruction: typing.Union['PropDataSetJoinInstruction', dict] = attr.ib(
        default=None,
        converter=PropDataSetJoinInstruction.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSetJoinInstruction)),
        metadata={AttrMeta.PROPERTY_NAME: "JoinInstruction"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-logicaltablesource.html#cfn-quicksight-dataset-logicaltablesource-joininstruction"""
    p_PhysicalTableId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PhysicalTableId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-logicaltablesource.html#cfn-quicksight-dataset-logicaltablesource-physicaltableid"""

@attr.s
class PropDataSourceSqlServerParameters(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSource.SqlServerParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-sqlserverparameters.html

    Property Document:
    
    - ``rp_Database``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-sqlserverparameters.html#cfn-quicksight-datasource-sqlserverparameters-database
    - ``rp_Host``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-sqlserverparameters.html#cfn-quicksight-datasource-sqlserverparameters-host
    - ``rp_Port``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-sqlserverparameters.html#cfn-quicksight-datasource-sqlserverparameters-port
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSource.SqlServerParameters"
    
    rp_Database: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Database"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-sqlserverparameters.html#cfn-quicksight-datasource-sqlserverparameters-database"""
    rp_Host: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Host"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-sqlserverparameters.html#cfn-quicksight-datasource-sqlserverparameters-host"""
    rp_Port: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "Port"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-sqlserverparameters.html#cfn-quicksight-datasource-sqlserverparameters-port"""

@attr.s
class PropTemplateTemplateSourceAnalysis(Property):
    """
    AWS Object Type = "AWS::QuickSight::Template.TemplateSourceAnalysis"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourceanalysis.html

    Property Document:
    
    - ``rp_Arn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourceanalysis.html#cfn-quicksight-template-templatesourceanalysis-arn
    - ``rp_DataSetReferences``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourceanalysis.html#cfn-quicksight-template-templatesourceanalysis-datasetreferences
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Template.TemplateSourceAnalysis"
    
    rp_Arn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Arn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourceanalysis.html#cfn-quicksight-template-templatesourceanalysis-arn"""
    rp_DataSetReferences: typing.List[typing.Union['PropTemplateDataSetReference', dict]] = attr.ib(
        default=None,
        converter=PropTemplateDataSetReference.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTemplateDataSetReference), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "DataSetReferences"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourceanalysis.html#cfn-quicksight-template-templatesourceanalysis-datasetreferences"""

@attr.s
class PropDataSetCreateColumnsOperation(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSet.CreateColumnsOperation"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-createcolumnsoperation.html

    Property Document:
    
    - ``rp_Columns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-createcolumnsoperation.html#cfn-quicksight-dataset-createcolumnsoperation-columns
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSet.CreateColumnsOperation"
    
    rp_Columns: typing.List[typing.Union['PropDataSetCalculatedColumn', dict]] = attr.ib(
        default=None,
        converter=PropDataSetCalculatedColumn.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDataSetCalculatedColumn), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Columns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-createcolumnsoperation.html#cfn-quicksight-dataset-createcolumnsoperation-columns"""

@attr.s
class PropAnalysisAnalysisSourceTemplate(Property):
    """
    AWS Object Type = "AWS::QuickSight::Analysis.AnalysisSourceTemplate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysissourcetemplate.html

    Property Document:
    
    - ``rp_Arn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysissourcetemplate.html#cfn-quicksight-analysis-analysissourcetemplate-arn
    - ``rp_DataSetReferences``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysissourcetemplate.html#cfn-quicksight-analysis-analysissourcetemplate-datasetreferences
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Analysis.AnalysisSourceTemplate"
    
    rp_Arn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Arn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysissourcetemplate.html#cfn-quicksight-analysis-analysissourcetemplate-arn"""
    rp_DataSetReferences: typing.List[typing.Union['PropAnalysisDataSetReference', dict]] = attr.ib(
        default=None,
        converter=PropAnalysisDataSetReference.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropAnalysisDataSetReference), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "DataSetReferences"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysissourcetemplate.html#cfn-quicksight-analysis-analysissourcetemplate-datasetreferences"""

@attr.s
class PropDataSourceS3Parameters(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSource.S3Parameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-s3parameters.html

    Property Document:
    
    - ``rp_ManifestFileLocation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-s3parameters.html#cfn-quicksight-datasource-s3parameters-manifestfilelocation
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSource.S3Parameters"
    
    rp_ManifestFileLocation: typing.Union['PropDataSourceManifestFileLocation', dict] = attr.ib(
        default=None,
        converter=PropDataSourceManifestFileLocation.from_dict,
        validator=attr.validators.instance_of(PropDataSourceManifestFileLocation),
        metadata={AttrMeta.PROPERTY_NAME: "ManifestFileLocation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-s3parameters.html#cfn-quicksight-datasource-s3parameters-manifestfilelocation"""

@attr.s
class PropAnalysisAnalysisSourceEntity(Property):
    """
    AWS Object Type = "AWS::QuickSight::Analysis.AnalysisSourceEntity"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysissourceentity.html

    Property Document:
    
    - ``p_SourceTemplate``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysissourceentity.html#cfn-quicksight-analysis-analysissourceentity-sourcetemplate
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Analysis.AnalysisSourceEntity"
    
    p_SourceTemplate: typing.Union['PropAnalysisAnalysisSourceTemplate', dict] = attr.ib(
        default=None,
        converter=PropAnalysisAnalysisSourceTemplate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropAnalysisAnalysisSourceTemplate)),
        metadata={AttrMeta.PROPERTY_NAME: "SourceTemplate"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysissourceentity.html#cfn-quicksight-analysis-analysissourceentity-sourcetemplate"""

@attr.s
class PropDashboardParameters(Property):
    """
    AWS Object Type = "AWS::QuickSight::Dashboard.Parameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-parameters.html

    Property Document:
    
    - ``p_DateTimeParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-parameters.html#cfn-quicksight-dashboard-parameters-datetimeparameters
    - ``p_DecimalParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-parameters.html#cfn-quicksight-dashboard-parameters-decimalparameters
    - ``p_IntegerParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-parameters.html#cfn-quicksight-dashboard-parameters-integerparameters
    - ``p_StringParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-parameters.html#cfn-quicksight-dashboard-parameters-stringparameters
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Dashboard.Parameters"
    
    p_DateTimeParameters: typing.List[typing.Union['PropDashboardDateTimeParameter', dict]] = attr.ib(
        default=None,
        converter=PropDashboardDateTimeParameter.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDashboardDateTimeParameter), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "DateTimeParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-parameters.html#cfn-quicksight-dashboard-parameters-datetimeparameters"""
    p_DecimalParameters: typing.List[typing.Union['PropDashboardDecimalParameter', dict]] = attr.ib(
        default=None,
        converter=PropDashboardDecimalParameter.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDashboardDecimalParameter), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "DecimalParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-parameters.html#cfn-quicksight-dashboard-parameters-decimalparameters"""
    p_IntegerParameters: typing.List[typing.Union['PropDashboardIntegerParameter', dict]] = attr.ib(
        default=None,
        converter=PropDashboardIntegerParameter.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDashboardIntegerParameter), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "IntegerParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-parameters.html#cfn-quicksight-dashboard-parameters-integerparameters"""
    p_StringParameters: typing.List[typing.Union['PropDashboardStringParameter', dict]] = attr.ib(
        default=None,
        converter=PropDashboardStringParameter.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDashboardStringParameter), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "StringParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-parameters.html#cfn-quicksight-dashboard-parameters-stringparameters"""

@attr.s
class PropDataSetColumnGroup(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSet.ColumnGroup"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-columngroup.html

    Property Document:
    
    - ``p_GeoSpatialColumnGroup``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-columngroup.html#cfn-quicksight-dataset-columngroup-geospatialcolumngroup
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSet.ColumnGroup"
    
    p_GeoSpatialColumnGroup: typing.Union['PropDataSetGeoSpatialColumnGroup', dict] = attr.ib(
        default=None,
        converter=PropDataSetGeoSpatialColumnGroup.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSetGeoSpatialColumnGroup)),
        metadata={AttrMeta.PROPERTY_NAME: "GeoSpatialColumnGroup"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-columngroup.html#cfn-quicksight-dataset-columngroup-geospatialcolumngroup"""

@attr.s
class PropDashboardDashboardSourceTemplate(Property):
    """
    AWS Object Type = "AWS::QuickSight::Dashboard.DashboardSourceTemplate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardsourcetemplate.html

    Property Document:
    
    - ``rp_Arn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardsourcetemplate.html#cfn-quicksight-dashboard-dashboardsourcetemplate-arn
    - ``rp_DataSetReferences``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardsourcetemplate.html#cfn-quicksight-dashboard-dashboardsourcetemplate-datasetreferences
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Dashboard.DashboardSourceTemplate"
    
    rp_Arn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Arn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardsourcetemplate.html#cfn-quicksight-dashboard-dashboardsourcetemplate-arn"""
    rp_DataSetReferences: typing.List[typing.Union['PropDashboardDataSetReference', dict]] = attr.ib(
        default=None,
        converter=PropDashboardDataSetReference.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDashboardDataSetReference), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "DataSetReferences"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardsourcetemplate.html#cfn-quicksight-dashboard-dashboardsourcetemplate-datasetreferences"""

@attr.s
class PropDataSetRelationalTable(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSet.RelationalTable"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-relationaltable.html

    Property Document:
    
    - ``rp_DataSourceArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-relationaltable.html#cfn-quicksight-dataset-relationaltable-datasourcearn
    - ``rp_InputColumns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-relationaltable.html#cfn-quicksight-dataset-relationaltable-inputcolumns
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-relationaltable.html#cfn-quicksight-dataset-relationaltable-name
    - ``p_Catalog``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-relationaltable.html#cfn-quicksight-dataset-relationaltable-catalog
    - ``p_Schema``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-relationaltable.html#cfn-quicksight-dataset-relationaltable-schema
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSet.RelationalTable"
    
    rp_DataSourceArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DataSourceArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-relationaltable.html#cfn-quicksight-dataset-relationaltable-datasourcearn"""
    rp_InputColumns: typing.List[typing.Union['PropDataSetInputColumn', dict]] = attr.ib(
        default=None,
        converter=PropDataSetInputColumn.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDataSetInputColumn), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "InputColumns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-relationaltable.html#cfn-quicksight-dataset-relationaltable-inputcolumns"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-relationaltable.html#cfn-quicksight-dataset-relationaltable-name"""
    p_Catalog: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Catalog"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-relationaltable.html#cfn-quicksight-dataset-relationaltable-catalog"""
    p_Schema: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Schema"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-relationaltable.html#cfn-quicksight-dataset-relationaltable-schema"""

@attr.s
class PropDashboardDashboardPublishOptions(Property):
    """
    AWS Object Type = "AWS::QuickSight::Dashboard.DashboardPublishOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardpublishoptions.html

    Property Document:
    
    - ``p_AdHocFilteringOption``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardpublishoptions.html#cfn-quicksight-dashboard-dashboardpublishoptions-adhocfilteringoption
    - ``p_ExportToCSVOption``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardpublishoptions.html#cfn-quicksight-dashboard-dashboardpublishoptions-exporttocsvoption
    - ``p_SheetControlsOption``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardpublishoptions.html#cfn-quicksight-dashboard-dashboardpublishoptions-sheetcontrolsoption
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Dashboard.DashboardPublishOptions"
    
    p_AdHocFilteringOption: typing.Union['PropDashboardAdHocFilteringOption', dict] = attr.ib(
        default=None,
        converter=PropDashboardAdHocFilteringOption.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDashboardAdHocFilteringOption)),
        metadata={AttrMeta.PROPERTY_NAME: "AdHocFilteringOption"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardpublishoptions.html#cfn-quicksight-dashboard-dashboardpublishoptions-adhocfilteringoption"""
    p_ExportToCSVOption: typing.Union['PropDashboardExportToCSVOption', dict] = attr.ib(
        default=None,
        converter=PropDashboardExportToCSVOption.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDashboardExportToCSVOption)),
        metadata={AttrMeta.PROPERTY_NAME: "ExportToCSVOption"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardpublishoptions.html#cfn-quicksight-dashboard-dashboardpublishoptions-exporttocsvoption"""
    p_SheetControlsOption: typing.Union['PropDashboardSheetControlsOption', dict] = attr.ib(
        default=None,
        converter=PropDashboardSheetControlsOption.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDashboardSheetControlsOption)),
        metadata={AttrMeta.PROPERTY_NAME: "SheetControlsOption"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardpublishoptions.html#cfn-quicksight-dashboard-dashboardpublishoptions-sheetcontrolsoption"""

@attr.s
class PropAnalysisParameters(Property):
    """
    AWS Object Type = "AWS::QuickSight::Analysis.Parameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-parameters.html

    Property Document:
    
    - ``p_DateTimeParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-parameters.html#cfn-quicksight-analysis-parameters-datetimeparameters
    - ``p_DecimalParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-parameters.html#cfn-quicksight-analysis-parameters-decimalparameters
    - ``p_IntegerParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-parameters.html#cfn-quicksight-analysis-parameters-integerparameters
    - ``p_StringParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-parameters.html#cfn-quicksight-analysis-parameters-stringparameters
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Analysis.Parameters"
    
    p_DateTimeParameters: typing.List[typing.Union['PropAnalysisDateTimeParameter', dict]] = attr.ib(
        default=None,
        converter=PropAnalysisDateTimeParameter.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropAnalysisDateTimeParameter), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "DateTimeParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-parameters.html#cfn-quicksight-analysis-parameters-datetimeparameters"""
    p_DecimalParameters: typing.List[typing.Union['PropAnalysisDecimalParameter', dict]] = attr.ib(
        default=None,
        converter=PropAnalysisDecimalParameter.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropAnalysisDecimalParameter), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "DecimalParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-parameters.html#cfn-quicksight-analysis-parameters-decimalparameters"""
    p_IntegerParameters: typing.List[typing.Union['PropAnalysisIntegerParameter', dict]] = attr.ib(
        default=None,
        converter=PropAnalysisIntegerParameter.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropAnalysisIntegerParameter), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "IntegerParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-parameters.html#cfn-quicksight-analysis-parameters-integerparameters"""
    p_StringParameters: typing.List[typing.Union['PropAnalysisStringParameter', dict]] = attr.ib(
        default=None,
        converter=PropAnalysisStringParameter.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropAnalysisStringParameter), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "StringParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-parameters.html#cfn-quicksight-analysis-parameters-stringparameters"""

@attr.s
class PropTemplateTemplateSourceEntity(Property):
    """
    AWS Object Type = "AWS::QuickSight::Template.TemplateSourceEntity"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourceentity.html

    Property Document:
    
    - ``p_SourceAnalysis``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourceentity.html#cfn-quicksight-template-templatesourceentity-sourceanalysis
    - ``p_SourceTemplate``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourceentity.html#cfn-quicksight-template-templatesourceentity-sourcetemplate
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Template.TemplateSourceEntity"
    
    p_SourceAnalysis: typing.Union['PropTemplateTemplateSourceAnalysis', dict] = attr.ib(
        default=None,
        converter=PropTemplateTemplateSourceAnalysis.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTemplateTemplateSourceAnalysis)),
        metadata={AttrMeta.PROPERTY_NAME: "SourceAnalysis"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourceentity.html#cfn-quicksight-template-templatesourceentity-sourceanalysis"""
    p_SourceTemplate: typing.Union['PropTemplateTemplateSourceTemplate', dict] = attr.ib(
        default=None,
        converter=PropTemplateTemplateSourceTemplate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTemplateTemplateSourceTemplate)),
        metadata={AttrMeta.PROPERTY_NAME: "SourceTemplate"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourceentity.html#cfn-quicksight-template-templatesourceentity-sourcetemplate"""

@attr.s
class PropDataSetTransformOperation(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSet.TransformOperation"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-transformoperation.html

    Property Document:
    
    - ``p_CastColumnTypeOperation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-transformoperation.html#cfn-quicksight-dataset-transformoperation-castcolumntypeoperation
    - ``p_CreateColumnsOperation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-transformoperation.html#cfn-quicksight-dataset-transformoperation-createcolumnsoperation
    - ``p_FilterOperation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-transformoperation.html#cfn-quicksight-dataset-transformoperation-filteroperation
    - ``p_ProjectOperation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-transformoperation.html#cfn-quicksight-dataset-transformoperation-projectoperation
    - ``p_RenameColumnOperation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-transformoperation.html#cfn-quicksight-dataset-transformoperation-renamecolumnoperation
    - ``p_TagColumnOperation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-transformoperation.html#cfn-quicksight-dataset-transformoperation-tagcolumnoperation
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSet.TransformOperation"
    
    p_CastColumnTypeOperation: typing.Union['PropDataSetCastColumnTypeOperation', dict] = attr.ib(
        default=None,
        converter=PropDataSetCastColumnTypeOperation.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSetCastColumnTypeOperation)),
        metadata={AttrMeta.PROPERTY_NAME: "CastColumnTypeOperation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-transformoperation.html#cfn-quicksight-dataset-transformoperation-castcolumntypeoperation"""
    p_CreateColumnsOperation: typing.Union['PropDataSetCreateColumnsOperation', dict] = attr.ib(
        default=None,
        converter=PropDataSetCreateColumnsOperation.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSetCreateColumnsOperation)),
        metadata={AttrMeta.PROPERTY_NAME: "CreateColumnsOperation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-transformoperation.html#cfn-quicksight-dataset-transformoperation-createcolumnsoperation"""
    p_FilterOperation: typing.Union['PropDataSetFilterOperation', dict] = attr.ib(
        default=None,
        converter=PropDataSetFilterOperation.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSetFilterOperation)),
        metadata={AttrMeta.PROPERTY_NAME: "FilterOperation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-transformoperation.html#cfn-quicksight-dataset-transformoperation-filteroperation"""
    p_ProjectOperation: typing.Union['PropDataSetProjectOperation', dict] = attr.ib(
        default=None,
        converter=PropDataSetProjectOperation.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSetProjectOperation)),
        metadata={AttrMeta.PROPERTY_NAME: "ProjectOperation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-transformoperation.html#cfn-quicksight-dataset-transformoperation-projectoperation"""
    p_RenameColumnOperation: typing.Union['PropDataSetRenameColumnOperation', dict] = attr.ib(
        default=None,
        converter=PropDataSetRenameColumnOperation.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSetRenameColumnOperation)),
        metadata={AttrMeta.PROPERTY_NAME: "RenameColumnOperation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-transformoperation.html#cfn-quicksight-dataset-transformoperation-renamecolumnoperation"""
    p_TagColumnOperation: typing.Union['PropDataSetTagColumnOperation', dict] = attr.ib(
        default=None,
        converter=PropDataSetTagColumnOperation.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSetTagColumnOperation)),
        metadata={AttrMeta.PROPERTY_NAME: "TagColumnOperation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-transformoperation.html#cfn-quicksight-dataset-transformoperation-tagcolumnoperation"""

@attr.s
class PropThemeSheetStyle(Property):
    """
    AWS Object Type = "AWS::QuickSight::Theme.SheetStyle"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-sheetstyle.html

    Property Document:
    
    - ``p_Tile``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-sheetstyle.html#cfn-quicksight-theme-sheetstyle-tile
    - ``p_TileLayout``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-sheetstyle.html#cfn-quicksight-theme-sheetstyle-tilelayout
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Theme.SheetStyle"
    
    p_Tile: typing.Union['PropThemeTileStyle', dict] = attr.ib(
        default=None,
        converter=PropThemeTileStyle.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropThemeTileStyle)),
        metadata={AttrMeta.PROPERTY_NAME: "Tile"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-sheetstyle.html#cfn-quicksight-theme-sheetstyle-tile"""
    p_TileLayout: typing.Union['PropThemeTileLayoutStyle', dict] = attr.ib(
        default=None,
        converter=PropThemeTileLayoutStyle.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropThemeTileLayoutStyle)),
        metadata={AttrMeta.PROPERTY_NAME: "TileLayout"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-sheetstyle.html#cfn-quicksight-theme-sheetstyle-tilelayout"""

@attr.s
class PropDataSourceDataSourceParameters(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSource.DataSourceParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html

    Property Document:
    
    - ``p_AmazonElasticsearchParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-amazonelasticsearchparameters
    - ``p_AmazonOpenSearchParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-amazonopensearchparameters
    - ``p_AthenaParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-athenaparameters
    - ``p_AuroraParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-auroraparameters
    - ``p_AuroraPostgreSqlParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-aurorapostgresqlparameters
    - ``p_MariaDbParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-mariadbparameters
    - ``p_MySqlParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-mysqlparameters
    - ``p_OracleParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-oracleparameters
    - ``p_PostgreSqlParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-postgresqlparameters
    - ``p_PrestoParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-prestoparameters
    - ``p_RdsParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-rdsparameters
    - ``p_RedshiftParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-redshiftparameters
    - ``p_S3Parameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-s3parameters
    - ``p_SnowflakeParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-snowflakeparameters
    - ``p_SparkParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-sparkparameters
    - ``p_SqlServerParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-sqlserverparameters
    - ``p_TeradataParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-teradataparameters
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSource.DataSourceParameters"
    
    p_AmazonElasticsearchParameters: typing.Union['PropDataSourceAmazonElasticsearchParameters', dict] = attr.ib(
        default=None,
        converter=PropDataSourceAmazonElasticsearchParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSourceAmazonElasticsearchParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "AmazonElasticsearchParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-amazonelasticsearchparameters"""
    p_AmazonOpenSearchParameters: typing.Union['PropDataSourceAmazonOpenSearchParameters', dict] = attr.ib(
        default=None,
        converter=PropDataSourceAmazonOpenSearchParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSourceAmazonOpenSearchParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "AmazonOpenSearchParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-amazonopensearchparameters"""
    p_AthenaParameters: typing.Union['PropDataSourceAthenaParameters', dict] = attr.ib(
        default=None,
        converter=PropDataSourceAthenaParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSourceAthenaParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "AthenaParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-athenaparameters"""
    p_AuroraParameters: typing.Union['PropDataSourceAuroraParameters', dict] = attr.ib(
        default=None,
        converter=PropDataSourceAuroraParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSourceAuroraParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "AuroraParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-auroraparameters"""
    p_AuroraPostgreSqlParameters: typing.Union['PropDataSourceAuroraPostgreSqlParameters', dict] = attr.ib(
        default=None,
        converter=PropDataSourceAuroraPostgreSqlParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSourceAuroraPostgreSqlParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "AuroraPostgreSqlParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-aurorapostgresqlparameters"""
    p_MariaDbParameters: typing.Union['PropDataSourceMariaDbParameters', dict] = attr.ib(
        default=None,
        converter=PropDataSourceMariaDbParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSourceMariaDbParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "MariaDbParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-mariadbparameters"""
    p_MySqlParameters: typing.Union['PropDataSourceMySqlParameters', dict] = attr.ib(
        default=None,
        converter=PropDataSourceMySqlParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSourceMySqlParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "MySqlParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-mysqlparameters"""
    p_OracleParameters: typing.Union['PropDataSourceOracleParameters', dict] = attr.ib(
        default=None,
        converter=PropDataSourceOracleParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSourceOracleParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "OracleParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-oracleparameters"""
    p_PostgreSqlParameters: typing.Union['PropDataSourcePostgreSqlParameters', dict] = attr.ib(
        default=None,
        converter=PropDataSourcePostgreSqlParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSourcePostgreSqlParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "PostgreSqlParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-postgresqlparameters"""
    p_PrestoParameters: typing.Union['PropDataSourcePrestoParameters', dict] = attr.ib(
        default=None,
        converter=PropDataSourcePrestoParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSourcePrestoParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "PrestoParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-prestoparameters"""
    p_RdsParameters: typing.Union['PropDataSourceRdsParameters', dict] = attr.ib(
        default=None,
        converter=PropDataSourceRdsParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSourceRdsParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "RdsParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-rdsparameters"""
    p_RedshiftParameters: typing.Union['PropDataSourceRedshiftParameters', dict] = attr.ib(
        default=None,
        converter=PropDataSourceRedshiftParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSourceRedshiftParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "RedshiftParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-redshiftparameters"""
    p_S3Parameters: typing.Union['PropDataSourceS3Parameters', dict] = attr.ib(
        default=None,
        converter=PropDataSourceS3Parameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSourceS3Parameters)),
        metadata={AttrMeta.PROPERTY_NAME: "S3Parameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-s3parameters"""
    p_SnowflakeParameters: typing.Union['PropDataSourceSnowflakeParameters', dict] = attr.ib(
        default=None,
        converter=PropDataSourceSnowflakeParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSourceSnowflakeParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "SnowflakeParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-snowflakeparameters"""
    p_SparkParameters: typing.Union['PropDataSourceSparkParameters', dict] = attr.ib(
        default=None,
        converter=PropDataSourceSparkParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSourceSparkParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "SparkParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-sparkparameters"""
    p_SqlServerParameters: typing.Union['PropDataSourceSqlServerParameters', dict] = attr.ib(
        default=None,
        converter=PropDataSourceSqlServerParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSourceSqlServerParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "SqlServerParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-sqlserverparameters"""
    p_TeradataParameters: typing.Union['PropDataSourceTeradataParameters', dict] = attr.ib(
        default=None,
        converter=PropDataSourceTeradataParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSourceTeradataParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "TeradataParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourceparameters.html#cfn-quicksight-datasource-datasourceparameters-teradataparameters"""

@attr.s
class PropDataSourceCredentialPair(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSource.CredentialPair"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-credentialpair.html

    Property Document:
    
    - ``rp_Password``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-credentialpair.html#cfn-quicksight-datasource-credentialpair-password
    - ``rp_Username``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-credentialpair.html#cfn-quicksight-datasource-credentialpair-username
    - ``p_AlternateDataSourceParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-credentialpair.html#cfn-quicksight-datasource-credentialpair-alternatedatasourceparameters
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSource.CredentialPair"
    
    rp_Password: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Password"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-credentialpair.html#cfn-quicksight-datasource-credentialpair-password"""
    rp_Username: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Username"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-credentialpair.html#cfn-quicksight-datasource-credentialpair-username"""
    p_AlternateDataSourceParameters: typing.List[typing.Union['PropDataSourceDataSourceParameters', dict]] = attr.ib(
        default=None,
        converter=PropDataSourceDataSourceParameters.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDataSourceDataSourceParameters), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AlternateDataSourceParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-credentialpair.html#cfn-quicksight-datasource-credentialpair-alternatedatasourceparameters"""

@attr.s
class PropDataSetPhysicalTable(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSet.PhysicalTable"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-physicaltable.html

    Property Document:
    
    - ``p_CustomSql``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-physicaltable.html#cfn-quicksight-dataset-physicaltable-customsql
    - ``p_RelationalTable``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-physicaltable.html#cfn-quicksight-dataset-physicaltable-relationaltable
    - ``p_S3Source``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-physicaltable.html#cfn-quicksight-dataset-physicaltable-s3source
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSet.PhysicalTable"
    
    p_CustomSql: typing.Union['PropDataSetCustomSql', dict] = attr.ib(
        default=None,
        converter=PropDataSetCustomSql.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSetCustomSql)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomSql"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-physicaltable.html#cfn-quicksight-dataset-physicaltable-customsql"""
    p_RelationalTable: typing.Union['PropDataSetRelationalTable', dict] = attr.ib(
        default=None,
        converter=PropDataSetRelationalTable.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSetRelationalTable)),
        metadata={AttrMeta.PROPERTY_NAME: "RelationalTable"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-physicaltable.html#cfn-quicksight-dataset-physicaltable-relationaltable"""
    p_S3Source: typing.Union['PropDataSetS3Source', dict] = attr.ib(
        default=None,
        converter=PropDataSetS3Source.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSetS3Source)),
        metadata={AttrMeta.PROPERTY_NAME: "S3Source"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-physicaltable.html#cfn-quicksight-dataset-physicaltable-s3source"""

@attr.s
class PropDashboardDashboardSourceEntity(Property):
    """
    AWS Object Type = "AWS::QuickSight::Dashboard.DashboardSourceEntity"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardsourceentity.html

    Property Document:
    
    - ``p_SourceTemplate``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardsourceentity.html#cfn-quicksight-dashboard-dashboardsourceentity-sourcetemplate
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Dashboard.DashboardSourceEntity"
    
    p_SourceTemplate: typing.Union['PropDashboardDashboardSourceTemplate', dict] = attr.ib(
        default=None,
        converter=PropDashboardDashboardSourceTemplate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDashboardDashboardSourceTemplate)),
        metadata={AttrMeta.PROPERTY_NAME: "SourceTemplate"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardsourceentity.html#cfn-quicksight-dashboard-dashboardsourceentity-sourcetemplate"""

@attr.s
class PropThemeThemeConfiguration(Property):
    """
    AWS Object Type = "AWS::QuickSight::Theme.ThemeConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeconfiguration.html

    Property Document:
    
    - ``p_DataColorPalette``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeconfiguration.html#cfn-quicksight-theme-themeconfiguration-datacolorpalette
    - ``p_Sheet``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeconfiguration.html#cfn-quicksight-theme-themeconfiguration-sheet
    - ``p_Typography``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeconfiguration.html#cfn-quicksight-theme-themeconfiguration-typography
    - ``p_UIColorPalette``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeconfiguration.html#cfn-quicksight-theme-themeconfiguration-uicolorpalette
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Theme.ThemeConfiguration"
    
    p_DataColorPalette: typing.Union['PropThemeDataColorPalette', dict] = attr.ib(
        default=None,
        converter=PropThemeDataColorPalette.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropThemeDataColorPalette)),
        metadata={AttrMeta.PROPERTY_NAME: "DataColorPalette"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeconfiguration.html#cfn-quicksight-theme-themeconfiguration-datacolorpalette"""
    p_Sheet: typing.Union['PropThemeSheetStyle', dict] = attr.ib(
        default=None,
        converter=PropThemeSheetStyle.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropThemeSheetStyle)),
        metadata={AttrMeta.PROPERTY_NAME: "Sheet"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeconfiguration.html#cfn-quicksight-theme-themeconfiguration-sheet"""
    p_Typography: typing.Union['PropThemeTypography', dict] = attr.ib(
        default=None,
        converter=PropThemeTypography.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropThemeTypography)),
        metadata={AttrMeta.PROPERTY_NAME: "Typography"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeconfiguration.html#cfn-quicksight-theme-themeconfiguration-typography"""
    p_UIColorPalette: typing.Union['PropThemeUIColorPalette', dict] = attr.ib(
        default=None,
        converter=PropThemeUIColorPalette.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropThemeUIColorPalette)),
        metadata={AttrMeta.PROPERTY_NAME: "UIColorPalette"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeconfiguration.html#cfn-quicksight-theme-themeconfiguration-uicolorpalette"""

@attr.s
class PropDataSetLogicalTable(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSet.LogicalTable"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-logicaltable.html

    Property Document:
    
    - ``rp_Alias``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-logicaltable.html#cfn-quicksight-dataset-logicaltable-alias
    - ``rp_Source``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-logicaltable.html#cfn-quicksight-dataset-logicaltable-source
    - ``p_DataTransforms``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-logicaltable.html#cfn-quicksight-dataset-logicaltable-datatransforms
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSet.LogicalTable"
    
    rp_Alias: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Alias"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-logicaltable.html#cfn-quicksight-dataset-logicaltable-alias"""
    rp_Source: typing.Union['PropDataSetLogicalTableSource', dict] = attr.ib(
        default=None,
        converter=PropDataSetLogicalTableSource.from_dict,
        validator=attr.validators.instance_of(PropDataSetLogicalTableSource),
        metadata={AttrMeta.PROPERTY_NAME: "Source"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-logicaltable.html#cfn-quicksight-dataset-logicaltable-source"""
    p_DataTransforms: typing.List[typing.Union['PropDataSetTransformOperation', dict]] = attr.ib(
        default=None,
        converter=PropDataSetTransformOperation.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDataSetTransformOperation), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "DataTransforms"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-logicaltable.html#cfn-quicksight-dataset-logicaltable-datatransforms"""

@attr.s
class PropDataSourceDataSourceCredentials(Property):
    """
    AWS Object Type = "AWS::QuickSight::DataSource.DataSourceCredentials"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourcecredentials.html

    Property Document:
    
    - ``p_CopySourceArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourcecredentials.html#cfn-quicksight-datasource-datasourcecredentials-copysourcearn
    - ``p_CredentialPair``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourcecredentials.html#cfn-quicksight-datasource-datasourcecredentials-credentialpair
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSource.DataSourceCredentials"
    
    p_CopySourceArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CopySourceArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourcecredentials.html#cfn-quicksight-datasource-datasourcecredentials-copysourcearn"""
    p_CredentialPair: typing.Union['PropDataSourceCredentialPair', dict] = attr.ib(
        default=None,
        converter=PropDataSourceCredentialPair.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSourceCredentialPair)),
        metadata={AttrMeta.PROPERTY_NAME: "CredentialPair"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-datasource-datasourcecredentials.html#cfn-quicksight-datasource-datasourcecredentials-credentialpair"""


#--- Resource declaration ---

@attr.s
class Dashboard(Resource):
    """
    AWS Object Type = "AWS::QuickSight::Dashboard"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html

    Property Document:
    
    - ``rp_AwsAccountId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-awsaccountid
    - ``rp_DashboardId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-dashboardid
    - ``rp_SourceEntity``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-sourceentity
    - ``p_DashboardPublishOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-dashboardpublishoptions
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-name
    - ``p_Parameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-parameters
    - ``p_Permissions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-permissions
    - ``p_ThemeArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-themearn
    - ``p_VersionDescription``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-versiondescription
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-tags
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Dashboard"

    
    rp_AwsAccountId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AwsAccountId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-awsaccountid"""
    rp_DashboardId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DashboardId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-dashboardid"""
    rp_SourceEntity: typing.Union['PropDashboardDashboardSourceEntity', dict] = attr.ib(
        default=None,
        converter=PropDashboardDashboardSourceEntity.from_dict,
        validator=attr.validators.instance_of(PropDashboardDashboardSourceEntity),
        metadata={AttrMeta.PROPERTY_NAME: "SourceEntity"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-sourceentity"""
    p_DashboardPublishOptions: typing.Union['PropDashboardDashboardPublishOptions', dict] = attr.ib(
        default=None,
        converter=PropDashboardDashboardPublishOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDashboardDashboardPublishOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "DashboardPublishOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-dashboardpublishoptions"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-name"""
    p_Parameters: typing.Union['PropDashboardParameters', dict] = attr.ib(
        default=None,
        converter=PropDashboardParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDashboardParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "Parameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-parameters"""
    p_Permissions: typing.List[typing.Union['PropDashboardResourcePermission', dict]] = attr.ib(
        default=None,
        converter=PropDashboardResourcePermission.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDashboardResourcePermission), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Permissions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-permissions"""
    p_ThemeArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ThemeArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-themearn"""
    p_VersionDescription: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "VersionDescription"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-versiondescription"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#cfn-quicksight-dashboard-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#aws-resource-quicksight-dashboard-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_CreatedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#aws-resource-quicksight-dashboard-return-values"""
        return GetAtt(resource=self, attr_name="CreatedTime")
    
    @property
    def rv_LastPublishedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#aws-resource-quicksight-dashboard-return-values"""
        return GetAtt(resource=self, attr_name="LastPublishedTime")
    
    @property
    def rv_LastUpdatedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html#aws-resource-quicksight-dashboard-return-values"""
        return GetAtt(resource=self, attr_name="LastUpdatedTime")
    

@attr.s
class Theme(Resource):
    """
    AWS Object Type = "AWS::QuickSight::Theme"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html

    Property Document:
    
    - ``rp_AwsAccountId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-awsaccountid
    - ``rp_ThemeId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-themeid
    - ``p_BaseThemeId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-basethemeid
    - ``p_Configuration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-configuration
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-name
    - ``p_Permissions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-permissions
    - ``p_VersionDescription``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-versiondescription
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-tags
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Theme"

    
    rp_AwsAccountId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AwsAccountId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-awsaccountid"""
    rp_ThemeId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ThemeId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-themeid"""
    p_BaseThemeId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BaseThemeId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-basethemeid"""
    p_Configuration: typing.Union['PropThemeThemeConfiguration', dict] = attr.ib(
        default=None,
        converter=PropThemeThemeConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropThemeThemeConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "Configuration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-configuration"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-name"""
    p_Permissions: typing.List[typing.Union['PropThemeResourcePermission', dict]] = attr.ib(
        default=None,
        converter=PropThemeResourcePermission.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropThemeResourcePermission), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Permissions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-permissions"""
    p_VersionDescription: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "VersionDescription"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-versiondescription"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#cfn-quicksight-theme-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#aws-resource-quicksight-theme-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_CreatedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#aws-resource-quicksight-theme-return-values"""
        return GetAtt(resource=self, attr_name="CreatedTime")
    
    @property
    def rv_LastUpdatedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#aws-resource-quicksight-theme-return-values"""
        return GetAtt(resource=self, attr_name="LastUpdatedTime")
    
    @property
    def rv_Type(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html#aws-resource-quicksight-theme-return-values"""
        return GetAtt(resource=self, attr_name="Type")
    

@attr.s
class Analysis(Resource):
    """
    AWS Object Type = "AWS::QuickSight::Analysis"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html

    Property Document:
    
    - ``rp_AnalysisId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-analysisid
    - ``rp_AwsAccountId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-awsaccountid
    - ``rp_SourceEntity``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-sourceentity
    - ``p_Errors``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-errors
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-name
    - ``p_Parameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-parameters
    - ``p_Permissions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-permissions
    - ``p_ThemeArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-themearn
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-tags
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Analysis"

    
    rp_AnalysisId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AnalysisId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-analysisid"""
    rp_AwsAccountId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AwsAccountId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-awsaccountid"""
    rp_SourceEntity: typing.Union['PropAnalysisAnalysisSourceEntity', dict] = attr.ib(
        default=None,
        converter=PropAnalysisAnalysisSourceEntity.from_dict,
        validator=attr.validators.instance_of(PropAnalysisAnalysisSourceEntity),
        metadata={AttrMeta.PROPERTY_NAME: "SourceEntity"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-sourceentity"""
    p_Errors: typing.List[typing.Union['PropAnalysisAnalysisError', dict]] = attr.ib(
        default=None,
        converter=PropAnalysisAnalysisError.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropAnalysisAnalysisError), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Errors"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-errors"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-name"""
    p_Parameters: typing.Union['PropAnalysisParameters', dict] = attr.ib(
        default=None,
        converter=PropAnalysisParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropAnalysisParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "Parameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-parameters"""
    p_Permissions: typing.List[typing.Union['PropAnalysisResourcePermission', dict]] = attr.ib(
        default=None,
        converter=PropAnalysisResourcePermission.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropAnalysisResourcePermission), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Permissions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-permissions"""
    p_ThemeArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ThemeArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-themearn"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#cfn-quicksight-analysis-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#aws-resource-quicksight-analysis-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_CreatedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#aws-resource-quicksight-analysis-return-values"""
        return GetAtt(resource=self, attr_name="CreatedTime")
    
    @property
    def rv_DataSetArns(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#aws-resource-quicksight-analysis-return-values"""
        return GetAtt(resource=self, attr_name="DataSetArns")
    
    @property
    def rv_LastUpdatedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#aws-resource-quicksight-analysis-return-values"""
        return GetAtt(resource=self, attr_name="LastUpdatedTime")
    
    @property
    def rv_Sheets(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#aws-resource-quicksight-analysis-return-values"""
        return GetAtt(resource=self, attr_name="Sheets")
    
    @property
    def rv_Status(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html#aws-resource-quicksight-analysis-return-values"""
        return GetAtt(resource=self, attr_name="Status")
    

@attr.s
class Template(Resource):
    """
    AWS Object Type = "AWS::QuickSight::Template"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html

    Property Document:
    
    - ``rp_AwsAccountId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-awsaccountid
    - ``rp_SourceEntity``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-sourceentity
    - ``rp_TemplateId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-templateid
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-name
    - ``p_Permissions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-permissions
    - ``p_VersionDescription``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-versiondescription
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-tags
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::Template"

    
    rp_AwsAccountId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AwsAccountId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-awsaccountid"""
    rp_SourceEntity: typing.Union['PropTemplateTemplateSourceEntity', dict] = attr.ib(
        default=None,
        converter=PropTemplateTemplateSourceEntity.from_dict,
        validator=attr.validators.instance_of(PropTemplateTemplateSourceEntity),
        metadata={AttrMeta.PROPERTY_NAME: "SourceEntity"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-sourceentity"""
    rp_TemplateId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TemplateId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-templateid"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-name"""
    p_Permissions: typing.List[typing.Union['PropTemplateResourcePermission', dict]] = attr.ib(
        default=None,
        converter=PropTemplateResourcePermission.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTemplateResourcePermission), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Permissions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-permissions"""
    p_VersionDescription: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "VersionDescription"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-versiondescription"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#cfn-quicksight-template-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#aws-resource-quicksight-template-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_CreatedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#aws-resource-quicksight-template-return-values"""
        return GetAtt(resource=self, attr_name="CreatedTime")
    
    @property
    def rv_LastUpdatedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html#aws-resource-quicksight-template-return-values"""
        return GetAtt(resource=self, attr_name="LastUpdatedTime")
    

@attr.s
class DataSource(Resource):
    """
    AWS Object Type = "AWS::QuickSight::DataSource"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html

    Property Document:
    
    - ``p_AlternateDataSourceParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-alternatedatasourceparameters
    - ``p_AwsAccountId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-awsaccountid
    - ``p_Credentials``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-credentials
    - ``p_DataSourceId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-datasourceid
    - ``p_DataSourceParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-datasourceparameters
    - ``p_ErrorInfo``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-errorinfo
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-name
    - ``p_Permissions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-permissions
    - ``p_SslProperties``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-sslproperties
    - ``p_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-type
    - ``p_VpcConnectionProperties``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-vpcconnectionproperties
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-tags
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSource"

    
    p_AlternateDataSourceParameters: typing.List[typing.Union['PropDataSourceDataSourceParameters', dict]] = attr.ib(
        default=None,
        converter=PropDataSourceDataSourceParameters.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDataSourceDataSourceParameters), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AlternateDataSourceParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-alternatedatasourceparameters"""
    p_AwsAccountId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AwsAccountId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-awsaccountid"""
    p_Credentials: typing.Union['PropDataSourceDataSourceCredentials', dict] = attr.ib(
        default=None,
        converter=PropDataSourceDataSourceCredentials.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSourceDataSourceCredentials)),
        metadata={AttrMeta.PROPERTY_NAME: "Credentials"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-credentials"""
    p_DataSourceId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DataSourceId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-datasourceid"""
    p_DataSourceParameters: typing.Union['PropDataSourceDataSourceParameters', dict] = attr.ib(
        default=None,
        converter=PropDataSourceDataSourceParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSourceDataSourceParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "DataSourceParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-datasourceparameters"""
    p_ErrorInfo: typing.Union['PropDataSourceDataSourceErrorInfo', dict] = attr.ib(
        default=None,
        converter=PropDataSourceDataSourceErrorInfo.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSourceDataSourceErrorInfo)),
        metadata={AttrMeta.PROPERTY_NAME: "ErrorInfo"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-errorinfo"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-name"""
    p_Permissions: typing.List[typing.Union['PropDataSourceResourcePermission', dict]] = attr.ib(
        default=None,
        converter=PropDataSourceResourcePermission.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDataSourceResourcePermission), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Permissions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-permissions"""
    p_SslProperties: typing.Union['PropDataSourceSslProperties', dict] = attr.ib(
        default=None,
        converter=PropDataSourceSslProperties.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSourceSslProperties)),
        metadata={AttrMeta.PROPERTY_NAME: "SslProperties"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-sslproperties"""
    p_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-type"""
    p_VpcConnectionProperties: typing.Union['PropDataSourceVpcConnectionProperties', dict] = attr.ib(
        default=None,
        converter=PropDataSourceVpcConnectionProperties.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSourceVpcConnectionProperties)),
        metadata={AttrMeta.PROPERTY_NAME: "VpcConnectionProperties"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-vpcconnectionproperties"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#cfn-quicksight-datasource-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#aws-resource-quicksight-datasource-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_CreatedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#aws-resource-quicksight-datasource-return-values"""
        return GetAtt(resource=self, attr_name="CreatedTime")
    
    @property
    def rv_LastUpdatedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#aws-resource-quicksight-datasource-return-values"""
        return GetAtt(resource=self, attr_name="LastUpdatedTime")
    
    @property
    def rv_Status(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html#aws-resource-quicksight-datasource-return-values"""
        return GetAtt(resource=self, attr_name="Status")
    

@attr.s
class DataSet(Resource):
    """
    AWS Object Type = "AWS::QuickSight::DataSet"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html

    Property Document:
    
    - ``p_AwsAccountId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-awsaccountid
    - ``p_ColumnGroups``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-columngroups
    - ``p_ColumnLevelPermissionRules``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-columnlevelpermissionrules
    - ``p_DataSetId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-datasetid
    - ``p_FieldFolders``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-fieldfolders
    - ``p_ImportMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-importmode
    - ``p_IngestionWaitPolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-ingestionwaitpolicy
    - ``p_LogicalTableMap``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-logicaltablemap
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-name
    - ``p_Permissions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-permissions
    - ``p_PhysicalTableMap``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-physicaltablemap
    - ``p_RowLevelPermissionDataSet``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-rowlevelpermissiondataset
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-tags
    """
    AWS_OBJECT_TYPE = "AWS::QuickSight::DataSet"

    
    p_AwsAccountId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AwsAccountId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-awsaccountid"""
    p_ColumnGroups: typing.List[typing.Union['PropDataSetColumnGroup', dict]] = attr.ib(
        default=None,
        converter=PropDataSetColumnGroup.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDataSetColumnGroup), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ColumnGroups"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-columngroups"""
    p_ColumnLevelPermissionRules: typing.List[typing.Union['PropDataSetColumnLevelPermissionRule', dict]] = attr.ib(
        default=None,
        converter=PropDataSetColumnLevelPermissionRule.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDataSetColumnLevelPermissionRule), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ColumnLevelPermissionRules"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-columnlevelpermissionrules"""
    p_DataSetId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DataSetId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-datasetid"""
    p_FieldFolders: typing.Union['PropDataSetFieldFolder', dict] = attr.ib(
        default=None,
        converter=PropDataSetFieldFolder.from_list,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSetFieldFolder)),
        metadata={AttrMeta.PROPERTY_NAME: "FieldFolders"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-fieldfolders"""
    p_ImportMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ImportMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-importmode"""
    p_IngestionWaitPolicy: typing.Union['PropDataSetIngestionWaitPolicy', dict] = attr.ib(
        default=None,
        converter=PropDataSetIngestionWaitPolicy.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSetIngestionWaitPolicy)),
        metadata={AttrMeta.PROPERTY_NAME: "IngestionWaitPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-ingestionwaitpolicy"""
    p_LogicalTableMap: typing.Union['PropDataSetLogicalTable', dict] = attr.ib(
        default=None,
        converter=PropDataSetLogicalTable.from_list,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSetLogicalTable)),
        metadata={AttrMeta.PROPERTY_NAME: "LogicalTableMap"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-logicaltablemap"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-name"""
    p_Permissions: typing.List[typing.Union['PropDataSetResourcePermission', dict]] = attr.ib(
        default=None,
        converter=PropDataSetResourcePermission.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDataSetResourcePermission), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Permissions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-permissions"""
    p_PhysicalTableMap: typing.Union['PropDataSetPhysicalTable', dict] = attr.ib(
        default=None,
        converter=PropDataSetPhysicalTable.from_list,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSetPhysicalTable)),
        metadata={AttrMeta.PROPERTY_NAME: "PhysicalTableMap"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-physicaltablemap"""
    p_RowLevelPermissionDataSet: typing.Union['PropDataSetRowLevelPermissionDataSet', dict] = attr.ib(
        default=None,
        converter=PropDataSetRowLevelPermissionDataSet.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataSetRowLevelPermissionDataSet)),
        metadata={AttrMeta.PROPERTY_NAME: "RowLevelPermissionDataSet"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-rowlevelpermissiondataset"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#aws-resource-quicksight-dataset-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_ConsumedSpiceCapacityInBytes(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#aws-resource-quicksight-dataset-return-values"""
        return GetAtt(resource=self, attr_name="ConsumedSpiceCapacityInBytes")
    
    @property
    def rv_CreatedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#aws-resource-quicksight-dataset-return-values"""
        return GetAtt(resource=self, attr_name="CreatedTime")
    
    @property
    def rv_LastUpdatedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#aws-resource-quicksight-dataset-return-values"""
        return GetAtt(resource=self, attr_name="LastUpdatedTime")
    
    @property
    def rv_OutputColumns(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#aws-resource-quicksight-dataset-return-values"""
        return GetAtt(resource=self, attr_name="OutputColumns")
    
