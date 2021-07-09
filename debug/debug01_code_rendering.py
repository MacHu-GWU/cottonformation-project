# -*- coding: utf-8 -*-

"""
The purpose of this file is to help developer to debug the jinja2 template
rendering issue.
"""
from cottonformation.code.spec import (
    CftSpec, ResourceType, PropertyType,
)

cft_spec = CftSpec.new()

# print(cft_spec.find_resource_type("AWS::S3::Bucket").render())
# print(cft_spec.find_resource_type("AWS::IAM::Role").render())

# print(cft_spec.find_property_type("AWS::S3::Bucket.NotificationConfiguration").render())
# print(cft_spec.find_property_type("AWS::Elasticsearch::Domain.ElasticsearchClusterConfig").render())
