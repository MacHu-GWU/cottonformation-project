# -*- coding: utf-8 -*-

"""
The best way to organize multi tier / multi app infrastructure is using
CloudFormation nested stack https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html.
However, with cottonformation, your nested template / resource can be easily declared
and import. The original purpose of CloudFormation nested stack is to split
big template into multiple small one. **With cottonformation, this is unnecessary**.

But if you still want to do that in nested stack, cottonformation can easily do
that too.

Assume you have a complex architect design like this. Each line represent a
CloudFormation Stack / Template. The ``infrastructure tier`` defines
the common resource for all other tier, for example, IAM Role, Security Group.
And the ``shared app tier`` can define the resources used for all other apps,
for example s3 bucket. Eventually the concrete ``app1, 2, ...`` can define
the resources needed to run the app::

    infrastructure
    |-- app tier
        |-- app1
        |-- app2
    |-- data tier
        |-- data1
        |-- data2
    ...
"""

import cottonformation as cf
from cottonformation.res import iam, awslambda, cloudformation

# global parameter
param_project_name = cf.Parameter(
    "ProjectName", Type=cf.Parameter.TypeEnum.String
)

param_stage = cf.Parameter(
    "Stage", Type=cf.Parameter.TypeEnum.String
)


# We declared lots of template here. Each one can be deployed independently
# but cottonformation will put them together using nested stack at the end.
#--- Template(infra) ---
tpl_infra_tier = cf.Template(Description="the master/infra tier")

tpl_infra_tier.add(param_project_name)
tpl_infra_tier.add(param_stage)

iam_role_for_lambda = iam.Role(
    "IamRoleForLambdaExecution",
    rp_AssumeRolePolicyDocument=cf.helpers.iam.AssumeRolePolicyBuilder(
        cf.helpers.iam.ServicePrincipal.awslambda()
    ).build(),
    p_RoleName=cf.Sub(
        "${ProjectName}-${Stage}-lambda-role",
        dict(ProjectName=param_project_name.ref(), Stage=param_stage.ref())
    ),
    p_Description="Minimal iam role for lambda execution",
    p_ManagedPolicyArns=[
        cf.helpers.iam.AwsManagedPolicy.AWSLambdaBasicExecutionRole,
    ]
)
tpl_infra_tier.add(iam_role_for_lambda)


#--- Template(app tier) ---
param_lambda_role_arn = cf.Parameter(
    "LambdaRoleArn", Type=cf.Parameter.TypeEnum.String,
)

tpl_app_tier = cf.Template(Description="the app tier")
tpl_app_tier.add(param_project_name)
tpl_app_tier.add(param_stage)
tpl_app_tier.add(param_lambda_role_arn)


#--- Template(app1) ---
tpl_app1 = cf.Template(Description="the app1")

tpl_app1.add(param_project_name)
tpl_app1.add(param_stage)
tpl_app1.add(param_lambda_role_arn)

lbd_source_code = """
def handler(event, context):
    return "this is app1"
""".strip()

lbd_func_app1 = awslambda.Function(
    "LbdFuncApp1",
    rp_Code=awslambda.PropFunctionCode(
        p_ZipFile=lbd_source_code,
    ),
    rp_Role=param_lambda_role_arn.ref(),
    p_FunctionName=cf.Sub(
        "${ProjectName}-${Stage}-app1",
        dict(ProjectName=param_project_name.ref(), Stage=param_stage.ref())
    ),
    p_MemorySize=128,
    p_Timeout=3,
    p_Runtime=cf.helpers.awslambda.LambdaRuntime.python37,
    p_Handler="index.handler",
)
tpl_app1.add(lbd_func_app1)


#--- Template(app2) ---
tpl_app2 = cf.Template(Description="the app2")

tpl_app2.add(param_project_name)
tpl_app2.add(param_stage)
tpl_app2.add(param_lambda_role_arn)

lbd_source_code = """
def handler(event, context):
    return "this is app2"
""".strip()

lbd_func_app2 = awslambda.Function(
    "LbdFuncApp2",
    rp_Code=awslambda.PropFunctionCode(
        p_ZipFile=lbd_source_code,
    ),
    rp_Role=param_lambda_role_arn.ref(),
    p_FunctionName=cf.Sub(
        "${ProjectName}-${Stage}-app2",
        dict(ProjectName=param_project_name.ref(), Stage=param_stage.ref())
    ),
    p_MemorySize=128,
    p_Timeout=3,
    p_Runtime=cf.helpers.awslambda.LambdaRuntime.python37,
    p_Handler="index.handler",
)
tpl_app2.add(lbd_func_app2)


#--- associate nested stack and template ---
# If you don't know how to do nested stack in classic way
# you can read: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html
#
# cottonformation gives you a simple way to define nested stack / template relationship
# you just need to create a ``cloudformation.Stack`` object in parent stack
# and use the ``parent_template.add_nested_stack(nested_stack_resource, child_template``
# method to associate them together. Then cottonformation will automatically
# handle the deployment for you


# define a stack resource to represent the nested stack
# you have to pass in the parameter into child stack from here
app_tier_stack = cloudformation.Stack(
    "AppTier",
    rp_TemplateURL="",  # will know later, just use "" as dummy data now
    p_Parameters={
        param_project_name.id: param_project_name.ref(),
        param_stage.id: param_stage.ref(),
        param_lambda_role_arn.id: iam_role_for_lambda.rv_Arn,
    },
)
tpl_infra_tier.add(app_tier_stack)
# associate stack and template 'infra tier' <---> 'app tier'
tpl_infra_tier.add_nested_stack(app_tier_stack, tpl_app_tier)


# repeat this for 'app tier' <---> 'app1 tier'
app1_stack = cloudformation.Stack(
    "App1",
    rp_TemplateURL="", # will know later
    p_Parameters={
        param_project_name.id: param_project_name.ref(),
        param_stage.id: param_stage.ref(),
        param_lambda_role_arn.id: param_lambda_role_arn.ref()
    },
)
tpl_app_tier.add(app1_stack)
tpl_app_tier.add_nested_stack(app1_stack, tpl_app1)

# repeat this for 'app tier' <---> 'app2 tier'
app2_stack = cloudformation.Stack(
    "App2",
    rp_TemplateURL="", # will know later
    p_Parameters={
        param_project_name.id: param_project_name.ref(),
        param_stage.id: param_stage.ref(),
        param_lambda_role_arn.id: param_lambda_role_arn.ref()
    },
)
tpl_app_tier.add(app2_stack)
tpl_app_tier.add_nested_stack(app2_stack, tpl_app2)

# Note, data tier is intentionally skipped. Since you can easily repeat
# this pattern for data tier


if __name__ == "__main__":
    # my private aws account session and bucket for testing
    from cottonformation.tests.boto_ses import bsm, bucket

    # define the Parameter.EnvName value
    project_name = "ctf-1-quick-start-3-nested-stack"
    stage = "dev"

    # there's no additional step to deploy a nested stack
    # cottonformation will automatically upload all nested template to s3
    # and update the AWS::CloudFormation::Stack.TemplateUrl property for you.
    env = cf.Env(bsm=bsm)
    env.deploy(
        template=tpl_infra_tier,
        stack_name=project_name,
        stack_parameters={
            param_project_name.id: project_name,
            param_stage.id: stage,
        },
        bucket_name=bucket,
        include_iam=True,
    )
