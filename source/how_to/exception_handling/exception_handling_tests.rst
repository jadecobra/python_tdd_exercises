.. meta::
  :description: Stop silent Python test failures. Learn to use unittest's assertRaises to verify exceptions like ModuleNotFoundError and NameError are properly raised.
  :keywords: Jacob Itegboje, python unittest assertraises, how to test for exceptions in python, python assert exception, python test specific exception raised, unittest assertraises example, python unit testing exceptions, python tdd exception handling, assertraises typeerror, assertraises keyerror

.. include:: ../../links.rst

#################################################################################
how to test that an Exception is raised
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/dQALevkVBWw?si=G9wK6OfhYF79-ORx" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

When an error happens in Python_, an :ref:`Exception<errors>` is raised to break execution of the program, this means nothing past the line that caused it will run.

It is useful because there is a problem to be solved to continue as expected, it can be a pain when it causes the program to stop early. What if I want it to run even with errors? I might want to give messages to the user who does not care about or understand the details of the error.

:ref:`Exception<errors>` Handling is a way to deal with this, it allows programs to make decisions when one happens.

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

  it makes the folders and files that are needed, installs packages, runs the first test, and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_exceptions.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and use the mouse to click on ``tests/test_exceptions.py:7`` to open it in the editor
* then I change ``True`` to ``False`` to make the test pass
* and I change ``test_failure`` to ``test_catching_module_not_found_error_in_tests`` with an `import statement`_

  .. code-block:: python

    class TestExceptions(unittest.TestCase):

        def test_catching_module_not_found_error_in_tests(self):
            import does_not_exist

  the terminal shows :ref:`ModuleNotFoundError`

  .. code-block:: python

    ModuleNotFoundError: No module named 'does_not_exist'

green: make it pass
#################################################################################

* I add it to the list of :ref:`Exceptions<errors>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError

* I can make ``does_not_exist.py`` to solve the problem but I want to catch or handle it in the test. I add the `unittest.TestCase.assertRaises`_ :ref:`method<functions>` which checks that the code in its context raises the :ref:`Exception<errors>` it is given

  .. code-block:: python

    def test_catching_module_not_found_error_in_tests(self):
        with self.assertRaises(ModuleNotFoundError):
            import does_not_exist

  the test passes

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

  the terminal shows NameError_

  .. code-block:: python

    NameError: name 'does_not_exist' is not defined

* I add it to the list of :ref:`Exceptions<errors>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # NameError

green: make it pass
#################################################################################

I add `unittest.TestCase.assertRaises`_

.. code-block:: python

  def test_catching_name_error_in_tests(self):
      with self.assertRaises(NameError):
          does_not_exist

the terminal shows passing tests

----

*********************************************************************************
test_catching_attribute_error_in_tests
*********************************************************************************

red: make it fail
#################################################################################

* I add another failing test

  .. code-block:: python

    def test_catching_attribute_error_in_tests(self):
        src.exceptions.does_not_exist

  the terminal shows NameError_

  .. code-block:: python

    NameError: name 'src' is not defined

* I add an `import statement`_ for the :ref:`module<ModuleNotFoundError>`

  .. code-block:: python

    import src.exceptions
    import unittest

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.exceptions' has no attribute 'does_not_exist'

  because I tried to get something that is not in something that exists

* I add the error to the list of :ref:`Exceptions<errors>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # NameError
    # AttributeError

green: make it pass
#################################################################################

then I add a call to the `unittest.TestCase.assertRaises`_ :ref:`method<functions>`

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

* I add a failing test

  .. code-block:: python

    def test_catching_type_error_in_tests(self):
        src.exceptions.function_name('argument')

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.exceptions' has no attribute 'function_name'

* I add the name to ``exceptions.py``

  .. code-block:: python

    function_name

  the terminal shows NameError_

  .. code-block:: python

    NameError: name 'function_name' is not defined

  then I assign it to :ref:`None` to define it

  .. code-block:: python

    function_name = None

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* I add it to the list of :ref:`Exceptions<errors>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # NameError
    # AttributeError
    # TypeError

green: make it pass
#################################################################################

then I add `unittest.TestCase.assertRaises`_ to the test

.. code-block:: python

  def test_catching_type_error_in_tests(self):
      with self.assertRaises(TypeError):
          src.exceptions.function_name('argument')

the terminal shows passing tests

refactor: make it better
#################################################################################

If I make ``function_name`` a :ref:`function<functions>`

.. code-block:: python

  def function_name():
      return None

the terminal shows :ref:`TypeError`

.. code-block:: python

  TypeError:

because the call sends an argument and the :ref:`function<functions>` does not accept input. When I add a parameter to the definition
.. code-block:: python

  def function_name(argument):
      return None

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: TypeError not raised

because the :ref:`function<functions>` call matches the signature. I undo the change, the terminal shows :ref:`TypeError` and I make the test pass

.. code-block:: python

  def function_name():
      return None

----

*********************************************************************************
test_catching_index_error_in_tests
*********************************************************************************

red: make it fail
#################################################################################

* I make a :ref:`list<lists>` in a new test

  .. code-block:: python

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']

  the first item in it has ``0`` as its index

  .. code-block:: python

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        a_list[0]

  the terminal shows green. The index for the last item is the total number of items minus ``1``, which is ``3`` in this case

  .. code-block:: python

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        a_list[3]

  still green. When I use a number that is bigger than the index for the last item

  .. code-block:: python

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        a_list[4]

  the terminal shows :ref:`IndexError<test_index_error>`

  .. code-block:: python

    IndexError: list index out of range

* I add it to the list of :ref:`Exceptions<errors>` encountered

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

* then I add assertRaises_

  .. code-block:: python

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        with self.assertRaises(IndexError):
            a_list[4]

  the test passes

* I can also index with negative numbers, the one for the last item in the :ref:`list<lists>` is ``-1``, think reading from right to left

  .. code-block:: python

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        with self.assertRaises(IndexError):
            a_list[4]
        a_list[-1]

  the terminal still shows passing tests. The index for the first item is negative the total number of items, ``-4`` in this case

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

  the terminal shows :ref:`IndexError<test_index_error>`

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

  the terminal shows green again

* It looks like there is a duplication of the assertRaises_ but it is not, even though the test is green when I remove the second one

  .. code-block:: python

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        with self.assertRaises(IndexError):
            a_list[4]
            a_list[-5]

  at the end of the chapter I show why this is not a repetition, I undo the change for now

  .. code-block:: python

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        with self.assertRaises(IndexError):
            a_list[4]
        with self.assertRaises(IndexError):
            a_list[-5]

----

*********************************************************************************
test_catching_key_error_in_tests
*********************************************************************************

red: make it fail
#################################################################################

* I add a :ref:`dictionary<dictionaries>` to a new test

  .. code-block:: python

    def test_catching_key_error_in_tests(self):
        {'key': 'value'}

  when I try to get the value for a key that exists

  .. code-block:: python

    def test_catching_key_error_in_tests(self):
        {'key': 'value'}['key']

  the terminal shows green, when I use a key that is in the :ref:`dictionary<dictionaries>`

  .. code-block:: python

    def test_catching_key_error_in_tests(self):
        {'key': 'value'}['does_not_exist']

  I get :ref:`KeyError <test_key_error>`

  .. code-block:: python

    KeyError: 'does_not_exist'

* another one for the list of :ref:`Exceptions<errors>` encountered

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

I add assertRaises_ to the test

.. code-block:: python

    def test_catching_key_error_in_tests(self):
        with self.assertRaises(KeyError):
            {'key': 'value'}['does_not_exist']

the terminal shows green again

*********************************************************************************
test_catching_zero_division_error_in_tests
*********************************************************************************

red: make it fail
#################################################################################

* I add another failing test for something that happened in :ref:`how to make a calculator`

  .. code-block:: python

    def test_catching_zero_division_error_in_tests(self):
        1 / 0

  any number divided by ``0`` the terminal shows a ZeroDivisionError_

  .. code-block:: python

    ZeroDivisionError: division by zero

* I add it to the list of :ref:`Exceptions<errors>` encountered

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

then add the assertRaises_ :ref:`method<functions>` to the test

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

  the terminal shows :ref:`Exception<errors>` which is the mother of the :ref:`Exceptions<errors>` encountered so far, they inherit from it

  .. code-block:: python

    Exception

* I can use the `raise statement`_ to cause any :ref:`Exception<errors>`

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

the terminal shows all tests are passing.

To review, the assertRaises_ :ref:`method<functions>` checks that the code in its context raises the :ref:`Exception<errors>` it is given.

refactor: make it better
#################################################################################

* I can use :ref:`Exception<errors>` to catch any of the :ref:`Exceptions<errors>` that inherit from it, its children if you will

  .. code-block:: python

    def test_catching_key_error_in_tests(self):
        with self.assertRaises(Exception):
            {'key': 'value'}['does_not_exist']


    def test_catching_zero_division_error_in_tests(self):
        with self.assertRaises(Exception):
            1 / 0

  all the tests are still green. The problem with using :ref:`Exception<errors>` to catch its children, is it does not tell anyone that reads the code what the actual error is or which line caused it, especially when there is more than one line of code in the context. It is better to be specific, from the :PEP:`Zen of Python <20>`: ``Explicit is better than implicit``

* I cannot use siblings or cousins to catch other :ref:`Exceptions<errors>`

  .. code-block:: python

    def test_catching_key_error_in_tests(self):
        with self.assertRaises(ModuleNotFoundError):
            {'key': 'value'}['does_not_exist']

  shows :ref:`KeyError <test_key_error>`

  .. code-block:: python

    KeyError: 'does_not_exist'

  because it is not :ref:`ModuleNotFoundError`

* As promised here is why the second AssertRaises_ in :ref:`test_catching_index_error_in_tests` is not a repetition, even though the test still passes when I remove it

  .. code-block:: python

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        with self.assertRaises(IndexError):
            a_list[4]
            a_list[-5]

  If I add a `raise statement`_ between the 2 lines

  .. code-block:: python

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        with self.assertRaises(IndexError):
            a_list[4]
            raise Exception
            a_list[-5]

  the terminal still shows a passing test, even though :ref:`Exception<errors>` is not :ref:`IndexError<test_index_error>`, it looks like the assertRaises_ exits after the first line that causes :ref:`IndexError<test_index_error>`. When I move the `raise statement`_ above it

  .. code-block:: python

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        with self.assertRaises(IndexError):
            raise Exception
            a_list[4]
            a_list[-5]

  the terminal shows :ref:`Exception<errors>`

  .. code-block:: python

    Exception

  because it is not :ref:`IndexError<test_index_error>`

* as a rule of thumb I write one line of code for one :ref:`how to test that an Exception is raised` to know which line caused which error

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

I have a way to catch :ref:`Exceptions<errors>` in tests and ran into the following

* :ref:`AssertionError`
* :ref:`ModuleNotFoundError`
* NameError_
* :ref:`AttributeError`
* :ref:`TypeError`
* :ref:`IndexError<test_index_error>`
* :ref:`KeyError <test_key_error>`
* ZeroDivisionError_

Would you like to test :ref:`handling Exceptions in programs?<how to handle Exceptions in programs>`

----

:ref:`how to handle Exceptions: tests and solutions`