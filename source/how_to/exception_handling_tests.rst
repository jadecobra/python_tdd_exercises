.. include:: ../links.rst

#################################################################################
how to test that an Exception is raised
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/xAgoCiCZIt0?si=CKmBIYAZU71gk45I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

----

.. contents:: table of contents
  :local:
  :depth: 1

----

When an error happens in Python, an Exception_ is raised breaking execution of the program, this means nothing past the line that caused it will run.

It is useful because there is a problem that needs to be solved for the program to continue as expected. It can be a pain when it causes the program to stop early. What if I want it to run with errors? I may want it to give messages to the user who does not understand or care about the details of the error.

Exception_ Handling is a way to deal with this, it allows programs to make decisions when one happens.

.. _test_catching_module_not_found_error_in_tests:

*********************************************************************************
test_catching_module_not_found_error_in_tests
*********************************************************************************

red: make it fail
#################################################################################

* I open a terminal to run :ref:`makePythonTdd.sh` with ``exceptions`` as the name of the project

  .. code-block:: python

    ./makePythonTdd.sh exceptions

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 exceptions

  it makes the folders and files that are needed, installs packages, runs the first test, and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_exceptions.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click on ``tests/test_exceptions.py:7`` with the mouse to open it
* then change ``True`` to ``False`` to make the test pass
* and change ``test_failure`` to ``test_catching_module_not_found_error_in_tests`` with an `import statement`_

  .. code-block:: python

    class TestException(unittest.TestCase):

        def test_catching_module_not_found_error_in_tests(self):
            import does_not_exist

  the terminal shows a :ref:`ModuleNotFoundError`

  .. code-block:: python

    ModuleNotFoundError: No module named 'does_not_exist'

green: make it pass
#################################################################################

* I add it to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError

  I can take care of this error by making the module, but I want to catch or handle the exception in the test
* I add the `unittest.TestCase.assertRaises`_ :ref:`method<functions>` introduced in :doc:`/how_to/calculator` to make sure that a :ref:`ModuleNotFoundError` is raised when I try to import ``does_not_exist``

  .. code-block:: python

    def test_catching_module_not_found_error_in_tests(self):
        with self.assertRaises(ModuleNotFoundError):
            import does_not_exist

  and the terminal shows passing tests

----

*********************************************************************************
test_catching_name_error_in_tests
*********************************************************************************

red: make it fail
#################################################################################

* I add a failing test

  .. code-block:: python

    def test_catching_name_error_in_tests(self):
        does_not_exist

  the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'does_not_exist' is not defined

* I add the exception to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # NameError

green: make it pass
#################################################################################

when I add a `unittest.TestCase.assertRaises`_ to the test

.. code-block:: python

  def test_catching_name_error_in_tests(self):
      with self.assertRaises(NameError):
          does_not_exist

the terminal shows passing tests

---

*********************************************************************************
test_catching_attribute_error_in_tests
*********************************************************************************

red: make it fail
#################################################################################

* I add a new failing test

  .. code-block:: python

    def test_catching_attribute_error_in_tests(self):
        src.exceptions.does_not_exist

  the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'src.exceptions' is not defined

* I add an `import statement`_

  .. code-block:: python

    import src.exceptions
    import unittest

  the terminal shows an:ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.exceptions' has no attribute 'does_not_exist'

* I add the exception to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # NameError
    # AttributeError

green: make it pass
#################################################################################

I add a call to the `unittest.TestCase.assertRaises`_ :ref:`method<functions>`

.. code-block:: python

  def test_catching_attribute_error_in_tests(self):
      with self.assertRaises(AttributeError):
          src.exceptions.does_not_exist

the terminal shows passing tests

----

*********************************************************************************
test_catching_type_error_in_tests
*********************************************************************************

red: make it fail
#################################################################################

* I add a failing test for a :ref:`TypeError`

  .. code-block:: python

    def test_catching_type_error_in_tests(self):
        src.exceptions.function('argument')

  the terminal shows an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.exceptions' has no attribute 'function'

* then add the :ref:`function<functions>` to ``exceptions.py``

  .. code-block:: python

    def function():
        return None

  and get a :ref:`TypeError`

  .. code-block:: python

    TypeError: function() takes 0 positional argument but 1 were given

  the call uses 1 positional argument but the :ref:`function<functions>` does not accept input

* I add the exception to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # NameError
    # AttributeError
    # TypeError

green: make it pass
#################################################################################

when I add a `unittest.TestCase.assertRaises`_ to the test

.. code-block:: python

  def test_catching_type_error_in_tests(self):
      with self.assertRaises(TypeError):
          src.exceptions.function('argument')

the terminal shows passing tests

----

*********************************************************************************
test_catching_index_error_in_tests
*********************************************************************************

An IndexError_ is raised when a :ref:`list<lists>` is accessed with a number that is more than the possible number of indexes for the items in it

red: make it fail
#################################################################################

* I add a failing test

  .. code-block:: python

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        a_list[4]

  the terminal shows an IndexError_

  .. code-block:: python

    IndexError: list index out of range

* I add the exception to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # NameError
    # AttributeError
    # TypeError
    # IndexError

green: make it pass
#################################################################################

* then add a `unittest.TestCase.assertRaises`_ to the test

  .. code-block:: python

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        with self.assertRaises(IndexError):
            a_list[4]

  and the terminal shows passing tests.

* I add another line that fails

  .. code-block:: python

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        with self.assertRaises(IndexError):
            a_list[4]
        a_list[-5]

  the terminal shows an IndexError_

  .. code-block:: python

    IndexError: list index out of range

  when I add the `assertRaises`

  .. code-block:: python

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        with self.assertRaises(IndexError):
            a_list[4]
        with self.assertRaises(IndexError):
            a_list[-5]

  the terminal shows green again

----

*********************************************************************************
test_catching_key_error_in_tests
*********************************************************************************

A KeyError_ is raised when a :ref:`dictionary<dictionaries>` is accessed with a key that is not in it

red: make it fail
#################################################################################

* I add a failing test

  .. code-block:: python

    def test_catching_key_error_in_tests(self):
        {'key': 'value'}['does_not_exist']

  the terminal shows a KeyError_

  .. code-block:: python

    KeyError: 'does_not_exist'

* I add the exception to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # NameError
    # AttributeError
    # TypeError
    # IndexError
    # KeyError

green: make it pass
#################################################################################

I add an `unittest.TestCase.assertRaises`_ context to the test

.. code-block:: python

    def test_catching_key_error_in_tests(self):
        with self.assertRaises(KeyError):
            {'key': 'value'}['does_not_exist']

and the terminal shows passing tests.

*********************************************************************************
test_catching_zero_division_error_in_tests
*********************************************************************************

red: make it fail
#################################################################################

* I add a failing test for a :ref:`TypeError`

  .. code-block:: python

    def test_catching_zero_division_error_in_tests(self):
        1 / 0

  the terminal shows an ZeroDivisionError_

  .. code-block:: python

    ZeroDivisionError: division by zero

  this also happens in :doc:`/how_to/calculator`

* I add the exception to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # NameError
    # AttributeError
    # TypeError
    # IndexError
    # KeyError
    # ZeroDivisionError

green: make it pass
#################################################################################

when I add an `unittest.TestCase.assertRaises` :ref:`method<functions>` to the test

.. code-block:: python

  def test_catching_zero_division_error_in_tests(self):
      with self.assertRaises(ZeroDivisionError):
          1 / 0

the terminal shows passing tests.

----

*********************************************************************************
test_catching_exceptions_in_tests
*********************************************************************************

red: make it fail
#################################################################################

I add a failing test for any :ref:`Exception<Exceptions>`

.. code-block:: python

  def test_catching_exceptions_in_tests(self):
      raise Exception

the terminal shows an Exception_

.. code-block:: python

  Exception

green: make it pass
#################################################################################

when I add a `unittest.TestCase.assertRaises`_ :ref:`method<functions>` to the test

.. code-block:: python

  def test_catching_exceptions_in_tests(self):
      with self.assertRaises(Exception):
          raise Exception

the terminal shows all tests are passing. Fantastic!

----

*********************************************************************************
review
*********************************************************************************

I have a way to catch :ref:`Exceptions<Exceptions>` when I am testing and encountered the following

* :ref:`AssertionError`
* :ref:`ModuleNotFoundError`
* NameError_
* :ref:`AttributeError`
* :ref:`TypeError`
* IndexError_
* KeyError_
* ZeroDivisionError_

Would you like to test :doc:`handling Exceptions in programs?</how_to/exception_handling_programs>`

----

:doc:`/code/code_exception_handling`