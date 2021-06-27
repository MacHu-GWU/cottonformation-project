# -*- coding: utf-8 -*-

import json
import typing

import attr
from attr import validators as vs

from . import constant


class TypeHint:
    """
    Constant value hosting class for typehint
    """
    intrinsic_str = typing.Union[str, dict, 'IntrinsicFunction']
    intrinsic_int = typing.Union[int, dict, 'IntrinsicFunction']
    addable_obj = typing.Union[
        'Parameter', 'Resource', 'Output',
        'Rule', 'Mapping', 'Condition',
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
    """


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
    in a dict.
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
    def from_dict(cls, dct_or_obj):
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
    def from_list(cls, list_of_dct_or_obj):
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


@attr.s
class Resource(_PropertyOrResource, _DictMember):
    AWS_OBJECT_TYPE = None

    id: str = attr.ib(
        validator=vs.optional(vs.instance_of(str)),
        metadata={constant.AttrMeta.PROPERTY_NAME: "Id"},
    )

    ra_CreationPolicy: str = attr.ib(
        default=None,
        validator=None,
        metadata={constant.AttrMeta.PROPERTY_NAME: constant.ResourceAttribute.CREATION_POLICY},
    )
    ra_DeletionPolicy: str = attr.ib(
        default=None,
        validator=None,
        metadata={constant.AttrMeta.PROPERTY_NAME: constant.ResourceAttribute.DELETION_POLICY},
    )
    ra_DependsOn: typing.Union[str, 'Resource', typing.List[typing.Union[str, 'Resource']]] = attr.ib(
        default=None,
        metadata={constant.AttrMeta.PROPERTY_NAME: constant.ResourceAttribute.DEPENDS_ON},
    )
    ra_Metadata: str = attr.ib(
        default=None,
        validator=None,
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

    @ra_DependsOn.validator
    def check_depends_on(self, attribute, value):
        if value is None:
            pass
        elif isinstance(value, (str, Resource)):
            pass
        elif isinstance(value, list):
            for item in value:
                if not isinstance(item, (str, Resource)):
                    raise TypeError
        else:
            raise TypeError

    def __attrs_post_init__(self):
        if self.ra_DependsOn is None:
            pass
        elif isinstance(self.ra_DependsOn, list):
            self.ra_DependsOn = [
                get_id(obj)
                for obj in self.ra_DependsOn
            ]
        else:
            self.ra_DependsOn = [
                get_id(self.ra_DependsOn)
            ]

    def ref(self) -> 'Ref':
        return Ref(self)

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
class Parameter(AwsObject, _DictMember):
    """
    Reference:


    - Parameters: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html
    - AWS-specific parameter types: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-specific-parameter-types
    - SSM parameter types: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#parameters-section-structure-grouping
    """
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
        dct = remove_id_and_empty(dct)
        dct = serialize(dct)
        return dct

@attr.s
class Export(AwsObject):
    Name: TypeHint.intrinsic_str = attr.ib(
        validator=vs.instance_of((str, dict, IntrinsicFunction))
    )

    def serialize(self, **kwargs):
        return {"Name": serialize(self.Name)}


@attr.s
class Output(AwsObject, _DictMember):
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

    def serialize(self, **kwargs) -> typing.Any:
        # you cannot use attr.asdict(self) here, because it will call
        # asdict AWSObject value too. actually we want to call the serialize
        # method instead of asdict here.
        dct = get_key_value_dict(self)
        dct = remove_id_and_empty(dct)
        dct = serialize(dct)
        return dct


@attr.s
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
    """
    region: TypeHint.intrinsic_str = attr.ib(
        validator=vs.instance_of(TypeCheck.intrinsic_str_type)
    )

    def serialize(self, **kwargs) -> dict:
        return {constant.IntrinsicFunction.GET_ATT: serialize(self.region)}


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
    delimiter: TypeHint.intrinsic_str = attr.ib(
        validator=vs.instance_of(TypeCheck.intrinsic_str_type)
    )
    list_of_values: typing.List[TypeHint.intrinsic_str] = attr.ib(
        validator=vs.deep_iterable(
            member_validator=vs.instance_of(TypeCheck.intrinsic_str_type),
            iterable_validator=list,
        )
    )

    def serialize(self, **kwargs) -> dict:
        return {
            constant.IntrinsicFunction.JOIN: [
                serialize(self.delimiter),
                serialize(self.list_of_values)
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

    def serialize(self, **kwargs) -> dict:
        return {
            constant.IntrinsicFunction.SUB: [
                self.string,
                serialize(self.data),
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
    list_of_objects: list = attr.ib(
        validator=vs.instance_of(list),
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
class Rule(AwsObject, _DictMember):
    id: str = attr.ib(
        validator=vs.instance_of(str)
    )


@attr.s
class Mapping(AwsObject, _DictMember):
    pass


@attr.s
class Condition(AwsObject, _DictMember):
    id: str = attr.ib(
        validator=vs.instance_of(str)
    )


@attr.s
class Transform(AwsObject, _ListMember):
    pass


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


def get_id(obj_or_id: typing.Union[str, Parameter, Resource, Output, Rule, Mapping, Condition]) -> str:
    """
    Get the logic id string.
    """
    if isinstance(obj_or_id, str):
        return obj_or_id
    else:
        return obj_or_id.id


def serialize(obj: typing.Union['AwsObject', dict, typing.Any]) -> typing.Any:
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
