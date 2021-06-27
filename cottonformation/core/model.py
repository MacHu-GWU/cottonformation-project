# -*- coding: utf-8 -*-

import json
import typing

import attr
from attr import validators as vs

from . import constant


class TypeHint:
    intrinsic_str = typing.Union[str, dict, 'IntrinsicFunction']
    addable_obj = typing.Union[
        'Parameter', 'Resource', 'Output',
        'Rule', 'Mapping', 'Condition',
    ]


@attr.s
class AwsObject:
    def serialize(self, **kwargs) -> typing.Any:
        raise NotImplementedError

    def deserialize(self, **kwargs) -> typing.Any:
        raise NotImplementedError


@attr.s
class IntrinsicFunction(AwsObject):
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
        class_data = _get_key_value_dict(self)
        attr_name_to_cf_name_mapper = self.get_attr_name_to_cf_name()

        property_dct = dict()
        for k, v in class_data.items():
            if k.startswith("rp_") or k.startswith("p_"):
                if v is not None:
                    property_dct[attr_name_to_cf_name_mapper[k]] = v
        property_dct = serialize(property_dct)
        return property_dct


@attr.s
class Resource(_PropertyOrResource):
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
        class_data = _get_key_value_dict(self)
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
class Parameter(AwsObject):
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
        dct = _get_key_value_dict(self)
        dct = _remove_id_and_empty(dct)
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
class Output(AwsObject):
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
        dct = _get_key_value_dict(self)
        dct = _remove_id_and_empty(dct)
        dct = serialize(dct)
        return dct


@attr.s
class Tag(Property):
    p_Key: str = attr.ib(
        default=None,
        validator=vs.optional(vs.instance_of(str)),
        metadata={constant.AttrMeta.PROPERTY_NAME: "Key"},
    )
    p_Value: typing.Union[str, dict, 'IntrinsicFunction'] = attr.ib(
        default=None,
        validator=vs.optional(vs.instance_of(str)),
        metadata={constant.AttrMeta.PROPERTY_NAME: "Value"},
    )

    def serialize(self, **kwargs) -> typing.Any:
        return {"Key": serialize(self.p_Key), "Value": serialize(self.p_Value)}


@attr.s
class Ref(IntrinsicFunction):
    """
    Reference:

    - Ref: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html
    """
    param_or_res: typing.Union[str, Parameter, Resource] = attr.ib(
        validator=vs.instance_of((str, Parameter, Resource))
    )

    def serialize(self):
        return {"Ref": get_id(self.param_or_res)}


@attr.s
class Base64(IntrinsicFunction):
    pass


@attr.s
class Cidr(IntrinsicFunction):
    pass


@attr.s
class FindInMap(IntrinsicFunction):
    pass


@attr.s
class GetAtt(IntrinsicFunction):
    """
    Reference:

    - Fn::GetAtt: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html
    """
    resource: typing.Union[str, Resource] = attr.field(validator=vs.instance_of((str, Resource)))
    attr_name: str = attr.field(validator=vs.instance_of(str))

    def serialize(self, **kwargs) -> typing.Any:
        return {
            constant.IntrinsicFunction.GET_ATT: [
                get_id(self.resource),
                self.attr_name,
            ]
        }


@attr.s
class GetAZs(IntrinsicFunction):
    pass


@attr.s
class ImportValue(IntrinsicFunction):
    pass


@attr.s
class Join(IntrinsicFunction):
    pass


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
    pass


@attr.s
class Split(IntrinsicFunction):
    pass


@attr.s
class Rule(AwsObject):
    id: str = attr.ib(
        validator=vs.instance_of(str)
    )


@attr.s
class Mapping(AwsObject):
    pass


@attr.s
class Condition(AwsObject):
    id: str = attr.ib(
        validator=vs.instance_of(str)
    )


@attr.s
class Transform(AwsObject):
    pass


@attr.s
class Transform(AwsObject):
    pass


def _get_key_value_dict(obj: attr.s) -> dict:
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


def _remove_id_and_empty(dct: dict) -> dict:
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


class TypeCheck:
    intrinsic_str_type = (str, dict, IntrinsicFunction)
    addable_type = (Parameter, Resource, Output, Rule, Mapping, Condition)


@attr.s
class Template:
    """
    Reference:

    - Template anatomy: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html
    """
    AWSTemplateFormatVersion: str = attr.ib(default="2010-09-09")
    Description: str = attr.ib(default=None)
    Metadata: dict = attr.ib(factory=dict)
    Parameters: typing.Dict[str, Parameter] = attr.ib(factory=dict)
    Rules: typing.Dict[str, Rule] = attr.ib(factory=dict)
    Mappings: typing.Dict[str, Mapping] = attr.ib(factory=dict)
    Conditions: typing.Dict[str, Condition] = attr.ib(factory=dict)
    Resources: typing.Dict[str, Resource] = attr.ib(factory=dict)
    Outputs: typing.Dict[str, Output] = attr.ib(factory=dict)
    Transform: typing.List['Transform'] = attr.ib(factory=list)

    def _add(self,
             obj: TypeHint.addable_obj,
             add_or_update: bool = False,
             add_or_ignore: bool = False):
        is_resource = False
        if isinstance(obj, Parameter):
            dct = self.Parameters
        elif isinstance(obj, Resource):
            dct = self.Resources
            is_resource = True
        elif isinstance(obj, Output): # pragma: no cover
            dct = self.Outputs
        elif isinstance(obj, Rule): # pragma: no cover
            dct = self.Rules
        elif isinstance(obj, Mapping): # pragma: no cover
            dct = self.Mappings
        elif isinstance(obj, Condition): # pragma: no cover
            dct = self.Conditions
        else:
            raise TypeError(f"You cannot add {obj.__class__.__name__}")
        if obj.id in dct:
            if add_or_update:
                dct[obj.id] = obj
            elif add_or_ignore:
                pass
            else:
                if is_resource:
                    type_name = Resource.__name__
                else:
                    type_name = obj.__class__.__name__
                raise ValueError(f"{type_name} logic id '{obj.id}' is already exists!")
        else:
            dct[obj.id] = obj

    def add(self, obj: TypeHint.addable_obj):
        self._add(obj)

    def add_or_update(self, obj: TypeHint.addable_obj):
        self._add(obj, add_or_update=True)

    def add_or_ignore(self, obj: TypeHint.addable_obj):
        self._add(obj, add_or_ignore=True)

    def to_dict(self) -> dict:
        dct = _get_key_value_dict(self)
        dct = _remove_id_and_empty(dct)
        dct = serialize(dct)
        return dct

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=4)

    def to_json_file(self, path): # pragma: no cover
        with open(path, "w") as f:
            f.write(self.to_json())

    def to_yml(self) -> str: # pragma: no cover
        raise NotImplementedError

    def to_yml_file(self, path): # pragma: no cover
        with open(path, "w") as f:
            f.write(self.to_yml())
