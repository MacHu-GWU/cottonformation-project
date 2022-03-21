# -*- coding: utf-8 -*-

"""
This module implements the AWS Object used in CloudFormation template.
"""

import typing
from typing import (
    Any,
    Optional,
    Union,
    List,
    Tuple,
    Dict,
)
from collections import OrderedDict
import attr
from attr import validators as vs

from . import constant


class TypeHint:
    """
    Constant value hosting class for typehint
    """
    intrinsic_str = Union[str, dict, 'IntrinsicFunction']
    intrinsic_int = Union[int, dict, 'IntrinsicFunction']
    addable_obj = Union[
        'Parameter', 'Resource', 'Output',
        'Rule', 'Mapping', 'Condition', 'ResourceGroup',
    ]
    dependency_obj = Union[
        str, 'Resource', 'Parameter', 'Mapping', 'Condition'
    ]


@attr.s
class _IntrinsicFunctionType:
    """
    A base class for type check for IntrinsicFunction object.
    """


@attr.s
class _Addable:
    """
    A base class for type check for item to be added to a Template.

    Includes 'Parameter', 'Resource', 'Output', 'Rule', 'Mapping', 'Condition', 'Pack'.
    """
    @property
    def gid(self) -> str:
        raise NotImplementedError

    @property
    def _ez_repr(self) -> str:
        raise NotImplementedError


@attr.s
class _ListMember(_Addable):
    """
    A base class for type check for item to be added to a Template, stored
    in a list.
    """


@attr.s
class _DictMember(_Addable):
    """
    A base class for type check for item to be added to a Template, stored
    in a dict. Includes:

    - :class:`Parameter`
    - :class:`Resource`
    - :class:`Output`
    - :class:`Rule`
    - :class:`Mapping`
    - :class:`Condition`
    """
    @property
    def gid(self) -> str:
        """
        Global Logic Id for
        :return:
        """
        return f"{self.CLASS_TYPE}--{self.id}"


    @property
    def _ez_repr(self) -> str:
        return "{}({})".format(
            _class_type_to_attr_mapper[self.CLASS_TYPE][:-1],
            self.id,
        )


@attr.s
class _Dependency:
    """
    A base class for type check for item that can be a dependency of another.
    (another object depends on this one)

    **中文文档**

    Dependency 是指那些可能被别人需要的人.
    Dependent 是指需要别人的人.
    """


class TypeCheck:
    intrinsic_str_type = (str, dict, _IntrinsicFunctionType)
    intrinsic_int_type = (int, dict, _IntrinsicFunctionType)


@attr.s
class AwsObject:
    def serialize(self, **kwargs) -> typing.Any:
        raise NotImplementedError

    def deserialize(self, **kwargs) -> typing.Any:
        raise NotImplementedError


@attr.s
class IntrinsicFunction(AwsObject, _IntrinsicFunctionType):
    CLASS_TYPE = "IntrinsicFunction"

    def special_int_fun(self):
        pass


@attr.s
class _PropertyOrResource(AwsObject):
    _attr_name_to_cf_name = None  # type: dict
    _cf_name_to_attr_name = None  # type: dict

    @classmethod
    def get_attr_name_to_cf_name(cls):
        if cls._attr_name_to_cf_name is None:
            cls._attr_name_to_cf_name = {
                field.name: field.metadata[constant.AttrMeta.PROPERTY_NAME]
                for field in attr.fields(cls)
            }
        return cls._attr_name_to_cf_name

    @classmethod
    def get_cf_name_to_attr_name(cls):
        if cls._cf_name_to_attr_name is None:
            cls._cf_name_to_attr_name = {
                field.metadata[constant.AttrMeta.PROPERTY_NAME]: field.name
                for field in attr.fields(cls)
            }
        return cls._cf_name_to_attr_name

    @classmethod
    def from_dict(
        cls,
        dct_or_obj,
    ):
        """
        Construct an instance from dictionary data.

        :type dct_or_obj: Union[dict, None]
        :rtype: cls
        """
        if isinstance(dct_or_obj, cls):
            return dct_or_obj
        elif dct_or_obj is None:
            return None
        elif isinstance(dct_or_obj, dict):
            return cls(**dct_or_obj)
        else:  # pragma: no cover
            return TypeError

    @classmethod
    def from_list(
        cls,
        list_of_dct_or_obj: Optional[
            List[
                Union['AwsObject', dict]
            ]
        ],
    ):
        """
        Construct list of instance from list of dictionary data.
        :type list_of_dct_or_obj: Union[List[cls], List[dict], None]
        :rtype: List[cls]
        """
        if isinstance(list_of_dct_or_obj, list):
            return [cls.from_dict(item) for item in list_of_dct_or_obj]
        elif list_of_dct_or_obj is None:
            return None
        else:  # pragma: no cover
            return TypeError


@attr.s
class Property(_PropertyOrResource):
    AWS_OBJECT_TYPE = None

    def serialize(self):
        class_data = get_key_value_dict(self)
        attr_name_to_cf_name_mapper = self.get_attr_name_to_cf_name()

        property_dct = dict()
        for k, v in class_data.items():
            if k.startswith("rp_") or k.startswith("p_"):
                if v is not None:
                    property_dct[attr_name_to_cf_name_mapper[k]] = v
        property_dct = serialize(property_dct)
        return property_dct


def ensure_list(obj):
    if not isinstance(obj, list):
        return [obj,]
    else:
        return obj


@attr.s
class Resource(_PropertyOrResource, _DictMember, _Dependency):
    AWS_OBJECT_TYPE = None
    CLASS_TYPE = "5-Resource"

    id: str = attr.ib(
        validator=vs.optional(vs.instance_of(str)),
        metadata={constant.AttrMeta.PROPERTY_NAME: "Id"},
    )

    ra_CreationPolicy: str = attr.ib(
        factory=dict,
        validator=None,
        metadata={constant.AttrMeta.PROPERTY_NAME: constant.ResourceAttribute.CREATION_POLICY},
    )
    ra_DeletionPolicy: str = attr.ib(
        default=None,
        validator=None,
        metadata={constant.AttrMeta.PROPERTY_NAME: constant.ResourceAttribute.DELETION_POLICY},
    )
    ra_DependsOn: typing.Union[TypeHint.dependency_obj, typing.List[TypeHint.dependency_obj]] = attr.ib(
        factory=list,
        validator=vs.instance_of((str, _Dependency, list)),
        metadata={constant.AttrMeta.PROPERTY_NAME: constant.ResourceAttribute.DEPENDS_ON},
    )
    ra_Metadata: dict = attr.ib(
        factory=dict,
        metadata={constant.AttrMeta.PROPERTY_NAME: constant.ResourceAttribute.METADATA},
    )
    ra_UpdatePolicy: str = attr.ib(
        default=None,
        validator=None,
        metadata={constant.AttrMeta.PROPERTY_NAME: constant.ResourceAttribute.UPDATE_POLICY},
    )
    ra_UpdateReplacePolicy: str = attr.ib(
        default=None,
        validator=None,
        metadata={constant.AttrMeta.PROPERTY_NAME: constant.ResourceAttribute.UPDATE_REPLACE_POLICY},
    )
    ra_Condition: str = attr.ib(
        default=None,
        validator=None,
        metadata={constant.AttrMeta.PROPERTY_NAME: constant.ResourceAttribute.CONDITION},
    )

    def __attrs_post_init__(self):
        self.ra_DependsOn = ensure_list(self.ra_DependsOn)

        # mt = constant.MetaData
        # if len(self.ra_DependsOn):
        #     self.ra_Metadata.setdefault(mt.CTF, dict())
        #     self.ra_Metadata[mt.CTF].setdefault(mt.DependsOn, dict())
        #     for k in [
        #         mt.Parameters,
        #         mt.Resources,
        #         mt.Mappings,
        #         mt.Conditions,
        #     ]:
        #         self.ra_Metadata[mt.CTF][mt.DependsOn].setdefault(k, dict())
        #
        # for obj in self.ra_DependsOn:
        #     if isinstance(obj, Parameter):
        #         self.ra_Metadata[mt.CTF][mt.DependsOn][mt.Parameters][get_id(obj)] = True
        #     elif isinstance(obj, Mapping):
        #         self.ra_Metadata[mt.CTF][mt.DependsOn][mt.Mappings][get_id(obj)] = True
        #     elif isinstance(obj, Condition):
        #         self.ra_Metadata[mt.CTF][mt.DependsOn][mt.Conditions][get_id(obj)] = True
        #     elif isinstance(obj, (str, Resource)):
        #         self.ra_Metadata[mt.CTF][mt.DependsOn][mt.Resources][get_id(obj)] = True

    @property
    def DependsOn(self) -> typing.List[TypeHint.dependency_obj]:
        return self.ra_DependsOn

    def ref(self) -> 'Ref':
        return Ref(self)

    @property
    def tags_dict(self) -> OrderedDict:
        if self.p_Tags is None:
            return OrderedDict()
        dct = OrderedDict([
            (t.p_Key, t.p_Value)
            for t in self.p_Tags
        ])
        if len(self.p_Tags) != len(dct):
            raise ValueError(f"duplicate key found in {self._ez_repr}")
        return dct

    @classmethod
    def support_tags(cls) -> bool:
        """
        Return a boolean value to indicate that whether this AWS Resource type
        support tagging.
        """
        return "p_Tags" in attr.fields_dict(cls)

    def update_tags(
        self,
        overwrite: bool = False,
        **kwargs,
    ):
        """
        Update tags. overwrite flag can be used to decide whether you want to
        the tag value if tag key already exists.
        """
        if self.p_Tags is None:
            existing_tags = OrderedDict()
        else:
            existing_tags = OrderedDict([
                (tag.p_Key, tag)
                for tag in self.p_Tags
            ])

        for k, v in kwargs.items():
            if k not in existing_tags:
                existing_tags[k] = Tag(p_Key=k, p_Value=v)
            elif overwrite:
                existing_tags[k] = Tag(p_Key=k, p_Value=v)
            else:
                pass

        if len(existing_tags):
            self.p_Tags = list(existing_tags.values())


    def serialize(self):
        class_data = get_key_value_dict(self)
        attr_name_to_cf_name_mapper = self.get_attr_name_to_cf_name()

        resource_dct = dict()
        resource_dct[constant.CloudFomation.Type] = self.AWS_OBJECT_TYPE
        properties_dct = dict()
        for k, v in class_data.items():
            if k.startswith("rp_") or k.startswith("p_"):
                if v is not None:
                    properties_dct[attr_name_to_cf_name_mapper[k]] = v
            elif k.startswith("ra_"):
                if v is not None:
                    resource_dct[attr_name_to_cf_name_mapper[k]] = v
        resource_dct[constant.CloudFomation.Properties] = properties_dct

        # only keep resource type depends on. other depends on object like
        # parameter, mapping, condition are only for cottonformation internal use
        depends_on = list()
        for obj in resource_dct[constant.ResourceAttribute.DEPENDS_ON]:
            if isinstance(obj, (str, Resource)):
                depends_on.append(get_id(obj))
        resource_dct[constant.ResourceAttribute.DEPENDS_ON] = depends_on

        resource_dct = remove_id_and_empty(resource_dct)
        if constant.CloudFomation.Properties not in resource_dct:
            resource_dct[constant.CloudFomation.Properties] = dict()

        resource_dct = serialize(resource_dct)
        return resource_dct

    @classmethod
    def deserialize(cls, data: dict): # pragma: no cover
        """
        TODO
        """
        class_data = dict()
        cf_name_to_attr_name_mapper = cls.get_cf_name_to_attr_name()
        for k, v in data.items():
            class_data = [
                cf_name_to_attr_name_mapper
            ]

@attr.s
class Parameter(AwsObject, _DictMember, _Dependency):
    """
    Reference:


    - Parameters: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html
    - AWS-specific parameter types: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-specific-parameter-types
    - SSM parameter types: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#parameters-section-structure-grouping
    """
    CLASS_TYPE = "1-Parameter"

    id: str = attr.ib(validator=vs.instance_of(str))
    Type: str = attr.ib(validator=vs.instance_of(str))
    Default: str = attr.ib(
        default=None,
    )
    NoEcho: bool = attr.ib(
        default=None,
        validator=vs.optional(vs.instance_of(bool))
    )
    AllowedValues: typing.List[typing.Any] = attr.ib(
        default=None,
        validator=vs.optional(vs.instance_of(list))
    )
    AllowedPattern: str = attr.ib(
        default=None,
        validator=vs.optional(vs.instance_of(str))
    )
    MaxLength: int = attr.ib(
        default=None,
        validator=vs.optional(vs.instance_of(int))
    )
    MinLength: int = attr.ib(
        default=None,
        validator=vs.optional(vs.instance_of(int))
    )
    MaxValue: str = attr.ib(
        default=None,
        validator=vs.optional(vs.and_(vs.instance_of(int), vs.instance_of(float)))
    )
    MinValue: str = attr.ib(
        default=None,
        validator=vs.optional(vs.and_(vs.instance_of(int), vs.instance_of(float)))
    )
    Description: str = attr.ib(
        default=None,
        validator=vs.optional(vs.instance_of(str))
    )
    ConstraintDescription: str = attr.ib(
        default=None,
        validator=vs.optional(vs.instance_of(str))
    )
    DependsOn: typing.Union[TypeHint.dependency_obj, typing.List[TypeHint.dependency_obj]] = attr.ib(
        factory=list,
        validator=vs.optional(vs.instance_of((str, _Dependency, list))),
        converter=ensure_list,
    )

    _value: typing.Any = attr.ib(
        default=None,
    )
    """
    Allow user to bind the value to use for deploy with the parameter.
    """

    class TypeEnum:
        String = "String"
        Number = "Number"
        ListNumber = "List<Number>"
        CommaDelimitedList = "CommaDelimitedList"
        AWS_EC2_AvailabilityZone_Name = "AWS::EC2::AvailabilityZone::Name"
        AWS_EC2_Image_Id = "AWS::EC2::Image::Id"
        AWS_EC2_Instance_Id = "AWS::EC2::Instance::Id"
        AWS_EC2_KeyPair_KeyName = "AWS::EC2::KeyPair::KeyName"
        AWS_EC2_SecurityGroup_GroupName = "AWS::EC2::SecurityGroup::GroupName"
        AWS_EC2_SecurityGroup_Id = "AWS::EC2::SecurityGroup::Id"
        AWS_EC2_Subnet_Id = "AWS::EC2::Subnet::Id"
        AWS_EC2_Volume_Id = "AWS::EC2::Volume::Id"
        AWS_EC2_VPC_Id = "AWS::EC2::VPC::Id"
        AWS_Route53_HostedZone_Id = "AWS::Route53::HostedZone::Id"
        List_AWS_EC2_AvailabilityZone_Name = "List<AWS::EC2::AvailabilityZone::Name>"
        List_AWS_EC2_Image_Id = "List<AWS::EC2::Image::Id>"
        List_AWS_EC2_Instance_Id = "List<AWS::EC2::Instance::Id>"
        List_AWS_EC2_SecurityGroup_GroupName = "List<AWS::EC2::SecurityGroup::GroupName>"
        List_AWS_EC2_SecurityGroup_Id = "List<AWS::EC2::SecurityGroup::Id>"
        List_AWS_EC2_Subnet_Id = "List<AWS::EC2::Subnet::Id>"
        List_AWS_EC2_Volume_Id = "List<AWS::EC2::Volume::Id>"
        List_AWS_EC2_VPC_Id = "List<AWS::EC2::VPC::Id>"
        List_AWS_Route53_HostedZone_Id = "List<AWS::Route53::HostedZone::Id>"

    constant.Collections.PARAMETER_TYPE_ENUM_SET = constant._collect_enum(TypeEnum)

    @Type.validator
    def check_Type(self, attribute, value):
        if value not in constant.Collections.PARAMETER_TYPE_ENUM_SET:
            if not value.startswith("AWS::SSM::Parameter::"):
                raise ValueError(f"{value} is not a Valid type for Parameter.Type")

    def ref(self) -> 'Ref':
        return Ref(self)

    def serialize(self, **kwargs) -> typing.Any:
        dct = get_key_value_dict(self)
        dct.pop("_value")
        dct = remove_id_and_empty(dct)
        dct = serialize(dct)
        return dct

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

@attr.s
class Export(AwsObject):
    Name: TypeHint.intrinsic_str = attr.ib(
        validator=vs.instance_of((str, dict, IntrinsicFunction))
    )

    def serialize(self, **kwargs):
        return {"Name": serialize(self.Name)}


@attr.s
class Output(AwsObject, _DictMember):
    CLASS_TYPE = "6-Output"

    id: str = attr.ib(
        validator=vs.instance_of(str)
    )
    Value: typing.Any = attr.ib()
    Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=vs.optional(vs.instance_of((str, dict, IntrinsicFunction)))
    )
    Export: Export = attr.ib(
        default=None,
        validator=vs.optional(vs.instance_of(Export))
    )
    DependsOn: typing.Union[TypeHint.dependency_obj, typing.List[TypeHint.dependency_obj]] = attr.ib(
        factory=list,
        validator=vs.optional(vs.instance_of((str, _Dependency, list))),
        converter=ensure_list,
    )

    def serialize(self, **kwargs) -> typing.Any:
        # you cannot use attr.asdict(self) here, because it will call
        # asdict AWSObject value too. actually we want to call the serialize
        # method instead of asdict here.
        dct = get_key_value_dict(self)
        dct.pop("DependsOn")
        dct = remove_id_and_empty(dct)
        dct = serialize(dct)
        return dct


@attr.s(frozen=True)
class Tag(Property):
    p_Key: TypeHint.intrinsic_str = attr.ib(
        validator=vs.optional(vs.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={constant.AttrMeta.PROPERTY_NAME: "Key"},
    )
    p_Value: TypeHint.intrinsic_str = attr.ib(
        validator=vs.optional(vs.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={constant.AttrMeta.PROPERTY_NAME: "Value"},
    )

    _tag_naming_limits_doc_url = "https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions"

    def __attrs_post_init__(self):
        if isinstance(self.p_Key, str) and len(self.p_Key) > 128:
            raise ValueError(f"invalid tag key, see aws doc about the limits {self._tag_naming_limits_doc_url}")
        if isinstance(self.p_Value, str) and len(self.p_Value) > 256:
            raise ValueError(f"invalid tag value, see aws doc about the limits {self._tag_naming_limits_doc_url}")

    def serialize(self, **kwargs) -> typing.Any:
        return {"Key": serialize(self.p_Key), "Value": serialize(self.p_Value)}

    @classmethod
    def make_many(cls, dict_data=None, **kwargs) -> typing.List['Tag']:
        if dict_data is None:
            dct = kwargs
        else:
            dct = dict_data
        dct.update(kwargs)
        return [
            cls(p_Key=k, p_Value=v)
            for k, v in dct.items()
        ]


@attr.s
class Ref(IntrinsicFunction):
    """
    Reference:

    - Ref: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html
    """
    param_or_res: typing.Union[str, Parameter, Resource] = attr.ib(
        validator=vs.instance_of((str, Parameter, Resource))
    )

    def serialize(self, **kwargs) -> dict:
        return {constant.IntrinsicFunction.REF: get_id(self.param_or_res)}


@attr.s
class Base64(IntrinsicFunction):
    value: TypeHint.intrinsic_str = attr.ib(
        validator=vs.instance_of(TypeCheck.intrinsic_str_type)
    )

    def serialize(self, **kwargs) -> dict:
        return {constant.IntrinsicFunction.BASE64: serialize(self.value)}


@attr.s
class Cidr(IntrinsicFunction):
    """
    Reference:

    - Fn::Cidr: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-cidr.html
    """
    ip_block: TypeHint.intrinsic_str = attr.ib(
        validator=vs.instance_of(TypeCheck.intrinsic_str_type)
    )
    count: TypeHint.intrinsic_int = attr.ib(
        validator=vs.instance_of(TypeCheck.intrinsic_int_type)
    )
    cidr_bits: TypeHint.intrinsic_int = attr.ib(
        validator=vs.instance_of(TypeCheck.intrinsic_int_type)
    )

    def serialize(self, **kwargs) -> dict:
        return {
            constant.IntrinsicFunction.CIDR: [
                serialize(self.ip_block),
                serialize(self.count),
                serialize(self.cidr_bits),
            ]
        }


@attr.s
class FindInMap(IntrinsicFunction):
    """
    Reference:

    - Fn::FindInMap: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-findinmap.html
    """
    map_name: TypeHint.intrinsic_str = attr.ib(
        validator=vs.instance_of(TypeCheck.intrinsic_str_type)
    )
    top_level_key: TypeHint.intrinsic_str = attr.ib(
        validator=vs.instance_of(TypeCheck.intrinsic_str_type)
    )
    second_level_key: TypeHint.intrinsic_str = attr.ib(
        validator=vs.instance_of(TypeCheck.intrinsic_str_type)
    )

    def serialize(self, **kwargs) -> dict:
        return {
            constant.IntrinsicFunction.FIND_IN_MAP: [
                serialize(self.map_name),
                serialize(self.top_level_key),
                serialize(self.second_level_key),
            ]
        }


@attr.s
class GetAtt(IntrinsicFunction):
    """
    Reference:

    - Fn::GetAtt: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html
    """
    resource: typing.Union[str, Resource] = attr.field(validator=vs.instance_of((str, Resource)))
    attr_name: str = attr.field(validator=vs.instance_of(str))

    def serialize(self, **kwargs) -> dict:
        return {
            constant.IntrinsicFunction.GET_ATT: [
                get_id(self.resource),
                self.attr_name,
            ]
        }


@attr.s
class GetAZs(IntrinsicFunction):
    """
    Reference:

    - Fn::GetAZs: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getavailabilityzones.html
    - Region and Az information: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
    """
    region: TypeHint.intrinsic_str = attr.ib(
        default="",
        validator=vs.optional(vs.instance_of(TypeCheck.intrinsic_str_type)),
    )

    @classmethod
    def n_th(
        cls,
        ind: int,
        region: str="",
    ):
        if ind <= 0:
            raise ValueError
        return Select(ind-1, cls(region=region))

    def serialize(self, **kwargs) -> dict:
        return {constant.IntrinsicFunction.GET_AZS: serialize(self.region)}


@attr.s
class ImportValue(IntrinsicFunction):
    """
    Reference:

    - Fn::ImportValue: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html
    """
    name: TypeHint.intrinsic_str = attr.ib(
        validator=vs.instance_of(TypeCheck.intrinsic_str_type)
    )

    def serialize(self, **kwargs) -> dict:
        return {constant.IntrinsicFunction.IMPORT_VALUE: serialize(self.name)}


@attr.s
class Join(IntrinsicFunction):
    """
    Reference:

    - Fn::Join: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-join.html
    """
    delimiter: Union[
        str,
        dict,
        IntrinsicFunction,
        Parameter,
    ] = attr.ib(
        validator=vs.instance_of((
            str,
            dict,
            IntrinsicFunction,
            Parameter,
        ))
    )
    list_of_values: List[Union[
        str,
        dict,
        IntrinsicFunction,
        Parameter,
        Resource,
    ]] = attr.ib(
        validator=vs.deep_iterable(
            member_validator=vs.instance_of((
                str,
                dict,
                IntrinsicFunction,
                Parameter,
                Resource,
            )),
            iterable_validator=vs.instance_of(list),
        )
    )

    def serialize(self, **kwargs) -> dict:
        if isinstance(self.delimiter, (Parameter, Resource)):
            delimiter = self.delimiter.ref()
        else:
            delimiter = self.delimiter

        list_of_values = list()
        for v in self.list_of_values:
            if isinstance(v, (Parameter, Resource)):
                list_of_values.append(v.ref())
            else:
                list_of_values.append(v)

        return {
            constant.IntrinsicFunction.JOIN: [
                serialize(delimiter),
                serialize(list_of_values)
            ]
        }


@attr.s
class Sub(IntrinsicFunction):
    """
    Reference:

    - Fn::Sub: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-sub.html
    """
    string: str = attr.ib(validator=vs.instance_of(str))
    data: dict = attr.ib(validator=vs.instance_of(dict))

    def __attrs_post_init__(self):
        for k in self.data:
            if ("${%s}" % k) not in self.string:
                raise ValueError

    @classmethod
    def from_params(
        cls,
        f_string,
        *params: Parameter,
    ):
        """
        A helper factory method to construct a Sub syntax from the popular
        positioning formatted string literals and multiple :class:`Parameter`.

        Sample usage::

            >>> p_project_name = Parameter("ProjName", Type=Parameter.TypeEnum.String)
            >>> p_stage = Parameter("Stage", Type=Parameter.TypeEnum.String)
            >>> sub = Sub.from_params("{}-{}-main-ec2-instance", p_project_name, p_stage)
            >>> sub.serialize() # the sub object is equavilent to
            {
                "Fn::Sub": [
                    "${ProjName}-${Stage}",
                    {
                        "ProjName": {"Ref": "ProjName"},
                        "Stage": {"Ref": "Stage"}
                    }
                ]
            }
        """
        string = f_string
        for p in params:
            string = string.replace("{}", "${" + p.id + "}", 1)
        return cls(string, {p.id: p.ref() for p in params})

    def serialize(self, **kwargs) -> dict:
        data = dict()
        v: typing.Union[Parameter, Resource]
        for k, v in self.data.items():
            if isinstance(v, (Parameter, Resource)):
                data[k] = v.ref()
            else:
                data[k] = v

        return {
            constant.IntrinsicFunction.SUB: [
                self.string,
                serialize(data),
            ]
        }


@attr.s
class Select(IntrinsicFunction):
    """
    Reference:

    - Fn::Select: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-select.html
    """
    index: typing.Union[int, str] = attr.ib(
        validator=vs.instance_of((int, str)),
        converter=int,
    )
    list_of_objects: typing.Union[list, IntrinsicFunction] = attr.ib(
        validator=vs.instance_of((list, IntrinsicFunction)),
    )

    def serialize(self, **kwargs) -> dict:
        return {
            constant.IntrinsicFunction.SELECT: [
                self.index,
                serialize(self.list_of_objects)
            ]
        }


@attr.s
class Split(IntrinsicFunction):
    """
    Reference:

    - Fn::Split: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-split.html
    """
    delimiter: TypeHint.intrinsic_str = attr.ib(
        validator=vs.instance_of(TypeCheck.intrinsic_str_type)
    )
    source_string: TypeHint.intrinsic_str = attr.ib(
        validator=vs.instance_of(TypeCheck.intrinsic_str_type)
    )

    def serialize(self, **kwargs) -> dict:
        return {
            constant.IntrinsicFunction.SELECT: [
                serialize(self.delimiter),
                serialize(self.source_string)
            ]
        }


@attr.s
class Mapping(AwsObject, _DictMember, _Dependency):
    CLASS_TYPE = "2-Mapping"

    id: str = attr.ib(
        validator=vs.instance_of(str)
    )
    DependsOn: typing.Union[TypeHint.dependency_obj, typing.List[TypeHint.dependency_obj]] = attr.ib(
        factory=list,
        validator=vs.optional(vs.instance_of((str, _Dependency, list))),
        converter=ensure_list,
    )


@attr.s
class Condition(AwsObject, _DictMember, _Dependency):
    CLASS_TYPE = "3-Condition"

    id: str = attr.ib(
        validator=vs.instance_of(str)
    )
    DependsOn: typing.Union[TypeHint.dependency_obj, typing.List[TypeHint.dependency_obj]] = attr.ib(
        factory=list,
        validator=vs.optional(vs.instance_of((str, _Dependency, list))),
        converter=ensure_list,
    )


@attr.s
class Rule(AwsObject, _DictMember):
    CLASS_TYPE = "4-Rule"

    id: str = attr.ib(
        validator=vs.instance_of(str)
    )
    DependsOn: typing.Union[TypeHint.dependency_obj, typing.List[TypeHint.dependency_obj]] = attr.ib(
        factory=list,
        validator=vs.optional(vs.instance_of((str, _Dependency, list))),
    )


@attr.s
class Transform(AwsObject, _ListMember):
    CLASS_TYPE = "7-Transform"


@attr.s
class ResourceGroup(AwsObject, _DictMember, _Dependency):
    CLASS_TYPE = "99-Resource-Group"

    id: str = attr.ib(
        default="__never_exists__",
        validator=vs.instance_of(str)
    )
    DependsOn: typing.Union[TypeHint.dependency_obj, typing.List[TypeHint.dependency_obj]] = attr.ib(
        factory=list,
        validator=vs.optional(vs.instance_of((str, _Dependency, list))),
        converter=ensure_list,
    )

    def add(self, obj: TypeHint.addable_obj):
        self.DependsOn.append(obj)

    def add_many(self, objects: typing.List[TypeHint.addable_obj]):
        self.DependsOn.extend(objects)


def get_key_value_dict(obj: attr.s) -> dict:
    """
    In serialization (convert object to dict data), since we are trying to
    unfold data in format of cloudformation, not the native python dict view.
    I don't want attr.asdict automatically unfold the nested object
    in a way I don't want.
    """
    dct = dict()
    for field in attr.fields(obj.__class__):
        dct[field.name] = getattr(obj, field.name)
    return dct


def remove_id_and_empty(dct: dict) -> dict:
    """
    In serialization (convert object to dict data), a common case is we ignore
    the id field and those key-valur pair having None value or empty collection
    object. This helper function does that.
    """
    new_dct = dict()
    for k, v in dct.items():
        if k == "id":
            continue
        if isinstance(v, (list, dict)) and len(v) == 0:
            continue
        if v is None:
            continue
        new_dct[k] = v
    return new_dct


def get_id(
    obj_or_id: typing.Union[
        str,
        Parameter,
        Resource,
        Output,
        Rule,
        Mapping,
        Condition,
    ],
) -> str:
    """
    Get the logic id string.
    """
    if isinstance(obj_or_id, str):
        return obj_or_id
    else:
        return obj_or_id.id


def serialize(obj: typing.Union['AwsObject', dict, typing.Any]) -> typing.Any:
    """
    An universal api that convert anything to json serializable python dictionary.
    """
    if isinstance(obj, AwsObject):
        return obj.serialize()
    elif isinstance(obj, (list, tuple)):
        return [
            serialize(nested_obj)
            for nested_obj in obj
        ]
    elif isinstance(obj, dict):
        return {
            key: serialize(nested_obj)
            for key, nested_obj in obj.items()
        }
    else:
        return obj


AWS_ACCOUNT_ID = Ref(constant.PseudoParameter.AWS_ACCOUNT_ID)
AWS_NOTIFICATION_ARNS = Ref(constant.PseudoParameter.AWS_NOTIFICATION_ARNS)
AWS_NO_VALUE = Ref(constant.PseudoParameter.AWS_NO_VALUE)
AWS_PARTITION = Ref(constant.PseudoParameter.AWS_PARTITION)
AWS_REGION = Ref(constant.PseudoParameter.AWS_REGION)
AWS_STACK_ID = Ref(constant.PseudoParameter.AWS_STACK_ID)
AWS_STACK_NAME = Ref(constant.PseudoParameter.AWS_STACK_NAME)
AWS_URL_SURFIX = Ref(constant.PseudoParameter.AWS_URL_SURFIX)


_class_type_to_attr_mapper = {
    Parameter.CLASS_TYPE: "Parameters",
    Resource.CLASS_TYPE: "Resources",
    Output.CLASS_TYPE: "Outputs",
    Rule.CLASS_TYPE: "Rules",
    Mapping.CLASS_TYPE: "Mappings",
    Condition.CLASS_TYPE: "Conditions",
    ResourceGroup.CLASS_TYPE: "Groups",
}
