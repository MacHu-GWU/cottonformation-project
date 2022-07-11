# -*- coding: utf-8 -*-

"""
To get started, let's learn how to define a very standard cloudformation template
including a simple Parameter, two Resource depending on each other, and
an Output. Eventually we deploy it to AWS Console. Everything is PURE PYTHON.

**I recommend to NOT COPY AND PASTE but typing the code in Pycharm to see
how type hint / auto complete / doc hint helps you to accelerate code writing**

You are responsible to prepare your AWS Credential to call cloudformation API
and a S3 bucket to upload template. Follow this
`boto3 Session reference <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html>`_
document to create your own boto session object for authentication.
My recommendation is to create a named profile in
``${HOME}/.aws/credentials`` and ``${HOME}/.aws/config``. And then the code
to create boto session looks like this
https://github.com/MacHu-GWU/cottonformation-project/blob/main/cottonformation/tests/boto_ses.py.
"""

# First, import cottonformation, I prefer to use ctf for a short name
import cottonformation as cf

# import the aws service module you need
from cottonformation.res import iam, awslambda

# create a ``Template`` object to represent your cloudformation template
tpl = cf.Template(
    Description="Sample CloudFormation template build on cottonformation library",
)

# create a ``Parameter`` object
param_env_name = cf.Parameter(
    "EnvName",
    Type=cf.Parameter.TypeEnum.String,
)
# the declared ``Parameter`` object is not associated to ``Template`` yet
# we need to explicitly add it to template
tpl.add(param_env_name)

# create a ``Resource`` object for aws iam role
iam_role_for_lambda = iam.Role(
    "IamRoleForLambdaExecution",
    # you don't need to remember the exact name or syntax for
    # trusted entity / assume role policy, cottonformation has a helper for this
    rp_AssumeRolePolicyDocument=cf.helpers.iam.AssumeRolePolicyBuilder(
        cf.helpers.iam.ServicePrincipal.awslambda()
    ).build(),
    p_RoleName=cf.Sub("${EnvName}-iam-role-for-lambda", dict(EnvName=param_env_name.ref())),
    p_Description="Minimal iam role for lambda execution",

    # you don't need to remember the exact ARN for aws managed policy.
    # cottonformation has a helper for this
    p_ManagedPolicyArns=[
        cf.helpers.iam.AwsManagedPolicy.AWSLambdaBasicExecutionRole,
    ]
)
# add resource object to template
tpl.add(iam_role_for_lambda)


# create a ``Resource`` object for aws lambda function
lbd_source_code = """
def handler(event, context):
    return "hello cottonformation"
""".strip()

lbd_func = awslambda.Function(
    "LbdFuncHelloWorld",
    # rp_ stands for Required Property, it will gives you parameter-hint
    # for all valid required properties.
    rp_Code=awslambda.PropFunctionCode(
        p_ZipFile=lbd_source_code,
    ),

    # normally we need to explicitly call GetAtt(resource, attribute)
    # and you need to remember the exact attribute name
    # but cottonformation allow you to instantly reference the attribute
    # powered by auto-complete. the prefix rv_ stands for Return Value
    rp_Role=iam_role_for_lambda.rv_Arn,

    # p_ stands for Property, it will gives you parameter-hint
    # for all valid properties
    p_MemorySize=256,
    p_Timeout=3,

    # some constant value helper here too
    p_Runtime=cf.helpers.awslambda.LambdaRuntime.python37,
    p_Handler="index.handler",
    ra_DependsOn=iam_role_for_lambda,
)
# add resource object to template
tpl.add(lbd_func)

out_lambda_role_arn = cf.Output(
    "LbdRoleArn",
    Description="aws lambda basic execution iam role for reuse",
    Value=iam_role_for_lambda.rv_Arn
)
# add Output object to template
tpl.add(out_lambda_role_arn)


if __name__ == "__main__":
    # my private aws account session and bucket for testing
    from cottonformation.tests.boto_ses import bsm, bucket

    # define the Parameter.EnvName value
    env_name = "ctf-1-quick-start-1-basic"

    # create an environment for deployment, it is generally a boto3 session
    # and a s3 bucket to upload cloudformation template
    env = cf.Env(bsm=bsm)
    env.deploy(
        template=tpl,
        stack_name=env_name,
        stack_parameters=dict(
            EnvName=env_name,
        ),
        bucket_name=bucket,
        include_iam=True,
    )
