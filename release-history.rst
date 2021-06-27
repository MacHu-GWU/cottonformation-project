.. _release_history:

Release and Version History
==============================================================================


1.0.0 (Goal)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.0.2 (TODO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Implement more instrinct function.
- Implement
- migrate lots of fancy feature I invented in `troposphere_mate <https://github.com/MacHu-GWU/troposphere_mate-project>`_ to cottonformation

**Minor Improvements**

- 95% + code cov

**Bugfixes**

**Miscellaneous**


0.0.1 (2021-06-25)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- **The birth of cottonformation!**
- use `AWS Cloudformation Spec file <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html>`_ and jinja2 template engine to generate all AWS resource and property class declaration code, type hint, and validation. **Now we can easily make this library up-to-date with latest AWS Cloudformation feature!**
- implements core components include ``Parameter, Property, Resource, Output, Export``. Instrinct function is partially implemented. Now only support ``Ref, GetAtt, Sub``.
- implement serializer for all object and ``Template``.
- implement simple wrapper allow deploy ``Template`` object from Python.

**Minor Improvements**



**Bugfixes**

**Miscellaneous**


0.0.1 (2021-06-22)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- First release