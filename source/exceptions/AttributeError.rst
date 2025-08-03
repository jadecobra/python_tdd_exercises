.. include:: ../links.rst

#################################################################################
AttributeError
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/4-KGDO3zMYk?si=TdPbniUMkoz0M7CI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

.. contents:: table of contents
  :local:
  :depth: 1

----

The `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ is raised when there is a reference to a name that is NOT in an :ref:`object<classes>` that exists. An attribute is a name for something that belongs to an :ref:`object<classes>`, for example, a human being has attributes like height, weight, sex and color.

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

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and use the mouse to click on ``tests/test_attribute_error.py:7`` to open it in the editor
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

  I think of ``src.attribute_error.variable_00`` as an address for ``variable_00`` in ``attribute_error.py`` in the ``src`` folder, since the file is empty, the variable is not in it and the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    AttributeError: module 'src.attribute_error' has no attribute 'variable_00'

* I add the error to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # AttributeError

green: make it pass
#################################################################################

* then I add a name to ``attribute_error.py``

  .. code-block:: python

    variable_00

  which gives me NameError_

  .. code-block::

    NameError: name 'variable_00' is not defined

* I add it to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # AttributeError
    # NameError

* and point ``variable_00`` to :ref:`None`

  .. code-block:: python

    variable_00 = None

  the test passes

refactor: make it better
#################################################################################

* I do it a few more times as a drill

  .. code-block:: python

    def test_attribute_error_w_variables(self):
        src.attribute_error.variable_00
        src.attribute_error.variable_01

  the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python
    :force:

    AttributeError: module 'src.attribute_error' has no attribute 'variable_01'. Did you mean: 'variable_00'?

  I add the name to ``attribute_error.py``

  .. code-block:: python

    variable_00 = None
    variable_01

  and get NameError_

  .. code-block:: python

    NameError: name 'variable_01' is not defined

  I point it to :ref:`None`

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
    :force:

    AttributeError: module 'src.attribute_error' has no attribute 'variable_02'. Did you mean: 'variable_00'?

  I add the name and point it to :ref:`None`

  .. code-block:: python

    variable_00 = None
    variable_01 = None
    variable_02 = None

  and the terminal shows green again

* one more time

  .. code-block:: python

    def test_attribute_error_w_variables(self):
        src.attribute_error.variable_00
        src.attribute_error.variable_01
        src.attribute_error.variable_02
        src.attribute_error.variable_03

  the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python
    :force:

    AttributeError: module 'src.attribute_error' has no attribute 'variable_03'. Did you mean: 'variable_00'?

  I add it to the file

  .. code-block:: python

    variable_00 = None
    variable_01 = None
    variable_02 = None
    variable_03 = None

  and the test passes

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

    variable_00 = None
    variable_01 = None
    variable_02 = None
    variable_03 = None


    function_00 = None

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* which I add to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # AttributeError
    # NameError
    # TypeError

* when I make it a :ref:`function<functions>`

  .. code-block:: python

    variable_00 = None
    variable_01 = None
    variable_02 = None
    variable_03 = None


    def function_00():
        return None

  the test passes

refactor: make it better
#################################################################################

* time to do it as a drill

  .. code-block:: python

    def test_attribute_error_w_functions(self):
        src.attribute_error.function_00()
        src.attribute_error.function_01()

  the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python
    :force:

    AttributeError: module 'src.attribute_error' has no attribute 'function_01'. Did you mean: 'function_00'?

  I add the :ref:`function<functions>` to ``attribute_error.py``

  .. code-block:: python

    def function_00():
        return None


    def function_01():
        return None

  and the test passes

* I add another line

  .. code-block:: python

    def test_attribute_error_w_functions(self):
        src.attribute_error.function_00()
        src.attribute_error.function_01()
        src.attribute_error.function_02()

  the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python
    :force:

    AttributeError: module 'src.attribute_error' has no attribute 'function_02'. Did you mean: 'function_00'?

  I make the test pass

  .. code-block:: python

    def function_00():
        return None


    def function_01():
        return None


    def function_02():
        return None

* then I add another line

  .. code-block:: python

    def test_attribute_error_w_functions(self):
        src.attribute_error.function_00()
        src.attribute_error.function_01()
        src.attribute_error.function_02()
        src.attribute_error.function_03()

  the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python
    :force:

    AttributeError: module 'src.attribute_error' has no attribute 'function_03'. Did you mean: 'function_00'?

  I add it to the :ref:`module<ModuleNotFoundError>`

  .. code-block:: python

    def function_00():
        return None


    def function_01():
        return None


    def function_02():
        return None


    def function_03():
        return None

  and the test passes

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
        src.attribute_error.AClass.attribute_00

  the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    AttributeError: module 'src.attribute_error' has no attribute 'AClass'

green: make it pass
#################################################################################

* I add it as a :ref:`function<functions>`

  .. code-block:: python

    def function_00():
        return None


    def function_01():
        return None


    def function_02():
        return None


    def function_03():
        return None


    def AClass():
        return None

  and the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    AttributeError: 'function' object has no attribute 'attribute_00'

* I define a variable in the :ref:`function <functions>`

  .. code-block:: python

    def AClass():

        attribute_00 = None
        return None

  and the terminal still shows the same Exception_ because I cannot access a variable that belongs to a :ref:`function<functions>` from outside of it

* I change the def_ keyword to the :ref:`class <classes>` keyword

  .. code-block:: python

    class AClass():

        attribute_00 = None
        return None

  and the terminal shows SyntaxError_

  .. code-block:: python

    E    return None
    E    ^^^^^^^^^^^
    E  SyntaxError: 'return' outside function

* I add it to the list of Exceptions_ Encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # AttributeError
    # NameError
    # TypeError
    # SyntaxError

* then remove the `return statement`_ since ``AClass`` is no longer a :ref:`function<functions>`

  .. code-block:: python

    class AClass():
        attribute_00 = None

  and the test passes

refactor: make it better
#################################################################################

* I add another line

  .. code-block:: python

    def test_attribute_error_w_class_attributes(self):
        src.attribute_error.AClass.attribute_00
        src.attribute_error.AClass.attribute_01

  and the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python
    :force:

    AttributeError: type object 'AClass' has no attribute 'attribute_01'. Did you mean: 'attribute_00'?

  I add the name to the :ref:`class<classes>` definition

  .. code-block:: python

    class AClass():

        attribute_00 = None
        attribute_01 = None

  and the test passes

* I do it again

  .. code-block:: python

    def test_attribute_error_w_class_attributes(self):
        src.attribute_error.AClass.attribute_00
        src.attribute_error.AClass.attribute_01
        src.attribute_error.AClass.attribute_02

  the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python
    :force:

     AttributeError: type object 'AClass' has no attribute 'attribute_02'. Did you mean: 'attribute_00'?

  I make the test pass

  .. code-block:: python

    class AClass():

        attribute_00 = None
        attribute_01 = None
        attribute_02 = None

* then add one more line

  .. code-block:: python

    def test_attribute_error_w_class_attributes(self):
        src.attribute_error.AClass.attribute_00
        src.attribute_error.AClass.attribute_01
        src.attribute_error.AClass.attribute_02
        src.attribute_error.AClass.attribute_03

  and the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python
    :force:

     AttributeError: type object 'AClass' has no attribute 'attribute_03'. Did you mean: 'attribute_00'?

  I add the name

  .. code-block:: python

    class AClass():

        attribute_00 = None
        attribute_01 = None
        attribute_02 = None
        attribute_03 = None

  and the terminal shows passing tests

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
        src.attribute_error.AClass.method_00()

  the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    AttributeError: type object 'AClass' has no attribute 'method_00'


green: make it pass
#################################################################################

* I add the name to ``AClass`` and point it to :ref:`None`

  .. code-block:: python

    class AClass():

        attribute_00 = None
        attribute_01 = None
        attribute_02 = None
        attribute_03 = None

        method_00 = None

  and the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* I make it a :ref:`method<functions>` by using the def_ keyword to make it callable_

  .. code-block:: python

    class AClass():

        attribute_00 = None
        attribute_01 = None
        attribute_02 = None
        attribute_03 = None

        def method_00():
            return None

  and the test passes

refactor: make it better
#################################################################################

* You know the "drill", I add a new line

  .. code-block:: python

    def test_attribute_error_w_class_methods(self):
        src.attribute_error.AClass.method_00()
        src.attribute_error.AClass.method_01()

  the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python
    :force:

    AttributeError: type object 'AClass' has no attribute 'method_01'. Did you mean: 'method_00'?

  I add a definition for it

  .. code-block:: python

    class AClass():

        ...

        def method_00():
            return None

        def method_01():
            return None

  and the terminal shows green again

* I add another line

  .. code-block:: python

    def test_attribute_error_w_class_methods(self):
        src.attribute_error.AClass.method_00()
        src.attribute_error.AClass.method_01()
        src.attribute_error.AClass.method_02()

  the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python
    :force:

    AttributeError: type object 'AClass' has no attribute 'method_02'. Did you mean: 'method_00'?

  I repeat the solution

  .. code-block:: python

    class AClass():

        ...

        def method_00():
            return None

        def method_01():
            return None

        def method_02():
            return None

  the test passes

* then I add the last line

  .. code-block:: python

    def test_attribute_error_w_class_methods(self):
        src.attribute_error.AClass.method_00()
        src.attribute_error.AClass.method_01()
        src.attribute_error.AClass.method_02()
        src.attribute_error.AClass.method_03()

  and the terminal shows `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python
    :force:

    AttributeError: type object 'AClass' has no attribute 'method_03'. Did you mean: 'method_00'?

  I make the test pass

  .. code-block:: python

    class AClass():

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

I ran tests for the `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ with

* variables
* :ref:`functions`
* :ref:`class<classes>` attributes (variables)
* :ref:`class<classes>` :ref:`methods<functions>` (functions)

I also ran into the following Exceptions_

* :ref:`AssertionError`
* NameError_
* :ref:`TypeError`
* SyntaxError_

Would you like to test the :ref:`TypeError?<TypeError>`

----

:doc:`/code/code_attribute_error`