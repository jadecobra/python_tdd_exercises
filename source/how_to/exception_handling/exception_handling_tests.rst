.. meta::
  :description: Stop silent Python test failures. Learn to use unittest's assertRaises to verify exceptions like ModuleNotFoundError and NameError are properly raised.
  :keywords: Jacob Itegboje, python unittest assertraises, how to test for exceptions in python, python assert exception, python test specific exception raised, unittest assertraises example, python unit testing exceptions, python tdd exception handling, assertraises typeerror, assertraises keyerror

.. include:: ../../links.rst

.. _NameError: https://docs.python.org/3/library/exceptions.html#NameError
.. _ZeroDivisionError: https://docs.python.org/3/library/exceptions.html#ZeroDivisionError

#################################################################################
how to test that an Exception is raised
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/dQALevkVBWw?si=G9wK6OfhYF79-ORx" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

*********************************************************************************
requirements
*********************************************************************************

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

  .. code-block:: python
    :lineno-start: 7

    self.assertFalse(False)

* I change the name of the :ref:`class<classes>` to match the :ref:`CapWords` format

  .. code-block:: python
    :lineno-start: 4

    class TestExceptions(unittest.TestCase):

*********************************************************************************
test_catching_module_not_found_error_in_tests
*********************************************************************************

red: make it fail
#################################################################################

* I change ``test_failure`` to ``test_catching_module_not_found_error_in_tests`` with an `import statement`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    import unittest


    class TestExceptions(unittest.TestCase):

        def test_catching_module_not_found_error_in_tests(self):
            import does_not_exist

  the terminal shows :ref:`ModuleNotFoundError`

  .. code-block:: python

    ModuleNotFoundError: No module named 'does_not_exist'

green: make it pass
#################################################################################

* I add it to the list of :ref:`Exceptions<errors>` encountered in ``test_exceptions.py``

  .. code-block:: python
    :emphasize-lines: 3

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError

* I can make ``does_not_exist.py`` in the ``src`` folder/directory to solve the problem but I want to catch/handle it in the test to show that ``import does_not_exist`` raises :ref:`ModuleNotFoundError` when the file does NOT exist. I add the `unittest.TestCase.assertRaises`_ :ref:`method<functions>` which checks that the code below it the :ref:`Exception<errors>` it is given

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 2-3

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

* I add another failing test

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 5-6

        def test_catching_module_not_found_error_in_tests(self):
            with self.assertRaises(ModuleNotFoundError):
                import does_not_exist

        def test_catching_name_error_in_tests(self):
            does_not_exist

  the terminal shows NameError_

  .. code-block:: python

    NameError: name 'does_not_exist' is not defined

  because there is no definition for `does_not_exist` in ``test_exceptions.py``

* I add it to the list of :ref:`Exceptions<errors>` encountered

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 4

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # NameError

green: make it pass
#################################################################################

I add assertRaises_

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 2-3

        def test_catching_name_error_in_tests(self):
            with self.assertRaises(NameError):
                does_not_exist

the test passes

----

*********************************************************************************
test_catching_attribute_error_in_tests
*********************************************************************************

red: make it fail
#################################################################################

* I add another failing test

  .. NOTE:: the ...(ellipsis) represents code that does not need to change in this part

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 5-6

        def test_catching_name_error_in_tests(self):
            with self.assertRaises(NameError):
                does_not_exist

        def test_catching_attribute_error_in_tests(self):
            src.exceptions.does_not_exist

  the terminal shows NameError_

  .. code-block:: python

    NameError: name 'src' is not defined

* I add an `import statement`_ at the top of the file for the :ref:`module<ModuleNotFoundError>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.exceptions
    import unittest

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.exceptions' has no attribute 'does_not_exist'

  because I tried to get something that does NOT exist from something that exists

* I add the error to the list of :ref:`Exceptions<errors>` encountered in ``test_exceptions.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 5

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # NameError
    # AttributeError

green: make it pass
#################################################################################

then I add the `unittest.TestCase.assertRaises`_ :ref:`method<functions>`

.. code-block:: python
  :lineno-start: 15
  :emphasize-lines: 5-6

        def test_catching_attribute_error_in_tests(self):
            with self.assertRaises(AttributeError):
                src.exceptions.does_not_exist

the test passes

----

*********************************************************************************
test_catching_type_error_in_tests
*********************************************************************************

red: make it fail
#################################################################################

* I add a failing test

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 5-6

        def test_catching_attribute_error_in_tests(self):
            with self.assertRaises(AttributeError):
                src.exceptions.does_not_exist

        def test_catching_type_error_in_tests(self):
            src.exceptions.function_name('argument')

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.exceptions' has no attribute 'function_name'

* I click on ``exceptions.py`` in the ``src`` folder to open it in the editor, then add the name

  .. code-block:: python
    :linenos:

    function_name

  the terminal shows NameError_

  .. code-block:: python

    NameError: name 'function_name' is not defined

  I assign it to :ref:`None` to define it

  .. code-block:: python
    :linenos:

    function_name = None

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* I add it to the list of :ref:`Exceptions<errors>` encountered in ``test_exceptions.py``

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 6

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
  :lineno-start: 19
  :emphasize-lines: 2-3

      def test_catching_type_error_in_tests(self):
          with self.assertRaises(TypeError):
              src.exceptions.function_name('argument')

the test passes

refactor: make it better
#################################################################################

* When I make ``function_name`` a :ref:`function<functions>` in ``exceptions.py``

  .. code-block:: python
    :linenos:

    def function_name():
        return None

  the terminal still shows green because :ref:`TypeError` is raised since the call from the test - ``src.exceptions.function_name('argument')`` sends ``'argument'`` as input and the :ref:`function<functions>` does not take input

* When I add a parameter to the definition

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def function_name(argument):
        return None

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: TypeError not raised

  because :ref:`TypeError` is NOT raised since the :ref:`function<functions>` call matches the definition. I undo the change

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def function_name():
        return None

  the terminal shows green again

----

*********************************************************************************
test_catching_index_error_in_tests
*********************************************************************************

red: make it fail
#################################################################################

* I make a :ref:`list<lists>` in a new test

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 5-6

        def test_catching_type_error_in_tests(self):
            with self.assertRaises(TypeError):
                src.exceptions.function_name('argument')

        def test_catching_index_error_in_tests(self):
            a_list = [1, 2, 3, 'n']

  the first item in a :ref:`list<lists>` has ``0`` as its :ref:`index<test_index_returns_first_position_of_item_in_a_list>`

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 3

        def test_catching_index_error_in_tests(self):
            a_list = [1, 2, 3, 'n']
            a_list[0]

  the terminal shows green. The :ref:`index<test_index_returns_first_position_of_item_in_a_list>` for the last item is the total number of items minus ``1``, which is ``3`` in this case

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 3

        def test_catching_index_error_in_tests(self):
            a_list = [1, 2, 3, 'n']
            a_list[3]

  still green. When I use a number that is bigger than the index for the last item

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 3

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        a_list[4]

  the terminal shows :ref:`IndexError<test_index_error>`

  .. code-block:: python

    IndexError: list index out of range

* I add it to the list of :ref:`Exceptions<errors>` encountered in ``test_exceptions.py``

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 7

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
    :lineno-start: 23
    :emphasize-lines: 3-4

        def test_catching_index_error_in_tests(self):
            a_list = [1, 2, 3, 'n']
            with self.assertRaises(IndexError):
                a_list[4]

  the test passes

* I can also :ref:`index<test_index_returns_first_position_of_item_in_a_list>` with negative numbers, the one for the last item in the :ref:`list<lists>` is ``-1``, think reading from right to left

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 5

        def test_catching_index_error_in_tests(self):
            a_list = [1, 2, 3, 'n']
            with self.assertRaises(IndexError):
                a_list[4]
            a_list[-1]

  the terminal still shows passing tests. The :ref:`index<test_index_returns_first_position_of_item_in_a_list>` for the first item is negative the total number of items, ``-4`` in this case

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 5

        def test_catching_index_error_in_tests(self):
            a_list = [1, 2, 3, 'n']
            with self.assertRaises(IndexError):
                a_list[4]
            a_list[-4]

  still green. When I use a negative number that is outside the range

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 5

        def test_catching_index_error_in_tests(self):
            a_list = [1, 2, 3, 'n']
            with self.assertRaises(IndexError):
                a_list[4]
            a_list[-5]

  the terminal shows :ref:`IndexError<test_index_error>`

  .. code-block:: python

    IndexError: list index out of range

  I add assertRaises_

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 5-6

        def test_catching_index_error_in_tests(self):
            a_list = [1, 2, 3, 'n']
            with self.assertRaises(IndexError):
                a_list[4]
            with self.assertRaises(IndexError):
                a_list[-5]

  the terminal shows green again

* It looks like this is a duplication of the assertRaises_ but it is not, even though the test is green when I remove the second one

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 5-6

    def test_catching_index_error_in_tests(self):
        a_list = [1, 2, 3, 'n']
        with self.assertRaises(IndexError):
            a_list[4]
            a_list[-5]
        # with self.assertRaises(IndexError):

  I show why this is not a repetition at :ref:`the end of the chapter<one_exception_one_exception_handler>`. I undo the change for now

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 5-6

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
    :lineno-start: 23
    :emphasize-lines: 8-9

        def test_catching_index_error_in_tests(self):
            a_list = [1, 2, 3, 'n']
            with self.assertRaises(IndexError):
                a_list[4]
            with self.assertRaises(IndexError):
                a_list[-5]

        def test_catching_key_error_in_tests(self):
            {'key': 'value'}

* when I try to get the value for a key that exists

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 2

        def test_catching_key_error_in_tests(self):
            {'key': 'value'}['key']

  the terminal shows green

* when I use a key that is NOT in the :ref:`dictionary<dictionaries>`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 2

        def test_catching_key_error_in_tests(self):
            {'key': 'value'}['not_in_dictionary']

  the terminal shows :ref:`KeyError <test_key_error>`

  .. code-block:: python

    KeyError: 'not_in_dictionary'

* I add it to the list of :ref:`Exceptions<errors>` encountered in ``test_exceptions.py``

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 8

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
  :lineno-start: 30
  :emphasize-lines: 2-3

        def test_catching_key_error_in_tests(self):
            with self.assertRaises(KeyError):
                {'key': 'value'}['not_in_dictionary']

the test passes

*********************************************************************************
test_catching_zero_division_error_in_tests
*********************************************************************************

red: make it fail
#################################################################################

* I add another failing test, this time for the :ref:`Exception<errors>` that happened in :ref:`how to make a calculator` when :ref:`testing division<test_division>`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 5-6

        def test_catching_key_error_in_tests(self):
            with self.assertRaises(KeyError):
                {'key': 'value'}['not_in_dictionary']

        def test_catching_zero_division_error_in_tests(self):
            1 / 0

  any number divided by ``0`` the terminal shows ZeroDivisionError_

  .. code-block:: python

    ZeroDivisionError: division by zero

* I add it to the list of :ref:`Exceptions<errors>` encountered in ``test_exceptions.py``

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 9

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

I add assertRaises_

.. code-block:: python
  :lineno-start: 34
  :emphasize-lines: 2-3

        def test_catching_zero_division_error_in_tests(self):
            with self.assertRaises(ZeroDivisionError):
                1 / 0

the test passes

----

*********************************************************************************
test_catching_exceptions_in_tests
*********************************************************************************

red: make it fail
#################################################################################

* I add a failing test with the `raise statement`_

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 5-6

        def test_catching_zero_division_error_in_tests(self):
            with self.assertRaises(ZeroDivisionError):
                1 / 0

        def test_catching_exceptions_in_tests(self):
            raise Exception

  the terminal shows :ref:`Exception<errors>`

  .. code-block:: python

    Exception

  :ref:`Exception<errors>` is the mother of all the :ref:`Exceptions<errors>` covered so far, they inherit from it

* I can use the `raise statement`_ to cause any :ref:`Exception<errors>` I want intentionally

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 2

        def test_catching_exceptions_in_tests(self):
            raise AssertionError

  and the terminal shows the :ref:`Exception<errors>`

  .. code-block:: python

    AssertionError

  I change the :ref:`Exception<errors>` back

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 2

        def test_catching_exceptions_in_tests(self):
            raise Exception

  the terminal shows :ref:`Exception<errors>`

  .. code-block:: python

    Exception

green: make it pass
#################################################################################

I add the assertRaises_ :ref:`method<functions>`

.. code-block:: python
  :lineno-start: 38
  :emphasize-lines: 2-3

      def test_catching_exceptions_in_tests(self):
          with self.assertRaises(Exception):
              raise Exception

the terminal shows all tests are passing. The assertRaises_ :ref:`method<functions>` checks that the code under it raises the :ref:`Exception<errors>` it is given.

refactor: make it better
#################################################################################

* I can use :ref:`Exception<errors>` to catch any of the :ref:`Exceptions<errors>` that inherit from it, its children

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 2, 6

        def test_catching_key_error_in_tests(self):
            with self.assertRaises(Exception):
                {'key': 'value'}['not_in_dictionary']

        def test_catching_zero_division_error_in_tests(self):
            with self.assertRaises(Exception):
                1 / 0

  all the tests are still green. The problem with using :ref:`Exception<errors>` to catch its children, is it does not tell anyone that reads the code what the actual :ref:`error<errors>` is or which line caused it, especially when there is more than one line of code in the context. It is better to be specific, from the :PEP:`Zen of Python <20>`: ``Explicit is better than implicit``

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 2, 6

        def test_catching_key_error_in_tests(self):
            with self.assertRaises(KeyError):
                {'key': 'value'}['not_in_dictionary']

        def test_catching_zero_division_error_in_tests(self):
            with self.assertRaises(ZeroDivisionError):
                1 / 0

* I cannot use sibling or cousin :ref:`Exceptions<errors>` to catch other :ref:`Exceptions<errors>`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 2

        def test_catching_key_error_in_tests(self):
            with self.assertRaises(ModuleNotFoundError):
                {'key': 'value'}['not_in_dictionary']

  the terminal shows :ref:`KeyError <test_key_error>`

  .. code-block:: python

    KeyError: 'not_in_dictionary'

  because it is not :ref:`ModuleNotFoundError` even though they are both :ref:`Exceptions<errors>`. I undo the change

  .. code-block:: python
    :emphasize-lines: 2

        def test_catching_key_error_in_tests(self):
            with self.assertRaises(KeyError):
                {'key': 'value'}['not_in_dictionary']

  the test passes

* I cannot use children :ref:`Exceptions<errors>` to catch parent :ref:`Exceptions<errors>`

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 2

        def test_catching_exceptions_in_tests(self):
            with self.assertRaises(ZeroDivisionError):
                raise Exception

  the terminal shows :ref:`Exception<errors>`

  .. code-block:: python

    Exception

  because it is not ZeroDivisionError_ even though it is an :ref:`Exceptions<errors>`. I undo the change

  .. code-block:: python
    :emphasize-lines: 2

        def test_catching_exceptions_in_tests(self):
            with self.assertRaises(Exception):
                raise Exception

  the test passes

.. _one_exception_one_exception_handler:

* As promised here is why the second AssertRaises_ in :ref:`test_catching_index_error_in_tests` is not a repetition, even though the test still passes when I remove it

  .. code-block:: python
    :emphasize-lines: 5-6

        def test_catching_index_error_in_tests(self):
            a_list = [1, 2, 3, 'n']
            with self.assertRaises(IndexError):
                a_list[4]
                a_list[-5]
            # with self.assertRaises(IndexError):

  If I add a `raise statement`_ between the 2 lines

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 5

        def test_catching_index_error_in_tests(self):
            a_list = [1, 2, 3, 'n']
            with self.assertRaises(IndexError):
                a_list[4]
                raise Exception
                a_list[-5]
            # with self.assertRaises(IndexError):

  the terminal still shows green, even though :ref:`Exception<errors>` is not :ref:`IndexError<test_index_error>`, it does NOT get raised. The assertRaises_ exits after the first line that causes :ref:`IndexError<test_index_error>` and does NOT run the other lines.

  When I move the `raise statement`_ above the first :ref:`IndexError<test_index_error>`

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 4

        def test_catching_index_error_in_tests(self):
            a_list = [1, 2, 3, 'n']
            with self.assertRaises(IndexError):
                raise Exception
                a_list[4]
                a_list[-5]
            # with self.assertRaises(IndexError):

  the terminal shows :ref:`Exception<errors>`

  .. code-block:: python

    Exception

  because it is NOT :ref:`IndexError<test_index_error>`, this is the expected behavior

* as a rule of thumb I write one line of code for one :ref:`Exception<errors>`, this way I always know exactly which line caused which :ref:`Exception<errors>`

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 3-6

        def test_catching_index_error_in_tests(self):
            a_list = [1, 2, 3, 'n']
            with self.assertRaises(IndexError):
                a_list[4]
            with self.assertRaises(IndexError):
                a_list[-5]

  all tests are passing! I know :ref:`how to test that an Exception is raised`!

----

*********************************************************************************
review
*********************************************************************************

I have a way to catch :ref:`Exceptions<errors>` in tests and tested the following

* :ref:`AssertionError`
* :ref:`ModuleNotFoundError`
* :ref:`NameError<test_catching_name_error_in_tests>`
* :ref:`AttributeError`
* :ref:`TypeError`
* :ref:`IndexError<test_index_error>`
* :ref:`KeyError <test_key_error>`
* :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>`

Would you like to :ref:`test handling Exceptions in programs?<how to handle Exceptions in programs>`

----

:ref:`how to handle Exceptions: tests and solutions`