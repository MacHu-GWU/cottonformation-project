# -*- coding: utf-8 -*-

# First, import cottonformation, I prefer to use ctf for a short name
import cottonformation as ctf

# import the aws service module you need
from cottonformation.res import iam, awslambda

# create a ``Template`` object to represent your cloudformation template
tpl = ctf.Template()

# create a ``Parameter`` object, and add it to template.
param_env_name = ctf.Parameter(
    "EnvName",
    Type=ctf.Parameter.TypeEnum.String,
)
tpl.add(param_env_name)

# create a ``Resource`` object for aws iam role
iam_role_for_lambda = iam.Role(
    "IamRoleForLambdaExecution",
    # you don't need to remember the exact name or syntax for
    # trusted entity / assume role policy, cottonformation has a helper for this
    rp_AssumeRolePolicyDocument=ctf.helpers.iam.AssumeRolePolicyBuilder(
        ctf.helpers.iam.ServicePrincipal.awslambda()
    ).build(),
    p_RoleName=ctf.Sub("${EnvName}-iam-role-for-lambda", dict(EnvName=param_env_name.ref())),
    p_Description="Minimal iam role for lambda execution",
    # you don't need to remember the exact ARN for aws managed policy.
    # cottonformation has a helper for this
    p_ManagedPolicyArns=[
        ctf.helpers.iam.AwsManagedPolicy.AWSLambdaBasicExecutionRole,
    ]
)
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
    rp_Code=awslambda.FunctionCode(
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
    p_Runtime=ctf.helpers.awslambda.LambdaRuntime.python37,
    p_Handler="index.handler",
    ra_DependsOn=iam_role_for_lambda,
)
tpl.add(lbd_func)

out_lambda_role_arn = ctf.Output(
    "LbdRoleArn",
    Description="aws lambda basic execution iam role for reuse",
    Value=iam_role_for_lambda.rv_Arn
)
tpl.add(out_lambda_role_arn)


if __name__ == "__main__":
    # my private aws account session and bucket for testing
    from cottonformation.tests.boto_ses import boto_ses, bucket

    # define the Parameter.EnvName value
    env_name = "ctf-1-quick-start-1-basic"

    # create an environment for deployment, it is generally a boto3 session
    # and a s3 bucket to upload cloudformation template
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
