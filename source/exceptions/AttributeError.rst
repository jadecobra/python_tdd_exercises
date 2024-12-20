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

An Attribute is a property, variable, function or name that belongs to an object_. For example when I describe a human being I can list attributes like height, weight, sex and color. The `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ is raised when there is a reference to a name that does not exist in an object_ that does exist.

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
    import src.attribute_error

* then change ``test_failure`` to ``test_attribute_error_w_variables``

  .. code-block:: python

    class TestAttributeError(unittest.TestCase):

        def test_attribute_error_w_variables(self):
            src.attribute_error.variable_00

  I think of ``src.attribute_error.variable_00`` as an address for ``variable_00`` in ``attribute_error.py`` in the ``src`` folder, since the address does not exist the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    AttributeError: module 'src.attribute_error' has no attribute 'variable_00'

* I add the error to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # AttributeError

* then add a name to ``attribute_error.py``

  .. code-block:: python

    variable_00

  and the terminal shows NameError_

  .. code-block::

    NameError: name 'variable_00' is not defined

  I add it to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # AttributeError
    # NameError

* I point ``variable_00`` to :ref:`None`

  .. code-block:: python

    variable_00 = None

refactor: make it better
#################################################################################

I can repeat the test as a drill to help remember it

* I add a failing line

  .. code-block:: python

    def test_attribute_error_w_variables(self):
        src.attribute_error.variable_00
        src.attribute_error.variable_01

  the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    AttributeError: module 'src.attribute_error' has no attribute 'variable_01'. Did you mean: 'variable_00'?

* I add the name to ``attribute_error.py``

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
        src.attribute_error.variable_00
        src.attribute_error.variable_01
        src.attribute_error.variable_02

  the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    AttributeError: module 'src.attribute_error' has no attribute 'variable_02'. Did you mean: 'variable_00'?

* I add the name to ``attribute_error.py`` and point it to :ref:`None`

  .. code-block:: python

    variable_00 = None
    variable_01 = None
    variable_02 = None

  and the terminal shows green again

* One more time

  .. code-block:: python

    def test_attribute_error_w_variables(self):
        src.attribute_error.variable_00
        src.attribute_error.variable_01
        src.attribute_error.variable_02
        src.attribute_error.variable_03

  the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    AttributeError: module 'src.attribute_error' has no attribute 'variable_03'. Did you mean: 'variable_00'?

* I add the name and point it to :ref:`None`

  .. code-block:: python

    variable_00 = None
    variable_01 = None
    variable_02 = None
    variable_03 = None

  and the terminal shows a passing test

The test shows that I get `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ when the attribute does not exist and NameError_ when I add the name to the :ref:`module <ModuleNotFoundError>` without defining it

----

*********************************************************************************
test_attribute_error_w_functions
*********************************************************************************

red: make it fail
#################################################################################

I add a new test

.. code-block:: python

  def test_attribute_error_w_functions(self):
      src.attribute_error.function_00()

the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

.. code-block:: python

  AttributeError: module 'src.attribute_error' has no attribute 'function_00'

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
        src.attribute_error.function_00()
        src.attribute_error.function_01()
        src.attribute_error.function_02()
        src.attribute_error.function_03()

  the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    AttributeError: module 'src.attribute_error' has no attribute 'function_01'. Did you mean: 'function_00'?

  I add the :ref:`functions` to ``attribute_error.py`` until all tests pass

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

*********************************************************************************
test_attribute_error_w_class_attributes
*********************************************************************************

attributes are variables defined inside a :ref:`class<classes>`

red: make it fail
#################################################################################


* I add a new test

  .. code-block:: python

    def test_attribute_error_w_class_attributes(self):
        src.attribute_error.Class.attribute_00

  the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    AttributeError: module 'src.attribute_error' has no attribute 'Class'. Did you mean: 'Class00'?

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

* I try to define a variable in the :ref:`function <functions>` and access it from outside

  .. code-block:: python

    def Class():
        attribute_00 = None
        return None

  and the terminal still shows the same error

* I use the :ref:`class <classes>` keyword it instead of the def_ keyword?

  .. code-block:: python

    class Class():
        attribute_00 = None
        return None

  and the terminal now shows SyntaxError_

  .. code-block:: python

    E    return None
    E    ^^^^^^^^^^^
    E  SyntaxError: 'return' outside function

* I add it to the list of Exceptions_

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # AttributeError
    # NameError
    # TypeError
    # SyntaxError

* then remove the `return statement`_

  .. code-block:: python

    class Class():
        attribute_00 = None

  and the test passes

refactor: make it better
#################################################################################

* I make it a drill

  .. code-block:: python

    def test_attribute_error_w_class_attributes(self):
        src.attribute_error.Class.attribute_00
        src.attribute_error.Class.attribute_01
        src.attribute_error.Class.attribute_02
        src.attribute_error.Class.attribute_03

  and the terminal shows

  .. code-block:: python

     AttributeError: type object 'Class' has no attribute 'attribute_01'. Did you mean: 'attribute_00'?

  I add the attributes to ``attribute_error.py`` until all tests pass

  .. code-block:: python

    class Class():

        attribute_00 = None
        attribute_01 = None
        attribute_02 = None
        attribute_03 = None

----

*********************************************************************************
test_attribute_error_w_class_methods
*********************************************************************************

:ref:`methods <functions>` are :ref:`functions` defined inside a :ref:`class<classes>`

red: make it fail
#################################################################################
* I add a new test

  .. code-block:: python

    def test_attribute_error_w_class_methods(self):
        src.attribute_error.Class.method_00()

  the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    AttributeError: type object 'Class' has no attribute 'method_00'


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
      src.attribute_error.Class.method_00()
      src.attribute_error.Class.method_01()
      src.attribute_error.Class.method_02()
      src.attribute_error.Class.method_03()

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
* :ref:`AttributeError`
* NameError_
* :ref:`TypeError`
* SyntaxError_

Would you like to test the :ref:`TypeError?<TypeError>`

----

:doc:`/code/code_attribute_error`