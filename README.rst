
.. image:: https://github.com/MacHu-GWU/cottonformation-project/workflows/CI/badge.svg
    :target: https://github.com/MacHu-GWU/cottonformation-project/actions?query=workflow:CI

.. image:: https://codecov.io/gh/MacHu-GWU/cottonformation-project/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/MacHu-GWU/cottonformation-project

.. image:: https://readthedocs.org/projects/cottonformation/badge/
    :target: https://cottonformation.readthedocs.io/en/latest/index.html

.. image:: https://img.shields.io/pypi/v/cottonformation.svg
    :target: https://pypi.python.org/pypi/cottonformation

.. image:: https://img.shields.io/pypi/l/cottonformation.svg
    :target: https://pypi.python.org/pypi/cottonformation

.. image:: https://img.shields.io/pypi/pyversions/cottonformation.svg
    :target: https://pypi.python.org/pypi/cottonformation

.. image:: https://badges.gitter.im/cottonformation/community.svg
    :target: https://gitter.im/cottonformation/community

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/cottonformation-project

------


.. image:: https://img.shields.io/badge/Link-Document-blue.svg
    :target: https://cottonformation.readthedocs.io/en/latest/index.html

.. image:: https://img.shields.io/badge/Link-API-blue.svg
    :target: https://cottonformation.readthedocs.io/en/latest/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Source_Code-blue.svg
    :target: https://cottonformation.readthedocs.io/en/latestpy-modindex.html

.. image:: https://img.shields.io/badge/Link-Install-blue.svg
    :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
    :target: https://github.com/MacHu-GWU/cottonformation-project

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
    :target: https://github.com/MacHu-GWU/cottonformation-project/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
    :target: https://github.com/MacHu-GWU/cottonformation-project/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
    :target: https://pypi.org/pypi/cottonformation#files


Welcome to ``cottonformation`` Documentation
==============================================================================

`Full Documentatioin Here <https://cottonformation.readthedocs.io/en/latest/index.html>`_

``cottonformation`` is a Python tool providing best development experience and highest productivity. Powered by modern **Type Hint, Advanced Auto Complete, Parameter Hint, Instant official AWS Document look up**. Here's how it looks like in `PyCharm <https://www.jetbrains.com/pycharm/>`_ (Supported by PyCharm out-of-the-box, but you can configure it by installing extension or plugin in VSCode, Sublime, Atom ...).

.. note::

    This example is based on PyCharm + MacOS. The shortcut key could be different on different OS (Windows / Linux) / IDE (VSCode / Sublime / Atom ...).


1. **Type hint and property hint**: tell you what property is available, what is the type, and auto complete the code for you. ``rp`` prefix stands for **Required Property**, ``p`` prefix stands for **Optional Property**, you can navigate property using UP and DOWN key. You can also view available property and type (Cmd + P), see how at `View Parameter Info <https://www.jetbrains.com/pycharm/guide/tips/parameter-info/>`_.

.. image:: https://user-images.githubusercontent.com/6800411/123467578-a691af00-d5be-11eb-8869-83c0db3253b5.gif

2. **Return value hint**: tell you what return value is available, and allow you instantly acccess it without need looking up the AWS Document. **You don't need to remember ANY API**. To be honest, looking up the exact Resource Attribute Name in https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html and then ``GetAtt(resource_object, attribute_name)`` is really **UGLY!**

.. image:: https://user-images.githubusercontent.com/6800411/123468458-ca092980-d5bf-11eb-906b-793c148dc3c0.gif

3. **Parameter hint**: tell you all available parameter and its type (Cmd + P). It works on both Resource Type and complex Property Type.

.. image:: https://user-images.githubusercontent.com/6800411/123477456-19eded80-d5cc-11eb-84a6-7c864e39a142.gif

4. **Jump to resource doc**: instantly open the AWS Doc about this AWS Resource in web browser. Click on the class, hit F1 and click on the link.

.. image:: https://user-images.githubusercontent.com/6800411/123477362-f0cd5d00-d5cb-11eb-9d09-32cfb1d96710.gif

5. **Jump to property doc method 1**: instantly open the AWS Doc about this Resource Property in web browser. Click on the class, hit F1 (view doc string), find the property and click on the link.

.. image:: https://user-images.githubusercontent.com/6800411/123478114-ff684400-d5cc-11eb-8a62-f168d3ae4ed3.gif

6. **Jump to property doc method 2**: reference the resource property using ``resource_object.property_name`` syntax, click on the property, hit F1 (view doc string), and click on the link.

.. image:: https://user-images.githubusercontent.com/6800411/123478125-042cf800-d5cd-11eb-8fc9-80cb5507845b.gif

7. **Jump to return value doc**: reference the resource attribute using ``resource_object.attribute_name`` syntax, click on the property, hit F1 (view doc string), and click on the link.

.. image:: https://user-images.githubusercontent.com/6800411/123478144-0bec9c80-d5cd-11eb-8260-a9de04690177.gif


**A sample infrastructure as code script may looks like this. And you can immediately deploy it from Python**:

.. code-block:: python

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


Getting Help
------------------------------------------------------------------------------

1. The easiest way to learn the best practice is to **learn by example**. You can start from `cottonformation by example <https://cottonformation.readthedocs.io/en/latest/01-cottonformation-by-example/index.html>`_. Then you can **learn best practice proved in production environment** in `cottonformation best practice <https://cottonformation.readthedocs.io/en/latest/02-cottonformation-best-practice/index.html>`_.

2. Second method is to `submit an GitHub issue <https://github.com/MacHu-GWU/cottonformation-project/issues>`_. So other people may see the discussion and solution too. In addition there's a `cottonformation community <https://gitter.im/cottonformation/community>`_ **on gitter to directly ASK THE AUTHOR**.

.. image:: https://badges.gitter.im/cottonformation/community.svg
    :target: https://gitter.im/cottonformation/community


Overview
------------------------------------------------------------------------------


Why this Project?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**The Goal**:

There are lots of Cloud infrastructure as code tools available `AWS CloudFormation <https://aws.amazon.com/cloudformation/>`_, `Terraform <https://www.terraform.io/>`_, `troposphere <https://github.com/cloudtools/troposphere>`_, `aws cdk <https://aws.amazon.com/cdk/>`_, `pulumi <https://www.pulumi.com>`_. They all be good in different way. ``cottonformation`` is not trying to beat or replace any of them, but focus on being the best in it's special way.

1. Most productive for development.
2. Most user friendly, no memorization, no difficult learning curve.
3. Less code, light weight, easy to customize and extend.

**The History**:

The first generation Infrastructure as Code (**IAC**) might be AWS CloudFormation firstly released on 2011 and Terraform firstly released on 2014. The first generation IAC are mostly Domain specific language (**DSL**). They are not as powerful as general programming language like Java, C#, Python, Ruby, Go. Because of the nature **DSL**, it is hard to manipulate data, customize logic flow, poor code reusability, difficult to customize and extend.

The rule breaker ``troposphere`` was released on 2013. It is a Python project allow you to write CloudFormation template in Python using Objective Oriented programming model. But due to the initial code design, natively it is not able to support modern developer features like "Auto Complete" and "Type Hint". As a result, at least 50% of development time is used in lookup manual, read documentations. At mean time, AWS Cloudformation is evolving very fast supporting more AWS Resource. Since ``troposphere`` relies on maintainer adding implementation manually, it usually falls behind the latest feature.

I started to maintain a parallel library ``troposphere_mate`` to support "Auto Complete" and "Type Hint" and more advanced feature. However, it cannot evolve fast since it is based on ``troposphere`` and I have no control at all on it. I used to think of re-design a new project using latest programming model to replace ``troposphere`` in my Organization. But there are 162 AWS Service, 768 AWS Resource, 2,499 AWS Property and 43,200 lines of declaration code to work on. It is impossible to keep it up-to-date as an individual developer.

**Fortunately, AWS published the** `AWS CloudFormation resource specification <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html>`_ as **a machine readable json file**, and type hint and static check technology is already mature in Python community, I believe it is a good timing to re-invent a modernized CloudFormation tool. **I figured out a way to automatically generate the 162 AWS Service, 768 AWS Resource, 2,499 AWS Property and 43,200 lines of declaration code with type hint / auto complete / aws doc jump features. Now we can easily keep cottonformation up-to-date with AWS CloudFormation!**


What about AWS CDK or Pulumi?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Again, ``cottomformation`` don't want to be the improved AWS CDK or Pulumi. It want to do the best on the limited, but important feature as IAC tool.

**AWS CDK**:

Python is not first class member in AWS CDK. The nature of AWS CDK is a TypeScript Library, and AWS find a way to call TypeScript / JavaScript API from other programming language like Java / Ruby / Python / C# / Go. When you run AWS CDK in programming language other than TypeScript, the code is actually been converted to low level api, and been handled by the backend TypeScript code. This causes two issue:

1. **Significant delay in editing**. Since "Type hint" and "Code Complete" is based on static code analysis technique and Python import engine. But internally AWS CDK import the underlying compiled Python - TypeScript ``*.jsii`` code when you import a AWS Resource declaration class. This is why it's slow with a 2019, 16GB memory Macbook Pro.
2. **Hard to customize and extend**. Because the python code is underlying calling TypeScript API, there's no way you can inject your custom logic in the python code because it is not recognized by TypeScript API.
3. **You have to configure the Node.JS environment the Node.JS version of AWS CDK**. In python community, we expect a simple ``pip install something`` then ``import something``. You need additional configuration steps when you run it in a remote or a CI environment.

**Pulumi**:

Pulumi is more like terraform. Unlike troposphere and AWS CDK, it doesn't convert script to CloudFormation, but using it's own executing engine to deploy resources. Although it is easy to learn and worth, but you need to learn lots of new concept and component.


.. _install:

Install
------------------------------------------------------------------------------

``cottonformation`` is released on PyPI, so all you need is:

.. code-block:: console

    $ pip install cottonformation

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade cottonformation