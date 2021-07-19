.. _resource-group:

Organize AWS Object using Resource Group
==============================================================================

When there are many resources in your template, it becomes difficult to manage and debug. You probably want to put resources into different logic "Resource Group", and you want to test them separately, even though in most of the case they depend on each other. For debugging, it is always better to deploy resources gradually rather than deploy all of them at once.

Let's walk through an example to demonstrate how and the benefit of doing this.


Step 1. Declare cottonformation style parameter
------------------------------------------------------------------------------

At begin, we simply declare a CloudFormation stack object. And declared two simple cottonformation style parameters ``project_name`` and ``stage``. Stack is not associated with a CloudFormation template object yet.


.. literalinclude:: ../../../../examples/02-best-practice/e03_res_group_1.py
    :linenos:


Step 2. Declare abstract resource group logic
------------------------------------------------------------------------------

Now we believe that we will need two resource groups. For each resource group, we define a method to put into creation logics. And we have a high level method ``post_hook`` to explicitly call resource group creation methods. Of course, you can easily comment them in-and-out to enable/disable those resources. Right now we have nothing in those resource group creation methods.

.. literalinclude:: ../../../../examples/02-best-practice/e03_res_group_2.py
    :linenos:


Step 3. Declare AWS Resources and Resource Group
------------------------------------------------------------------------------

We declare some AWS Resource for each resource group. Here we use IAM.Group, because it is fast to create and basically has no effect to the AWS Account.

Resource group itself is similar to other AWS Object, you have to pass a unique logic id. Basically you can think that it is just a AWS Object container (Parameter, Resource, Output, Mapping, Condition, Rule ...), even for another Resource Group. You can use :class:`cottonformation.core.model.ResourceGroup.add` or :class:`cottonformation.core.model.ResourceGroup.add_many` API to add other resource to a resource group.

At the end, we create a instance of this stack and a template object for future use. At this moment, stack and template doesn't know each other yet.

.. literalinclude:: ../../../../examples/02-best-practice/e03_res_group_3.py
    :linenos:


Step 4. Manage Resource Group in Template
------------------------------------------------------------------------------

To add resource declared in a stack to a cloudformation Template is easy. You can add resource group in ascending order. Or you can just add the last resource group in dependency chain. All dependency resource will be automatically added. We can easily enable/disable many resources by comment in/out.

For debug, sometime you want to remove resource in descending order.

.. literalinclude:: ../../../../examples/02-best-practice/e03_res_group_4.py
    :linenos:


Step 5. Play with Deployment
------------------------------------------------------------------------------

Now we can play with the deployment. And feel free to comment in and out either in the ``template.add(resource_group)`` code block, either in the ``template.remove(resource_group)`` code block.

.. literalinclude:: ../../../../examples/02-best-practice/e03_res_group_5.py
    :linenos:
