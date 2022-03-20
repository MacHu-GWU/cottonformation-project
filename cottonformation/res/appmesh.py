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
class PropVirtualRouterPortMapping(Property):
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
class PropVirtualNodeTlsValidationContextSdsTrust(Property):
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
class PropGatewayRouteHttpQueryParameterMatch(Property):
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
class PropRouteDuration(Property):
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
class PropRouteWeightedTarget(Property):
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
class PropGatewayRouteHttpGatewayRoutePrefixRewrite(Property):
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
class PropVirtualGatewayVirtualGatewayListenerTlsAcmCertificate(Property):
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
class PropVirtualNodeFileAccessLog(Property):
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
class PropVirtualNodeAwsCloudMapInstanceAttribute(Property):
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
class PropVirtualGatewayVirtualGatewayTlsValidationContextFileTrust(Property):
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
class PropMeshMeshServiceDiscovery(Property):
    """
    AWS Object Type = "AWS::AppMesh::Mesh.MeshServiceDiscovery"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-meshservicediscovery.html

    Property Document:
    
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Mesh.MeshServiceDiscovery"
    

@attr.s
class PropRouteHttpPathMatch(Property):
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
class PropVirtualGatewayVirtualGatewayHttp2ConnectionPool(Property):
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
class PropGatewayRouteGatewayRouteHostnameRewrite(Property):
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
class PropVirtualNodePortMapping(Property):
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
class PropVirtualServiceVirtualRouterServiceProvider(Property):
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
class PropVirtualNodeListenerTlsSdsCertificate(Property):
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
class PropGatewayRouteQueryParameter(Property):
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
    p_Match: typing.Union['PropGatewayRouteHttpQueryParameterMatch', dict] = attr.ib(
        default=None,
        converter=PropGatewayRouteHttpQueryParameterMatch.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGatewayRouteHttpQueryParameterMatch)),
        metadata={AttrMeta.PROPERTY_NAME: "Match"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-queryparameter.html#cfn-appmesh-gatewayroute-queryparameter-match"""

@attr.s
class PropVirtualGatewayVirtualGatewayGrpcConnectionPool(Property):
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
class PropGatewayRouteGrpcGatewayRouteRewrite(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.GrpcGatewayRouteRewrite"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouterewrite.html

    Property Document:
    
    - ``p_Hostname``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouterewrite.html#cfn-appmesh-gatewayroute-grpcgatewayrouterewrite-hostname
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.GrpcGatewayRouteRewrite"
    
    p_Hostname: typing.Union['PropGatewayRouteGatewayRouteHostnameRewrite', dict] = attr.ib(
        default=None,
        converter=PropGatewayRouteGatewayRouteHostnameRewrite.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGatewayRouteGatewayRouteHostnameRewrite)),
        metadata={AttrMeta.PROPERTY_NAME: "Hostname"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouterewrite.html#cfn-appmesh-gatewayroute-grpcgatewayrouterewrite-hostname"""

@attr.s
class PropVirtualNodeVirtualNodeTcpConnectionPool(Property):
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
class PropVirtualNodeHealthCheck(Property):
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
class PropVirtualNodeAwsCloudMapServiceDiscovery(Property):
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
    p_Attributes: typing.List[typing.Union['PropVirtualNodeAwsCloudMapInstanceAttribute', dict]] = attr.ib(
        default=None,
        converter=PropVirtualNodeAwsCloudMapInstanceAttribute.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropVirtualNodeAwsCloudMapInstanceAttribute), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Attributes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapservicediscovery.html#cfn-appmesh-virtualnode-awscloudmapservicediscovery-attributes"""

@attr.s
class PropGatewayRouteHttpGatewayRoutePathRewrite(Property):
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
class PropVirtualNodeVirtualNodeHttpConnectionPool(Property):
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
class PropVirtualServiceVirtualNodeServiceProvider(Property):
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
class PropVirtualGatewayVirtualGatewayListenerTlsFileCertificate(Property):
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
class PropRouteHttpQueryParameterMatch(Property):
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
class PropVirtualNodeListenerTlsFileCertificate(Property):
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
class PropVirtualGatewaySubjectAlternativeNameMatchers(Property):
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
class PropRouteGrpcRouteAction(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.GrpcRouteAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcrouteaction.html

    Property Document:
    
    - ``rp_WeightedTargets``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcrouteaction.html#cfn-appmesh-route-grpcrouteaction-weightedtargets
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.GrpcRouteAction"
    
    rp_WeightedTargets: typing.List[typing.Union['PropRouteWeightedTarget', dict]] = attr.ib(
        default=None,
        converter=PropRouteWeightedTarget.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropRouteWeightedTarget), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "WeightedTargets"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcrouteaction.html#cfn-appmesh-route-grpcrouteaction-weightedtargets"""

@attr.s
class PropVirtualServiceVirtualServiceProvider(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualService.VirtualServiceProvider"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualserviceprovider.html

    Property Document:
    
    - ``p_VirtualNode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualserviceprovider.html#cfn-appmesh-virtualservice-virtualserviceprovider-virtualnode
    - ``p_VirtualRouter``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualserviceprovider.html#cfn-appmesh-virtualservice-virtualserviceprovider-virtualrouter
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualService.VirtualServiceProvider"
    
    p_VirtualNode: typing.Union['PropVirtualServiceVirtualNodeServiceProvider', dict] = attr.ib(
        default=None,
        converter=PropVirtualServiceVirtualNodeServiceProvider.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualServiceVirtualNodeServiceProvider)),
        metadata={AttrMeta.PROPERTY_NAME: "VirtualNode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualserviceprovider.html#cfn-appmesh-virtualservice-virtualserviceprovider-virtualnode"""
    p_VirtualRouter: typing.Union['PropVirtualServiceVirtualRouterServiceProvider', dict] = attr.ib(
        default=None,
        converter=PropVirtualServiceVirtualRouterServiceProvider.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualServiceVirtualRouterServiceProvider)),
        metadata={AttrMeta.PROPERTY_NAME: "VirtualRouter"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualserviceprovider.html#cfn-appmesh-virtualservice-virtualserviceprovider-virtualrouter"""

@attr.s
class PropVirtualNodeDnsServiceDiscovery(Property):
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
class PropVirtualNodeTlsValidationContextFileTrust(Property):
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
class PropGatewayRouteGatewayRouteRangeMatch(Property):
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
class PropRouteTcpRouteAction(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.TcpRouteAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcprouteaction.html

    Property Document:
    
    - ``rp_WeightedTargets``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcprouteaction.html#cfn-appmesh-route-tcprouteaction-weightedtargets
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.TcpRouteAction"
    
    rp_WeightedTargets: typing.List[typing.Union['PropRouteWeightedTarget', dict]] = attr.ib(
        default=None,
        converter=PropRouteWeightedTarget.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropRouteWeightedTarget), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "WeightedTargets"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcprouteaction.html#cfn-appmesh-route-tcprouteaction-weightedtargets"""

@attr.s
class PropVirtualRouterVirtualRouterListener(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualRouter.VirtualRouterListener"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-virtualrouterlistener.html

    Property Document:
    
    - ``rp_PortMapping``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-virtualrouterlistener.html#cfn-appmesh-virtualrouter-virtualrouterlistener-portmapping
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualRouter.VirtualRouterListener"
    
    rp_PortMapping: typing.Union['PropVirtualRouterPortMapping', dict] = attr.ib(
        default=None,
        converter=PropVirtualRouterPortMapping.from_dict,
        validator=attr.validators.instance_of(PropVirtualRouterPortMapping),
        metadata={AttrMeta.PROPERTY_NAME: "PortMapping"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-virtualrouterlistener.html#cfn-appmesh-virtualrouter-virtualrouterlistener-portmapping"""

@attr.s
class PropVirtualGatewayVirtualGatewayTlsValidationContextSdsTrust(Property):
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
class PropRouteGrpcRetryPolicy(Property):
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
    rp_PerRetryTimeout: typing.Union['PropRouteDuration', dict] = attr.ib(
        default=None,
        converter=PropRouteDuration.from_dict,
        validator=attr.validators.instance_of(PropRouteDuration),
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
class PropVirtualNodeServiceDiscovery(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.ServiceDiscovery"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-servicediscovery.html

    Property Document:
    
    - ``p_AWSCloudMap``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-servicediscovery.html#cfn-appmesh-virtualnode-servicediscovery-awscloudmap
    - ``p_DNS``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-servicediscovery.html#cfn-appmesh-virtualnode-servicediscovery-dns
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.ServiceDiscovery"
    
    p_AWSCloudMap: typing.Union['PropVirtualNodeAwsCloudMapServiceDiscovery', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeAwsCloudMapServiceDiscovery.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeAwsCloudMapServiceDiscovery)),
        metadata={AttrMeta.PROPERTY_NAME: "AWSCloudMap"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-servicediscovery.html#cfn-appmesh-virtualnode-servicediscovery-awscloudmap"""
    p_DNS: typing.Union['PropVirtualNodeDnsServiceDiscovery', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeDnsServiceDiscovery.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeDnsServiceDiscovery)),
        metadata={AttrMeta.PROPERTY_NAME: "DNS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-servicediscovery.html#cfn-appmesh-virtualnode-servicediscovery-dns"""

@attr.s
class PropVirtualNodeDuration(Property):
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
class PropRouteHttpRetryPolicy(Property):
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
    rp_PerRetryTimeout: typing.Union['PropRouteDuration', dict] = attr.ib(
        default=None,
        converter=PropRouteDuration.from_dict,
        validator=attr.validators.instance_of(PropRouteDuration),
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
class PropVirtualGatewayVirtualGatewayPortMapping(Property):
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
class PropGatewayRouteHttpGatewayRouteRewrite(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.HttpGatewayRouteRewrite"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite.html

    Property Document:
    
    - ``p_Hostname``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite.html#cfn-appmesh-gatewayroute-httpgatewayrouterewrite-hostname
    - ``p_Path``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite.html#cfn-appmesh-gatewayroute-httpgatewayrouterewrite-path
    - ``p_Prefix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite.html#cfn-appmesh-gatewayroute-httpgatewayrouterewrite-prefix
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.HttpGatewayRouteRewrite"
    
    p_Hostname: typing.Union['PropGatewayRouteGatewayRouteHostnameRewrite', dict] = attr.ib(
        default=None,
        converter=PropGatewayRouteGatewayRouteHostnameRewrite.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGatewayRouteGatewayRouteHostnameRewrite)),
        metadata={AttrMeta.PROPERTY_NAME: "Hostname"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite.html#cfn-appmesh-gatewayroute-httpgatewayrouterewrite-hostname"""
    p_Path: typing.Union['PropGatewayRouteHttpGatewayRoutePathRewrite', dict] = attr.ib(
        default=None,
        converter=PropGatewayRouteHttpGatewayRoutePathRewrite.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGatewayRouteHttpGatewayRoutePathRewrite)),
        metadata={AttrMeta.PROPERTY_NAME: "Path"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite.html#cfn-appmesh-gatewayroute-httpgatewayrouterewrite-path"""
    p_Prefix: typing.Union['PropGatewayRouteHttpGatewayRoutePrefixRewrite', dict] = attr.ib(
        default=None,
        converter=PropGatewayRouteHttpGatewayRoutePrefixRewrite.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGatewayRouteHttpGatewayRoutePrefixRewrite)),
        metadata={AttrMeta.PROPERTY_NAME: "Prefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite.html#cfn-appmesh-gatewayroute-httpgatewayrouterewrite-prefix"""

@attr.s
class PropVirtualNodeListenerTlsAcmCertificate(Property):
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
class PropRouteGrpcTimeout(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.GrpcTimeout"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpctimeout.html

    Property Document:
    
    - ``p_Idle``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpctimeout.html#cfn-appmesh-route-grpctimeout-idle
    - ``p_PerRequest``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpctimeout.html#cfn-appmesh-route-grpctimeout-perrequest
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.GrpcTimeout"
    
    p_Idle: typing.Union['PropRouteDuration', dict] = attr.ib(
        default=None,
        converter=PropRouteDuration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRouteDuration)),
        metadata={AttrMeta.PROPERTY_NAME: "Idle"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpctimeout.html#cfn-appmesh-route-grpctimeout-idle"""
    p_PerRequest: typing.Union['PropRouteDuration', dict] = attr.ib(
        default=None,
        converter=PropRouteDuration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRouteDuration)),
        metadata={AttrMeta.PROPERTY_NAME: "PerRequest"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpctimeout.html#cfn-appmesh-route-grpctimeout-perrequest"""

@attr.s
class PropGatewayRouteGatewayRouteHostnameMatch(Property):
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
class PropVirtualNodeVirtualNodeHttp2ConnectionPool(Property):
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
class PropVirtualNodeListenerTlsCertificate(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.ListenerTlsCertificate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlscertificate.html

    Property Document:
    
    - ``p_ACM``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlscertificate.html#cfn-appmesh-virtualnode-listenertlscertificate-acm
    - ``p_File``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlscertificate.html#cfn-appmesh-virtualnode-listenertlscertificate-file
    - ``p_SDS``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlscertificate.html#cfn-appmesh-virtualnode-listenertlscertificate-sds
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.ListenerTlsCertificate"
    
    p_ACM: typing.Union['PropVirtualNodeListenerTlsAcmCertificate', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeListenerTlsAcmCertificate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeListenerTlsAcmCertificate)),
        metadata={AttrMeta.PROPERTY_NAME: "ACM"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlscertificate.html#cfn-appmesh-virtualnode-listenertlscertificate-acm"""
    p_File: typing.Union['PropVirtualNodeListenerTlsFileCertificate', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeListenerTlsFileCertificate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeListenerTlsFileCertificate)),
        metadata={AttrMeta.PROPERTY_NAME: "File"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlscertificate.html#cfn-appmesh-virtualnode-listenertlscertificate-file"""
    p_SDS: typing.Union['PropVirtualNodeListenerTlsSdsCertificate', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeListenerTlsSdsCertificate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeListenerTlsSdsCertificate)),
        metadata={AttrMeta.PROPERTY_NAME: "SDS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlscertificate.html#cfn-appmesh-virtualnode-listenertlscertificate-sds"""

@attr.s
class PropRouteTcpTimeout(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.TcpTimeout"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcptimeout.html

    Property Document:
    
    - ``p_Idle``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcptimeout.html#cfn-appmesh-route-tcptimeout-idle
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.TcpTimeout"
    
    p_Idle: typing.Union['PropRouteDuration', dict] = attr.ib(
        default=None,
        converter=PropRouteDuration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRouteDuration)),
        metadata={AttrMeta.PROPERTY_NAME: "Idle"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcptimeout.html#cfn-appmesh-route-tcptimeout-idle"""

@attr.s
class PropVirtualGatewayVirtualGatewayFileAccessLog(Property):
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
class PropGatewayRouteGatewayRouteVirtualService(Property):
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
class PropRouteHttpTimeout(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.HttpTimeout"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httptimeout.html

    Property Document:
    
    - ``p_Idle``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httptimeout.html#cfn-appmesh-route-httptimeout-idle
    - ``p_PerRequest``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httptimeout.html#cfn-appmesh-route-httptimeout-perrequest
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.HttpTimeout"
    
    p_Idle: typing.Union['PropRouteDuration', dict] = attr.ib(
        default=None,
        converter=PropRouteDuration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRouteDuration)),
        metadata={AttrMeta.PROPERTY_NAME: "Idle"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httptimeout.html#cfn-appmesh-route-httptimeout-idle"""
    p_PerRequest: typing.Union['PropRouteDuration', dict] = attr.ib(
        default=None,
        converter=PropRouteDuration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRouteDuration)),
        metadata={AttrMeta.PROPERTY_NAME: "PerRequest"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httptimeout.html#cfn-appmesh-route-httptimeout-perrequest"""

@attr.s
class PropVirtualServiceVirtualServiceSpec(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualService.VirtualServiceSpec"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualservicespec.html

    Property Document:
    
    - ``p_Provider``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualservicespec.html#cfn-appmesh-virtualservice-virtualservicespec-provider
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualService.VirtualServiceSpec"
    
    p_Provider: typing.Union['PropVirtualServiceVirtualServiceProvider', dict] = attr.ib(
        default=None,
        converter=PropVirtualServiceVirtualServiceProvider.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualServiceVirtualServiceProvider)),
        metadata={AttrMeta.PROPERTY_NAME: "Provider"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualservicespec.html#cfn-appmesh-virtualservice-virtualservicespec-provider"""

@attr.s
class PropVirtualGatewayVirtualGatewayHttpConnectionPool(Property):
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
class PropVirtualNodeOutlierDetection(Property):
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
    
    rp_BaseEjectionDuration: typing.Union['PropVirtualNodeDuration', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeDuration.from_dict,
        validator=attr.validators.instance_of(PropVirtualNodeDuration),
        metadata={AttrMeta.PROPERTY_NAME: "BaseEjectionDuration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-outlierdetection.html#cfn-appmesh-virtualnode-outlierdetection-baseejectionduration"""
    rp_Interval: typing.Union['PropVirtualNodeDuration', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeDuration.from_dict,
        validator=attr.validators.instance_of(PropVirtualNodeDuration),
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
class PropVirtualGatewayVirtualGatewayHealthCheckPolicy(Property):
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
class PropGatewayRouteHttpPathMatch(Property):
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
class PropVirtualNodeTlsValidationContextAcmTrust(Property):
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
class PropMeshEgressFilter(Property):
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
class PropVirtualNodeClientTlsCertificate(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.ClientTlsCertificate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clienttlscertificate.html

    Property Document:
    
    - ``p_File``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clienttlscertificate.html#cfn-appmesh-virtualnode-clienttlscertificate-file
    - ``p_SDS``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clienttlscertificate.html#cfn-appmesh-virtualnode-clienttlscertificate-sds
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.ClientTlsCertificate"
    
    p_File: typing.Union['PropVirtualNodeListenerTlsFileCertificate', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeListenerTlsFileCertificate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeListenerTlsFileCertificate)),
        metadata={AttrMeta.PROPERTY_NAME: "File"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clienttlscertificate.html#cfn-appmesh-virtualnode-clienttlscertificate-file"""
    p_SDS: typing.Union['PropVirtualNodeListenerTlsSdsCertificate', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeListenerTlsSdsCertificate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeListenerTlsSdsCertificate)),
        metadata={AttrMeta.PROPERTY_NAME: "SDS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clienttlscertificate.html#cfn-appmesh-virtualnode-clienttlscertificate-sds"""

@attr.s
class PropVirtualNodeListenerTlsValidationContextTrust(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.ListenerTlsValidationContextTrust"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontexttrust.html

    Property Document:
    
    - ``p_File``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontexttrust.html#cfn-appmesh-virtualnode-listenertlsvalidationcontexttrust-file
    - ``p_SDS``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontexttrust.html#cfn-appmesh-virtualnode-listenertlsvalidationcontexttrust-sds
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.ListenerTlsValidationContextTrust"
    
    p_File: typing.Union['PropVirtualNodeTlsValidationContextFileTrust', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeTlsValidationContextFileTrust.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeTlsValidationContextFileTrust)),
        metadata={AttrMeta.PROPERTY_NAME: "File"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontexttrust.html#cfn-appmesh-virtualnode-listenertlsvalidationcontexttrust-file"""
    p_SDS: typing.Union['PropVirtualNodeTlsValidationContextSdsTrust', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeTlsValidationContextSdsTrust.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeTlsValidationContextSdsTrust)),
        metadata={AttrMeta.PROPERTY_NAME: "SDS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontexttrust.html#cfn-appmesh-virtualnode-listenertlsvalidationcontexttrust-sds"""

@attr.s
class PropVirtualGatewayVirtualGatewayTlsValidationContextAcmTrust(Property):
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
class PropRouteHttpRouteAction(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.HttpRouteAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteaction.html

    Property Document:
    
    - ``rp_WeightedTargets``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteaction.html#cfn-appmesh-route-httprouteaction-weightedtargets
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.HttpRouteAction"
    
    rp_WeightedTargets: typing.List[typing.Union['PropRouteWeightedTarget', dict]] = attr.ib(
        default=None,
        converter=PropRouteWeightedTarget.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropRouteWeightedTarget), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "WeightedTargets"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteaction.html#cfn-appmesh-route-httprouteaction-weightedtargets"""

@attr.s
class PropVirtualNodeAccessLog(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.AccessLog"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-accesslog.html

    Property Document:
    
    - ``p_File``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-accesslog.html#cfn-appmesh-virtualnode-accesslog-file
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.AccessLog"
    
    p_File: typing.Union['PropVirtualNodeFileAccessLog', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeFileAccessLog.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeFileAccessLog)),
        metadata={AttrMeta.PROPERTY_NAME: "File"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-accesslog.html#cfn-appmesh-virtualnode-accesslog-file"""

@attr.s
class PropVirtualGatewayVirtualGatewayListenerTlsValidationContextTrust(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTlsValidationContextTrust"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust.html

    Property Document:
    
    - ``p_File``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust-file
    - ``p_SDS``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust-sds
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTlsValidationContextTrust"
    
    p_File: typing.Union['PropVirtualGatewayVirtualGatewayTlsValidationContextFileTrust', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewayTlsValidationContextFileTrust.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualGatewayVirtualGatewayTlsValidationContextFileTrust)),
        metadata={AttrMeta.PROPERTY_NAME: "File"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust-file"""
    p_SDS: typing.Union['PropVirtualGatewayVirtualGatewayTlsValidationContextSdsTrust', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewayTlsValidationContextSdsTrust.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualGatewayVirtualGatewayTlsValidationContextSdsTrust)),
        metadata={AttrMeta.PROPERTY_NAME: "SDS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust-sds"""

@attr.s
class PropVirtualGatewayVirtualGatewayListenerTlsSdsCertificate(Property):
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
class PropVirtualNodeSubjectAlternativeNameMatchers(Property):
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
class PropVirtualNodeSubjectAlternativeNames(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.SubjectAlternativeNames"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-subjectalternativenames.html

    Property Document:
    
    - ``rp_Match``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-subjectalternativenames.html#cfn-appmesh-virtualnode-subjectalternativenames-match
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.SubjectAlternativeNames"
    
    rp_Match: typing.Union['PropVirtualNodeSubjectAlternativeNameMatchers', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeSubjectAlternativeNameMatchers.from_dict,
        validator=attr.validators.instance_of(PropVirtualNodeSubjectAlternativeNameMatchers),
        metadata={AttrMeta.PROPERTY_NAME: "Match"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-subjectalternativenames.html#cfn-appmesh-virtualnode-subjectalternativenames-match"""

@attr.s
class PropVirtualNodeVirtualNodeGrpcConnectionPool(Property):
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
class PropRouteMatchRange(Property):
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
class PropVirtualGatewayVirtualGatewayTlsValidationContextTrust(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayTlsValidationContextTrust"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust.html

    Property Document:
    
    - ``p_ACM``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-acm
    - ``p_File``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-file
    - ``p_SDS``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-sds
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayTlsValidationContextTrust"
    
    p_ACM: typing.Union['PropVirtualGatewayVirtualGatewayTlsValidationContextAcmTrust', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewayTlsValidationContextAcmTrust.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualGatewayVirtualGatewayTlsValidationContextAcmTrust)),
        metadata={AttrMeta.PROPERTY_NAME: "ACM"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-acm"""
    p_File: typing.Union['PropVirtualGatewayVirtualGatewayTlsValidationContextFileTrust', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewayTlsValidationContextFileTrust.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualGatewayVirtualGatewayTlsValidationContextFileTrust)),
        metadata={AttrMeta.PROPERTY_NAME: "File"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-file"""
    p_SDS: typing.Union['PropVirtualGatewayVirtualGatewayTlsValidationContextSdsTrust', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewayTlsValidationContextSdsTrust.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualGatewayVirtualGatewayTlsValidationContextSdsTrust)),
        metadata={AttrMeta.PROPERTY_NAME: "SDS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-sds"""

@attr.s
class PropRouteGrpcRouteMetadataMatchMethod(Property):
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
    p_Range: typing.Union['PropRouteMatchRange', dict] = attr.ib(
        default=None,
        converter=PropRouteMatchRange.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRouteMatchRange)),
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
class PropGatewayRouteHttpGatewayRouteHeaderMatch(Property):
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
    p_Range: typing.Union['PropGatewayRouteGatewayRouteRangeMatch', dict] = attr.ib(
        default=None,
        converter=PropGatewayRouteGatewayRouteRangeMatch.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGatewayRouteGatewayRouteRangeMatch)),
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
class PropRouteHeaderMatchMethod(Property):
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
    p_Range: typing.Union['PropRouteMatchRange', dict] = attr.ib(
        default=None,
        converter=PropRouteMatchRange.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRouteMatchRange)),
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
class PropGatewayRouteHttpGatewayRouteHeader(Property):
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
    p_Match: typing.Union['PropGatewayRouteHttpGatewayRouteHeaderMatch', dict] = attr.ib(
        default=None,
        converter=PropGatewayRouteHttpGatewayRouteHeaderMatch.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGatewayRouteHttpGatewayRouteHeaderMatch)),
        metadata={AttrMeta.PROPERTY_NAME: "Match"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheader.html#cfn-appmesh-gatewayroute-httpgatewayrouteheader-match"""

@attr.s
class PropVirtualNodeListenerTlsValidationContext(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.ListenerTlsValidationContext"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontext.html

    Property Document:
    
    - ``rp_Trust``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontext.html#cfn-appmesh-virtualnode-listenertlsvalidationcontext-trust
    - ``p_SubjectAlternativeNames``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontext.html#cfn-appmesh-virtualnode-listenertlsvalidationcontext-subjectalternativenames
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.ListenerTlsValidationContext"
    
    rp_Trust: typing.Union['PropVirtualNodeListenerTlsValidationContextTrust', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeListenerTlsValidationContextTrust.from_dict,
        validator=attr.validators.instance_of(PropVirtualNodeListenerTlsValidationContextTrust),
        metadata={AttrMeta.PROPERTY_NAME: "Trust"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontext.html#cfn-appmesh-virtualnode-listenertlsvalidationcontext-trust"""
    p_SubjectAlternativeNames: typing.Union['PropVirtualNodeSubjectAlternativeNames', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeSubjectAlternativeNames.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeSubjectAlternativeNames)),
        metadata={AttrMeta.PROPERTY_NAME: "SubjectAlternativeNames"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontext.html#cfn-appmesh-virtualnode-listenertlsvalidationcontext-subjectalternativenames"""

@attr.s
class PropVirtualNodeTcpTimeout(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.TcpTimeout"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tcptimeout.html

    Property Document:
    
    - ``p_Idle``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tcptimeout.html#cfn-appmesh-virtualnode-tcptimeout-idle
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.TcpTimeout"
    
    p_Idle: typing.Union['PropVirtualNodeDuration', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeDuration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeDuration)),
        metadata={AttrMeta.PROPERTY_NAME: "Idle"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tcptimeout.html#cfn-appmesh-virtualnode-tcptimeout-idle"""

@attr.s
class PropVirtualNodeListenerTls(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.ListenerTls"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertls.html

    Property Document:
    
    - ``rp_Certificate``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertls.html#cfn-appmesh-virtualnode-listenertls-certificate
    - ``rp_Mode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertls.html#cfn-appmesh-virtualnode-listenertls-mode
    - ``p_Validation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertls.html#cfn-appmesh-virtualnode-listenertls-validation
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.ListenerTls"
    
    rp_Certificate: typing.Union['PropVirtualNodeListenerTlsCertificate', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeListenerTlsCertificate.from_dict,
        validator=attr.validators.instance_of(PropVirtualNodeListenerTlsCertificate),
        metadata={AttrMeta.PROPERTY_NAME: "Certificate"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertls.html#cfn-appmesh-virtualnode-listenertls-certificate"""
    rp_Mode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Mode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertls.html#cfn-appmesh-virtualnode-listenertls-mode"""
    p_Validation: typing.Union['PropVirtualNodeListenerTlsValidationContext', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeListenerTlsValidationContext.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeListenerTlsValidationContext)),
        metadata={AttrMeta.PROPERTY_NAME: "Validation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertls.html#cfn-appmesh-virtualnode-listenertls-validation"""

@attr.s
class PropGatewayRouteGatewayRouteMetadataMatch(Property):
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
    p_Range: typing.Union['PropGatewayRouteGatewayRouteRangeMatch', dict] = attr.ib(
        default=None,
        converter=PropGatewayRouteGatewayRouteRangeMatch.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGatewayRouteGatewayRouteRangeMatch)),
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
class PropVirtualGatewayVirtualGatewayListenerTlsCertificate(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTlsCertificate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlscertificate.html

    Property Document:
    
    - ``p_ACM``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlscertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-acm
    - ``p_File``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlscertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-file
    - ``p_SDS``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlscertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-sds
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTlsCertificate"
    
    p_ACM: typing.Union['PropVirtualGatewayVirtualGatewayListenerTlsAcmCertificate', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewayListenerTlsAcmCertificate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualGatewayVirtualGatewayListenerTlsAcmCertificate)),
        metadata={AttrMeta.PROPERTY_NAME: "ACM"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlscertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-acm"""
    p_File: typing.Union['PropVirtualGatewayVirtualGatewayListenerTlsFileCertificate', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewayListenerTlsFileCertificate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualGatewayVirtualGatewayListenerTlsFileCertificate)),
        metadata={AttrMeta.PROPERTY_NAME: "File"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlscertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-file"""
    p_SDS: typing.Union['PropVirtualGatewayVirtualGatewayListenerTlsSdsCertificate', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewayListenerTlsSdsCertificate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualGatewayVirtualGatewayListenerTlsSdsCertificate)),
        metadata={AttrMeta.PROPERTY_NAME: "SDS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlscertificate.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-sds"""

@attr.s
class PropVirtualGatewayVirtualGatewayConnectionPool(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayConnectionPool"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayconnectionpool.html

    Property Document:
    
    - ``p_GRPC``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayconnectionpool.html#cfn-appmesh-virtualgateway-virtualgatewayconnectionpool-grpc
    - ``p_HTTP``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayconnectionpool.html#cfn-appmesh-virtualgateway-virtualgatewayconnectionpool-http
    - ``p_HTTP2``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayconnectionpool.html#cfn-appmesh-virtualgateway-virtualgatewayconnectionpool-http2
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayConnectionPool"
    
    p_GRPC: typing.Union['PropVirtualGatewayVirtualGatewayGrpcConnectionPool', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewayGrpcConnectionPool.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualGatewayVirtualGatewayGrpcConnectionPool)),
        metadata={AttrMeta.PROPERTY_NAME: "GRPC"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayconnectionpool.html#cfn-appmesh-virtualgateway-virtualgatewayconnectionpool-grpc"""
    p_HTTP: typing.Union['PropVirtualGatewayVirtualGatewayHttpConnectionPool', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewayHttpConnectionPool.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualGatewayVirtualGatewayHttpConnectionPool)),
        metadata={AttrMeta.PROPERTY_NAME: "HTTP"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayconnectionpool.html#cfn-appmesh-virtualgateway-virtualgatewayconnectionpool-http"""
    p_HTTP2: typing.Union['PropVirtualGatewayVirtualGatewayHttp2ConnectionPool', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewayHttp2ConnectionPool.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualGatewayVirtualGatewayHttp2ConnectionPool)),
        metadata={AttrMeta.PROPERTY_NAME: "HTTP2"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayconnectionpool.html#cfn-appmesh-virtualgateway-virtualgatewayconnectionpool-http2"""

@attr.s
class PropVirtualGatewaySubjectAlternativeNames(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.SubjectAlternativeNames"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-subjectalternativenames.html

    Property Document:
    
    - ``rp_Match``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-subjectalternativenames.html#cfn-appmesh-virtualgateway-subjectalternativenames-match
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.SubjectAlternativeNames"
    
    rp_Match: typing.Union['PropVirtualGatewaySubjectAlternativeNameMatchers', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewaySubjectAlternativeNameMatchers.from_dict,
        validator=attr.validators.instance_of(PropVirtualGatewaySubjectAlternativeNameMatchers),
        metadata={AttrMeta.PROPERTY_NAME: "Match"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-subjectalternativenames.html#cfn-appmesh-virtualgateway-subjectalternativenames-match"""

@attr.s
class PropRouteGrpcRouteMetadata(Property):
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
    p_Match: typing.Union['PropRouteGrpcRouteMetadataMatchMethod', dict] = attr.ib(
        default=None,
        converter=PropRouteGrpcRouteMetadataMatchMethod.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRouteGrpcRouteMetadataMatchMethod)),
        metadata={AttrMeta.PROPERTY_NAME: "Match"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadata.html#cfn-appmesh-route-grpcroutemetadata-match"""

@attr.s
class PropRouteQueryParameter(Property):
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
    p_Match: typing.Union['PropRouteHttpQueryParameterMatch', dict] = attr.ib(
        default=None,
        converter=PropRouteHttpQueryParameterMatch.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRouteHttpQueryParameterMatch)),
        metadata={AttrMeta.PROPERTY_NAME: "Match"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-queryparameter.html#cfn-appmesh-route-queryparameter-match"""

@attr.s
class PropGatewayRouteGatewayRouteTarget(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.GatewayRouteTarget"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutetarget.html

    Property Document:
    
    - ``rp_VirtualService``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutetarget.html#cfn-appmesh-gatewayroute-gatewayroutetarget-virtualservice
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.GatewayRouteTarget"
    
    rp_VirtualService: typing.Union['PropGatewayRouteGatewayRouteVirtualService', dict] = attr.ib(
        default=None,
        converter=PropGatewayRouteGatewayRouteVirtualService.from_dict,
        validator=attr.validators.instance_of(PropGatewayRouteGatewayRouteVirtualService),
        metadata={AttrMeta.PROPERTY_NAME: "VirtualService"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutetarget.html#cfn-appmesh-gatewayroute-gatewayroutetarget-virtualservice"""

@attr.s
class PropVirtualNodeHttpTimeout(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.HttpTimeout"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-httptimeout.html

    Property Document:
    
    - ``p_Idle``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-httptimeout.html#cfn-appmesh-virtualnode-httptimeout-idle
    - ``p_PerRequest``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-httptimeout.html#cfn-appmesh-virtualnode-httptimeout-perrequest
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.HttpTimeout"
    
    p_Idle: typing.Union['PropVirtualNodeDuration', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeDuration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeDuration)),
        metadata={AttrMeta.PROPERTY_NAME: "Idle"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-httptimeout.html#cfn-appmesh-virtualnode-httptimeout-idle"""
    p_PerRequest: typing.Union['PropVirtualNodeDuration', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeDuration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeDuration)),
        metadata={AttrMeta.PROPERTY_NAME: "PerRequest"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-httptimeout.html#cfn-appmesh-virtualnode-httptimeout-perrequest"""

@attr.s
class PropVirtualGatewayVirtualGatewayClientTlsCertificate(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayClientTlsCertificate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclienttlscertificate.html

    Property Document:
    
    - ``p_File``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclienttlscertificate.html#cfn-appmesh-virtualgateway-virtualgatewayclienttlscertificate-file
    - ``p_SDS``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclienttlscertificate.html#cfn-appmesh-virtualgateway-virtualgatewayclienttlscertificate-sds
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayClientTlsCertificate"
    
    p_File: typing.Union['PropVirtualGatewayVirtualGatewayListenerTlsFileCertificate', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewayListenerTlsFileCertificate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualGatewayVirtualGatewayListenerTlsFileCertificate)),
        metadata={AttrMeta.PROPERTY_NAME: "File"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclienttlscertificate.html#cfn-appmesh-virtualgateway-virtualgatewayclienttlscertificate-file"""
    p_SDS: typing.Union['PropVirtualGatewayVirtualGatewayListenerTlsSdsCertificate', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewayListenerTlsSdsCertificate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualGatewayVirtualGatewayListenerTlsSdsCertificate)),
        metadata={AttrMeta.PROPERTY_NAME: "SDS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclienttlscertificate.html#cfn-appmesh-virtualgateway-virtualgatewayclienttlscertificate-sds"""

@attr.s
class PropVirtualGatewayVirtualGatewayListenerTlsValidationContext(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTlsValidationContext"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext.html

    Property Document:
    
    - ``rp_Trust``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext-trust
    - ``p_SubjectAlternativeNames``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext-subjectalternativenames
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTlsValidationContext"
    
    rp_Trust: typing.Union['PropVirtualGatewayVirtualGatewayListenerTlsValidationContextTrust', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewayListenerTlsValidationContextTrust.from_dict,
        validator=attr.validators.instance_of(PropVirtualGatewayVirtualGatewayListenerTlsValidationContextTrust),
        metadata={AttrMeta.PROPERTY_NAME: "Trust"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext-trust"""
    p_SubjectAlternativeNames: typing.Union['PropVirtualGatewaySubjectAlternativeNames', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewaySubjectAlternativeNames.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualGatewaySubjectAlternativeNames)),
        metadata={AttrMeta.PROPERTY_NAME: "SubjectAlternativeNames"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext-subjectalternativenames"""

@attr.s
class PropVirtualRouterVirtualRouterSpec(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualRouter.VirtualRouterSpec"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-virtualrouterspec.html

    Property Document:
    
    - ``rp_Listeners``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-virtualrouterspec.html#cfn-appmesh-virtualrouter-virtualrouterspec-listeners
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualRouter.VirtualRouterSpec"
    
    rp_Listeners: typing.List[typing.Union['PropVirtualRouterVirtualRouterListener', dict]] = attr.ib(
        default=None,
        converter=PropVirtualRouterVirtualRouterListener.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropVirtualRouterVirtualRouterListener), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Listeners"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-virtualrouterspec.html#cfn-appmesh-virtualrouter-virtualrouterspec-listeners"""

@attr.s
class PropVirtualGatewayVirtualGatewayListenerTls(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTls"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertls.html

    Property Document:
    
    - ``rp_Certificate``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertls.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertls-certificate
    - ``rp_Mode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertls.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertls-mode
    - ``p_Validation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertls.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertls-validation
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTls"
    
    rp_Certificate: typing.Union['PropVirtualGatewayVirtualGatewayListenerTlsCertificate', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewayListenerTlsCertificate.from_dict,
        validator=attr.validators.instance_of(PropVirtualGatewayVirtualGatewayListenerTlsCertificate),
        metadata={AttrMeta.PROPERTY_NAME: "Certificate"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertls.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertls-certificate"""
    rp_Mode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Mode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertls.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertls-mode"""
    p_Validation: typing.Union['PropVirtualGatewayVirtualGatewayListenerTlsValidationContext', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewayListenerTlsValidationContext.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualGatewayVirtualGatewayListenerTlsValidationContext)),
        metadata={AttrMeta.PROPERTY_NAME: "Validation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertls.html#cfn-appmesh-virtualgateway-virtualgatewaylistenertls-validation"""

@attr.s
class PropRouteGrpcRouteMatch(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.GrpcRouteMatch"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutematch.html

    Property Document:
    
    - ``p_Metadata``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutematch.html#cfn-appmesh-route-grpcroutematch-metadata
    - ``p_MethodName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutematch.html#cfn-appmesh-route-grpcroutematch-methodname
    - ``p_ServiceName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutematch.html#cfn-appmesh-route-grpcroutematch-servicename
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.GrpcRouteMatch"
    
    p_Metadata: typing.List[typing.Union['PropRouteGrpcRouteMetadata', dict]] = attr.ib(
        default=None,
        converter=PropRouteGrpcRouteMetadata.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropRouteGrpcRouteMetadata), iterable_validator=attr.validators.instance_of(list))),
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
class PropVirtualNodeGrpcTimeout(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.GrpcTimeout"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-grpctimeout.html

    Property Document:
    
    - ``p_Idle``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-grpctimeout.html#cfn-appmesh-virtualnode-grpctimeout-idle
    - ``p_PerRequest``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-grpctimeout.html#cfn-appmesh-virtualnode-grpctimeout-perrequest
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.GrpcTimeout"
    
    p_Idle: typing.Union['PropVirtualNodeDuration', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeDuration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeDuration)),
        metadata={AttrMeta.PROPERTY_NAME: "Idle"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-grpctimeout.html#cfn-appmesh-virtualnode-grpctimeout-idle"""
    p_PerRequest: typing.Union['PropVirtualNodeDuration', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeDuration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeDuration)),
        metadata={AttrMeta.PROPERTY_NAME: "PerRequest"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-grpctimeout.html#cfn-appmesh-virtualnode-grpctimeout-perrequest"""

@attr.s
class PropVirtualNodeVirtualNodeConnectionPool(Property):
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
    
    p_GRPC: typing.Union['PropVirtualNodeVirtualNodeGrpcConnectionPool', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeVirtualNodeGrpcConnectionPool.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeVirtualNodeGrpcConnectionPool)),
        metadata={AttrMeta.PROPERTY_NAME: "GRPC"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodeconnectionpool.html#cfn-appmesh-virtualnode-virtualnodeconnectionpool-grpc"""
    p_HTTP: typing.Union['PropVirtualNodeVirtualNodeHttpConnectionPool', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeVirtualNodeHttpConnectionPool.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeVirtualNodeHttpConnectionPool)),
        metadata={AttrMeta.PROPERTY_NAME: "HTTP"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodeconnectionpool.html#cfn-appmesh-virtualnode-virtualnodeconnectionpool-http"""
    p_HTTP2: typing.Union['PropVirtualNodeVirtualNodeHttp2ConnectionPool', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeVirtualNodeHttp2ConnectionPool.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeVirtualNodeHttp2ConnectionPool)),
        metadata={AttrMeta.PROPERTY_NAME: "HTTP2"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodeconnectionpool.html#cfn-appmesh-virtualnode-virtualnodeconnectionpool-http2"""
    p_TCP: typing.Union['PropVirtualNodeVirtualNodeTcpConnectionPool', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeVirtualNodeTcpConnectionPool.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeVirtualNodeTcpConnectionPool)),
        metadata={AttrMeta.PROPERTY_NAME: "TCP"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodeconnectionpool.html#cfn-appmesh-virtualnode-virtualnodeconnectionpool-tcp"""

@attr.s
class PropVirtualNodeLogging(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.Logging"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-logging.html

    Property Document:
    
    - ``p_AccessLog``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-logging.html#cfn-appmesh-virtualnode-logging-accesslog
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.Logging"
    
    p_AccessLog: typing.Union['PropVirtualNodeAccessLog', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeAccessLog.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeAccessLog)),
        metadata={AttrMeta.PROPERTY_NAME: "AccessLog"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-logging.html#cfn-appmesh-virtualnode-logging-accesslog"""

@attr.s
class PropRouteTcpRoute(Property):
    """
    AWS Object Type = "AWS::AppMesh::Route.TcpRoute"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcproute.html

    Property Document:
    
    - ``rp_Action``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcproute.html#cfn-appmesh-route-tcproute-action
    - ``p_Timeout``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcproute.html#cfn-appmesh-route-tcproute-timeout
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Route.TcpRoute"
    
    rp_Action: typing.Union['PropRouteTcpRouteAction', dict] = attr.ib(
        default=None,
        converter=PropRouteTcpRouteAction.from_dict,
        validator=attr.validators.instance_of(PropRouteTcpRouteAction),
        metadata={AttrMeta.PROPERTY_NAME: "Action"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcproute.html#cfn-appmesh-route-tcproute-action"""
    p_Timeout: typing.Union['PropRouteTcpTimeout', dict] = attr.ib(
        default=None,
        converter=PropRouteTcpTimeout.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRouteTcpTimeout)),
        metadata={AttrMeta.PROPERTY_NAME: "Timeout"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcproute.html#cfn-appmesh-route-tcproute-timeout"""

@attr.s
class PropVirtualGatewayVirtualGatewayListener(Property):
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
    
    rp_PortMapping: typing.Union['PropVirtualGatewayVirtualGatewayPortMapping', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewayPortMapping.from_dict,
        validator=attr.validators.instance_of(PropVirtualGatewayVirtualGatewayPortMapping),
        metadata={AttrMeta.PROPERTY_NAME: "PortMapping"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistener.html#cfn-appmesh-virtualgateway-virtualgatewaylistener-portmapping"""
    p_ConnectionPool: typing.Union['PropVirtualGatewayVirtualGatewayConnectionPool', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewayConnectionPool.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualGatewayVirtualGatewayConnectionPool)),
        metadata={AttrMeta.PROPERTY_NAME: "ConnectionPool"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistener.html#cfn-appmesh-virtualgateway-virtualgatewaylistener-connectionpool"""
    p_HealthCheck: typing.Union['PropVirtualGatewayVirtualGatewayHealthCheckPolicy', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewayHealthCheckPolicy.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualGatewayVirtualGatewayHealthCheckPolicy)),
        metadata={AttrMeta.PROPERTY_NAME: "HealthCheck"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistener.html#cfn-appmesh-virtualgateway-virtualgatewaylistener-healthcheck"""
    p_TLS: typing.Union['PropVirtualGatewayVirtualGatewayListenerTls', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewayListenerTls.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualGatewayVirtualGatewayListenerTls)),
        metadata={AttrMeta.PROPERTY_NAME: "TLS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistener.html#cfn-appmesh-virtualgateway-virtualgatewaylistener-tls"""

@attr.s
class PropVirtualNodeTlsValidationContextTrust(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.TlsValidationContextTrust"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontexttrust.html

    Property Document:
    
    - ``p_ACM``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontexttrust.html#cfn-appmesh-virtualnode-tlsvalidationcontexttrust-acm
    - ``p_File``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontexttrust.html#cfn-appmesh-virtualnode-tlsvalidationcontexttrust-file
    - ``p_SDS``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontexttrust.html#cfn-appmesh-virtualnode-tlsvalidationcontexttrust-sds
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.TlsValidationContextTrust"
    
    p_ACM: typing.Union['PropVirtualNodeTlsValidationContextAcmTrust', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeTlsValidationContextAcmTrust.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeTlsValidationContextAcmTrust)),
        metadata={AttrMeta.PROPERTY_NAME: "ACM"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontexttrust.html#cfn-appmesh-virtualnode-tlsvalidationcontexttrust-acm"""
    p_File: typing.Union['PropVirtualNodeTlsValidationContextFileTrust', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeTlsValidationContextFileTrust.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeTlsValidationContextFileTrust)),
        metadata={AttrMeta.PROPERTY_NAME: "File"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontexttrust.html#cfn-appmesh-virtualnode-tlsvalidationcontexttrust-file"""
    p_SDS: typing.Union['PropVirtualNodeTlsValidationContextSdsTrust', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeTlsValidationContextSdsTrust.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeTlsValidationContextSdsTrust)),
        metadata={AttrMeta.PROPERTY_NAME: "SDS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontexttrust.html#cfn-appmesh-virtualnode-tlsvalidationcontexttrust-sds"""

@attr.s
class PropGatewayRouteGrpcGatewayRouteMetadata(Property):
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
    p_Match: typing.Union['PropGatewayRouteGatewayRouteMetadataMatch', dict] = attr.ib(
        default=None,
        converter=PropGatewayRouteGatewayRouteMetadataMatch.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGatewayRouteGatewayRouteMetadataMatch)),
        metadata={AttrMeta.PROPERTY_NAME: "Match"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutemetadata.html#cfn-appmesh-gatewayroute-grpcgatewayroutemetadata-match"""

@attr.s
class PropGatewayRouteHttpGatewayRouteAction(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.HttpGatewayRouteAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteaction.html

    Property Document:
    
    - ``rp_Target``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteaction.html#cfn-appmesh-gatewayroute-httpgatewayrouteaction-target
    - ``p_Rewrite``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteaction.html#cfn-appmesh-gatewayroute-httpgatewayrouteaction-rewrite
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.HttpGatewayRouteAction"
    
    rp_Target: typing.Union['PropGatewayRouteGatewayRouteTarget', dict] = attr.ib(
        default=None,
        converter=PropGatewayRouteGatewayRouteTarget.from_dict,
        validator=attr.validators.instance_of(PropGatewayRouteGatewayRouteTarget),
        metadata={AttrMeta.PROPERTY_NAME: "Target"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteaction.html#cfn-appmesh-gatewayroute-httpgatewayrouteaction-target"""
    p_Rewrite: typing.Union['PropGatewayRouteHttpGatewayRouteRewrite', dict] = attr.ib(
        default=None,
        converter=PropGatewayRouteHttpGatewayRouteRewrite.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGatewayRouteHttpGatewayRouteRewrite)),
        metadata={AttrMeta.PROPERTY_NAME: "Rewrite"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteaction.html#cfn-appmesh-gatewayroute-httpgatewayrouteaction-rewrite"""

@attr.s
class PropMeshMeshSpec(Property):
    """
    AWS Object Type = "AWS::AppMesh::Mesh.MeshSpec"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-meshspec.html

    Property Document:
    
    - ``p_EgressFilter``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-meshspec.html#cfn-appmesh-mesh-meshspec-egressfilter
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::Mesh.MeshSpec"
    
    p_EgressFilter: typing.Union['PropMeshEgressFilter', dict] = attr.ib(
        default=None,
        converter=PropMeshEgressFilter.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropMeshEgressFilter)),
        metadata={AttrMeta.PROPERTY_NAME: "EgressFilter"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-meshspec.html#cfn-appmesh-mesh-meshspec-egressfilter"""

@attr.s
class PropVirtualGatewayVirtualGatewayAccessLog(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayAccessLog"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayaccesslog.html

    Property Document:
    
    - ``p_File``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayaccesslog.html#cfn-appmesh-virtualgateway-virtualgatewayaccesslog-file
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayAccessLog"
    
    p_File: typing.Union['PropVirtualGatewayVirtualGatewayFileAccessLog', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewayFileAccessLog.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualGatewayVirtualGatewayFileAccessLog)),
        metadata={AttrMeta.PROPERTY_NAME: "File"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayaccesslog.html#cfn-appmesh-virtualgateway-virtualgatewayaccesslog-file"""

@attr.s
class PropRouteGrpcRoute(Property):
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
    
    rp_Action: typing.Union['PropRouteGrpcRouteAction', dict] = attr.ib(
        default=None,
        converter=PropRouteGrpcRouteAction.from_dict,
        validator=attr.validators.instance_of(PropRouteGrpcRouteAction),
        metadata={AttrMeta.PROPERTY_NAME: "Action"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroute.html#cfn-appmesh-route-grpcroute-action"""
    rp_Match: typing.Union['PropRouteGrpcRouteMatch', dict] = attr.ib(
        default=None,
        converter=PropRouteGrpcRouteMatch.from_dict,
        validator=attr.validators.instance_of(PropRouteGrpcRouteMatch),
        metadata={AttrMeta.PROPERTY_NAME: "Match"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroute.html#cfn-appmesh-route-grpcroute-match"""
    p_RetryPolicy: typing.Union['PropRouteGrpcRetryPolicy', dict] = attr.ib(
        default=None,
        converter=PropRouteGrpcRetryPolicy.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRouteGrpcRetryPolicy)),
        metadata={AttrMeta.PROPERTY_NAME: "RetryPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroute.html#cfn-appmesh-route-grpcroute-retrypolicy"""
    p_Timeout: typing.Union['PropRouteGrpcTimeout', dict] = attr.ib(
        default=None,
        converter=PropRouteGrpcTimeout.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRouteGrpcTimeout)),
        metadata={AttrMeta.PROPERTY_NAME: "Timeout"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroute.html#cfn-appmesh-route-grpcroute-timeout"""

@attr.s
class PropGatewayRouteHttpGatewayRouteMatch(Property):
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
    
    p_Headers: typing.List[typing.Union['PropGatewayRouteHttpGatewayRouteHeader', dict]] = attr.ib(
        default=None,
        converter=PropGatewayRouteHttpGatewayRouteHeader.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropGatewayRouteHttpGatewayRouteHeader), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Headers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-headers"""
    p_Hostname: typing.Union['PropGatewayRouteGatewayRouteHostnameMatch', dict] = attr.ib(
        default=None,
        converter=PropGatewayRouteGatewayRouteHostnameMatch.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGatewayRouteGatewayRouteHostnameMatch)),
        metadata={AttrMeta.PROPERTY_NAME: "Hostname"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-hostname"""
    p_Method: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Method"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-method"""
    p_Path: typing.Union['PropGatewayRouteHttpPathMatch', dict] = attr.ib(
        default=None,
        converter=PropGatewayRouteHttpPathMatch.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGatewayRouteHttpPathMatch)),
        metadata={AttrMeta.PROPERTY_NAME: "Path"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-path"""
    p_Prefix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Prefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-prefix"""
    p_QueryParameters: typing.List[typing.Union['PropGatewayRouteQueryParameter', dict]] = attr.ib(
        default=None,
        converter=PropGatewayRouteQueryParameter.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropGatewayRouteQueryParameter), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "QueryParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html#cfn-appmesh-gatewayroute-httpgatewayroutematch-queryparameters"""

@attr.s
class PropRouteHttpRouteHeader(Property):
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
    p_Match: typing.Union['PropRouteHeaderMatchMethod', dict] = attr.ib(
        default=None,
        converter=PropRouteHeaderMatchMethod.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRouteHeaderMatchMethod)),
        metadata={AttrMeta.PROPERTY_NAME: "Match"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteheader.html#cfn-appmesh-route-httprouteheader-match"""

@attr.s
class PropGatewayRouteHttpGatewayRoute(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.HttpGatewayRoute"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroute.html

    Property Document:
    
    - ``rp_Action``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroute.html#cfn-appmesh-gatewayroute-httpgatewayroute-action
    - ``rp_Match``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroute.html#cfn-appmesh-gatewayroute-httpgatewayroute-match
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.HttpGatewayRoute"
    
    rp_Action: typing.Union['PropGatewayRouteHttpGatewayRouteAction', dict] = attr.ib(
        default=None,
        converter=PropGatewayRouteHttpGatewayRouteAction.from_dict,
        validator=attr.validators.instance_of(PropGatewayRouteHttpGatewayRouteAction),
        metadata={AttrMeta.PROPERTY_NAME: "Action"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroute.html#cfn-appmesh-gatewayroute-httpgatewayroute-action"""
    rp_Match: typing.Union['PropGatewayRouteHttpGatewayRouteMatch', dict] = attr.ib(
        default=None,
        converter=PropGatewayRouteHttpGatewayRouteMatch.from_dict,
        validator=attr.validators.instance_of(PropGatewayRouteHttpGatewayRouteMatch),
        metadata={AttrMeta.PROPERTY_NAME: "Match"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroute.html#cfn-appmesh-gatewayroute-httpgatewayroute-match"""

@attr.s
class PropVirtualNodeListenerTimeout(Property):
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
    
    p_GRPC: typing.Union['PropVirtualNodeGrpcTimeout', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeGrpcTimeout.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeGrpcTimeout)),
        metadata={AttrMeta.PROPERTY_NAME: "GRPC"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertimeout.html#cfn-appmesh-virtualnode-listenertimeout-grpc"""
    p_HTTP: typing.Union['PropVirtualNodeHttpTimeout', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeHttpTimeout.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeHttpTimeout)),
        metadata={AttrMeta.PROPERTY_NAME: "HTTP"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertimeout.html#cfn-appmesh-virtualnode-listenertimeout-http"""
    p_HTTP2: typing.Union['PropVirtualNodeHttpTimeout', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeHttpTimeout.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeHttpTimeout)),
        metadata={AttrMeta.PROPERTY_NAME: "HTTP2"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertimeout.html#cfn-appmesh-virtualnode-listenertimeout-http2"""
    p_TCP: typing.Union['PropVirtualNodeTcpTimeout', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeTcpTimeout.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeTcpTimeout)),
        metadata={AttrMeta.PROPERTY_NAME: "TCP"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertimeout.html#cfn-appmesh-virtualnode-listenertimeout-tcp"""

@attr.s
class PropVirtualGatewayVirtualGatewayTlsValidationContext(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayTlsValidationContext"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext.html

    Property Document:
    
    - ``rp_Trust``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext-trust
    - ``p_SubjectAlternativeNames``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext-subjectalternativenames
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayTlsValidationContext"
    
    rp_Trust: typing.Union['PropVirtualGatewayVirtualGatewayTlsValidationContextTrust', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewayTlsValidationContextTrust.from_dict,
        validator=attr.validators.instance_of(PropVirtualGatewayVirtualGatewayTlsValidationContextTrust),
        metadata={AttrMeta.PROPERTY_NAME: "Trust"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext-trust"""
    p_SubjectAlternativeNames: typing.Union['PropVirtualGatewaySubjectAlternativeNames', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewaySubjectAlternativeNames.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualGatewaySubjectAlternativeNames)),
        metadata={AttrMeta.PROPERTY_NAME: "SubjectAlternativeNames"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext.html#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext-subjectalternativenames"""

@attr.s
class PropGatewayRouteGrpcGatewayRouteAction(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.GrpcGatewayRouteAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouteaction.html

    Property Document:
    
    - ``rp_Target``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouteaction.html#cfn-appmesh-gatewayroute-grpcgatewayrouteaction-target
    - ``p_Rewrite``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouteaction.html#cfn-appmesh-gatewayroute-grpcgatewayrouteaction-rewrite
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.GrpcGatewayRouteAction"
    
    rp_Target: typing.Union['PropGatewayRouteGatewayRouteTarget', dict] = attr.ib(
        default=None,
        converter=PropGatewayRouteGatewayRouteTarget.from_dict,
        validator=attr.validators.instance_of(PropGatewayRouteGatewayRouteTarget),
        metadata={AttrMeta.PROPERTY_NAME: "Target"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouteaction.html#cfn-appmesh-gatewayroute-grpcgatewayrouteaction-target"""
    p_Rewrite: typing.Union['PropGatewayRouteGrpcGatewayRouteRewrite', dict] = attr.ib(
        default=None,
        converter=PropGatewayRouteGrpcGatewayRouteRewrite.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGatewayRouteGrpcGatewayRouteRewrite)),
        metadata={AttrMeta.PROPERTY_NAME: "Rewrite"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouteaction.html#cfn-appmesh-gatewayroute-grpcgatewayrouteaction-rewrite"""

@attr.s
class PropRouteHttpRouteMatch(Property):
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
    
    p_Headers: typing.List[typing.Union['PropRouteHttpRouteHeader', dict]] = attr.ib(
        default=None,
        converter=PropRouteHttpRouteHeader.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropRouteHttpRouteHeader), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Headers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html#cfn-appmesh-route-httproutematch-headers"""
    p_Method: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Method"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html#cfn-appmesh-route-httproutematch-method"""
    p_Path: typing.Union['PropRouteHttpPathMatch', dict] = attr.ib(
        default=None,
        converter=PropRouteHttpPathMatch.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRouteHttpPathMatch)),
        metadata={AttrMeta.PROPERTY_NAME: "Path"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html#cfn-appmesh-route-httproutematch-path"""
    p_Prefix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Prefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html#cfn-appmesh-route-httproutematch-prefix"""
    p_QueryParameters: typing.List[typing.Union['PropRouteQueryParameter', dict]] = attr.ib(
        default=None,
        converter=PropRouteQueryParameter.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropRouteQueryParameter), iterable_validator=attr.validators.instance_of(list))),
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
class PropGatewayRouteGrpcGatewayRouteMatch(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.GrpcGatewayRouteMatch"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutematch.html

    Property Document:
    
    - ``p_Hostname``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutematch.html#cfn-appmesh-gatewayroute-grpcgatewayroutematch-hostname
    - ``p_Metadata``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutematch.html#cfn-appmesh-gatewayroute-grpcgatewayroutematch-metadata
    - ``p_ServiceName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutematch.html#cfn-appmesh-gatewayroute-grpcgatewayroutematch-servicename
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.GrpcGatewayRouteMatch"
    
    p_Hostname: typing.Union['PropGatewayRouteGatewayRouteHostnameMatch', dict] = attr.ib(
        default=None,
        converter=PropGatewayRouteGatewayRouteHostnameMatch.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGatewayRouteGatewayRouteHostnameMatch)),
        metadata={AttrMeta.PROPERTY_NAME: "Hostname"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutematch.html#cfn-appmesh-gatewayroute-grpcgatewayroutematch-hostname"""
    p_Metadata: typing.List[typing.Union['PropGatewayRouteGrpcGatewayRouteMetadata', dict]] = attr.ib(
        default=None,
        converter=PropGatewayRouteGrpcGatewayRouteMetadata.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropGatewayRouteGrpcGatewayRouteMetadata), iterable_validator=attr.validators.instance_of(list))),
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
class PropGatewayRouteGrpcGatewayRoute(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.GrpcGatewayRoute"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroute.html

    Property Document:
    
    - ``rp_Action``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroute.html#cfn-appmesh-gatewayroute-grpcgatewayroute-action
    - ``rp_Match``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroute.html#cfn-appmesh-gatewayroute-grpcgatewayroute-match
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.GrpcGatewayRoute"
    
    rp_Action: typing.Union['PropGatewayRouteGrpcGatewayRouteAction', dict] = attr.ib(
        default=None,
        converter=PropGatewayRouteGrpcGatewayRouteAction.from_dict,
        validator=attr.validators.instance_of(PropGatewayRouteGrpcGatewayRouteAction),
        metadata={AttrMeta.PROPERTY_NAME: "Action"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroute.html#cfn-appmesh-gatewayroute-grpcgatewayroute-action"""
    rp_Match: typing.Union['PropGatewayRouteGrpcGatewayRouteMatch', dict] = attr.ib(
        default=None,
        converter=PropGatewayRouteGrpcGatewayRouteMatch.from_dict,
        validator=attr.validators.instance_of(PropGatewayRouteGrpcGatewayRouteMatch),
        metadata={AttrMeta.PROPERTY_NAME: "Match"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroute.html#cfn-appmesh-gatewayroute-grpcgatewayroute-match"""

@attr.s
class PropVirtualGatewayVirtualGatewayLogging(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayLogging"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylogging.html

    Property Document:
    
    - ``p_AccessLog``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylogging.html#cfn-appmesh-virtualgateway-virtualgatewaylogging-accesslog
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayLogging"
    
    p_AccessLog: typing.Union['PropVirtualGatewayVirtualGatewayAccessLog', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewayAccessLog.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualGatewayVirtualGatewayAccessLog)),
        metadata={AttrMeta.PROPERTY_NAME: "AccessLog"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylogging.html#cfn-appmesh-virtualgateway-virtualgatewaylogging-accesslog"""

@attr.s
class PropVirtualNodeTlsValidationContext(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.TlsValidationContext"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontext.html

    Property Document:
    
    - ``rp_Trust``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontext.html#cfn-appmesh-virtualnode-tlsvalidationcontext-trust
    - ``p_SubjectAlternativeNames``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontext.html#cfn-appmesh-virtualnode-tlsvalidationcontext-subjectalternativenames
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.TlsValidationContext"
    
    rp_Trust: typing.Union['PropVirtualNodeTlsValidationContextTrust', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeTlsValidationContextTrust.from_dict,
        validator=attr.validators.instance_of(PropVirtualNodeTlsValidationContextTrust),
        metadata={AttrMeta.PROPERTY_NAME: "Trust"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontext.html#cfn-appmesh-virtualnode-tlsvalidationcontext-trust"""
    p_SubjectAlternativeNames: typing.Union['PropVirtualNodeSubjectAlternativeNames', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeSubjectAlternativeNames.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeSubjectAlternativeNames)),
        metadata={AttrMeta.PROPERTY_NAME: "SubjectAlternativeNames"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontext.html#cfn-appmesh-virtualnode-tlsvalidationcontext-subjectalternativenames"""

@attr.s
class PropVirtualNodeListener(Property):
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
    
    rp_PortMapping: typing.Union['PropVirtualNodePortMapping', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodePortMapping.from_dict,
        validator=attr.validators.instance_of(PropVirtualNodePortMapping),
        metadata={AttrMeta.PROPERTY_NAME: "PortMapping"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html#cfn-appmesh-virtualnode-listener-portmapping"""
    p_ConnectionPool: typing.Union['PropVirtualNodeVirtualNodeConnectionPool', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeVirtualNodeConnectionPool.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeVirtualNodeConnectionPool)),
        metadata={AttrMeta.PROPERTY_NAME: "ConnectionPool"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html#cfn-appmesh-virtualnode-listener-connectionpool"""
    p_HealthCheck: typing.Union['PropVirtualNodeHealthCheck', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeHealthCheck.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeHealthCheck)),
        metadata={AttrMeta.PROPERTY_NAME: "HealthCheck"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html#cfn-appmesh-virtualnode-listener-healthcheck"""
    p_OutlierDetection: typing.Union['PropVirtualNodeOutlierDetection', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeOutlierDetection.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeOutlierDetection)),
        metadata={AttrMeta.PROPERTY_NAME: "OutlierDetection"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html#cfn-appmesh-virtualnode-listener-outlierdetection"""
    p_TLS: typing.Union['PropVirtualNodeListenerTls', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeListenerTls.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeListenerTls)),
        metadata={AttrMeta.PROPERTY_NAME: "TLS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html#cfn-appmesh-virtualnode-listener-tls"""
    p_Timeout: typing.Union['PropVirtualNodeListenerTimeout', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeListenerTimeout.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeListenerTimeout)),
        metadata={AttrMeta.PROPERTY_NAME: "Timeout"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html#cfn-appmesh-virtualnode-listener-timeout"""

@attr.s
class PropRouteHttpRoute(Property):
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
    
    rp_Action: typing.Union['PropRouteHttpRouteAction', dict] = attr.ib(
        default=None,
        converter=PropRouteHttpRouteAction.from_dict,
        validator=attr.validators.instance_of(PropRouteHttpRouteAction),
        metadata={AttrMeta.PROPERTY_NAME: "Action"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproute.html#cfn-appmesh-route-httproute-action"""
    rp_Match: typing.Union['PropRouteHttpRouteMatch', dict] = attr.ib(
        default=None,
        converter=PropRouteHttpRouteMatch.from_dict,
        validator=attr.validators.instance_of(PropRouteHttpRouteMatch),
        metadata={AttrMeta.PROPERTY_NAME: "Match"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproute.html#cfn-appmesh-route-httproute-match"""
    p_RetryPolicy: typing.Union['PropRouteHttpRetryPolicy', dict] = attr.ib(
        default=None,
        converter=PropRouteHttpRetryPolicy.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRouteHttpRetryPolicy)),
        metadata={AttrMeta.PROPERTY_NAME: "RetryPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproute.html#cfn-appmesh-route-httproute-retrypolicy"""
    p_Timeout: typing.Union['PropRouteHttpTimeout', dict] = attr.ib(
        default=None,
        converter=PropRouteHttpTimeout.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRouteHttpTimeout)),
        metadata={AttrMeta.PROPERTY_NAME: "Timeout"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproute.html#cfn-appmesh-route-httproute-timeout"""

@attr.s
class PropVirtualGatewayVirtualGatewayClientPolicyTls(Property):
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
    
    rp_Validation: typing.Union['PropVirtualGatewayVirtualGatewayTlsValidationContext', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewayTlsValidationContext.from_dict,
        validator=attr.validators.instance_of(PropVirtualGatewayVirtualGatewayTlsValidationContext),
        metadata={AttrMeta.PROPERTY_NAME: "Validation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicytls.html#cfn-appmesh-virtualgateway-virtualgatewayclientpolicytls-validation"""
    p_Certificate: typing.Union['PropVirtualGatewayVirtualGatewayClientTlsCertificate', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewayClientTlsCertificate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualGatewayVirtualGatewayClientTlsCertificate)),
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
class PropVirtualNodeClientPolicyTls(Property):
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
    
    rp_Validation: typing.Union['PropVirtualNodeTlsValidationContext', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeTlsValidationContext.from_dict,
        validator=attr.validators.instance_of(PropVirtualNodeTlsValidationContext),
        metadata={AttrMeta.PROPERTY_NAME: "Validation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicytls.html#cfn-appmesh-virtualnode-clientpolicytls-validation"""
    p_Certificate: typing.Union['PropVirtualNodeClientTlsCertificate', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeClientTlsCertificate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeClientTlsCertificate)),
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
class PropGatewayRouteGatewayRouteSpec(Property):
    """
    AWS Object Type = "AWS::AppMesh::GatewayRoute.GatewayRouteSpec"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutespec.html

    Property Document:
    
    - ``p_GrpcRoute``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutespec.html#cfn-appmesh-gatewayroute-gatewayroutespec-grpcroute
    - ``p_Http2Route``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutespec.html#cfn-appmesh-gatewayroute-gatewayroutespec-http2route
    - ``p_HttpRoute``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutespec.html#cfn-appmesh-gatewayroute-gatewayroutespec-httproute
    - ``p_Priority``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutespec.html#cfn-appmesh-gatewayroute-gatewayroutespec-priority
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::GatewayRoute.GatewayRouteSpec"
    
    p_GrpcRoute: typing.Union['PropGatewayRouteGrpcGatewayRoute', dict] = attr.ib(
        default=None,
        converter=PropGatewayRouteGrpcGatewayRoute.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGatewayRouteGrpcGatewayRoute)),
        metadata={AttrMeta.PROPERTY_NAME: "GrpcRoute"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutespec.html#cfn-appmesh-gatewayroute-gatewayroutespec-grpcroute"""
    p_Http2Route: typing.Union['PropGatewayRouteHttpGatewayRoute', dict] = attr.ib(
        default=None,
        converter=PropGatewayRouteHttpGatewayRoute.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGatewayRouteHttpGatewayRoute)),
        metadata={AttrMeta.PROPERTY_NAME: "Http2Route"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutespec.html#cfn-appmesh-gatewayroute-gatewayroutespec-http2route"""
    p_HttpRoute: typing.Union['PropGatewayRouteHttpGatewayRoute', dict] = attr.ib(
        default=None,
        converter=PropGatewayRouteHttpGatewayRoute.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGatewayRouteHttpGatewayRoute)),
        metadata={AttrMeta.PROPERTY_NAME: "HttpRoute"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutespec.html#cfn-appmesh-gatewayroute-gatewayroutespec-httproute"""
    p_Priority: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Priority"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutespec.html#cfn-appmesh-gatewayroute-gatewayroutespec-priority"""

@attr.s
class PropRouteRouteSpec(Property):
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
    
    p_GrpcRoute: typing.Union['PropRouteGrpcRoute', dict] = attr.ib(
        default=None,
        converter=PropRouteGrpcRoute.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRouteGrpcRoute)),
        metadata={AttrMeta.PROPERTY_NAME: "GrpcRoute"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html#cfn-appmesh-route-routespec-grpcroute"""
    p_Http2Route: typing.Union['PropRouteHttpRoute', dict] = attr.ib(
        default=None,
        converter=PropRouteHttpRoute.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRouteHttpRoute)),
        metadata={AttrMeta.PROPERTY_NAME: "Http2Route"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html#cfn-appmesh-route-routespec-http2route"""
    p_HttpRoute: typing.Union['PropRouteHttpRoute', dict] = attr.ib(
        default=None,
        converter=PropRouteHttpRoute.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRouteHttpRoute)),
        metadata={AttrMeta.PROPERTY_NAME: "HttpRoute"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html#cfn-appmesh-route-routespec-httproute"""
    p_Priority: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Priority"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html#cfn-appmesh-route-routespec-priority"""
    p_TcpRoute: typing.Union['PropRouteTcpRoute', dict] = attr.ib(
        default=None,
        converter=PropRouteTcpRoute.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRouteTcpRoute)),
        metadata={AttrMeta.PROPERTY_NAME: "TcpRoute"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html#cfn-appmesh-route-routespec-tcproute"""

@attr.s
class PropVirtualGatewayVirtualGatewayClientPolicy(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayClientPolicy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicy.html

    Property Document:
    
    - ``p_TLS``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayclientpolicy-tls
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayClientPolicy"
    
    p_TLS: typing.Union['PropVirtualGatewayVirtualGatewayClientPolicyTls', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewayClientPolicyTls.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualGatewayVirtualGatewayClientPolicyTls)),
        metadata={AttrMeta.PROPERTY_NAME: "TLS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicy.html#cfn-appmesh-virtualgateway-virtualgatewayclientpolicy-tls"""

@attr.s
class PropVirtualGatewayVirtualGatewayBackendDefaults(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewayBackendDefaults"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaybackenddefaults.html

    Property Document:
    
    - ``p_ClientPolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaybackenddefaults.html#cfn-appmesh-virtualgateway-virtualgatewaybackenddefaults-clientpolicy
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewayBackendDefaults"
    
    p_ClientPolicy: typing.Union['PropVirtualGatewayVirtualGatewayClientPolicy', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewayClientPolicy.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualGatewayVirtualGatewayClientPolicy)),
        metadata={AttrMeta.PROPERTY_NAME: "ClientPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaybackenddefaults.html#cfn-appmesh-virtualgateway-virtualgatewaybackenddefaults-clientpolicy"""

@attr.s
class PropVirtualNodeClientPolicy(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.ClientPolicy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicy.html

    Property Document:
    
    - ``p_TLS``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicy.html#cfn-appmesh-virtualnode-clientpolicy-tls
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.ClientPolicy"
    
    p_TLS: typing.Union['PropVirtualNodeClientPolicyTls', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeClientPolicyTls.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeClientPolicyTls)),
        metadata={AttrMeta.PROPERTY_NAME: "TLS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicy.html#cfn-appmesh-virtualnode-clientpolicy-tls"""

@attr.s
class PropVirtualGatewayVirtualGatewaySpec(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualGateway.VirtualGatewaySpec"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayspec.html

    Property Document:
    
    - ``rp_Listeners``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayspec.html#cfn-appmesh-virtualgateway-virtualgatewayspec-listeners
    - ``p_BackendDefaults``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayspec.html#cfn-appmesh-virtualgateway-virtualgatewayspec-backenddefaults
    - ``p_Logging``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayspec.html#cfn-appmesh-virtualgateway-virtualgatewayspec-logging
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualGateway.VirtualGatewaySpec"
    
    rp_Listeners: typing.List[typing.Union['PropVirtualGatewayVirtualGatewayListener', dict]] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewayListener.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropVirtualGatewayVirtualGatewayListener), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Listeners"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayspec.html#cfn-appmesh-virtualgateway-virtualgatewayspec-listeners"""
    p_BackendDefaults: typing.Union['PropVirtualGatewayVirtualGatewayBackendDefaults', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewayBackendDefaults.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualGatewayVirtualGatewayBackendDefaults)),
        metadata={AttrMeta.PROPERTY_NAME: "BackendDefaults"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayspec.html#cfn-appmesh-virtualgateway-virtualgatewayspec-backenddefaults"""
    p_Logging: typing.Union['PropVirtualGatewayVirtualGatewayLogging', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewayLogging.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualGatewayVirtualGatewayLogging)),
        metadata={AttrMeta.PROPERTY_NAME: "Logging"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayspec.html#cfn-appmesh-virtualgateway-virtualgatewayspec-logging"""

@attr.s
class PropVirtualNodeBackendDefaults(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.BackendDefaults"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-backenddefaults.html

    Property Document:
    
    - ``p_ClientPolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-backenddefaults.html#cfn-appmesh-virtualnode-backenddefaults-clientpolicy
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.BackendDefaults"
    
    p_ClientPolicy: typing.Union['PropVirtualNodeClientPolicy', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeClientPolicy.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeClientPolicy)),
        metadata={AttrMeta.PROPERTY_NAME: "ClientPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-backenddefaults.html#cfn-appmesh-virtualnode-backenddefaults-clientpolicy"""

@attr.s
class PropVirtualNodeVirtualServiceBackend(Property):
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
    p_ClientPolicy: typing.Union['PropVirtualNodeClientPolicy', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeClientPolicy.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeClientPolicy)),
        metadata={AttrMeta.PROPERTY_NAME: "ClientPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualservicebackend.html#cfn-appmesh-virtualnode-virtualservicebackend-clientpolicy"""

@attr.s
class PropVirtualNodeBackend(Property):
    """
    AWS Object Type = "AWS::AppMesh::VirtualNode.Backend"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-backend.html

    Property Document:
    
    - ``p_VirtualService``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-backend.html#cfn-appmesh-virtualnode-backend-virtualservice
    """
    AWS_OBJECT_TYPE = "AWS::AppMesh::VirtualNode.Backend"
    
    p_VirtualService: typing.Union['PropVirtualNodeVirtualServiceBackend', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeVirtualServiceBackend.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeVirtualServiceBackend)),
        metadata={AttrMeta.PROPERTY_NAME: "VirtualService"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-backend.html#cfn-appmesh-virtualnode-backend-virtualservice"""

@attr.s
class PropVirtualNodeVirtualNodeSpec(Property):
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
    
    p_BackendDefaults: typing.Union['PropVirtualNodeBackendDefaults', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeBackendDefaults.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeBackendDefaults)),
        metadata={AttrMeta.PROPERTY_NAME: "BackendDefaults"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodespec.html#cfn-appmesh-virtualnode-virtualnodespec-backenddefaults"""
    p_Backends: typing.List[typing.Union['PropVirtualNodeBackend', dict]] = attr.ib(
        default=None,
        converter=PropVirtualNodeBackend.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropVirtualNodeBackend), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Backends"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodespec.html#cfn-appmesh-virtualnode-virtualnodespec-backends"""
    p_Listeners: typing.List[typing.Union['PropVirtualNodeListener', dict]] = attr.ib(
        default=None,
        converter=PropVirtualNodeListener.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropVirtualNodeListener), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Listeners"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodespec.html#cfn-appmesh-virtualnode-virtualnodespec-listeners"""
    p_Logging: typing.Union['PropVirtualNodeLogging', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeLogging.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeLogging)),
        metadata={AttrMeta.PROPERTY_NAME: "Logging"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodespec.html#cfn-appmesh-virtualnode-virtualnodespec-logging"""
    p_ServiceDiscovery: typing.Union['PropVirtualNodeServiceDiscovery', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeServiceDiscovery.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVirtualNodeServiceDiscovery)),
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
    rp_Spec: typing.Union['PropRouteRouteSpec', dict] = attr.ib(
        default=None,
        converter=PropRouteRouteSpec.from_dict,
        validator=attr.validators.instance_of(PropRouteRouteSpec),
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
    rp_Spec: typing.Union['PropVirtualNodeVirtualNodeSpec', dict] = attr.ib(
        default=None,
        converter=PropVirtualNodeVirtualNodeSpec.from_dict,
        validator=attr.validators.instance_of(PropVirtualNodeVirtualNodeSpec),
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
    rp_Spec: typing.Union['PropVirtualRouterVirtualRouterSpec', dict] = attr.ib(
        default=None,
        converter=PropVirtualRouterVirtualRouterSpec.from_dict,
        validator=attr.validators.instance_of(PropVirtualRouterVirtualRouterSpec),
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
    p_Spec: typing.Union['PropMeshMeshSpec', dict] = attr.ib(
        default=None,
        converter=PropMeshMeshSpec.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropMeshMeshSpec)),
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
    rp_Spec: typing.Union['PropGatewayRouteGatewayRouteSpec', dict] = attr.ib(
        default=None,
        converter=PropGatewayRouteGatewayRouteSpec.from_dict,
        validator=attr.validators.instance_of(PropGatewayRouteGatewayRouteSpec),
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
    rp_Spec: typing.Union['PropVirtualGatewayVirtualGatewaySpec', dict] = attr.ib(
        default=None,
        converter=PropVirtualGatewayVirtualGatewaySpec.from_dict,
        validator=attr.validators.instance_of(PropVirtualGatewayVirtualGatewaySpec),
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
    rp_Spec: typing.Union['PropVirtualServiceVirtualServiceSpec', dict] = attr.ib(
        default=None,
        converter=PropVirtualServiceVirtualServiceSpec.from_dict,
        validator=attr.validators.instance_of(PropVirtualServiceVirtualServiceSpec),
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
    
