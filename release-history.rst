.. _release_history:

Release and Version History
==============================================================================


Backlog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

- Fix a bug that remove a resource that in a resource group will also remove the entire resource group. Logically, a resource group is a container of a resource, so resource group depends on the resource member. But practically resource, group should not be removed.

**Miscellaneous**


1.1.2 (2023-03-16)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- :meth`~cottonformation.core.env.Env.deploy` now return a ``DeployStackResponse`` object

**Miscellaneous**

- depends on ``aws-cloudformation>=1.3.2``


1.1.1 (2023-03-10)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- support full list of boto3 ``create_stack`` and ``update_stack`` arguments

**Miscellaneous**

- depends on ``aws-cloudformation>=1.3.1``


1.0.1 (2022-12-08)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- First API Stable release!
- Before this version, :meth:`cottonformation.core.model.Resource.update_tags`` only works with List of Tag typed resource tags property. Due to the historical reason, the AWS CloudFormation resource tags type definition is not consistent. I added more logic to handle both old tag type and new tag type.
- Use `aws_cloudformation <https://pypi.org/project/aws-cloudformation/>`_ library to provide better deployment user experience.

**Bugfixes**

- Special handler for appflow, some property are special type but not defined.


0.0.8 (2022-07-12)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- add `Condition Function <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-conditions.html>`_ support.
- add :meth:`cottonformation.core.env.Env.validate`` method to validate a template.

**Minor Improvements**

- add Intrinsic Function and Condition Function example in document.

**Bugfixes**

**Miscellaneous**

- fix out-dated document
- improve test coverage


0.0.7 (2022-05-20)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- remove ``boto_ses`` argument from ``Env``, use ``boto_session_manager.BotoSesManager`` to manage boto3 sessions.
- add localstack support.


0.0.6 (2022-05-07)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- add aws lambda permission builder to ``helpers.awslambda.py``
- add ``.to_yaml_file`` and ``.to_yaml`` method

**Minor Improvements**

- update AWS Managed Policy ARN list

**Bugfixes**

**Miscellaneous**


0.0.5 (2022-03-21)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- update code to adapt latest spec file
- add ``DeletePolicy`` and ``UpdateReplacePolicy`` constant.
- string interpolation intrinsic function ``JOIN``, ``SUB`` now support passing ``Parameter`` and ``Resource`` directly, assuming that it use ``{"Ref": "LogicId"}``.

**Minor Improvements**

- add ``human_readable`` parameter to :meth:`cottonformation.core.template.Template.to_json`` method.

**Bugfixes**

**Miscellaneous**


0.0.4 (2021-11-29)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- update code to adapt latest spec file


0.0.3 (2021-07-08)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Allow :meth:`~cottonformation.core.template.Template.add` to automatically add dependencies AWS object if available
- A CloudFormation stack abstraction class :class:`~cottonformation.core.stack.Stack` provided. It is the best practice to organize AWS Object declaration.
- Add :class:`~cottonformation.core.model.ResourceGroup` class. It is a AWS Object container object. Allow you to group AWS objects and add / remove them in batch. It also support auto-add/auto-remove if dependency relationship is declared.
- Add exception module.
- Add more best practice / programming pattern example

**Minor Improvements**

- refactor :meth:`~cottonformation.core.template.Template.add` and :meth:`~cottonformation.core.template.Template.remove` API.
- re implement the code generator with topo sort algorithm.

**Bugfixes**

**Miscellaneous**

- Unittest improvement.


0.0.2 (2021-06-28)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Implement all intrinsic function.
- Add :meth:`~cottonformation.core.model.Tag.make_many` helper factory method.
- Add support to deploy complex nested stacks from the top template. ``cottonformation`` handles all underlying trivial steps for you.
- Add :meth:`~cottonformation.core.template.Template.remove` method, it also remove dependent resource if you choose to remove the parent resource.
- Allow visit resource from :class:`~cottonformation.core.template.Template` object.


**Minor Improvements**

- more test to cover object serialization
- two more learn-by-example

**Bugfixes**

**Miscellaneous**


0.0.1 (2021-06-25)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- **The birth of cottonformation!**
- use `AWS Cloudformation Spec file <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html>`_ and jinja2 template engine to generate all AWS resource and property class declaration code, type hint, and validation. **Now we can easily make this library up-to-date with latest AWS Cloudformation feature!**
- implements core components include ``Parameter, Property, Resource, Output, Export``. Instrinct function is partially implemented. Now only support ``Ref, GetAtt, Sub``.
- implement serializer for all object and :class:`~cottonformation.core.template.Template`.
- implement simple wrapper allow deploy :class:`~cottonformation.core.template.Template` object from Python.

**Minor Improvements**

**Bugfixes**

**Miscellaneous**
