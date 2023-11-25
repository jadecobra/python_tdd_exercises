
AttributeError
==============

In this chapter I cover the `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

An Attribute is a property, variable, function or name that belongs to an `object <https://docs.python.org/3/glossary.html#term-object>`_. For example when I describe a human being I can list attributes like height, weight, sex and color.
An `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ is raised when there is a reference to a name in an `object <https://docs.python.org/3/glossary.html#term-object>`_ that does not exist.


----

Solve an AttributeError by defining variables
----------------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I open a new file, save it as ``test_attribute_error.py`` in the ``tests`` folder created in :doc:`How to Setup a Test Driven Development Environment <setup_tdd_environment>` and type the following

.. code-block:: python

  import unittest
  import module

* ``import unittest`` imports the `unittest <https://docs.python.org/3/library/unittest.html>`_ module from the python standard library
* ``import module`` imports the ``module`` module - which will hold the code I am testing

The terminal responds with a :doc:`ModuleNotFoundError`

.. code-block:: python

  ImportError while importing test module '/<PATH_TO_PROJECT_NAME>/{PROJECT_NAME}/tests/test_attribute_error.py'.
  Hint: make sure your test modules/packages have valid python names.
  Traceback:
  ...
  tests/test_attribute_error.py:2: in <module>
    import module
  E  ModuleNotFoundError: No module called 'module'

A :doc:`ModuleNotFoundError` is raised when a name is provided to an ``import`` statement and python cannot find the name. Since there is currently no file called ``module.py`` the ``import module`` line causes a failure

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

* I change the running list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError

* then create ``module.py`` in the ``{PROJECT_NAME}`` folder and the terminal all tests are passing
* I continue updating ``test_attribute_error.py`` to add the tests

  .. code-block:: python

    import unittest
    import module


    class TestAttributeErrors(unittest.TestCase):

      def test_defining_variables_to_solve_attribute_errors(self):
          module.variable_0

  - ``class TestAttributeErrors(unittest.TestCase):`` is a class definition that inherits from `unittest.TestCase <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase>`_ and will hold the tests
  - ``def test_defining_variables_to_solve_attribute_errors(self):`` is the definition of the first test function to find out if defining variables can solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_
  - ``module.variable_0`` - the actual test, I think of this as making a phone call to ``variable_0`` in ``module.py``

* the terminal shows an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    self = <tests.test_attribute_error.TestAttributeError testMethod=test_defining_variables_to_solve_attribute_errors>

      def test_defining_variables_to_solve_attribute_errors(self):
    >    module.variable_0
    E    AttributeError: module 'module' has no attribute 'variable_0'


  - ``tests/test_attribute_error.py:7: AttributeError`` the filename, line number and name of the Exception that is raised by the code at that location
  - ``E    AttributeError: module 'module' has no attribute 'variable_0'`` an explanation of the error raised. The module I imported has no definitions called ``variable_0``
  - ``>    module.variable_0`` the line of code that caused the error. The file ``module.py`` has no definitions called ``variable_0``. This is like making a phone call to a number that is not in service or sending an e-mail to an address that does not exist
  - ``def test_defining_variables_to_solve_attribute_errors(self):`` the function definition where the error occurs
  - ``self = <tests.test_attribute_error.TestAttributeError testMethod=test_defining_variables_to_solve_attribute_errors>`` is a reference to the :doc:`class <classes>` and :doc:`method (function) <functions>` where the failure occurred

* I add the error to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError

* then add a name to ``module.py``

  .. code-block:: python

    variable_0

  and the terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_

  .. code-block::

    tests/test_attribute_error.py:2: in <module>
      import module
    module.py:1: in <module>
      variable_0
    E  NameError: name 'variable_0' is not defined

  - ``E  NameError: name 'variable_0' is not defined`` the `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_ is raised because ``variable_0`` in ``module.py`` is viewed as a reference and there is currently no definition or assignment for that name
  - ``variable_0`` the offending line
  - ``module.py:1: in <module>`` the location of the offending line

* I add `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_ to my running list of errors encountered

  .. code-block::

  # Exceptions Encountered
  # AssertionError
  # ModuleNotFoundError
  # AttributeError
  # NameError

* then change the failing line in ``module.py`` to fix it

  .. code-block:: python

    variable_0 = None

  this assigns the name ``variable_0`` to :doc:`None <data_structures_none>` and the terminal shows a passing test. YES!

  .. code-block:: python

    collected 2 items

    tests/test_attribute_error.py .                    [ 50%]
    tests/test_{PROJECT_NAME}.py .                     [100%]

    ============================== 2 passed in 0.03s==================================

I solved the `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining a variable

.. NOTE::

  - In python ``=`` is used to assign names to objects, for example ``five = 5``, means I can later refer to the number ``5`` with the name ``five``
  - the equality sign ``==`` is used to check if two things are equal  example  ``5 == 4`` means "is ``5`` is equal to ``4``?"

AttributeError vs NameError
~~~~~~~~~~~~~~~~~~~~~~~~~~~

An `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ is raised when there is a reference to a name in an `object <https://docs.python.org/3/glossary.html#term-object>`_ from outside the `object <https://docs.python.org/3/glossary.html#term-object>`_ and the name does not exist, for example ``humans.wings``

A `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_ is raised when there is a reference to a name within an object and there is no prior definition with the name


REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

I could repeat the above as a drill to help remember the solution

RED: make it fail
~~~~~~~~~~~~~~~~~


* When I add a failing line to ``test_defining_variables_to_solve_attribute_errors``

  .. code-block:: python

    def test_defining_variables_to_solve_attribute_errors(self):
        module.variable_0
        module.variable_1

  the terminal shows an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    E    AttributeError: module 'module' has no attribute 'variable_1'

GREEN: make it pass
~~~~~~~~~~~~~~~~~~~

* RED: make it fail

  I add the name to ``module.py``

  .. code-block:: python

    variable_0 = None
    variable_1

  the terminal displays a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_

  .. code-block:: python

    E  NameError: name 'variable_1' is not defined

* GREEN: make it pass
  I add a definition for ``variable_1``

  .. code-block:: python

    variable_0 = None
    variable_1 = None

  the terminal displays passing tests

RED: make it fail
~~~~~~~~~~~~~~~~~


* I add another failing line to ``test_defining_variables_to_solve_attribute_errors``

  .. code-block:: python

    def test_defining_variables_to_solve_attribute_errors(self):
        module.variable_0
        module.variable_1
        module.variable_2

  the terminal shows an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    >    module.variable_2
    E    AttributeError: module 'module' has no attribute 'variable_2'

GREEN: make it pass
~~~~~~~~~~~~~~~~~~~


* RED: make it fail - I add the name to ``module.py``

  .. code-block:: python

    variable_0 = None
    variable_1 = None
    variable_2

  the terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_

  .. code-block:: python

    E  NameError: name 'variable_2' is not defined

* GREEN: make it pass - I define ``variable_2`` in ``module.py``

  .. code-block:: python

    variable_0 = None
    variable_1 = None
    variable_2 = None

  The tests pass

RED: make it fail
~~~~~~~~~~~~~~~~~


* I add another failing line to ``test_defining_variables_to_solve_attribute_errors``

  .. code-block:: python

    def test_defining_variables_to_solve_attribute_errors(self):
        module.variable_0
        module.variable_1
        module.variable_2
        module.variable_3

  the terminal shows an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    E    AttributeError: module 'module' has no attribute 'variable_3'

GREEN: make it pass
~~~~~~~~~~~~~~~~~~~


* RED: make it fail

  I add the name

  .. code-block:: python

    variable_0 = None
    variable_1 = None
    variable_2 = None
    variable_3

  the terminal displays a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_

  .. code-block:: python

    E  NameError: name 'variable_3' is not defined

* GREEN: make it pass

  I define the name

  .. code-block:: python

    variable_0 = None
    variable_1 = None
    variable_2 = None
    variable_3 = None

I have a pattern for the drill. When I test an attribute in a module, I get


* an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ when the attribute does not exist
* a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_ when I add the name to the module
* a passing test when I define the name as a variable

If you are feeling adventurous you can add more tests to ``test_defining_variables_to_solve_attribute_errors`` until you get to ``module.variable_99``

.. code-block:: python

  def test_defining_variables_to_solve_attribute_errors(self):
    module.variable_0
    module.variable_1
    module.variable_2
    module.variable_3
    ...
    module.variable_99

Repeat the pattern until all tests pass.

If you have been typing along *WELL DONE!* You now know


* How to solve a :doc:`ModuleNotFoundError`
* How to solve a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_ using variables
* How to solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining variables

----


Solve an AttributeError by defining functions
----------------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I change the ``TestAttributeError`` class in ``tests/test_attribute_error.py`` with a new test

.. code-block:: python

  def test_defining_functions_to_solve_attribute_errors(self):
      module.function_0()

the terminal responds with an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ as expected

.. code-block:: python

  E    AttributeError: module 'module' has no attribute 'function_0'

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* I try the solution I know for solving `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ with variables and change ``module.py`` to include a new variable

  .. code-block:: python

    function_0 = None

  I see a :doc:`TypeError` in the terminal

  .. code-block:: python

    E    TypeError: 'NoneType' object is not callable

* this is new so I add it to the list of exceptions encountered

  .. code-block:: python

   # Exceptions Encountered
   # AssertionError
   # ModuleNotFoundError
   # AttributeError
   # NameError
   # TypeError

* a :doc:`TypeError` is raised in this case because I called an object that was not `callable <https://docs.python.org/3/glossary.html#term-callable>`_.

  A `callable <https://docs.python.org/3/glossary.html#term-callable>`_ object is an object that may be able to handle inputs. I can make an `object <https://docs.python.org/3/glossary.html#term-object>`_ `callable <https://docs.python.org/3/glossary.html#term-callable>`_ by defining it as a :doc:`class <classes>` or a :doc:`function <functions>`

  Parentheses are used at the end of the name of an object when calling it, for example  ``module.function_0()`` will call ``function_0`` from ``module.py``

* What if I change ``function_0`` in ``module.py`` to a function by changing its definition using the `def <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ keyword?

  .. code-block:: python

    def function_0():
        return None

  the terminal shows passing tests


REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


* Time to make a drill. You can change ``test_defining_functions_to_solve_attribute_errors`` in the ``TestAttributeError`` class in ``tests/test_attribute_error.py`` to include calls to functions in ``module.py`` until you have one for ``module.function_99()``

  .. code-block:: python

    def test_defining_functions_to_solve_attribute_errors(self):
        module.function_0()
        module.function_1()
        module.function_2()
        module.function_3()
        ...
        module.function_99()

  the terminal shows an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    E    AttributeError: module 'module' has no attribute 'function_1'

  change ``module.py`` with the solution until all tests pass

*YOU DID IT AGAIN!* You now know


* How to solve a :doc:`ModuleNotFoundError`
* How to solve a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_
* How to solve a :doc:`TypeError` by defining a callable
* How to solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining variables
* How to solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining :doc:`functions`


----


Solve an AttributeError by defining classes
--------------------------------------------

A :doc:`class <classes>` is a blueprint that represents an `object <https://docs.python.org/3/glossary.html#term-object>`_. I think of it is a collection of :doc:`methods (functions) <functions>` and attributes

- attributes are names which represent a value
- :doc:`methods <functions>` are :doc:`functions` that may be able to accept inputs and return a value, they are `callable <https://docs.python.org/3/glossary.html#term-callable>`_

For example I could define a ``Human`` class with attributes like eye color, date of birth, height and weight, and :doc:`methods <functions>` like age which returns a value based on the current year and date of birth attribute, you can see an example of this in :doc:`classes` for more

RED: make it fail
^^^^^^^^^^^^^^^^^

* I add a test function to the ``TestAttributeError`` class in ``tests/test_attribute_error.py``

  .. code-block:: python

    def test_defining_classes_to_solve_attribute_errors(self):
        module.Class0()

  the terminal shows

  .. code-block:: python

    E    AttributeError: module 'module' has no attribute 'Class0'


GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* I add a name to ``module.py``

  .. code-block:: python

    Class0 = None

  and the terminal shows a :doc:`TypeError`

  .. code-block:: python

    E    TypeError: 'NoneType' object is not callable

  I had a similar issue earlier, what if I make ``Class0`` `callable <https://docs.python.org/3/glossary.html#term-callable>`_ by changing the variable to a function using the `def <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ keyword in ``module.py``

  .. code-block:: python

    def Class():
        return None

  The test passes! Something is odd here, what is the difference between :doc:`classes` and :doc:`functions`? Why am I writing a different set of tests for :doc:`classes` if the solutions are the same for :doc:`functions`?

  For now, I will move on with these questions unanswered until they become obvious

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


* This could also be a drill, add lines to ``test_defining_classes_to_solve_attribute_errors`` in the ``TestAttributeError`` class in ``tests/test_attribute_error.py`` until you have one for ``module.Class99()``

  .. code-block:: python

    def test_defining_classes_to_solve_attribute_errors(self):
        module.Class0()
        module.Class1()
        module.Class2()
        module.Class3()
        ...
        module.Class99()

  the terminal shows an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    E    AttributeError: module 'module' has no attribute 'Class1'

  change ``module.py`` with each solution until all tests pass

*WELL DONE!* You now know

* How to solve a :doc:`ModuleNotFoundError`
* How to solve a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_
* How to solve a :doc:`TypeError` by defining a callable
* How to solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining variables
* How to solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining :doc:`functions`
* How to solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining :doc:`classes`? do I know how to define :doc:`classes` if I define them the same way I do :doc:`functions`?

----


Solve an AttributeError by defining class attributes
-----------------------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^


* I add a new test to the ``TestAttributeError`` class in ``test_attribute_error.py``

  .. code-block:: python

    def test_defining_attributes_in_classes_to_solve_attribute_errors(self):
        module.Class.attribute_0

  the terminal shows an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    >    module.Class.attribute_0
    E    AttributeError: module 'module' has no attribute 'Class'

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* I add a variable to ``module.py``

  .. code-block:: python

    Class = None

  and the terminal still displays an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ but with a different message

  .. code-block:: python

    E    AttributeError: 'NoneType' object has no attribute 'attribute_0'

  when I change the variable to a function

  .. code-block:: python

    def Class():
        return None

  the terminal shows an an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ but with a slightly different message

  .. code-block:: python

    E    AttributeError: 'function' object has no attribute 'attribute_0'

* I wonder if it is possible to define an attribute in a function and access it from outside the function. I change ``module.py``

  .. code-block:: python

    def Class():
        attribute_0 = None
        return None

  the terminal still shows the same error, my guess was wrong

* what if I use the `class <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ keyword to define ``Class`` instead of `def <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_?

  .. code-block:: python

    class Class():
        attribute_0 = None
        return None

  the terminal now shows a `SyntaxError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#SyntaxError>`_

  .. code-block:: python

    E    return None
    E    ^^^^^^^^^^^
    E  SyntaxError: 'return' outside function

  the error is caused by the ``return`` statement being outside a :doc:`function <functions>`


* I add `SyntaxError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#SyntaxError>`_ to the running list of exceptions

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # NameError
    # TypeError
    # SyntaxError

* when I remove the return statement

  .. code-block:: python

    class Class():
        attribute_0 = None

  and the test passes. WOO HOO!

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


* The current solution for ``test_defining_classes_to_solve_attribute_errors`` was done by defining functions but the test name contains ``definining_classes``, time to go back and change ``module.py`` using the `class <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ keyword instead of `def <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_

  .. code-block:: python

    class Class0():
     pass
   ...
    class Class99():
     pass

  `pass <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ is a keyword used as a placeholder

* I now know how to properly define a :doc:`class <classes>` with an attribute. You can make a drill to practice by adding more lines to ``test_defining_attributes_in_classes_to_solve_attribute_errors`` until you have a total of 100 lines

  .. code-block:: python

    def test_defining_attributes_in_classes_to_solve_attribute_errors(self):
        module.Class.attribute_0
        module.Class.attribute_1
        module.Class.attribute_2
        module.Class.attribute_3
        ...
        module.Class.attribute_99

  the terminal shows

  .. code-block:: python

    E    AttributeError: type object 'Class' has no attribute 'attribute_1'

  change ``module.py`` with the solutions until all tests pass

*WELL DONE!* You now know You now know


* How to solve a :doc:`ModuleNotFoundError`
* How to solve a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_
* How to solve a :doc:`TypeError` by defining a callable
* How to solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining variables
* How to solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining :doc:`functions`
* How to solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining :doc:`classes`
* How to solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining attributes (variables) in :doc:`classes`


----


Solve an AttributeError by defining class methods
--------------------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^


* I add a new test to the ``TestAttributeError`` class in ``test_attribute_error.py``

  .. code-block:: python

    def test_defining_functions_in_classes_to_solve_attribute_errors(self):
        module.Class.method_0()

  the terminal shows an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_

  .. code-block:: python

    >    module.Class.method_0()
    E    AttributeError: type object 'Class' has no attribute 'method_0'

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* I add a name to ``Class`` in ``module.py``

  .. code-block:: python

    class Class():
        ...
        method_0 = None

  and the terminal shows a :doc:`TypeError`

  .. code-block:: python

    >    module.Class.method_0()
    E    TypeError: 'NoneType' object is not callable

* then I change ``method_0`` from an attribute to a :doc:`method <functions>` using the `def <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ keyword to make it callable

  .. code-block:: python

    class Class():
        ...
        def method_0():
          return None

  and all tests pass. Fantastic!

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

You know the "drill", change ``test_defining_functions_in_classes_to_solve_attribute_errors`` in ``TestAttributeError`` in ``test_attribute_error.py`` with more lines until there are 100 tests ending with one for ``module.Class.method_99()``

.. code-block:: python

  def test_defining_functions_in_classes_to_solve_attribute_errors(self):
      module.Class.method_0()
      module.Class.method_1()
      module.Class.method_2()
      module.Class.method_3()
      ...
      module.Class.method_99()

repeat the solution until all tests pass

*CONGRATULATIONS!* You now know


* How to solve a :doc:`ModuleNotFoundError`
* How to solve a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_
* How to solve a :doc:`TypeError` by defining a callable
* How to solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining variables
* How to solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining :doc:`functions`
* How to solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining :doc:`classes`
* How to solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining attributes (variables) in :doc:`classes`
* How to solve an `AttributeError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#AttributeError>`_ by defining :doc:`methods (functions) <functions>` in :doc:`classes`

:doc:`classes` vs :doc:`functions` in python
--------------------------------------------

* I can access attributes (variables) or methods of a class from outside the class
* I cannot access variables or functions defined in a function from outside the function
* keywords used to define them - `class <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ vs `def <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_
* naming conventions - ``CamelCase`` vs ``snake_case``
