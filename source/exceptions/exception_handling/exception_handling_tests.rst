.. meta::
  :description: How to test that a Python Exception is raised with try/except/else, a homemade assert_raises plus exec, and unittest assertRaises (with self.assertRaises(...)). TDD RED/GREEN drills for ModuleNotFoundError (import does_not_exist), NameError, AttributeError (src.exceptions.does_not_exist), TypeError (None not callable, then function_name() takes 0 positional arguments but 1 was given), IndexError on strings and tuples (positive and negative indexes), KeyError not_in_dictionary, ZeroDivisionError (1/0), and raise Exception. One exception per handler — assertRaises exits after the first matching raise. Pumping Python TDD by Jacob Itegboje.
  :keywords: Jacob Itegboje, Pumping Python TDD, how to test if an Exception is raised, try except else raise AssertionError, exec function, homemade assert_raises, unittest assertRaises, self.assertRaises context manager, ModuleNotFoundError No module named, NameError is not defined, AttributeError has no attribute, TypeError NoneType not callable, TypeError positional arguments, IndexError string index out of range, IndexError tuple index out of range, KeyError not_in_dictionary, ZeroDivisionError division by zero, raise Exception, one exception one exception handler, exceptions/tests/test_exceptions.py, python tdd exception handling

.. include:: ../../links.rst

.. _NameError: https://docs.python.org/3/library/exceptions.html#NameError
.. _ZeroDivisionError: https://docs.python.org/3/library/exceptions.html#ZeroDivisionError
.. _try statement: https://docs.python.org/3/reference/compound_stmts.html#the-try-statement
.. _assertRaises: https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertRaises
.. _assertRaises method: assertRaises_
.. _unittest.TestCase.assertRaises: assertRaises_
.. _unittest.TestCase.assertRaisesRegex: assertRaisesRegex_
.. _exec: https://docs.python.org/3/library/functions.html#exec
.. _exec built-in function: exec
.. _raise: https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement
.. _raises: raise_
.. _raise statement: raises_

#################################################################################
how to test if an Exception is raised
#################################################################################

----

When an :ref:`error<how to test if an Exception is raised>` happens in Python_, an :ref:`Exception<how to test if an Exception is raised>` is raised to stop the program_, this means nothing past the line that caused the :ref:`error<how to test if an Exception is raised>` will run.

It is useful because there is a problem that must be solved for the program_ to continue. It is a problem when it causes the program_ to stop early.

What if I want to test that a program_ raises an :ref:`Exception<how to test if an Exception is raised>`? If the :ref:`Exception<how to test if an Exception is raised>` is raised, the test will not continue past the line that caused it.

I can use the :ref:`try statement<how to use try...except...else>` to test that some code raises an :ref:`Exception<how to test if an Exception is raised>` and continue past the line that caused it.

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/exception_handling/test_exceptions_in_tests.py
  :language: python
  :linenos:
  :caption: exceptions/tests/test_exceptions.py
  :lines: 1-21

.. literalinclude:: ../../code/exception_handling/test_exceptions_in_tests.py
  :language: python
  :lineno-start: 23
  :caption: exceptions/tests/test_exceptions.py
  :lines: 23-41

.. literalinclude:: ../../code/exception_handling/test_exceptions_in_tests.py
  :language: python
  :lineno-start: 43
  :caption: exceptions/tests/test_exceptions.py
  :lines: 43-62

.. literalinclude:: ../../code/exception_handling/test_exceptions_in_tests.py
  :language: python
  :lineno-start: 64
  :caption: exceptions/tests/test_exceptions.py
  :lines: 64-

----

*********************************************************************************
questions about testing Exceptions
*********************************************************************************

Questions to think about as I go through the chapter

* :ref:`how can I handle an Exception when it happens?<how to handle Exceptions>`
* :ref:`how can I make sure an Exception is raised?<how to test if an Exception is raised>`
* :ref:`what causes ModuleNotFoundError?<test_catching_module_not_found_error>`
* :ref:`what causes NameError?<test_catching_name_error>`
* :ref:`what causes AttributeError?<test_catching_attribute_error>`
* :ref:`what causes TypeError?<test_catching_type_error>`
* :ref:`what causes IndexError?<test_catching_index_error>`
* :ref:`what causes KeyError?<test_catching_key_error>`
* :ref:`what causes ZeroDivisionError?<test_catching_zero_division_error>`
* :ref:`what Exception do all the other Exceptions come (inherit) from?<test_catching_exceptions>`
* :ref:`what is the exec function?<the exec function>`
* :ref:`why use one exception handler for one exception?<one exception one exception handler>`
* :ref:`how can I use the else clause when handling Exceptions?<how to use try...except...else>`

----

*********************************************************************************
requirements
*********************************************************************************

:ref:`makePythonTdd<how to make a Python Test Driven Development environment automatically with variables>`

----

*********************************************************************************
start the project
*********************************************************************************

* I open a terminal_
* I give ``exceptions`` as the first argument to the ``makePythonTdd`` program

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        ./makePythonTdd.sh exceptions

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        .\makePythonTdd.ps1 exceptions

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 10
    :emphasize-text: tests/test_exceptions.py:7

    ======================== FAILURES ==========================
    ______________ Testexceptions.test_failure _________________

    self = <tests.test_exceptions.Testexceptions testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_exceptions.py:7: AssertionError
    ================== short test summary info ==================
    FAILED tests/test_exceptions.py::Testexceptions::test_failure - AssertionError: True is not false
    ===================== 1 failed in X.YZs =====================

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option/command` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_exceptions.py:7`` to put the cursor on line 7

* I change :ref:`assertFalse<another way to test if something is grouped as False>` to :ref:`assertTrue<another way to test if something is grouped as True>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 4-5

    class Testexceptions(unittest.TestCase):

        def test_failure(self):
            # self.assertFalse(True)
            self.assertTrue(True)


    # Exceptions seen

  the test passes.

* I open a new terminal_ then `change directory`_ to ``exceptions``

  .. code-block:: python
    :emphasize-lines: 1

    cd exceptions

* I add the new files_ and folder_ to git_ for tracking

  .. code-block:: python
    :emphasize-lines: 1

    git add .

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'setup project'

----

*********************************************************************************
test_catching_module_not_found_error
*********************************************************************************

:ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>` is :ref:`raised<how to raise an Exception>` when I try to import a :ref:`module<what is a module?>` that does NOT exist.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I change ``Testexceptions`` to ``TestExceptions`` to match the :ref:`CapWords format<CapWords>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4

    import unittest


    class TestExceptions(unittest.TestCase):

        def test_failure(self):

* I change :ref:`test_failure` to ``test_catching_module_not_found_error`` with an `import statement`_ in ``tests/test_exceptions.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3-4

    class TestExceptions(unittest.TestCase):

        def test_catching_module_not_found_error(self):
            import does_not_exist


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

  .. code-block:: shell

    ModuleNotFoundError: No module named 'does_not_exist'

  I cannot import a :ref:`module<what is a module?>` that does not exist. A :ref:`module<what is a module?>` is any file_ that ends in ``.py``

* I add :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>` to the list of :ref:`Exceptions<how to test if an Exception is raised>` seen

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 3
    :emphasize-text: ModuleNotFoundError

    # Exceptions seen
    # AssertionError
    # ModuleNotFoundError

I can make a file_ named ``does_not_exist.py`` to solve the problem. What I want to do is :ref:`catch/handle the Exception<how to use try...except...else>` in the test to show that ``import does_not_exist`` raises :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>` when the file_ does NOT exist and the test can continue running after confirming the :ref:`Exception<how to test if an Exception is raised>`.

----

*********************************************************************************
how to handle Exceptions
*********************************************************************************

The `try statement`_ is like an :ref:`if statement<if statements>` for :ref:`Exceptions<how to test if an Exception is raised>`. It tells the program_ what to do if an :ref:`Exception<how to test if an Exception is raised>` is :ref:`raised<how to raise an Exception>`. A simple way to think of it is

* ``try`` **something**
* ``except`` - if **something** raises an :ref:`Exception<how to test if an Exception is raised>` do something else

If the statement in the :ref:`try clause<how to handle Exceptions>` :ref:`raises the Exception<how to raise an Exception>` in the :ref:`except clause<how to handle Exceptions>`, Python_ runs the code in the :ref:`except block<how to handle Exceptions>`

.. code-block:: shell

      try:
  ┌───┴── do something
  └── except Exception:
      └── do something else

If the statement in the :ref:`try clause<how to handle Exceptions>` block works, Python_ exits the `try statement`_

.. code-block:: shell

      try:
  ┌───┴── do something
  │   except Exception:
  │       do something else

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a `try statement`_ to :ref:`test_catching_module_not_found_error` to :ref:`handle ModuleNotFoundError<how to handle Exceptions>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 2-5

        def test_catching_module_not_found_error(self):
            try:
                import does_not_exist
            except ModuleNotFoundError:
                pass


    # Exceptions seen

  the test passes because ``import does_not_exist`` :ref:`raises ModuleNotFoundError<what causes ModuleNotFoundError?>`.

  .. code-block:: shell

        try:
    ┌───┴── import does_not_exist
    └── except ModuleNotFoundError:
        └── pass

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_catching_module_not_found_error'

:ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>` is :ref:`raised<how to raise an Exception>` when I try to import a :ref:`module<what is a module?>` that does NOT exist.

----

*********************************************************************************
test_catching_name_error
*********************************************************************************

NameError_ is :ref:`raised<how to raise an Exception>` when I try to use a name that is not defined in the file_ I am working in.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a test for :ref:`NameError<test_catching_name_error>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 4-5

            except ModuleNotFoundError:
                pass

        def test_catching_name_error(self):
            not_defined


    # Exceptions seen

  the terminal_ is my friend, and shows NameError_

  .. code-block:: shell

    NameError: name 'not_defined' is not defined

  because there is no definition for ``not_defined`` in ``tests/test_exceptions.py``.

* I add NameError_ to the list of :ref:`Exceptions<how to test if an Exception is raised>` seen

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 4
    :emphasize-text: NameError

    # Exceptions seen
    # AssertionError
    # ModuleNotFoundError
    # NameError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a `try statement`_ to :ref:`test_catching_name_error` to :ref:`handle NameError<how to handle Exceptions>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 2-5

        def test_catching_name_error(self):
            try:
                not_defined
            except NameError:
                pass


    # Exceptions seen

  the test passes because ``not_defined`` :ref:`raises NameError<test_catching_name_error>`.

  .. code-block:: shell

        try:
    ┌───┴── not_defined
    └── except NameError:
        └── pass

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_catching_name_error'

NameError_ is :ref:`raised<how to raise an Exception>` when I try to use a name that is not defined in the file_.

----

*********************************************************************************
test_catching_attribute_error
*********************************************************************************

:ref:`AttributeError<what causes AttributeError?>` is :ref:`raised<how to raise an Exception>` when I try to get something that does NOT exist from an :ref:`object<everything is an object>` that exists.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a test for :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 4-5

            except NameError:
                pass

        def test_catching_attribute_error(self):
            src.exceptions.does_not_exist


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: shell

    NameError: name 'src' is not defined

* I add an `import statement`_ at the top of the file_ for the :ref:`module<what is a module?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.exceptions
    import unittest

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.exceptions'
                    has no attribute 'does_not_exist'

  ``src.exceptions.does_not_exist`` is like an address

  - ``src`` is the ``src`` folder_
  - ``exceptions`` is the ``exceptions`` folder_ in the ``src`` folder_
  - ``src.exceptions.does_not_exist`` is pointing to something named ``does_not_exist`` in ``__init__.py`` in the ``exceptions`` folder_ in the ``src`` folder_

  the failure happens because Python_ cannot find ``does_not_exist`` in the ``__init__.py`` file_ in the ``exceptions`` folder_ in the ``src`` folder_. I tried to get something that does NOT exist from an :ref:`object<everything is an object>` that exists.

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<how to test if an Exception is raised>` seen

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 5
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # ModuleNotFoundError
    # NameError
    # AttributeError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a `try statement`_ to :ref:`test_catching_attribute_error` to :ref:`handle AttributeError<how to handle Exceptions>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 2-5

        def test_catching_attribute_error(self):
            try:
                src.exceptions.does_not_exist
            except AttributeError:
                pass


    # Exceptions seen

  the test passes because ``src.exceptions.does_not_exist`` :ref:`raises AttributeError<what causes AttributeError?>`

  .. code-block:: shell

        try:
        └── src.exceptions.does_not_exist
            └── src
                └── exceptions
    ┌───────────────┴── __init__.py
    └── except AttributeError:
        └── pass

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_catching_attribute_error'

:ref:`AttributeError<what causes AttributeError?>` is :ref:`raised<how to raise an Exception>` when I try to get something that does NOT exist from an :ref:`object<everything is an object>` that exists.

----

*********************************************************************************
test_catching_type_error
*********************************************************************************

:ref:`TypeError<what causes TypeError?>` is :ref:`raised<how to raise an Exception>` when I try to use an :ref:`object<everything is an object>` in a way that it cannot be used.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a test for :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 4-5

            except AttributeError:
                pass

        def test_catching_type_error(self):
            src.exceptions.function_name('the input')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.exceptions'
                    has no attribute 'function_name'

* I open ``__init__.py`` from the ``exceptions`` folder_ in the ``src`` folder_

* I delete all the text in the file_, then add ``function_name`` to ``src/exceptions/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    function_name

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: shell

    NameError: name 'function_name' is not defined

  because there is no definition for ``function_name`` in ``src/exceptions/__init__.py``

* I point ``function_name`` to :ref:`None<what is None?>` to define it

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    function_name = None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

  a reminder that :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`.

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<how to test if an Exception is raised>` seen, in ``tests/test_exceptions.py``

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 6
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # ModuleNotFoundError
    # NameError
    # AttributeError
    # TypeError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a `try statement`_ to :ref:`test_catching_type_error` to :ref:`handle TypeError<how to handle Exceptions>`

.. code-block:: python
  :lineno-start: 25
  :emphasize-lines: 2-5

      def test_catching_type_error(self):
          try:
              src.exceptions.function_name('the input')
          except TypeError:
              pass


  # Exceptions seen

the test passes because ``src.exceptions.function_name('the input')`` :ref:`raises TypeError<what causes TypeError?>`.

.. code-block:: shell

      try:
      └── src.exceptions.function_name('the input')
          └── src
              └── exceptions
                  └── __init__.py
  ┌───────────────────┴── function_name = None
  └── except TypeError:
      └── pass

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I make ``function_name`` a :ref:`function<what is a function?>` in ``src/exceptions/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def function_name():
        return None

  the test is still green because :ref:`TypeError<what causes TypeError?>` is :ref:`raised<how to raise an Exception>` since the call from the test - ``src.exceptions.function_name('the input')`` sends ``'the input'`` as input and the ``function_name`` :ref:`function<what is a function?>` does not take input (the parentheses are empty).

* I add a parameter to the definition

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def function_name(parameter_name):
        return None

  the test is still green, because the statement no longer gets to the :ref:`except block<how to handle Exceptions>`

  .. code-block:: shell

        try:
        └── src.exceptions.function_name('the input')
            └── src
                └── exceptions
                    └── __init__.py
                        └── def function_name(parameter_name):
                            └── return None
        except TypeError:
            pass

  I need :ref:`a better try statement<how to use try...except...else>`.

----

*********************************************************************************
how to use try...except...else
*********************************************************************************

The :ref:`try statement<how to handle Exceptions>` has an `else clause`_ that I can use to make a program do something if the :ref:`Exception<how to test if an Exception is raised>` in the :ref:`except clause<how to handle Exceptions>` is not :ref:`raised<how to raise an Exception>`

* I add an `else clause`_ to the :ref:`try statement<how to handle Exceptions>` to :ref:`raise AssertionError<what causes AssertionError?>` if :ref:`TypeError<what causes TypeError?>` is not :ref:`raised<how to raise an Exception>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 6-7

        def test_catching_type_error(self):
            try:
                src.exceptions.function_name('the input')
            except TypeError:
                pass
            else:
                raise AssertionError


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    E           AssertionError

  because :ref:`TypeError<what causes TypeError?>` is NOT raised since the :ref:`function call<how to call a function with input>` matches the :ref:`definition<how to make a function that takes input>`.

  .. code-block:: shell

        try:
    ┌───┴── src.exceptions.function_name('the input')
    │        └── src
    │            └── exceptions
    │                └── __init__.py
    │                    └── def function_name(parameter_name):
    │                        └── return None
    │   except TypeError:
    │       pass
    └── else:
        └── raise AssertionError

* I undo the change

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def function_name():
        return

  the test is green again.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_catching_type_error'

:ref:`TypeError<what causes TypeError?>` is :ref:`raised<how to raise an Exception>` when I try to use an :ref:`object<everything is an object>` in a way that it cannot be used.

----

*********************************************************************************
add else clause to try statements
*********************************************************************************

* I add the `else clause`_ to :ref:`test_catching_attribute_error` to make sure it raises :ref:`AssertionError<what causes AssertionError?>` if :ref:`AttributeError<what causes AttributeError?>` is not :ref:`raised<how to raise an Exception>` by the code in the :ref:`try block<how to use try...except...else>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 6-7

        def test_catching_attribute_error(self):
            try:
                src.exceptions.does_not_exist
            except AttributeError:
                pass
            else:
                raise AssertionError

        def test_catching_type_error(self):

  the test is still green.

* I add the `else clause`_ to :ref:`test_catching_name_error` to make sure it raises :ref:`AssertionError<what causes AssertionError?>` if :ref:`NameError<test_catching_name_error>` is not :ref:`raised<how to raise an Exception>` by the code in the :ref:`try block<how to use try...except...else>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 6-7

        def test_catching_name_error(self):
            try:
                not_defined
            except NameError:
                pass
            else:
                raise AssertionError

        def test_catching_attribute_error(self):

  still green.

* I add the `else clause`_ to :ref:`test_catching_module_not_found_error` to make sure it raises :ref:`AssertionError<what causes AssertionError?>` if :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>` is not :ref:`raised<how to raise an Exception>` by the code in the :ref:`try block<how to use try...except...else>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 6-7

        def test_catching_module_not_found_error(self):
            try:
                import does_not_exist
            except ModuleNotFoundError:
                pass
            else:
                raise AssertionError

        def test_catching_name_error(self):

  green.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add else clause to try statements'

----

*********************************************************************************
extract assert_raises method
*********************************************************************************

The :ref:`try statements<how to use try...except...else>` all look the same, the only differences are the code in the :ref:`try block<how to use try...except...else>` and the :ref:`Exception<how to test if an Exception is raised>` in the :ref:`except clause<how to use try...except...else>`

.. code-block:: python

  try:
      code
  except Exception:
      pass
  else:
      raise AssertionError

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a :ref:`method<what is a method?>` for the :ref:`try statement<how to use try...except...else>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3-10

    class TestExceptions(unittest.TestCase):

        @staticmethod
        def assert_raises(code, exception):
            try:
                code
            except exception:
                pass
            else:
                raise AssertionError

        def test_catching_module_not_found_error(self):

* I use the :ref:`assert_raises method<extract assert_raises method>` in :ref:`test_catching_module_not_found_error`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 2-4

        def test_catching_module_not_found_error(self):
            self.assert_raises(
                import does_not_exist, ModuleNotFoundError
            )
            try:

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  because ``import does_not_exist`` runs before it is passed as input to the :ref:`assert_raises method<extract assert_raises method>`. I need a way to pass it as a value that will be run inside the :ref:`assert_raises method<extract assert_raises method>` not before.

* I add SyntaxError_ to the list of :ref:`Exceptions<how to test if an Exception is raised>` seen

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 7
    :emphasize-text: SyntaxError

    # Exceptions seen
    # AssertionError
    # ModuleNotFoundError
    # NameError
    # AttributeError
    # TypeError
    # SyntaxError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the ``import does_not_exist`` line in :ref:`test_catching_module_not_found_error` to a string_

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 3

        def test_catching_module_not_found_error(self):
            self.assert_raises(
                'import does_not_exist', ModuleNotFoundError
            )
            try:
                import does_not_exist
            except ModuleNotFoundError:
                pass
            else:
                raise AssertionError

        def test_catching_name_error(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E           AssertionError

  because the string_ (``'import does_not_exist'``) does not :ref:`raise ModuleNotFoundError<how to raise an Exception>`

  .. code-block:: shell

    assert_raises('import does_not_exist', ModuleNotFoundError)
    └── def assert_raises(code, exception):
        ├── code = 'import does_not_exist'
        ├── exception = ModuleNotFoundError
        └── try:
        ┌───┴── code
        │   except exception:
        │       pass
        └── else:
            └── raise AssertionError

  I still need a way to run the code in the string_ inside the :ref:`assert_raises method<extract assert_raises method>`.

----

*********************************************************************************
the exec function
*********************************************************************************

I can use the `exec built-in function`_ to run any Python_ code I pass as a string_ to it.

* I add exec_ to the :ref:`try block<how to use try...except...else>` in the :ref:`assert_raises method<extract assert_raises method>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4

        @staticmethod
        def assert_raises(code, exception):
            try:
                exec(code)
            except exception:
                pass
            else:
                raise AssertionError

        def test_catching_module_not_found_error(self):

  the test passes, showing that ``import does_not_exist`` raises :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>` which happens when I try to import a :ref:`module<what is a module?>` that does NOT exist.

  .. code-block:: shell

    assert_raises('import does_not_exist', ModuleNotFoundError)
    └── def assert_raises(code, exception):
        ├── code = 'import does_not_exist'
        ├── exception = ModuleNotFoundError
        └── try:
        ┌───┴── exec(code)
        └── except exception:
            └── pass
            else:
                raise AssertionError

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the :ref:`try block<how to use try...except...else>` from :ref:`test_catching_module_not_found_error` because it is now a repetition of the :ref:`assert_raises method<extract assert_raises method>`

  .. code-block:: python
    :lineno-start: 16

        def test_catching_module_not_found_error(self):
            self.assert_raises(
                'import does_not_exist', ModuleNotFoundError
            )

        def test_catching_name_error(self):

* I use the :ref:`assert_raises method<extract assert_raises method>` in :ref:`test_catching_name_error`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2

    def test_catching_name_error(self):
        self.assert_raises('not_defined', ModuleNotFoundError)
        try:

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: python

    NameError: name 'not_defined' is not defined

  because :ref:`NameError<test_catching_name_error>` is not :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>` or a :ref:`child<how to test if something is a subclass>` of :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`.

* I change the expected :ref:`Exception<how to test if an Exception is raised>` to :ref:`NameError<test_catching_name_error>`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2

        def test_catching_name_error(self):
            self.assert_raises('not_defined', NameError)
            try:
                not_defined
            except NameError:
                pass
            else:
                raise AssertionError

        def test_catching_attribute_error(self):

  the test passes, showing that ``not_defined`` raises :ref:`NameError<test_catching_name_error>` which happens when I try to use a name that is not defined in the file_.

* I remove the :ref:`try block<how to use try...except...else>` from :ref:`test_catching_name_error` because it is now a repetition of the :ref:`assert_raises method<extract assert_raises method>`

  .. code-block:: python
    :lineno-start: 21

        def test_catching_name_error(self):
            self.assert_raises('not_defined', NameError)

        def test_catching_attribute_error(self):

* I use the :ref:`assert_raises method<extract assert_raises method>` in :ref:`test_catching_attribute_error`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 2-4

        def test_catching_attribute_error(self):
            self.assert_raises(
                'src.exceptions.does_not_exist', NameError
            )
            try:

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.exceptions'
                    has no attribute 'does_not_exist'

  because :ref:`AttributeError<what causes AttributeError?>` is not :ref:`NameError<test_catching_name_error>` or a :ref:`child<how to test if something is a subclass>` of :ref:`NameError<test_catching_name_error>`.

* I change the expected :ref:`Exception<how to test if an Exception is raised>` to :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 3

        def test_catching_attribute_error(self):
            self.assert_raises(
                'src.exceptions.does_not_exist', AttributeError
            )
            try:
                src.exceptions.does_not_exist
            except AttributeError:
                pass
            else:
                raise AssertionError

        def test_catching_type_error(self):

  the test passes, showing that ``src.exceptions.does_not_exist`` raises :ref:`AttributeError<what causes AttributeError?>` which happens when I try to get something that does NOT exist from an :ref:`object<everything is an object>` that exists.

* I remove the :ref:`try block<how to use try...except...else>` from :ref:`test_catching_attribute_error` because it is now a repetition of the :ref:`assert_raises method<extract assert_raises method>`

  .. code-block:: python
    :lineno-start: 24

        def test_catching_attribute_error(self):
            self.assert_raises(
                'src.exceptions.does_not_exist', AttributeError
            )

        def test_catching_type_error(self):

* I use the :ref:`assert_raises method<extract assert_raises method>` in :ref:`test_catching_type_error`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2-5

        def test_catching_type_error(self):
            self.assert_raises(
                "src.exceptions.function_name('the input')",
                AttributeError
            )
            try:

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: function_name() takes
               0 positional arguments but 1 was given

  because :ref:`TypeError<what causes TypeError?>` is not :ref:`AttributeError<what causes AttributeError?>` or a :ref:`child<how to test if something is a subclass>` of :ref:`AttributeError<what causes AttributeError?>`.

* I change the expected :ref:`Exception<how to test if an Exception is raised>` to :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 4

        def test_catching_type_error(self):
            self.assert_raises(
                "src.exceptions.function_name('the input')",
                TypeError
            )
            try:
                src.exceptions.function_name('the input')
            except TypeError:
                pass
            else:
                raise AssertionError


    # Exceptions seen

  the test passes, showing that ``src.exceptions.function_name('the input')`` raises :ref:`TypeError<what causes TypeError?>` which happens when I try to use an :ref:`object<everything is an object>` in a way that it cannot be used.

* I remove the :ref:`try block<how to use try...except...else>` from :ref:`test_catching_type_error` because it is now a repetition of the :ref:`assert_raises method<extract assert_raises method>`

  .. code-block:: python
    :lineno-start: 29

        def test_catching_type_error(self):
            self.assert_raises(
                "src.exceptions.function_name('the input')",
                TypeError
            )


    # Exceptions seen

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract assert_raises method'

----

*********************************************************************************
test_catching_index_error
*********************************************************************************

:ref:`IndexError<test_index_error>` is :ref:`raised<how to raise an Exception>` when I try to :ref:`index a list<test_index_returns_first_position_of_item_in_a_list>`, tuple_ or string_ with a number that is

- bigger than or the same as the number of items in the :ref:`list<what is a list?>`, tuple_ or string_
- smaller than the negative of the number of items in the :ref:`list<what is a list?>`, tuple_ or string_

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a test for :ref:`IndexError<test_index_error>` with a string_

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 7-8

        def test_catching_type_error(self):
            self.assert_raises(
                "src.exceptions.function_name('the input')",
                TypeError
            )

        def test_catching_index_error(self):
            'a string'[0]


    # Exceptions seen

  the test is still green because the first item in a :ref:`list<what is a list?>`, tuple_ or string_ has ``0`` as its :ref:`index<test_index_returns_first_position_of_item_in_a_list>` (its position in the container).

* I change the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` from ``0`` to ``7``

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 2

        def test_catching_index_error(self):
            'a string'[7]


    # Exceptions seen

  the test is still green because the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` for the last item is the total number of items minus ``1``, which is ``7`` in this case.

* If I use a number that is bigger than the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` of the last item

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 2

        def test_catching_index_error(self):
            'a string'[8]


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`IndexError<test_index_error>`

  .. code-block:: python

    IndexError: string index out of range

  I cannot use a number that is bigger than the index of the last item in a string_ or that is greater than or equal to the length of the string_.

* I add :ref:`IndexError<test_index_error>` to the list of :ref:`Exceptions<how to test if an Exception is raised>` seen

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 8
    :emphasize-text: IndexError

    # Exceptions seen
    # AssertionError
    # ModuleNotFoundError
    # NameError
    # AttributeError
    # TypeError
    # SyntaxError
    # IndexError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I use the :ref:`assert_raises method<extract assert_raises method>` in :ref:`test_catching_index_error`

.. code-block:: python
  :lineno-start: 35
  :emphasize-lines: 2

      def test_catching_index_error(self):
          self.assert_raises("'a string'[8]", IndexError)


  # Exceptions seen

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I can also :ref:`index<test_index_returns_first_position_of_item_in_a_list>` with negative numbers, the one for the last item is ``-1``, like reading from right to left

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 3

        def test_catching_index_error(self):
            self.assert_raises("'a string'[8]", IndexError)
            'a string'[-1]


    # Exceptions seen

  the test is still green.

* I change the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` from ``-1`` to ``-8`` for the first item, which is negative the total number of items (like reading from right to left)

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 3

        def test_catching_index_error(self):
            self.assert_raises("'a string'[8]", IndexError)
            'a string'[-8]


    # Exceptions seen

  still green.

* I use a negative number that is smaller than the negative of the number of characters in the string_

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 3

        def test_catching_index_error(self):
            self.assert_raises("'a string'[8]", IndexError)
            'a string'[-9]


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`IndexError<test_index_error>`

  .. code-block:: python

    IndexError: string index out of range

* I use the :ref:`assert_raises method<extract assert_raises method>` to :ref:`handle the Exception<how to use try...except...else>`

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 3

        def test_catching_index_error(self):
            self.assert_raises("'a string'[8]", IndexError)
            self.assert_raises("'a string'[-9]", IndexError)


    # Exceptions seen

  the test is green again. I cannot use a number that is smaller than the negative of the total number of items in the string_ to :ref:`index the string<test_index_returns_first_position_of_item_in_a_list>`.

* I add a tuple_ to :ref:`test_catching_index_error`

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 5

        def test_catching_index_error(self):
            self.assert_raises("'a string'[8]", IndexError)
            self.assert_raises("'a string'[-9]", IndexError)

            (0, 1, 2, 'n')[1]


    # Exceptions seen

  the test is still green because ``1`` is the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` of the second item.

* I use a number that is bigger than the number of items in the tuple_

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 5

        def test_catching_index_error(self):
            self.assert_raises("'a string'[8]", IndexError)
            self.assert_raises("'a string'[-9]", IndexError)

            (0, 1, 2, 'n')[100]


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`IndexError<test_index_error>`

  .. code-block:: python

    IndexError: tuple index out of range

* I use the :ref:`assert_raises method<extract assert_raises method>`

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 5-7

        def test_catching_index_error(self):
            self.assert_raises("'a string'[8]", IndexError)
            self.assert_raises("'a string'[-9]", IndexError)

            self.assert_raises(
                "(0, 1, 2, 'n')[100]", IndexError
            )


    # Exceptions seen

  the test passes.

* I use a negative number to :ref:`index<test_index_returns_first_position_of_item_in_a_list>` the tuple_

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 4

            self.assert_raises(
                "(0, 1, 2, 'n')[100]", IndexError
            )
            (0, 1, 2, 'n')[-2]


    # Exceptions seen

  the test is still green.

* I use a number that is smaller than the negative of the number of items in the tuple_

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 4

            self.assert_raises(
                "(0, 1, 2, 'n')[100]", IndexError
            )
            (0, 1, 2, 'n')[-100]


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`IndexError<test_index_error>`

  .. code-block:: python

    IndexError: tuple index out of range

  I cannot use a number that is smaller than the negative of the number of items in a tuple_.

* I use the :ref:`assert_raises method<extract assert_raises method>` to :ref:`catch the Exception<how to use try...except...else>`

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 8-10

        def test_catching_index_error(self):
            self.assert_raises("'a string'[8]", IndexError)
            self.assert_raises("'a string'[-9]", IndexError)

            self.assert_raises(
                "(0, 1, 2, 'n')[100]", IndexError
            )
            self.assert_raises(
                "(0, 1, 2, 'n')[-100]", IndexError
            )

        def test_catching_key_error(self):

  the test passes.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_catching_index_error'

:ref:`IndexError<test_index_error>` is :ref:`raised<how to raise an Exception>` when I try to :ref:`index a list<test_index_returns_first_position_of_item_in_a_list>`, tuple_ or string_ with a number that is

- bigger than or the same as the number of items in the :ref:`list<what is a list?>`, tuple_ or string_.
- smaller than the negative of the number of items in the :ref:`list<what is a list?>`, tuple_ or string_.

----

*********************************************************************************
test_catching_key_error
*********************************************************************************

:ref:`KeyError<test_key_error>` is :ref:`raised<how to raise an Exception>` when I try to use a :ref:`key<test_keys_of_a_dictionary>` that is NOT in a :ref:`dictionary<what is a dictionary?>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a test for :ref:`KeyError<test_key_error>` with a :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 5-6

            self.assert_raises(
                "(0, 1, 2, 'n')[-100]", IndexError
            )

        def test_catching_key_error(self):
            {'key': 'value'}['key']


    # Exceptions seen

  the test is green because ``'key'`` is a :ref:`key<test_keys_of_a_dictionary>` of the ``{'key': 'value'}`` :ref:`dictionary<what is a dictionary?>`.

* If I use a :ref:`key<test_keys_of_a_dictionary>` that is NOT in the :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 2

        def test_catching_key_error(self):
            {'key': 'value'}['not_in_dictionary']


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`KeyError<test_key_error>`

  .. code-block:: shell

    KeyError: 'not_in_dictionary'

* I add :ref:`KeyError<test_key_error>` to the list of :ref:`Exceptions<how to test if an Exception is raised>` seen

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 9
    :emphasize-text: KeyError

    # Exceptions seen
    # AssertionError
    # ModuleNotFoundError
    # NameError
    # AttributeError
    # TypeError
    # SyntaxError
    # IndexError
    # KeyError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I use the :ref:`assert_raises method<extract assert_raises method>` to :ref:`catch the Exception<how to use try...except...else>` in :ref:`test_catching_key_error`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 2-5

        def test_catching_key_error(self):
            self.assert_raises(
                "{'key': 'value'}['not_in_dictionary']",
                KeyError
            )


    # Exceptions seen

  the test passes.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_catching_key_error'

:ref:`KeyError<test_key_error>` is :ref:`raised<how to raise an Exception>` when I try to use a :ref:`key<test_keys_of_a_dictionary>` that is NOT in a :ref:`dictionary<what is a dictionary?>`.

----

*********************************************************************************
test_catching_zero_division_error
*********************************************************************************

ZeroDivisionError_ is :ref:`raised<how to raise an Exception>` when I try to divide a number by ``0``.

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a test for ZeroDivisionError_

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 7-8

        def test_catching_key_error(self):
            self.assert_raises(
                "{'key': 'value'}['not_in_dictionary']",
                KeyError
            )

        def test_catching_zero_division_error(self):
            1 / 0


    # Exceptions seen

  the terminal_ is my friend, and shows ZeroDivisionError_

  .. code-block:: python

    ZeroDivisionError: division by zero

  because I cannot divide a number by ``0``.

* I add ZeroDivisionError_ to the list of :ref:`Exceptions<how to test if an Exception is raised>` seen

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 10
    :emphasize-text: ZeroDivisionError

    # Exceptions seen
    # AssertionError
    # ModuleNotFoundError
    # NameError
    # AttributeError
    # TypeError
    # SyntaxError
    # IndexError
    # KeyError
    # ZeroDivisionError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I use the :ref:`assert_raises method<extract assert_raises method>` to :ref:`catch the Exception<how to use try...except...else>` in :ref:`test_catching_zero_division_error`

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 2

        def test_catching_zero_division_error(self):
            self.assert_raises('1 / 0', ZeroDivisionError)


    # Exceptions seen

  the test passes.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_catching_zero_division_error'

ZeroDivisionError_ is :ref:`raised<how to raise an Exception>` when I try to divide a number by ``0``.

----

*********************************************************************************
test_catching_exceptions
*********************************************************************************

=================================================================================
how to raise an Exception
=================================================================================

----

I can cause an :ref:`Exception<how to test if an Exception is raised>` to happen with the `raise statement`_.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a test with the `raise statement`_

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 4-5

        def test_catching_zero_division_error(self):
            self.assert_raises('1 / 0', ZeroDivisionError)

        def test_catching_exceptions(self):
            raise Exception


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`Exception<how to test if an Exception is raised>`

  .. code-block:: python

    Exception

  :ref:`Exception<how to test if an Exception is raised>` is the mother of all the :ref:`Exceptions<how to test if an Exception is raised>` covered so far, they :ref:`inherit<everything is an object>` from it.

* I can use the `raise statement`_ to cause any :ref:`Exception<how to test if an Exception is raised>` I want

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 2

        def test_catching_exceptions(self):
            raise AssertionError


    # Exceptions seen

  the terminal_ shows the :ref:`Exception<how to test if an Exception is raised>` I give the `raise statement`_

  .. code-block:: python

    AssertionError

* I change the :ref:`Exception<how to test if an Exception is raised>` back

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 2

        def test_catching_exceptions(self):
            raise Exception


    # Exceptions seen

  the terminal_ shows :ref:`Exception<how to test if an Exception is raised>`

  .. code-block:: python

    Exception

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I use the :ref:`assert_raises method<extract assert_raises method>` to :ref:`catch Exception<how to use try...except...else>`

.. code-block:: python
  :lineno-start: 55
  :emphasize-lines: 2

      def test_catching_exceptions(self):
          self.assert_raises('raise Exception', Exception)


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I can use :ref:`Exception<how to test if an Exception is raised>` to catch any of the :ref:`Exceptions<how to test if an Exception is raised>` that :ref:`inherit<everything is an object>` from it (its :ref:`children/subclasses<how to test if something is a subclass>`)

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 4-5, 9-10

        def test_catching_key_error(self):
            self.assert_raises(
                "{'key': 'value'}['not_in_dictionary']",
                # KeyError
                Exception
            )

        def test_catching_zero_division_error(self):
            # self.assert_raises('1 / 0', ZeroDivisionError)
            self.assert_raises('1 / 0', Exception)

        def test_catching_exceptions(self):

  the tests are still green.

  The problem with using :ref:`Exception<how to test if an Exception is raised>` to catch its children, is it does not tell anyone that reads the code what the actual :ref:`Exception<how to test if an Exception is raised>` is. It is better to be specific.

  From the :PEP:`Zen of Python <20>`: ``Explicit is better than implicit``. I change the :ref:`Exceptions<how to test if an Exception is raised>` back.

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 4, 8

    def test_catching_key_error(self):
        self.assert_raises(
            "{'key': 'value'}['not_in_dictionary']",
            KeyError
        )

    def test_catching_zero_division_error(self):
        self.assert_raises('1 / 0', ZeroDivisionError)

    def test_catching_exceptions(self):

* I cannot use sibling or cousin :ref:`Exceptions<how to test if an Exception is raised>` to catch other :ref:`Exceptions<how to test if an Exception is raised>`

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 9-10

        def test_catching_index_error(self):
            self.assert_raises("'a string'[8]", IndexError)
            self.assert_raises("'a string'[-9]", IndexError)

            self.assert_raises(
                "(0, 1, 2, 'n')[100]", IndexError
            )
            self.assert_raises(
                # "(0, 1, 2, 'n')[-100]", IndexError
                "(0, 1, 2, 'n')[-100]", ModuleNotFoundError
            )

        def test_catching_key_error(self):

  the terminal_ is my friend, and shows :ref:`IndexError<test_index_error>`

  .. code-block:: shell

    IndexError: tuple index out of range

  because :ref:`IndexError<test_index_error>` is not :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>` even though they are both :ref:`Exceptions<how to test if an Exception is raised>`.

* I undo the change

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 9

        def test_catching_index_error(self):
            self.assert_raises("'a string'[8]", IndexError)
            self.assert_raises("'a string'[-9]", IndexError)

            self.assert_raises(
                "(0, 1, 2, 'n')[100]", IndexError
            )
            self.assert_raises(
                "(0, 1, 2, 'n')[-100]", IndexError
            )

        def test_catching_key_error(self):

  the test is green again.

* I cannot use a :ref:`child<how to test if something is a subclass>` :ref:`Exceptions<how to test if an Exception is raised>` to catch its parent :ref:`Exception<how to test if an Exception is raised>`.

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 2-5

        def test_catching_exceptions(self):
            # self.assert_raises('raise Exception', Exception)
            self.assert_raises(
                'raise Exception', ZeroDivisionError
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`Exception<how to test if an Exception is raised>`

  .. code-block:: python

    Exception

  because :ref:`Exception<how to test if an Exception is raised>` is not ZeroDivisionError_ or a :ref:`child<how to test if something is a subclass>` of ZeroDivisionError_, even though ZeroDivisionError_ is an :ref:`Exception<how to test if an Exception is raised>`.

* I undo the change

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 2

        def test_catching_exceptions(self):
            self.assert_raises('raise Exception', Exception)


    # Exceptions seen

  the test is green again.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_catching_exceptions'

I know :ref:`how to test if an Exception is raised`.

----

*********************************************************************************
another way to test if an Exception is raised
*********************************************************************************

:ref:`unittest.TestCase<test_dir_unittest_testcase>` has a :ref:`method<what is a method?>` I can use to test if code :ref:`raises an Exception<how to raise an Exception>`, it is called assertRaises_.

assertRaises_ checks that the code in its context :ref:`raises the Exception<how to raise an Exception>` it is given in parentheses.

----

* I add the failing line for :ref:`test_catching_exceptions`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 3

        def test_catching_exceptions(self):
            self.assert_raises('raise Exception', Exception)
            raise Exception


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`Exception<how to test if an Exception is raised>`.

* I add assertRaises_ to :ref:`handle Exception<how to handle Exceptions>`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 3-4

        def test_catching_exceptions(self):
            self.assert_raises('raise Exception', Exception)
            with self.assertRaises(Exception):
                raise Exception


    # Exceptions seen

  the test passes, showing that assertRaises_ checks that the code in its context (``raise Exception``), :ref:`raises the Exception<how to raise an Exception>` it is given in parentheses.

* I add a failing line to :ref:`test_catching_zero_division_error`

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 3

        def test_catching_zero_division_error(self):
            self.assert_raises('1 / 0', ZeroDivisionError)
            1 / 0

        def test_catching_exceptions(self):

  the terminal_ is my friend, and shows ZeroDivisionError_

* I add assertRaises_ to :ref:`handle ZeroDivisionError<how to handle Exceptions>`.

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 3-4

        def test_catching_zero_division_error(self):
            self.assert_raises('1 / 0', ZeroDivisionError)
            with self.assertRaises(ZeroDivisionError):
                1 / 0

        def test_catching_exceptions(self):

  the test passes, showing that assertRaises_ checks that the code in its context (``1 / 0``), :ref:`raises the Exception<how to raise an Exception>` it is given in parentheses (ZeroDivisionError_).

* I add a failing line to :ref:`test_catching_key_error`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 6

        def test_catching_key_error(self):
            self.assert_raises(
                "{'key': 'value'}['not_in_dictionary']",
                KeyError
            )
            {'key': 'value'}['not_in_dictionary']

        def test_catching_zero_division_error(self):

  the terminal_ is my friend, and shows :ref:`KeyError<test_key_error>`.

* I add assertRaises_ to :ref:`handle KeyError<how to handle Exceptions>`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 6-7

        def test_catching_key_error(self):
            self.assert_raises(
                "{'key': 'value'}['not_in_dictionary']",
                KeyError
            )
            with self.assertRaises(KeyError):
                {'key': 'value'}['not_in_dictionary']

        def test_catching_zero_division_error(self):

  the test passes, showing that assertRaises_ checks that the code in its context (``{'key': 'value'}['not_in_dictionary']``), :ref:`raises the Exception<how to raise an Exception>` it is given in parentheses (:ref:`KeyError<test_key_error>`).

* I add a failure with the `assertRaises method`_ to :ref:`test_catching_index_error`

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 5-6

        def test_catching_index_error(self):
            self.assert_raises("'a string'[8]", IndexError)
            self.assert_raises("'a string'[-9]", IndexError)

            with self.assertRaises(ZeroDivisionError):
                'a string'[8]

            self.assert_raises(
                "(0, 1, 2, 'n')[100]", IndexError
            )

  the terminal_ is my friend, and shows :ref:`IndexError<test_index_error>`.

* I change ZeroDivisionError_ to :ref:`IndexError<test_index_error>` in :ref:`test_catching_index_error`

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 5

        def test_catching_index_error(self):
            self.assert_raises("'a string'[8]", IndexError)
            self.assert_raises("'a string'[-9]", IndexError)

            with self.assertRaises(IndexError):
                'a string'[8]

  the test passes, showing that assertRaises_ checks that the code in its context (``'a string'[8]``), :ref:`raises the Exception<how to raise an Exception>` it is given in parentheses (:ref:`IndexError<test_index_error>`).

* I add assertRaises_ for the second statement in :ref:`test_catching_index_error`

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 3-4

            with self.assertRaises(IndexError):
                'a string'[8]
            with self.assertRaises(IndexError):
                'a string'[0]

            self.assert_raises(
                "(0, 1, 2, 'n')[100]", IndexError
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: IndexError not raised

  a better error message than the one from my :ref:`assert_raises method<extract assert_raises method>`

  .. code-block:: python

    AssertionError

* I change the statement to make it raise :ref:`IndexError<test_index_error>`

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 4

            with self.assertRaises(IndexError):
                'a string'[8]
            with self.assertRaises(IndexError):
                'a string'[-9]

            self.assert_raises(
                "(0, 1, 2, 'n')[100]", IndexError
            )

  the test passes, showing that assertRaises_ checks that the code in its context (``'a string'[-9]``), :ref:`raises the Exception<how to raise an Exception>` it is given in parentheses (:ref:`IndexError<test_index_error>`).

* I add assertRaises_ for the third statement

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 8-9

            self.assert_raises(
                "(0, 1, 2, 'n')[100]", IndexError
            )
            self.assert_raises(
                "(0, 1, 2, 'n')[-100]", IndexError
            )

            with self.assertRaises(IndexError):
                (0, 1, 2, 'n')[100]

        def test_catching_key_error(self):

  the test is still green.

* I add assertRaises_ for the fourth statement in :ref:`test_catching_index_error`

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 3-4

            with self.assertRaises(IndexError):
                (0, 1, 2, 'n')[100]
            with self.assertRaises(IndexError):
                (0, 1, 2, 'n')[-100]

        def test_catching_key_error(self):

  still green.

* I use assertRaises_ in :ref:`test_catching_type_error`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 6-7

        def test_catching_type_error(self):
            self.assert_raises(
                "src.exceptions.function_name('the input')",
                TypeError
            )
            with self.assertRaises(TypeError):
                src.exceptions.function_name('the input')

        def test_catching_index_error(self):

  green, showing that assertRaises_ checks that the code in its context (``src.exceptions.function_name('the input')``), :ref:`raises the Exception<how to raise an Exception>` it is given in parentheses (:ref:`TypeError<what causes TypeError?>`).

* I add assertRaises_ to :ref:`test_catching_attribute_error`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 5-6

        def test_catching_attribute_error(self):
            self.assert_raises(
                'src.exceptions.does_not_exist', AttributeError
            )
            with self.assertRaises(AttributeError):
                src.exceptions.does_not_exist

        def test_catching_type_error(self):

  still green, showing that assertRaises_ checks that the code in its context (``src.exceptions.does_not_exist``), :ref:`raises the Exception<how to raise an Exception>` it is given in parentheses (:ref:`AttributeError<what causes AttributeError?>`).

* I use the `assertRaises method`_ in :ref:`test_catching_name_error`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 3-4

        def test_catching_name_error(self):
            self.assert_raises('not_defined', NameError)
            with self.assertRaises(NameError):
                not_defined

        def test_catching_attribute_error(self):

  the test is still green.

* I use assertRaises_ in :ref:`test_catching_module_not_found_error`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 5-6

        def test_catching_module_not_found_error(self):
            self.assert_raises(
                'import does_not_exist', ModuleNotFoundError
            )
            with self.assertRaises(ModuleNotFoundError):
                import src.exceptions

        def test_catching_name_error(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: ModuleNotFoundError not raised

  because ``import src.exceptions`` does not :ref:`raise ModuleNotFoundError<how to raise an Exception>`

* I change the statement

  .. code-block:: python
    :lineno-start: 16

        def test_catching_module_not_found_error(self):
            self.assert_raises(
                'import does_not_exist', ModuleNotFoundError
            )
            with self.assertRaises(ModuleNotFoundError):
                import does_not_exist

        def test_catching_name_error(self):

  the test passes, showing that assertRaises_ checks that the code in its context (``import does_not_exist``), :ref:`raises the Exception<how to raise an Exception>` it is given in parentheses (:ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`).

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'use assertRaises'

*********************************************************************************
one exception one exception handler
*********************************************************************************

The assertRaises_ in :ref:`test_catching_index_error` all catch the same :ref:`Exception<how to test if an Exception is raised>`, the only difference is the actual statements that cause :ref:`IndexError<test_index_error>`

* If I remove the second assertRaises_

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 7

        def test_catching_index_error(self):
            self.assert_raises("'a string'[8]", IndexError)
            self.assert_raises("'a string'[-9]", IndexError)

            with self.assertRaises(IndexError):
                'a string'[8]
            # with self.assertRaises(IndexError):
                'a string'[-9]

  the test is still green for ``'a string'[-9]`` which should cause :ref:`IndexError<test_index_error>`, this makes it look like a second assertRaises_ is a repetition.

* If I add a `raise statement`_ before ``'a string'[-9]``

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 4

            with self.assertRaises(IndexError):
                'a string'[8]
            # with self.assertRaises(IndexError):
                raise Exception
                'a string'[-9]

  the test is still green, which is not the expected behavior.

  - :ref:`Exception<how to test if an Exception is raised>` is not :ref:`IndexError<test_index_error>` and still does not get :ref:`raised<how to raise an Exception>`, which means the assertRaises_ exits after the first line that causes :ref:`IndexError<test_index_error>` and does not run the other lines.
  - It should only catch :ref:`IndexError<test_index_error>` NOT :ref:`Exception<how to test if an Exception is raised>` since I cannot use a :ref:`child Exception<how to test if something is a subclass>` to catch its parent.

* If I move the `raise statement`_ above the first :ref:`IndexError<test_index_error>`

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 2

            with self.assertRaises(IndexError):
                raise Exception
                'a string'[8]
            # with self.assertRaises(IndexError):
                'a string'[-9]


  the terminal_ is my friend, and shows :ref:`Exception<how to test if an Exception is raised>`

  .. code-block:: python

    Exception

  because it is NOT :ref:`IndexError<test_index_error>`, this is the expected behavior.

* I undo the changes

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 3-6

            with self.assertRaises(IndexError):
                'a string'[8]
            with self.assertRaises(IndexError):
                'a string'[-9]

  the test is green again.

As a rule of thumb I write one line of code for one :ref:`Exception<how to test if an Exception is raised>`, this way I always know which line caused which :ref:`Exception<how to test if an Exception is raised>`.

----

*********************************************************************************
close the exceptions project
*********************************************************************************

* I close ``tests/test_exceptions.py``

* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``exceptions``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ is my friend, and shows

  .. code-block:: PowerShell

    ...\pumping_python

  I am back in the ``pumping_python`` directory_.

----

*********************************************************************************
review
*********************************************************************************

I ran tests to show that I can use the :ref:`try statement<how to handle Exceptions>` and assertRaises_ to catch :ref:`Exceptions<how to test if an Exception is raised>`

----

:ref:`How many questions can you answer after going through this chapter?<questions about testing Exceptions>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<how to handle Exceptions (Errors): tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

* :ref:`I know how to make a Python Test Driven Development environment manually<how to make a Python Test Driven Development environment manually>`.
* :ref:`I know what a Python module is<what is a module?>`.
* :ref:`I know how to run tests automatically<how to run tests automatically>`.
* :ref:`I know what an assertion is<what is an assertion?>`.
* :ref:`I know how to make functions<what is a function?>`.
* :ref:`I know how to make a person with strings<how to make a person with strings>`.
* :ref:`I know how to make functions that take input<functions that take input>`.
* :ref:`I know what causes TypeError<what causes TypeError?>`.
* :ref:`I know how to place values in strings<telephone>`.
* :ref:`I know how to make a person say hello with f-strings<how to make a person with f-strings>`.
* :ref:`I know how to separate tests from solutions<separate and equal>`.
* :ref:`I know what causes AttributeError<what causes AttributeError?>`.
* :ref:`I know how to make a person with a class<how to make a person with a class>`.
* :ref:`I know that everything in Python is an object<everything is an object>`.
* :ref:`I know how to use the unittest library<another way to write tests>`.
* :ref:`I know how to use the datetime library<test person with datetime>`.
* :ref:`I know what None is<what is None?>`.
* :ref:`I know how to make a person with conditions<how to make a person with conditions>`.
* :ref:`I know how Python groups objects into False or True<what are booleans?>`.
* :ref:`I know how to make a Python Test Driven Development environment automatically<how to make a Python Test Driven Development environment automatically>`.
* :ref:`I know how to write programs that make decisions<truth table>`.
* :ref:`I know how to make a Python Test Driven Development environment automatically with variables<how to make a Python Test Driven Development environment automatically with variables>`.
* :ref:`I know how to make a person with Exceptions<how to make a person with Exceptions>`.
* :ref:`I know how to test if an Exception is raised<how to test if an Exception is raised>`.

:ref:`Would you like to test handling Exceptions in programs?<how to handle Exceptions in programs>`

-----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too.

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->