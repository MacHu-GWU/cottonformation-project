# -*- coding: utf-8 -*-

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


class AWSObjectLogicIdConflictError(Exception):
    pass


class AWSObjectNotExistsError(Exception):
    @classmethod
    def make(cls, obj_type: str, logic_id: str):
        msg = f"Template.{obj_type} doesn't have logic id = '{logic_id}'"
        return cls(msg)
