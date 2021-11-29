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
class PropPermissionsDataLocationResource(Property):
    """
    AWS Object Type = "AWS::LakeFormation::Permissions.DataLocationResource"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html

    Property Document:
    
    - ``p_CatalogId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html#cfn-lakeformation-permissions-datalocationresource-catalogid
    - ``p_S3Resource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html#cfn-lakeformation-permissions-datalocationresource-s3resource
    """
    AWS_OBJECT_TYPE = "AWS::LakeFormation::Permissions.DataLocationResource"
    
    p_CatalogId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CatalogId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html#cfn-lakeformation-permissions-datalocationresource-catalogid"""
    p_S3Resource: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "S3Resource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html#cfn-lakeformation-permissions-datalocationresource-s3resource"""

@attr.s
class PropDataLakeSettingsDataLakePrincipal(Property):
    """
    AWS Object Type = "AWS::LakeFormation::DataLakeSettings.DataLakePrincipal"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-datalakeprincipal.html

    Property Document:
    
    - ``p_DataLakePrincipalIdentifier``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-datalakeprincipal.html#cfn-lakeformation-datalakesettings-datalakeprincipal-datalakeprincipalidentifier
    """
    AWS_OBJECT_TYPE = "AWS::LakeFormation::DataLakeSettings.DataLakePrincipal"
    
    p_DataLakePrincipalIdentifier: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DataLakePrincipalIdentifier"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-datalakeprincipal.html#cfn-lakeformation-datalakesettings-datalakeprincipal-datalakeprincipalidentifier"""

@attr.s
class PropPermissionsColumnWildcard(Property):
    """
    AWS Object Type = "AWS::LakeFormation::Permissions.ColumnWildcard"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-columnwildcard.html

    Property Document:
    
    - ``p_ExcludedColumnNames``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-columnwildcard.html#cfn-lakeformation-permissions-columnwildcard-excludedcolumnnames
    """
    AWS_OBJECT_TYPE = "AWS::LakeFormation::Permissions.ColumnWildcard"
    
    p_ExcludedColumnNames: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ExcludedColumnNames"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-columnwildcard.html#cfn-lakeformation-permissions-columnwildcard-excludedcolumnnames"""

@attr.s
class PropPermissionsDatabaseResource(Property):
    """
    AWS Object Type = "AWS::LakeFormation::Permissions.DatabaseResource"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-databaseresource.html

    Property Document:
    
    - ``p_CatalogId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-databaseresource.html#cfn-lakeformation-permissions-databaseresource-catalogid
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-databaseresource.html#cfn-lakeformation-permissions-databaseresource-name
    """
    AWS_OBJECT_TYPE = "AWS::LakeFormation::Permissions.DatabaseResource"
    
    p_CatalogId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CatalogId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-databaseresource.html#cfn-lakeformation-permissions-databaseresource-catalogid"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-databaseresource.html#cfn-lakeformation-permissions-databaseresource-name"""

@attr.s
class PropPermissionsTableWildcard(Property):
    """
    AWS Object Type = "AWS::LakeFormation::Permissions.TableWildcard"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewildcard.html

    Property Document:
    
    """
    AWS_OBJECT_TYPE = "AWS::LakeFormation::Permissions.TableWildcard"
    

@attr.s
class PropPermissionsDataLakePrincipal(Property):
    """
    AWS Object Type = "AWS::LakeFormation::Permissions.DataLakePrincipal"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalakeprincipal.html

    Property Document:
    
    - ``p_DataLakePrincipalIdentifier``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalakeprincipal.html#cfn-lakeformation-permissions-datalakeprincipal-datalakeprincipalidentifier
    """
    AWS_OBJECT_TYPE = "AWS::LakeFormation::Permissions.DataLakePrincipal"
    
    p_DataLakePrincipalIdentifier: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DataLakePrincipalIdentifier"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalakeprincipal.html#cfn-lakeformation-permissions-datalakeprincipal-datalakeprincipalidentifier"""

@attr.s
class PropPermissionsTableResource(Property):
    """
    AWS Object Type = "AWS::LakeFormation::Permissions.TableResource"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html

    Property Document:
    
    - ``p_CatalogId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-catalogid
    - ``p_DatabaseName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-databasename
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-name
    - ``p_TableWildcard``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-tablewildcard
    """
    AWS_OBJECT_TYPE = "AWS::LakeFormation::Permissions.TableResource"
    
    p_CatalogId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CatalogId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-catalogid"""
    p_DatabaseName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DatabaseName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-databasename"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-name"""
    p_TableWildcard: typing.Union['PropPermissionsTableWildcard', dict] = attr.ib(
        default=None,
        converter=PropPermissionsTableWildcard.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropPermissionsTableWildcard)),
        metadata={AttrMeta.PROPERTY_NAME: "TableWildcard"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-tablewildcard"""

@attr.s
class PropPermissionsTableWithColumnsResource(Property):
    """
    AWS Object Type = "AWS::LakeFormation::Permissions.TableWithColumnsResource"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html

    Property Document:
    
    - ``p_CatalogId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-catalogid
    - ``p_ColumnNames``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-columnnames
    - ``p_ColumnWildcard``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-columnwildcard
    - ``p_DatabaseName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-databasename
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-name
    """
    AWS_OBJECT_TYPE = "AWS::LakeFormation::Permissions.TableWithColumnsResource"
    
    p_CatalogId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CatalogId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-catalogid"""
    p_ColumnNames: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ColumnNames"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-columnnames"""
    p_ColumnWildcard: typing.Union['PropPermissionsColumnWildcard', dict] = attr.ib(
        default=None,
        converter=PropPermissionsColumnWildcard.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropPermissionsColumnWildcard)),
        metadata={AttrMeta.PROPERTY_NAME: "ColumnWildcard"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-columnwildcard"""
    p_DatabaseName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DatabaseName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-databasename"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-name"""

@attr.s
class PropDataLakeSettingsAdmins(Property):
    """
    AWS Object Type = "AWS::LakeFormation::DataLakeSettings.Admins"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-admins.html

    Property Document:
    
    """
    AWS_OBJECT_TYPE = "AWS::LakeFormation::DataLakeSettings.Admins"
    

@attr.s
class PropPermissionsResource(Property):
    """
    AWS Object Type = "AWS::LakeFormation::Permissions.Resource"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html

    Property Document:
    
    - ``p_DataLocationResource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-datalocationresource
    - ``p_DatabaseResource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-databaseresource
    - ``p_TableResource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-tableresource
    - ``p_TableWithColumnsResource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-tablewithcolumnsresource
    """
    AWS_OBJECT_TYPE = "AWS::LakeFormation::Permissions.Resource"
    
    p_DataLocationResource: typing.Union['PropPermissionsDataLocationResource', dict] = attr.ib(
        default=None,
        converter=PropPermissionsDataLocationResource.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropPermissionsDataLocationResource)),
        metadata={AttrMeta.PROPERTY_NAME: "DataLocationResource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-datalocationresource"""
    p_DatabaseResource: typing.Union['PropPermissionsDatabaseResource', dict] = attr.ib(
        default=None,
        converter=PropPermissionsDatabaseResource.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropPermissionsDatabaseResource)),
        metadata={AttrMeta.PROPERTY_NAME: "DatabaseResource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-databaseresource"""
    p_TableResource: typing.Union['PropPermissionsTableResource', dict] = attr.ib(
        default=None,
        converter=PropPermissionsTableResource.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropPermissionsTableResource)),
        metadata={AttrMeta.PROPERTY_NAME: "TableResource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-tableresource"""
    p_TableWithColumnsResource: typing.Union['PropPermissionsTableWithColumnsResource', dict] = attr.ib(
        default=None,
        converter=PropPermissionsTableWithColumnsResource.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropPermissionsTableWithColumnsResource)),
        metadata={AttrMeta.PROPERTY_NAME: "TableWithColumnsResource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-tablewithcolumnsresource"""


#--- Resource declaration ---

@attr.s
class Resource(Resource):
    """
    AWS Object Type = "AWS::LakeFormation::Resource"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html

    Property Document:
    
    - ``rp_ResourceArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-resourcearn
    - ``rp_UseServiceLinkedRole``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-useservicelinkedrole
    - ``p_RoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-rolearn
    """
    AWS_OBJECT_TYPE = "AWS::LakeFormation::Resource"

    
    rp_ResourceArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-resourcearn"""
    rp_UseServiceLinkedRole: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "UseServiceLinkedRole"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-useservicelinkedrole"""
    p_RoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-rolearn"""

    

@attr.s
class DataLakeSettings(Resource):
    """
    AWS Object Type = "AWS::LakeFormation::DataLakeSettings"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html

    Property Document:
    
    - ``p_Admins``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-admins
    - ``p_TrustedResourceOwners``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-trustedresourceowners
    """
    AWS_OBJECT_TYPE = "AWS::LakeFormation::DataLakeSettings"

    
    p_Admins: typing.Union['PropDataLakeSettingsAdmins', dict] = attr.ib(
        default=None,
        converter=PropDataLakeSettingsAdmins.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDataLakeSettingsAdmins)),
        metadata={AttrMeta.PROPERTY_NAME: "Admins"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-admins"""
    p_TrustedResourceOwners: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "TrustedResourceOwners"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-trustedresourceowners"""

    

@attr.s
class Permissions(Resource):
    """
    AWS Object Type = "AWS::LakeFormation::Permissions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html

    Property Document:
    
    - ``rp_DataLakePrincipal``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-datalakeprincipal
    - ``rp_Resource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-resource
    - ``p_Permissions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-permissions
    - ``p_PermissionsWithGrantOption``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-permissionswithgrantoption
    """
    AWS_OBJECT_TYPE = "AWS::LakeFormation::Permissions"

    
    rp_DataLakePrincipal: typing.Union['PropPermissionsDataLakePrincipal', dict] = attr.ib(
        default=None,
        converter=PropPermissionsDataLakePrincipal.from_dict,
        validator=attr.validators.instance_of(PropPermissionsDataLakePrincipal),
        metadata={AttrMeta.PROPERTY_NAME: "DataLakePrincipal"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-datalakeprincipal"""
    rp_Resource: typing.Union['PropPermissionsResource', dict] = attr.ib(
        default=None,
        converter=PropPermissionsResource.from_dict,
        validator=attr.validators.instance_of(PropPermissionsResource),
        metadata={AttrMeta.PROPERTY_NAME: "Resource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-resource"""
    p_Permissions: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Permissions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-permissions"""
    p_PermissionsWithGrantOption: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "PermissionsWithGrantOption"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-permissionswithgrantoption"""

    
