cottonformation by Example
==============================================================================


1. Basic Template
------------------------------------------------------------------------------

To get started, let's learn how to define a very standard cloudformation template including a simple Parameter, two Resource depending on each other, and
an Output. Eventually we deploy it to AWS Console. Everything is PURE PYTHON.

**I recommend to NOT COPY AND PASTE but typing the code in Pycharm to see how type hint / auto complete / doc hint helps you to accelerate code writing**

You are responsible to prepare your AWS Credential to call cloudformation API and a S3 bucket to upload template. Follow this `boto3 Session reference <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html>`_ document to create your own boto session object for authentication. My recommendation is to create a named profile in ``${HOME}/.aws/credentials`` and ``${HOME}/.aws/config``. And then the code to create boto session looks like this https://github.com/MacHu-GWU/cottonformation-project/blob/main/cottonformation/tests/boto_ses.py.

.. literalinclude:: ../../../examples/01-quick-start/e01_basic.py
    :linenos:


2. Batch Tagging
------------------------------------------------------------------------------

**Tagging is very important and can be used for many things**:

1. aggregate your bill by project
2. implement automation based on tag
3. isolate resources for different environment
4. optimize cost and automatically shut down invalid resources

In this example, let's learn how to use the :meth:`~cottonformation.core.template.Template.batch_tagging` method to **manage tag at scale**. You don't need to memorize whether an AWS Resource
supports Tagging. cottonformation will handle that automatically for you.

.. literalinclude:: ../../../examples/01-quick-start/e02_tagging.py
    :linenos:


3. Nested Stack / Template
------------------------------------------------------------------------------

The best way to organize multi tier / multi app infrastructure is using CloudFormation nested stack https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html. However, **with cottonformation, your nested template / resource can be easily declared and import**. The original purpose of CloudFormation nested stack is to split big template into multiple small one. **With cottonformation, this is unnecessary**.

But if you still want to do that in nested stack, cottonformation can easily do that too.

Assume you have a complex architect design like this. Each line represent a CloudFormation Stack / Template. The ``infrastructure tier`` defines the common resource for all other tier, for example, IAM Role, Security Group. And the ``shared app tier`` can define the resources used for all other apps, for example s3 bucket. Eventually the concrete ``app1, 2, ...`` can define the resources needed to run the app::

    infrastructure
    |-- app tier
        |-- app1
        |-- app2
    |-- data tier
        |-- data1
        |-- data2
    ...


.. literalinclude:: ../../../examples/01-quick-start/e03_nested.py
    :linenos:
