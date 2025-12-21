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

*********************************************************************************
preview
*********************************************************************************

Here are the tests I have by the end of the chapter

.. literalinclude:: ../../code/tests/test_exceptions.py
  :language: python
  :linenos:
  :lines: 1-40

----

*********************************************************************************
requirements
*********************************************************************************

:ref:`makePythonTdd.sh<how to make a Python Test Driven Development environment automatically>` or :ref:`makePythonTdd.ps1<how to make a Python Test Driven Development environment automatically on Windows without Windows Subsystem for Linux>`

----

*********************************************************************************
start the project
*********************************************************************************

* I open a terminal_
* I type pwd_ to make sure I am in the ``pumping_python`` folder_

  .. code-block:: shell
    :emphasize-lines: 1

    pwd

  the terminal_ goes back to the command line

  .. code-block:: shell

    .../pumping_python

  .. NOTE:: if you are not in the ``pumping_python`` folder_, try ``cd ~/pumping_python``

* I pick ``exceptions`` as the name of this project
* I open ``makePythonTdd.sh`` in the :ref:`editor<2 editors>`

  .. TIP:: Here is a quick way to open ``makePythonTdd.sh`` or ``makePythonTdd.ps1`` if you are using `Visual Studio Code`_

    .. code-block:: shell
      :emphasize-lines: 1

      code makePythonTdd.sh

    on `Windows`_ without `Windows Subsystem for Linux` use

    .. code-block:: shell
      :emphasize-lines: 1

      code makePythonTdd.ps1

* I change everywhere I have ``more_magic`` in ``makePythonTdd.sh`` or ``makePythonTdd.ps1`` to the name of this project

  .. code-block:: shell
    :linenos:
    :emphasize-lines: 2,3, 5, 12, 20
    :emphasize-text: exceptions, Exceptions

    #!/bin/bash
    mkdir exceptions
    cd exceptions
    mkdir src
    touch src/exceptions.py
    mkdir tests
    touch tests/__init__.py

    echo "import unittest


    class TestExceptions(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions Encountered
    # AssertionError
    " > tests/test_exceptions.py

* I run the program_ in the terminal_

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.sh

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use ``makePythonTdd.ps1`` instead of ``makePythonTdd.sh``

    .. code-block:: shell
      :emphasize-lines: 1

      ./makePythonTdd.ps1

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell
    :emphasize-lines: 10
    :emphasize-text: tests/test_exceptions.py:7

    ======================================= FAILURES =======================================
    _____________________________ TestExceptions.test_failure ______________________________

    self = <tests.test_exceptions.TestExceptions testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_exceptions.py:7: AssertionError
    =============================== short test summary info ================================
    FAILED tests/test_exceptions.py::TestMagic::test_failure - AssertionError: True is not false
    ================================== 1 failed in X.YZs ===================================

* I hold :kbd:`ctrl` (Windows_/Linux_) or ``option or command`` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_exceptions.py:7`` to open it in the :ref:`editor<2 editors>`
* I add :ref:`AssertionError` to the list of :ref:`Exceptions<errors>` encountered in ``test_.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4-5

    # Exceptions Encountered
    # AssertionError

* then I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in ``test_exceptions.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

  the test passes

----

*********************************************************************************
test_catching_module_not_found_error_in_tests
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I change ``test_failure`` to ``test_catching_module_not_found_error_in_tests`` with an `import statement`_ in ``test_exceptions.py``

.. code-block:: python
  :lineno-start: 5
  :emphasize-lines: 3-4

  class TestExceptions(unittest.TestCase):

      def test_catching_module_not_found_error_in_tests(self):
          import does_not_exist


  # Exceptions Encountered

the terminal_ shows :ref:`ModuleNotFoundError`

.. code-block:: shell

  ModuleNotFoundError: No module named 'does_not_exist'

I cannot import a :ref:`module<ModuleNotFoundError>` that does not exist. A :ref:`module<ModuleNotFoundError>` is any file_ that ends in ``.py``

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I add :ref:`ModuleNotFoundError` to the list of :ref:`Exceptions<errors>` encountered

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 3

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError

* I can make ``does_not_exist.py`` in the ``src`` `folder (directory)`_ to solve the problem but I want to catch/handle it in the test. This way I can show that ``import does_not_exist`` raises :ref:`ModuleNotFoundError` when the file does NOT exist. I add the `assertRaises method`_

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 2-3

        def test_catching_module_not_found_error_in_tests(self):
            with self.assertRaises(ModuleNotFoundError):
                import does_not_exist

  the test passes.

assertRaises_ checks that the code in its context, raises the :ref:`Exception<errors>` it is given in parentheses. :ref:`ModuleNotFoundError` is raised when I try to import a :ref:`module<ModuleNotFoundError>` that does NOT exist

----

*********************************************************************************
test_catching_name_error_in_tests
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

* I add another failing test

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 5-6

        def test_catching_module_not_found_error_in_tests(self):
            with self.assertRaises(ModuleNotFoundError):
                import does_not_exist

        def test_catching_name_error_in_tests(self):
            does_not_exist

  the terminal_ shows NameError_

  .. code-block:: shell

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

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add assertRaises_

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 2-3

        def test_catching_name_error_in_tests(self):
            with self.assertRaises(NameError):
                does_not_exist

the test passes, showing that NameError_ is raised when I used a name that has no definition for it

----

*********************************************************************************
test_catching_attribute_error_in_tests
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

* I add another failing test, this time for :ref:`AttributeError`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 5-6

        def test_catching_name_error_in_tests(self):
            with self.assertRaises(NameError):
                does_not_exist

        def test_catching_attribute_error_in_tests(self):
            src.exceptions.does_not_exist

  the terminal_ shows NameError_

  .. code-block:: shell

    NameError: name 'src' is not defined

* I add an `import statement`_ at the top of the file for the :ref:`module<ModuleNotFoundError>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.exceptions
    import unittest

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.exceptions' has no attribute 'does_not_exist'

  ``src.exceptions.does_not_exist`` is like an address

  - ``src`` is the ``src`` folder_
  - ``exceptions`` is ``exceptions.py`` in the ``src`` folder_
  - ``src.exceptions.does_not_exist`` is pointing to something named ``does_not_exist`` in ``exceptions.py`` in the ``src`` folder_

  the failure happened because Python_ cannot find ``does_not_exist`` in ``exceptions.py`` in the ``src`` folder_. tried to get something that does NOT exist from something that exists

* I add the :ref:`AttributeError` to the list of :ref:`Exceptions<errors>` encountered

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 5

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # NameError
    # AttributeError

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add the `assertRaises method`_

.. code-block:: python
  :lineno-start: 15
  :emphasize-lines: 2-3

      def test_catching_attribute_error_in_tests(self):
          with self.assertRaises(AttributeError):
              src.exceptions.does_not_exist

the test passes. :ref:`AttributeError` is raised when I try to call something that does NOT exist from something that does exist

----

*********************************************************************************
test_catching_type_error_in_tests
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

* I add a failing test for :ref:`TypeError`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 5-6

        def test_catching_attribute_error_in_tests(self):
            with self.assertRaises(AttributeError):
                src.exceptions.does_not_exist

        def test_catching_type_error_in_tests(self):
            src.exceptions.function_name('the input')

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.exceptions' has no attribute 'function_name'

* I open ``exceptions.py`` from the ``src`` folder in the :ref:`editor<2 editors>`, then add the name

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    function_name

  the terminal_ shows NameError_

  .. code-block:: shell

    NameError: name 'function_name' is not defined

  I point it to :ref:`None` to define it

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    function_name = None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

  a reminder that I cannot call :ref:`None` like a :ref:`function<functions>`

* I add :ref:`TypeError` to the list of :ref:`Exceptions<errors>` encountered in ``test_exceptions.py``

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 6

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # NameError
    # AttributeError
    # TypeError

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I use assertRaises_ to take care of the :ref:`Exception<errors>`

.. code-block:: python
  :lineno-start: 19
  :emphasize-lines: 2-3

      def test_catching_type_error_in_tests(self):
          with self.assertRaises(TypeError):
              src.exceptions.function_name('the input')

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* when I make ``function_name`` a :ref:`function<functions>` in ``exceptions.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def function_name():
        return None

  the terminal_ still shows green because :ref:`TypeError` is raised since the call from the test - ``src.exceptions.function_name('the input')`` sends ``'the input'`` as input and the :ref:`function<functions>` does not take input

* when I add a parameter to the definition

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def function_name(parameter_name):
        return None

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: TypeError not raised

  because :ref:`TypeError` is NOT raised since the :ref:`function<functions>` call matches the definition. I undo the change

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def function_name():
        return None

  the terminal_ shows green again

:ref:`TypeError` is raised when I call something in a way that it should NOT be called

----

*********************************************************************************
test_catching_index_error_in_tests
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

* I want to test catching :ref:`IndexError<test_index_error>`, I add a new test with a :ref:`list<lists>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 5-6

        def test_catching_type_error_in_tests(self):
            with self.assertRaises(TypeError):
                src.exceptions.function_name('the input')

        def test_catching_index_error_in_tests(self):
            a_list = [1, 2, 3, 'n']

* the first item in a :ref:`list<lists>` has ``0`` as its :ref:`index<test_index_returns_first_position_of_item_in_a_list>`

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 3

        def test_catching_index_error_in_tests(self):
            a_list = [1, 2, 3, 'n']
            a_list[0]

  the terminal_ shows green

* The :ref:`index<test_index_returns_first_position_of_item_in_a_list>` for the last item is the total number of items minus ``1``, which is ``3`` in this case

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 3

        def test_catching_index_error_in_tests(self):
            a_list = [1, 2, 3, 'n']
            a_list[3]

  still green

* When I use a number that is bigger than the index for the last item

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 3

        def test_catching_index_error_in_tests(self):
            a_list = [1, 2, 3, 'n']
            a_list[4]

  the terminal_ shows :ref:`IndexError<test_index_error>`

  .. code-block:: python

    IndexError: list index out of range

  I cannot use a number that is bigger than the index of the last item in a :ref:`list<lists>` or that is greater than or equal to the length of the list

* I add :ref:`IndexError<test_index_error>` to the list of :ref:`Exceptions<errors>` encountered

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

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add assertRaises_

.. code-block:: python
  :lineno-start: 23
  :emphasize-lines: 3-4

      def test_catching_index_error_in_tests(self):
          a_list = [1, 2, 3, 'n']
          with self.assertRaises(IndexError):
              a_list[4]

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I can also :ref:`index<test_index_returns_first_position_of_item_in_a_list>` with negative numbers, the one for the last item in the :ref:`list<lists>` is ``-1``, like reading from right to left

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 5

        def test_catching_index_error_in_tests(self):
            a_list = [1, 2, 3, 'n']
            with self.assertRaises(IndexError):
                a_list[4]
            a_list[-1]

  the terminal_ still shows passing tests

* The :ref:`index<test_index_returns_first_position_of_item_in_a_list>` for the first item is negative the total number of items, ``-4`` in this case

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 5

        def test_catching_index_error_in_tests(self):
            a_list = [1, 2, 3, 'n']
            with self.assertRaises(IndexError):
                a_list[4]
            a_list[-4]

  still green

* When I use a negative number that is outside the range

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 5

        def test_catching_index_error_in_tests(self):
            a_list = [1, 2, 3, 'n']
            with self.assertRaises(IndexError):
                a_list[4]
            a_list[-5]

  the terminal_ shows :ref:`IndexError<test_index_error>`

  .. code-block:: python

    IndexError: list index out of range

* I add assertRaises_

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 5-6

        def test_catching_index_error_in_tests(self):
            a_list = [1, 2, 3, 'n']
            with self.assertRaises(IndexError):
                a_list[4]
            with self.assertRaises(IndexError):
                a_list[-5]

  the terminal_ shows green again. I cannot use a number that is smaller than the negative of the total number of items in the :ref:`list<lists>` to :ref:`index the list<test_index_returns_first_position_of_item_in_a_list>`

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

  :ref:`I show why this is not a repetition at the end of the chapter<one exception one exception handler>`

* I undo the change for now

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 5-6

        def test_catching_index_error_in_tests(self):
            a_list = [1, 2, 3, 'n']
            with self.assertRaises(IndexError):
                a_list[4]
            with self.assertRaises(IndexError):
                a_list[-5]

:ref:`IndexError<test_index_error>` is raised when I try to :ref:`index a list<test_index_returns_first_position_of_item_in_a_list>` with a number that is

- bigger than or the same as the number of items in the :ref:`lists`
- smaller than the negative of the number of items in the :ref:`list<lists>`

----

*********************************************************************************
test_catching_key_error_in_tests
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

* I add a :ref:`dictionary<dictionaries>` to a new test for :ref:`KeyError<test_key_error>`

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

* when I try to get the value of a :ref:`key<test_keys_of_a_dictionary>` that is in the :ref:`dictionary<dictionaries>`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 2

        def test_catching_key_error_in_tests(self):
            {'key': 'value'}['key']

  the terminal_ shows green

* when I use a :ref:`key<test_keys_of_a_dictionary>` that is NOT in the :ref:`dictionary<dictionaries>`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 2

        def test_catching_key_error_in_tests(self):
            {'key': 'value'}['not_in_dictionary']

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: shell

    KeyError: 'not_in_dictionary'

* I add :ref:`KeyError<test_key_error>` to the list of :ref:`Exceptions<errors>` encountered

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

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add assertRaises_ to the test

.. code-block:: python
  :lineno-start: 30
  :emphasize-lines: 2-3

      def test_catching_key_error_in_tests(self):
          with self.assertRaises(KeyError):
              {'key': 'value'}['not_in_dictionary']

the test passes. :ref:`KeyError<test_key_error>` is raised when I try to use a :ref:`key<test_keys_of_a_dictionary>` that is not in a :ref:`dictionary<dictionaries>`

*********************************************************************************
test_catching_zero_division_error_in_tests
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

* I add another failing test, this time for the :ref:`Exception<errors>` that happened in :ref:`how to make a calculator` when :ref:`testing division<test_division>`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 5-6

        def test_catching_key_error_in_tests(self):
            with self.assertRaises(KeyError):
                {'key': 'value'}['not_in_dictionary']

        def test_catching_zero_division_error_in_tests(self):
            1 / 0

  the terminal_ shows ZeroDivisionError_

  .. code-block:: python

    ZeroDivisionError: division by zero

  I cannot divide a number by ``0``

* I add ZeroDivisionError_ to the list of :ref:`Exceptions<errors>` encountered

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

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add assertRaises_

.. code-block:: python
  :lineno-start: 34
  :emphasize-lines: 2-3

      def test_catching_zero_division_error_in_tests(self):
          with self.assertRaises(ZeroDivisionError):
              1 / 0

the test passes. ZeroDivisionError_ is raised when I try to divide any number by ``0``, same as I get ``undefined`` when I try it with a calculator, because dividing by ``0`` is underfined in Mathematics_

----

*********************************************************************************
test_catching_exceptions_in_tests
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

* I add a failing test with the `raise statement`_

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 5-6

        def test_catching_zero_division_error_in_tests(self):
            with self.assertRaises(ZeroDivisionError):
                1 / 0

        def test_catching_exceptions_in_tests(self):
            raise Exception

  the terminal_ shows :ref:`Exception<errors>`

  .. code-block:: python

    Exception

  :ref:`Exception<errors>` is the mother of all the :ref:`Exceptions<errors>` covered so far, they inherit from it

* I can use the `raise statement`_ to cause any :ref:`Exception<errors>` I want

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 2

        def test_catching_exceptions_in_tests(self):
            raise AssertionError

  and the terminal_ shows the :ref:`Exception<errors>` I give the `raise statement`_

  .. code-block:: python

    AssertionError

  I change the :ref:`Exception<errors>` back

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 2

        def test_catching_exceptions_in_tests(self):
            raise Exception

  the terminal_ shows :ref:`Exception<errors>`

  .. code-block:: python

    Exception

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add the `assertRaises method`_ to catch it

.. code-block:: python
  :lineno-start: 38
  :emphasize-lines: 2-3

      def test_catching_exceptions_in_tests(self):
          with self.assertRaises(Exception):
              raise Exception


  # Exceptions Encountered

the terminal_ shows all tests are passing. The `assertRaises method`_ checks that the code under it raises the :ref:`Exception<errors>` it is given in parentheses

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

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

  all the tests are still green.

  The problem with using :ref:`Exception<errors>` to catch its children, is it does not tell anyone that reads the code what the actual :ref:`error<errors>` is or which line caused it, especially when there is more than one line of code in the context.

  It is better to be specific, from the :PEP:`Zen of Python <20>`: ``Explicit is better than implicit``

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
    :lineno-start: 30
    :emphasize-lines: 2

        def test_catching_key_error_in_tests(self):
            with self.assertRaises(ModuleNotFoundError):
                {'key': 'value'}['not_in_dictionary']

  the terminal_ shows :ref:`KeyError<test_key_error>`

  .. code-block:: shell

    KeyError: 'not_in_dictionary'

  because it is not :ref:`ModuleNotFoundError` even though they are both :ref:`Exceptions<errors>`. I undo the change

  .. code-block:: python
    :lineno-start: 30
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

  the terminal_ shows :ref:`Exception<errors>`

  .. code-block:: python

    Exception

  because it is not ZeroDivisionError_ even though it is an :ref:`Exception<errors>`. I undo the change

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 2

        def test_catching_exceptions_in_tests(self):
            with self.assertRaises(Exception):
                raise Exception

  the test passes

----

*********************************************************************************
one exception one exception handler
*********************************************************************************

* As promised here is why the second AssertRaises_ in :ref:`test_catching_index_error_in_tests` is not a repetition, even though the test still passes when I remove it

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 5-6

        def test_catching_index_error_in_tests(self):
            a_list = [1, 2, 3, 'n']
            with self.assertRaises(IndexError):
                a_list[4]
                a_list[-5]
            # with self.assertRaises(IndexError):

* If I add a `raise statement`_ between the 2 lines

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

  the terminal_ still shows green, which is NOT the expected behavior. :ref:`Exception<errors>` is not :ref:`IndexError<test_index_error>` and still does NOT get raised. The assertRaises_ exits after the first line that causes :ref:`IndexError<test_index_error>` and does NOT run the other lines.

* When I move the `raise statement`_ above the first :ref:`IndexError<test_index_error>`

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

  the terminal_ shows :ref:`Exception<errors>`

  .. code-block:: python

    Exception

  because it is NOT :ref:`IndexError<test_index_error>`, this is the expected behavior

* I remove the failing line and put the assertRaises_ back in the right place

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 3-6

        def test_catching_index_error_in_tests(self):
            a_list = [1, 2, 3, 'n']
            with self.assertRaises(IndexError):
                a_list[4]
            with self.assertRaises(IndexError):
                a_list[-5]

  all tests are passing!

I know :ref:`how to test that an Exception is raised`. As a rule of thumb I write one line of code for one :ref:`Exception<errors>`, this way I always know which line caused which :ref:`Exception<errors>`

----

*********************************************************************************
review
*********************************************************************************

I can use assertRaises_ to catch :ref:`Exceptions<errors>` in tests and tested the following

* :ref:`ModuleNotFoundError`
* :ref:`NameError<test_catching_name_error_in_tests>`
* :ref:`AttributeError`
* :ref:`TypeError`
* :ref:`IndexError<test_index_error>`
* :ref:`KeyError<test_key_error>`
* :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>` and
* :ref:`The Mother of all Exceptions<test_catching_exceptions_in_tests>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<how to handle Exceptions (Errors): tests and solutions>`

----

*********************************************************************************
what is next?
*********************************************************************************

you know

* :ref:`how to make a test driven development environment`
* :ref:`how to raise AssertionError with assert methods<AssertionError>`
* :ref:`how to write functions<functions>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what is None and NOT None<None>`
* :ref:`what is True and False in Python<booleans>`
* :ref:`how to write programs that make decisions<booleans: truth table>`
* :ref:`how to make a calculator<how to make a calculator>`
* :ref:`how to make a Python Test Driven Development environment automatically` or :ref:`how to make a Python Test Driven Development environment automatically on Windows without Windows Subsystem for Linux` and
* :ref:`how to test that an Exception is raised with assertRaises<how to test that an Exception is raised>`

:ref:`Would you like to test handling Exceptions in programs?<how to handle Exceptions (Errors) in programs>`

-----

*********************************************************************************
please leave a review
*********************************************************************************

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review, if this has been a 5 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->