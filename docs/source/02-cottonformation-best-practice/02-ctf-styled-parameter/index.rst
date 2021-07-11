.. _ctf-styled-parameter:

cottonformation Styled Parameter
==============================================================================

Parameterization of the CloudFormation is awesome. Because the nature of CloudFormation is JSON and YAML, there's no easy way to implement data visiting and data handling. That's the reason why CloudFormation invent Parameter / Mapping / Condition / Rule and Intrinsic Function system (like "Fn::Join", "Fn::Sub").

**HOWEVER**, with cottonformation, Infrastructure is simply Python Code. Python can do far more better parameterization and data handling over the Parameter and Intrinsict Function system. Here's the introduction of the **cottonformation Styled Parameter system** that can completely replace the Cloudformation Parameter / Mapping / Condition / Rule and Intrisic Function system.

.. literalinclude:: ../../../../examples/02-best-practice/e02_ctf_styled_parameter.py
    :linenos:

Template json:

.. code-block:: javascript

    {
        "AWSTemplateFormatVersion": "2010-09-09",
        "Description": "Demo: ctf styled parameter",
        "Metadata": {
            "cottonformation": {
                "version": "0.0.3"
            }
        },
        "Resources": {
            "MyBucket": {
                "Type": "AWS::S3::Bucket",
                "Properties": {
                    "BucketName": "ctf-styled-param-dev-my-bucket",
                    "Tags": [
                        {
                            "Key": "EnvName",
                            "Value": "ctf-styled-param-dev"
                        }
                    ]
                }
            }
        }
    }
