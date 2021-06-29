# -*- coding: utf-8 -*-

"""
Tagging is very important and can be used for many things:

1. aggregate your bill by project
2. implement automation based on tag
3. isolate resources for different environment
4. optimize cost and automatically shut down invalid resources

In this example, let's learn how to use the
:meth:`cottonformation.core.template.Template.batch_tagging` method
to manage tag at scale. You don't need to memorize whether an AWS Resource
supports Tagging. cottonformation will handle that automatically for you.
"""

import cottonformation as ctf
from cottonformation.res import iam

# declare a Template
tpl = ctf.Template(
    Description="Tagging best practice in cottonformation demo",
)

# declare one Parameter and two Resource
param_env_name = ctf.Parameter(
    "EnvName",
    Type=ctf.Parameter.TypeEnum.String,
)
tpl.add(param_env_name)

# this iam role doesn't have existing tag
iam_role_for_ec2 = iam.Role(
    "IamRoleEC2",
    rp_AssumeRolePolicyDocument=ctf.helpers.iam.AssumeRolePolicyBuilder(
        ctf.helpers.iam.ServicePrincipal.awslambda()
    ).build(),
    p_RoleName=ctf.Sub("${EnvName}-ec2-role", dict(EnvName=param_env_name.ref())),
)
tpl.add(iam_role_for_ec2)

# this iam role has existing tag
iam_role_for_lambda = iam.Role(
    "IamRoleLambda",
    rp_AssumeRolePolicyDocument=ctf.helpers.iam.AssumeRolePolicyBuilder(
        ctf.helpers.iam.ServicePrincipal.awslambda()
    ).build(),
    p_RoleName=ctf.Sub("${EnvName}-lbd-role", dict(EnvName=param_env_name.ref())),
    p_Tags=ctf.Tag.make_many(
        Creator="bob@email.com",
    ),
)
tpl.add(iam_role_for_lambda)

# a common best practice is to define some common tag and assign to all
# AWS resource that support Tags. For example, you can use ``ProjectName``
# to indicate what project it belongs to and you can use it to calculate
# AWS Billing. Another example could be using the ``Stage`` tag to implement
# some automation to process resource in different stage differently.
# For instance, ec2 in dev will be automatically shut down to save cost,
# but ec2 in prod will never be stopped.
tpl.batch_tagging(
    EnvName=param_env_name.ref(),
    Creator="alice@example.com",
    overwrite=False, # you can use overwrite flag to choice whether you want to overwrite existing tag
)


if __name__ == "__main__":
    # my private aws account session and bucket for testing
    from cottonformation.tests.boto_ses import boto_ses, bucket

    # define the Parameter.EnvName value
    env_name = "ctf-1-quick-start-2-tagging"

    env = ctf.Env(boto_ses=boto_ses)
    env.deploy(
        template=tpl,
        stack_name=env_name,
        stack_parameters=dict(
            EnvName=env_name,
        ),
        bucket_name=bucket,
        include_iam=True,
    )
