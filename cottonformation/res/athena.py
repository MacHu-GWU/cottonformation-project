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
class PropWorkGroupEncryptionConfiguration(Property):
    """
    AWS Object Type = "AWS::Athena::WorkGroup.EncryptionConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-encryptionconfiguration.html

    Property Document:
    
    - ``rp_EncryptionOption``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-encryptionconfiguration.html#cfn-athena-workgroup-encryptionconfiguration-encryptionoption
    - ``p_KmsKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-encryptionconfiguration.html#cfn-athena-workgroup-encryptionconfiguration-kmskey
    """
    AWS_OBJECT_TYPE = "AWS::Athena::WorkGroup.EncryptionConfiguration"
    
    rp_EncryptionOption: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "EncryptionOption"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-encryptionconfiguration.html#cfn-athena-workgroup-encryptionconfiguration-encryptionoption"""
    p_KmsKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "KmsKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-encryptionconfiguration.html#cfn-athena-workgroup-encryptionconfiguration-kmskey"""

@attr.s
class PropWorkGroupEngineVersion(Property):
    """
    AWS Object Type = "AWS::Athena::WorkGroup.EngineVersion"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-engineversion.html

    Property Document:
    
    - ``p_EffectiveEngineVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-engineversion.html#cfn-athena-workgroup-engineversion-effectiveengineversion
    - ``p_SelectedEngineVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-engineversion.html#cfn-athena-workgroup-engineversion-selectedengineversion
    """
    AWS_OBJECT_TYPE = "AWS::Athena::WorkGroup.EngineVersion"
    
    p_EffectiveEngineVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "EffectiveEngineVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-engineversion.html#cfn-athena-workgroup-engineversion-effectiveengineversion"""
    p_SelectedEngineVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SelectedEngineVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-engineversion.html#cfn-athena-workgroup-engineversion-selectedengineversion"""

@attr.s
class PropWorkGroupResultConfiguration(Property):
    """
    AWS Object Type = "AWS::Athena::WorkGroup.ResultConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfiguration.html

    Property Document:
    
    - ``p_EncryptionConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfiguration.html#cfn-athena-workgroup-resultconfiguration-encryptionconfiguration
    - ``p_OutputLocation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfiguration.html#cfn-athena-workgroup-resultconfiguration-outputlocation
    """
    AWS_OBJECT_TYPE = "AWS::Athena::WorkGroup.ResultConfiguration"
    
    p_EncryptionConfiguration: typing.Union['PropWorkGroupEncryptionConfiguration', dict] = attr.ib(
        default=None,
        converter=PropWorkGroupEncryptionConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWorkGroupEncryptionConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "EncryptionConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfiguration.html#cfn-athena-workgroup-resultconfiguration-encryptionconfiguration"""
    p_OutputLocation: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "OutputLocation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfiguration.html#cfn-athena-workgroup-resultconfiguration-outputlocation"""

@attr.s
class PropWorkGroupResultConfigurationUpdates(Property):
    """
    AWS Object Type = "AWS::Athena::WorkGroup.ResultConfigurationUpdates"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html

    Property Document:
    
    - ``p_EncryptionConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html#cfn-athena-workgroup-resultconfigurationupdates-encryptionconfiguration
    - ``p_OutputLocation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html#cfn-athena-workgroup-resultconfigurationupdates-outputlocation
    - ``p_RemoveEncryptionConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html#cfn-athena-workgroup-resultconfigurationupdates-removeencryptionconfiguration
    - ``p_RemoveOutputLocation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html#cfn-athena-workgroup-resultconfigurationupdates-removeoutputlocation
    """
    AWS_OBJECT_TYPE = "AWS::Athena::WorkGroup.ResultConfigurationUpdates"
    
    p_EncryptionConfiguration: typing.Union['PropWorkGroupEncryptionConfiguration', dict] = attr.ib(
        default=None,
        converter=PropWorkGroupEncryptionConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWorkGroupEncryptionConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "EncryptionConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html#cfn-athena-workgroup-resultconfigurationupdates-encryptionconfiguration"""
    p_OutputLocation: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "OutputLocation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html#cfn-athena-workgroup-resultconfigurationupdates-outputlocation"""
    p_RemoveEncryptionConfiguration: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "RemoveEncryptionConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html#cfn-athena-workgroup-resultconfigurationupdates-removeencryptionconfiguration"""
    p_RemoveOutputLocation: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "RemoveOutputLocation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html#cfn-athena-workgroup-resultconfigurationupdates-removeoutputlocation"""

@attr.s
class PropWorkGroupWorkGroupConfiguration(Property):
    """
    AWS Object Type = "AWS::Athena::WorkGroup.WorkGroupConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html

    Property Document:
    
    - ``p_BytesScannedCutoffPerQuery``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-bytesscannedcutoffperquery
    - ``p_EnforceWorkGroupConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-enforceworkgroupconfiguration
    - ``p_EngineVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-engineversion
    - ``p_PublishCloudWatchMetricsEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-publishcloudwatchmetricsenabled
    - ``p_RequesterPaysEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-requesterpaysenabled
    - ``p_ResultConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-resultconfiguration
    """
    AWS_OBJECT_TYPE = "AWS::Athena::WorkGroup.WorkGroupConfiguration"
    
    p_BytesScannedCutoffPerQuery: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "BytesScannedCutoffPerQuery"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-bytesscannedcutoffperquery"""
    p_EnforceWorkGroupConfiguration: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EnforceWorkGroupConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-enforceworkgroupconfiguration"""
    p_EngineVersion: typing.Union['PropWorkGroupEngineVersion', dict] = attr.ib(
        default=None,
        converter=PropWorkGroupEngineVersion.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWorkGroupEngineVersion)),
        metadata={AttrMeta.PROPERTY_NAME: "EngineVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-engineversion"""
    p_PublishCloudWatchMetricsEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "PublishCloudWatchMetricsEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-publishcloudwatchmetricsenabled"""
    p_RequesterPaysEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "RequesterPaysEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-requesterpaysenabled"""
    p_ResultConfiguration: typing.Union['PropWorkGroupResultConfiguration', dict] = attr.ib(
        default=None,
        converter=PropWorkGroupResultConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWorkGroupResultConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "ResultConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-resultconfiguration"""

@attr.s
class PropWorkGroupWorkGroupConfigurationUpdates(Property):
    """
    AWS Object Type = "AWS::Athena::WorkGroup.WorkGroupConfigurationUpdates"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html

    Property Document:
    
    - ``p_BytesScannedCutoffPerQuery``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-bytesscannedcutoffperquery
    - ``p_EnforceWorkGroupConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-enforceworkgroupconfiguration
    - ``p_EngineVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-engineversion
    - ``p_PublishCloudWatchMetricsEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-publishcloudwatchmetricsenabled
    - ``p_RemoveBytesScannedCutoffPerQuery``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-removebytesscannedcutoffperquery
    - ``p_RequesterPaysEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-requesterpaysenabled
    - ``p_ResultConfigurationUpdates``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-resultconfigurationupdates
    """
    AWS_OBJECT_TYPE = "AWS::Athena::WorkGroup.WorkGroupConfigurationUpdates"
    
    p_BytesScannedCutoffPerQuery: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "BytesScannedCutoffPerQuery"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-bytesscannedcutoffperquery"""
    p_EnforceWorkGroupConfiguration: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EnforceWorkGroupConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-enforceworkgroupconfiguration"""
    p_EngineVersion: typing.Union['PropWorkGroupEngineVersion', dict] = attr.ib(
        default=None,
        converter=PropWorkGroupEngineVersion.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWorkGroupEngineVersion)),
        metadata={AttrMeta.PROPERTY_NAME: "EngineVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-engineversion"""
    p_PublishCloudWatchMetricsEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "PublishCloudWatchMetricsEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-publishcloudwatchmetricsenabled"""
    p_RemoveBytesScannedCutoffPerQuery: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "RemoveBytesScannedCutoffPerQuery"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-removebytesscannedcutoffperquery"""
    p_RequesterPaysEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "RequesterPaysEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-requesterpaysenabled"""
    p_ResultConfigurationUpdates: typing.Union['PropWorkGroupResultConfigurationUpdates', dict] = attr.ib(
        default=None,
        converter=PropWorkGroupResultConfigurationUpdates.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWorkGroupResultConfigurationUpdates)),
        metadata={AttrMeta.PROPERTY_NAME: "ResultConfigurationUpdates"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-resultconfigurationupdates"""


#--- Resource declaration ---

@attr.s
class DataCatalog(Resource):
    """
    AWS Object Type = "AWS::Athena::DataCatalog"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-name
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-type
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-description
    - ``p_Parameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-parameters
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-tags
    """
    AWS_OBJECT_TYPE = "AWS::Athena::DataCatalog"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-name"""
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-type"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-description"""
    p_Parameters: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type))),
        metadata={AttrMeta.PROPERTY_NAME: "Parameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-parameters"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-tags"""

    

@attr.s
class WorkGroup(Resource):
    """
    AWS Object Type = "AWS::Athena::WorkGroup"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-name
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-description
    - ``p_RecursiveDeleteOption``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-recursivedeleteoption
    - ``p_State``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-state
    - ``p_WorkGroupConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-workgroupconfiguration
    - ``p_WorkGroupConfigurationUpdates``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-workgroupconfigurationupdates
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-tags
    """
    AWS_OBJECT_TYPE = "AWS::Athena::WorkGroup"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-name"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-description"""
    p_RecursiveDeleteOption: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "RecursiveDeleteOption"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-recursivedeleteoption"""
    p_State: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "State"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-state"""
    p_WorkGroupConfiguration: typing.Union['PropWorkGroupWorkGroupConfiguration', dict] = attr.ib(
        default=None,
        converter=PropWorkGroupWorkGroupConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWorkGroupWorkGroupConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "WorkGroupConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-workgroupconfiguration"""
    p_WorkGroupConfigurationUpdates: typing.Union['PropWorkGroupWorkGroupConfigurationUpdates', dict] = attr.ib(
        default=None,
        converter=PropWorkGroupWorkGroupConfigurationUpdates.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWorkGroupWorkGroupConfigurationUpdates)),
        metadata={AttrMeta.PROPERTY_NAME: "WorkGroupConfigurationUpdates"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-workgroupconfigurationupdates"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-tags"""

    
    @property
    def rv_WorkGroupConfigurationEngineVersionEffectiveEngineVersion(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#aws-resource-athena-workgroup-return-values"""
        return GetAtt(resource=self, attr_name="WorkGroupConfiguration.EngineVersion.EffectiveEngineVersion")
    
    @property
    def rv_WorkGroupConfigurationUpdatesEngineVersionEffectiveEngineVersion(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#aws-resource-athena-workgroup-return-values"""
        return GetAtt(resource=self, attr_name="WorkGroupConfigurationUpdates.EngineVersion.EffectiveEngineVersion")
    
    @property
    def rv_CreationTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#aws-resource-athena-workgroup-return-values"""
        return GetAtt(resource=self, attr_name="CreationTime")
    

@attr.s
class PreparedStatement(Resource):
    """
    AWS Object Type = "AWS::Athena::PreparedStatement"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html

    Property Document:
    
    - ``rp_QueryStatement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html#cfn-athena-preparedstatement-querystatement
    - ``rp_StatementName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html#cfn-athena-preparedstatement-statementname
    - ``rp_WorkGroup``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html#cfn-athena-preparedstatement-workgroup
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html#cfn-athena-preparedstatement-description
    """
    AWS_OBJECT_TYPE = "AWS::Athena::PreparedStatement"

    
    rp_QueryStatement: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "QueryStatement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html#cfn-athena-preparedstatement-querystatement"""
    rp_StatementName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "StatementName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html#cfn-athena-preparedstatement-statementname"""
    rp_WorkGroup: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "WorkGroup"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html#cfn-athena-preparedstatement-workgroup"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html#cfn-athena-preparedstatement-description"""

    

@attr.s
class NamedQuery(Resource):
    """
    AWS Object Type = "AWS::Athena::NamedQuery"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html

    Property Document:
    
    - ``rp_Database``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-database
    - ``rp_QueryString``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-querystring
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-description
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-name
    - ``p_WorkGroup``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-workgroup
    """
    AWS_OBJECT_TYPE = "AWS::Athena::NamedQuery"

    
    rp_Database: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Database"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-database"""
    rp_QueryString: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "QueryString"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-querystring"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-description"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-name"""
    p_WorkGroup: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "WorkGroup"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-workgroup"""

    
    @property
    def rv_NamedQueryId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#aws-resource-athena-namedquery-return-values"""
        return GetAtt(resource=self, attr_name="NamedQueryId")
    
