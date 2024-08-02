.. include:: ../links.rst

.. _AttributeError:

#################################################################################
AttributeError
#################################################################################

----

.. contents:: table of contents
  :local:
  :depth: 1

----

An Attribute is a property, variable, function or name that belongs to an object_. For example when I describe a human being I can list attributes like height, weight, sex and color.

An `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ is raised when there is a reference to a name in an object_ that does not exist.

*********************************************************************************
requirements
*********************************************************************************


:doc:`how to make a python test driven development environment </how_to/make_tdd_environment>`

----

*********************************************************************************
test_attribute_error_w_variables
*********************************************************************************

red: make it fail
#################################################################################

I open a new file, save it as ``test_attribute_error.py`` in the ``tests`` folder made in :doc:`how to make a python test driven development environment </how_to/make_tdd_environment>` and type the following

.. code-block:: python

  import unittest
  import module

* ``import unittest`` imports the unittest_ module from thePython standard library
* ``import module`` imports the ``module`` module - which will hold the code I am testing

the terminal shows a :ref:`ModuleNotFoundError` if you have not yet done the :doc:`/how_to/exception_handling_tests` chapter

.. code-block:: python

  ModuleNotFoundError: No module called 'module'

A :ref:`ModuleNotFoundError` is raised when a name is provided to an `import statement`_ andPython cannot find the name. Since there is currently no file called ``module.py`` the ``import module`` line causes a failure

green: make it pass
#################################################################################

* I make the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError

* then make ``module.py`` in the ``magic`` folder and the terminal all tests are passing
* I continue adding tests to ``test_attribute_error.py``

  .. code-block:: python

    import unittest
    import module


    class TestAttributeErrors(unittest.TestCase):

        def test_attribute_error_w_variables(self):
            module.variable_0

  - ``class TestAttributeErrors(unittest.TestCase):`` is a class definition that inherits from `unittest.TestCase`_ and will hold the tests
  - ``def test_attribute_error_w_variables(self):`` is the definition of the first test function to find out if defining variables can solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_
  - ``module.variable_0`` - the actual test, I think of this as making a phone call to ``variable_0`` in ``module.py``

  the terminal shows an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    AttributeError: module 'module' has no attribute 'variable_0'

* I add the error to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError

* then add a name to ``module.py``

  .. code-block:: python

    variable_0

  and the terminal shows a NameError_

  .. code-block::

    NameError: name 'variable_0' is not defined

  ``NameError: name 'variable_0' is not defined`` the NameError_ is raised because ``variable_0`` in ``module.py`` is considered a reference and there is currently no definition or assignment for that name

* I add NameError_ to the list of errors encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # NameError

* then change the failing line in ``module.py`` to fix it by assigning the name ``variable_0`` to the :doc:`null value </data_structures/none>`

  .. code-block:: python

    variable_0 = None

  this assigns the name ``variable_0`` to :ref:`None` and the terminal shows a passing test. YES!

I solved the `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining a variable

.. NOTE::

  - in Python ``=`` is used to assign names to objects, for example ``five = 5`` means I can refer to the number ``5`` with the name ``five``
  - the equality sign ``==`` is used to check if two things are equal example  ``5 == 4`` means "is ``5`` is equal to ``4``?"

AttributeError vs NameError
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ is raised when there is a reference to a name in an object_ from outside the object_ and the name does not exist, for example ``humans.wings``

A NameError_ is raised when there is a reference to a name within an object_ and there is no definition for the name


refactor: make it better
#################################################################################

I could repeat the above tests as a drill to help remember the solution

* I add a failing line

  .. code-block:: python

    def test_attribute_error_w_variables(self):
        module.variable_0
        module.variable_1

  the terminal shows an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    AttributeError: module 'module' has no attribute 'variable_1'

* I add the name to ``module.py``

  .. code-block:: python

    variable_0 = None
    variable_1

  the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'variable_1' is not defined

* I add a definition for ``variable_1``

  .. code-block:: python

    variable_0 = None
    variable_1 = None

  the terminal shows passing tests

* I add a failing line

  .. code-block:: python

    def test_attribute_error_w_variables(self):
        module.variable_0
        module.variable_1
        module.variable_2

  the terminal shows an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    AttributeError: module 'module' has no attribute 'variable_2'

* I add the name to ``module.py``

  .. code-block:: python

    variable_0 = None
    variable_1 = None
    variable_2

  the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'variable_2' is not defined

* I define ``variable_2`` in ``module.py``

  .. code-block:: python

    variable_0 = None
    variable_1 = None
    variable_2 = None

  The tests pass

* I add a failing line

  .. code-block:: python

    def test_attribute_error_w_variables(self):
        module.variable_0
        module.variable_1
        module.variable_2
        module.variable_3

  the terminal shows an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    AttributeError: module 'module' has no attribute 'variable_3'

* I add the name

  .. code-block:: python

    variable_0 = None
    variable_1 = None
    variable_2 = None
    variable_3

  the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'variable_3' is not defined

* I define the name

  .. code-block:: python

    variable_0 = None
    variable_1 = None
    variable_2 = None
    variable_3 = None

I have a pattern for the drill. When I test an attribute in a module, I get

* an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ when the attribute does not exist
* a NameError_ when I add the name to the module
* a passing test when I define the name as a variable

If you are feeling adventurous you can add more tests to ``test_attribute_error_w_variables`` until you get to ``module.variable_99``, you will have 100 lines

.. code-block:: python

  def test_attribute_error_w_variables(self):
      module.variable_0
      module.variable_1
      module.variable_2
      module.variable_3
      ...
      module.variable_99

Repeat the pattern until all tests pass.

If you have been typing along *WELL DONE!* You now know

* how to solve a :ref:`ModuleNotFoundError`
* how to solve a NameError_ using variables
* how to solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining variables

----

*********************************************************************************
test_attribute_error_w_functions
*********************************************************************************

red: make it fail
#################################################################################

I add a new test to ``TestAttributeError`` class in ``tests/test_attribute_error.py``

.. code-block:: python

  def test_attribute_error_w_functions(self):
      module.function_0()

the terminal shows an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

.. code-block:: python

  AttributeError: module 'module' has no attribute 'function_0'

green: make it pass
#################################################################################

* I try the solution I know for solving `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ with variables and change ``module.py`` to include a new variable

  .. code-block:: python

    function_0 = None

  I see a :ref:`TypeError` in the terminal

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* I add it to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # NameError
    # TypeError

* a :ref:`TypeError` is raised in this case because I called an object that was not callable_

  A callable_ object is an object that may be able to handle inputs. I can make an object_ callable_ by defining it as a :ref:`class <classes>` or a :ref:`function<functions>`

  Parentheses are used at the end of the name of an object when calling it, for example  ``module.function_0()`` will call ``function_0`` from ``module.py``

* What if I make ``function_0`` in ``module.py`` to a function by using the def_ keyword?

  .. code-block:: python

    def function_0():
        return None

  the terminal shows passing tests

refactor: make it better
#################################################################################

* Time to make a drill. You can change ``test_attribute_error_w_functions`` in the ``TestAttributeError`` class in ``tests/test_attribute_error.py`` to include calls to functions in ``module.py`` until you have one for ``module.function_99()``

  .. code-block:: python

    def test_attribute_error_w_functions(self):
        module.function_0()
        module.function_1()
        module.function_2()
        module.function_3()
        ...
        module.function_99()

  the terminal shows an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    AttributeError: module 'module' has no attribute 'function_1'

  add the solutions to ``module.py`` until all tests pass

*YOU DID IT AGAIN!* You now know

* how to solve a :ref:`ModuleNotFoundError`
* how to solve a NameError_
* how to solve a :ref:`TypeError` by defining a callable
* how to solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining variables
* how to solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining :doc:`/functions/functions`

----

.. _test_attribute_error_w_classes:

*********************************************************************************
test_attribute_error_w_classes
*********************************************************************************

I think of a :ref:`class <classes>` as a container of :ref:`attributes<AttributeError>` and :ref:`methods (functions) <functions>` that represents an object_

- attributes are names which represent something
- :ref:`methods<functions>` are :doc:`/functions/functions`, they

  * can take inputs if you want
  * return values and
  * are callable_

For example I can define a ``Human`` class with attributes like eye color, date of birth, height and weight. I can also define :ref:`methods<functions>` like age which returns a value based on the current year and date of birth attribute

.. _test_attribute_error_w_classes_red:

red: make it fail
#################################################################################

* I add a test function to the ``TestAttributeError`` class in ``tests/test_attribute_error.py``

  .. code-block:: python

    def test_attribute_error_w_classes(self):
        module.Class0()

  the terminal shows

  .. code-block:: python

    AttributeError: module 'module' has no attribute 'Class0'

.. _test_attribute_error_w_classes_green:

green: make it pass
#################################################################################

* I add a name to ``module.py``

  .. code-block:: python

    Class0 = None

  and the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  I had a similar issue earlier, what if I make ``Class0`` callable_ by changing the variable to a function using the def_ keyword in ``module.py``

  .. code-block:: python

    def Class0():
        return None

  The test passes! Something is odd here, what is the difference between :ref:`classes` and :doc:`/functions/functions`? Why am I writing a different set of tests for :ref:`classes` if the solutions are the same for :doc:`/functions/functions`?

  For now, I move on with these questions unanswered until they become obvious

.. _test_attribute_error_w_classes_refactor:

refactor: make it better
#################################################################################

* This could also be a drill, add lines to ``test_attribute_error_w_classes`` in the ``TestAttributeError`` class in ``tests/test_attribute_error.py`` until you have one for ``module.Class99()``, you will have 100 lines

  .. code-block:: python

    def test_attribute_error_w_classes(self):
        module.Class0()
        module.Class1()
        module.Class2()
        module.Class3()
        ...
        module.Class99()

  the terminal shows an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    AttributeError: module 'module' has no attribute 'Class1'

  add each solution to ``module.py`` until all the tests pass

*WELL DONE!* You now know

* how to solve a :ref:`ModuleNotFoundError`
* how to solve a NameError_
* how to solve a :ref:`TypeError` by defining a callable_
* how to solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining variables
* how to solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining :doc:`/functions/functions`
* how to solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining a :ref:`class <classes>`? do I know how to define :ref:`class <classes>` if I define them the same way I do :doc:`/functions/functions`?

----

.. _test_attribute_error_w_class_attributes:

*********************************************************************************
test_attribute_error_w_class_attributes
*********************************************************************************

.. _test_attribute_error_w_class_attributes_red:

red: make it fail
#################################################################################


* I add a new test to the ``TestAttributeError`` class in ``test_attribute_error.py``

  .. code-block:: python

    def test_attribute_error_w_class_attributes(self):
        module.Class.attribute_0

  the terminal shows an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    AttributeError: module 'module' has no attribute 'Class'

.. _test_attribute_error_w_class_attributes_green:

green: make it pass
#################################################################################

* I add a variable to ``module.py``

  .. code-block:: python

    Class = None

  and the terminal still shows an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ but with a different message

  .. code-block:: python

    AttributeError: 'NoneType' object has no attribute 'attribute_0'

  when I make the variable to a function

  .. code-block:: python

    def Class():
        return None

  the terminal shows an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ but with a slightly different message

  .. code-block:: python

    AttributeError: 'function' object has no attribute 'attribute_0'

* I wonder if it is possible to define an attribute in a function and access it from outside the function. I add an attribute to ``Class`` in ``module.py``

  .. code-block:: python

    def Class():
        attribute_0 = None
        return None

  the terminal still shows the same error, my guess was wrong

* what if I use the :ref:`class <classes>` keyword to define ``Class`` instead of def_?

  .. code-block:: python

    class Class():
        attribute_0 = None
        return None

  the terminal now shows a SyntaxError_

  .. code-block:: python

    E    return None
    E    ^^^^^^^^^^^
    E  SyntaxError: 'return' outside function

  the error is caused by the ``return`` statement being outside a :ref:`function<functions>`

* I add SyntaxError_ to the list of exceptions

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # NameError
    # TypeError
    # SyntaxError

* when I remove the `return statement`_

  .. code-block:: python

    class Class():
        attribute_0 = None

  the test passes. WOO HOO!

.. _test_attribute_error_w_class_attributes_refactor:

refactor: make it better
#################################################################################

* The current solution for ``test_attribute_error_w_classes`` was done by defining functions but the test name has ``defining_classes``, time to go back and change ``module.py`` using the :ref:`class <classes>` keyword instead of def_

  .. code-block:: python

    class Class0():
        pass
    ...
    class Class99():
        pass

  `pass <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ is a keyword used as a placeholder

* I now know how to properly define a :ref:`class <classes>` with an attribute. You can make a drill to practice by adding more lines to ``test_attribute_error_w_class_attributes`` until you have a total of 100 lines

  .. code-block:: python

    def test_attribute_error_w_class_attributes(self):
        module.Class.attribute_0
        module.Class.attribute_1
        module.Class.attribute_2
        module.Class.attribute_3
        ...
        module.Class.attribute_99

  the terminal shows

  .. code-block:: python

    AttributeError: type object 'Class' has no attribute 'attribute_1'

  add the solutions to ``module.py`` until all tests pass

*WELL DONE!* You now know You now know

* how to solve a :ref:`ModuleNotFoundError`
* how to solve a NameError_
* how to solve a :ref:`TypeError` by defining a callable_
* how to solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining variables
* how to solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining :doc:`/functions/functions`
* how to solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining a :ref:`class <classes>`
* how to solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining attributes (variables) in a :ref:`class <classes>`

----

.. _test_attribute_error_w_class_methods:

*********************************************************************************
test_attribute_error_w_class_methods
*********************************************************************************

.. _test_attribute_error_w_class_methods_red:

red: make it fail
#################################################################################
* I add a new test to the ``TestAttributeError`` class in ``test_attribute_error.py``

  .. code-block:: python

    def test_attribute_error_w_class_methods(self):
        module.Class.method_0()

  the terminal shows an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    AttributeError: type object 'Class' has no attribute 'method_0'

.. _test_attribute_error_w_class_methods_green:

green: make it pass
#################################################################################

* I add a name to ``Class`` in ``module.py``

  .. code-block:: python

    class Class():
        attribute_0 = None
        attribute_1 = None
        attribute_2 = None
        attribute_3 = None
        ...
        method_0 = None

  and the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* then I make ``method_0`` from an attribute to a :ref:`method<functions>` using the def_ keyword to make it callable_

  .. code-block:: python

    class Class():
    ...
        def method_0():
            return None

  and all tests pass. Fantastic!

.. _test_attribute_error_w_class_methods_refactor:

refactor: make it better
#################################################################################

You know the "drill", add more lines until there are 100 tests ending with one for ``module.Class.method_99()`` to ``test_attribute_error_w_class_methods`` in ``TestAttributeError`` in ``test_attribute_error.py``

.. code-block:: python

  def test_attribute_error_w_class_methods(self):
      module.Class.method_0()
      module.Class.method_1()
      module.Class.method_2()
      module.Class.method_3()
      ...
      module.Class.method_99()

repeat the solution until all tests pass

----

.. _AttributeError_review:

*********************************************************************************
review
*********************************************************************************

*CONGRATULATIONS!* you encountered the following exceptions

* :ref:`AssertionError`
* :ref:`ModuleNotFoundError`
* :ref:`AttributeError`
* NameError_
* :ref:`TypeError`
* SyntaxError_

and learned

* how to solve a :ref:`ModuleNotFoundError`
* how to solve a NameError_
* how to solve a :ref:`TypeError` by defining a callable_
* how to solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining variables
* how to solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining :doc:`/functions/functions`
* how to solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining a :ref:`class <classes>`
* how to solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining attributes (variables) in a :ref:`class <classes>`
* how to solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining :ref:`methods (functions) <functions>` in a :ref:`class <classes>`

:ref:`classes` vs :doc:`/functions/functions` in Python

-------------------------------------------------------

* :ref:`attributes<AttributeError>` and :ref:`methods<functions>` in a :ref:`class <classes>` can be accessible from outside the :ref:`class <classes>`
* attributes and :ref:`functions<functions>` in a :ref:`function<functions>` are not accessible from outside the :ref:`function<functions>`
* keywords used to define them - :ref:`class <classes>` vs def_
* naming conventions - ``CamelCase`` vs ``snake_case``
