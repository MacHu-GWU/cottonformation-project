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
class VirtualRouterPortMapping(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualRouter.PortMapping"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-portmapping.html

    Property Document:
    
    - ``rp_Port``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-portmapping.html#cfn-appmesh-virtualrouter-portmapping-port
    - ``rp_Protocol``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-portmapping.html#cfn-appmesh-virtualrouter-portmapping-protocol
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualRouter.PortMapping"
    
    rp_Port: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Port"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-portmapping.html#cfn-appmesh-virtualrouter-portmapping-port"""
    rp_Protocol: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Protocol"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-portmapping.html#cfn-appmesh-virtualrouter-portmapping-protocol"""

@attr.s
class VirtualNodeTlsValidationContextSdsTrust(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.TlsValidationContextSdsTrust"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontextsdstrust.html

    Property Document:
    
    - ``rp_SecretName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontextsdstrust.html#cfn-appmesh-virtualnode-tlsvalidationcontextsdstrust-secretname
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.TlsValidationContextSdsTrust"
    
    rp_SecretName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SecretName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontextsdstrust.html#cfn-appmesh-virtualnode-tlsvalidationcontextsdstrust-secretname"""

@attr.s
class GatewayRouteHttpQueryParameterMatch(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.HttpQueryParameterMatch"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpqueryparametermatch.html

    Property Document:
    
    - ``p_Exact``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpqueryparametermatch.html#cfn-appmesh-gatewayroute-httpqueryparametermatch-exact
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.HttpQueryParameterMatch"
    
    p_Exact: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Exact"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpqueryparametermatch.html#cfn-appmesh-gatewayroute-httpqueryparametermatch-exact"""

@attr.s
class RouteDuration(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.Duration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-duration.html

    Property Document:
    
    - ``rp_Unit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-duration.html#cfn-appmesh-route-duration-unit
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-duration.html#cfn-appmesh-route-duration-value
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.Duration"
    
    rp_Unit: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Unit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-duration.html#cfn-appmesh-route-duration-unit"""
    rp_Value: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-duration.html#cfn-appmesh-route-duration-value"""

@attr.s
class RouteWeightedTarget(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.WeightedTarget"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-weightedtarget.html

    Property Document:
    
    - ``rp_VirtualNode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-weightedtarget.html#cfn-appmesh-route-weightedtarget-virtualnode
    - ``rp_Weight``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-weightedtarget.html#cfn-appmesh-route-weightedtarget-weight
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.WeightedTarget"
    
    rp_VirtualNode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "VirtualNode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-weightedtarget.html#cfn-appmesh-route-weightedtarget-virtualnode"""
    rp_Weight: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Weight"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-weightedtarget.html#cfn-appmesh-route-weightedtarget-weight"""

@attr.s
class GatewayRouteHttpGatewayRoutePrefixRewrite(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.HttpGatewayRoutePrefixRewrite"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteprefixrewrite.html

    Property Document:
    
    - ``p_DefaultPrefix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteprefixrewrite.html#cfn-appmesh-gatewayroute-httpgatewayrouteprefixrewrite-defaultprefix
    - ``p_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteprefixrewrite.html#cfn-appmesh-gatewayroute-httpgatewayrouteprefixrewrite-value
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.HttpGatewayRoutePrefixRewrite"
    
    p_DefaultPrefix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultPrefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteprefixrewrite.html#cfn-appmesh-gatewayroute-httpgatewayrouteprefixrewrite-defaultprefix"""
    p_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteprefixrewrite.html#cfn-appmesh-gatewayroute-httpgatewayrouteprefixrewrite-value"""

@attr.s
class VirtualGatewayVirtualGatewayListenerTlsAcmCertificate(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTlsAcmCertificate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsacmcertificate.html

    Property Document:
    
    - ``rp_CertificateArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsacmcertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsacmcertificate-certificatearn
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTlsAcmCertificate"
    
    rp_CertificateArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "CertificateArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsacmcertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsacmcertificate-certificatearn"""

@attr.s
class VirtualNodeFileAccessLog(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.FileAccessLog"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-fileaccesslog.html

    Property Document:
    
    - ``rp_Path``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-fileaccesslog.html#cfn-appmesh-virtualnode-fileaccesslog-path
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.FileAccessLog"
    
    rp_Path: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Path"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-fileaccesslog.html#cfn-appmesh-virtualnode-fileaccesslog-path"""

@attr.s
class VirtualNodeAwsCloudMapInstanceAttribute(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.AwsCloudMapInstanceAttribute"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapinstanceattribute.html

    Property Document:
    
    - ``rp_Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapinstanceattribute.html#cfn-appmesh-virtualnode-awscloudmapinstanceattribute-key
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapinstanceattribute.html#cfn-appmesh-virtualnode-awscloudmapinstanceattribute-value
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.AwsCloudMapInstanceAttribute"
    
    rp_Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapinstanceattribute.html#cfn-appmesh-virtualnode-awscloudmapinstanceattribute-key"""
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapinstanceattribute.html#cfn-appmesh-virtualnode-awscloudmapinstanceattribute-value"""

@attr.s
class VirtualGatewayVirtualGatewayTlsValidationContextFileTrust(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayTlsValidationContextFileTrust"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextfiletrust.html

    Property Document:
    
    - ``rp_CertificateChain``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextfiletrust.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextfiletrust-certificatechain
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayTlsValidationContextFileTrust"
    
    rp_CertificateChain: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "CertificateChain"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextfiletrust.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextfiletrust-certificatechain"""

@attr.s
class RouteHttpPathMatch(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.HttpPathMatch"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httppathmatch.html

    Property Document:
    
    - ``p_Exact``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httppathmatch.html#cfn-appmesh-route-httppathmatch-exact
    - ``p_Regex``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httppathmatch.html#cfn-appmesh-route-httppathmatch-regex
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.HttpPathMatch"
    
    p_Exact: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Exact"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httppathmatch.html#cfn-appmesh-route-httppathmatch-exact"""
    p_Regex: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Regex"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httppathmatch.html#cfn-appmesh-route-httppathmatch-regex"""

@attr.s
class VirtualGatewayVirtualGatewayHttp2ConnectionPool(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayHttp2ConnectionPool"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhttp2connectionpool.html

    Property Document:
    
    - ``rp_MaxRequests``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhttp2connectionpool.html#cfn-appmesh-virtualgateway-virtualgatewayhttp2connectionpool-maxrequests
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayHttp2ConnectionPool"
    
    rp_MaxRequests: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "MaxRequests"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhttp2connectionpool.html#cfn-appmesh-virtualgateway-virtualgatewayhttp2connectionpool-maxrequests"""

@attr.s
class GatewayRouteGatewayRouteHostnameRewrite(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.GatewayRouteHostnameRewrite"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutehostnamerewrite.html

    Property Document:
    
    - ``p_DefaultTargetHostname``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutehostnamerewrite.html#cfn-appmesh-gatewayroute-gatewayroutehostnamerewrite-defaulttargethostname
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.GatewayRouteHostnameRewrite"
    
    p_DefaultTargetHostname: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultTargetHostname"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutehostnamerewrite.html#cfn-appmesh-gatewayroute-gatewayroutehostnamerewrite-defaulttargethostname"""

@attr.s
class VirtualNodePortMapping(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.PortMapping"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-portmapping.html

    Property Document:
    
    - ``rp_Port``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-portmapping.html#cfn-appmesh-virtualnode-portmapping-port
    - ``rp_Protocol``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-portmapping.html#cfn-appmesh-virtualnode-portmapping-protocol
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.PortMapping"
    
    rp_Port: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Port"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-portmapping.html#cfn-appmesh-virtualnode-portmapping-port"""
    rp_Protocol: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Protocol"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-portmapping.html#cfn-appmesh-virtualnode-portmapping-protocol"""

@attr.s
class VirtualServiceVirtualRouterServiceProvider(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualService.VirtualRouterServiceProvider"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualrouterserviceprovider.html

    Property Document:
    
    - ``rp_VirtualRouterName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualrouterserviceprovider.html#cfn-appmesh-virtualservice-virtualrouterserviceprovider-virtualroutername
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualService.VirtualRouterServiceProvider"
    
    rp_VirtualRouterName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "VirtualRouterName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualrouterserviceprovider.html#cfn-appmesh-virtualservice-virtualrouterserviceprovider-virtualroutername"""

@attr.s
class VirtualNodeListenerTlsSdsCertificate(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.ListenerTlsSdsCertificate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlssdscertificate.html

    Property Document:
    
    - ``rp_SecretName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlssdscertificate.html#cfn-appmesh-virtualnode-listenertlssdscertificate-secretname
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.ListenerTlsSdsCertificate"
    
    rp_SecretName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SecretName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlssdscertificate.html#cfn-appmesh-virtualnode-listenertlssdscertificate-secretname"""

@attr.s
class GatewayRouteQueryParameter(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.QueryParameter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-queryparameter.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-queryparameter.html#cfn-appmesh-gatewayroute-queryparameter-name
    - ``p_Match``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-queryparameter.html#cfn-appmesh-gatewayroute-queryparameter-match
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.QueryParameter"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-queryparameter.html#cfn-appmesh-gatewayroute-queryparameter-name"""
    p_Match: typing.Union['GatewayRouteHttpQueryParameterMatch', dict] = attr.ib(
        default=None,
        converter=GatewayRouteHttpQueryParameterMatch.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(GatewayRouteHttpQueryParameterMatch)),
        metadata={AttrMeta.PROPERTY_NAME: "Match"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-queryparameter.html#cfn-appmesh-gatewayroute-queryparameter-match"""

@attr.s
class VirtualGatewayVirtualGatewayGrpcConnectionPool(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayGrpcConnectionPool"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaygrpcconnectionpool.html

    Property Document:
    
    - ``rp_MaxRequests``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaygrpcconnectionpool.html#cfn-appmesh-virtualgateway-virtualgatewaygrpcconnectionpool-maxrequests
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayGrpcConnectionPool"
    
    rp_MaxRequests: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "MaxRequests"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaygrpcconnectionpool.html#cfn-appmesh-virtualgateway-virtualgatewaygrpcconnectionpool-maxrequests"""

@attr.s
class GatewayRouteGrpcGatewayRouteRewrite(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.GrpcGatewayRouteRewrite"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouterewrite.html

    Property Document:
    
    - ``p_Hostname``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouterewrite.html#cfn-appmesh-gatewayroute-grpcgatewayrouterewrite-hostname
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.GrpcGatewayRouteRewrite"
    
    p_Hostname: typing.Union['GatewayRouteGatewayRouteHostnameRewrite', dict] = attr.ib(
        default=None,
        converter=GatewayRouteGatewayRouteHostnameRewrite.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(GatewayRouteGatewayRouteHostnameRewrite)),
        metadata={AttrMeta.PROPERTY_NAME: "Hostname"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouterewrite.html#cfn-appmesh-gatewayroute-grpcgatewayrouterewrite-hostname"""

@attr.s
class VirtualNodeVirtualNodeTcpConnectionPool(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.VirtualNodeTcpConnectionPool"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodetcpconnectionpool.html

    Property Document:
    
    - ``rp_MaxConnections``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodetcpconnectionpool.html#cfn-appmesh-virtualnode-virtualnodetcpconnectionpool-maxconnections
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.VirtualNodeTcpConnectionPool"
    
    rp_MaxConnections: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "MaxConnections"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodetcpconnectionpool.html#cfn-appmesh-virtualnode-virtualnodetcpconnectionpool-maxconnections"""

@attr.s
class VirtualNodeHealthCheck(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.HealthCheck"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html

    Property Document:
    
    - ``rp_HealthyThreshold``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html#cfn-appmesh-virtualnode-healthcheck-healthythreshold
    - ``rp_IntervalMillis``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html#cfn-appmesh-virtualnode-healthcheck-intervalmillis
    - ``rp_Protocol``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html#cfn-appmesh-virtualnode-healthcheck-protocol
    - ``rp_TimeoutMillis``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html#cfn-appmesh-virtualnode-healthcheck-timeoutmillis
    - ``rp_UnhealthyThreshold``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html#cfn-appmesh-virtualnode-healthcheck-unhealthythreshold
    - ``p_Path``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html#cfn-appmesh-virtualnode-healthcheck-path
    - ``p_Port``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html#cfn-appmesh-virtualnode-healthcheck-port
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.HealthCheck"
    
    rp_HealthyThreshold: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "HealthyThreshold"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html#cfn-appmesh-virtualnode-healthcheck-healthythreshold"""
    rp_IntervalMillis: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "IntervalMillis"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html#cfn-appmesh-virtualnode-healthcheck-intervalmillis"""
    rp_Protocol: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Protocol"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html#cfn-appmesh-virtualnode-healthcheck-protocol"""
    rp_TimeoutMillis: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "TimeoutMillis"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html#cfn-appmesh-virtualnode-healthcheck-timeoutmillis"""
    rp_UnhealthyThreshold: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "UnhealthyThreshold"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html#cfn-appmesh-virtualnode-healthcheck-unhealthythreshold"""
    p_Path: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Path"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html#cfn-appmesh-virtualnode-healthcheck-path"""
    p_Port: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Port"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html#cfn-appmesh-virtualnode-healthcheck-port"""

@attr.s
class VirtualNodeAwsCloudMapServiceDiscovery(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.AwsCloudMapServiceDiscovery"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapservicediscovery.html

    Property Document:
    
    - ``rp_NamespaceName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapservicediscovery.html#cfn-appmesh-virtualnode-awscloudmapservicediscovery-namespacename
    - ``rp_ServiceName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapservicediscovery.html#cfn-appmesh-virtualnode-awscloudmapservicediscovery-servicename
    - ``p_Attributes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapservicediscovery.html#cfn-appmesh-virtualnode-awscloudmapservicediscovery-attributes
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.AwsCloudMapServiceDiscovery"
    
    rp_NamespaceName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "NamespaceName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapservicediscovery.html#cfn-appmesh-virtualnode-awscloudmapservicediscovery-namespacename"""
    rp_ServiceName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ServiceName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapservicediscovery.html#cfn-appmesh-virtualnode-awscloudmapservicediscovery-servicename"""
    p_Attributes: typing.List[typing.Union['VirtualNodeAwsCloudMapInstanceAttribute', dict]] = attr.ib(
        default=None,
        converter=VirtualNodeAwsCloudMapInstanceAttribute.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(VirtualNodeAwsCloudMapInstanceAttribute), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Attributes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapservicediscovery.html#cfn-appmesh-virtualnode-awscloudmapservicediscovery-attributes"""

@attr.s
class GatewayRouteHttpGatewayRoutePathRewrite(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.HttpGatewayRoutePathRewrite"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutepathrewrite.html

    Property Document:
    
    - ``p_Exact``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutepathrewrite.html#cfn-appmesh-gatewayroute-httpgatewayroutepathrewrite-exact
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.HttpGatewayRoutePathRewrite"
    
    p_Exact: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Exact"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutepathrewrite.html#cfn-appmesh-gatewayroute-httpgatewayroutepathrewrite-exact"""

@attr.s
class VirtualNodeVirtualNodeHttpConnectionPool(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.VirtualNodeHttpConnectionPool"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodehttpconnectionpool.html

    Property Document:
    
    - ``rp_MaxConnections``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodehttpconnectionpool.html#cfn-appmesh-virtualnode-virtualnodehttpconnectionpool-maxconnections
    - ``p_MaxPendingRequests``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodehttpconnectionpool.html#cfn-appmesh-virtualnode-virtualnodehttpconnectionpool-maxpendingrequests
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.VirtualNodeHttpConnectionPool"
    
    rp_MaxConnections: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "MaxConnections"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodehttpconnectionpool.html#cfn-appmesh-virtualnode-virtualnodehttpconnectionpool-maxconnections"""
    p_MaxPendingRequests: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MaxPendingRequests"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodehttpconnectionpool.html#cfn-appmesh-virtualnode-virtualnodehttpconnectionpool-maxpendingrequests"""

@attr.s
class VirtualServiceVirtualNodeServiceProvider(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualService.VirtualNodeServiceProvider"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualnodeserviceprovider.html

    Property Document:
    
    - ``rp_VirtualNodeName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualnodeserviceprovider.html#cfn-appmesh-virtualservice-virtualnodeserviceprovider-virtualnodename
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualService.VirtualNodeServiceProvider"
    
    rp_VirtualNodeName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "VirtualNodeName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualnodeserviceprovider.html#cfn-appmesh-virtualservice-virtualnodeserviceprovider-virtualnodename"""

@attr.s
class VirtualGatewayVirtualGatewayListenerTlsFileCertificate(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTlsFileCertificate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate.html

    Property Document:
    
    - ``rp_CertificateChain``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate-certificatechain
    - ``rp_PrivateKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate-privatekey
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTlsFileCertificate"
    
    rp_CertificateChain: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "CertificateChain"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate-certificatechain"""
    rp_PrivateKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PrivateKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate-privatekey"""

@attr.s
class RouteHttpQueryParameterMatch(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.HttpQueryParameterMatch"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpqueryparametermatch.html

    Property Document:
    
    - ``p_Exact``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpqueryparametermatch.html#cfn-appmesh-route-httpqueryparametermatch-exact
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.HttpQueryParameterMatch"
    
    p_Exact: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Exact"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpqueryparametermatch.html#cfn-appmesh-route-httpqueryparametermatch-exact"""

@attr.s
class VirtualNodeListenerTlsFileCertificate(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.ListenerTlsFileCertificate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsfilecertificate.html

    Property Document:
    
    - ``rp_CertificateChain``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsfilecertificate.html#cfn-appmesh-virtualnode-listenertlsfilecertificate-certificatechain
    - ``rp_PrivateKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsfilecertificate.html#cfn-appmesh-virtualnode-listenertlsfilecertificate-privatekey
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.ListenerTlsFileCertificate"
    
    rp_CertificateChain: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "CertificateChain"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsfilecertificate.html#cfn-appmesh-virtualnode-listenertlsfilecertificate-certificatechain"""
    rp_PrivateKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PrivateKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsfilecertificate.html#cfn-appmesh-virtualnode-listenertlsfilecertificate-privatekey"""

@attr.s
class VirtualGatewaySubjectAlternativeNameMatchers(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.SubjectAlternativeNameMatchers"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-subjectalternativenamematchers.html

    Property Document:
    
    - ``p_Exact``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-subjectalternativenamematchers.html#cfn-appmesh-virtualgateway-subjectalternativenamematchers-exact
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.SubjectAlternativeNameMatchers"
    
    p_Exact: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Exact"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-subjectalternativenamematchers.html#cfn-appmesh-virtualgateway-subjectalternativenamematchers-exact"""

@attr.s
class RouteGrpcRouteAction(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.GrpcRouteAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcrouteaction.html

    Property Document:
    
    - ``rp_WeightedTargets``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcrouteaction.html#cfn-appmesh-route-grpcrouteaction-weightedtargets
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.GrpcRouteAction"
    
    rp_WeightedTargets: typing.List[typing.Union['RouteWeightedTarget', dict]] = attr.ib(
        default=None,
        converter=RouteWeightedTarget.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(RouteWeightedTarget), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "WeightedTargets"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcrouteaction.html#cfn-appmesh-route-grpcrouteaction-weightedtargets"""

@attr.s
class VirtualServiceVirtualServiceProvider(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualService.VirtualServiceProvider"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualserviceprovider.html

    Property Document:
    
    - ``p_VirtualNode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualserviceprovider.html#cfn-appmesh-virtualservice-virtualserviceprovider-virtualnode
    - ``p_VirtualRouter``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualserviceprovider.html#cfn-appmesh-virtualservice-virtualserviceprovider-virtualrouter
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualService.VirtualServiceProvider"
    
    p_VirtualNode: typing.Union['VirtualServiceVirtualNodeServiceProvider', dict] = attr.ib(
        default=None,
        converter=VirtualServiceVirtualNodeServiceProvider.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualServiceVirtualNodeServiceProvider)),
        metadata={AttrMeta.PROPERTY_NAME: "VirtualNode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualserviceprovider.html#cfn-appmesh-virtualservice-virtualserviceprovider-virtualnode"""
    p_VirtualRouter: typing.Union['VirtualServiceVirtualRouterServiceProvider', dict] = attr.ib(
        default=None,
        converter=VirtualServiceVirtualRouterServiceProvider.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualServiceVirtualRouterServiceProvider)),
        metadata={AttrMeta.PROPERTY_NAME: "VirtualRouter"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualserviceprovider.html#cfn-appmesh-virtualservice-virtualserviceprovider-virtualrouter"""

@attr.s
class VirtualNodeDnsServiceDiscovery(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.DnsServiceDiscovery"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-dnsservicediscovery.html

    Property Document:
    
    - ``rp_Hostname``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-dnsservicediscovery.html#cfn-appmesh-virtualnode-dnsservicediscovery-hostname
    - ``p_ResponseType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-dnsservicediscovery.html#cfn-appmesh-virtualnode-dnsservicediscovery-responsetype
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.DnsServiceDiscovery"
    
    rp_Hostname: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Hostname"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-dnsservicediscovery.html#cfn-appmesh-virtualnode-dnsservicediscovery-hostname"""
    p_ResponseType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ResponseType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-dnsservicediscovery.html#cfn-appmesh-virtualnode-dnsservicediscovery-responsetype"""

@attr.s
class VirtualNodeTlsValidationContextFileTrust(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.TlsValidationContextFileTrust"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontextfiletrust.html

    Property Document:
    
    - ``rp_CertificateChain``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontextfiletrust.html#cfn-appmesh-virtualnode-tlsvalidationcontextfiletrust-certificatechain
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.TlsValidationContextFileTrust"
    
    rp_CertificateChain: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "CertificateChain"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontextfiletrust.html#cfn-appmesh-virtualnode-tlsvalidationcontextfiletrust-certificatechain"""

@attr.s
class GatewayRouteGatewayRouteRangeMatch(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.GatewayRouteRangeMatch"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayrouterangematch.html

    Property Document:
    
    - ``rp_End``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayrouterangematch.html#cfn-appmesh-gatewayroute-gatewayrouterangematch-end
    - ``rp_Start``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayrouterangematch.html#cfn-appmesh-gatewayroute-gatewayrouterangematch-start
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.GatewayRouteRangeMatch"
    
    rp_End: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "End"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayrouterangematch.html#cfn-appmesh-gatewayroute-gatewayrouterangematch-end"""
    rp_Start: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Start"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayrouterangematch.html#cfn-appmesh-gatewayroute-gatewayrouterangematch-start"""

@attr.s
class RouteTcpRouteAction(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.TcpRouteAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcprouteaction.html

    Property Document:
    
    - ``rp_WeightedTargets``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcprouteaction.html#cfn-appmesh-route-tcprouteaction-weightedtargets
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.TcpRouteAction"
    
    rp_WeightedTargets: typing.List[typing.Union['RouteWeightedTarget', dict]] = attr.ib(
        default=None,
        converter=RouteWeightedTarget.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(RouteWeightedTarget), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "WeightedTargets"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcprouteaction.html#cfn-appmesh-route-tcprouteaction-weightedtargets"""

@attr.s
class VirtualRouterVirtualRouterListener(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualRouter.VirtualRouterListener"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-virtualrouterlistener.html

    Property Document:
    
    - ``rp_PortMapping``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-virtualrouterlistener.html#cfn-appmesh-virtualrouter-virtualrouterlistener-portmapping
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualRouter.VirtualRouterListener"
    
    rp_PortMapping: typing.Union['VirtualRouterPortMapping', dict] = attr.ib(
        default=None,
        converter=VirtualRouterPortMapping.from_dict,
        validator=attr.validators.instance_of(VirtualRouterPortMapping),
        metadata={AttrMeta.PROPERTY_NAME: "PortMapping"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-virtualrouterlistener.html#cfn-appmesh-virtualrouter-virtualrouterlistener-portmapping"""

@attr.s
class VirtualGatewayVirtualGatewayTlsValidationContextSdsTrust(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayTlsValidationContextSdsTrust"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextsdstrust.html

    Property Document:
    
    - ``rp_SecretName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextsdstrust.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextsdstrust-secretname
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayTlsValidationContextSdsTrust"
    
    rp_SecretName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SecretName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextsdstrust.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextsdstrust-secretname"""

@attr.s
class RouteGrpcRetryPolicy(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.GrpcRetryPolicy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcretrypolicy.html

    Property Document:
    
    - ``rp_MaxRetries``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcretrypolicy.html#cfn-appmesh-route-grpcretrypolicy-maxretries
    - ``rp_PerRetryTimeout``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcretrypolicy.html#cfn-appmesh-route-grpcretrypolicy-perretrytimeout
    - ``p_GrpcRetryEvents``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcretrypolicy.html#cfn-appmesh-route-grpcretrypolicy-grpcretryevents
    - ``p_HttpRetryEvents``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcretrypolicy.html#cfn-appmesh-route-grpcretrypolicy-httpretryevents
    - ``p_TcpRetryEvents``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcretrypolicy.html#cfn-appmesh-route-grpcretrypolicy-tcpretryevents
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.GrpcRetryPolicy"
    
    rp_MaxRetries: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "MaxRetries"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcretrypolicy.html#cfn-appmesh-route-grpcretrypolicy-maxretries"""
    rp_PerRetryTimeout: typing.Union['RouteDuration', dict] = attr.ib(
        default=None,
        converter=RouteDuration.from_dict,
        validator=attr.validators.instance_of(RouteDuration),
        metadata={AttrMeta.PROPERTY_NAME: "PerRetryTimeout"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcretrypolicy.html#cfn-appmesh-route-grpcretrypolicy-perretrytimeout"""
    p_GrpcRetryEvents: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "GrpcRetryEvents"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcretrypolicy.html#cfn-appmesh-route-grpcretrypolicy-grpcretryevents"""
    p_HttpRetryEvents: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "HttpRetryEvents"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcretrypolicy.html#cfn-appmesh-route-grpcretrypolicy-httpretryevents"""
    p_TcpRetryEvents: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "TcpRetryEvents"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcretrypolicy.html#cfn-appmesh-route-grpcretrypolicy-tcpretryevents"""

@attr.s
class VirtualNodeServiceDiscovery(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.ServiceDiscovery"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-servicediscovery.html

    Property Document:
    
    - ``p_AWSCloudMap``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-servicediscovery.html#cfn-appmesh-virtualnode-servicediscovery-awscloudmap
    - ``p_DNS``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-servicediscovery.html#cfn-appmesh-virtualnode-servicediscovery-dns
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.ServiceDiscovery"
    
    p_AWSCloudMap: typing.Union['VirtualNodeAwsCloudMapServiceDiscovery', dict] = attr.ib(
        default=None,
        converter=VirtualNodeAwsCloudMapServiceDiscovery.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeAwsCloudMapServiceDiscovery)),
        metadata={AttrMeta.PROPERTY_NAME: "AWSCloudMap"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-servicediscovery.html#cfn-appmesh-virtualnode-servicediscovery-awscloudmap"""
    p_DNS: typing.Union['VirtualNodeDnsServiceDiscovery', dict] = attr.ib(
        default=None,
        converter=VirtualNodeDnsServiceDiscovery.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeDnsServiceDiscovery)),
        metadata={AttrMeta.PROPERTY_NAME: "DNS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-servicediscovery.html#cfn-appmesh-virtualnode-servicediscovery-dns"""

@attr.s
class VirtualNodeDuration(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.Duration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-duration.html

    Property Document:
    
    - ``rp_Unit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-duration.html#cfn-appmesh-virtualnode-duration-unit
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-duration.html#cfn-appmesh-virtualnode-duration-value
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.Duration"
    
    rp_Unit: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Unit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-duration.html#cfn-appmesh-virtualnode-duration-unit"""
    rp_Value: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-duration.html#cfn-appmesh-virtualnode-duration-value"""

@attr.s
class RouteHttpRetryPolicy(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.HttpRetryPolicy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpretrypolicy.html

    Property Document:
    
    - ``rp_MaxRetries``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpretrypolicy.html#cfn-appmesh-route-httpretrypolicy-maxretries
    - ``rp_PerRetryTimeout``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpretrypolicy.html#cfn-appmesh-route-httpretrypolicy-perretrytimeout
    - ``p_HttpRetryEvents``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpretrypolicy.html#cfn-appmesh-route-httpretrypolicy-httpretryevents
    - ``p_TcpRetryEvents``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpretrypolicy.html#cfn-appmesh-route-httpretrypolicy-tcpretryevents
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.HttpRetryPolicy"
    
    rp_MaxRetries: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "MaxRetries"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpretrypolicy.html#cfn-appmesh-route-httpretrypolicy-maxretries"""
    rp_PerRetryTimeout: typing.Union['RouteDuration', dict] = attr.ib(
        default=None,
        converter=RouteDuration.from_dict,
        validator=attr.validators.instance_of(RouteDuration),
        metadata={AttrMeta.PROPERTY_NAME: "PerRetryTimeout"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpretrypolicy.html#cfn-appmesh-route-httpretrypolicy-perretrytimeout"""
    p_HttpRetryEvents: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "HttpRetryEvents"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpretrypolicy.html#cfn-appmesh-route-httpretrypolicy-httpretryevents"""
    p_TcpRetryEvents: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "TcpRetryEvents"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpretrypolicy.html#cfn-appmesh-route-httpretrypolicy-tcpretryevents"""

@attr.s
class VirtualGatewayVirtualGatewayPortMapping(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayPortMapping"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayportmapping.html

    Property Document:
    
    - ``rp_Port``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayportmapping.html#cfn-appmesh-virtualgateway-virtualgatewayportmapping-port
    - ``rp_Protocol``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayportmapping.html#cfn-appmesh-virtualgateway-virtualgatewayportmapping-protocol
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayPortMapping"
    
    rp_Port: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Port"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayportmapping.html#cfn-appmesh-virtualgateway-virtualgatewayportmapping-port"""
    rp_Protocol: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Protocol"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayportmapping.html#cfn-appmesh-virtualgateway-virtualgatewayportmapping-protocol"""

@attr.s
class GatewayRouteHttpGatewayRouteRewrite(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.HttpGatewayRouteRewrite"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite.html

    Property Document:
    
    - ``p_Hostname``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite.html#cfn-appmesh-gatewayroute-httpgatewayrouterewrite-hostname
    - ``p_Path``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite.html#cfn-appmesh-gatewayroute-httpgatewayrouterewrite-path
    - ``p_Prefix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite.html#cfn-appmesh-gatewayroute-httpgatewayrouterewrite-prefix
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.HttpGatewayRouteRewrite"
    
    p_Hostname: typing.Union['GatewayRouteGatewayRouteHostnameRewrite', dict] = attr.ib(
        default=None,
        converter=GatewayRouteGatewayRouteHostnameRewrite.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(GatewayRouteGatewayRouteHostnameRewrite)),
        metadata={AttrMeta.PROPERTY_NAME: "Hostname"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite.html#cfn-appmesh-gatewayroute-httpgatewayrouterewrite-hostname"""
    p_Path: typing.Union['GatewayRouteHttpGatewayRoutePathRewrite', dict] = attr.ib(
        default=None,
        converter=GatewayRouteHttpGatewayRoutePathRewrite.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(GatewayRouteHttpGatewayRoutePathRewrite)),
        metadata={AttrMeta.PROPERTY_NAME: "Path"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite.html#cfn-appmesh-gatewayroute-httpgatewayrouterewrite-path"""
    p_Prefix: typing.Union['GatewayRouteHttpGatewayRoutePrefixRewrite', dict] = attr.ib(
        default=None,
        converter=GatewayRouteHttpGatewayRoutePrefixRewrite.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(GatewayRouteHttpGatewayRoutePrefixRewrite)),
        metadata={AttrMeta.PROPERTY_NAME: "Prefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite.html#cfn-appmesh-gatewayroute-httpgatewayrouterewrite-prefix"""

@attr.s
class VirtualNodeListenerTlsAcmCertificate(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.ListenerTlsAcmCertificate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsacmcertificate.html

    Property Document:
    
    - ``rp_CertificateArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsacmcertificate.html#cfn-appmesh-virtualnode-listenertlsacmcertificate-certificatearn
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.ListenerTlsAcmCertificate"
    
    rp_CertificateArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "CertificateArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsacmcertificate.html#cfn-appmesh-virtualnode-listenertlsacmcertificate-certificatearn"""

@attr.s
class RouteGrpcTimeout(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.GrpcTimeout"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpctimeout.html

    Property Document:
    
    - ``p_Idle``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpctimeout.html#cfn-appmesh-route-grpctimeout-idle
    - ``p_PerRequest``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpctimeout.html#cfn-appmesh-route-grpctimeout-perrequest
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.GrpcTimeout"
    
    p_Idle: typing.Union['RouteDuration', dict] = attr.ib(
        default=None,
        converter=RouteDuration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(RouteDuration)),
        metadata={AttrMeta.PROPERTY_NAME: "Idle"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpctimeout.html#cfn-appmesh-route-grpctimeout-idle"""
    p_PerRequest: typing.Union['RouteDuration', dict] = attr.ib(
        default=None,
        converter=RouteDuration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(RouteDuration)),
        metadata={AttrMeta.PROPERTY_NAME: "PerRequest"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpctimeout.html#cfn-appmesh-route-grpctimeout-perrequest"""

@attr.s
class GatewayRouteGatewayRouteHostnameMatch(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.GatewayRouteHostnameMatch"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutehostnamematch.html

    Property Document:
    
    - ``p_Exact``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutehostnamematch.html#cfn-appmesh-gatewayroute-gatewayroutehostnamematch-exact
    - ``p_Suffix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutehostnamematch.html#cfn-appmesh-gatewayroute-gatewayroutehostnamematch-suffix
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.GatewayRouteHostnameMatch"
    
    p_Exact: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Exact"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutehostnamematch.html#cfn-appmesh-gatewayroute-gatewayroutehostnamematch-exact"""
    p_Suffix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Suffix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutehostnamematch.html#cfn-appmesh-gatewayroute-gatewayroutehostnamematch-suffix"""

@attr.s
class VirtualNodeVirtualNodeHttp2ConnectionPool(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.VirtualNodeHttp2ConnectionPool"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodehttp2connectionpool.html

    Property Document:
    
    - ``rp_MaxRequests``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodehttp2connectionpool.html#cfn-appmesh-virtualnode-virtualnodehttp2connectionpool-maxrequests
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.VirtualNodeHttp2ConnectionPool"
    
    rp_MaxRequests: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "MaxRequests"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodehttp2connectionpool.html#cfn-appmesh-virtualnode-virtualnodehttp2connectionpool-maxrequests"""

@attr.s
class VirtualNodeListenerTlsCertificate(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.ListenerTlsCertificate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlscertificate.html

    Property Document:
    
    - ``p_ACM``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlscertificate.html#cfn-appmesh-virtualnode-listenertlscertificate-acm
    - ``p_File``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlscertificate.html#cfn-appmesh-virtualnode-listenertlscertificate-file
    - ``p_SDS``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlscertificate.html#cfn-appmesh-virtualnode-listenertlscertificate-sds
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.ListenerTlsCertificate"
    
    p_ACM: typing.Union['VirtualNodeListenerTlsAcmCertificate', dict] = attr.ib(
        default=None,
        converter=VirtualNodeListenerTlsAcmCertificate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeListenerTlsAcmCertificate)),
        metadata={AttrMeta.PROPERTY_NAME: "ACM"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlscertificate.html#cfn-appmesh-virtualnode-listenertlscertificate-acm"""
    p_File: typing.Union['VirtualNodeListenerTlsFileCertificate', dict] = attr.ib(
        default=None,
        converter=VirtualNodeListenerTlsFileCertificate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeListenerTlsFileCertificate)),
        metadata={AttrMeta.PROPERTY_NAME: "File"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlscertificate.html#cfn-appmesh-virtualnode-listenertlscertificate-file"""
    p_SDS: typing.Union['VirtualNodeListenerTlsSdsCertificate', dict] = attr.ib(
        default=None,
        converter=VirtualNodeListenerTlsSdsCertificate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeListenerTlsSdsCertificate)),
        metadata={AttrMeta.PROPERTY_NAME: "SDS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlscertificate.html#cfn-appmesh-virtualnode-listenertlscertificate-sds"""

@attr.s
class RouteTcpTimeout(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.TcpTimeout"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcptimeout.html

    Property Document:
    
    - ``p_Idle``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcptimeout.html#cfn-appmesh-route-tcptimeout-idle
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.TcpTimeout"
    
    p_Idle: typing.Union['RouteDuration', dict] = attr.ib(
        default=None,
        converter=RouteDuration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(RouteDuration)),
        metadata={AttrMeta.PROPERTY_NAME: "Idle"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcptimeout.html#cfn-appmesh-route-tcptimeout-idle"""

@attr.s
class VirtualGatewayVirtualGatewayFileAccessLog(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayFileAccessLog"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayfileaccesslog.html

    Property Document:
    
    - ``rp_Path``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayfileaccesslog.html#cfn-appmesh-virtualgateway-virtualgatewayfileaccesslog-path
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayFileAccessLog"
    
    rp_Path: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Path"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayfileaccesslog.html#cfn-appmesh-virtualgateway-virtualgatewayfileaccesslog-path"""

@attr.s
class GatewayRouteGatewayRouteVirtualService(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.GatewayRouteVirtualService"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutevirtualservice.html

    Property Document:
    
    - ``rp_VirtualServiceName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutevirtualservice.html#cfn-appmesh-gatewayroute-gatewayroutevirtualservice-virtualservicename
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.GatewayRouteVirtualService"
    
    rp_VirtualServiceName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "VirtualServiceName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutevirtualservice.html#cfn-appmesh-gatewayroute-gatewayroutevirtualservice-virtualservicename"""

@attr.s
class RouteHttpTimeout(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.HttpTimeout"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httptimeout.html

    Property Document:
    
    - ``p_Idle``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httptimeout.html#cfn-appmesh-route-httptimeout-idle
    - ``p_PerRequest``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httptimeout.html#cfn-appmesh-route-httptimeout-perrequest
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.HttpTimeout"
    
    p_Idle: typing.Union['RouteDuration', dict] = attr.ib(
        default=None,
        converter=RouteDuration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(RouteDuration)),
        metadata={AttrMeta.PROPERTY_NAME: "Idle"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httptimeout.html#cfn-appmesh-route-httptimeout-idle"""
    p_PerRequest: typing.Union['RouteDuration', dict] = attr.ib(
        default=None,
        converter=RouteDuration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(RouteDuration)),
        metadata={AttrMeta.PROPERTY_NAME: "PerRequest"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httptimeout.html#cfn-appmesh-route-httptimeout-perrequest"""

@attr.s
class VirtualServiceVirtualServiceSpec(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualService.VirtualServiceSpec"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualservicespec.html

    Property Document:
    
    - ``p_Provider``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualservicespec.html#cfn-appmesh-virtualservice-virtualservicespec-provider
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualService.VirtualServiceSpec"
    
    p_Provider: typing.Union['VirtualServiceVirtualServiceProvider', dict] = attr.ib(
        default=None,
        converter=VirtualServiceVirtualServiceProvider.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualServiceVirtualServiceProvider)),
        metadata={AttrMeta.PROPERTY_NAME: "Provider"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualservicespec.html#cfn-appmesh-virtualservice-virtualservicespec-provider"""

@attr.s
class VirtualGatewayVirtualGatewayHttpConnectionPool(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayHttpConnectionPool"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhttpconnectionpool.html

    Property Document:
    
    - ``rp_MaxConnections``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhttpconnectionpool.html#cfn-appmesh-virtualgateway-virtualgatewayhttpconnectionpool-maxconnections
    - ``p_MaxPendingRequests``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhttpconnectionpool.html#cfn-appmesh-virtualgateway-virtualgatewayhttpconnectionpool-maxpendingrequests
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayHttpConnectionPool"
    
    rp_MaxConnections: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "MaxConnections"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhttpconnectionpool.html#cfn-appmesh-virtualgateway-virtualgatewayhttpconnectionpool-maxconnections"""
    p_MaxPendingRequests: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MaxPendingRequests"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhttpconnectionpool.html#cfn-appmesh-virtualgateway-virtualgatewayhttpconnectionpool-maxpendingrequests"""

@attr.s
class VirtualNodeOutlierDetection(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.OutlierDetection"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-outlierdetection.html

    Property Document:
    
    - ``rp_BaseEjectionDuration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-outlierdetection.html#cfn-appmesh-virtualnode-outlierdetection-baseejectionduration
    - ``rp_Interval``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-outlierdetection.html#cfn-appmesh-virtualnode-outlierdetection-interval
    - ``rp_MaxEjectionPercent``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-outlierdetection.html#cfn-appmesh-virtualnode-outlierdetection-maxejectionpercent
    - ``rp_MaxServerErrors``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-outlierdetection.html#cfn-appmesh-virtualnode-outlierdetection-maxservererrors
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.OutlierDetection"
    
    rp_BaseEjectionDuration: typing.Union['VirtualNodeDuration', dict] = attr.ib(
        default=None,
        converter=VirtualNodeDuration.from_dict,
        validator=attr.validators.instance_of(VirtualNodeDuration),
        metadata={AttrMeta.PROPERTY_NAME: "BaseEjectionDuration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-outlierdetection.html#cfn-appmesh-virtualnode-outlierdetection-baseejectionduration"""
    rp_Interval: typing.Union['VirtualNodeDuration', dict] = attr.ib(
        default=None,
        converter=VirtualNodeDuration.from_dict,
        validator=attr.validators.instance_of(VirtualNodeDuration),
        metadata={AttrMeta.PROPERTY_NAME: "Interval"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-outlierdetection.html#cfn-appmesh-virtualnode-outlierdetection-interval"""
    rp_MaxEjectionPercent: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "MaxEjectionPercent"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-outlierdetection.html#cfn-appmesh-virtualnode-outlierdetection-maxejectionpercent"""
    rp_MaxServerErrors: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "MaxServerErrors"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-outlierdetection.html#cfn-appmesh-virtualnode-outlierdetection-maxservererrors"""

@attr.s
class VirtualGatewayVirtualGatewayHealthCheckPolicy(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayHealthCheckPolicy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html

    Property Document:
    
    - ``rp_HealthyThreshold``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy-healthythreshold
    - ``rp_IntervalMillis``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy-intervalmillis
    - ``rp_Protocol``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy-protocol
    - ``rp_TimeoutMillis``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy-timeoutmillis
    - ``rp_UnhealthyThreshold``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy-unhealthythreshold
    - ``p_Path``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy-path
    - ``p_Port``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy-port
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayHealthCheckPolicy"
    
    rp_HealthyThreshold: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "HealthyThreshold"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy-healthythreshold"""
    rp_IntervalMillis: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "IntervalMillis"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy-intervalmillis"""
    rp_Protocol: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Protocol"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy-protocol"""
    rp_TimeoutMillis: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "TimeoutMillis"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy-timeoutmillis"""
    rp_UnhealthyThreshold: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "UnhealthyThreshold"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy-unhealthythreshold"""
    p_Path: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Path"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy-path"""
    p_Port: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Port"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy-port"""

@attr.s
class GatewayRouteHttpPathMatch(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.HttpPathMatch"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httppathmatch.html

    Property Document:
    
    - ``p_Exact``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httppathmatch.html#cfn-appmesh-gatewayroute-httppathmatch-exact
    - ``p_Regex``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httppathmatch.html#cfn-appmesh-gatewayroute-httppathmatch-regex
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.HttpPathMatch"
    
    p_Exact: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Exact"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httppathmatch.html#cfn-appmesh-gatewayroute-httppathmatch-exact"""
    p_Regex: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Regex"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httppathmatch.html#cfn-appmesh-gatewayroute-httppathmatch-regex"""

@attr.s
class VirtualNodeTlsValidationContextAcmTrust(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.TlsValidationContextAcmTrust"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontextacmtrust.html

    Property Document:
    
    - ``rp_CertificateAuthorityArns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontextacmtrust.html#cfn-appmesh-virtualnode-tlsvalidationcontextacmtrust-certificateauthorityarns
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.TlsValidationContextAcmTrust"
    
    rp_CertificateAuthorityArns: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "CertificateAuthorityArns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontextacmtrust.html#cfn-appmesh-virtualnode-tlsvalidationcontextacmtrust-certificateauthorityarns"""

@attr.s
class MeshEgressFilter(Property):
    """
    AWS Object Type = "AWS::AppMesh::Mesh.EgressFilter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-egressfilter.html

    Property Document:
    
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-egressfilter.html#cfn-appmesh-mesh-egressfilter-type
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Mesh.EgressFilter"
    
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-egressfilter.html#cfn-appmesh-mesh-egressfilter-type"""

@attr.s
class VirtualNodeClientTlsCertificate(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.ClientTlsCertificate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clienttlscertificate.html

    Property Document:
    
    - ``p_File``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clienttlscertificate.html#cfn-appmesh-virtualnode-clienttlscertificate-file
    - ``p_SDS``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clienttlscertificate.html#cfn-appmesh-virtualnode-clienttlscertificate-sds
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.ClientTlsCertificate"
    
    p_File: typing.Union['VirtualNodeListenerTlsFileCertificate', dict] = attr.ib(
        default=None,
        converter=VirtualNodeListenerTlsFileCertificate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeListenerTlsFileCertificate)),
        metadata={AttrMeta.PROPERTY_NAME: "File"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clienttlscertificate.html#cfn-appmesh-virtualnode-clienttlscertificate-file"""
    p_SDS: typing.Union['VirtualNodeListenerTlsSdsCertificate', dict] = attr.ib(
        default=None,
        converter=VirtualNodeListenerTlsSdsCertificate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeListenerTlsSdsCertificate)),
        metadata={AttrMeta.PROPERTY_NAME: "SDS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clienttlscertificate.html#cfn-appmesh-virtualnode-clienttlscertificate-sds"""

@attr.s
class VirtualNodeListenerTlsValidationContextTrust(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.ListenerTlsValidationContextTrust"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontexttrust.html

    Property Document:
    
    - ``p_File``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontexttrust.html#cfn-appmesh-virtualnode-listenertlsvalidationcontexttrust-file
    - ``p_SDS``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontexttrust.html#cfn-appmesh-virtualnode-listenertlsvalidationcontexttrust-sds
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.ListenerTlsValidationContextTrust"
    
    p_File: typing.Union['VirtualNodeTlsValidationContextFileTrust', dict] = attr.ib(
        default=None,
        converter=VirtualNodeTlsValidationContextFileTrust.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeTlsValidationContextFileTrust)),
        metadata={AttrMeta.PROPERTY_NAME: "File"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontexttrust.html#cfn-appmesh-virtualnode-listenertlsvalidationcontexttrust-file"""
    p_SDS: typing.Union['VirtualNodeTlsValidationContextSdsTrust', dict] = attr.ib(
        default=None,
        converter=VirtualNodeTlsValidationContextSdsTrust.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeTlsValidationContextSdsTrust)),
        metadata={AttrMeta.PROPERTY_NAME: "SDS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontexttrust.html#cfn-appmesh-virtualnode-listenertlsvalidationcontexttrust-sds"""

@attr.s
class VirtualGatewayVirtualGatewayTlsValidationContextAcmTrust(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayTlsValidationContextAcmTrust"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextacmtrust.html

    Property Document:
    
    - ``rp_CertificateAuthorityArns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextacmtrust.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextacmtrust-certificateauthorityarns
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayTlsValidationContextAcmTrust"
    
    rp_CertificateAuthorityArns: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "CertificateAuthorityArns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextacmtrust.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextacmtrust-certificateauthorityarns"""

@attr.s
class RouteHttpRouteAction(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.HttpRouteAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteaction.html

    Property Document:
    
    - ``rp_WeightedTargets``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteaction.html#cfn-appmesh-route-httprouteaction-weightedtargets
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.HttpRouteAction"
    
    rp_WeightedTargets: typing.List[typing.Union['RouteWeightedTarget', dict]] = attr.ib(
        default=None,
        converter=RouteWeightedTarget.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(RouteWeightedTarget), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "WeightedTargets"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteaction.html#cfn-appmesh-route-httprouteaction-weightedtargets"""

@attr.s
class VirtualNodeAccessLog(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.AccessLog"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-accesslog.html

    Property Document:
    
    - ``p_File``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-accesslog.html#cfn-appmesh-virtualnode-accesslog-file
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.AccessLog"
    
    p_File: typing.Union['VirtualNodeFileAccessLog', dict] = attr.ib(
        default=None,
        converter=VirtualNodeFileAccessLog.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeFileAccessLog)),
        metadata={AttrMeta.PROPERTY_NAME: "File"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-accesslog.html#cfn-appmesh-virtualnode-accesslog-file"""

@attr.s
class VirtualGatewayVirtualGatewayListenerTlsValidationContextTrust(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTlsValidationContextTrust"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust.html

    Property Document:
    
    - ``p_File``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust-file
    - ``p_SDS``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust-sds
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTlsValidationContextTrust"
    
    p_File: typing.Union['VirtualGatewayVirtualGatewayTlsValidationContextFileTrust', dict] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewayTlsValidationContextFileTrust.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualGatewayVirtualGatewayTlsValidationContextFileTrust)),
        metadata={AttrMeta.PROPERTY_NAME: "File"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust-file"""
    p_SDS: typing.Union['VirtualGatewayVirtualGatewayTlsValidationContextSdsTrust', dict] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewayTlsValidationContextSdsTrust.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualGatewayVirtualGatewayTlsValidationContextSdsTrust)),
        metadata={AttrMeta.PROPERTY_NAME: "SDS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust-sds"""

@attr.s
class VirtualGatewayVirtualGatewayListenerTlsSdsCertificate(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTlsSdsCertificate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlssdscertificate.html

    Property Document:
    
    - ``rp_SecretName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlssdscertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlssdscertificate-secretname
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTlsSdsCertificate"
    
    rp_SecretName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SecretName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlssdscertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlssdscertificate-secretname"""

@attr.s
class VirtualNodeSubjectAlternativeNameMatchers(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.SubjectAlternativeNameMatchers"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-subjectalternativenamematchers.html

    Property Document:
    
    - ``p_Exact``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-subjectalternativenamematchers.html#cfn-appmesh-virtualnode-subjectalternativenamematchers-exact
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.SubjectAlternativeNameMatchers"
    
    p_Exact: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Exact"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-subjectalternativenamematchers.html#cfn-appmesh-virtualnode-subjectalternativenamematchers-exact"""

@attr.s
class VirtualNodeSubjectAlternativeNames(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.SubjectAlternativeNames"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-subjectalternativenames.html

    Property Document:
    
    - ``rp_Match``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-subjectalternativenames.html#cfn-appmesh-virtualnode-subjectalternativenames-match
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.SubjectAlternativeNames"
    
    rp_Match: typing.Union['VirtualNodeSubjectAlternativeNameMatchers', dict] = attr.ib(
        default=None,
        converter=VirtualNodeSubjectAlternativeNameMatchers.from_dict,
        validator=attr.validators.instance_of(VirtualNodeSubjectAlternativeNameMatchers),
        metadata={AttrMeta.PROPERTY_NAME: "Match"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-subjectalternativenames.html#cfn-appmesh-virtualnode-subjectalternativenames-match"""

@attr.s
class VirtualNodeVirtualNodeGrpcConnectionPool(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.VirtualNodeGrpcConnectionPool"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodegrpcconnectionpool.html

    Property Document:
    
    - ``rp_MaxRequests``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodegrpcconnectionpool.html#cfn-appmesh-virtualnode-virtualnodegrpcconnectionpool-maxrequests
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.VirtualNodeGrpcConnectionPool"
    
    rp_MaxRequests: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "MaxRequests"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodegrpcconnectionpool.html#cfn-appmesh-virtualnode-virtualnodegrpcconnectionpool-maxrequests"""

@attr.s
class RouteMatchRange(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.MatchRange"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-matchrange.html

    Property Document:
    
    - ``rp_End``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-matchrange.html#cfn-appmesh-route-matchrange-end
    - ``rp_Start``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-matchrange.html#cfn-appmesh-route-matchrange-start
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.MatchRange"
    
    rp_End: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "End"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-matchrange.html#cfn-appmesh-route-matchrange-end"""
    rp_Start: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Start"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-matchrange.html#cfn-appmesh-route-matchrange-start"""

@attr.s
class VirtualGatewayVirtualGatewayTlsValidationContextTrust(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayTlsValidationContextTrust"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust.html

    Property Document:
    
    - ``p_ACM``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-acm
    - ``p_File``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-file
    - ``p_SDS``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-sds
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayTlsValidationContextTrust"
    
    p_ACM: typing.Union['VirtualGatewayVirtualGatewayTlsValidationContextAcmTrust', dict] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewayTlsValidationContextAcmTrust.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualGatewayVirtualGatewayTlsValidationContextAcmTrust)),
        metadata={AttrMeta.PROPERTY_NAME: "ACM"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-acm"""
    p_File: typing.Union['VirtualGatewayVirtualGatewayTlsValidationContextFileTrust', dict] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewayTlsValidationContextFileTrust.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualGatewayVirtualGatewayTlsValidationContextFileTrust)),
        metadata={AttrMeta.PROPERTY_NAME: "File"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-file"""
    p_SDS: typing.Union['VirtualGatewayVirtualGatewayTlsValidationContextSdsTrust', dict] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewayTlsValidationContextSdsTrust.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualGatewayVirtualGatewayTlsValidationContextSdsTrust)),
        metadata={AttrMeta.PROPERTY_NAME: "SDS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-sds"""

@attr.s
class RouteGrpcRouteMetadataMatchMethod(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.GrpcRouteMetadataMatchMethod"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadatamatchmethod.html

    Property Document:
    
    - ``p_Exact``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadatamatchmethod.html#cfn-appmesh-route-grpcroutemetadatamatchmethod-exact
    - ``p_Prefix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadatamatchmethod.html#cfn-appmesh-route-grpcroutemetadatamatchmethod-prefix
    - ``p_Range``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadatamatchmethod.html#cfn-appmesh-route-grpcroutemetadatamatchmethod-range
    - ``p_Regex``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadatamatchmethod.html#cfn-appmesh-route-grpcroutemetadatamatchmethod-regex
    - ``p_Suffix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadatamatchmethod.html#cfn-appmesh-route-grpcroutemetadatamatchmethod-suffix
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.GrpcRouteMetadataMatchMethod"
    
    p_Exact: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Exact"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadatamatchmethod.html#cfn-appmesh-route-grpcroutemetadatamatchmethod-exact"""
    p_Prefix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Prefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadatamatchmethod.html#cfn-appmesh-route-grpcroutemetadatamatchmethod-prefix"""
    p_Range: typing.Union['RouteMatchRange', dict] = attr.ib(
        default=None,
        converter=RouteMatchRange.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(RouteMatchRange)),
        metadata={AttrMeta.PROPERTY_NAME: "Range"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadatamatchmethod.html#cfn-appmesh-route-grpcroutemetadatamatchmethod-range"""
    p_Regex: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Regex"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadatamatchmethod.html#cfn-appmesh-route-grpcroutemetadatamatchmethod-regex"""
    p_Suffix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Suffix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadatamatchmethod.html#cfn-appmesh-route-grpcroutemetadatamatchmethod-suffix"""

@attr.s
class GatewayRouteHttpGatewayRouteHeaderMatch(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.HttpGatewayRouteHeaderMatch"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheadermatch.html

    Property Document:
    
    - ``p_Exact``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheadermatch.html#cfn-appmesh-gatewayroute-httpgatewayrouteheadermatch-exact
    - ``p_Prefix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheadermatch.html#cfn-appmesh-gatewayroute-httpgatewayrouteheadermatch-prefix
    - ``p_Range``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheadermatch.html#cfn-appmesh-gatewayroute-httpgatewayrouteheadermatch-range
    - ``p_Regex``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheadermatch.html#cfn-appmesh-gatewayroute-httpgatewayrouteheadermatch-regex
    - ``p_Suffix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheadermatch.html#cfn-appmesh-gatewayroute-httpgatewayrouteheadermatch-suffix
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.HttpGatewayRouteHeaderMatch"
    
    p_Exact: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Exact"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheadermatch.html#cfn-appmesh-gatewayroute-httpgatewayrouteheadermatch-exact"""
    p_Prefix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Prefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheadermatch.html#cfn-appmesh-gatewayroute-httpgatewayrouteheadermatch-prefix"""
    p_Range: typing.Union['GatewayRouteGatewayRouteRangeMatch', dict] = attr.ib(
        default=None,
        converter=GatewayRouteGatewayRouteRangeMatch.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(GatewayRouteGatewayRouteRangeMatch)),
        metadata={AttrMeta.PROPERTY_NAME: "Range"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheadermatch.html#cfn-appmesh-gatewayroute-httpgatewayrouteheadermatch-range"""
    p_Regex: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Regex"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheadermatch.html#cfn-appmesh-gatewayroute-httpgatewayrouteheadermatch-regex"""
    p_Suffix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Suffix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheadermatch.html#cfn-appmesh-gatewayroute-httpgatewayrouteheadermatch-suffix"""

@attr.s
class RouteHeaderMatchMethod(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.HeaderMatchMethod"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-headermatchmethod.html

    Property Document:
    
    - ``p_Exact``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-headermatchmethod.html#cfn-appmesh-route-headermatchmethod-exact
    - ``p_Prefix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-headermatchmethod.html#cfn-appmesh-route-headermatchmethod-prefix
    - ``p_Range``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-headermatchmethod.html#cfn-appmesh-route-headermatchmethod-range
    - ``p_Regex``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-headermatchmethod.html#cfn-appmesh-route-headermatchmethod-regex
    - ``p_Suffix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-headermatchmethod.html#cfn-appmesh-route-headermatchmethod-suffix
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.HeaderMatchMethod"
    
    p_Exact: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Exact"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-headermatchmethod.html#cfn-appmesh-route-headermatchmethod-exact"""
    p_Prefix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Prefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-headermatchmethod.html#cfn-appmesh-route-headermatchmethod-prefix"""
    p_Range: typing.Union['RouteMatchRange', dict] = attr.ib(
        default=None,
        converter=RouteMatchRange.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(RouteMatchRange)),
        metadata={AttrMeta.PROPERTY_NAME: "Range"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-headermatchmethod.html#cfn-appmesh-route-headermatchmethod-range"""
    p_Regex: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Regex"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-headermatchmethod.html#cfn-appmesh-route-headermatchmethod-regex"""
    p_Suffix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Suffix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-headermatchmethod.html#cfn-appmesh-route-headermatchmethod-suffix"""

@attr.s
class GatewayRouteHttpGatewayRouteHeader(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.HttpGatewayRouteHeader"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheader.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheader.html#cfn-appmesh-gatewayroute-httpgatewayrouteheader-name
    - ``p_Invert``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheader.html#cfn-appmesh-gatewayroute-httpgatewayrouteheader-invert
    - ``p_Match``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheader.html#cfn-appmesh-gatewayroute-httpgatewayrouteheader-match
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.HttpGatewayRouteHeader"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheader.html#cfn-appmesh-gatewayroute-httpgatewayrouteheader-name"""
    p_Invert: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Invert"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheader.html#cfn-appmesh-gatewayroute-httpgatewayrouteheader-invert"""
    p_Match: typing.Union['GatewayRouteHttpGatewayRouteHeaderMatch', dict] = attr.ib(
        default=None,
        converter=GatewayRouteHttpGatewayRouteHeaderMatch.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(GatewayRouteHttpGatewayRouteHeaderMatch)),
        metadata={AttrMeta.PROPERTY_NAME: "Match"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheader.html#cfn-appmesh-gatewayroute-httpgatewayrouteheader-match"""

@attr.s
class VirtualNodeListenerTlsValidationContext(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.ListenerTlsValidationContext"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontext.html

    Property Document:
    
    - ``rp_Trust``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontext.html#cfn-appmesh-virtualnode-listenertlsvalidationcontext-trust
    - ``p_SubjectAlternativeNames``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontext.html#cfn-appmesh-virtualnode-listenertlsvalidationcontext-subjectalternativenames
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.ListenerTlsValidationContext"
    
    rp_Trust: typing.Union['VirtualNodeListenerTlsValidationContextTrust', dict] = attr.ib(
        default=None,
        converter=VirtualNodeListenerTlsValidationContextTrust.from_dict,
        validator=attr.validators.instance_of(VirtualNodeListenerTlsValidationContextTrust),
        metadata={AttrMeta.PROPERTY_NAME: "Trust"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontext.html#cfn-appmesh-virtualnode-listenertlsvalidationcontext-trust"""
    p_SubjectAlternativeNames: typing.Union['VirtualNodeSubjectAlternativeNames', dict] = attr.ib(
        default=None,
        converter=VirtualNodeSubjectAlternativeNames.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeSubjectAlternativeNames)),
        metadata={AttrMeta.PROPERTY_NAME: "SubjectAlternativeNames"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontext.html#cfn-appmesh-virtualnode-listenertlsvalidationcontext-subjectalternativenames"""

@attr.s
class VirtualNodeTcpTimeout(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.TcpTimeout"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tcptimeout.html

    Property Document:
    
    - ``p_Idle``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tcptimeout.html#cfn-appmesh-virtualnode-tcptimeout-idle
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.TcpTimeout"
    
    p_Idle: typing.Union['VirtualNodeDuration', dict] = attr.ib(
        default=None,
        converter=VirtualNodeDuration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeDuration)),
        metadata={AttrMeta.PROPERTY_NAME: "Idle"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tcptimeout.html#cfn-appmesh-virtualnode-tcptimeout-idle"""

@attr.s
class VirtualNodeListenerTls(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.ListenerTls"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertls.html

    Property Document:
    
    - ``rp_Certificate``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertls.html#cfn-appmesh-virtualnode-listenertls-certificate
    - ``rp_Mode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertls.html#cfn-appmesh-virtualnode-listenertls-mode
    - ``p_Validation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertls.html#cfn-appmesh-virtualnode-listenertls-validation
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.ListenerTls"
    
    rp_Certificate: typing.Union['VirtualNodeListenerTlsCertificate', dict] = attr.ib(
        default=None,
        converter=VirtualNodeListenerTlsCertificate.from_dict,
        validator=attr.validators.instance_of(VirtualNodeListenerTlsCertificate),
        metadata={AttrMeta.PROPERTY_NAME: "Certificate"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertls.html#cfn-appmesh-virtualnode-listenertls-certificate"""
    rp_Mode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Mode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertls.html#cfn-appmesh-virtualnode-listenertls-mode"""
    p_Validation: typing.Union['VirtualNodeListenerTlsValidationContext', dict] = attr.ib(
        default=None,
        converter=VirtualNodeListenerTlsValidationContext.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeListenerTlsValidationContext)),
        metadata={AttrMeta.PROPERTY_NAME: "Validation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertls.html#cfn-appmesh-virtualnode-listenertls-validation"""

@attr.s
class VirtualGatewayVirtualGatewayListenerTlsCertificate(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTlsCertificate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlscertificate.html

    Property Document:
    
    - ``p_ACM``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlscertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-acm
    - ``p_File``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlscertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-file
    - ``p_SDS``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlscertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-sds
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTlsCertificate"
    
    p_ACM: typing.Union['VirtualGatewayVirtualGatewayListenerTlsAcmCertificate', dict] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewayListenerTlsAcmCertificate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualGatewayVirtualGatewayListenerTlsAcmCertificate)),
        metadata={AttrMeta.PROPERTY_NAME: "ACM"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlscertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-acm"""
    p_File: typing.Union['VirtualGatewayVirtualGatewayListenerTlsFileCertificate', dict] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewayListenerTlsFileCertificate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualGatewayVirtualGatewayListenerTlsFileCertificate)),
        metadata={AttrMeta.PROPERTY_NAME: "File"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlscertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-file"""
    p_SDS: typing.Union['VirtualGatewayVirtualGatewayListenerTlsSdsCertificate', dict] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewayListenerTlsSdsCertificate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualGatewayVirtualGatewayListenerTlsSdsCertificate)),
        metadata={AttrMeta.PROPERTY_NAME: "SDS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlscertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-sds"""

@attr.s
class GatewayRouteGatewayRouteMetadataMatch(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.GatewayRouteMetadataMatch"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutemetadatamatch.html

    Property Document:
    
    - ``p_Exact``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutemetadatamatch.html#cfn-appmesh-gatewayroute-gatewayroutemetadatamatch-exact
    - ``p_Prefix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutemetadatamatch.html#cfn-appmesh-gatewayroute-gatewayroutemetadatamatch-prefix
    - ``p_Range``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutemetadatamatch.html#cfn-appmesh-gatewayroute-gatewayroutemetadatamatch-range
    - ``p_Regex``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutemetadatamatch.html#cfn-appmesh-gatewayroute-gatewayroutemetadatamatch-regex
    - ``p_Suffix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutemetadatamatch.html#cfn-appmesh-gatewayroute-gatewayroutemetadatamatch-suffix
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.GatewayRouteMetadataMatch"
    
    p_Exact: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Exact"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutemetadatamatch.html#cfn-appmesh-gatewayroute-gatewayroutemetadatamatch-exact"""
    p_Prefix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Prefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutemetadatamatch.html#cfn-appmesh-gatewayroute-gatewayroutemetadatamatch-prefix"""
    p_Range: typing.Union['GatewayRouteGatewayRouteRangeMatch', dict] = attr.ib(
        default=None,
        converter=GatewayRouteGatewayRouteRangeMatch.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(GatewayRouteGatewayRouteRangeMatch)),
        metadata={AttrMeta.PROPERTY_NAME: "Range"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutemetadatamatch.html#cfn-appmesh-gatewayroute-gatewayroutemetadatamatch-range"""
    p_Regex: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Regex"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutemetadatamatch.html#cfn-appmesh-gatewayroute-gatewayroutemetadatamatch-regex"""
    p_Suffix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Suffix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutemetadatamatch.html#cfn-appmesh-gatewayroute-gatewayroutemetadatamatch-suffix"""

@attr.s
class VirtualGatewayVirtualGatewayConnectionPool(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayConnectionPool"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayconnectionpool.html

    Property Document:
    
    - ``p_GRPC``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayconnectionpool.html#cfn-appmesh-virtualgateway-virtualgatewayconnectionpool-grpc
    - ``p_HTTP``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayconnectionpool.html#cfn-appmesh-virtualgateway-virtualgatewayconnectionpool-http
    - ``p_HTTP2``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayconnectionpool.html#cfn-appmesh-virtualgateway-virtualgatewayconnectionpool-http2
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayConnectionPool"
    
    p_GRPC: typing.Union['VirtualGatewayVirtualGatewayGrpcConnectionPool', dict] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewayGrpcConnectionPool.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualGatewayVirtualGatewayGrpcConnectionPool)),
        metadata={AttrMeta.PROPERTY_NAME: "GRPC"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayconnectionpool.html#cfn-appmesh-virtualgateway-virtualgatewayconnectionpool-grpc"""
    p_HTTP: typing.Union['VirtualGatewayVirtualGatewayHttpConnectionPool', dict] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewayHttpConnectionPool.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualGatewayVirtualGatewayHttpConnectionPool)),
        metadata={AttrMeta.PROPERTY_NAME: "HTTP"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayconnectionpool.html#cfn-appmesh-virtualgateway-virtualgatewayconnectionpool-http"""
    p_HTTP2: typing.Union['VirtualGatewayVirtualGatewayHttp2ConnectionPool', dict] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewayHttp2ConnectionPool.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualGatewayVirtualGatewayHttp2ConnectionPool)),
        metadata={AttrMeta.PROPERTY_NAME: "HTTP2"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayconnectionpool.html#cfn-appmesh-virtualgateway-virtualgatewayconnectionpool-http2"""

@attr.s
class VirtualGatewaySubjectAlternativeNames(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.SubjectAlternativeNames"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-subjectalternativenames.html

    Property Document:
    
    - ``rp_Match``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-subjectalternativenames.html#cfn-appmesh-virtualgateway-subjectalternativenames-match
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.SubjectAlternativeNames"
    
    rp_Match: typing.Union['VirtualGatewaySubjectAlternativeNameMatchers', dict] = attr.ib(
        default=None,
        converter=VirtualGatewaySubjectAlternativeNameMatchers.from_dict,
        validator=attr.validators.instance_of(VirtualGatewaySubjectAlternativeNameMatchers),
        metadata={AttrMeta.PROPERTY_NAME: "Match"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-subjectalternativenames.html#cfn-appmesh-virtualgateway-subjectalternativenames-match"""

@attr.s
class RouteGrpcRouteMetadata(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.GrpcRouteMetadata"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadata.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadata.html#cfn-appmesh-route-grpcroutemetadata-name
    - ``p_Invert``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadata.html#cfn-appmesh-route-grpcroutemetadata-invert
    - ``p_Match``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadata.html#cfn-appmesh-route-grpcroutemetadata-match
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.GrpcRouteMetadata"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadata.html#cfn-appmesh-route-grpcroutemetadata-name"""
    p_Invert: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Invert"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadata.html#cfn-appmesh-route-grpcroutemetadata-invert"""
    p_Match: typing.Union['RouteGrpcRouteMetadataMatchMethod', dict] = attr.ib(
        default=None,
        converter=RouteGrpcRouteMetadataMatchMethod.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(RouteGrpcRouteMetadataMatchMethod)),
        metadata={AttrMeta.PROPERTY_NAME: "Match"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadata.html#cfn-appmesh-route-grpcroutemetadata-match"""

@attr.s
class RouteQueryParameter(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.QueryParameter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-queryparameter.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-queryparameter.html#cfn-appmesh-route-queryparameter-name
    - ``p_Match``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-queryparameter.html#cfn-appmesh-route-queryparameter-match
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.QueryParameter"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-queryparameter.html#cfn-appmesh-route-queryparameter-name"""
    p_Match: typing.Union['RouteHttpQueryParameterMatch', dict] = attr.ib(
        default=None,
        converter=RouteHttpQueryParameterMatch.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(RouteHttpQueryParameterMatch)),
        metadata={AttrMeta.PROPERTY_NAME: "Match"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-queryparameter.html#cfn-appmesh-route-queryparameter-match"""

@attr.s
class GatewayRouteGatewayRouteTarget(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.GatewayRouteTarget"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutetarget.html

    Property Document:
    
    - ``rp_VirtualService``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutetarget.html#cfn-appmesh-gatewayroute-gatewayroutetarget-virtualservice
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.GatewayRouteTarget"
    
    rp_VirtualService: typing.Union['GatewayRouteGatewayRouteVirtualService', dict] = attr.ib(
        default=None,
        converter=GatewayRouteGatewayRouteVirtualService.from_dict,
        validator=attr.validators.instance_of(GatewayRouteGatewayRouteVirtualService),
        metadata={AttrMeta.PROPERTY_NAME: "VirtualService"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutetarget.html#cfn-appmesh-gatewayroute-gatewayroutetarget-virtualservice"""

@attr.s
class VirtualNodeHttpTimeout(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.HttpTimeout"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-httptimeout.html

    Property Document:
    
    - ``p_Idle``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-httptimeout.html#cfn-appmesh-virtualnode-httptimeout-idle
    - ``p_PerRequest``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-httptimeout.html#cfn-appmesh-virtualnode-httptimeout-perrequest
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.HttpTimeout"
    
    p_Idle: typing.Union['VirtualNodeDuration', dict] = attr.ib(
        default=None,
        converter=VirtualNodeDuration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeDuration)),
        metadata={AttrMeta.PROPERTY_NAME: "Idle"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-httptimeout.html#cfn-appmesh-virtualnode-httptimeout-idle"""
    p_PerRequest: typing.Union['VirtualNodeDuration', dict] = attr.ib(
        default=None,
        converter=VirtualNodeDuration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeDuration)),
        metadata={AttrMeta.PROPERTY_NAME: "PerRequest"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-httptimeout.html#cfn-appmesh-virtualnode-httptimeout-perrequest"""

@attr.s
class VirtualGatewayVirtualGatewayClientTlsCertificate(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayClientTlsCertificate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclienttlscertificate.html

    Property Document:
    
    - ``p_File``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclienttlscertificate.html#cfn-appmesh-virtualgateway-virtualgatewayclienttlscertificate-file
    - ``p_SDS``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclienttlscertificate.html#cfn-appmesh-virtualgateway-virtualgatewayclienttlscertificate-sds
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayClientTlsCertificate"
    
    p_File: typing.Union['VirtualGatewayVirtualGatewayListenerTlsFileCertificate', dict] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewayListenerTlsFileCertificate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualGatewayVirtualGatewayListenerTlsFileCertificate)),
        metadata={AttrMeta.PROPERTY_NAME: "File"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclienttlscertificate.html#cfn-appmesh-virtualgateway-virtualgatewayclienttlscertificate-file"""
    p_SDS: typing.Union['VirtualGatewayVirtualGatewayListenerTlsSdsCertificate', dict] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewayListenerTlsSdsCertificate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualGatewayVirtualGatewayListenerTlsSdsCertificate)),
        metadata={AttrMeta.PROPERTY_NAME: "SDS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclienttlscertificate.html#cfn-appmesh-virtualgateway-virtualgatewayclienttlscertificate-sds"""

@attr.s
class VirtualGatewayVirtualGatewayListenerTlsValidationContext(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTlsValidationContext"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext.html

    Property Document:
    
    - ``rp_Trust``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext-trust
    - ``p_SubjectAlternativeNames``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext-subjectalternativenames
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTlsValidationContext"
    
    rp_Trust: typing.Union['VirtualGatewayVirtualGatewayListenerTlsValidationContextTrust', dict] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewayListenerTlsValidationContextTrust.from_dict,
        validator=attr.validators.instance_of(VirtualGatewayVirtualGatewayListenerTlsValidationContextTrust),
        metadata={AttrMeta.PROPERTY_NAME: "Trust"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext-trust"""
    p_SubjectAlternativeNames: typing.Union['VirtualGatewaySubjectAlternativeNames', dict] = attr.ib(
        default=None,
        converter=VirtualGatewaySubjectAlternativeNames.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualGatewaySubjectAlternativeNames)),
        metadata={AttrMeta.PROPERTY_NAME: "SubjectAlternativeNames"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext-subjectalternativenames"""

@attr.s
class VirtualRouterVirtualRouterSpec(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualRouter.VirtualRouterSpec"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-virtualrouterspec.html

    Property Document:
    
    - ``rp_Listeners``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-virtualrouterspec.html#cfn-appmesh-virtualrouter-virtualrouterspec-listeners
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualRouter.VirtualRouterSpec"
    
    rp_Listeners: typing.List[typing.Union['VirtualRouterVirtualRouterListener', dict]] = attr.ib(
        default=None,
        converter=VirtualRouterVirtualRouterListener.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(VirtualRouterVirtualRouterListener), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Listeners"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-virtualrouterspec.html#cfn-appmesh-virtualrouter-virtualrouterspec-listeners"""

@attr.s
class VirtualGatewayVirtualGatewayListenerTls(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTls"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertls.html

    Property Document:
    
    - ``rp_Certificate``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertls.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertls-certificate
    - ``rp_Mode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertls.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertls-mode
    - ``p_Validation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertls.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertls-validation
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTls"
    
    rp_Certificate: typing.Union['VirtualGatewayVirtualGatewayListenerTlsCertificate', dict] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewayListenerTlsCertificate.from_dict,
        validator=attr.validators.instance_of(VirtualGatewayVirtualGatewayListenerTlsCertificate),
        metadata={AttrMeta.PROPERTY_NAME: "Certificate"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertls.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertls-certificate"""
    rp_Mode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Mode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertls.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertls-mode"""
    p_Validation: typing.Union['VirtualGatewayVirtualGatewayListenerTlsValidationContext', dict] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewayListenerTlsValidationContext.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualGatewayVirtualGatewayListenerTlsValidationContext)),
        metadata={AttrMeta.PROPERTY_NAME: "Validation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertls.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertls-validation"""

@attr.s
class RouteGrpcRouteMatch(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.GrpcRouteMatch"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutematch.html

    Property Document:
    
    - ``p_Metadata``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutematch.html#cfn-appmesh-route-grpcroutematch-metadata
    - ``p_MethodName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutematch.html#cfn-appmesh-route-grpcroutematch-methodname
    - ``p_ServiceName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutematch.html#cfn-appmesh-route-grpcroutematch-servicename
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.GrpcRouteMatch"
    
    p_Metadata: typing.List[typing.Union['RouteGrpcRouteMetadata', dict]] = attr.ib(
        default=None,
        converter=RouteGrpcRouteMetadata.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(RouteGrpcRouteMetadata), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Metadata"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutematch.html#cfn-appmesh-route-grpcroutematch-metadata"""
    p_MethodName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MethodName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutematch.html#cfn-appmesh-route-grpcroutematch-methodname"""
    p_ServiceName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ServiceName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutematch.html#cfn-appmesh-route-grpcroutematch-servicename"""

@attr.s
class VirtualNodeGrpcTimeout(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.GrpcTimeout"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-grpctimeout.html

    Property Document:
    
    - ``p_Idle``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-grpctimeout.html#cfn-appmesh-virtualnode-grpctimeout-idle
    - ``p_PerRequest``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-grpctimeout.html#cfn-appmesh-virtualnode-grpctimeout-perrequest
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.GrpcTimeout"
    
    p_Idle: typing.Union['VirtualNodeDuration', dict] = attr.ib(
        default=None,
        converter=VirtualNodeDuration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeDuration)),
        metadata={AttrMeta.PROPERTY_NAME: "Idle"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-grpctimeout.html#cfn-appmesh-virtualnode-grpctimeout-idle"""
    p_PerRequest: typing.Union['VirtualNodeDuration', dict] = attr.ib(
        default=None,
        converter=VirtualNodeDuration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeDuration)),
        metadata={AttrMeta.PROPERTY_NAME: "PerRequest"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-grpctimeout.html#cfn-appmesh-virtualnode-grpctimeout-perrequest"""

@attr.s
class VirtualNodeVirtualNodeConnectionPool(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.VirtualNodeConnectionPool"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodeconnectionpool.html

    Property Document:
    
    - ``p_GRPC``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodeconnectionpool.html#cfn-appmesh-virtualnode-virtualnodeconnectionpool-grpc
    - ``p_HTTP``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodeconnectionpool.html#cfn-appmesh-virtualnode-virtualnodeconnectionpool-http
    - ``p_HTTP2``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodeconnectionpool.html#cfn-appmesh-virtualnode-virtualnodeconnectionpool-http2
    - ``p_TCP``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodeconnectionpool.html#cfn-appmesh-virtualnode-virtualnodeconnectionpool-tcp
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.VirtualNodeConnectionPool"
    
    p_GRPC: typing.Union['VirtualNodeVirtualNodeGrpcConnectionPool', dict] = attr.ib(
        default=None,
        converter=VirtualNodeVirtualNodeGrpcConnectionPool.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeVirtualNodeGrpcConnectionPool)),
        metadata={AttrMeta.PROPERTY_NAME: "GRPC"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodeconnectionpool.html#cfn-appmesh-virtualnode-virtualnodeconnectionpool-grpc"""
    p_HTTP: typing.Union['VirtualNodeVirtualNodeHttpConnectionPool', dict] = attr.ib(
        default=None,
        converter=VirtualNodeVirtualNodeHttpConnectionPool.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeVirtualNodeHttpConnectionPool)),
        metadata={AttrMeta.PROPERTY_NAME: "HTTP"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodeconnectionpool.html#cfn-appmesh-virtualnode-virtualnodeconnectionpool-http"""
    p_HTTP2: typing.Union['VirtualNodeVirtualNodeHttp2ConnectionPool', dict] = attr.ib(
        default=None,
        converter=VirtualNodeVirtualNodeHttp2ConnectionPool.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeVirtualNodeHttp2ConnectionPool)),
        metadata={AttrMeta.PROPERTY_NAME: "HTTP2"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodeconnectionpool.html#cfn-appmesh-virtualnode-virtualnodeconnectionpool-http2"""
    p_TCP: typing.Union['VirtualNodeVirtualNodeTcpConnectionPool', dict] = attr.ib(
        default=None,
        converter=VirtualNodeVirtualNodeTcpConnectionPool.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeVirtualNodeTcpConnectionPool)),
        metadata={AttrMeta.PROPERTY_NAME: "TCP"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodeconnectionpool.html#cfn-appmesh-virtualnode-virtualnodeconnectionpool-tcp"""

@attr.s
class VirtualNodeLogging(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.Logging"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-logging.html

    Property Document:
    
    - ``p_AccessLog``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-logging.html#cfn-appmesh-virtualnode-logging-accesslog
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.Logging"
    
    p_AccessLog: typing.Union['VirtualNodeAccessLog', dict] = attr.ib(
        default=None,
        converter=VirtualNodeAccessLog.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeAccessLog)),
        metadata={AttrMeta.PROPERTY_NAME: "AccessLog"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-logging.html#cfn-appmesh-virtualnode-logging-accesslog"""

@attr.s
class RouteTcpRoute(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.TcpRoute"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcproute.html

    Property Document:
    
    - ``rp_Action``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcproute.html#cfn-appmesh-route-tcproute-action
    - ``p_Timeout``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcproute.html#cfn-appmesh-route-tcproute-timeout
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.TcpRoute"
    
    rp_Action: typing.Union['RouteTcpRouteAction', dict] = attr.ib(
        default=None,
        converter=RouteTcpRouteAction.from_dict,
        validator=attr.validators.instance_of(RouteTcpRouteAction),
        metadata={AttrMeta.PROPERTY_NAME: "Action"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcproute.html#cfn-appmesh-route-tcproute-action"""
    p_Timeout: typing.Union['RouteTcpTimeout', dict] = attr.ib(
        default=None,
        converter=RouteTcpTimeout.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(RouteTcpTimeout)),
        metadata={AttrMeta.PROPERTY_NAME: "Timeout"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcproute.html#cfn-appmesh-route-tcproute-timeout"""

@attr.s
class VirtualGatewayVirtualGatewayListener(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayListener"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistener.html

    Property Document:
    
    - ``rp_PortMapping``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistener.html#cfn-appmesh-virtualgateway-virtualgatewaylistener-portmapping
    - ``p_ConnectionPool``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistener.html#cfn-appmesh-virtualgateway-virtualgatewaylistener-connectionpool
    - ``p_HealthCheck``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistener.html#cfn-appmesh-virtualgateway-virtualgatewaylistener-healthcheck
    - ``p_TLS``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistener.html#cfn-appmesh-virtualgateway-virtualgatewaylistener-tls
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayListener"
    
    rp_PortMapping: typing.Union['VirtualGatewayVirtualGatewayPortMapping', dict] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewayPortMapping.from_dict,
        validator=attr.validators.instance_of(VirtualGatewayVirtualGatewayPortMapping),
        metadata={AttrMeta.PROPERTY_NAME: "PortMapping"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistener.html#cfn-appmesh-virtualgateway-virtualgatewaylistener-portmapping"""
    p_ConnectionPool: typing.Union['VirtualGatewayVirtualGatewayConnectionPool', dict] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewayConnectionPool.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualGatewayVirtualGatewayConnectionPool)),
        metadata={AttrMeta.PROPERTY_NAME: "ConnectionPool"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistener.html#cfn-appmesh-virtualgateway-virtualgatewaylistener-connectionpool"""
    p_HealthCheck: typing.Union['VirtualGatewayVirtualGatewayHealthCheckPolicy', dict] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewayHealthCheckPolicy.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualGatewayVirtualGatewayHealthCheckPolicy)),
        metadata={AttrMeta.PROPERTY_NAME: "HealthCheck"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistener.html#cfn-appmesh-virtualgateway-virtualgatewaylistener-healthcheck"""
    p_TLS: typing.Union['VirtualGatewayVirtualGatewayListenerTls', dict] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewayListenerTls.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualGatewayVirtualGatewayListenerTls)),
        metadata={AttrMeta.PROPERTY_NAME: "TLS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistener.html#cfn-appmesh-virtualgateway-virtualgatewaylistener-tls"""

@attr.s
class VirtualNodeTlsValidationContextTrust(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.TlsValidationContextTrust"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontexttrust.html

    Property Document:
    
    - ``p_ACM``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontexttrust.html#cfn-appmesh-virtualnode-tlsvalidationcontexttrust-acm
    - ``p_File``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontexttrust.html#cfn-appmesh-virtualnode-tlsvalidationcontexttrust-file
    - ``p_SDS``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontexttrust.html#cfn-appmesh-virtualnode-tlsvalidationcontexttrust-sds
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.TlsValidationContextTrust"
    
    p_ACM: typing.Union['VirtualNodeTlsValidationContextAcmTrust', dict] = attr.ib(
        default=None,
        converter=VirtualNodeTlsValidationContextAcmTrust.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeTlsValidationContextAcmTrust)),
        metadata={AttrMeta.PROPERTY_NAME: "ACM"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontexttrust.html#cfn-appmesh-virtualnode-tlsvalidationcontexttrust-acm"""
    p_File: typing.Union['VirtualNodeTlsValidationContextFileTrust', dict] = attr.ib(
        default=None,
        converter=VirtualNodeTlsValidationContextFileTrust.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeTlsValidationContextFileTrust)),
        metadata={AttrMeta.PROPERTY_NAME: "File"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontexttrust.html#cfn-appmesh-virtualnode-tlsvalidationcontexttrust-file"""
    p_SDS: typing.Union['VirtualNodeTlsValidationContextSdsTrust', dict] = attr.ib(
        default=None,
        converter=VirtualNodeTlsValidationContextSdsTrust.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeTlsValidationContextSdsTrust)),
        metadata={AttrMeta.PROPERTY_NAME: "SDS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontexttrust.html#cfn-appmesh-virtualnode-tlsvalidationcontexttrust-sds"""

@attr.s
class GatewayRouteGrpcGatewayRouteMetadata(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.GrpcGatewayRouteMetadata"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutemetadata.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutemetadata.html#cfn-appmesh-gatewayroute-grpcgatewayroutemetadata-name
    - ``p_Invert``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutemetadata.html#cfn-appmesh-gatewayroute-grpcgatewayroutemetadata-invert
    - ``p_Match``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutemetadata.html#cfn-appmesh-gatewayroute-grpcgatewayroutemetadata-match
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.GrpcGatewayRouteMetadata"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutemetadata.html#cfn-appmesh-gatewayroute-grpcgatewayroutemetadata-name"""
    p_Invert: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Invert"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutemetadata.html#cfn-appmesh-gatewayroute-grpcgatewayroutemetadata-invert"""
    p_Match: typing.Union['GatewayRouteGatewayRouteMetadataMatch', dict] = attr.ib(
        default=None,
        converter=GatewayRouteGatewayRouteMetadataMatch.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(GatewayRouteGatewayRouteMetadataMatch)),
        metadata={AttrMeta.PROPERTY_NAME: "Match"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutemetadata.html#cfn-appmesh-gatewayroute-grpcgatewayroutemetadata-match"""

@attr.s
class GatewayRouteHttpGatewayRouteAction(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.HttpGatewayRouteAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteaction.html

    Property Document:
    
    - ``rp_Target``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteaction.html#cfn-appmesh-gatewayroute-httpgatewayrouteaction-target
    - ``p_Rewrite``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteaction.html#cfn-appmesh-gatewayroute-httpgatewayrouteaction-rewrite
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.HttpGatewayRouteAction"
    
    rp_Target: typing.Union['GatewayRouteGatewayRouteTarget', dict] = attr.ib(
        default=None,
        converter=GatewayRouteGatewayRouteTarget.from_dict,
        validator=attr.validators.instance_of(GatewayRouteGatewayRouteTarget),
        metadata={AttrMeta.PROPERTY_NAME: "Target"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteaction.html#cfn-appmesh-gatewayroute-httpgatewayrouteaction-target"""
    p_Rewrite: typing.Union['GatewayRouteHttpGatewayRouteRewrite', dict] = attr.ib(
        default=None,
        converter=GatewayRouteHttpGatewayRouteRewrite.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(GatewayRouteHttpGatewayRouteRewrite)),
        metadata={AttrMeta.PROPERTY_NAME: "Rewrite"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteaction.html#cfn-appmesh-gatewayroute-httpgatewayrouteaction-rewrite"""

@attr.s
class MeshMeshSpec(Property):
    """
    AWS Object Type = "AWS::AppMesh::Mesh.MeshSpec"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-meshspec.html

    Property Document:
    
    - ``p_EgressFilter``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-meshspec.html#cfn-appmesh-mesh-meshspec-egressfilter
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Mesh.MeshSpec"
    
    p_EgressFilter: typing.Union['MeshEgressFilter', dict] = attr.ib(
        default=None,
        converter=MeshEgressFilter.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(MeshEgressFilter)),
        metadata={AttrMeta.PROPERTY_NAME: "EgressFilter"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-meshspec.html#cfn-appmesh-mesh-meshspec-egressfilter"""

@attr.s
class VirtualGatewayVirtualGatewayAccessLog(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayAccessLog"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayaccesslog.html

    Property Document:
    
    - ``p_File``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayaccesslog.html#cfn-appmesh-virtualgateway-virtualgatewayaccesslog-file
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayAccessLog"
    
    p_File: typing.Union['VirtualGatewayVirtualGatewayFileAccessLog', dict] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewayFileAccessLog.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualGatewayVirtualGatewayFileAccessLog)),
        metadata={AttrMeta.PROPERTY_NAME: "File"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayaccesslog.html#cfn-appmesh-virtualgateway-virtualgatewayaccesslog-file"""

@attr.s
class RouteGrpcRoute(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.GrpcRoute"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroute.html

    Property Document:
    
    - ``rp_Action``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroute.html#cfn-appmesh-route-grpcroute-action
    - ``rp_Match``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroute.html#cfn-appmesh-route-grpcroute-match
    - ``p_RetryPolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroute.html#cfn-appmesh-route-grpcroute-retrypolicy
    - ``p_Timeout``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroute.html#cfn-appmesh-route-grpcroute-timeout
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.GrpcRoute"
    
    rp_Action: typing.Union['RouteGrpcRouteAction', dict] = attr.ib(
        default=None,
        converter=RouteGrpcRouteAction.from_dict,
        validator=attr.validators.instance_of(RouteGrpcRouteAction),
        metadata={AttrMeta.PROPERTY_NAME: "Action"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroute.html#cfn-appmesh-route-grpcroute-action"""
    rp_Match: typing.Union['RouteGrpcRouteMatch', dict] = attr.ib(
        default=None,
        converter=RouteGrpcRouteMatch.from_dict,
        validator=attr.validators.instance_of(RouteGrpcRouteMatch),
        metadata={AttrMeta.PROPERTY_NAME: "Match"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroute.html#cfn-appmesh-route-grpcroute-match"""
    p_RetryPolicy: typing.Union['RouteGrpcRetryPolicy', dict] = attr.ib(
        default=None,
        converter=RouteGrpcRetryPolicy.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(RouteGrpcRetryPolicy)),
        metadata={AttrMeta.PROPERTY_NAME: "RetryPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroute.html#cfn-appmesh-route-grpcroute-retrypolicy"""
    p_Timeout: typing.Union['RouteGrpcTimeout', dict] = attr.ib(
        default=None,
        converter=RouteGrpcTimeout.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(RouteGrpcTimeout)),
        metadata={AttrMeta.PROPERTY_NAME: "Timeout"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroute.html#cfn-appmesh-route-grpcroute-timeout"""

@attr.s
class GatewayRouteHttpGatewayRouteMatch(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.HttpGatewayRouteMatch"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html

    Property Document:
    
    - ``p_Headers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-headers
    - ``p_Hostname``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-hostname
    - ``p_Method``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-method
    - ``p_Path``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-path
    - ``p_Prefix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-prefix
    - ``p_QueryParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-queryparameters
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.HttpGatewayRouteMatch"
    
    p_Headers: typing.List[typing.Union['GatewayRouteHttpGatewayRouteHeader', dict]] = attr.ib(
        default=None,
        converter=GatewayRouteHttpGatewayRouteHeader.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(GatewayRouteHttpGatewayRouteHeader), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Headers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-headers"""
    p_Hostname: typing.Union['GatewayRouteGatewayRouteHostnameMatch', dict] = attr.ib(
        default=None,
        converter=GatewayRouteGatewayRouteHostnameMatch.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(GatewayRouteGatewayRouteHostnameMatch)),
        metadata={AttrMeta.PROPERTY_NAME: "Hostname"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-hostname"""
    p_Method: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Method"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-method"""
    p_Path: typing.Union['GatewayRouteHttpPathMatch', dict] = attr.ib(
        default=None,
        converter=GatewayRouteHttpPathMatch.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(GatewayRouteHttpPathMatch)),
        metadata={AttrMeta.PROPERTY_NAME: "Path"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-path"""
    p_Prefix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Prefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-prefix"""
    p_QueryParameters: typing.List[typing.Union['GatewayRouteQueryParameter', dict]] = attr.ib(
        default=None,
        converter=GatewayRouteQueryParameter.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(GatewayRouteQueryParameter), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "QueryParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-queryparameters"""

@attr.s
class RouteHttpRouteHeader(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.HttpRouteHeader"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteheader.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteheader.html#cfn-appmesh-route-httprouteheader-name
    - ``p_Invert``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteheader.html#cfn-appmesh-route-httprouteheader-invert
    - ``p_Match``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteheader.html#cfn-appmesh-route-httprouteheader-match
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.HttpRouteHeader"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteheader.html#cfn-appmesh-route-httprouteheader-name"""
    p_Invert: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Invert"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteheader.html#cfn-appmesh-route-httprouteheader-invert"""
    p_Match: typing.Union['RouteHeaderMatchMethod', dict] = attr.ib(
        default=None,
        converter=RouteHeaderMatchMethod.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(RouteHeaderMatchMethod)),
        metadata={AttrMeta.PROPERTY_NAME: "Match"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteheader.html#cfn-appmesh-route-httprouteheader-match"""

@attr.s
class GatewayRouteHttpGatewayRoute(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.HttpGatewayRoute"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroute.html

    Property Document:
    
    - ``rp_Action``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroute.html#cfn-appmesh-gatewayroute-httpgatewayroute-action
    - ``rp_Match``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroute.html#cfn-appmesh-gatewayroute-httpgatewayroute-match
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.HttpGatewayRoute"
    
    rp_Action: typing.Union['GatewayRouteHttpGatewayRouteAction', dict] = attr.ib(
        default=None,
        converter=GatewayRouteHttpGatewayRouteAction.from_dict,
        validator=attr.validators.instance_of(GatewayRouteHttpGatewayRouteAction),
        metadata={AttrMeta.PROPERTY_NAME: "Action"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroute.html#cfn-appmesh-gatewayroute-httpgatewayroute-action"""
    rp_Match: typing.Union['GatewayRouteHttpGatewayRouteMatch', dict] = attr.ib(
        default=None,
        converter=GatewayRouteHttpGatewayRouteMatch.from_dict,
        validator=attr.validators.instance_of(GatewayRouteHttpGatewayRouteMatch),
        metadata={AttrMeta.PROPERTY_NAME: "Match"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroute.html#cfn-appmesh-gatewayroute-httpgatewayroute-match"""

@attr.s
class VirtualNodeListenerTimeout(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.ListenerTimeout"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertimeout.html

    Property Document:
    
    - ``p_GRPC``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertimeout.html#cfn-appmesh-virtualnode-listenertimeout-grpc
    - ``p_HTTP``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertimeout.html#cfn-appmesh-virtualnode-listenertimeout-http
    - ``p_HTTP2``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertimeout.html#cfn-appmesh-virtualnode-listenertimeout-http2
    - ``p_TCP``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertimeout.html#cfn-appmesh-virtualnode-listenertimeout-tcp
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.ListenerTimeout"
    
    p_GRPC: typing.Union['VirtualNodeGrpcTimeout', dict] = attr.ib(
        default=None,
        converter=VirtualNodeGrpcTimeout.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeGrpcTimeout)),
        metadata={AttrMeta.PROPERTY_NAME: "GRPC"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertimeout.html#cfn-appmesh-virtualnode-listenertimeout-grpc"""
    p_HTTP: typing.Union['VirtualNodeHttpTimeout', dict] = attr.ib(
        default=None,
        converter=VirtualNodeHttpTimeout.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeHttpTimeout)),
        metadata={AttrMeta.PROPERTY_NAME: "HTTP"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertimeout.html#cfn-appmesh-virtualnode-listenertimeout-http"""
    p_HTTP2: typing.Union['VirtualNodeHttpTimeout', dict] = attr.ib(
        default=None,
        converter=VirtualNodeHttpTimeout.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeHttpTimeout)),
        metadata={AttrMeta.PROPERTY_NAME: "HTTP2"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertimeout.html#cfn-appmesh-virtualnode-listenertimeout-http2"""
    p_TCP: typing.Union['VirtualNodeTcpTimeout', dict] = attr.ib(
        default=None,
        converter=VirtualNodeTcpTimeout.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeTcpTimeout)),
        metadata={AttrMeta.PROPERTY_NAME: "TCP"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertimeout.html#cfn-appmesh-virtualnode-listenertimeout-tcp"""

@attr.s
class VirtualGatewayVirtualGatewayTlsValidationContext(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayTlsValidationContext"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext.html

    Property Document:
    
    - ``rp_Trust``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext-trust
    - ``p_SubjectAlternativeNames``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext-subjectalternativenames
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayTlsValidationContext"
    
    rp_Trust: typing.Union['VirtualGatewayVirtualGatewayTlsValidationContextTrust', dict] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewayTlsValidationContextTrust.from_dict,
        validator=attr.validators.instance_of(VirtualGatewayVirtualGatewayTlsValidationContextTrust),
        metadata={AttrMeta.PROPERTY_NAME: "Trust"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext-trust"""
    p_SubjectAlternativeNames: typing.Union['VirtualGatewaySubjectAlternativeNames', dict] = attr.ib(
        default=None,
        converter=VirtualGatewaySubjectAlternativeNames.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualGatewaySubjectAlternativeNames)),
        metadata={AttrMeta.PROPERTY_NAME: "SubjectAlternativeNames"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext-subjectalternativenames"""

@attr.s
class GatewayRouteGrpcGatewayRouteAction(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.GrpcGatewayRouteAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouteaction.html

    Property Document:
    
    - ``rp_Target``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouteaction.html#cfn-appmesh-gatewayroute-grpcgatewayrouteaction-target
    - ``p_Rewrite``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouteaction.html#cfn-appmesh-gatewayroute-grpcgatewayrouteaction-rewrite
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.GrpcGatewayRouteAction"
    
    rp_Target: typing.Union['GatewayRouteGatewayRouteTarget', dict] = attr.ib(
        default=None,
        converter=GatewayRouteGatewayRouteTarget.from_dict,
        validator=attr.validators.instance_of(GatewayRouteGatewayRouteTarget),
        metadata={AttrMeta.PROPERTY_NAME: "Target"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouteaction.html#cfn-appmesh-gatewayroute-grpcgatewayrouteaction-target"""
    p_Rewrite: typing.Union['GatewayRouteGrpcGatewayRouteRewrite', dict] = attr.ib(
        default=None,
        converter=GatewayRouteGrpcGatewayRouteRewrite.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(GatewayRouteGrpcGatewayRouteRewrite)),
        metadata={AttrMeta.PROPERTY_NAME: "Rewrite"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouteaction.html#cfn-appmesh-gatewayroute-grpcgatewayrouteaction-rewrite"""

@attr.s
class RouteHttpRouteMatch(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.HttpRouteMatch"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html

    Property Document:
    
    - ``p_Headers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html#cfn-appmesh-route-httproutematch-headers
    - ``p_Method``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html#cfn-appmesh-route-httproutematch-method
    - ``p_Path``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html#cfn-appmesh-route-httproutematch-path
    - ``p_Prefix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html#cfn-appmesh-route-httproutematch-prefix
    - ``p_QueryParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html#cfn-appmesh-route-httproutematch-queryparameters
    - ``p_Scheme``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html#cfn-appmesh-route-httproutematch-scheme
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.HttpRouteMatch"
    
    p_Headers: typing.List[typing.Union['RouteHttpRouteHeader', dict]] = attr.ib(
        default=None,
        converter=RouteHttpRouteHeader.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(RouteHttpRouteHeader), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Headers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html#cfn-appmesh-route-httproutematch-headers"""
    p_Method: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Method"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html#cfn-appmesh-route-httproutematch-method"""
    p_Path: typing.Union['RouteHttpPathMatch', dict] = attr.ib(
        default=None,
        converter=RouteHttpPathMatch.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(RouteHttpPathMatch)),
        metadata={AttrMeta.PROPERTY_NAME: "Path"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html#cfn-appmesh-route-httproutematch-path"""
    p_Prefix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Prefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html#cfn-appmesh-route-httproutematch-prefix"""
    p_QueryParameters: typing.List[typing.Union['RouteQueryParameter', dict]] = attr.ib(
        default=None,
        converter=RouteQueryParameter.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(RouteQueryParameter), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "QueryParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html#cfn-appmesh-route-httproutematch-queryparameters"""
    p_Scheme: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Scheme"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html#cfn-appmesh-route-httproutematch-scheme"""

@attr.s
class GatewayRouteGrpcGatewayRouteMatch(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.GrpcGatewayRouteMatch"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutematch.html

    Property Document:
    
    - ``p_Hostname``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutematch.html#cfn-appmesh-gatewayroute-grpcgatewayroutematch-hostname
    - ``p_Metadata``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutematch.html#cfn-appmesh-gatewayroute-grpcgatewayroutematch-metadata
    - ``p_ServiceName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutematch.html#cfn-appmesh-gatewayroute-grpcgatewayroutematch-servicename
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.GrpcGatewayRouteMatch"
    
    p_Hostname: typing.Union['GatewayRouteGatewayRouteHostnameMatch', dict] = attr.ib(
        default=None,
        converter=GatewayRouteGatewayRouteHostnameMatch.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(GatewayRouteGatewayRouteHostnameMatch)),
        metadata={AttrMeta.PROPERTY_NAME: "Hostname"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutematch.html#cfn-appmesh-gatewayroute-grpcgatewayroutematch-hostname"""
    p_Metadata: typing.List[typing.Union['GatewayRouteGrpcGatewayRouteMetadata', dict]] = attr.ib(
        default=None,
        converter=GatewayRouteGrpcGatewayRouteMetadata.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(GatewayRouteGrpcGatewayRouteMetadata), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Metadata"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutematch.html#cfn-appmesh-gatewayroute-grpcgatewayroutematch-metadata"""
    p_ServiceName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ServiceName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutematch.html#cfn-appmesh-gatewayroute-grpcgatewayroutematch-servicename"""

@attr.s
class GatewayRouteGrpcGatewayRoute(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.GrpcGatewayRoute"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroute.html

    Property Document:
    
    - ``rp_Action``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroute.html#cfn-appmesh-gatewayroute-grpcgatewayroute-action
    - ``rp_Match``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroute.html#cfn-appmesh-gatewayroute-grpcgatewayroute-match
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.GrpcGatewayRoute"
    
    rp_Action: typing.Union['GatewayRouteGrpcGatewayRouteAction', dict] = attr.ib(
        default=None,
        converter=GatewayRouteGrpcGatewayRouteAction.from_dict,
        validator=attr.validators.instance_of(GatewayRouteGrpcGatewayRouteAction),
        metadata={AttrMeta.PROPERTY_NAME: "Action"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroute.html#cfn-appmesh-gatewayroute-grpcgatewayroute-action"""
    rp_Match: typing.Union['GatewayRouteGrpcGatewayRouteMatch', dict] = attr.ib(
        default=None,
        converter=GatewayRouteGrpcGatewayRouteMatch.from_dict,
        validator=attr.validators.instance_of(GatewayRouteGrpcGatewayRouteMatch),
        metadata={AttrMeta.PROPERTY_NAME: "Match"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroute.html#cfn-appmesh-gatewayroute-grpcgatewayroute-match"""

@attr.s
class VirtualGatewayVirtualGatewayLogging(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayLogging"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylogging.html

    Property Document:
    
    - ``p_AccessLog``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylogging.html#cfn-appmesh-virtualgateway-virtualgatewaylogging-accesslog
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayLogging"
    
    p_AccessLog: typing.Union['VirtualGatewayVirtualGatewayAccessLog', dict] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewayAccessLog.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualGatewayVirtualGatewayAccessLog)),
        metadata={AttrMeta.PROPERTY_NAME: "AccessLog"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylogging.html#cfn-appmesh-virtualgateway-virtualgatewaylogging-accesslog"""

@attr.s
class VirtualNodeTlsValidationContext(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.TlsValidationContext"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontext.html

    Property Document:
    
    - ``rp_Trust``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontext.html#cfn-appmesh-virtualnode-tlsvalidationcontext-trust
    - ``p_SubjectAlternativeNames``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontext.html#cfn-appmesh-virtualnode-tlsvalidationcontext-subjectalternativenames
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.TlsValidationContext"
    
    rp_Trust: typing.Union['VirtualNodeTlsValidationContextTrust', dict] = attr.ib(
        default=None,
        converter=VirtualNodeTlsValidationContextTrust.from_dict,
        validator=attr.validators.instance_of(VirtualNodeTlsValidationContextTrust),
        metadata={AttrMeta.PROPERTY_NAME: "Trust"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontext.html#cfn-appmesh-virtualnode-tlsvalidationcontext-trust"""
    p_SubjectAlternativeNames: typing.Union['VirtualNodeSubjectAlternativeNames', dict] = attr.ib(
        default=None,
        converter=VirtualNodeSubjectAlternativeNames.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeSubjectAlternativeNames)),
        metadata={AttrMeta.PROPERTY_NAME: "SubjectAlternativeNames"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontext.html#cfn-appmesh-virtualnode-tlsvalidationcontext-subjectalternativenames"""

@attr.s
class VirtualNodeListener(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.Listener"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html

    Property Document:
    
    - ``rp_PortMapping``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html#cfn-appmesh-virtualnode-listener-portmapping
    - ``p_ConnectionPool``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html#cfn-appmesh-virtualnode-listener-connectionpool
    - ``p_HealthCheck``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html#cfn-appmesh-virtualnode-listener-healthcheck
    - ``p_OutlierDetection``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html#cfn-appmesh-virtualnode-listener-outlierdetection
    - ``p_TLS``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html#cfn-appmesh-virtualnode-listener-tls
    - ``p_Timeout``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html#cfn-appmesh-virtualnode-listener-timeout
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.Listener"
    
    rp_PortMapping: typing.Union['VirtualNodePortMapping', dict] = attr.ib(
        default=None,
        converter=VirtualNodePortMapping.from_dict,
        validator=attr.validators.instance_of(VirtualNodePortMapping),
        metadata={AttrMeta.PROPERTY_NAME: "PortMapping"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html#cfn-appmesh-virtualnode-listener-portmapping"""
    p_ConnectionPool: typing.Union['VirtualNodeVirtualNodeConnectionPool', dict] = attr.ib(
        default=None,
        converter=VirtualNodeVirtualNodeConnectionPool.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeVirtualNodeConnectionPool)),
        metadata={AttrMeta.PROPERTY_NAME: "ConnectionPool"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html#cfn-appmesh-virtualnode-listener-connectionpool"""
    p_HealthCheck: typing.Union['VirtualNodeHealthCheck', dict] = attr.ib(
        default=None,
        converter=VirtualNodeHealthCheck.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeHealthCheck)),
        metadata={AttrMeta.PROPERTY_NAME: "HealthCheck"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html#cfn-appmesh-virtualnode-listener-healthcheck"""
    p_OutlierDetection: typing.Union['VirtualNodeOutlierDetection', dict] = attr.ib(
        default=None,
        converter=VirtualNodeOutlierDetection.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeOutlierDetection)),
        metadata={AttrMeta.PROPERTY_NAME: "OutlierDetection"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html#cfn-appmesh-virtualnode-listener-outlierdetection"""
    p_TLS: typing.Union['VirtualNodeListenerTls', dict] = attr.ib(
        default=None,
        converter=VirtualNodeListenerTls.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeListenerTls)),
        metadata={AttrMeta.PROPERTY_NAME: "TLS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html#cfn-appmesh-virtualnode-listener-tls"""
    p_Timeout: typing.Union['VirtualNodeListenerTimeout', dict] = attr.ib(
        default=None,
        converter=VirtualNodeListenerTimeout.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeListenerTimeout)),
        metadata={AttrMeta.PROPERTY_NAME: "Timeout"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html#cfn-appmesh-virtualnode-listener-timeout"""

@attr.s
class RouteHttpRoute(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.HttpRoute"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproute.html

    Property Document:
    
    - ``rp_Action``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproute.html#cfn-appmesh-route-httproute-action
    - ``rp_Match``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproute.html#cfn-appmesh-route-httproute-match
    - ``p_RetryPolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproute.html#cfn-appmesh-route-httproute-retrypolicy
    - ``p_Timeout``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproute.html#cfn-appmesh-route-httproute-timeout
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.HttpRoute"
    
    rp_Action: typing.Union['RouteHttpRouteAction', dict] = attr.ib(
        default=None,
        converter=RouteHttpRouteAction.from_dict,
        validator=attr.validators.instance_of(RouteHttpRouteAction),
        metadata={AttrMeta.PROPERTY_NAME: "Action"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproute.html#cfn-appmesh-route-httproute-action"""
    rp_Match: typing.Union['RouteHttpRouteMatch', dict] = attr.ib(
        default=None,
        converter=RouteHttpRouteMatch.from_dict,
        validator=attr.validators.instance_of(RouteHttpRouteMatch),
        metadata={AttrMeta.PROPERTY_NAME: "Match"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproute.html#cfn-appmesh-route-httproute-match"""
    p_RetryPolicy: typing.Union['RouteHttpRetryPolicy', dict] = attr.ib(
        default=None,
        converter=RouteHttpRetryPolicy.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(RouteHttpRetryPolicy)),
        metadata={AttrMeta.PROPERTY_NAME: "RetryPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproute.html#cfn-appmesh-route-httproute-retrypolicy"""
    p_Timeout: typing.Union['RouteHttpTimeout', dict] = attr.ib(
        default=None,
        converter=RouteHttpTimeout.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(RouteHttpTimeout)),
        metadata={AttrMeta.PROPERTY_NAME: "Timeout"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproute.html#cfn-appmesh-route-httproute-timeout"""

@attr.s
class VirtualGatewayVirtualGatewayClientPolicyTls(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayClientPolicyTls"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicytls.html

    Property Document:
    
    - ``rp_Validation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicytls.html#cfn-appmesh-virtualgateway-virtualgatewayclientpolicytls-validation
    - ``p_Certificate``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicytls.html#cfn-appmesh-virtualgateway-virtualgatewayclientpolicytls-certificate
    - ``p_Enforce``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicytls.html#cfn-appmesh-virtualgateway-virtualgatewayclientpolicytls-enforce
    - ``p_Ports``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicytls.html#cfn-appmesh-virtualgateway-virtualgatewayclientpolicytls-ports
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayClientPolicyTls"
    
    rp_Validation: typing.Union['VirtualGatewayVirtualGatewayTlsValidationContext', dict] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewayTlsValidationContext.from_dict,
        validator=attr.validators.instance_of(VirtualGatewayVirtualGatewayTlsValidationContext),
        metadata={AttrMeta.PROPERTY_NAME: "Validation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicytls.html#cfn-appmesh-virtualgateway-virtualgatewayclientpolicytls-validation"""
    p_Certificate: typing.Union['VirtualGatewayVirtualGatewayClientTlsCertificate', dict] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewayClientTlsCertificate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualGatewayVirtualGatewayClientTlsCertificate)),
        metadata={AttrMeta.PROPERTY_NAME: "Certificate"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicytls.html#cfn-appmesh-virtualgateway-virtualgatewayclientpolicytls-certificate"""
    p_Enforce: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enforce"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicytls.html#cfn-appmesh-virtualgateway-virtualgatewayclientpolicytls-enforce"""
    p_Ports: typing.List[int] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(int), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Ports"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicytls.html#cfn-appmesh-virtualgateway-virtualgatewayclientpolicytls-ports"""

@attr.s
class VirtualNodeClientPolicyTls(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.ClientPolicyTls"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicytls.html

    Property Document:
    
    - ``rp_Validation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicytls.html#cfn-appmesh-virtualnode-clientpolicytls-validation
    - ``p_Certificate``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicytls.html#cfn-appmesh-virtualnode-clientpolicytls-certificate
    - ``p_Enforce``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicytls.html#cfn-appmesh-virtualnode-clientpolicytls-enforce
    - ``p_Ports``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicytls.html#cfn-appmesh-virtualnode-clientpolicytls-ports
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.ClientPolicyTls"
    
    rp_Validation: typing.Union['VirtualNodeTlsValidationContext', dict] = attr.ib(
        default=None,
        converter=VirtualNodeTlsValidationContext.from_dict,
        validator=attr.validators.instance_of(VirtualNodeTlsValidationContext),
        metadata={AttrMeta.PROPERTY_NAME: "Validation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicytls.html#cfn-appmesh-virtualnode-clientpolicytls-validation"""
    p_Certificate: typing.Union['VirtualNodeClientTlsCertificate', dict] = attr.ib(
        default=None,
        converter=VirtualNodeClientTlsCertificate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeClientTlsCertificate)),
        metadata={AttrMeta.PROPERTY_NAME: "Certificate"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicytls.html#cfn-appmesh-virtualnode-clientpolicytls-certificate"""
    p_Enforce: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enforce"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicytls.html#cfn-appmesh-virtualnode-clientpolicytls-enforce"""
    p_Ports: typing.List[int] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(int), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Ports"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicytls.html#cfn-appmesh-virtualnode-clientpolicytls-ports"""

@attr.s
class GatewayRouteGatewayRouteSpec(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.GatewayRouteSpec"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutespec.html

    Property Document:
    
    - ``p_GrpcRoute``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutespec.html#cfn-appmesh-gatewayroute-gatewayroutespec-grpcroute
    - ``p_Http2Route``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutespec.html#cfn-appmesh-gatewayroute-gatewayroutespec-http2route
    - ``p_HttpRoute``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutespec.html#cfn-appmesh-gatewayroute-gatewayroutespec-httproute
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.GatewayRouteSpec"
    
    p_GrpcRoute: typing.Union['GatewayRouteGrpcGatewayRoute', dict] = attr.ib(
        default=None,
        converter=GatewayRouteGrpcGatewayRoute.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(GatewayRouteGrpcGatewayRoute)),
        metadata={AttrMeta.PROPERTY_NAME: "GrpcRoute"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutespec.html#cfn-appmesh-gatewayroute-gatewayroutespec-grpcroute"""
    p_Http2Route: typing.Union['GatewayRouteHttpGatewayRoute', dict] = attr.ib(
        default=None,
        converter=GatewayRouteHttpGatewayRoute.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(GatewayRouteHttpGatewayRoute)),
        metadata={AttrMeta.PROPERTY_NAME: "Http2Route"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutespec.html#cfn-appmesh-gatewayroute-gatewayroutespec-http2route"""
    p_HttpRoute: typing.Union['GatewayRouteHttpGatewayRoute', dict] = attr.ib(
        default=None,
        converter=GatewayRouteHttpGatewayRoute.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(GatewayRouteHttpGatewayRoute)),
        metadata={AttrMeta.PROPERTY_NAME: "HttpRoute"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutespec.html#cfn-appmesh-gatewayroute-gatewayroutespec-httproute"""

@attr.s
class RouteRouteSpec(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.RouteSpec"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html

    Property Document:
    
    - ``p_GrpcRoute``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html#cfn-appmesh-route-routespec-grpcroute
    - ``p_Http2Route``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html#cfn-appmesh-route-routespec-http2route
    - ``p_HttpRoute``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html#cfn-appmesh-route-routespec-httproute
    - ``p_Priority``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html#cfn-appmesh-route-routespec-priority
    - ``p_TcpRoute``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html#cfn-appmesh-route-routespec-tcproute
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.RouteSpec"
    
    p_GrpcRoute: typing.Union['RouteGrpcRoute', dict] = attr.ib(
        default=None,
        converter=RouteGrpcRoute.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(RouteGrpcRoute)),
        metadata={AttrMeta.PROPERTY_NAME: "GrpcRoute"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html#cfn-appmesh-route-routespec-grpcroute"""
    p_Http2Route: typing.Union['RouteHttpRoute', dict] = attr.ib(
        default=None,
        converter=RouteHttpRoute.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(RouteHttpRoute)),
        metadata={AttrMeta.PROPERTY_NAME: "Http2Route"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html#cfn-appmesh-route-routespec-http2route"""
    p_HttpRoute: typing.Union['RouteHttpRoute', dict] = attr.ib(
        default=None,
        converter=RouteHttpRoute.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(RouteHttpRoute)),
        metadata={AttrMeta.PROPERTY_NAME: "HttpRoute"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html#cfn-appmesh-route-routespec-httproute"""
    p_Priority: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Priority"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html#cfn-appmesh-route-routespec-priority"""
    p_TcpRoute: typing.Union['RouteTcpRoute', dict] = attr.ib(
        default=None,
        converter=RouteTcpRoute.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(RouteTcpRoute)),
        metadata={AttrMeta.PROPERTY_NAME: "TcpRoute"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html#cfn-appmesh-route-routespec-tcproute"""

@attr.s
class VirtualGatewayVirtualGatewayClientPolicy(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayClientPolicy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicy.html

    Property Document:
    
    - ``p_TLS``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayclientpolicy-tls
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayClientPolicy"
    
    p_TLS: typing.Union['VirtualGatewayVirtualGatewayClientPolicyTls', dict] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewayClientPolicyTls.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualGatewayVirtualGatewayClientPolicyTls)),
        metadata={AttrMeta.PROPERTY_NAME: "TLS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayclientpolicy-tls"""

@attr.s
class VirtualGatewayVirtualGatewayBackendDefaults(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayBackendDefaults"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaybackenddefaults.html

    Property Document:
    
    - ``p_ClientPolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaybackenddefaults.html#cfn-appmesh-virtualgateway-virtualgatewaybackenddefaults-clientpolicy
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayBackendDefaults"
    
    p_ClientPolicy: typing.Union['VirtualGatewayVirtualGatewayClientPolicy', dict] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewayClientPolicy.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualGatewayVirtualGatewayClientPolicy)),
        metadata={AttrMeta.PROPERTY_NAME: "ClientPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaybackenddefaults.html#cfn-appmesh-virtualgateway-virtualgatewaybackenddefaults-clientpolicy"""

@attr.s
class VirtualNodeClientPolicy(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.ClientPolicy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicy.html

    Property Document:
    
    - ``p_TLS``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicy.html#cfn-appmesh-virtualnode-clientpolicy-tls
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.ClientPolicy"
    
    p_TLS: typing.Union['VirtualNodeClientPolicyTls', dict] = attr.ib(
        default=None,
        converter=VirtualNodeClientPolicyTls.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeClientPolicyTls)),
        metadata={AttrMeta.PROPERTY_NAME: "TLS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicy.html#cfn-appmesh-virtualnode-clientpolicy-tls"""

@attr.s
class VirtualGatewayVirtualGatewaySpec(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewaySpec"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayspec.html

    Property Document:
    
    - ``rp_Listeners``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayspec.html#cfn-appmesh-virtualgateway-virtualgatewayspec-listeners
    - ``p_BackendDefaults``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayspec.html#cfn-appmesh-virtualgateway-virtualgatewayspec-backenddefaults
    - ``p_Logging``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayspec.html#cfn-appmesh-virtualgateway-virtualgatewayspec-logging
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewaySpec"
    
    rp_Listeners: typing.List[typing.Union['VirtualGatewayVirtualGatewayListener', dict]] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewayListener.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(VirtualGatewayVirtualGatewayListener), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Listeners"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayspec.html#cfn-appmesh-virtualgateway-virtualgatewayspec-listeners"""
    p_BackendDefaults: typing.Union['VirtualGatewayVirtualGatewayBackendDefaults', dict] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewayBackendDefaults.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualGatewayVirtualGatewayBackendDefaults)),
        metadata={AttrMeta.PROPERTY_NAME: "BackendDefaults"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayspec.html#cfn-appmesh-virtualgateway-virtualgatewayspec-backenddefaults"""
    p_Logging: typing.Union['VirtualGatewayVirtualGatewayLogging', dict] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewayLogging.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualGatewayVirtualGatewayLogging)),
        metadata={AttrMeta.PROPERTY_NAME: "Logging"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayspec.html#cfn-appmesh-virtualgateway-virtualgatewayspec-logging"""

@attr.s
class VirtualNodeBackendDefaults(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.BackendDefaults"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-backenddefaults.html

    Property Document:
    
    - ``p_ClientPolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-backenddefaults.html#cfn-appmesh-virtualnode-backenddefaults-clientpolicy
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.BackendDefaults"
    
    p_ClientPolicy: typing.Union['VirtualNodeClientPolicy', dict] = attr.ib(
        default=None,
        converter=VirtualNodeClientPolicy.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeClientPolicy)),
        metadata={AttrMeta.PROPERTY_NAME: "ClientPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-backenddefaults.html#cfn-appmesh-virtualnode-backenddefaults-clientpolicy"""

@attr.s
class VirtualNodeVirtualServiceBackend(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.VirtualServiceBackend"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualservicebackend.html

    Property Document:
    
    - ``rp_VirtualServiceName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualservicebackend.html#cfn-appmesh-virtualnode-virtualservicebackend-virtualservicename
    - ``p_ClientPolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualservicebackend.html#cfn-appmesh-virtualnode-virtualservicebackend-clientpolicy
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.VirtualServiceBackend"
    
    rp_VirtualServiceName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "VirtualServiceName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualservicebackend.html#cfn-appmesh-virtualnode-virtualservicebackend-virtualservicename"""
    p_ClientPolicy: typing.Union['VirtualNodeClientPolicy', dict] = attr.ib(
        default=None,
        converter=VirtualNodeClientPolicy.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeClientPolicy)),
        metadata={AttrMeta.PROPERTY_NAME: "ClientPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualservicebackend.html#cfn-appmesh-virtualnode-virtualservicebackend-clientpolicy"""

@attr.s
class VirtualNodeBackend(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.Backend"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-backend.html

    Property Document:
    
    - ``p_VirtualService``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-backend.html#cfn-appmesh-virtualnode-backend-virtualservice
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.Backend"
    
    p_VirtualService: typing.Union['VirtualNodeVirtualServiceBackend', dict] = attr.ib(
        default=None,
        converter=VirtualNodeVirtualServiceBackend.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeVirtualServiceBackend)),
        metadata={AttrMeta.PROPERTY_NAME: "VirtualService"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-backend.html#cfn-appmesh-virtualnode-backend-virtualservice"""

@attr.s
class VirtualNodeVirtualNodeSpec(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.VirtualNodeSpec"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodespec.html

    Property Document:
    
    - ``p_BackendDefaults``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodespec.html#cfn-appmesh-virtualnode-virtualnodespec-backenddefaults
    - ``p_Backends``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodespec.html#cfn-appmesh-virtualnode-virtualnodespec-backends
    - ``p_Listeners``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodespec.html#cfn-appmesh-virtualnode-virtualnodespec-listeners
    - ``p_Logging``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodespec.html#cfn-appmesh-virtualnode-virtualnodespec-logging
    - ``p_ServiceDiscovery``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodespec.html#cfn-appmesh-virtualnode-virtualnodespec-servicediscovery
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.VirtualNodeSpec"
    
    p_BackendDefaults: typing.Union['VirtualNodeBackendDefaults', dict] = attr.ib(
        default=None,
        converter=VirtualNodeBackendDefaults.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeBackendDefaults)),
        metadata={AttrMeta.PROPERTY_NAME: "BackendDefaults"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodespec.html#cfn-appmesh-virtualnode-virtualnodespec-backenddefaults"""
    p_Backends: typing.List[typing.Union['VirtualNodeBackend', dict]] = attr.ib(
        default=None,
        converter=VirtualNodeBackend.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(VirtualNodeBackend), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Backends"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodespec.html#cfn-appmesh-virtualnode-virtualnodespec-backends"""
    p_Listeners: typing.List[typing.Union['VirtualNodeListener', dict]] = attr.ib(
        default=None,
        converter=VirtualNodeListener.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(VirtualNodeListener), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Listeners"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodespec.html#cfn-appmesh-virtualnode-virtualnodespec-listeners"""
    p_Logging: typing.Union['VirtualNodeLogging', dict] = attr.ib(
        default=None,
        converter=VirtualNodeLogging.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeLogging)),
        metadata={AttrMeta.PROPERTY_NAME: "Logging"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodespec.html#cfn-appmesh-virtualnode-virtualnodespec-logging"""
    p_ServiceDiscovery: typing.Union['VirtualNodeServiceDiscovery', dict] = attr.ib(
        default=None,
        converter=VirtualNodeServiceDiscovery.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(VirtualNodeServiceDiscovery)),
        metadata={AttrMeta.PROPERTY_NAME: "ServiceDiscovery"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodespec.html#cfn-appmesh-virtualnode-virtualnodespec-servicediscovery"""


#--- Resource declaration ---

@attr.s
class Route(Resource):
    """
    AWS Object Type = "AWS::AppMesh::Route"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html

    Property Document:
    
    - ``rp_MeshName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#cfn-appmesh-route-meshname
    - ``rp_Spec``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#cfn-appmesh-route-spec
    - ``rp_VirtualRouterName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#cfn-appmesh-route-virtualroutername
    - ``p_MeshOwner``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#cfn-appmesh-route-meshowner
    - ``p_RouteName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#cfn-appmesh-route-routename
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#cfn-appmesh-route-tags
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route"

    
    rp_MeshName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "MeshName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#cfn-appmesh-route-meshname"""
    rp_Spec: typing.Union['RouteRouteSpec', dict] = attr.ib(
        default=None,
        converter=RouteRouteSpec.from_dict,
        validator=attr.validators.instance_of(RouteRouteSpec),
        metadata={AttrMeta.PROPERTY_NAME: "Spec"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#cfn-appmesh-route-spec"""
    rp_VirtualRouterName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "VirtualRouterName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#cfn-appmesh-route-virtualroutername"""
    p_MeshOwner: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MeshOwner"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#cfn-appmesh-route-meshowner"""
    p_RouteName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RouteName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#cfn-appmesh-route-routename"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#cfn-appmesh-route-tags"""

    
    @property
    def rv_Uid(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#aws-resource-appmesh-route-return-values"""
        return GetAtt(resource=self, attr_name="Uid")
    
    @property
    def rv_MeshName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#aws-resource-appmesh-route-return-values"""
        return GetAtt(resource=self, attr_name="MeshName")
    
    @property
    def rv_VirtualRouterName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#aws-resource-appmesh-route-return-values"""
        return GetAtt(resource=self, attr_name="VirtualRouterName")
    
    @property
    def rv_MeshOwner(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#aws-resource-appmesh-route-return-values"""
        return GetAtt(resource=self, attr_name="MeshOwner")
    
    @property
    def rv_ResourceOwner(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#aws-resource-appmesh-route-return-values"""
        return GetAtt(resource=self, attr_name="ResourceOwner")
    
    @property
    def rv_RouteName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#aws-resource-appmesh-route-return-values"""
        return GetAtt(resource=self, attr_name="RouteName")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html#aws-resource-appmesh-route-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class GatewayRoute(Resource):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html

    Property Document:
    
    - ``rp_MeshName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#cfn-appmesh-gatewayroute-meshname
    - ``rp_Spec``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#cfn-appmesh-gatewayroute-spec
    - ``rp_VirtualGatewayName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#cfn-appmesh-gatewayroute-virtualgatewayname
    - ``p_GatewayRouteName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#cfn-appmesh-gatewayroute-gatewayroutename
    - ``p_MeshOwner``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#cfn-appmesh-gatewayroute-meshowner
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#cfn-appmesh-gatewayroute-tags
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute"

    
    rp_MeshName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "MeshName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#cfn-appmesh-gatewayroute-meshname"""
    rp_Spec: typing.Union['GatewayRouteGatewayRouteSpec', dict] = attr.ib(
        default=None,
        converter=GatewayRouteGatewayRouteSpec.from_dict,
        validator=attr.validators.instance_of(GatewayRouteGatewayRouteSpec),
        metadata={AttrMeta.PROPERTY_NAME: "Spec"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#cfn-appmesh-gatewayroute-spec"""
    rp_VirtualGatewayName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "VirtualGatewayName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#cfn-appmesh-gatewayroute-virtualgatewayname"""
    p_GatewayRouteName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "GatewayRouteName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#cfn-appmesh-gatewayroute-gatewayroutename"""
    p_MeshOwner: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MeshOwner"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#cfn-appmesh-gatewayroute-meshowner"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#cfn-appmesh-gatewayroute-tags"""

    
    @property
    def rv_Uid(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#aws-resource-appmesh-gatewayroute-return-values"""
        return GetAtt(resource=self, attr_name="Uid")
    
    @property
    def rv_MeshName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#aws-resource-appmesh-gatewayroute-return-values"""
        return GetAtt(resource=self, attr_name="MeshName")
    
    @property
    def rv_VirtualGatewayName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#aws-resource-appmesh-gatewayroute-return-values"""
        return GetAtt(resource=self, attr_name="VirtualGatewayName")
    
    @property
    def rv_MeshOwner(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#aws-resource-appmesh-gatewayroute-return-values"""
        return GetAtt(resource=self, attr_name="MeshOwner")
    
    @property
    def rv_ResourceOwner(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#aws-resource-appmesh-gatewayroute-return-values"""
        return GetAtt(resource=self, attr_name="ResourceOwner")
    
    @property
    def rv_GatewayRouteName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#aws-resource-appmesh-gatewayroute-return-values"""
        return GetAtt(resource=self, attr_name="GatewayRouteName")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html#aws-resource-appmesh-gatewayroute-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class VirtualGateway(Resource):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html

    Property Document:
    
    - ``rp_MeshName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#cfn-appmesh-virtualgateway-meshname
    - ``rp_Spec``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#cfn-appmesh-virtualgateway-spec
    - ``p_MeshOwner``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#cfn-appmesh-virtualgateway-meshowner
    - ``p_VirtualGatewayName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#cfn-appmesh-virtualgateway-virtualgatewayname
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#cfn-appmesh-virtualgateway-tags
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway"

    
    rp_MeshName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "MeshName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#cfn-appmesh-virtualgateway-meshname"""
    rp_Spec: typing.Union['VirtualGatewayVirtualGatewaySpec', dict] = attr.ib(
        default=None,
        converter=VirtualGatewayVirtualGatewaySpec.from_dict,
        validator=attr.validators.instance_of(VirtualGatewayVirtualGatewaySpec),
        metadata={AttrMeta.PROPERTY_NAME: "Spec"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#cfn-appmesh-virtualgateway-spec"""
    p_MeshOwner: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MeshOwner"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#cfn-appmesh-virtualgateway-meshowner"""
    p_VirtualGatewayName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "VirtualGatewayName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#cfn-appmesh-virtualgateway-virtualgatewayname"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#cfn-appmesh-virtualgateway-tags"""

    
    @property
    def rv_Uid(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#aws-resource-appmesh-virtualgateway-return-values"""
        return GetAtt(resource=self, attr_name="Uid")
    
    @property
    def rv_VirtualGatewayName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#aws-resource-appmesh-virtualgateway-return-values"""
        return GetAtt(resource=self, attr_name="VirtualGatewayName")
    
    @property
    def rv_MeshName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#aws-resource-appmesh-virtualgateway-return-values"""
        return GetAtt(resource=self, attr_name="MeshName")
    
    @property
    def rv_MeshOwner(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#aws-resource-appmesh-virtualgateway-return-values"""
        return GetAtt(resource=self, attr_name="MeshOwner")
    
    @property
    def rv_ResourceOwner(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#aws-resource-appmesh-virtualgateway-return-values"""
        return GetAtt(resource=self, attr_name="ResourceOwner")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html#aws-resource-appmesh-virtualgateway-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class VirtualNode(Resource):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html

    Property Document:
    
    - ``rp_MeshName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#cfn-appmesh-virtualnode-meshname
    - ``rp_Spec``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#cfn-appmesh-virtualnode-spec
    - ``p_MeshOwner``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#cfn-appmesh-virtualnode-meshowner
    - ``p_VirtualNodeName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#cfn-appmesh-virtualnode-virtualnodename
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#cfn-appmesh-virtualnode-tags
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode"

    
    rp_MeshName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "MeshName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#cfn-appmesh-virtualnode-meshname"""
    rp_Spec: typing.Union['VirtualNodeVirtualNodeSpec', dict] = attr.ib(
        default=None,
        converter=VirtualNodeVirtualNodeSpec.from_dict,
        validator=attr.validators.instance_of(VirtualNodeVirtualNodeSpec),
        metadata={AttrMeta.PROPERTY_NAME: "Spec"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#cfn-appmesh-virtualnode-spec"""
    p_MeshOwner: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MeshOwner"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#cfn-appmesh-virtualnode-meshowner"""
    p_VirtualNodeName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "VirtualNodeName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#cfn-appmesh-virtualnode-virtualnodename"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#cfn-appmesh-virtualnode-tags"""

    
    @property
    def rv_Uid(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#aws-resource-appmesh-virtualnode-return-values"""
        return GetAtt(resource=self, attr_name="Uid")
    
    @property
    def rv_MeshName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#aws-resource-appmesh-virtualnode-return-values"""
        return GetAtt(resource=self, attr_name="MeshName")
    
    @property
    def rv_MeshOwner(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#aws-resource-appmesh-virtualnode-return-values"""
        return GetAtt(resource=self, attr_name="MeshOwner")
    
    @property
    def rv_ResourceOwner(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#aws-resource-appmesh-virtualnode-return-values"""
        return GetAtt(resource=self, attr_name="ResourceOwner")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#aws-resource-appmesh-virtualnode-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_VirtualNodeName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html#aws-resource-appmesh-virtualnode-return-values"""
        return GetAtt(resource=self, attr_name="VirtualNodeName")
    

@attr.s
class VirtualRouter(Resource):
    """
    AWS Object Type = "AWS::AppMesh::VirtualRouter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html

    Property Document:
    
    - ``rp_MeshName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#cfn-appmesh-virtualrouter-meshname
    - ``rp_Spec``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#cfn-appmesh-virtualrouter-spec
    - ``p_MeshOwner``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#cfn-appmesh-virtualrouter-meshowner
    - ``p_VirtualRouterName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#cfn-appmesh-virtualrouter-virtualroutername
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#cfn-appmesh-virtualrouter-tags
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualRouter"

    
    rp_MeshName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "MeshName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#cfn-appmesh-virtualrouter-meshname"""
    rp_Spec: typing.Union['VirtualRouterVirtualRouterSpec', dict] = attr.ib(
        default=None,
        converter=VirtualRouterVirtualRouterSpec.from_dict,
        validator=attr.validators.instance_of(VirtualRouterVirtualRouterSpec),
        metadata={AttrMeta.PROPERTY_NAME: "Spec"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#cfn-appmesh-virtualrouter-spec"""
    p_MeshOwner: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MeshOwner"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#cfn-appmesh-virtualrouter-meshowner"""
    p_VirtualRouterName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "VirtualRouterName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#cfn-appmesh-virtualrouter-virtualroutername"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#cfn-appmesh-virtualrouter-tags"""

    
    @property
    def rv_Uid(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#aws-resource-appmesh-virtualrouter-return-values"""
        return GetAtt(resource=self, attr_name="Uid")
    
    @property
    def rv_MeshName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#aws-resource-appmesh-virtualrouter-return-values"""
        return GetAtt(resource=self, attr_name="MeshName")
    
    @property
    def rv_VirtualRouterName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#aws-resource-appmesh-virtualrouter-return-values"""
        return GetAtt(resource=self, attr_name="VirtualRouterName")
    
    @property
    def rv_MeshOwner(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#aws-resource-appmesh-virtualrouter-return-values"""
        return GetAtt(resource=self, attr_name="MeshOwner")
    
    @property
    def rv_ResourceOwner(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#aws-resource-appmesh-virtualrouter-return-values"""
        return GetAtt(resource=self, attr_name="ResourceOwner")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html#aws-resource-appmesh-virtualrouter-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class VirtualService(Resource):
    """
    AWS Object Type = "AWS::AppMesh::VirtualService"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html

    Property Document:
    
    - ``rp_MeshName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#cfn-appmesh-virtualservice-meshname
    - ``rp_Spec``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#cfn-appmesh-virtualservice-spec
    - ``rp_VirtualServiceName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#cfn-appmesh-virtualservice-virtualservicename
    - ``p_MeshOwner``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#cfn-appmesh-virtualservice-meshowner
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#cfn-appmesh-virtualservice-tags
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualService"

    
    rp_MeshName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "MeshName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#cfn-appmesh-virtualservice-meshname"""
    rp_Spec: typing.Union['VirtualServiceVirtualServiceSpec', dict] = attr.ib(
        default=None,
        converter=VirtualServiceVirtualServiceSpec.from_dict,
        validator=attr.validators.instance_of(VirtualServiceVirtualServiceSpec),
        metadata={AttrMeta.PROPERTY_NAME: "Spec"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#cfn-appmesh-virtualservice-spec"""
    rp_VirtualServiceName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "VirtualServiceName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#cfn-appmesh-virtualservice-virtualservicename"""
    p_MeshOwner: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MeshOwner"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#cfn-appmesh-virtualservice-meshowner"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#cfn-appmesh-virtualservice-tags"""

    
    @property
    def rv_Uid(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#aws-resource-appmesh-virtualservice-return-values"""
        return GetAtt(resource=self, attr_name="Uid")
    
    @property
    def rv_MeshName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#aws-resource-appmesh-virtualservice-return-values"""
        return GetAtt(resource=self, attr_name="MeshName")
    
    @property
    def rv_MeshOwner(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#aws-resource-appmesh-virtualservice-return-values"""
        return GetAtt(resource=self, attr_name="MeshOwner")
    
    @property
    def rv_ResourceOwner(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#aws-resource-appmesh-virtualservice-return-values"""
        return GetAtt(resource=self, attr_name="ResourceOwner")
    
    @property
    def rv_VirtualServiceName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#aws-resource-appmesh-virtualservice-return-values"""
        return GetAtt(resource=self, attr_name="VirtualServiceName")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html#aws-resource-appmesh-virtualservice-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class Mesh(Resource):
    """
    AWS Object Type = "AWS::AppMesh::Mesh"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.html

    Property Document:
    
    - ``p_MeshName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.html#cfn-appmesh-mesh-meshname
    - ``p_Spec``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.html#cfn-appmesh-mesh-spec
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.html#cfn-appmesh-mesh-tags
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Mesh"

    
    p_MeshName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MeshName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.html#cfn-appmesh-mesh-meshname"""
    p_Spec: typing.Union['MeshMeshSpec', dict] = attr.ib(
        default=None,
        converter=MeshMeshSpec.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(MeshMeshSpec)),
        metadata={AttrMeta.PROPERTY_NAME: "Spec"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.html#cfn-appmesh-mesh-spec"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.html#cfn-appmesh-mesh-tags"""

    
    @property
    def rv_Uid(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.html#aws-resource-appmesh-mesh-return-values"""
        return GetAtt(resource=self, attr_name="Uid")
    
    @property
    def rv_MeshName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.html#aws-resource-appmesh-mesh-return-values"""
        return GetAtt(resource=self, attr_name="MeshName")
    
    @property
    def rv_MeshOwner(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.html#aws-resource-appmesh-mesh-return-values"""
        return GetAtt(resource=self, attr_name="MeshOwner")
    
    @property
    def rv_ResourceOwner(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.html#aws-resource-appmesh-mesh-return-values"""
        return GetAtt(resource=self, attr_name="ResourceOwner")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.html#aws-resource-appmesh-mesh-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
