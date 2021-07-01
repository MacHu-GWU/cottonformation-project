# -*- coding: utf-8 -*-

import attr

@attr.s
class Stack:
    _stack_data = None

    @property
    def stack_name(self):
        raise NotImplementedError

    def get_stack_data(self, boto_ses):
        cf_client = boto_ses.client("cloudformation")
        if self._stack_data is None:
            self._stack_data = cf_client.describe_stacks(StackName=self.stack_name) \
                ["Stacks"][0]
        return self._stack_data

    def get_output_value(self, boto_ses, output_id):
        stack_data = self.get_stack_data(boto_ses)
        output_key_values = {
            dct["OutputKey"]: dct["OutputValue"]
            for dct in stack_data["Outputs"]
        }
        return output_key_values[output_id]


