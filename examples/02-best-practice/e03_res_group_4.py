# -*- coding: utf-8 -*-

import attr
import cottonformation as ctf
from cottonformation.res import iam


@attr.s
class IamStack(ctf.Stack):
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

    def mk_rg1(self):
        """
        Make resource group 1
        """
        # declare a resource group, you can use Stack.rg1 to access it later.
        self.rg1 = ctf.ResourceGroup("RG1")

        # declare a resource
        self.iam_group1 = iam.Group(
            "IamGroup1",
            p_GroupName=f"{self.env_name}-group1",
        )

        # add resource to resource group
        # internally it use "Depends On" mechanism. In this example, we can say
        # rg1 depends on iam_group1
        self.rg1.add(self.iam_group1)

    def mk_rg2(self):
        """
        Make resource group 2
        """
        self.rg2 = ctf.ResourceGroup("RG2")
        # you can even add another resource group to it
        self.rg2.add(self.rg1)

        self.iam_group2 = iam.Group(
            "IamGroup2",
            p_GroupName=f"{self.env_name}-group2",
        )
        self.rg2.add(self.iam_group2)

    def mk_rg3(self):
        """
        Make resource group 3
        """
        self.rg3 = ctf.ResourceGroup("RG3")
        self.rg3.add(self.rg2)

        self.iam_group3 = iam.Group(
            "IamGroup3",
            p_GroupName=f"{self.env_name}-group3",
        )
        self.rg3.add(self.iam_group3)

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

iam_stack = IamStack(
    project_name="ctf-best-prac-res-group",
    stage="dev",
)

tpl = ctf.Template(Description="Demo: Resource Group best practice")


#=============================================================================
#                            New Code starts here
#=============================================================================
# add resource group from stack to template, in ascending order.
tpl.add(iam_stack.rg1)
tpl.add(iam_stack.rg2)
tpl.add(iam_stack.rg3)

# or you can just do: add(rg3). since we declared that rg3 depends on rg2
# and rg2 depends on rg1, all resource declared in rg2 and rg1 will be
# automatically added.
# tpl.add(iam_stack.rg3) # uncomment this for testing


# For debugging, you could just remove some resource group and comment them
# in and out one by one between cloudformation deployment.
tpl.remove(iam_stack.rg3)
tpl.remove(iam_stack.rg2)

# or you can just do: remove(rg2). since rg3 depends on rg2
# if we remove rg2, rg3 will be automatically removed
# tpl.add(iam_stack.rg2) # uncomment this for testing