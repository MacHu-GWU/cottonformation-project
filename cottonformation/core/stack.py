# -*- coding: utf-8 -*-

"""

"""

import typing as T

import attr
from boto_session_manager import BotoSesManager, AwsServiceEnum

from .template import Template


@attr.s
class Stack:
    """
    Stack is an abstraction layer representing a CloudFormation stack.

    All AWS Resource declaration logics should go to the method of a Stack object.
    Declare aws resource directly in python script without putting them into a
    method / function is a bad idea. If there's a single line of code breaks,
    it breaks the entire scripts. And you have to comment in/out big chunk of
    code for debugging. But if you organize AWS Resource declaration logics
    in many methods. You can easily control the subset of the resources to create,
    the order of those resources to be created.

    .. versionadded:: 1.0.1
    """

    _stack_data: T.Optional[dict] = None  # cloudformation stack data cache

    @property
    def stack_name(self) -> str:
        """
        CloudFormation stack name.
        """
        raise NotImplementedError

    def get_stack_data(self, bsm: "BotoSesManager") -> dict:
        """
        Get the boto3 cloudformation.describe_stacks response data that represent
        the current stack.

        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.describe_stacks
        """
        cf_client = bsm.get_client(AwsServiceEnum.CloudFormation)
        if self._stack_data is None:
            self._stack_data = cf_client.describe_stacks(StackName=self.stack_name)[
                "Stacks"
            ][0]
        return self._stack_data

    def get_output_value(self, bsm: "BotoSesManager", output_id: str):
        stack_data = self.get_stack_data(bsm)
        output_key_values = {
            dct["OutputKey"]: dct["OutputValue"] for dct in stack_data["Outputs"]
        }
        return output_key_values[output_id]

    def __attrs_post_init__(self):
        self.template: Template = Template()
        self.post_hook()

    def post_hook(self):
        """
        A user custom post stack initialization hook function. Will be executed
        after object initialization.
        """
        pass
