.. meta::
  :description: Stop silent Python test failures. Learn to use unittest's assertRaises to verify exceptions like ModuleNotFoundError and NameError are properly raised.
  :keywords: Jacob Itegboje, python unittest assertraises, how to test for exceptions in python, python assert exception, python test specific exception raised, unittest assertraises example, python unit testing exceptions, python tdd exception handling, assertraises typeerror, assertraises keyerror

.. include:: ../../links.rst

.. _NameError: https://docs.python.org/3/library/exceptions.html#NameError
.. _ZeroDivisionError: https://docs.python.org/3/library/exceptions.html#ZeroDivisionError

#################################################################################
how to test that an Exception is raised
#################################################################################

----

When an :ref:`Exception<errors>` is raised, it stops the program from running. It is useful because there is a problem that must be solved for the program_ to continue, and it is a problem when it causes the program_ to stop early.

What if I want to test that a program_ raises an :ref:`Exception<errors>`? If the :ref:`Exception<errors>` is raised, the test will not continue past the line that caused it.

I can use the `assertRaises method`_ from the :ref:`unittest.TestCase class<test_dir_unittest_testcase>` to test that some code raises an :ref:`Exception<errors>` and continue past the line that caused it.

assertRaises_ checks that the code in its context, raises the :ref:`Exception<errors>` it is given in parentheses.

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
  :lines: 23-42

.. literalinclude:: ../../code/exception_handling/test_exceptions_in_tests.py
  :language: python
  :lineno-start: 44
  :caption: exceptions/tests/test_exceptions.py
  :lines: 44-

----

*********************************************************************************
questions about testing Exceptions
*********************************************************************************

Questions to think about as I go through the chapter

* :ref:`how can I make sure an Exception is raised?<how to test that an Exception is raised>`
* :ref:`what causes ModuleNotFoundError?<test_catching_module_not_found_error_in_tests>`
* :ref:`what causes NameError?<test_catching_name_error_in_tests>`
* :ref:`what causes AttributeError?<test_catching_attribute_error_in_tests>`
* :ref:`what causes TypeError?<test_catching_type_error_in_tests>`
* :ref:`what causes IndexError?<test_catching_index_error_in_tests>`
* :ref:`what causes KeyError?<test_catching_key_error_in_tests>`
* :ref:`what causes ZeroDivisionError?<test_catching_zero_division_error_in_tests>`
* :ref:`what Exception do all the other Exceptions come (inherit) from?<test_catching_exceptions_in_tests>`

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
* I give ``exceptions`` as the ``PROJECT_NAME`` :ref:`variable<what is a variable?>`

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
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertTrue(True)

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
test_catching_module_not_found_error_in_tests
*********************************************************************************

:ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>` is raised when I try to import a :ref:`module<what is a module?>` that does NOT exist.

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

* I change :ref:`test_failure` to ``test_catching_module_not_found_error_in_tests`` with an `import statement`_ in ``test_exceptions.py``

.. code-block:: python
  :lineno-start: 4
  :emphasize-lines: 3-4

  class TestExceptions(unittest.TestCase):

      def test_catching_module_not_found_error_in_tests(self):
          import does_not_exist


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

.. code-block:: shell

  ModuleNotFoundError: No module named 'does_not_exist'

I cannot import a :ref:`module<what is a module?>` that does not exist. A :ref:`module<what is a module?>` is any file_ that ends in ``.py``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 3

    # Exceptions seen
    # AssertionError
    # ModuleNotFoundError

  I can make ``does_not_exist.py`` to solve the problem. What I want to do is catch/handle it in the test to show that ``import does_not_exist`` raises :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>` when the file_ does NOT exist and the test can continue running after confirming the :ref:`Exception<errors>`.

* I add the `assertRaises method`_ to :ref:`test_catching_module_not_found_error_in_tests`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 2-3

        def test_catching_module_not_found_error_in_tests(self):
            with self.assertRaises(ModuleNotFoundError):
                import does_not_exist

  the test passes, showing that

  * assertRaises_ checks that the code in its context (``import does_not_exist``), raises the :ref:`Exception<errors>` (:ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`) it is given in parentheses.
  * :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>` is raised when I try to import a :ref:`module<what is a module?>` that does NOT exist.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_catching_module_not_found_error_in_tests'

----

*********************************************************************************
test_catching_name_error_in_tests
*********************************************************************************

NameError_ is raised when I use a name that is not defined in the file_ I am working in.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add another failing test

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 5-6

        def test_catching_module_not_found_error_in_tests(self):
            with self.assertRaises(ModuleNotFoundError):
                import does_not_exist

        def test_catching_name_error_in_tests(self):
            does_not_exist

  the terminal_ is my friend, and shows NameError_

  .. code-block:: shell

    NameError: name 'does_not_exist' is not defined

  because there is no definition for ``does_not_exist`` in ``test_exceptions.py``.

* I add NameError_ to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 4

    # Exceptions seen
    # AssertionError
    # ModuleNotFoundError
    # NameError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add assertRaises_ to :ref:`test_catching_name_error_in_tests`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 2-3

          def test_catching_name_error_in_tests(self):
              with self.assertRaises(NameError):
                  does_not_exist

  the test passes, showing that

  * assertRaises_ checks that the code in its context (``does_not_exist``), raises the :ref:`Exception<errors>` (NameError_) it is given in parentheses.
  * NameError_ is raised when I use a name that is not defined in the file.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_catching_name_error_in_tests'

----

*********************************************************************************
test_catching_attribute_error_in_tests
*********************************************************************************

:ref:`AttributeError<what causes AttributeError?>` is raised when I try to get something that does NOT exist from an :ref:`object<everything is an object>` that exists.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a failing test for :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 5-6

        def test_catching_name_error_in_tests(self):
            with self.assertRaises(NameError):
                does_not_exist

        def test_catching_attribute_error_in_tests(self):
            src.exceptions.does_not_exist

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

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

  the failure happens because Python_ cannot find ``does_not_exist`` in the ``__init__.py`` in the ``exceptions`` folder_ in the ``src`` folder_. I tried to get something that does NOT exist from an :ref:`object<everything is an object>` that exists.

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 5

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

I add the `assertRaises method`_ to :ref:`test_catching_attribute_error_in_tests`

.. code-block:: python
  :lineno-start: 15
  :emphasize-lines: 2-3

      def test_catching_attribute_error_in_tests(self):
          with self.assertRaises(AttributeError):
              src.exceptions.does_not_exist

the test passes, showing that

* assertRaises_ checks that the code in its context (``src.exceptions.does_not_exist``), raises the :ref:`Exception<errors>` (:ref:`AttributeError<what causes AttributeError?>`) it is given in parentheses.
* :ref:`AttributeError<what causes AttributeError?>` is raised when I try to get something that does NOT exist from an :ref:`object<everything is an object>` that exists.

----

*********************************************************************************
test_catching_type_error_in_tests
*********************************************************************************

:ref:`TypeError<what causes TypeError?>` is raised when I use :ref:`object<everything is an object>` in a way that it cannot be used.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a failing test for :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 5-6

        def test_catching_attribute_error_in_tests(self):
            with self.assertRaises(AttributeError):
                src.exceptions.does_not_exist

        def test_catching_type_error_in_tests(self):
            src.exceptions.function_name('the input')

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

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'function_name' is not defined

* I point ``function_name`` to :ref:`None<what is None?>` to define it

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    function_name = None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

  a reminder that :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`.

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen, in ``tests/test_exceptions.py``

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 6

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

I use assertRaises_ to :ref:`test_catching_type_error_in_tests`

.. code-block:: python
  :lineno-start: 19
  :emphasize-lines: 2-3

      def test_catching_type_error_in_tests(self):
          with self.assertRaises(TypeError):
              src.exceptions.function_name('the input')

the test passes, showing that assertRaises_ checks that the code in its context (``src.exceptions.function_name('the input')``), raises the :ref:`Exception<errors>` (:ref:`TypeError<what causes TypeError?>`) it is given in parentheses.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I make ``function_name`` a :ref:`function<what is a function?>` in ``exceptions.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def function_name():
        return None

  the test is still green because :ref:`TypeError<what causes TypeError?>` is raised since the call from the test - ``src.exceptions.function_name('the input')`` sends ``'the input'`` as input and the ``function_name`` :ref:`function<what is a function?>` does not take input.

* I add a parameter to the definition

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def function_name(parameter_name):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: TypeError not raised

  because :ref:`TypeError<what causes TypeError?>` is NOT raised since the :ref:`function<what is a function?>` :ref:`call<how to call a function with input>` matches the :ref:`definition<how to make a function that takes input>`. I undo the change

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def function_name():
        return None


* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_catching_type_error_in_tests'

:ref:`TypeError<what causes TypeError?>` is raised when I use :ref:`object<everything is an object>` in a way that it cannot be used.

----

*********************************************************************************
test_catching_index_error_in_tests
*********************************************************************************

:ref:`IndexError<test_index_error>` is raised when I try to :ref:`index a list<test_index_returns_first_position_of_item_in_a_list>`, set_, tuple_ or string_ with a number that is

- bigger than or the same as the number of items in the :ref:`list`, set_, tuple_ or string_
- smaller than the negative of the number of items in the :ref:`list<what is a list?>`, tuple_ or string_

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a new test with a string_

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 5-7

        def test_catching_type_error_in_tests(self):
            with self.assertRaises(TypeError):
                src.exceptions.function_name('the input')

        def test_catching_index_error_in_tests(self):
            a_string = 'a string'
            a_string[0]


    # Exceptions seen

  the test is still green because the first item in a :ref:`list<what is a list?>`, tuple_ or string_ has ``0`` as its :ref:`index<test_index_returns_first_position_of_item_in_a_list>` (its position in the container)

* I add another line

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 4

        def test_catching_index_error_in_tests(self):
            a_string = 'a string'
            a_string[0]
            a_string[7]


    # Exceptions seen

  the test is still green because the :ref:`index<test_index_returns_first_position_of_item_in_a_list>` for the last item is the total number of items minus ``1``, which is ``7`` in this case.

* If I use a number that is bigger than the index for the last item

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 5

        def test_catching_index_error_in_tests(self):
            a_string = 'a string'
            a_string[0]
            a_string[7]
            a_string[8]


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`IndexError<test_index_error>`

  .. code-block:: python

    IndexError: string index out of range

  I cannot use a number that is bigger than the index of the last item in a string_ or that is greater than or equal to the length of the string_.

* I add :ref:`IndexError<test_index_error>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 7

    # Exceptions seen
    # AssertionError
    # ModuleNotFoundError
    # NameError
    # AttributeError
    # TypeError
    # IndexError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add assertRaises_ to :ref:`test_catching_index_error_in_tests`

.. code-block:: python
  :lineno-start: 23
  :emphasize-lines: 6-7

      def test_catching_index_error_in_tests(self):
          a_string = 'a string'
          a_string[0]
          a_string[7]

          with self.assertRaises(IndexError):
              a_string[8]


  # Exceptions seen

the test passes, showing that assertRaises_ checks that the code in its context (``a_string[8]``), raises the :ref:`Exception<errors>` (:ref:`IndexError<test_index_error>`) it is given in parentheses.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I can also :ref:`index<test_index_returns_first_position_of_item_in_a_list>` with negative numbers, the one for the last item in the :ref:`list<what is a list?>` is ``-1``, like reading from right to left

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 5

        def test_catching_index_error_in_tests(self):
            a_string = 'a string'
            a_string[0]
            a_string[7]
            a_string[-1]

            with self.assertRaises(IndexError):
                a_string[8]

  the test is still green.

* The :ref:`index<test_index_returns_first_position_of_item_in_a_list>` for the first item is negative the total number of items, ``-8`` in this case (like reading from right to left)

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 6

        def test_catching_index_error_in_tests(self):
            a_string = 'a string'
            a_string[0]
            a_string[7]
            a_string[-1]
            a_string[-8]

            with self.assertRaises(IndexError):
                a_string[8]

  still green.

* If I use a negative number that is smaller than the negative of the number of characters in the string_

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 3

            with self.assertRaises(IndexError):
                a_string[8]
            a_string[-9]


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`IndexError<test_index_error>`

  .. code-block:: python

    IndexError: string index out of range

* I add assertRaises_ to :ref:`test_catching_index_error_in_tests`

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 10-11

        def test_catching_index_error_in_tests(self):
            a_string = 'a string'
            a_string[0]
            a_string[7]
            a_string[-1]
            a_string[-8]

            with self.assertRaises(IndexError):
                a_string[8]
            with self.assertRaises(IndexError):
                a_string[-9]


    # Exceptions seen

  the test is green again. I cannot use a number that is smaller than the negative of the total number of items in the string_ to :ref:`index the string<test_index_returns_first_position_of_item_in_a_list>`.

* I add a tuple_ to :ref:`test_catching_index_error_in_tests`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 6

            with self.assertRaises(IndexError):
                a_string[8]
            with self.assertRaises(IndexError):
                a_string[-9]

            a_tuple = (0, 1, 2, 'n')


    # Exceptions seen

* I :ref:`index the tuple<test_index_returns_first_position_of_item_in_a_list>` with ``1``

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 2

            a_tuple = (0, 1, 2, 'n')
            a_tuple[1]


    # Exceptions seen

  the test is still green.

* I use a number that is bigger than the number of items in the tuple_

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 3

            a_tuple = (0, 1, 2, 'n')
            a_tuple[1]
            a_tuple[100]


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`IndexError<test_index_error>`

  .. code-block:: python

    IndexError: tuple index out of range

* I add assertRaises_ to :ref:`test_catching_index_error_in_tests`

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 4-5

            a_tuple = (0, 1, 2, 'n')
            a_tuple[1]

            with self.assertRaises(IndexError):
                a_tuple[100]


    # Exceptions seen

  the test passes.

* I use a negative number to :ref:`index<test_index_returns_first_position_of_item_in_a_list>` the tuple_

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 3

            a_tuple = (0, 1, 2, 'n')
            a_tuple[1]
            a_tuple[-2]

            with self.assertRaises(IndexError):
                a_tuple[100]


    # Exceptions seen

  the test is still green.

* I use a number that is smaller than the negative of the number of items in the tuple_

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 3

            with self.assertRaises(IndexError):
                a_tuple[100]
            a_tuple[-100]


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`IndexError<test_index_error>`

  .. code-block:: python

    IndexError: tuple index out of range

  I cannot use a number that is smaller than the index of the last item in a tuple_.

* I add assertRaises_ to :ref:`test_catching_index_error_in_tests`

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 7-8

            a_tuple = (0, 1, 2, 'n')
            a_tuple[1]
            a_tuple[-2]

            with self.assertRaises(IndexError):
                a_tuple[100]
            with self.assertRaises(IndexError):
                a_tuple[-100]


    # Exceptions seen

* It looks like the assertRaises_ in :ref:`test_catching_index_error_in_tests` are repetitions. They are not, even if the test is still green when I remove the second assertRaises_

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 3

            with self.assertRaises(IndexError):
                a_tuple[100]
            # with self.assertRaises(IndexError):
                a_tuple[-100]


    # Exceptions seen

  :ref:`I show why this is not a repetition at the end of the chapter<one exception one exception handler>`

* I undo the change for now

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 3

            with self.assertRaises(IndexError):
                a_tuple[100]
            with self.assertRaises(IndexError):
                a_tuple[-100]


    # Exceptions seen

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_catching_index_error_in_tests'

:ref:`IndexError<test_index_error>` is raised when I try to :ref:`index a list<test_index_returns_first_position_of_item_in_a_list>`, set_, tuple_ or string_ with a number that is

- bigger than or the same as the number of items in the :ref:`list<what is a list?>`, set_, tuple_ or string_.
- smaller than the negative of the number of items in the :ref:`list<what is a list?>`, set_, tuple_ or string_.

----

*********************************************************************************
test_catching_key_error_in_tests
*********************************************************************************

:ref:`KeyError<test_key_error>` is raised when I try to use a :ref:`key<test_keys_of_a_dictionary>` that is NOT in a :ref:`dictionary<what is a dictionary?>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a test for :ref:`KeyError<test_key_error>` with a :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 6-7

            with self.assertRaises(IndexError):
                a_tuple[100]
            with self.assertRaises(IndexError):
                a_tuple[-100]

        def test_catching_key_error_in_tests(self):
            a_dictionary = {'key': 'value'}


    # Exceptions seen

* If I try to get the value of a :ref:`key<test_keys_of_a_dictionary>` that is in the :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 3

        def test_catching_key_error_in_tests(self):
            a_dictionary = {'key': 'value'}
            a_dictionary['key']


    # Exceptions seen

  the test is green. No issues.

* If I use a :ref:`key<test_keys_of_a_dictionary>` that is NOT in the :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 4

        def test_catching_key_error_in_tests(self):
            a_dictionary = {'key': 'value'}
            a_dictionary['key']
            a_dictionary['not_in_dictionary']


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`KeyError<test_key_error>`

  .. code-block:: shell

    KeyError: 'not_in_dictionary'

* I add :ref:`KeyError<test_key_error>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 8

    # Exceptions seen
    # AssertionError
    # ModuleNotFoundError
    # NameError
    # AttributeError
    # TypeError
    # IndexError
    # KeyError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add assertRaises_ to :ref:`test_catching_key_error_in_tests`

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 5-6

        def test_catching_key_error_in_tests(self):
            a_dictionary = {'key': 'value'}
            a_dictionary['key']

            with self.assertRaises(KeyError):
                a_dictionary['not_in_dictionary']


    # Exceptions seen

  the test passes. showing that

  * assertRaises_ checks that the code in its context (``{'key': 'value'}['not_in_dictionary']``), raises the :ref:`Exception<errors>` (:ref:`KeyError<test_key_error>`) it is given in parentheses.
  * :ref:`KeyError<test_key_error>` is raised when I try to use a :ref:`key<test_keys_of_a_dictionary>` that is NOT in a :ref:`dictionary<what is a dictionary?>`.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_catching_key_error_in_tests'

*********************************************************************************
test_catching_zero_division_error_in_tests
*********************************************************************************

ZeroDivisionError_ is raised when I try to divide a number by ``0``.

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a test for ZeroDivisionError_

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 4-5

            with self.assertRaises(KeyError):
                a_dictionary['not_in_dictionary']

        def test_catching_zero_division_error_in_tests(self):
            1 / 0


    # Exceptions seen

  the terminal_ is my friend, and shows ZeroDivisionError_

  .. code-block:: python

    ZeroDivisionError: division by zero

  because I cannot divide a number by ``0``.

* I add ZeroDivisionError_ to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 9

    # Exceptions seen
    # AssertionError
    # ModuleNotFoundError
    # NameError
    # AttributeError
    # TypeError
    # IndexError
    # KeyError
    # ZeroDivisionError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add assertRaises_ to :ref:`test_catching_zero_division_error_in_tests`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 2-3

        def test_catching_zero_division_error_in_tests(self):
            with self.assertRaises(ZeroDivisionError):
                1 / 0


    # Exceptions seen

  the test passes, showing that

  * assertRaises_ checks that the code in its context (``1 / 0``), raises the :ref:`Exception<errors>` (ZeroDivisionError_) it is given in parentheses.
  * ZeroDivisionError_ is raised when I try to divide any number by ``0``, same as I get ``undefined`` when I try it with a :ref:`calculator`, because dividing by ``0`` is undefined in Mathematics_.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_catching_zero_division_error_in_tests'

----

*********************************************************************************
test_catching_exceptions_in_tests
*********************************************************************************

=================================================================================
how to raise an Exception
=================================================================================

----

I can cause an :ref:`Exception<errors>` to happen with the `raise statement`.

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a test with the `raise statement`_

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 5-6

        def test_catching_zero_division_error_in_tests(self):
            with self.assertRaises(ZeroDivisionError):
                1 / 0

        def test_catching_exceptions_in_tests(self):
            raise Exception


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`Exception<errors>`

  .. code-block:: python

    Exception

  :ref:`Exception<errors>` is the mother of all the :ref:`Exceptions<errors>` covered so far, they :ref:`inherit<everything is an object>` from it.

* I can use the `raise statement`_ to cause any :ref:`Exception<errors>` I want

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 2

        def test_catching_exceptions_in_tests(self):
            raise AssertionError


    # Exceptions seen

  the terminal_ shows the :ref:`Exception<errors>` I give the `raise statement`_

  .. code-block:: python

    AssertionError

* I change the :ref:`Exception<errors>` back

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 2

        def test_catching_exceptions_in_tests(self):
            raise Exception


    # Exceptions seen

  the terminal_ shows :ref:`Exception<errors>`

  .. code-block:: python

    Exception

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add the `assertRaises method`_ to :ref:`test_catching_exceptions_in_tests` to handle the :ref:`Exception<errors>`

.. code-block:: python
  :lineno-start: 55
  :emphasize-lines: 2-3

      def test_catching_exceptions_in_tests(self):
          with self.assertRaises(Exception):
              raise Exception


  # Exceptions seen

the test passes. The `assertRaises method`_ checks that the code under it raises the :ref:`Exception<errors>` it is given in parentheses.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I can use :ref:`Exception<errors>` to catch any of the :ref:`Exceptions<errors>` that :ref:`inherit<everything is an object>` from it (its :ref:`children/subclasses<how to test if something is a subclass>`)

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 5-6

    def test_catching_key_error_in_tests(self):
        a_dictionary = {'key': 'value'}
        a_dictionary['key']

        # with self.assertRaises(KeyError):
        with self.assertRaises(Exception):
            a_dictionary['not_in_dictionary']

    def test_catching_zero_division_error_in_tests(self):

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 2-3

    def test_catching_zero_division_error_in_tests(self):
        # with self.assertRaises(ZeroDivisionError):
        with self.assertRaises(Exception):
            1 / 0

    def test_catching_exceptions_in_tests(self):

  the tests are still green.

  The problem with using :ref:`Exception<errors>` to catch its children, is it does not tell anyone that reads the code what the actual :ref:`Exception<errors>` is.

  It is better to be specific, from the :PEP:`Zen of Python <20>`: ``Explicit is better than implicit``

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 5, 9

        def test_catching_key_error_in_tests(self):
            a_dictionary = {'key': 'value'}
            a_dictionary['key']

            with self.assertRaises(KeyError):
                a_dictionary['not_in_dictionary']

        def test_catching_zero_division_error_in_tests(self):
            with self.assertRaises(ZeroDivisionError):
                1 / 0

        def test_catching_exceptions_in_tests(self):

* I cannot use sibling or cousin :ref:`Exceptions<errors>` to catch other :ref:`Exceptions<errors>`

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 5-6

        def test_catching_key_error_in_tests(self):
            a_dictionary = {'key': 'value'}
            a_dictionary['key']

            # with self.assertRaises(KeyError):
            with self.assertRaises(ModuleNotFoundError):
                a_dictionary['not_in_dictionary']

        def test_catching_zero_division_error_in_tests(self):

  the terminal_ is my friend, and shows :ref:`KeyError<test_key_error>`

  .. code-block:: shell

    KeyError: 'not_in_dictionary'

  because it is not :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>` even though they are both :ref:`Exceptions<errors>`.

* I undo the change

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 2

        def test_catching_key_error_in_tests(self):
            a_dictionary = {'key': 'value'}
            a_dictionary['key']

            with self.assertRaises(KeyError):
                a_dictionary['not_in_dictionary']

        def test_catching_zero_division_error_in_tests(self):

  the test is green again.

* I cannot use children :ref:`Exceptions<errors>` to catch parent :ref:`Exceptions<errors>`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 2-3

        def test_catching_exceptions_in_tests(self):
            # with self.assertRaises(Exception):
            with self.assertRaises(ZeroDivisionError):
                raise Exception


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`Exception<errors>`

  .. code-block:: python

    Exception

  because it is not ZeroDivisionError_ even though it is an :ref:`Exception<errors>`.

* I undo the change

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 2

        def test_catching_exceptions_in_tests(self):
            with self.assertRaises(Exception):
                raise Exception


    # Exceptions seen

  the test is green again.

----

*********************************************************************************
one exception one exception handler
*********************************************************************************

* As promised here is why the second AssertRaises_ in :ref:`test_catching_index_error_in_tests` is not a repetition

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 10

        def test_catching_index_error_in_tests(self):
            a_string = 'a string'
            a_string[0]
            a_string[7]
            a_string[-1]
            a_string[-8]

            with self.assertRaises(IndexError):
                a_string[8]
            # with self.assertRaises(IndexError):
                a_string[-9]

  the test is still green for ``a_string[-9]`` which should causes :ref:`IndexError<test_index_error>`

* If I add a `raise statement`_ before ``a_string[-9]``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 3

            with self.assertRaises(IndexError):
                a_string[8]
                raise Exception
            # with self.assertRaises(IndexError):
                a_string[-9]

  the test is still green, which is NOT the expected behavior. :ref:`Exception<errors>` is not :ref:`IndexError<test_index_error>` and still does NOT get raised, which means the assertRaises_ exits after the first line that causes :ref:`IndexError<test_index_error>` and does NOT run the other lines.

* If I move the `raise statement`_ above the first :ref:`IndexError<test_index_error>`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 2-3

            with self.assertRaises(IndexError):
                raise Exception
                a_string[8]
            # with self.assertRaises(IndexError):
                a_string[-9]

  the terminal_ is my friend, and shows :ref:`Exception<errors>`

  .. code-block:: python

    Exception

  because it is NOT :ref:`IndexError<test_index_error>`, this is the expected behavior.

* I remove the failing line and put the assertRaises_ back in the right place

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 3-6

        def test_catching_index_error_in_tests(self):
            a_string = 'a string'
            a_string[0]
            a_string[7]
            a_string[-1]
            a_string[-8]

            with self.assertRaises(IndexError):
                a_string[8]
            with self.assertRaises(IndexError):
                a_string[-9]

            a_tuple = (0, 1, 2, 'n')
            a_tuple[1]
            a_tuple[-2]

            with self.assertRaises(IndexError):
                a_tuple[100]
            with self.assertRaises(IndexError):
                a_tuple[-100]

        def test_catching_key_error_in_tests(self):

  the test is green again.

I know :ref:`how to test that an Exception is raised`. As a rule of thumb I write one line of code for one :ref:`Exception<errors>`, this way I always know which line caused which :ref:`Exception<errors>`.

----

*********************************************************************************
close the exceptions project
*********************************************************************************

* I close ``test_exceptions.py``

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

I can use assertRaises_ to catch :ref:`Exceptions<errors>` in tests and tested these

* :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`
* :ref:`NameError<test_catching_name_error_in_tests>`
* :ref:`AttributeError<what causes AttributeError?>`
* :ref:`TypeError<what causes TypeError?>`
* :ref:`IndexError<test_index_error>`
* :ref:`KeyError<test_key_error>`
* ZeroDivisionError_ and
* :ref:`The Mother of all Exceptions<test_catching_exceptions_in_tests>`

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
* :ref:`I know how to make a person with Exceptions<how to make a person with exceptions>`

:ref:`Would you like to test handling Exceptions in programs?<how to handle Exceptions (Errors) in programs>`

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