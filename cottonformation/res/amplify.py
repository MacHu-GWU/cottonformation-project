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
class PropAppEnvironmentVariable(Property):
    """
    AWS Object Type = "AWS::Amplify::App.EnvironmentVariable"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-environmentvariable.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-environmentvariable.html#cfn-amplify-app-environmentvariable-name
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-environmentvariable.html#cfn-amplify-app-environmentvariable-value
    """
    AWS_OBJECT_TYPE = "AWS::Amplify::App.EnvironmentVariable"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-environmentvariable.html#cfn-amplify-app-environmentvariable-name"""
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-environmentvariable.html#cfn-amplify-app-environmentvariable-value"""

@attr.s
class PropDomainSubDomainSetting(Property):
    """
    AWS Object Type = "AWS::Amplify::Domain.SubDomainSetting"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-domain-subdomainsetting.html

    Property Document:
    
    - ``rp_BranchName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-domain-subdomainsetting.html#cfn-amplify-domain-subdomainsetting-branchname
    - ``rp_Prefix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-domain-subdomainsetting.html#cfn-amplify-domain-subdomainsetting-prefix
    """
    AWS_OBJECT_TYPE = "AWS::Amplify::Domain.SubDomainSetting"
    
    rp_BranchName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "BranchName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-domain-subdomainsetting.html#cfn-amplify-domain-subdomainsetting-branchname"""
    rp_Prefix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Prefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-domain-subdomainsetting.html#cfn-amplify-domain-subdomainsetting-prefix"""

@attr.s
class PropBranchBasicAuthConfig(Property):
    """
    AWS Object Type = "AWS::Amplify::Branch.BasicAuthConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-basicauthconfig.html

    Property Document:
    
    - ``rp_Password``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-basicauthconfig.html#cfn-amplify-branch-basicauthconfig-password
    - ``rp_Username``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-basicauthconfig.html#cfn-amplify-branch-basicauthconfig-username
    - ``p_EnableBasicAuth``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-basicauthconfig.html#cfn-amplify-branch-basicauthconfig-enablebasicauth
    """
    AWS_OBJECT_TYPE = "AWS::Amplify::Branch.BasicAuthConfig"
    
    rp_Password: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Password"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-basicauthconfig.html#cfn-amplify-branch-basicauthconfig-password"""
    rp_Username: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Username"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-basicauthconfig.html#cfn-amplify-branch-basicauthconfig-username"""
    p_EnableBasicAuth: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EnableBasicAuth"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-basicauthconfig.html#cfn-amplify-branch-basicauthconfig-enablebasicauth"""

@attr.s
class PropAppBasicAuthConfig(Property):
    """
    AWS Object Type = "AWS::Amplify::App.BasicAuthConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-basicauthconfig.html

    Property Document:
    
    - ``p_EnableBasicAuth``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-basicauthconfig.html#cfn-amplify-app-basicauthconfig-enablebasicauth
    - ``p_Password``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-basicauthconfig.html#cfn-amplify-app-basicauthconfig-password
    - ``p_Username``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-basicauthconfig.html#cfn-amplify-app-basicauthconfig-username
    """
    AWS_OBJECT_TYPE = "AWS::Amplify::App.BasicAuthConfig"
    
    p_EnableBasicAuth: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EnableBasicAuth"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-basicauthconfig.html#cfn-amplify-app-basicauthconfig-enablebasicauth"""
    p_Password: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Password"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-basicauthconfig.html#cfn-amplify-app-basicauthconfig-password"""
    p_Username: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Username"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-basicauthconfig.html#cfn-amplify-app-basicauthconfig-username"""

@attr.s
class PropBranchEnvironmentVariable(Property):
    """
    AWS Object Type = "AWS::Amplify::Branch.EnvironmentVariable"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-environmentvariable.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-environmentvariable.html#cfn-amplify-branch-environmentvariable-name
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-environmentvariable.html#cfn-amplify-branch-environmentvariable-value
    """
    AWS_OBJECT_TYPE = "AWS::Amplify::Branch.EnvironmentVariable"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-environmentvariable.html#cfn-amplify-branch-environmentvariable-name"""
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-environmentvariable.html#cfn-amplify-branch-environmentvariable-value"""

@attr.s
class PropAppCustomRule(Property):
    """
    AWS Object Type = "AWS::Amplify::App.CustomRule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-customrule.html

    Property Document:
    
    - ``rp_Source``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-customrule.html#cfn-amplify-app-customrule-source
    - ``rp_Target``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-customrule.html#cfn-amplify-app-customrule-target
    - ``p_Condition``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-customrule.html#cfn-amplify-app-customrule-condition
    - ``p_Status``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-customrule.html#cfn-amplify-app-customrule-status
    """
    AWS_OBJECT_TYPE = "AWS::Amplify::App.CustomRule"
    
    rp_Source: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Source"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-customrule.html#cfn-amplify-app-customrule-source"""
    rp_Target: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Target"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-customrule.html#cfn-amplify-app-customrule-target"""
    p_Condition: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Condition"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-customrule.html#cfn-amplify-app-customrule-condition"""
    p_Status: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Status"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-customrule.html#cfn-amplify-app-customrule-status"""

@attr.s
class PropAppAutoBranchCreationConfig(Property):
    """
    AWS Object Type = "AWS::Amplify::App.AutoBranchCreationConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html

    Property Document:
    
    - ``p_AutoBranchCreationPatterns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-autobranchcreationpatterns
    - ``p_BasicAuthConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-basicauthconfig
    - ``p_BuildSpec``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-buildspec
    - ``p_EnableAutoBranchCreation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-enableautobranchcreation
    - ``p_EnableAutoBuild``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-enableautobuild
    - ``p_EnablePerformanceMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-enableperformancemode
    - ``p_EnablePullRequestPreview``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-enablepullrequestpreview
    - ``p_EnvironmentVariables``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-environmentvariables
    - ``p_PullRequestEnvironmentName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-pullrequestenvironmentname
    - ``p_Stage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-stage
    """
    AWS_OBJECT_TYPE = "AWS::Amplify::App.AutoBranchCreationConfig"
    
    p_AutoBranchCreationPatterns: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AutoBranchCreationPatterns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-autobranchcreationpatterns"""
    p_BasicAuthConfig: typing.Union['PropAppBasicAuthConfig', dict] = attr.ib(
        default=None,
        converter=PropAppBasicAuthConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropAppBasicAuthConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "BasicAuthConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-basicauthconfig"""
    p_BuildSpec: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BuildSpec"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-buildspec"""
    p_EnableAutoBranchCreation: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EnableAutoBranchCreation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-enableautobranchcreation"""
    p_EnableAutoBuild: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EnableAutoBuild"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-enableautobuild"""
    p_EnablePerformanceMode: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EnablePerformanceMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-enableperformancemode"""
    p_EnablePullRequestPreview: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EnablePullRequestPreview"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-enablepullrequestpreview"""
    p_EnvironmentVariables: typing.List[typing.Union['PropAppEnvironmentVariable', dict]] = attr.ib(
        default=None,
        converter=PropAppEnvironmentVariable.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropAppEnvironmentVariable), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "EnvironmentVariables"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-environmentvariables"""
    p_PullRequestEnvironmentName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PullRequestEnvironmentName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-pullrequestenvironmentname"""
    p_Stage: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Stage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-stage"""


#--- Resource declaration ---

@attr.s
class App(Resource):
    """
    AWS Object Type = "AWS::Amplify::App"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-name
    - ``p_AccessToken``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-accesstoken
    - ``p_AutoBranchCreationConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-autobranchcreationconfig
    - ``p_BasicAuthConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-basicauthconfig
    - ``p_BuildSpec``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-buildspec
    - ``p_CustomHeaders``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-customheaders
    - ``p_CustomRules``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-customrules
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-description
    - ``p_EnableBranchAutoDeletion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-enablebranchautodeletion
    - ``p_EnvironmentVariables``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-environmentvariables
    - ``p_IAMServiceRole``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-iamservicerole
    - ``p_OauthToken``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-oauthtoken
    - ``p_Repository``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-repository
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-tags
    """
    AWS_OBJECT_TYPE = "AWS::Amplify::App"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-name"""
    p_AccessToken: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AccessToken"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-accesstoken"""
    p_AutoBranchCreationConfig: typing.Union['PropAppAutoBranchCreationConfig', dict] = attr.ib(
        default=None,
        converter=PropAppAutoBranchCreationConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropAppAutoBranchCreationConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "AutoBranchCreationConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-autobranchcreationconfig"""
    p_BasicAuthConfig: typing.Union['PropAppBasicAuthConfig', dict] = attr.ib(
        default=None,
        converter=PropAppBasicAuthConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropAppBasicAuthConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "BasicAuthConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-basicauthconfig"""
    p_BuildSpec: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BuildSpec"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-buildspec"""
    p_CustomHeaders: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomHeaders"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-customheaders"""
    p_CustomRules: typing.List[typing.Union['PropAppCustomRule', dict]] = attr.ib(
        default=None,
        converter=PropAppCustomRule.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropAppCustomRule), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "CustomRules"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-customrules"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-description"""
    p_EnableBranchAutoDeletion: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EnableBranchAutoDeletion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-enablebranchautodeletion"""
    p_EnvironmentVariables: typing.List[typing.Union['PropAppEnvironmentVariable', dict]] = attr.ib(
        default=None,
        converter=PropAppEnvironmentVariable.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropAppEnvironmentVariable), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "EnvironmentVariables"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-environmentvariables"""
    p_IAMServiceRole: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "IAMServiceRole"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-iamservicerole"""
    p_OauthToken: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "OauthToken"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-oauthtoken"""
    p_Repository: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Repository"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-repository"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-tags"""

    
    @property
    def rv_AppId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#aws-resource-amplify-app-return-values"""
        return GetAtt(resource=self, attr_name="AppId")
    
    @property
    def rv_AppName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#aws-resource-amplify-app-return-values"""
        return GetAtt(resource=self, attr_name="AppName")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#aws-resource-amplify-app-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_DefaultDomain(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#aws-resource-amplify-app-return-values"""
        return GetAtt(resource=self, attr_name="DefaultDomain")
    

@attr.s
class Domain(Resource):
    """
    AWS Object Type = "AWS::Amplify::Domain"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html

    Property Document:
    
    - ``rp_AppId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#cfn-amplify-domain-appid
    - ``rp_DomainName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#cfn-amplify-domain-domainname
    - ``rp_SubDomainSettings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#cfn-amplify-domain-subdomainsettings
    - ``p_AutoSubDomainCreationPatterns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#cfn-amplify-domain-autosubdomaincreationpatterns
    - ``p_AutoSubDomainIAMRole``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#cfn-amplify-domain-autosubdomainiamrole
    - ``p_EnableAutoSubDomain``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#cfn-amplify-domain-enableautosubdomain
    """
    AWS_OBJECT_TYPE = "AWS::Amplify::Domain"

    
    rp_AppId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AppId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#cfn-amplify-domain-appid"""
    rp_DomainName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DomainName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#cfn-amplify-domain-domainname"""
    rp_SubDomainSettings: typing.List[typing.Union['PropDomainSubDomainSetting', dict]] = attr.ib(
        default=None,
        converter=PropDomainSubDomainSetting.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDomainSubDomainSetting), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "SubDomainSettings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#cfn-amplify-domain-subdomainsettings"""
    p_AutoSubDomainCreationPatterns: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AutoSubDomainCreationPatterns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#cfn-amplify-domain-autosubdomaincreationpatterns"""
    p_AutoSubDomainIAMRole: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AutoSubDomainIAMRole"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#cfn-amplify-domain-autosubdomainiamrole"""
    p_EnableAutoSubDomain: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EnableAutoSubDomain"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#cfn-amplify-domain-enableautosubdomain"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#aws-resource-amplify-domain-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_AutoSubDomainCreationPatterns(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#aws-resource-amplify-domain-return-values"""
        return GetAtt(resource=self, attr_name="AutoSubDomainCreationPatterns")
    
    @property
    def rv_AutoSubDomainIAMRole(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#aws-resource-amplify-domain-return-values"""
        return GetAtt(resource=self, attr_name="AutoSubDomainIAMRole")
    
    @property
    def rv_CertificateRecord(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#aws-resource-amplify-domain-return-values"""
        return GetAtt(resource=self, attr_name="CertificateRecord")
    
    @property
    def rv_DomainName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#aws-resource-amplify-domain-return-values"""
        return GetAtt(resource=self, attr_name="DomainName")
    
    @property
    def rv_DomainStatus(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#aws-resource-amplify-domain-return-values"""
        return GetAtt(resource=self, attr_name="DomainStatus")
    
    @property
    def rv_EnableAutoSubDomain(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#aws-resource-amplify-domain-return-values"""
        return GetAtt(resource=self, attr_name="EnableAutoSubDomain")
    
    @property
    def rv_StatusReason(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#aws-resource-amplify-domain-return-values"""
        return GetAtt(resource=self, attr_name="StatusReason")
    

@attr.s
class Branch(Resource):
    """
    AWS Object Type = "AWS::Amplify::Branch"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html

    Property Document:
    
    - ``rp_AppId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-appid
    - ``rp_BranchName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-branchname
    - ``p_BasicAuthConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-basicauthconfig
    - ``p_BuildSpec``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-buildspec
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-description
    - ``p_EnableAutoBuild``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-enableautobuild
    - ``p_EnablePerformanceMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-enableperformancemode
    - ``p_EnablePullRequestPreview``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-enablepullrequestpreview
    - ``p_EnvironmentVariables``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-environmentvariables
    - ``p_PullRequestEnvironmentName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-pullrequestenvironmentname
    - ``p_Stage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-stage
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-tags
    """
    AWS_OBJECT_TYPE = "AWS::Amplify::Branch"

    
    rp_AppId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AppId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-appid"""
    rp_BranchName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "BranchName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-branchname"""
    p_BasicAuthConfig: typing.Union['PropBranchBasicAuthConfig', dict] = attr.ib(
        default=None,
        converter=PropBranchBasicAuthConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBranchBasicAuthConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "BasicAuthConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-basicauthconfig"""
    p_BuildSpec: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BuildSpec"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-buildspec"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-description"""
    p_EnableAutoBuild: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EnableAutoBuild"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-enableautobuild"""
    p_EnablePerformanceMode: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EnablePerformanceMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-enableperformancemode"""
    p_EnablePullRequestPreview: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EnablePullRequestPreview"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-enablepullrequestpreview"""
    p_EnvironmentVariables: typing.List[typing.Union['PropBranchEnvironmentVariable', dict]] = attr.ib(
        default=None,
        converter=PropBranchEnvironmentVariable.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBranchEnvironmentVariable), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "EnvironmentVariables"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-environmentvariables"""
    p_PullRequestEnvironmentName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PullRequestEnvironmentName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-pullrequestenvironmentname"""
    p_Stage: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Stage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-stage"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#aws-resource-amplify-branch-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_BranchName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#aws-resource-amplify-branch-return-values"""
        return GetAtt(resource=self, attr_name="BranchName")
    
