.. _quick-start:

Quick Start
==============================================================================

1. Basic Template
------------------------------------------------------------------------------

Let's define one Parameter, two AWS Resource one depends on another and then use Output to catch a value for future reuse. And finally we deploy it and view it in AWS Console. Everything is pure Python.

But you are responsible to prepare your AWS Credential and a S3 bucket to upload template. Follow this `boto3 Session reference <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html>`_ document to create your own boto session object for authentication.

.. literalinclude:: ../../../../examples/01-quick-start/e01_basic.py
    :linenos:
