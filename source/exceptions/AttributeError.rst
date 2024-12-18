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

An Attribute is a property, variable, function or name that belongs to an object_. For example when I describe a human being I can list attributes like height, weight, sex and color. The `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ is raised when there is a reference to a name in an object_ that does not exist.

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

* I open a terminal to run :ref:`makePythonTdd.sh` with ``attribute_error`` as the name of the project

  .. code-block:: python

    ./makePythonTdd.sh attribute_error

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 attribute_error

  it makes the folders and files that are needed, installs packages, runs the first test, and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_attribute_error.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click on ``tests/test_attribute_error.py:7`` with the mouse to open it in the editor
* then change ``True`` to ``False`` to make the test pass
* I add an `import statement`_

  .. code-block:: python

    import unittest
    import src.module

  and the terminal shows :ref:`ModuleNotFoundError`

  .. code-block:: python

    ModuleNotFoundError: No module named 'src.module'

  I add it to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError

  then open the ``src`` folder and rename ``attribute_error.py`` to ``module.py`` and the test passes

* I change ``test_failure`` to ``test_attribute_error_w_variables``

  .. code-block:: python

    class TestAttributeError(unittest.TestCase):

        def test_attribute_error_w_variables(self):
            src.module.variable_00

  I think of ``src.module.variable_00`` as an address for ``variable_00`` in ``module.py`` in the ``src`` folder, since the address does not exist the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    AttributeError: module 'src.module' has no attribute 'variable_00'

* I add the error to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError

* then add a name to ``module.py``

  .. code-block:: python

    variable_00

  and the terminal shows NameError_

  .. code-block::

    NameError: name 'variable_00' is not defined

  because ``variable_00`` in ``module.py`` is a reference to something that does not exist. I add NameError_ to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # NameError

* I point ``variable_00`` to :ref:`None`

  .. code-block:: python

    variable_00 = None

  and the terminal shows a passing test. I solved the `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining a variable

AttributeError vs NameError
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ is raised when there is a reference to a name that does not exist in an object_ that does exist, for example ``humans.wings``

NameError_ is raised when there is a reference to a name within an object_ and there is no definition for the name


refactor: make it better
#################################################################################

I can repeat the test as a drill to help remember it

* I add a failing line

  .. code-block:: python

    def test_attribute_error_w_variables(self):
        src.module.variable_00
        src.module.variable_01

  the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    AttributeError: module 'src.module' has no attribute 'variable_01'. Did you mean: 'variable_00'?

* I add the name to ``module.py``

  .. code-block:: python

    variable_00 = None
    variable_01

  the terminal shows NameError_

  .. code-block:: python

    NameError: name 'variable_01' is not defined

* I point it to :ref:`None`

  .. code-block:: python

    variable_00 = None
    variable_01 = None

  and the test passes

* I do it again

  .. code-block:: python

    def test_attribute_error_w_variables(self):
        src.module.variable_00
        src.module.variable_01
        src.module.variable_02

  the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    AttributeError: module 'src.module' has no attribute 'variable_02'. Did you mean: 'variable_00'?

* I add the name to ``module.py`` and point it to :ref:`None`

  .. code-block:: python

    variable_00 = None
    variable_01 = None
    variable_02 = None

  and the terminal shows green again

* One more time

  .. code-block:: python

    def test_attribute_error_w_variables(self):
        src.module.variable_00
        src.module.variable_01
        src.module.variable_02
        src.module.variable_03

  the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    AttributeError: module 'src.module' has no attribute 'variable_03'. Did you mean: 'variable_00'?

* I add the name and point it to :ref:`None`

  .. code-block:: python

    variable_00 = None
    variable_01 = None
    variable_02 = None
    variable_03 = None

  and the terminal shows a passing test

The test shows that I get `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ when the attribute does not exist and NameError_ when I add the name to the module without defining it

----

*********************************************************************************
test_attribute_error_w_functions
*********************************************************************************

red: make it fail
#################################################################################

I add a new test

.. code-block:: python

  def test_attribute_error_w_functions(self):
      src.module.function_00()

the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

.. code-block:: python

  AttributeError: module 'src.module' has no attribute 'function_00'

green: make it pass
#################################################################################

* I add the name and point it to :ref:`None`

  .. code-block:: python

    function_00 = None

  and get :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* I add it to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # NameError
    # TypeError

* When I make it a :ref:`function<functions>`

  .. code-block:: python

    def function_00():
        return None

  the terminal shows passing tests

refactor: make it better
#################################################################################

* Time to make it a drill

  .. code-block:: python

    def test_attribute_error_w_functions(self):
        src.module.function_00()
        src.module.function_01()
        src.module.function_02()
        src.module.function_03()

  the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    AttributeError: module 'src.module' has no attribute 'function_01'. Did you mean: 'function_00'?

  I add the :ref:`functions` to ``module.py`` until all tests pass

  .. code-block:: python

    def function_00():
        return None


    def function_01():
        return None


    def function_02():
        return None


    def function_03():
        return None

----

.. _test_attribute_error_w_classes:

*********************************************************************************
test_attribute_error_w_classes
*********************************************************************************

I think of a :ref:`class <classes>` as a container of :ref:`attributes<AttributeError>` and :ref:`methods (functions) <functions>` that represent an object_

- attributes are names which represent something
- :ref:`methods<functions>` are :doc:`/functions/functions`, they

  * can take inputs if you want
  * return values and
  * are callable_

For example I can define a ``Human`` class with attributes like eye color, date of birth, height and weight. I can also define :ref:`methods<functions>` like age which returns a value based on the current year and date of birth attribute

.. _test_attribute_error_w_classes_red:

red: make it fail
#################################################################################

* I add a failing test

  .. code-block:: python

    def test_attribute_error_w_classes(self):
        src.module.Class00()

  the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    AttributeError: module 'src.module' has no attribute 'Class00'

.. _test_attribute_error_w_classes_green:

green: make it pass
#################################################################################

* I add it as a :ref:`function<functions>` using the previous solution

  .. code-block:: python

    def Class00():
        return None

  The test passes! Something is odd here, what is the difference between :ref:`classes` and :doc:`/functions/functions`? Why am I writing a different set of tests for :ref:`classes` if the solutions are the same for :doc:`/functions/functions`?

  For now, I move on with these questions unanswered until they become obvious

.. _test_attribute_error_w_classes_refactor:

refactor: make it better
#################################################################################

* I make it a drill

  .. code-block:: python

    def test_attribute_error_w_classes(self):
        src.module.Class00()
        src.module.Class01()
        src.module.Class02()
        src.module.Class03()

  the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    AttributeError: module 'src.module' has no attribute 'Class01'. Did you mean: 'Class00'?

  I add each solution to ``module.py`` until all the tests pass

  .. code-block:: python

    def Class00():
        return None


    def Class01():
        return None


    def Class02():
        return None


    def Class03():
        return None

----

.. _test_attribute_error_w_class_attributes:

*********************************************************************************
test_attribute_error_w_class_attributes
*********************************************************************************

.. _test_attribute_error_w_class_attributes_red:

red: make it fail
#################################################################################


* I add a new test

  .. code-block:: python

    def test_attribute_error_w_class_attributes(self):
        src.module.Class.attribute_00

  the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    AttributeError: module 'src.module' has no attribute 'Class'. Did you mean: 'Class00'?

.. _test_attribute_error_w_class_attributes_green:

green: make it pass
#################################################################################

* I add it as a :ref:`function<functions>`

  .. code-block:: python

    def Class():
        return None

  the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    AttributeError: 'function' object has no attribute 'attribute_00'

* I try to define an attribute in a :ref:`function` and access it from outside

  .. code-block:: python

    def Class():
        attribute_00 = None
        return None

  and the terminal still shows the same error

* I use the :ref:`class <classes>` keyword to define it instead of def_?

  .. code-block:: python

    class Class():
        attribute_00 = None
        return None

  the terminal now shows SyntaxError_

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
        attribute_00 = None

  the test passes. WOO HOO!

.. _test_attribute_error_w_class_attributes_refactor:

refactor: make it better
#################################################################################

* The current solution for ``test_attribute_error_w_classes`` was done by defining :ref:`functions` but the test name has ``defining_classes``, time to go back and change ``module.py`` using the :ref:`class <classes>` keyword instead of def_

  .. code-block:: python

    class Class00():
        pass
    ...
    class Class04():
        pass

  `pass <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ is a keyword used as a placeholder

* I make it a drill to practice

  .. code-block:: python

    def test_attribute_error_w_class_attributes(self):
        src.module.Class.attribute_00
        src.module.Class.attribute_01
        src.module.Class.attribute_02
        src.module.Class.attribute_03

  the terminal shows

  .. code-block:: python

     AttributeError: type object 'Class' has no attribute 'attribute_01'. Did you mean: 'attribute_00'?

  I add the solutions to ``module.py`` until all tests pass

  .. code-block:: python

    class Class():

        attribute_00 = None
        attribute_01 = None
        attribute_02 = None
        attribute_03 = None

----

.. _test_attribute_error_w_class_methods:

*********************************************************************************
test_attribute_error_w_class_methods
*********************************************************************************

.. _test_attribute_error_w_class_methods_red:

red: make it fail
#################################################################################
* I add a new test

  .. code-block:: python

    def test_attribute_error_w_class_methods(self):
        src.module.Class.method_00()

  the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    AttributeError: type object 'Class' has no attribute 'method_00'

.. _test_attribute_error_w_class_methods_green:

green: make it pass
#################################################################################

* I add the name to ``Class`` and point it to :ref:`None`

  .. code-block:: python

    class Class():

        attribute_00 = None
        attribute_01 = None
        attribute_02 = None
        attribute_03 = None

        method_00 = None

  and the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* then I make it :ref:`method<functions>` by using the def_ keyword to make it callable_

  .. code-block:: python

    class Class():
    ...
        def method_00():
            return None

  and the tests passes

.. _test_attribute_error_w_class_methods_refactor:

refactor: make it better
#################################################################################

You know the "drill", I add more lines

.. code-block:: python

  def test_attribute_error_w_class_methods(self):
      src.module.Class.method_00()
      src.module.Class.method_01()
      src.module.Class.method_02()
      src.module.Class.method_03()

the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

.. code-block:: python

  AttributeError: type object 'Class' has no attribute 'method_01'. Did you mean: 'method_00'?

I repeat the solution until all tests pass

.. code-block:: python

  class Class():

      ...

      def method_00():
          return None

      def method_01():
          return None

      def method_02():
          return None

      def method_03():
          return None

----

*********************************************************************************
review
*********************************************************************************

I ran tests for `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ to show how to solve it by defining

* variables
* :ref:`functions`
* :ref:`classes <classes>`
* attributes (variables) in :ref:`classes <classes>`
* :ref:`methods (functions) <functions>` in :ref:`classes <classes>`

I also ran into the following Exceptions_

* :ref:`AssertionError`
* :ref:`ModuleNotFoundError`
* :ref:`AttributeError`
* NameError_
* :ref:`TypeError`
* SyntaxError_

Would you like to test the :ref:`TypeError`?

----

:doc:`/code/code_attribute_error`