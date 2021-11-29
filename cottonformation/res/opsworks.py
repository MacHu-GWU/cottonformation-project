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
class PropLayerShutdownEventConfiguration(Property):
    """
    AWS Object Type = "AWS::OpsWorks::Layer.ShutdownEventConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-lifecycleeventconfiguration-shutdowneventconfiguration.html

    Property Document:
    
    - ``p_DelayUntilElbConnectionsDrained``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-lifecycleeventconfiguration-shutdowneventconfiguration.html#cfn-opsworks-layer-lifecycleconfiguration-shutdowneventconfiguration-delayuntilelbconnectionsdrained
    - ``p_ExecutionTimeout``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-lifecycleeventconfiguration-shutdowneventconfiguration.html#cfn-opsworks-layer-lifecycleconfiguration-shutdowneventconfiguration-executiontimeout
    """
    AWS_OBJECT_TYPE = "AWS::OpsWorks::Layer.ShutdownEventConfiguration"
    
    p_DelayUntilElbConnectionsDrained: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "DelayUntilElbConnectionsDrained"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-lifecycleeventconfiguration-shutdowneventconfiguration.html#cfn-opsworks-layer-lifecycleconfiguration-shutdowneventconfiguration-delayuntilelbconnectionsdrained"""
    p_ExecutionTimeout: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ExecutionTimeout"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-lifecycleeventconfiguration-shutdowneventconfiguration.html#cfn-opsworks-layer-lifecycleconfiguration-shutdowneventconfiguration-executiontimeout"""

@attr.s
class PropAppDataSource(Property):
    """
    AWS Object Type = "AWS::OpsWorks::App.DataSource"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-datasource.html

    Property Document:
    
    - ``p_Arn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-datasource.html#cfn-opsworks-app-datasource-arn
    - ``p_DatabaseName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-datasource.html#cfn-opsworks-app-datasource-databasename
    - ``p_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-datasource.html#cfn-opsworks-app-datasource-type
    """
    AWS_OBJECT_TYPE = "AWS::OpsWorks::App.DataSource"
    
    p_Arn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Arn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-datasource.html#cfn-opsworks-app-datasource-arn"""
    p_DatabaseName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DatabaseName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-datasource.html#cfn-opsworks-app-datasource-databasename"""
    p_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-datasource.html#cfn-opsworks-app-datasource-type"""

@attr.s
class PropLayerVolumeConfiguration(Property):
    """
    AWS Object Type = "AWS::OpsWorks::Layer.VolumeConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html

    Property Document:
    
    - ``p_Encrypted``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volumeconfiguration-encrypted
    - ``p_Iops``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volconfig-iops
    - ``p_MountPoint``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volconfig-mountpoint
    - ``p_NumberOfDisks``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volconfig-numberofdisks
    - ``p_RaidLevel``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volconfig-raidlevel
    - ``p_Size``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volconfig-size
    - ``p_VolumeType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volconfig-volumetype
    """
    AWS_OBJECT_TYPE = "AWS::OpsWorks::Layer.VolumeConfiguration"
    
    p_Encrypted: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Encrypted"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volumeconfiguration-encrypted"""
    p_Iops: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Iops"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volconfig-iops"""
    p_MountPoint: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MountPoint"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volconfig-mountpoint"""
    p_NumberOfDisks: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "NumberOfDisks"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volconfig-numberofdisks"""
    p_RaidLevel: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "RaidLevel"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volconfig-raidlevel"""
    p_Size: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Size"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volconfig-size"""
    p_VolumeType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "VolumeType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volconfig-volumetype"""

@attr.s
class PropStackStackConfigurationManager(Property):
    """
    AWS Object Type = "AWS::OpsWorks::Stack.StackConfigurationManager"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-stackconfigmanager.html

    Property Document:
    
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-stackconfigmanager.html#cfn-opsworks-configmanager-name
    - ``p_Version``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-stackconfigmanager.html#cfn-opsworks-configmanager-version
    """
    AWS_OBJECT_TYPE = "AWS::OpsWorks::Stack.StackConfigurationManager"
    
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-stackconfigmanager.html#cfn-opsworks-configmanager-name"""
    p_Version: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Version"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-stackconfigmanager.html#cfn-opsworks-configmanager-version"""

@attr.s
class PropStackRdsDbInstance(Property):
    """
    AWS Object Type = "AWS::OpsWorks::Stack.RdsDbInstance"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-rdsdbinstance.html

    Property Document:
    
    - ``rp_DbPassword``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-rdsdbinstance.html#cfn-opsworks-stack-rdsdbinstance-dbpassword
    - ``rp_DbUser``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-rdsdbinstance.html#cfn-opsworks-stack-rdsdbinstance-dbuser
    - ``rp_RdsDbInstanceArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-rdsdbinstance.html#cfn-opsworks-stack-rdsdbinstance-rdsdbinstancearn
    """
    AWS_OBJECT_TYPE = "AWS::OpsWorks::Stack.RdsDbInstance"
    
    rp_DbPassword: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DbPassword"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-rdsdbinstance.html#cfn-opsworks-stack-rdsdbinstance-dbpassword"""
    rp_DbUser: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DbUser"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-rdsdbinstance.html#cfn-opsworks-stack-rdsdbinstance-dbuser"""
    rp_RdsDbInstanceArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RdsDbInstanceArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-rdsdbinstance.html#cfn-opsworks-stack-rdsdbinstance-rdsdbinstancearn"""

@attr.s
class PropStackSource(Property):
    """
    AWS Object Type = "AWS::OpsWorks::Stack.Source"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html

    Property Document:
    
    - ``p_Password``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-password
    - ``p_Revision``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-revision
    - ``p_SshKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-sshkey
    - ``p_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-type
    - ``p_Url``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-url
    - ``p_Username``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-username
    """
    AWS_OBJECT_TYPE = "AWS::OpsWorks::Stack.Source"
    
    p_Password: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Password"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-password"""
    p_Revision: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Revision"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-revision"""
    p_SshKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SshKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-sshkey"""
    p_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-type"""
    p_Url: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Url"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-url"""
    p_Username: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Username"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-username"""

@attr.s
class PropStackChefConfiguration(Property):
    """
    AWS Object Type = "AWS::OpsWorks::Stack.ChefConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-chefconfiguration.html

    Property Document:
    
    - ``p_BerkshelfVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-chefconfiguration.html#cfn-opsworks-chefconfiguration-berkshelfversion
    - ``p_ManageBerkshelf``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-chefconfiguration.html#cfn-opsworks-chefconfiguration-berkshelfversion
    """
    AWS_OBJECT_TYPE = "AWS::OpsWorks::Stack.ChefConfiguration"
    
    p_BerkshelfVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BerkshelfVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-chefconfiguration.html#cfn-opsworks-chefconfiguration-berkshelfversion"""
    p_ManageBerkshelf: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "ManageBerkshelf"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-chefconfiguration.html#cfn-opsworks-chefconfiguration-berkshelfversion"""

@attr.s
class PropAppSslConfiguration(Property):
    """
    AWS Object Type = "AWS::OpsWorks::App.SslConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-sslconfiguration.html

    Property Document:
    
    - ``p_Certificate``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-sslconfiguration.html#cfn-opsworks-app-sslconfig-certificate
    - ``p_Chain``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-sslconfiguration.html#cfn-opsworks-app-sslconfig-chain
    - ``p_PrivateKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-sslconfiguration.html#cfn-opsworks-app-sslconfig-privatekey
    """
    AWS_OBJECT_TYPE = "AWS::OpsWorks::App.SslConfiguration"
    
    p_Certificate: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Certificate"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-sslconfiguration.html#cfn-opsworks-app-sslconfig-certificate"""
    p_Chain: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Chain"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-sslconfiguration.html#cfn-opsworks-app-sslconfig-chain"""
    p_PrivateKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PrivateKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-sslconfiguration.html#cfn-opsworks-app-sslconfig-privatekey"""

@attr.s
class PropLayerRecipes(Property):
    """
    AWS Object Type = "AWS::OpsWorks::Layer.Recipes"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-recipes.html

    Property Document:
    
    - ``p_Configure``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-recipes.html#cfn-opsworks-layer-customrecipes-configure
    - ``p_Deploy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-recipes.html#cfn-opsworks-layer-customrecipes-deploy
    - ``p_Setup``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-recipes.html#cfn-opsworks-layer-customrecipes-setup
    - ``p_Shutdown``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-recipes.html#cfn-opsworks-layer-customrecipes-shutdown
    - ``p_Undeploy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-recipes.html#cfn-opsworks-layer-customrecipes-undeploy
    """
    AWS_OBJECT_TYPE = "AWS::OpsWorks::Layer.Recipes"
    
    p_Configure: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Configure"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-recipes.html#cfn-opsworks-layer-customrecipes-configure"""
    p_Deploy: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Deploy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-recipes.html#cfn-opsworks-layer-customrecipes-deploy"""
    p_Setup: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Setup"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-recipes.html#cfn-opsworks-layer-customrecipes-setup"""
    p_Shutdown: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Shutdown"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-recipes.html#cfn-opsworks-layer-customrecipes-shutdown"""
    p_Undeploy: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Undeploy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-recipes.html#cfn-opsworks-layer-customrecipes-undeploy"""

@attr.s
class PropInstanceTimeBasedAutoScaling(Property):
    """
    AWS Object Type = "AWS::OpsWorks::Instance.TimeBasedAutoScaling"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html

    Property Document:
    
    - ``p_Friday``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-friday
    - ``p_Monday``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-monday
    - ``p_Saturday``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-saturday
    - ``p_Sunday``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-sunday
    - ``p_Thursday``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-thursday
    - ``p_Tuesday``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-tuesday
    - ``p_Wednesday``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-wednesday
    """
    AWS_OBJECT_TYPE = "AWS::OpsWorks::Instance.TimeBasedAutoScaling"
    
    p_Friday: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type))),
        metadata={AttrMeta.PROPERTY_NAME: "Friday"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-friday"""
    p_Monday: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type))),
        metadata={AttrMeta.PROPERTY_NAME: "Monday"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-monday"""
    p_Saturday: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type))),
        metadata={AttrMeta.PROPERTY_NAME: "Saturday"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-saturday"""
    p_Sunday: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type))),
        metadata={AttrMeta.PROPERTY_NAME: "Sunday"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-sunday"""
    p_Thursday: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type))),
        metadata={AttrMeta.PROPERTY_NAME: "Thursday"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-thursday"""
    p_Tuesday: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type))),
        metadata={AttrMeta.PROPERTY_NAME: "Tuesday"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-tuesday"""
    p_Wednesday: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type))),
        metadata={AttrMeta.PROPERTY_NAME: "Wednesday"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-wednesday"""

@attr.s
class PropAppEnvironmentVariable(Property):
    """
    AWS Object Type = "AWS::OpsWorks::App.EnvironmentVariable"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-environment.html

    Property Document:
    
    - ``rp_Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-environment.html#cfn-opsworks-app-environment-key
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-environment.html#value
    - ``p_Secure``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-environment.html#cfn-opsworks-app-environment-secure
    """
    AWS_OBJECT_TYPE = "AWS::OpsWorks::App.EnvironmentVariable"
    
    rp_Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-environment.html#cfn-opsworks-app-environment-key"""
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-environment.html#value"""
    p_Secure: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Secure"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-environment.html#cfn-opsworks-app-environment-secure"""

@attr.s
class PropInstanceEbsBlockDevice(Property):
    """
    AWS Object Type = "AWS::OpsWorks::Instance.EbsBlockDevice"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-ebsblockdevice.html

    Property Document:
    
    - ``p_DeleteOnTermination``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-ebsblockdevice.html#cfn-opsworks-instance-ebsblockdevice-deleteontermination
    - ``p_Iops``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-ebsblockdevice.html#cfn-opsworks-instance-ebsblockdevice-iops
    - ``p_SnapshotId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-ebsblockdevice.html#cfn-opsworks-instance-ebsblockdevice-snapshotid
    - ``p_VolumeSize``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-ebsblockdevice.html#cfn-opsworks-instance-ebsblockdevice-volumesize
    - ``p_VolumeType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-ebsblockdevice.html#cfn-opsworks-instance-ebsblockdevice-volumetype
    """
    AWS_OBJECT_TYPE = "AWS::OpsWorks::Instance.EbsBlockDevice"
    
    p_DeleteOnTermination: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "DeleteOnTermination"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-ebsblockdevice.html#cfn-opsworks-instance-ebsblockdevice-deleteontermination"""
    p_Iops: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Iops"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-ebsblockdevice.html#cfn-opsworks-instance-ebsblockdevice-iops"""
    p_SnapshotId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SnapshotId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-ebsblockdevice.html#cfn-opsworks-instance-ebsblockdevice-snapshotid"""
    p_VolumeSize: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "VolumeSize"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-ebsblockdevice.html#cfn-opsworks-instance-ebsblockdevice-volumesize"""
    p_VolumeType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "VolumeType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-ebsblockdevice.html#cfn-opsworks-instance-ebsblockdevice-volumetype"""

@attr.s
class PropLayerLifecycleEventConfiguration(Property):
    """
    AWS Object Type = "AWS::OpsWorks::Layer.LifecycleEventConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-lifecycleeventconfiguration.html

    Property Document:
    
    - ``p_ShutdownEventConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-lifecycleeventconfiguration.html#cfn-opsworks-layer-lifecycleconfiguration-shutdowneventconfiguration
    """
    AWS_OBJECT_TYPE = "AWS::OpsWorks::Layer.LifecycleEventConfiguration"
    
    p_ShutdownEventConfiguration: typing.Union['PropLayerShutdownEventConfiguration', dict] = attr.ib(
        default=None,
        converter=PropLayerShutdownEventConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropLayerShutdownEventConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "ShutdownEventConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-lifecycleeventconfiguration.html#cfn-opsworks-layer-lifecycleconfiguration-shutdowneventconfiguration"""

@attr.s
class PropLayerAutoScalingThresholds(Property):
    """
    AWS Object Type = "AWS::OpsWorks::Layer.AutoScalingThresholds"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling-autoscalingthresholds.html

    Property Document:
    
    - ``p_CpuThreshold``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling-autoscalingthresholds.html#cfn-opsworks-layer-loadbasedautoscaling-autoscalingthresholds-cputhreshold
    - ``p_IgnoreMetricsTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling-autoscalingthresholds.html#cfn-opsworks-layer-loadbasedautoscaling-autoscalingthresholds-ignoremetricstime
    - ``p_InstanceCount``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling-autoscalingthresholds.html#cfn-opsworks-layer-loadbasedautoscaling-autoscalingthresholds-instancecount
    - ``p_LoadThreshold``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling-autoscalingthresholds.html#cfn-opsworks-layer-loadbasedautoscaling-autoscalingthresholds-loadthreshold
    - ``p_MemoryThreshold``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling-autoscalingthresholds.html#cfn-opsworks-layer-loadbasedautoscaling-autoscalingthresholds-memorythreshold
    - ``p_ThresholdsWaitTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling-autoscalingthresholds.html#cfn-opsworks-layer-loadbasedautoscaling-autoscalingthresholds-thresholdwaittime
    """
    AWS_OBJECT_TYPE = "AWS::OpsWorks::Layer.AutoScalingThresholds"
    
    p_CpuThreshold: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "CpuThreshold"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling-autoscalingthresholds.html#cfn-opsworks-layer-loadbasedautoscaling-autoscalingthresholds-cputhreshold"""
    p_IgnoreMetricsTime: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "IgnoreMetricsTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling-autoscalingthresholds.html#cfn-opsworks-layer-loadbasedautoscaling-autoscalingthresholds-ignoremetricstime"""
    p_InstanceCount: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "InstanceCount"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling-autoscalingthresholds.html#cfn-opsworks-layer-loadbasedautoscaling-autoscalingthresholds-instancecount"""
    p_LoadThreshold: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "LoadThreshold"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling-autoscalingthresholds.html#cfn-opsworks-layer-loadbasedautoscaling-autoscalingthresholds-loadthreshold"""
    p_MemoryThreshold: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "MemoryThreshold"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling-autoscalingthresholds.html#cfn-opsworks-layer-loadbasedautoscaling-autoscalingthresholds-memorythreshold"""
    p_ThresholdsWaitTime: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ThresholdsWaitTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling-autoscalingthresholds.html#cfn-opsworks-layer-loadbasedautoscaling-autoscalingthresholds-thresholdwaittime"""

@attr.s
class PropStackElasticIp(Property):
    """
    AWS Object Type = "AWS::OpsWorks::Stack.ElasticIp"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-elasticip.html

    Property Document:
    
    - ``rp_Ip``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-elasticip.html#cfn-opsworks-stack-elasticip-ip
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-elasticip.html#cfn-opsworks-stack-elasticip-name
    """
    AWS_OBJECT_TYPE = "AWS::OpsWorks::Stack.ElasticIp"
    
    rp_Ip: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Ip"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-elasticip.html#cfn-opsworks-stack-elasticip-ip"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-elasticip.html#cfn-opsworks-stack-elasticip-name"""

@attr.s
class PropAppSource(Property):
    """
    AWS Object Type = "AWS::OpsWorks::App.Source"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html

    Property Document:
    
    - ``p_Password``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-pw
    - ``p_Revision``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-revision
    - ``p_SshKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-sshkey
    - ``p_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-type
    - ``p_Url``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-url
    - ``p_Username``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-username
    """
    AWS_OBJECT_TYPE = "AWS::OpsWorks::App.Source"
    
    p_Password: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Password"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-pw"""
    p_Revision: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Revision"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-revision"""
    p_SshKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SshKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-sshkey"""
    p_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-type"""
    p_Url: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Url"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-url"""
    p_Username: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Username"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-username"""

@attr.s
class PropInstanceBlockDeviceMapping(Property):
    """
    AWS Object Type = "AWS::OpsWorks::Instance.BlockDeviceMapping"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-blockdevicemapping.html

    Property Document:
    
    - ``p_DeviceName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-blockdevicemapping.html#cfn-opsworks-instance-blockdevicemapping-devicename
    - ``p_Ebs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-blockdevicemapping.html#cfn-opsworks-instance-blockdevicemapping-ebs
    - ``p_NoDevice``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-blockdevicemapping.html#cfn-opsworks-instance-blockdevicemapping-nodevice
    - ``p_VirtualName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-blockdevicemapping.html#cfn-opsworks-instance-blockdevicemapping-virtualname
    """
    AWS_OBJECT_TYPE = "AWS::OpsWorks::Instance.BlockDeviceMapping"
    
    p_DeviceName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DeviceName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-blockdevicemapping.html#cfn-opsworks-instance-blockdevicemapping-devicename"""
    p_Ebs: typing.Union['PropInstanceEbsBlockDevice', dict] = attr.ib(
        default=None,
        converter=PropInstanceEbsBlockDevice.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropInstanceEbsBlockDevice)),
        metadata={AttrMeta.PROPERTY_NAME: "Ebs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-blockdevicemapping.html#cfn-opsworks-instance-blockdevicemapping-ebs"""
    p_NoDevice: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "NoDevice"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-blockdevicemapping.html#cfn-opsworks-instance-blockdevicemapping-nodevice"""
    p_VirtualName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "VirtualName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-blockdevicemapping.html#cfn-opsworks-instance-blockdevicemapping-virtualname"""

@attr.s
class PropLayerLoadBasedAutoScaling(Property):
    """
    AWS Object Type = "AWS::OpsWorks::Layer.LoadBasedAutoScaling"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling.html

    Property Document:
    
    - ``p_DownScaling``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling.html#cfn-opsworks-layer-loadbasedautoscaling-downscaling
    - ``p_Enable``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling.html#cfn-opsworks-layer-loadbasedautoscaling-enable
    - ``p_UpScaling``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling.html#cfn-opsworks-layer-loadbasedautoscaling-upscaling
    """
    AWS_OBJECT_TYPE = "AWS::OpsWorks::Layer.LoadBasedAutoScaling"
    
    p_DownScaling: typing.Union['PropLayerAutoScalingThresholds', dict] = attr.ib(
        default=None,
        converter=PropLayerAutoScalingThresholds.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropLayerAutoScalingThresholds)),
        metadata={AttrMeta.PROPERTY_NAME: "DownScaling"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling.html#cfn-opsworks-layer-loadbasedautoscaling-downscaling"""
    p_Enable: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enable"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling.html#cfn-opsworks-layer-loadbasedautoscaling-enable"""
    p_UpScaling: typing.Union['PropLayerAutoScalingThresholds', dict] = attr.ib(
        default=None,
        converter=PropLayerAutoScalingThresholds.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropLayerAutoScalingThresholds)),
        metadata={AttrMeta.PROPERTY_NAME: "UpScaling"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling.html#cfn-opsworks-layer-loadbasedautoscaling-upscaling"""


#--- Resource declaration ---

@attr.s
class UserProfile(Resource):
    """
    AWS Object Type = "AWS::OpsWorks::UserProfile"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html

    Property Document:
    
    - ``rp_IamUserArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html#cfn-opsworks-userprofile-iamuserarn
    - ``p_AllowSelfManagement``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html#cfn-opsworks-userprofile-allowselfmanagement
    - ``p_SshPublicKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html#cfn-opsworks-userprofile-sshpublickey
    - ``p_SshUsername``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html#cfn-opsworks-userprofile-sshusername
    """
    AWS_OBJECT_TYPE = "AWS::OpsWorks::UserProfile"

    
    rp_IamUserArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "IamUserArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html#cfn-opsworks-userprofile-iamuserarn"""
    p_AllowSelfManagement: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "AllowSelfManagement"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html#cfn-opsworks-userprofile-allowselfmanagement"""
    p_SshPublicKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SshPublicKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html#cfn-opsworks-userprofile-sshpublickey"""
    p_SshUsername: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SshUsername"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html#cfn-opsworks-userprofile-sshusername"""

    
    @property
    def rv_SshUsername(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html#aws-resource-opsworks-userprofile-return-values"""
        return GetAtt(resource=self, attr_name="SshUsername")
    

@attr.s
class Volume(Resource):
    """
    AWS Object Type = "AWS::OpsWorks::Volume"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html

    Property Document:
    
    - ``rp_Ec2VolumeId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html#cfn-opsworks-volume-ec2volumeid
    - ``rp_StackId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html#cfn-opsworks-volume-stackid
    - ``p_MountPoint``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html#cfn-opsworks-volume-mountpoint
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html#cfn-opsworks-volume-name
    """
    AWS_OBJECT_TYPE = "AWS::OpsWorks::Volume"

    
    rp_Ec2VolumeId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Ec2VolumeId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html#cfn-opsworks-volume-ec2volumeid"""
    rp_StackId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "StackId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html#cfn-opsworks-volume-stackid"""
    p_MountPoint: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MountPoint"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html#cfn-opsworks-volume-mountpoint"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html#cfn-opsworks-volume-name"""

    

@attr.s
class App(Resource):
    """
    AWS Object Type = "AWS::OpsWorks::App"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-name
    - ``rp_StackId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-stackid
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-type
    - ``p_AppSource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-appsource
    - ``p_Attributes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-attributes
    - ``p_DataSources``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-datasources
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-description
    - ``p_Domains``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-domains
    - ``p_EnableSsl``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-enablessl
    - ``p_Environment``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-environment
    - ``p_Shortname``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-shortname
    - ``p_SslConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-sslconfiguration
    """
    AWS_OBJECT_TYPE = "AWS::OpsWorks::App"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-name"""
    rp_StackId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "StackId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-stackid"""
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-type"""
    p_AppSource: typing.Union['PropAppSource', dict] = attr.ib(
        default=None,
        converter=PropAppSource.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropAppSource)),
        metadata={AttrMeta.PROPERTY_NAME: "AppSource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-appsource"""
    p_Attributes: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type))),
        metadata={AttrMeta.PROPERTY_NAME: "Attributes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-attributes"""
    p_DataSources: typing.List[typing.Union['PropAppDataSource', dict]] = attr.ib(
        default=None,
        converter=PropAppDataSource.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropAppDataSource), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "DataSources"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-datasources"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-description"""
    p_Domains: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Domains"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-domains"""
    p_EnableSsl: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EnableSsl"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-enablessl"""
    p_Environment: typing.List[typing.Union['PropAppEnvironmentVariable', dict]] = attr.ib(
        default=None,
        converter=PropAppEnvironmentVariable.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropAppEnvironmentVariable), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Environment"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-environment"""
    p_Shortname: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Shortname"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-shortname"""
    p_SslConfiguration: typing.Union['PropAppSslConfiguration', dict] = attr.ib(
        default=None,
        converter=PropAppSslConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropAppSslConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "SslConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-sslconfiguration"""

    

@attr.s
class ElasticLoadBalancerAttachment(Resource):
    """
    AWS Object Type = "AWS::OpsWorks::ElasticLoadBalancerAttachment"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-elbattachment.html

    Property Document:
    
    - ``rp_ElasticLoadBalancerName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-elbattachment.html#cfn-opsworks-elbattachment-elbname
    - ``rp_LayerId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-elbattachment.html#cfn-opsworks-elbattachment-layerid
    """
    AWS_OBJECT_TYPE = "AWS::OpsWorks::ElasticLoadBalancerAttachment"

    
    rp_ElasticLoadBalancerName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ElasticLoadBalancerName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-elbattachment.html#cfn-opsworks-elbattachment-elbname"""
    rp_LayerId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "LayerId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-elbattachment.html#cfn-opsworks-elbattachment-layerid"""

    

@attr.s
class Instance(Resource):
    """
    AWS Object Type = "AWS::OpsWorks::Instance"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html

    Property Document:
    
    - ``rp_InstanceType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-instancetype
    - ``rp_LayerIds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-layerids
    - ``rp_StackId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-stackid
    - ``p_AgentVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-agentversion
    - ``p_AmiId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-amiid
    - ``p_Architecture``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-architecture
    - ``p_AutoScalingType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-autoscalingtype
    - ``p_AvailabilityZone``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-availabilityzone
    - ``p_BlockDeviceMappings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-blockdevicemappings
    - ``p_EbsOptimized``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-ebsoptimized
    - ``p_ElasticIps``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-elasticips
    - ``p_Hostname``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-hostname
    - ``p_InstallUpdatesOnBoot``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-installupdatesonboot
    - ``p_Os``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-os
    - ``p_RootDeviceType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-rootdevicetype
    - ``p_SshKeyName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-sshkeyname
    - ``p_SubnetId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-subnetid
    - ``p_Tenancy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-tenancy
    - ``p_TimeBasedAutoScaling``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-timebasedautoscaling
    - ``p_VirtualizationType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-virtualizationtype
    - ``p_Volumes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-volumes
    """
    AWS_OBJECT_TYPE = "AWS::OpsWorks::Instance"

    
    rp_InstanceType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "InstanceType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-instancetype"""
    rp_LayerIds: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "LayerIds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-layerids"""
    rp_StackId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "StackId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-stackid"""
    p_AgentVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AgentVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-agentversion"""
    p_AmiId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AmiId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-amiid"""
    p_Architecture: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Architecture"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-architecture"""
    p_AutoScalingType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AutoScalingType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-autoscalingtype"""
    p_AvailabilityZone: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AvailabilityZone"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-availabilityzone"""
    p_BlockDeviceMappings: typing.List[typing.Union['PropInstanceBlockDeviceMapping', dict]] = attr.ib(
        default=None,
        converter=PropInstanceBlockDeviceMapping.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropInstanceBlockDeviceMapping), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "BlockDeviceMappings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-blockdevicemappings"""
    p_EbsOptimized: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EbsOptimized"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-ebsoptimized"""
    p_ElasticIps: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ElasticIps"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-elasticips"""
    p_Hostname: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Hostname"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-hostname"""
    p_InstallUpdatesOnBoot: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "InstallUpdatesOnBoot"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-installupdatesonboot"""
    p_Os: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Os"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-os"""
    p_RootDeviceType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RootDeviceType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-rootdevicetype"""
    p_SshKeyName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SshKeyName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-sshkeyname"""
    p_SubnetId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SubnetId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-subnetid"""
    p_Tenancy: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Tenancy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-tenancy"""
    p_TimeBasedAutoScaling: typing.Union['PropInstanceTimeBasedAutoScaling', dict] = attr.ib(
        default=None,
        converter=PropInstanceTimeBasedAutoScaling.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropInstanceTimeBasedAutoScaling)),
        metadata={AttrMeta.PROPERTY_NAME: "TimeBasedAutoScaling"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-timebasedautoscaling"""
    p_VirtualizationType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "VirtualizationType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-virtualizationtype"""
    p_Volumes: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Volumes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-volumes"""

    
    @property
    def rv_AvailabilityZone(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#aws-resource-opsworks-instance-return-values"""
        return GetAtt(resource=self, attr_name="AvailabilityZone")
    
    @property
    def rv_PrivateDnsName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#aws-resource-opsworks-instance-return-values"""
        return GetAtt(resource=self, attr_name="PrivateDnsName")
    
    @property
    def rv_PrivateIp(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#aws-resource-opsworks-instance-return-values"""
        return GetAtt(resource=self, attr_name="PrivateIp")
    
    @property
    def rv_PublicDnsName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#aws-resource-opsworks-instance-return-values"""
        return GetAtt(resource=self, attr_name="PublicDnsName")
    
    @property
    def rv_PublicIp(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#aws-resource-opsworks-instance-return-values"""
        return GetAtt(resource=self, attr_name="PublicIp")
    

@attr.s
class Layer(Resource):
    """
    AWS Object Type = "AWS::OpsWorks::Layer"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html

    Property Document:
    
    - ``rp_AutoAssignElasticIps``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-autoassignelasticips
    - ``rp_AutoAssignPublicIps``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-autoassignpublicips
    - ``rp_EnableAutoHealing``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-enableautohealing
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-name
    - ``rp_Shortname``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-shortname
    - ``rp_StackId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-stackid
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-type
    - ``p_Attributes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-attributes
    - ``p_CustomInstanceProfileArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-custominstanceprofilearn
    - ``p_CustomJson``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-customjson
    - ``p_CustomRecipes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-customrecipes
    - ``p_CustomSecurityGroupIds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-customsecuritygroupids
    - ``p_InstallUpdatesOnBoot``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-installupdatesonboot
    - ``p_LifecycleEventConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-lifecycleeventconfiguration
    - ``p_LoadBasedAutoScaling``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-loadbasedautoscaling
    - ``p_Packages``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-packages
    - ``p_UseEbsOptimizedInstances``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-useebsoptimizedinstances
    - ``p_VolumeConfigurations``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-volumeconfigurations
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-tags
    """
    AWS_OBJECT_TYPE = "AWS::OpsWorks::Layer"

    
    rp_AutoAssignElasticIps: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "AutoAssignElasticIps"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-autoassignelasticips"""
    rp_AutoAssignPublicIps: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "AutoAssignPublicIps"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-autoassignpublicips"""
    rp_EnableAutoHealing: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "EnableAutoHealing"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-enableautohealing"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-name"""
    rp_Shortname: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Shortname"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-shortname"""
    rp_StackId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "StackId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-stackid"""
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-type"""
    p_Attributes: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type))),
        metadata={AttrMeta.PROPERTY_NAME: "Attributes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-attributes"""
    p_CustomInstanceProfileArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomInstanceProfileArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-custominstanceprofilearn"""
    p_CustomJson: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomJson"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-customjson"""
    p_CustomRecipes: typing.Union['PropLayerRecipes', dict] = attr.ib(
        default=None,
        converter=PropLayerRecipes.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropLayerRecipes)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomRecipes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-customrecipes"""
    p_CustomSecurityGroupIds: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "CustomSecurityGroupIds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-customsecuritygroupids"""
    p_InstallUpdatesOnBoot: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "InstallUpdatesOnBoot"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-installupdatesonboot"""
    p_LifecycleEventConfiguration: typing.Union['PropLayerLifecycleEventConfiguration', dict] = attr.ib(
        default=None,
        converter=PropLayerLifecycleEventConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropLayerLifecycleEventConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "LifecycleEventConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-lifecycleeventconfiguration"""
    p_LoadBasedAutoScaling: typing.Union['PropLayerLoadBasedAutoScaling', dict] = attr.ib(
        default=None,
        converter=PropLayerLoadBasedAutoScaling.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropLayerLoadBasedAutoScaling)),
        metadata={AttrMeta.PROPERTY_NAME: "LoadBasedAutoScaling"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-loadbasedautoscaling"""
    p_Packages: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Packages"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-packages"""
    p_UseEbsOptimizedInstances: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "UseEbsOptimizedInstances"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-useebsoptimizedinstances"""
    p_VolumeConfigurations: typing.List[typing.Union['PropLayerVolumeConfiguration', dict]] = attr.ib(
        default=None,
        converter=PropLayerVolumeConfiguration.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropLayerVolumeConfiguration), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "VolumeConfigurations"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-volumeconfigurations"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-tags"""

    

@attr.s
class Stack(Resource):
    """
    AWS Object Type = "AWS::OpsWorks::Stack"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html

    Property Document:
    
    - ``rp_DefaultInstanceProfileArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultinstanceprof
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-name
    - ``rp_ServiceRoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-servicerolearn
    - ``p_AgentVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-agentversion
    - ``p_Attributes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-attributes
    - ``p_ChefConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-chefconfiguration
    - ``p_CloneAppIds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-cloneappids
    - ``p_ClonePermissions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-clonepermissions
    - ``p_ConfigurationManager``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-configmanager
    - ``p_CustomCookbooksSource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-custcookbooksource
    - ``p_CustomJson``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-custjson
    - ``p_DefaultAvailabilityZone``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultaz
    - ``p_DefaultOs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultos
    - ``p_DefaultRootDeviceType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultrootdevicetype
    - ``p_DefaultSshKeyName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultsshkeyname
    - ``p_DefaultSubnetId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#defaultsubnet
    - ``p_EcsClusterArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-ecsclusterarn
    - ``p_ElasticIps``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-elasticips
    - ``p_HostnameTheme``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-hostnametheme
    - ``p_RdsDbInstances``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-rdsdbinstances
    - ``p_SourceStackId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-sourcestackid
    - ``p_UseCustomCookbooks``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#usecustcookbooks
    - ``p_UseOpsworksSecurityGroups``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-useopsworkssecuritygroups
    - ``p_VpcId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-vpcid
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-tags
    """
    AWS_OBJECT_TYPE = "AWS::OpsWorks::Stack"

    
    rp_DefaultInstanceProfileArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultInstanceProfileArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultinstanceprof"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-name"""
    rp_ServiceRoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ServiceRoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-servicerolearn"""
    p_AgentVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AgentVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-agentversion"""
    p_Attributes: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type))),
        metadata={AttrMeta.PROPERTY_NAME: "Attributes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-attributes"""
    p_ChefConfiguration: typing.Union['PropStackChefConfiguration', dict] = attr.ib(
        default=None,
        converter=PropStackChefConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropStackChefConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "ChefConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-chefconfiguration"""
    p_CloneAppIds: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "CloneAppIds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-cloneappids"""
    p_ClonePermissions: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "ClonePermissions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-clonepermissions"""
    p_ConfigurationManager: typing.Union['PropStackStackConfigurationManager', dict] = attr.ib(
        default=None,
        converter=PropStackStackConfigurationManager.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropStackStackConfigurationManager)),
        metadata={AttrMeta.PROPERTY_NAME: "ConfigurationManager"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-configmanager"""
    p_CustomCookbooksSource: typing.Union['PropStackSource', dict] = attr.ib(
        default=None,
        converter=PropStackSource.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropStackSource)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomCookbooksSource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-custcookbooksource"""
    p_CustomJson: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomJson"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-custjson"""
    p_DefaultAvailabilityZone: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultAvailabilityZone"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultaz"""
    p_DefaultOs: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultOs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultos"""
    p_DefaultRootDeviceType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultRootDeviceType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultrootdevicetype"""
    p_DefaultSshKeyName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultSshKeyName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultsshkeyname"""
    p_DefaultSubnetId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultSubnetId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#defaultsubnet"""
    p_EcsClusterArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "EcsClusterArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-ecsclusterarn"""
    p_ElasticIps: typing.List[typing.Union['PropStackElasticIp', dict]] = attr.ib(
        default=None,
        converter=PropStackElasticIp.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropStackElasticIp), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ElasticIps"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-elasticips"""
    p_HostnameTheme: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "HostnameTheme"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-hostnametheme"""
    p_RdsDbInstances: typing.List[typing.Union['PropStackRdsDbInstance', dict]] = attr.ib(
        default=None,
        converter=PropStackRdsDbInstance.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropStackRdsDbInstance), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "RdsDbInstances"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-rdsdbinstances"""
    p_SourceStackId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SourceStackId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-sourcestackid"""
    p_UseCustomCookbooks: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "UseCustomCookbooks"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#usecustcookbooks"""
    p_UseOpsworksSecurityGroups: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "UseOpsworksSecurityGroups"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-useopsworkssecuritygroups"""
    p_VpcId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "VpcId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-vpcid"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-tags"""

    
