.. meta::
  :description: Getting an AttributeError in Python? Learn to fix the common 'NoneType' object and other attribute errors with our step-by-step guide and video tutorial.
  :keywords: Jacob Itegboje, python attributeerror 'NoneType' object has no attribute, how to fix attributeerror in python, python 'int' object has no attribute 'append', python attributeerror 'str' object has no attribute, AttributeError: 'list' object has no attribute 'add', python check if attribute exists before access, python debug AttributeError in class, python common causes of AttributeError, AttributeError vs TypeError in Python

.. include:: ../links.rst

.. _AttributeError: https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError

#################################################################################
AttributeError
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/4-KGDO3zMYk?si=TdPbniUMkoz0M7CI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

AttributeError_ is raised when there is a reference to a name that is NOT in an :ref:`object<classes>` that exists.

An :ref:`attribute<AttributeError>` is a name for something that belongs to an :ref:`object<classes>`, for example, a human being has attributes like height, weight, sex and color. They are also known as properties

----

*********************************************************************************
requirements
*********************************************************************************

* I open a terminal_ to run :ref:`makePythonTdd.sh` with ``attribute_error`` as the name of the project

  .. code-block:: python
    :emphasize-lines: 1

    ./makePythonTdd.sh attribute_error

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1` instead of :ref:`makePythonTdd.sh`

    .. code-block:: python

      ./makePythonTdd.ps1 attribute_error

  it makes the folders_ and files_ that are needed, installs packages_, runs the first test, and the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_attribute_error.py:7: AssertionError

* I hold ``ctrl`` (Windows_/Linux_) or ``option or command`` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_attribute_error.py:7`` to open it in the :ref:`editor<2 editors>`
* then I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` to make the test pass

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

* I change the name of the :ref:`class<classes>` to match the :ref:`CapWords` format to follow Python_ :ref:`convention<conventions>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 1

    class TestAttributeError(unittest.TestCase):

*********************************************************************************
test_attribute_error_w_variables
*********************************************************************************

RED: make it fail
#################################################################################

* I add an `import statement`_ at the top of  ``test_attribute_error.py``

  .. code-block:: python
    :linenos:

    import unittest
    import src.attribute_error

* I change ``test_failure`` to ``test_attribute_error_w_variables``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3-4

    class TestAttributeError(unittest.TestCase):

        def test_attribute_error_w_variables(self):
            src.attribute_error.variable_00


    # Exceptions Encountered

  I think of ``src.attribute_error.variable_00`` as an address for ``variable_00`` in ``attribute_error.py`` which is in the ``src`` folder. Since the file is empty, the variable_ is not in it.

  The terminal_ shows AttributeError_

  .. code-block:: shell

    AttributeError: module 'src.attribute_error' has no attribute 'variable_00'

* I add the error to the list of :ref:`Exceptions<errors>` encountered in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3

    # Exceptions Encountered
    # AssertionError
    # AttributeError

GREEN: make it pass
#################################################################################

* I click on ``attribute_error.py`` in the ``src`` folder_ to open it in the :ref:`editor<2 editors>` of my `Integrated Development Environment (IDE)`_, then I add a name

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    variable_00

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'variable_00' is not defined

* I add it to the list of :ref:`Exceptions<errors>` encountered in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 4

    # Exceptions Encountered
    # AssertionError
    # AttributeError
    # NameError

* I point ``variable_00`` to :ref:`None` in ``attribute_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    variable_00 = None

  the test passes. ``variable_00`` is now an attribute/property of ``attribute_error.py`` which is in the ``src`` folder_ and I can reach it by using ``src.attribute_error.variable_00``

REFACTOR: make it better
#################################################################################

* I do the same test a few more times as a drill in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 3

        def test_attribute_error_w_variables(self):
            src.attribute_error.variable_00
            src.attribute_error.variable_01

  the terminal_ shows AttributeError_

  .. code-block:: shell

    AttributeError: module 'src.attribute_error' has no attribute 'variable_01'. Did you mean: 'variable_00'?

* I add the name to ``attribute_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    variable_00 = None
    variable_01

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'variable_01' is not defined

  I point it to :ref:`None`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    variable_00 = None
    variable_01 = None

  the test passes

* I another statement to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4

        def test_attribute_error_w_variables(self):
            src.attribute_error.variable_00
            src.attribute_error.variable_01
            src.attribute_error.variable_02

  the terminal_ shows AttributeError_

  .. code-block:: shell
    :force:

    AttributeError: module 'src.attribute_error' has no attribute 'variable_02'. Did you mean: 'variable_00'?

* I add the name and point it to :ref:`None`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    variable_00 = None
    variable_01 = None
    variable_02 = None

  the test passes

* one more line in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 5


        def test_attribute_error_w_variables(self):
            src.attribute_error.variable_00
            src.attribute_error.variable_01
            src.attribute_error.variable_02
            src.attribute_error.variable_03

  the terminal_ shows AttributeError_

  .. code-block:: shell

    AttributeError: module 'src.attribute_error' has no attribute 'variable_03'. Did you mean: 'variable_00'?

* I add the attribute to ``attribute_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4

    variable_00 = None
    variable_01 = None
    variable_02 = None
    variable_03 = None

  the test passes

A variable_ in a :ref:`module<ModuleNotFoundError>` is an attribute of the :ref:`module<ModuleNotFoundError>`

----

*********************************************************************************
test_attribute_error_w_functions
*********************************************************************************

RED: make it fail
#################################################################################

I add a new test to ``test_attribute_error.py``

.. code-block:: python
  :lineno-start: 11
  :emphasize-lines: 3-4

          src.attribute_error.variable_03

      def test_attribute_error_w_functions(self):
          src.attribute_error.function_00()


  # Exceptions Encountered

the terminal_ shows AttributeError_

.. code-block:: shell

  AttributeError: module 'src.attribute_error' has no attribute 'function_00'

GREEN: make it pass
#################################################################################

* I add the name and point it to :ref:`None` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 4

    variable_03 = None


    function_00 = None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

* I add it to the list of :ref:`Exceptions<errors>` encountered in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 5

    # Exceptions Encountered
    # AssertionError
    # AttributeError
    # NameError
    # TypeError

* I change the attribute to a :ref:`function<functions>` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 4-5

    variable_03 = None


    def function_00():
        return None

  the test passes. ``function_00`` is now an attribute/property of ``attribute_error.py`` which is in the ``src`` folder_ and I can call it by using ``src.attribute_error.function_00()``

REFACTOR: make it better
#################################################################################

* time to do it as a drill, I add another call in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

        def test_attribute_error_w_functions(self):
            src.attribute_error.function_00()
            src.attribute_error.function_01()

  the terminal_ shows AttributeError_

  .. code-block:: shell

    AttributeError: module 'src.attribute_error' has no attribute 'function_01'. Did you mean: 'function_00'?

* I add the :ref:`function<functions>` to ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 5-6

    def function_00():
        return None


    def function_01():
        return None

  the test passes

* I add another line to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 13

        def test_attribute_error_w_functions(self):
            src.attribute_error.function_00()
            src.attribute_error.function_01()
            src.attribute_error.function_02()

  the terminal_ shows AttributeError_

  .. code-block:: shell

    AttributeError: module 'src.attribute_error' has no attribute 'function_02'. Did you mean: 'function_00'?

* I add a :ref:`function<functions>` for it in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 5-6

    def function_01():
        return None


    def function_02():
        return None

  the test passes

* then I add another line in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 5

        def test_attribute_error_w_functions(self):
            src.attribute_error.function_00()
            src.attribute_error.function_01()
            src.attribute_error.function_02()
            src.attribute_error.function_03()


    # Exceptions Encountered

  the terminal_ shows AttributeError_

  .. code-block:: shell

    AttributeError: module 'src.attribute_error' has no attribute 'function_03'. Did you mean: 'function_00'?

* I add it the :ref:`function<functions>` to ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 5-6

    def function_02():
        return None


    def function_03():
        return None

  the test passes

A :ref:`function<functions>` in a :ref:`module<ModuleNotFoundError>` is an attribute of the :ref:`module<ModuleNotFoundError>`

----

*********************************************************************************
test_attribute_error_w_class_attributes
*********************************************************************************

We know that variables_ and :ref:`functions` defined in a :ref:`module<ModuleNotFoundError>` are attributes. variables_ defined inside a :ref:`class<classes>` are also attributes.

RED: make it fail
#################################################################################

I add a new test to ``test_attribute_error.py``

.. code-block:: python

          src.attribute_error.function_03()

      def test_attribute_error_w_class_attributes(self):
          src.attribute_error.AClass.attribute_00


  # Exceptions Encountered

the terminal_ shows AttributeError_

.. code-block:: shell

  AttributeError: module 'src.attribute_error' has no attribute 'AClass'

GREEN: make it pass
#################################################################################

* I add a :ref:`function<functions>` to ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 5-6

    def function_03():
        return None


    def AClass():
        return None

  the terminal_ shows AttributeError_

  .. code-block:: shell

    AttributeError: 'function' object has no attribute 'attribute_00'

* I define a variable_ inside the :ref:`function <functions>`

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 3-4

    def AClass():

        attribute_00 = None
        return None

  the terminal_ still shows the same :ref:`Exception<errors>` because I cannot access a variable_ that belongs to a :ref:`function<functions>` from outside of the :ref:`function<functions>`

* I use the :ref:`class<classes>` keyword instead of the def_ keyword to make ``AClass`` a :ref:`class<classes>`

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 1

    class AClass():

        attribute_00 = None
        return None

  the terminal_ shows SyntaxError_

  .. code-block:: python

    E    return None
    E    ^^^^^^^^^^^
    E  SyntaxError: 'return' outside function

* I add it to the list of :ref:`Exceptions<errors>` encountered in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 6

    # Exceptions Encountered
    # AssertionError
    # AttributeError
    # NameError
    # TypeError
    # SyntaxError

* I remove the `return statement`_ from ``AClass`` in ``attribute_error.py`` since it is no longer a :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 23

    class AClass():
        attribute_00 = None

  the test passes. ``attribute_00`` is now an attribute/property of ``AClass`` which is an attribute/property of ``attribute_error.py`` which is in the ``src`` folder_ and I can reach it by using ``src.attribute_error.AClass.attribute_00()``

REFACTOR: make it better
#################################################################################

* I add another failing line to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 3

        def test_attribute_error_w_class_attributes(self):
            src.attribute_error.AClass.attribute_00
            src.attribute_error.AClass.attribute_01

  the terminal_ shows AttributeError_

  .. code-block:: shell

    AttributeError: type object 'AClass' has no attribute 'attribute_01'. Did you mean: 'attribute_00'?

* I add the name to the :ref:`class<classes>` definition in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 4

    class AClass():

        attribute_00 = None
        attribute_01 = None

  the test passes

* I add another line to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 4

        def test_attribute_error_w_class_attributes(self):
            src.attribute_error.AClass.attribute_00
            src.attribute_error.AClass.attribute_01
            src.attribute_error.AClass.attribute_02

  the terminal_ shows AttributeError_

  .. code-block:: shell

     AttributeError: type object 'AClass' has no attribute 'attribute_02'. Did you mean: 'attribute_00'?

* I add the attribute to ``AClass`` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 5

    class AClass():

        attribute_00 = None
        attribute_01 = None
        attribute_02 = None

  the test passes

* I add another line to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 5

        def test_attribute_error_w_class_attributes(self):
            src.attribute_error.AClass.attribute_00
            src.attribute_error.AClass.attribute_01
            src.attribute_error.AClass.attribute_02
            src.attribute_error.AClass.attribute_03


    # Exceptions Encountered

  the terminal_ shows AttributeError_

  .. code-block:: shell

    AttributeError: type object 'AClass' has no attribute 'attribute_03'. Did you mean: 'attribute_00'?

* I add the name to ``AClass`` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 6

    class AClass():

        attribute_00 = None
        attribute_01 = None
        attribute_02 = None
        attribute_03 = None

  the test passes

* A variable_ in a :ref:`class<classes>` in a :ref:`module<ModuleNotFoundError>` is an attribute of the :ref:`class<classes>`.
* A :ref:`class<classes>` in a :ref:`module<ModuleNotFoundError>` is an attribute of the :ref:`module<ModuleNotFoundError>`

----

*********************************************************************************
test_attribute_error_w_class_methods
*********************************************************************************

We know that variables_, :ref:`functions` and :ref:`classes` defined in a :ref:`module<ModuleNotFoundError>` are attributes. We also know that variables_ defined inside a :ref:`class<classes>` are attributes.

:ref:`functions<functions>` defined inside a :ref:`class<classes>` are also attributes, they are known as :ref:`methods<functions>`

RED: make it fail
#################################################################################

* I add a new test to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 3-4

            src.attribute_error.AClass.attribute_03

        def test_attribute_error_w_class_methods(self):
            src.attribute_error.AClass.method_00()


    # Exceptions Encountered

  the terminal_ shows AttributeError_

  .. code-block:: shell

    AttributeError: type object 'AClass' has no attribute 'method_00'

GREEN: make it pass
#################################################################################

* I add the name to ``AClass`` and point it to :ref:`None` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 8

    class AClass():

        attribute_00 = None
        attribute_01 = None
        attribute_02 = None
        attribute_03 = None

        method_00 = None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

* I make it a :ref:`method<functions>` by using the def_ keyword

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 3-4

        attribute_03 = None

        def method_00():
            return None

  the test passes. ``method_00`` is now an attribute/property of ``AClass`` which is an attribute/property of ``attribute_error.py`` which is in the ``src`` folder_ and I can reach it by using ``src.attribute_error.AClass.method_00()``

REFACTOR: make it better
#################################################################################

* You know the "drill", I add a new failing line to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 3

        def test_attribute_error_w_class_methods(self):
            src.attribute_error.AClass.method_00()
            src.attribute_error.AClass.method_01()

  the terminal_ shows AttributeError_

  .. code-block:: shell

    AttributeError: type object 'AClass' has no attribute 'method_01'. Did you mean: 'method_00'?

* I add a definition for it in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 4-5

        def method_00():
            return None

        def method_01():
            return None

  the terminal_ shows green again

* I add another failing line to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 4

        def test_attribute_error_w_class_methods(self):
            src.attribute_error.AClass.method_00()
            src.attribute_error.AClass.method_01()
            src.attribute_error.AClass.method_02()

  the terminal_ shows AttributeError_

  .. code-block:: shell

    AttributeError: type object 'AClass' has no attribute 'method_02'. Did you mean: 'method_00'?

* I add the :ref:`method<functions>` to ``AClass`` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 4-5

        def method_01():
            return None

        def method_02():
            return None

  the test passes

* I add the last line to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 5

        def test_attribute_error_w_class_methods(self):
            src.attribute_error.AClass.method_00()
            src.attribute_error.AClass.method_01()
            src.attribute_error.AClass.method_02()
            src.attribute_error.AClass.method_03()


    # Exceptions Encountered

  the terminal_ shows AttributeError_

  .. code-block:: shell

    AttributeError: type object 'AClass' has no attribute 'method_03'. Did you mean: 'method_00'?

* I add the :ref:`method<functions>` to ``AClass`` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 4-5

        def method_02():
            return None

        def method_03():
            return None

  the test passes

* A :ref:`function<functions>` in a :ref:`class<classes>` is called a :ref:`method<functions>` and is an attribute of the :ref:`class<classes>`
* A :ref:`class<classes>` in a :ref:`module<ModuleNotFoundError>` is an attribute of the :ref:`module<ModuleNotFoundError>`

----

*********************************************************************************
review
*********************************************************************************

I ran tests for AttributeError_ with

* :ref:`variables<test_attribute_error_w_variables>`
* :ref:`functions<test_attribute_error_w_functions>`
* :ref:`variables in classes aka class attributes<test_attribute_error_w_class_attributes>`
* :ref:`functions in classes aka methods<test_attribute_error_w_class_methods>`

I also ran into the following :ref:`Exceptions<errors>`

* :ref:`AssertionError`
* :ref:`NameError<test_catching_name_error_in_tests>`
* :ref:`TypeError` and
* SyntaxError_

:ref:`can we measure learning?`

----

:ref:`Click here to see the code I typed in this chapter<AttributeError: tests and solutions>`

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">Click Here to leave a 5 star review on TrustPilot, if you found this helpful</a>
  </div>
  <!-- End TrustBox widget -->