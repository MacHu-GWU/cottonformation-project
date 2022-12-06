# -*- coding: utf-8 -*-

import typing

import cottonformation as ctf
from cottonformation.res import iam


# declare multiple Parameter
# use one data container class to organize everything
class Params:
    env_name: ctf.Parameter = ctf.Parameter("EnvName", Type=ctf.Parameter.TypeEnum.String)
    all_group: ctf.Parameter = ctf.Parameter("AllGroup", Type=ctf.Parameter.TypeEnum.CommaDelimitedList)


# declare a function that creates Template object from Parameters, Mappings,
# Conditions, Rules ...
# In this example, parameters data container class is the only argument
# But you could use mapping container class, condition container class too
def create_template(params: typing.Type[Params]) -> ctf.Template:
    tpl = ctf.Template(Description="Demo: ctf styled parameter")

    # add all parameter declaration to template
    tpl.add(params.env_name)
    tpl.add(params.all_group)

    # create many iam users based on the list data in parameter all_user_email
    for group_name in params.all_group.get_value().split(","):
        iam_group = iam.Group(
            f"IamGroup{group_name}",
            p_GroupName=group_name,
        )
        tpl.add(iam_group)

    # tag everything using parameter env_name
    tpl.batch_tagging(dict(EnvName=params.env_name.ref()))

    return tpl


if __name__ == "__main__":
    # give values to parameters before the creation of Template
    Params.env_name.set_value("ctf-old-style-param")

    all_group_values = [
        "Developer",
        "DevOps",
        "Manager",
    ]
    Params.all_group.set_value(",".join(all_group_values))

    # now generate the template base on the parameter value
    tpl = create_template(Params)
    print(tpl.to_json())

    # my private aws account session and bucket for testing
    from cottonformation.tests.boto_ses import bsm, bucket

    env = ctf.Env(bsm=bsm)
    env.deploy(
        template=tpl,
        stack_name=Params.env_name.get_value(),
        # helper method gives you the python dict view of parameter id and value
        stack_parameters=tpl.get_param_values(),
        bucket_name=bucket,
        include_iam=True,
    )
