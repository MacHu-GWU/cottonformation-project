# -*- coding: utf-8 -*-
import typing

import cottonformation as ctf
from cottonformation.res import s3

# tpl.to_json_file("tpl.json")
# data = tpl.to_dict()

# import cottonformation.res._imp
resource_class_mapper: typing.Dict[str, typing.Type[ctf.Resource]] = dict()
for resource_class in ctf.Resource.__subclasses__():
    resource_class_mapper[resource_class.AWS_OBJECT_TYPE] = resource_class

property_class_mapper: typing.Dict[str, typing.Type[ctf.Property]] = dict()
for property_class in ctf.Property.__subclasses__():
    property_class_mapper[property_class.AWS_OBJECT_TYPE] = property_class

tpl = ctf.Template()

param_env_name = ctf.Parameter("EnvName", Type=ctf.Parameter.TypeEnum.String)
tpl.add(param_env_name)

data_bucket = s3.Bucket(
    "DataBucket",
    p_BucketName=ctf.Sub.from_params("{}-data-bucket", param_env_name),
    p_PublicAccessBlockConfiguration=s3.PropBucketPublicAccessBlockConfiguration(
        p_BlockPublicPolicy=True
    )
)
tpl.add(data_bucket)

out_data_bucket_dns_name = ctf.Output(
    "DataBucketDnsName",
    Value=data_bucket.rv_DomainName,
)
tpl.add(out_data_bucket_dns_name)

data = tpl.to_dict()

for param_id, param_dct in data[ctf.constant.CloudFomation.Parameters].items():
    param_env_name = ctf.Parameter(id=param_id, **param_dct)
    print(param_env_name)


for resource_id, resource_dct in data[ctf.constant.CloudFomation.Resources].items():
    aws_object_type = resource_dct.pop(ctf.constant.CloudFomation.Type)
    resource_class: typing.Type[ctf.Resource] = resource_class_mapper[aws_object_type]

    cf_to_attr_name_mapper: dict = resource_class.get_cf_name_to_attr_name()

    kwargs = {
        cf_to_attr_name_mapper[k]: v
        for k, v in resource_dct[ctf.constant.CloudFomation.Properties].items()
    }
    print(kwargs)
    kwargs[f"ra_{ctf.constant.ResourceAttribute.METADATA}"] = resource_dct.get(ctf.constant.ResourceAttribute.METADATA, dict())
    kwargs[f"ra_{ctf.constant.ResourceAttribute.CREATION_POLICY}"] = resource_dct.get(ctf.constant.ResourceAttribute.CREATION_POLICY, dict())
    kwargs[f"ra_{ctf.constant.ResourceAttribute.UPDATE_POLICY}"] = resource_dct.get(ctf.constant.ResourceAttribute.UPDATE_POLICY, None)
    kwargs[f"ra_{ctf.constant.ResourceAttribute.UPDATE_REPLACE_POLICY}"] = resource_dct.get(ctf.constant.ResourceAttribute.UPDATE_REPLACE_POLICY, None)
    kwargs[f"ra_{ctf.constant.ResourceAttribute.CONDITION}"] = resource_dct.get(ctf.constant.ResourceAttribute.CONDITION, None)
    kwargs[f"ra_{ctf.constant.ResourceAttribute.DEPENDS_ON}"] = resource_dct.get(ctf.constant.ResourceAttribute.DEPENDS_ON, list())
    resource = resource_class(id=resource_id, **kwargs)

    # print(param_env_name)





