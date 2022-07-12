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

    #=============================================================================
    #                            New Code starts here
    #=============================================================================
    def mk_rg1(self):
        """
        Make resource group 1
        """
        pass

    def mk_rg2(self):
        """
        Make resource group 2
        """
        pass

    def mk_rg3(self):
        """
        Make resource group 3
        """
        pass

    def post_hook(self):
        """
        A user custom post stack initialization hook function. Will be executed
        after object initialization.

        We will put all resources in two different resource group.
        And there will be a factory method for each resource group. Of course
        we have to explicitly call it to create those resources.
        """
        self.mk_rg1()
        self.mk_rg2()
        self.mk_rg3()
