.. _release_history:

Release and Version History
==============================================================================


1.0.0 (Next Milestone)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.0.5 (Next Milestone)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

- fix a bug that remove a resource that in a resource group will also remove the entire resource group. Logically, a resource group is a container of a resource, so resource group depends on the resource member. But practically resource group should not be removed.ma

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
