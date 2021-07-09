cottonformation Styled Parameter
==============================================================================

Parameterization of the CloudFormation is awesome. Because the nature of CloudFormation is JSON and YAML, there's no easy way to implement data visiting and data handling. That's the reason why CloudFormation invent Parameter / Mapping / Condition / Rule and Intrinsic Function system (like "Fn::Join", "Fn::Sub").

**HOWEVER**, with cottonformation, Infrastructure is simply Python Code. Python can do far more better parameterization and data handling over the Parameter and Intrinsict Function system. Here's the introduction of the **cottonformation Styled Parameter system** that can completely replace the Cloudformation Parameter / Mapping / Condition / Rule and Intrisic Function system.

.. literalinclude:: ../../../../examples/02-best-practice/e01_ctf_styled_parameter.py
    :linenos:
