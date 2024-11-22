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

When an error happens in Python, an Exception_ is raised to break execution of the program, this means nothing past the line that caused it will run.

It is useful because there is a problem to be solved to continue as expected, It can be a pain when it causes the program to stop early. What if I want it to run with errors? I may want to give messages to the user who does not care about or understand the details of the error.

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

* I want to catch or handle the :ref:`Exception<Exceptions>` in the test, instead of making the :ref:`module<ModuleNotFoundError>` to solve the problem. I add the `unittest.TestCase.assertRaises`_ :ref:`method<functions>` introduced in :doc:`/how_to/calculator` which checks that the code within its context raises the :ref:`Exception<Exceptions>` it is given

  .. code-block:: python

    def test_catching_module_not_found_error_in_tests(self):
        with self.assertRaises(ModuleNotFoundError):
            import does_not_exist

  and the test passes, showing that when I try to import a file that does not exist, I get a :ref:`ModuleNotFoundError`

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

  and the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'does_not_exist' is not defined

* I add it to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # NameError

green: make it pass
#################################################################################

then add `unittest.TestCase.assertRaises`_

.. code-block:: python

  def test_catching_name_error_in_tests(self):
      with self.assertRaises(NameError):
          does_not_exist

and the terminal shows passing tests

---

*********************************************************************************
test_catching_attribute_error_in_tests
*********************************************************************************

red: make it fail
#################################################################################

* I add another failing test

  .. code-block:: python

    def test_catching_attribute_error_in_tests(self):
        src.exceptions.does_not_exist

  the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'src.exceptions' is not defined

* I add an `import statement`_ for the :ref:`module<ModuleNotFoundError>`

  .. code-block:: python

    import src.exceptions
    import unittest

  and get an:ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.exceptions' has no attribute 'does_not_exist'

  because I called something that does not exist from something that does exist

* I add the error to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # NameError
    # AttributeError

green: make it pass
#################################################################################

then add a call to the `unittest.TestCase.assertRaises`_ :ref:`method<functions>`

.. code-block:: python

  def test_catching_attribute_error_in_tests(self):
      with self.assertRaises(AttributeError):
          src.exceptions.does_not_exist

and the terminal shows passing tests

----

*********************************************************************************
test_catching_type_error_in_tests
*********************************************************************************

red: make it fail
#################################################################################

* I add a failing test

  .. code-block:: python

    def test_catching_type_error_in_tests(self):
        src.exceptions.function('argument')

  and get an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.exceptions' has no attribute 'function'

* I add the name to ``exceptions.py``

  .. code-block:: python

    function

  and get a NameError_

  .. code-block:: python

    NameError: name 'function' is not defined

  I assign it to :ref:`None` to define it

  .. code-block:: python

    function = None

  and get a :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* I add it to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # NameError
    # AttributeError
    # TypeError

green: make it pass
#################################################################################

I add `unittest.TestCase.assertRaises`_ to the test

.. code-block:: python

  def test_catching_type_error_in_tests(self):
      with self.assertRaises(TypeError):
          src.exceptions.function('argument')

and the terminal shows passing tests

refactor: make it better
#################################################################################

If I define it as a :ref:`function<functions>`

.. code-block:: python

  def function():
      return None

the terminal still shows passing tests because the call uses 1 positional argument but the :ref:`function<functions>` does not accept input, I still have a :ref:`TypeError`. When I add a parameter to the definition

.. code-block:: python

  def function(argument):
      return None

the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: TypeError not raised

because the :ref:`function<functions>` call now matches the signature, no :ref:`TypeError` is raised. I undo the change to make the test pass

.. code-block:: python

  def function():
      return None


----

*********************************************************************************
test_catching_index_error_in_tests
*********************************************************************************

An IndexError_ is raised with a :ref:`list<lists>`

red: make it fail
#################################################################################

* I make one in a new test

  .. code-block:: python

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']

  the first item in the :ref:`list<lists>` has `0` as its index

  .. code-block:: python

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        a_list[0]

  the terminal still shows green. The index for the last item is the total number of items minus 1, which is ``3`` in this case

  .. code-block:: python

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        a_list[3]

  still green. When I use a number bigger than the total number of items

  .. code-block:: python

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        a_list[4]

  the terminal shows an IndexError_

  .. code-block:: python

    IndexError: list index out of range

* I add it to the list of :ref:`Exceptions<Exceptions>` encountered

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

* then add `unittest.TestCase.assertRaises`_

  .. code-block:: python

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        with self.assertRaises(IndexError):
            a_list[4]

  and the test passes

* I can also use negative numbers, the index for the last item in the :ref:`list<lists>` is ``-1```

  .. code-block:: python

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        with self.assertRaises(IndexError):
            a_list[4]
        a_list[-1]

  the terminal still shows passing tests. The index for the first item in the :ref:`list<lists>` is negative the total number of items, ``-4`` in this case

  .. code-block:: python

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        with self.assertRaises(IndexError):
            a_list[4]
        a_list[-4]

  still green. When I use a negative number that is outside the range

  .. code-block:: python

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        with self.assertRaises(IndexError):
            a_list[4]
        a_list[-5]

  the terminal shows an IndexError_

  .. code-block:: python

    IndexError: list index out of range

  I add the assertRaises_

  .. code-block:: python

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        with self.assertRaises(IndexError):
            a_list[4]
        with self.assertRaises(IndexError):
            a_list[-5]

  and the terminal shows green again

* It looks like there is a duplication of the IndexError_ but this is not true even though the test is still green when I remove the second one

  .. code-block:: python

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        with self.assertRaises(IndexError):
            a_list[4]
            a_list[-5]

  I will show why this is a problem before the end of the chapter

----

*********************************************************************************
test_catching_key_error_in_tests
*********************************************************************************

A KeyError_ is raised with a :ref:`dictionary<dictionaries>`

red: make it fail
#################################################################################

* I add one to a new test

  .. code-block:: python

    def test_catching_key_error_in_tests(self):
        {'key': 'value'}

  when I access it with a key that exists

  .. code-block:: python

    def test_catching_key_error_in_tests(self):
        {'key': 'value'}['key']

  the terminal shows green. When I access it with a key that does not exist

  .. code-block:: python

    def test_catching_key_error_in_tests(self):
        {'key': 'value'}['does_not_exist']

  the terminal shows a KeyError_

  .. code-block:: python

    KeyError: 'does_not_exist'

* I add it to the list of :ref:`Exceptions<Exceptions>` encountered

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

then add assertRaises_ to the test

.. code-block:: python

    def test_catching_key_error_in_tests(self):
        with self.assertRaises(KeyError):
            {'key': 'value'}['does_not_exist']

and the terminal shows green again

*********************************************************************************
test_catching_zero_division_error_in_tests
*********************************************************************************

red: make it fail
#################################################################################

* I add another failing test

  .. code-block:: python

    def test_catching_zero_division_error_in_tests(self):
        1 / 0

  the terminal shows a ZeroDivisionError_

  .. code-block:: python

    ZeroDivisionError: division by zero

* I add it to the list of :ref:`Exceptions<Exceptions>` encountered

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

when I add the assertRaises_ :ref:`method<functions>` to the test

.. code-block:: python

  def test_catching_zero_division_error_in_tests(self):
      with self.assertRaises(ZeroDivisionError):
          1 / 0

the terminal shows passing tests

----

*********************************************************************************
test_catching_exceptions_in_tests
*********************************************************************************

red: make it fail
#################################################################################

* I add a failing test

  .. code-block:: python

    def test_catching_exceptions_in_tests(self):
        raise Exception

  the terminal shows an Exception_ which is the mother of the other exceptions encountered so far

  .. code-block:: python

    Exception

* I can use the raise_ keyword to cause any :ref:`Exception<Exceptions>`

  .. code-block:: python

    def test_catching_exceptions_in_tests(self):
        raise AssertionError

  and the terminal will show it

  .. code-block:: python

    AssertionError

green: make it pass
#################################################################################

when I add the assertRaises_ :ref:`method<functions>` to the test

.. code-block:: python

  def test_catching_exceptions_in_tests(self):
      with self.assertRaises(Exception):
          raise Exception

the terminal shows all tests are passing. The assertRaises_ :ref:`method<functions>` checks that the code within its context raises the :ref:`Exception<Exceptions>` it is given

refactor: make it better
#################################################################################

* I can use Exception_ to catch any of the :ref:`Exception<Exceptions>` encountered so far, because they inherit from it

  .. code-block:: python

    def test_catching_key_error_in_tests(self):
        with self.assertRaises(Exception):
            {'key': 'value'}['does_not_exist']


    def test_catching_zero_division_error_in_tests(self):
        with self.assertRaises(Exception):
            1 / 0

  all the tests are still green. The problem with using Exception_ to catch its children is that it does not tell anyone who reads the code what the specific error is or which line caused the error if there is more than one line of code in the assertRaises_. It is better to be specific and clearly state what error is raised by the line of code

* as promised here is why the IndexError_ from earlier is not a duplicate, even though when I remove the second one the tests still pass

  .. code-block:: python

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        with self.assertRaises(IndexError):
            a_list[4]
            a_list[-5]

  the second line that causes an IndexError_ never runs, here is how I know, if I add another :ref:`Exception<Exceptions>` between them

  .. code-block:: python

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        with self.assertRaises(IndexError):
            a_list[4]
            raise Exception
            a_list[-5]

  the terminal shows a passing test, even though an Exception_ is not an IndexError_, it looks like assertRaises_ exits after it encounters the first line that causes an IndexError_. If I move the new line above the first line that raises an IndexError_

  .. code-block:: python

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        with self.assertRaises(IndexError):
            raise Exception
            a_list[4]
            a_list[-5]

  I get an Exception_

  .. code-block:: python

    Exception

  because Exception_ is not an IndexError_. As a rule of thumb I write one line of code for one exception handler, that way I know which line causes which error

  .. code-block:: python

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        with self.assertRaises(IndexError):
            a_list[4]
        with self.assertRaises(IndexError):
            a_list[-5]

----

*********************************************************************************
review
*********************************************************************************

I have a way to catch :ref:`Exceptions<Exceptions>` when testing and encountered the following

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