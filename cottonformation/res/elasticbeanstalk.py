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
class PropEnvironmentOptionSetting(Property):
    """
    AWS Object Type = "AWS::ElasticBeanstalk::Environment.OptionSetting"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-option-settings.html

    Property Document:
    
    - ``rp_Namespace``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-option-settings.html#cfn-beanstalk-optionsettings-namespace
    - ``rp_OptionName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-option-settings.html#cfn-beanstalk-optionsettings-optionname
    - ``p_ResourceName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-option-settings.html#cfn-elasticbeanstalk-environment-optionsetting-resourcename
    - ``p_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-option-settings.html#cfn-beanstalk-optionsettings-value
    """
    AWS_OBJECT_TYPE = "AWS::ElasticBeanstalk::Environment.OptionSetting"
    
    rp_Namespace: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Namespace"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-option-settings.html#cfn-beanstalk-optionsettings-namespace"""
    rp_OptionName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "OptionName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-option-settings.html#cfn-beanstalk-optionsettings-optionname"""
    p_ResourceName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-option-settings.html#cfn-elasticbeanstalk-environment-optionsetting-resourcename"""
    p_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-option-settings.html#cfn-beanstalk-optionsettings-value"""

@attr.s
class PropApplicationVersionSourceBundle(Property):
    """
    AWS Object Type = "AWS::ElasticBeanstalk::ApplicationVersion.SourceBundle"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-sourcebundle.html

    Property Document:
    
    - ``rp_S3Bucket``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-sourcebundle.html#cfn-beanstalk-sourcebundle-s3bucket
    - ``rp_S3Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-sourcebundle.html#cfn-beanstalk-sourcebundle-s3key
    """
    AWS_OBJECT_TYPE = "AWS::ElasticBeanstalk::ApplicationVersion.SourceBundle"
    
    rp_S3Bucket: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "S3Bucket"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-sourcebundle.html#cfn-beanstalk-sourcebundle-s3bucket"""
    rp_S3Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "S3Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-sourcebundle.html#cfn-beanstalk-sourcebundle-s3key"""

@attr.s
class PropApplicationMaxAgeRule(Property):
    """
    AWS Object Type = "AWS::ElasticBeanstalk::Application.MaxAgeRule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxagerule.html

    Property Document:
    
    - ``p_DeleteSourceFromS3``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxagerule.html#cfn-elasticbeanstalk-application-maxagerule-deletesourcefroms3
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxagerule.html#cfn-elasticbeanstalk-application-maxagerule-enabled
    - ``p_MaxAgeInDays``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxagerule.html#cfn-elasticbeanstalk-application-maxagerule-maxageindays
    """
    AWS_OBJECT_TYPE = "AWS::ElasticBeanstalk::Application.MaxAgeRule"
    
    p_DeleteSourceFromS3: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "DeleteSourceFromS3"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxagerule.html#cfn-elasticbeanstalk-application-maxagerule-deletesourcefroms3"""
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxagerule.html#cfn-elasticbeanstalk-application-maxagerule-enabled"""
    p_MaxAgeInDays: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MaxAgeInDays"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxagerule.html#cfn-elasticbeanstalk-application-maxagerule-maxageindays"""

@attr.s
class PropConfigurationTemplateSourceConfiguration(Property):
    """
    AWS Object Type = "AWS::ElasticBeanstalk::ConfigurationTemplate.SourceConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-sourceconfiguration.html

    Property Document:
    
    - ``rp_ApplicationName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-sourceconfiguration.html#cfn-elasticbeanstalk-configurationtemplate-sourceconfiguration-applicationname
    - ``rp_TemplateName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-sourceconfiguration.html#cfn-elasticbeanstalk-configurationtemplate-sourceconfiguration-templatename
    """
    AWS_OBJECT_TYPE = "AWS::ElasticBeanstalk::ConfigurationTemplate.SourceConfiguration"
    
    rp_ApplicationName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-sourceconfiguration.html#cfn-elasticbeanstalk-configurationtemplate-sourceconfiguration-applicationname"""
    rp_TemplateName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TemplateName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-sourceconfiguration.html#cfn-elasticbeanstalk-configurationtemplate-sourceconfiguration-templatename"""

@attr.s
class PropEnvironmentTier(Property):
    """
    AWS Object Type = "AWS::ElasticBeanstalk::Environment.Tier"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment-tier.html

    Property Document:
    
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment-tier.html#cfn-beanstalk-env-tier-name
    - ``p_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment-tier.html#cfn-beanstalk-env-tier-type
    - ``p_Version``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment-tier.html#cfn-beanstalk-env-tier-version
    """
    AWS_OBJECT_TYPE = "AWS::ElasticBeanstalk::Environment.Tier"
    
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment-tier.html#cfn-beanstalk-env-tier-name"""
    p_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment-tier.html#cfn-beanstalk-env-tier-type"""
    p_Version: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Version"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment-tier.html#cfn-beanstalk-env-tier-version"""

@attr.s
class PropConfigurationTemplateConfigurationOptionSetting(Property):
    """
    AWS Object Type = "AWS::ElasticBeanstalk::ConfigurationTemplate.ConfigurationOptionSetting"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-configurationoptionsetting.html

    Property Document:
    
    - ``rp_Namespace``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-configurationoptionsetting.html#cfn-elasticbeanstalk-configurationtemplate-configurationoptionsetting-namespace
    - ``rp_OptionName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-configurationoptionsetting.html#cfn-elasticbeanstalk-configurationtemplate-configurationoptionsetting-optionname
    - ``p_ResourceName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-configurationoptionsetting.html#cfn-elasticbeanstalk-configurationtemplate-configurationoptionsetting-resourcename
    - ``p_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-configurationoptionsetting.html#cfn-elasticbeanstalk-configurationtemplate-configurationoptionsetting-value
    """
    AWS_OBJECT_TYPE = "AWS::ElasticBeanstalk::ConfigurationTemplate.ConfigurationOptionSetting"
    
    rp_Namespace: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Namespace"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-configurationoptionsetting.html#cfn-elasticbeanstalk-configurationtemplate-configurationoptionsetting-namespace"""
    rp_OptionName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "OptionName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-configurationoptionsetting.html#cfn-elasticbeanstalk-configurationtemplate-configurationoptionsetting-optionname"""
    p_ResourceName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-configurationoptionsetting.html#cfn-elasticbeanstalk-configurationtemplate-configurationoptionsetting-resourcename"""
    p_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-configurationoptionsetting.html#cfn-elasticbeanstalk-configurationtemplate-configurationoptionsetting-value"""

@attr.s
class PropApplicationMaxCountRule(Property):
    """
    AWS Object Type = "AWS::ElasticBeanstalk::Application.MaxCountRule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxcountrule.html

    Property Document:
    
    - ``p_DeleteSourceFromS3``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxcountrule.html#cfn-elasticbeanstalk-application-maxcountrule-deletesourcefroms3
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxcountrule.html#cfn-elasticbeanstalk-application-maxcountrule-enabled
    - ``p_MaxCount``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxcountrule.html#cfn-elasticbeanstalk-application-maxcountrule-maxcount
    """
    AWS_OBJECT_TYPE = "AWS::ElasticBeanstalk::Application.MaxCountRule"
    
    p_DeleteSourceFromS3: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "DeleteSourceFromS3"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxcountrule.html#cfn-elasticbeanstalk-application-maxcountrule-deletesourcefroms3"""
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxcountrule.html#cfn-elasticbeanstalk-application-maxcountrule-enabled"""
    p_MaxCount: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MaxCount"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxcountrule.html#cfn-elasticbeanstalk-application-maxcountrule-maxcount"""

@attr.s
class PropApplicationApplicationVersionLifecycleConfig(Property):
    """
    AWS Object Type = "AWS::ElasticBeanstalk::Application.ApplicationVersionLifecycleConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationversionlifecycleconfig.html

    Property Document:
    
    - ``p_MaxAgeRule``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationversionlifecycleconfig.html#cfn-elasticbeanstalk-application-applicationversionlifecycleconfig-maxagerule
    - ``p_MaxCountRule``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationversionlifecycleconfig.html#cfn-elasticbeanstalk-application-applicationversionlifecycleconfig-maxcountrule
    """
    AWS_OBJECT_TYPE = "AWS::ElasticBeanstalk::Application.ApplicationVersionLifecycleConfig"
    
    p_MaxAgeRule: typing.Union['PropApplicationMaxAgeRule', dict] = attr.ib(
        default=None,
        converter=PropApplicationMaxAgeRule.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationMaxAgeRule)),
        metadata={AttrMeta.PROPERTY_NAME: "MaxAgeRule"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationversionlifecycleconfig.html#cfn-elasticbeanstalk-application-applicationversionlifecycleconfig-maxagerule"""
    p_MaxCountRule: typing.Union['PropApplicationMaxCountRule', dict] = attr.ib(
        default=None,
        converter=PropApplicationMaxCountRule.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationMaxCountRule)),
        metadata={AttrMeta.PROPERTY_NAME: "MaxCountRule"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationversionlifecycleconfig.html#cfn-elasticbeanstalk-application-applicationversionlifecycleconfig-maxcountrule"""

@attr.s
class PropApplicationApplicationResourceLifecycleConfig(Property):
    """
    AWS Object Type = "AWS::ElasticBeanstalk::Application.ApplicationResourceLifecycleConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationresourcelifecycleconfig.html

    Property Document:
    
    - ``p_ServiceRole``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationresourcelifecycleconfig.html#cfn-elasticbeanstalk-application-applicationresourcelifecycleconfig-servicerole
    - ``p_VersionLifecycleConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationresourcelifecycleconfig.html#cfn-elasticbeanstalk-application-applicationresourcelifecycleconfig-versionlifecycleconfig
    """
    AWS_OBJECT_TYPE = "AWS::ElasticBeanstalk::Application.ApplicationResourceLifecycleConfig"
    
    p_ServiceRole: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ServiceRole"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationresourcelifecycleconfig.html#cfn-elasticbeanstalk-application-applicationresourcelifecycleconfig-servicerole"""
    p_VersionLifecycleConfig: typing.Union['PropApplicationApplicationVersionLifecycleConfig', dict] = attr.ib(
        default=None,
        converter=PropApplicationApplicationVersionLifecycleConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationApplicationVersionLifecycleConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "VersionLifecycleConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationresourcelifecycleconfig.html#cfn-elasticbeanstalk-application-applicationresourcelifecycleconfig-versionlifecycleconfig"""


#--- Resource declaration ---

@attr.s
class ConfigurationTemplate(Resource):
    """
    AWS Object Type = "AWS::ElasticBeanstalk::ConfigurationTemplate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html

    Property Document:
    
    - ``rp_ApplicationName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-applicationname
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-description
    - ``p_EnvironmentId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-environmentid
    - ``p_OptionSettings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-optionsettings
    - ``p_PlatformArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-platformarn
    - ``p_SolutionStackName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-solutionstackname
    - ``p_SourceConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-sourceconfiguration
    """
    AWS_OBJECT_TYPE = "AWS::ElasticBeanstalk::ConfigurationTemplate"

    
    rp_ApplicationName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-applicationname"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-description"""
    p_EnvironmentId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "EnvironmentId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-environmentid"""
    p_OptionSettings: typing.List[typing.Union['PropConfigurationTemplateConfigurationOptionSetting', dict]] = attr.ib(
        default=None,
        converter=PropConfigurationTemplateConfigurationOptionSetting.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropConfigurationTemplateConfigurationOptionSetting), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "OptionSettings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-optionsettings"""
    p_PlatformArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PlatformArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-platformarn"""
    p_SolutionStackName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SolutionStackName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-solutionstackname"""
    p_SourceConfiguration: typing.Union['PropConfigurationTemplateSourceConfiguration', dict] = attr.ib(
        default=None,
        converter=PropConfigurationTemplateSourceConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropConfigurationTemplateSourceConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "SourceConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-sourceconfiguration"""

    

@attr.s
class Environment(Resource):
    """
    AWS Object Type = "AWS::ElasticBeanstalk::Environment"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html

    Property Document:
    
    - ``rp_ApplicationName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-applicationname
    - ``p_CNAMEPrefix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-cnameprefix
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-description
    - ``p_EnvironmentName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-name
    - ``p_OperationsRole``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-operations-role
    - ``p_OptionSettings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-optionsettings
    - ``p_PlatformArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-platformarn
    - ``p_SolutionStackName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-solutionstackname
    - ``p_TemplateName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-templatename
    - ``p_Tier``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-tier
    - ``p_VersionLabel``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-versionlabel
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-elasticbeanstalk-environment-tags
    """
    AWS_OBJECT_TYPE = "AWS::ElasticBeanstalk::Environment"

    
    rp_ApplicationName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-applicationname"""
    p_CNAMEPrefix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CNAMEPrefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-cnameprefix"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-description"""
    p_EnvironmentName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "EnvironmentName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-name"""
    p_OperationsRole: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "OperationsRole"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-operations-role"""
    p_OptionSettings: typing.List[typing.Union['PropEnvironmentOptionSetting', dict]] = attr.ib(
        default=None,
        converter=PropEnvironmentOptionSetting.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropEnvironmentOptionSetting), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "OptionSettings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-optionsettings"""
    p_PlatformArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PlatformArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-platformarn"""
    p_SolutionStackName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SolutionStackName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-solutionstackname"""
    p_TemplateName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TemplateName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-templatename"""
    p_Tier: typing.Union['PropEnvironmentTier', dict] = attr.ib(
        default=None,
        converter=PropEnvironmentTier.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropEnvironmentTier)),
        metadata={AttrMeta.PROPERTY_NAME: "Tier"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-tier"""
    p_VersionLabel: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "VersionLabel"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-versionlabel"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-elasticbeanstalk-environment-tags"""

    
    @property
    def rv_EndpointURL(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#aws-properties-beanstalk-environment-return-values"""
        return GetAtt(resource=self, attr_name="EndpointURL")
    

@attr.s
class Application(Resource):
    """
    AWS Object Type = "AWS::ElasticBeanstalk::Application"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk.html

    Property Document:
    
    - ``p_ApplicationName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk.html#cfn-elasticbeanstalk-application-name
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk.html#cfn-elasticbeanstalk-application-description
    - ``p_ResourceLifecycleConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk.html#cfn-elasticbeanstalk-application-resourcelifecycleconfig
    """
    AWS_OBJECT_TYPE = "AWS::ElasticBeanstalk::Application"

    
    p_ApplicationName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk.html#cfn-elasticbeanstalk-application-name"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk.html#cfn-elasticbeanstalk-application-description"""
    p_ResourceLifecycleConfig: typing.Union['PropApplicationApplicationResourceLifecycleConfig', dict] = attr.ib(
        default=None,
        converter=PropApplicationApplicationResourceLifecycleConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationApplicationResourceLifecycleConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceLifecycleConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk.html#cfn-elasticbeanstalk-application-resourcelifecycleconfig"""

    

@attr.s
class ApplicationVersion(Resource):
    """
    AWS Object Type = "AWS::ElasticBeanstalk::ApplicationVersion"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-version.html

    Property Document:
    
    - ``rp_ApplicationName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-version.html#cfn-elasticbeanstalk-applicationversion-applicationname
    - ``rp_SourceBundle``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-version.html#cfn-elasticbeanstalk-applicationversion-sourcebundle
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-version.html#cfn-elasticbeanstalk-applicationversion-description
    """
    AWS_OBJECT_TYPE = "AWS::ElasticBeanstalk::ApplicationVersion"

    
    rp_ApplicationName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-version.html#cfn-elasticbeanstalk-applicationversion-applicationname"""
    rp_SourceBundle: typing.Union['PropApplicationVersionSourceBundle', dict] = attr.ib(
        default=None,
        converter=PropApplicationVersionSourceBundle.from_dict,
        validator=attr.validators.instance_of(PropApplicationVersionSourceBundle),
        metadata={AttrMeta.PROPERTY_NAME: "SourceBundle"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-version.html#cfn-elasticbeanstalk-applicationversion-sourcebundle"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-version.html#cfn-elasticbeanstalk-applicationversion-description"""

    
