# -*- coding: utf-8 -*-

import attr
import cottonformation as cf


@attr.s
class IamStack(cf.Stack):
    project_name: str = attr.ib()
    stage: str = attr.ib()

    @property
    def env_name(self):
        """
        A prefix for most of naming convention. Isolate resource from each other.
        """
        return f"{self.project_name}-{self.stage}"

    @property
    def stack_name(self):
        """
        CloudFormation stack name.
        """
        return f"{self.env_name}-iam-stack"
