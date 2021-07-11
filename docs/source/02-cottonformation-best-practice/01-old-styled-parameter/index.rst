.. _old-styled-parameter:

Old Styled Parameter
==============================================================================

Unlike writing in JSON and YAML Cloudformation Template, you can leverage the built-in control flow, if else condition, for loop iteration in Python. Sometimes the value of Parameter can be used as a factor in control flow, however the value is not avaialble yet in Template Declaration phase. Because people usually pass in value to Parameter after the full Template is declared.

In ``cottonformation``, there's a best practice called **Late Template Creation** for this Situation. In this example, we declared a comma delimitered string parameter called ``Parameter(AllGroup, ...)``. It is the list IAM Group name you want to create. The number of IAM Group Resource to declare should equal to number of item in this Parameter.

:class:`~cottonformation.core.model.Parameter` has two method that allow to "set" value for template creation and "get" value for future use. You can firstly declare all :class:`~cottonformation.core.model.Parameter`, give them values, and eventually execute the :class:`~cottonformation.core.template.Template` generation logic.

.. literalinclude:: ../../../../examples/02-best-practice/e01_old_styled_parameter.py
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
        "Parameters": {
            "EnvName": {
                "Type": "String"
            },
            "AllGroup": {
                "Type": "CommaDelimitedList"
            }
        },
        "Resources": {
            "IamGroupDeveloper": {
                "Type": "AWS::IAM::Group",
                "Properties": {
                    "GroupName": "Developer"
                }
            },
            "IamGroupDevOps": {
                "Type": "AWS::IAM::Group",
                "Properties": {
                    "GroupName": "DevOps"
                }
            },
            "IamGroupManager": {
                "Type": "AWS::IAM::Group",
                "Properties": {
                    "GroupName": "Manager"
                }
            }
        }
    }

