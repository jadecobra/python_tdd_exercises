AttributeError
==============

Our exploration of python using Test Driven Development continues in this chapter with the ``AttributeError``

Prerequisites
-------------


* `How I setup a Test Driven Development Environment <./How I setup a Test Driven Development Environment.rst>`_


What is an Attribute?
---------------------

An Attribute is a property, variable, function or name that belongs to an ``object``. For example, if we describe a human being we could list attributes like height, weight, sex and color.
An ``AttributeError`` is raised when there is a reference to a name in an ``object`` that does not exist.


----

Solve AttributeError by defining a Variable
-------------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

We open a new file, save it as ``test_attribute_error.py`` in the ``tests`` folder created in `How I setup a Test Driven Development Environment <./How I setup a Test Driven Development Environment.rst>`_ and type the following

.. code-block:: python

   import unittest
   import module


   class TestAttributeErrors(unittest.TestCase):

       def test_defining_variables_to_solve_attribute_errors(self):
           self.assertIsNone(module.variable_0)

What does the code above mean?


* ``import unittest`` imports the ``unittest`` module from the python standard library
* ``import module`` imports the ``module`` module - this is going to hold the solution we write
* ``class TestAttributeErrors(unittest.TestCase):`` - a class definition that inherits from ``unittest.TestCase`` and will hold our tests. We learn more about this in `Classes <./classes.rst>`_
* ``def test_defining_variables_to_solve_attribute_errors(self):`` the definition of our first test function to find out if defining variables can solve an ``AttributeError``
* ``self.assertIsNone(module.variable_0)`` - the actual test. This is equivalent to asking the question ``is module.variable_0 equal to None``
* ``assertIsNone`` is one of the helper functions inherited from ``unittest.TestCase``. We learn more about this in `AssertionError <./AssertionError.rst>`_
* ``self`` refers to the ``TestAttributeError`` class

If you left ``pytest-watch`` running from `How I setup a Test Driven Development Environment <./How I setup a Test Driven Development Environment.rst>`_ you should see a message similar to the following in the terminal

.. code-block:: python

   ImportError while importing test module '/<PATH_TO_PROJECT_NAME>/{PROJECT_NAME}/tests/test_attribute_error.py'.
   Hint: make sure your test modules/packages have valid python names.
   Traceback:
   ...
   tests/test_attribute_error.py:2: in <module>
       import module
   E   ModuleNotFoundError: No module named 'module'

We practice solving this error in `ModuleNotFoundError <./ModuleNotFoundError.rst>`_

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* we update the running list of exceptions encountered

  .. code-block:: python

       # Exceptions Encountered
       # AssertionError
       # ModuleNotFoundError

* create ``module.py`` in the ``{PROJECT_NAME}`` folder and the terminal will update to show the following

  .. code-block:: python

       self = <tests.test_attribute_error.TestAttributeError testMethod=test_defining_variables_to_solve_attribute_errors>

           def test_defining_variables_to_solve_attribute_errors(self):
       >       self.assertIsNone(module.variable_0)
       E       AttributeError: module 'module' has no attribute 'variable_0'

  Looking at the traceback starting from the bottom


  * ``tests/test_attribute_error.py:7: AttributeError`` the location i.e. filename and line number and name of the Exception that is raised
  * ``E       AttributeError: module 'module' has no attribute 'variable_0'`` an explanation of the error raised. The module we imported has no definitions named ``variable_0``. We update our list of exceptions encountered

    .. code-block:: python

         # Exceptions Encountered
         # AssertionError
         # ModuleNotFoundError
         # AttributeError

  * ``>       self.assertIsNone(module.variable_0)`` the line of code that caused the error. As seen from the error explanation above the file ``module.py`` has no definitions named ``variable_0``. This is like making a phone call to a number that is not in service or sending an e-mail to an address that does not exist
  * ``def test_defining_variables_to_solve_attribute_errors(self):`` the function definition where the error occurs
  * ``self = <tests.test_attribute_error.TestAttributeError testMethod=test_defining_variables_to_solve_attribute_errors>`` - A reference to the class and method(function) where the failure occurred

* edit ``module.py`` with a name

  .. code-block:: python

      variable_0

  The terminal will update to show the following

  .. code-block::

       tests/test_attribute_error.py:2: in <module>
           import module
       module.py:1: in <module>
           variable_0
       E   NameError: name 'variable_0' is not defined

  Looking at the traceback going from the bottom upwards

  * ``E   NameError: name 'variable_0' is not defined`` this is a new error, we add it to our running list of errors encountered. The running list of exceptions encountered is now

    .. code-block::

        # Exceptions Encountered
        # AssertionError
        # ModuleNotFoundError
        # AttributeError
        # NameError

  * ``variable_0`` the offending line
  * ``module.py:1: in <module>`` the location of the offending line

* update the failing line in ``module.py`` in the Interactive Development Environment(IDE) to fix it

  .. code-block:: python

      variable_0 = None

  this explicity defines ``variable_0`` with a value of ``None`` and the terminal updates to show a passing test. YES!

  .. code-block:: python

      collected 2 items

      tests/test_attribute_error.py .                                             [ 50%]
      tests/test_{PROJECT_NAME}.py .                                              [100%]

      ============================== 2 passed in 0.03s==================================

What is similar? What is different?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An ``AttributeError`` occurs when there is a reference to a name in an object from outside the object and the name does not exist e.g. ``humans.wings`` while a ``NameError`` occurs when there is a reference to a name within an object and there is no prior definition of the name e.g. ``wings``

What is similar between ``ModuleNotFoundError``, ``AttributeError`` and ``NameError``?

.. NOTE::

  In python ``=`` is used to assign names to objects, for example ``five = 5``, means we can later refer to the number ``5`` with the name ``five``, the equality sign ``==`` on the other hand is used to check if two things are equal e.g. ``5 == 4`` means "is ``5`` is equal to ``4``?"


REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

There's not much to do here, we could repeat the above as a drill to help remember the solution

RED: make it fail
~~~~~~~~~~~~~~~~~


* add a failing line to ``test_defining_variables_to_solve_attribute_errors``

  .. code-block:: python

      def test_defining_variables_to_solve_attribute_errors(self):
          self.assertIsNone(module.variable_0)
          self.assertIsNone(module.variable_1)

  the terminal will update to show an ``AttributeError``

  .. code-block:: python

      E       AttributeError: module 'module' has no attribute 'variable_1'

GREEN: make it pass
~~~~~~~~~~~~~~~~~~~

* RED: make it fail

  add the name to ``module.py``

  .. code-block:: python

      variable_0 = None
      variable_1

  the terminal reveals a ``NameError``

  .. code-block:: python

      E   NameError: name 'variable_1' is not defined

* GREEN: make it pass
  add a definition for ``variable_1``

  .. code-block:: python

      variable_0 = None
      variable_1 = None

  the terminal displays passing tests

RED: make it fail
~~~~~~~~~~~~~~~~~


* we add another failing line to ``test_defining_variables_to_solve_attribute_errors``

  .. code-block:: python

    def test_defining_variables_to_solve_attribute_errors(self):
        self.assertIsNone(module.variable_0)
        self.assertIsNone(module.variable_1)
        self.assertIsNone(module.variable_2)

  the terminal updates with an ``AttributeError``

  .. code-block:: python

      >       self.assertIsNone(module.variable_2)
      E       AttributeError: module 'module' has no attribute 'variable_2'

GREEN: make it pass
~~~~~~~~~~~~~~~~~~~


* RED: make it fail - add the name to ``module.py``

  .. code-block:: python

      variable_0 = None
      variable_1 = None
      variable_2

  the terminal outputs a ``NameError``

  .. code-block:: python

      E   NameError: name 'variable_2' is not defined

* GREEN: make it pass - define ``variable_2`` in ``module.py``

  .. code-block:: python

      variable_0 = None
      variable_1 = None
      variable_2 = None

  The tests pass

RED: make it fail
~~~~~~~~~~~~~~~~~


* we add another failing line to ``test_defining_variables_to_solve_attribute_errors``

  .. code-block:: python

      def test_defining_variables_to_solve_attribute_errors(self):
          self.assertIsNone(module.variable_0)
          self.assertIsNone(module.variable_1)
          self.assertIsNone(module.variable_2)
          self.assertIsNone(module.variable_3)

  the terminal gives an ``AttributeError``

  .. code-block:: python

      E       AttributeError: module 'module' has no attribute 'variable_3'

GREEN: make it pass
"""""""""""""""""""


* RED: make it fail

  we add the name

  .. code-block:: python

      variable_0 = None
      variable_1 = None
      variable_2 = None
      variable_3

  the terminal displays a ``NameError``

  .. code-block:: python

      E   NameError: name 'variable_3' is not defined

* GREEN: make it pass

  we define the name

  .. code-block:: python

      variable_0 = None
      variable_1 = None
      variable_2 = None
      variable_3 = None

We have a pattern for our drill. When we test an attribute in a module, we encounter


* an ``AttributeError`` when the attribute does not exist
* a ``NameError`` when we add the name to the module
* a passing test when we define the name as a variable

Update the ``TestAttributeError`` class in ``tests/test_attribute_error.py`` by adding more tests until you get to ``self.assertIsNone(module.variable_99)``, you will have 102 statements in total

.. code-block:: python

    def test_defining_variables_to_solve_attribute_errors(self):
        self.assertIsNone(module.variable_0)
        self.assertIsNone(module.variable_1)
        self.assertIsNone(module.variable_2)
        self.assertIsNone(module.variable_3)
        ...
        self.assertIsNone(module.variable_99)
        self.assertFalse(module.false)
        self.assertTrue(module.true)

Repeat the pattern until all tests pass.


* What's your solution to the last two tests? They are similar to the test for failure in `How I setup a Test Driven Development Environment <./How I setup a Test Driven Development Environment.rst>`_
* did you update ``module.py`` this way?

  .. code-block::

      true = True
      false = False

*WELL DONE!* You now know


* How to solve `ModuleNotFoundError <./ModuleNotFoundError.rst>`_
* How to solve ``NameError`` using variables
* How to solve `AttributeError <./AttributeError.rst>`_ by defining variables

----


Solve AttributeError by defining a Function
-------------------------------------------

Let us take a look at solving ``AttributeError`` with functions

RED: make it fail
^^^^^^^^^^^^^^^^^

Update the ``TestAttributeError`` class in ``tests/test_attribute_error.py`` with a new test

.. code-block:: python

    def test_defining_functions_to_solve_attribute_errors(self):
        self.assertIsNone(module.function_0())

the terminal updates to show

.. code-block:: python

   E       AttributeError: module 'module' has no attribute 'function_0'

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* we try the solution we know for solving ``AttributeError`` using variables and update ``module.py``

  .. code-block:: python

      function_0 = None

  we see a ``TypeError`` in the terminal

  .. code-block:: python

      E       TypeError: 'NoneType' object is not callable

  this is new so we update our list of exceptions encountered

  .. code-block:: python

      # Exceptions Encountered
      # AssertionError
      # ModuleNotFoundError
      # AttributeError
      # NameError
      # TypeError

  a ``TypeError`` is raised in this case because we ``called`` an object that was not ``callable``. A callable object is an object that can potentially handle inputs. We can define a callable as a ``class`` or a ``function``.

  We go over callables in `Functions <./functions.rst>`_ and `Classes <./classes.rst>`_. When an object is defined as a callable, we call it by adding parentheses at the end e.g. ``module.function_0()`` will call ``function_0`` in ``module.py``

* let us change ``function_0`` in ``module.py`` to a function by modifying its definition using the ``def`` keyword

  .. code-block:: python

      def function_0():
          return None

  the terminal updates to show tests pass

  .. note::

     *What is a Function?*


     * A ``function`` is a named block of code that performs some action or series of actions
     * In python a function always returns something
     * the default return value of a function is ``None``
     * the line with ``return`` is the last executable line of code in a function


REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


* Time to a drill like we did with variables. Update ``test_defining_functions_to_solve_attribute_errors`` in the ``TestAttributeError`` class in\ ``tests/test_attribute_error.py`` to include calls to functions in ``module.py`` until you have one for ``module.function_99()``, you will have 100 tests in total

  .. code-block:: python

      def test_defining_functions_to_solve_attribute_errors(self):
          self.assertIsNone(module.function_0())
          self.assertIsNone(module.function_1())
          self.assertIsNone(module.function_2())
          self.assertIsNone(module.function_3())
          ...
          self.assertIsNone(module.function_99())

  the terminal updates to show an error

  .. code-block:: python

      E       AttributeError: module 'module' has no attribute 'function_1'

  update ``module.py`` with the solution until all tests pass

*YOU DID IT AGAIN!* You now know


* How to solve `ModuleNotFoundError <./ModuleNotFoundError.rst>`_
* How to solve ``NameError``
* How to solve `AttributeError <./AttributeError.rst>`_ by defining variables and functions


----


Solve AttributeError by defining a Class
----------------------------------------

A class is a blueprint that represents an object, it is a collection of functions(methods) and attributes. Attributes are names which represent a value. Methods are functions that can accept inputs and return a value. For example we could define a `Human` class with attributes like eye color, date of birth, height and weight, and methods like age which returns a value based on the current year and date of birth. Let us explore ``AttributeError`` with classes.

RED: make it fail
^^^^^^^^^^^^^^^^^


* We add a test function to the ``TestAttributeError`` class in ``tests/test_attribute_error.py``

  .. code-block:: python

       def test_defining_functions_to_solve_attribute_errors(self):
           self.assertIsNone(module.Class0())

  the terminal shows

  .. code-block:: python

      E       AttributeError: module 'module' has no attribute 'Class0'

  Looking at the `traceback` we see it's the line we added that caused the failure

  * We are familiar with an ``AttributeError``
  * This also looks exactly like the tests in ``test_defining_functions_to_solve_attribute_errors``
  * What's the difference?

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* Update ``module.py``

  .. code-block:: python

      Class0 = None

  the terminal updates to show a ``TypeError``

  .. code-block:: python

      E       TypeError: 'NoneType' object is not callable

  We dealt with a similar issue earlier, let us make ``Class0`` callable the way we know how. Change the variable to a function using the ``def`` keyword in ``module.py``

  .. code-block:: python

      def Class():
          return None

  The tests pass! Something is odd here, what is the difference between `Classes <./classes.rst>`_ and `Functions <./functions.rst>`_\ ? Why are we writing a different set of tests for Classes if the solutions are the same?

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


* let us make it a drill. Add lines to ``test_defining_functions_to_solve_attribute_errors`` in the ``TestAttributeError`` class in ``tests/test_attribute_error.py`` until we have one for ``module.Class99()``, there will be 100 tests in total

  .. code-block:: python

      def test_defining_classes_to_solve_attribute_errors(self):
          self.assertIsNone(module.Class0())
          self.assertIsNone(module.Class1())
          self.assertIsNone(module.Class2())
          self.assertIsNone(module.Class3())
          ...
          self.assertIsNone(module.Class99())

  the terminal updates to show

  .. code-block:: python

      E       AttributeError: module 'module' has no attribute 'Class1'

  update ``module.py`` with each solution until all tests pass

*WELL DONE!* You now know


* How to solve `ModuleNotFoundError <./ModuleNotFoundError.rst>`_
* How to solve ``NameError``
* How to solve `AttributeError <./AttributeError.rst>`_ by defining variables, `functions <./functions.rst>`_ and `classes <./classes.rst>`_

  * do we know how to define `classes <./classes.rst>`_ if we define them the same was as `functions <./functions.rst>`_\ ?

----


Solve AttributeError by defining an Attribute in a Class
--------------------------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^


* We add a new test to the ``TestAttributeError`` class in ``test_attribute_error.py``

  .. code-block:: python

       def test_defining_attributes_in_classes_to_solve_attribute_errors(self):
           self.assertIsNone(module.Class.attribute_0)

  the terminal updates to show an ``AttributeError``

  .. code-block:: python

       >       self.assertIsNone(module.Class.attribute_0)
       E       AttributeError: module 'module' has no attribute 'Class'

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* update ``module.py`` with a variable

  .. code-block:: python

       Class = None

  the terminal updates to show

  .. code-block:: python

      E       AttributeError: 'NoneType' object has no attribute 'attribute_0'

  change the variable to a function

  .. code-block:: python

      def Class():
          return None

  the terminal updates to show

  .. code-block:: python

      E       AttributeError: 'function' object has no attribute 'attribute_0'

  is it possible to define an attribute in a function and access it? update ``module.py``

  .. code-block:: python

      def Class():
          attribute_0 = None
          return None

  the terminal still gives the same error, our experiment had no effect on the test

* what if we use the ``class`` keyword to define ``Class`` instead of ``def``

  .. code-block:: python

      class Class():
          attribute_0 = None
          return None

  the terminal now shows a ``SyntaxError``

  .. code-block:: python

      E       return None
      E       ^^^^^^^^^^^
      E   SyntaxError: 'return' outside function


  * We add ``SyntaxError`` to our running list of exceptions

    .. code-block:: python

        # Exceptions Encountered
        # AssertionError
        # ModuleNotFoundError
        # AttributeError
        # NameError
        # TypeError
        # SyntaxError

  * The error is caused by the ``return`` statement being outside of a function

* remove the return statement

  .. code-block:: python

      class Class():
          attribute_0 = None

  Eureka! The Tests pass!!

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


* The current solution for ``test_defining_classes_to_solve_attribute_errors`` was done by defining functions but the test says ``definining_classes``. let us update those tests to use the proper way of defining `classes <./classes.rst>`_ that we just learned. Update ``module.py`` to use ``class`` instead of ``def`` e.g.

  .. code-block:: python

      class Class0():
          pass
      ...
      class Class99():
          pass

  ``pass`` is a keyword used as a placeholder that does nothing

* We now know how to properly define a class with an attribute. To practice defining an attribute we will make a drill by adding more lines like we did for variables, functions and classes, until you have a total of 100 lines with the last test for ``module.Class.attribute_99``

  .. code-block:: python

      def test_defining_attributes_in_classes_to_solve_attribute_errors(self):
          self.assertIsNone(module.Class.attribute_0)
          self.assertIsNone(module.Class.attribute_1)
          self.assertIsNone(module.Class.attribute_2)
          self.assertIsNone(module.Class.attribute_3)
          ...
          self.assertIsNone(module.Class.attribute_99)

  the terminal updates to show

  .. code-block:: python

      E       AttributeError: type object 'Class' has no attribute 'attribute_1'

  update ``module.py`` with the solutions until all tests pass

*WELL DONE!* You now know You now know


* How to solve `ModuleNotFoundError <./ModuleNotFoundError.rst>`_
* How to solve ``NameError``
* How to solve `AttributeError <./AttributeError.rst>`_ by defining variables, `functions <./functions.rst>`_ and `classes <./classes.rst>`_
* How to solve `AttributeError <./AttributeError.rst>`_ by defining

  * variables
  * `functions <./functions.rst>`_
  * `classes <./AssertionError.rst>`_
  * attributes (variables) in classes


----


Solve AttributeError by defining a Method(Function) in a Class
--------------------------------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^


* we add a new test to the ``TestAttributeError`` class in ``test_attribute_error.py``

  .. code-block:: python

      def test_defining_functions_in_classes_to_solve_attribute_errors(self):
          self.assertIsNone(module.Class.method_0())

  the terminal updates to show an ``AttributeError``

  .. code-block:: python

      >       self.assertIsNone(module.Class.method_0())
      E       AttributeError: type object 'Class' has no attribute 'method_0'

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* Update the class ``Class`` in ``module.py``

  .. code-block:: python

      class Class():
          ...
          method_0 = None

  the terminal will update to show a ``TypeError``

  .. code-block:: python

      >       self.assertIsNone(module.Class.method_0())
      E       TypeError: 'NoneType' object is not callable

  this is in our list of errors

* using the solution we know for it, we change ``method_0`` from an attribute to a method using the ``def`` keyword to make it callable

  .. code-block:: python

      class Class():
          ...
          def method_0():
              return None

  Fantastic! the terminal has all tests passing.

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

You know the "drill", update ``test_defining_functions_in_classes_to_solve_attribute_errors`` in ``TestAttributeError`` in ``test_attribute_error.py`` with more lines until we have 100 tests ending with one for ``module.Class.method_99()``

.. code-block:: python

    def test_defining_functions_in_classes_to_solve_attribute_errors(self):
        self.assertIsNone(module.Class.method_0())
        self.assertIsNone(module.Class.method_1())
        self.assertIsNone(module.Class.method_2())
        self.assertIsNone(module.Class.method_3())
        ...
        self.assertIsNone(module.Class.method_99())

repeat the solution until all tests pass

*CONGRATULATIONS!* You now know


* How to solve `ModuleNotFoundError <./ModuleNotFoundError.rst>`_
* How to solve ``NameError``
* How to solve `AttributeError <./AttributeError.rst>`_ by defining variables, `functions <./functions.rst>`_ and `classes <./classes.rst>`_
* How to solve `AttributeError <./AttributeError.rst>`_ by defining

  - variables
  - `functions <./functions.rst>`_
  - `classes <./AssertionError.rst>`_
  - attributes (variables) in classes
  - methods (functions) in classes

*WHAT IS THE DIFFERENCE BETWEEN CLASSES AND FUNCTIONS?*


* we can access attributes (variables) we define in a class from outside the class
* we cannot access variables we define in a function from outside the function
* the keywords used to define them are different - ``def`` vs ``class``
* their naming conventions are different - ``snake_case`` vs ``CamelCase``
