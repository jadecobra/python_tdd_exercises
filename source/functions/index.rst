.. meta::
  :description: Master Python functions step-by-step using Test-Driven Development (TDD). Learn positional and keyword arguments, default values, *args, **kwargs, return statements, and argument unpacking with unittest. Perfect for programming beginners and hands-on coders.
  :keywords: Jacob Itegboje, Python functions for beginners, learn Python functions with TDD, test-driven development Python tutorial, positional vs keyword arguments Python, what does a function return by default, how to write a function in Python, Python *args and **kwargs explained, Python function return None, constant and identity functions Python, Python unittest function examples, argument unpacking python asterisk, beginner Python coding exercises

.. include:: ../links.rst

.. _function: https://docs.python.org/3/glossary.html#term-function
.. _functions: :ref:`function<what is a function?>`
.. _argument: https://docs.python.org/3/glossary.html#term-argument
.. _arguments: argument_
.. _keyword arguments: arguments_
.. _positional arguments: arguments_
.. _return: `return statement`_

#################################################################################
what is a function?
#################################################################################

A function_ is code that is callable_, this means I can write code to do something one time, and call the name for it to do that thing at a different time from when I write it.

functions_ can make code simpler, easier to read, test, reuse, maintain and improve - all the good things.

Part of `Computer Programming`_ is sending :ref:`input data<data structures>` to a process and getting :ref:`output data<data structures>` back

.. code-block:: python

    input_data -> process -> output_data

where ``process`` is the function_. I think of it like mapping a function ``f`` in Mathematics_ with inputs ``x`` and output ``y``

.. math::

  f(x) -> y

in other words

.. code-block:: python

                  f(x) -> y
  function(input_data) -> output_data

the :ref:`function<what is a function?>` does something (the process) with ``input_data`` and returns ``output_data`` as the result.

----

*********************************************************************************
how to make a function
*********************************************************************************

functions_ are made with

* the def_ keyword
* a name
* parentheses and a colon at the end
* the code that makes up the :ref:`function<what is a function?>` (its body) comes after the colon

.. code-block:: python

  def name_of_function():
      the body of the function
      ...

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../code/functions/test_functions.py
  :language: python
  :linenos:

*********************************************************************************
questions about functions
*********************************************************************************

Questions to think about as I go through the chapter

* :ref:`what is a function?<what is a function?>`
* :ref:`what do functions return by default?<test_making_a_function_w_return_none>`
* :ref:`what happens after a function returns?<test_what_happens_after_functions_return>`
* :ref:`what is a constant function?<test_constant_function>`
* :ref:`what is the identity function?<test_identity_function>`
* :ref:`what is a positional argument?<test_functions_w_positional_arguments>`
* :ref:`what is a keyword argument?<test_functions_w_keyword_arguments>`
* :ref:`how can I make arguments a choice in a function?<test_functions_w_optional_arguments>`
* :ref:`how can I make a function take any number of positional arguments?<test_functions_w_unknown_arguments>`
* :ref:`how can I make a function take any number of keyword arguments?<test_functions_w_unknown_arguments>`
* :ref:`how does Python represent positional arguments in a function?<how Python reads positional arguments>`
* :ref:`how does Python represent keyword arguments in a function?<how Python reads keyword arguments>`

----

*********************************************************************************
start the project
*********************************************************************************

* I name this project ``functions``
* I open a terminal_
* I use uv_ to make a directory_ for the project and initialize it

  .. code-block:: python
    :emphasize-lines: 1

    uv init functions

  the terminal_ shows

  .. code-block:: shell

    Initialized project `functions`
    at `.../pumping_python/functions`

  then goes back to the command line.

* I change directory_ to the project

  .. code-block:: python
    :emphasize-lines: 1

    cd functions

  the terminal_ shows I am in the ``functions`` folder_

  .. code-block:: python

    .../pumping_python/functions

* I make a directory_ for the source code

  .. code-block:: python
    :emphasize-lines: 1

    mkdir src

  the terminal_ goes back to the command line.

  .. code-block:: python

    .../pumping_python/functions

* I use the `mv program`_ to change the name of ``main.py`` to ``functions.py`` and move it to the ``src`` folder_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 1

        mv main.py src/functions.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        Move-Item main.py src/functions.py

  the terminal_ goes back to the command line.

* I `make a directory`_ for the tests

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir tests

  the terminal_ goes back to the command line.

* I make the ``tests`` directory_ a `Python package`_

  .. danger:: use 2 underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 1

        touch tests/__init__.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        New-Item tests/__init__.py

  the terminal_ goes back to the command line.

* I make a :ref:`Python file<what is a module?>` for the tests in the ``tests`` directory_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 1

        touch tests/test_functions.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        New-Item tests/test_functions.py

  the terminal_ goes back to the command line.

* I open ``test_functions.py`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_

  .. tip::

    I can open a file_ from the terminal_ in the `Integrated Development Environment (IDE)`_ with the name of the program_ and the name of the file_. That means if I type this in the terminal_

    .. code-block:: python
      :emphasize-lines: 1

      code tests/test_functions.py

    `Visual Studio Code`_ opens ``test_functions.py`` in the :ref:`editor<2 editors>`

* I add :ref:`the first failing test<test_failure>` to ``test_functions.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-7

    import unittest


    class TestFunctions(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

* I go back to the terminal_ to make a requirements file_ for the `Python packages`_ I need

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest" > requirements.txt

  the terminal_ goes back to the command line.

* I add `pytest-watcher`_ to the requirements file_

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest-watcher" >> requirements.txt

  the terminal_ goes back to the command line.

* I install the `Python packages`_ that I wrote in the requirements file_

  .. code-block:: python
    :emphasize-lines: 1

    uv add --requirement requirements.txt

  the terminal_ shows that it installed the `Python packages`_

* I add the new files_ and folders_ to git_ for tracking

  .. code-block:: python
    :emphasize-lines: 1

    git add .

  the terminal_ goes back to the command line.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit --all --message 'setup project'

  the terminal_ shows

  .. code-block:: python

    [main (root-commit) a0b12c3] setup project
     9 files changed, 148 insertions(+)
     create mode 100644 .gitignore
     create mode 100644 .python-version
     create mode 100644 README.md
     create mode 100644 pyproject.toml
     create mode 100644 requirements.txt
     create mode 100644 src/functions.py
     create mode 100644 tests/__init__.py
     create mode 100644 tests/test_functions.py
     create mode 100644 uv.lock

  then goes back to the command line.

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 8, 10

    ================================ FAILURES ================================
    _______________________ TestFunctions.test_failure _______________________

    self = <tests.test_functions.TestFunctions testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_functions.py:7: AssertionError
    ======================== short test summary info =========================
    FAILED tests/test_functions.py::TestFunctions::test_failure - AssertionError: True is not false
    =========================== 1 failed in X.YZs ============================

  because :ref:`True<test_what_is_true>` is NOT :ref:`False<test_what_is_false>`

  .. admonition:: if the terminal_ does not show the same error, then check

    * if your ``tests/__init__.py`` has two underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``
    * if you ran ``echo "pytest-watcher" >> requirements.txt``, to add ``pytest-watcher`` to the requirements file_

    fix those errors and try to run ``uv run pytest-watcher . --now`` again

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_functions.py`` in the :ref:`editor<2 editors>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7-8
    :emphasize-text: AssertionError

    class TestFunctions(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions seen
    # AssertionError

* then I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

  the test passes.

----

*********************************************************************************
test_why_use_a_function
*********************************************************************************

Why would I use a :ref:`function<what is a function?>` when I can just write code to do the thing I want?

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I change ``test_failure`` to ``test_why_use_a_function`` with an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3-6

    class TestFunctions(unittest.TestCase):

        def test_why_use_a_function(self):
            reality = 1 + 0
            my_expectation = 0
            self.assertEqual(reality, my_expectation)


    # Exceptions seen
    # AssertionError

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 1 != 0

  because ``1`` is NOT equal to ``0``

  - ``reality`` is the name or :ref:`variable<what is a variable?>` I gave to the result of ``1 + 0``
  - ``my_expectation`` is the name or :ref:`variable<what is a variable?>` I gave to ``0``
  - ``assertEqual(reality, my_expectation)`` is  asking Python_ if ``1 + 0 is equal to 0``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change ``my_expectation`` to match reality

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 3-4

        def test_why_use_a_function(self):
            reality = 1 + 0
            # my_expectation = 0
            my_expectation = 1
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 7-9

        def test_why_use_a_function(self):
            reality = 1 + 0
            # my_expectation = 0
            my_expectation = 1
            self.assertEqual(reality, my_expectation)

            reality = 1 + 1
            my_expectation = 1
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 2 != 1

* I change ``my_expectation`` to ``2``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 2-3

            reality = 1 + 1
            # my_expectation = 1
            my_expectation = 2
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 6-8

            reality = 1 + 1
            # my_expectation = 1
            my_expectation = 2
            self.assertEqual(reality, my_expectation)

            reality = 1 + 2
            my_expectation = 2
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<What causes AssertionError?>`

  .. code-block:: python

    AssertionError: 3 != 2

* I change ``my_expectation`` to ``3``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 2-3

            reality = 1 + 2
            # my_expectation = 2
            my_expectation = 3
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 6-8

            reality = 1 + 2
            # my_expectation = 2
            my_expectation = 3
            self.assertEqual(reality, my_expectation)

            reality = 1 + 3
            my_expectation = 3
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 4 != 3

* I change ``my_expectation`` to ``4``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 2-3

            reality = 1 + 3
            # my_expectation = 3
            my_expectation = 4
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 6-8

            reality = 1 + 3
            # my_expectation = 3
            my_expectation = 4
            self.assertEqual(reality, my_expectation)

            reality = 1 + 4
            my_expectation = 4
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 5 != 4

* I change ``my_expectation`` to ``5``

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 2-3

            reality = 1 + 4
            # my_expectation = 4
            my_expectation = 5
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 6-8

            reality = 1 + 4
            # my_expectation = 4
            my_expectation = 5
            self.assertEqual(reality, my_expectation)

            reality = 1 + 5
            my_expectation = 5
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 6 != 5

* I change ``my_expectation`` to ``6``

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 2-3

            reality = 1 + 5
            # my_expectation = 5
            my_expectation = 6
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 6-8

            reality = 1 + 5
            # my_expectation = 5
            my_expectation = 6
            self.assertEqual(reality, my_expectation)

            reality = 1 + 6
            my_expectation = 6
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 7 != 6

* I change ``my_expectation`` to ``7``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2-3

            reality = 1 + 6
            # my_expectation = 6
            my_expectation = 7
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 6-8

            reality = 1 + 6
            # my_expectation = 6
            my_expectation = 7
            self.assertEqual(reality, my_expectation)

            reality = 1 + 7
            my_expectation = 7
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 8 != 7

* I change ``my_expectation`` to ``8``

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 2-3

            reality = 1 + 7
            # my_expectation = 7
            my_expectation = 8
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 6-8

            reality = 1 + 7
            # my_expectation = 7
            my_expectation = 8
            self.assertEqual(reality, my_expectation)

            reality = 1 + 8
            my_expectation = 8
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 9 != 8

* I change ``my_expectation`` to ``9``

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 2-3

            reality = 1 + 8
            # my_expectation = 8
            my_expectation = 9
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 6-8

            reality = 1 + 8
            # my_expectation = 8
            my_expectation = 9
            self.assertEqual(reality, my_expectation)

            reality = 1 + 9
            my_expectation = 9
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 10 != 9

* I change ``my_expectation`` to ``10``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 49-50

        def test_why_use_a_function(self):
            reality = 1 + 0
            # my_expectation = 0
            my_expectation = 1
            self.assertEqual(reality, my_expectation)

            reality = 1 + 1
            # my_expectation = 1
            my_expectation = 2
            self.assertEqual(reality, my_expectation)

            reality = 1 + 2
            # my_expectation = 2
            my_expectation = 3
            self.assertEqual(reality, my_expectation)

            reality = 1 + 3
            # my_expectation = 3
            my_expectation = 4
            self.assertEqual(reality, my_expectation)

            reality = 1 + 4
            # my_expectation = 4
            my_expectation = 5
            self.assertEqual(reality, my_expectation)

            reality = 1 + 5
            # my_expectation = 5
            my_expectation = 6
            self.assertEqual(reality, my_expectation)

            reality = 1 + 6
            # my_expectation = 6
            my_expectation = 7
            self.assertEqual(reality, my_expectation)

            reality = 1 + 7
            # my_expectation = 7
            my_expectation = 8
            self.assertEqual(reality, my_expectation)

            reality = 1 + 8
            # my_expectation = 8
            my_expectation = 9
            self.assertEqual(reality, my_expectation)

            reality = 1 + 9
            # my_expectation = 9
            my_expectation = 10
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* all those :ref:`assertions<what is an assertion?>` test what happens when I add a number to ``1``, what if I want to test what happens when I add a number to ``2``? I would have to   change ``1`` in 10 places. I change ``1`` to ``2`` for the ``reality`` :ref:`variables<what is a variable?>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 2-3, 8-9, 14-15, 20-21, 26-27, 32-33, 38-39, 44-45, 50-51, 56-57
    :emphasize-text: 2

        def test_why_use_a_function(self):
            # reality = 1 + 0
            reality = 2 + 0
            # my_expectation = 0
            my_expectation = 1
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 1
            reality = 2 + 1
            # my_expectation = 1
            my_expectation = 2
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 2
            reality = 2 + 2
            # my_expectation = 2
            my_expectation = 3
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 3
            reality = 2 + 3
            # my_expectation = 3
            my_expectation = 4
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 4
            reality = 2 + 4
            # my_expectation = 4
            my_expectation = 5
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 5
            reality = 2 + 5
            # my_expectation = 5
            my_expectation = 6
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 6
            reality = 2 + 6
            # my_expectation = 6
            my_expectation = 7
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 7
            reality = 2 + 7
            # my_expectation = 7
            my_expectation = 8
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 8
            reality = 2 + 8
            # my_expectation = 8
            my_expectation = 9
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 9
            reality = 2 + 9
            # my_expectation = 9
            my_expectation = 10
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 2 != 1

* I change ``my_expectation`` for each :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 5-6, 12-13, 19-20, 26-27, 33-34, 40-41, 47-48, 54-55, 61-62, 68-69
    :emphasize-text: 2 3 4 5 6 7 8 9 10 11

        def test_why_use_a_function(self):
            # reality = 1 + 0
            reality = 2 + 0
            # my_expectation = 0
            # my_expectation = 1
            my_expectation = 2
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 1
            reality = 2 + 1
            # my_expectation = 1
            # my_expectation = 2
            my_expectation = 3
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 2
            reality = 2 + 2
            # my_expectation = 2
            # my_expectation = 3
            my_expectation = 4
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 3
            reality = 2 + 3
            # my_expectation = 3
            # my_expectation = 4
            my_expectation = 5
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 4
            reality = 2 + 4
            # my_expectation = 4
            # my_expectation = 5
            my_expectation = 6
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 5
            reality = 2 + 5
            # my_expectation = 5
            # my_expectation = 6
            my_expectation = 7
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 6
            reality = 2 + 6
            # my_expectation = 6
            # my_expectation = 7
            my_expectation = 8
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 7
            reality = 2 + 7
            # my_expectation = 7
            # my_expectation = 8
            my_expectation = 9
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 8
            reality = 2 + 8
            # my_expectation = 8
            # my_expectation = 9
            my_expectation = 10
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 9
            reality = 2 + 9
            # my_expectation = 9
            # my_expectation = 10
            my_expectation = 11
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* I open a new terminal_ then change directories to ``functions``

  .. code-block:: python
    :emphasize-lines: 1

    cd functions

  the terminal_ shows I am in the ``functions`` folder_

  .. code-block:: python

    .../pumping_python/functions

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_why_use_a_function'

  the terminal_ shows a summary of the changes then goes back to the command line.

* I go back to the terminal_ that is running the tests

-----

* What if I want to test what happens when I add ``3`` to a number? Wait! No more, please! I do not want to have to make a change for each new number, there has to be a better way. I can use a :ref:`function<what is a function?>` for the parts that repeat, I add one to ``test_functions.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    import unittest


    def add_x(number):
        return 2 + number


    class TestFunctions(unittest.TestCase):

* I use the new :ref:`function<what is a function?>` for ``reality`` in the first :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 5-6
    :emphasize-text: add_x

    class TestFunctions(unittest.TestCase):

        def test_why_use_a_function(self):
            # reality = 1 + 0
            # reality = 2 + 0
            reality = add_x(0)
            # my_expectation = 0
            # my_expectation = 1
            my_expectation = 2
            self.assertEqual(reality, my_expectation)


  the test is still green.

* I use the ``add_x`` :ref:`function<what is a function?>` for the other :ref:`assertions<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 11-12, 19-20, 27-28, 35-36, 43-44, 51-52
    :emphasize-text: add_x

        def test_why_use_a_function(self):
            # reality = 1 + 0
            # reality = 2 + 0
            reality = add_x(0)
            # my_expectation = 0
            # my_expectation = 1
            my_expectation = 2
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 1
            # reality = 2 + 1
            reality = add_x(1)
            # my_expectation = 1
            # my_expectation = 2
            my_expectation = 3
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 2
            # reality = 2 + 2
            reality = add_x(2)
            # my_expectation = 2
            # my_expectation = 3
            my_expectation = 4
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 3
            # reality = 2 + 3
            reality = add_x(3)
            # my_expectation = 3
            # my_expectation = 4
            my_expectation = 5
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 4
            # reality = 2 + 4
            reality = add_x(4)
            # my_expectation = 4
            # my_expectation = 5
            my_expectation = 6
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 5
            # reality = 2 + 5
            reality = add_x(5)
            # my_expectation = 5
            # my_expectation = 6
            my_expectation = 7
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 6
            # reality = 2 + 6
            reality = add_x(6)
            # my_expectation = 6
            # my_expectation = 7
            my_expectation = 8

  still green.

* Now I only have to make a change in one place if I want to test what happens if I add ``3`` to a number

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4
    :emphasize-text: 5-6

    import unittest


    def add_x(number):
        # return 2 + number
        return 3 + number


    class TestFunctions(unittest.TestCase):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 3 != 2

* I change the expectations for the :ref:`assertions<what is an assertion?>` one at a time

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 7-8, 16-17, 25-26, 34-35, 43-44, 52-53, 61-62, 70-71, 79-80, 88-89

        def test_why_use_a_function(self):
            # reality = 1 + 0
            # reality = 2 + 0
            reality = add_x(0)
            # my_expectation = 0
            # my_expectation = 1
            # my_expectation = 2
            my_expectation = 3
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 1
            # reality = 2 + 1
            reality = add_x(1)
            # my_expectation = 1
            # my_expectation = 2
            # my_expectation = 3
            my_expectation = 4
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 2
            # reality = 2 + 2
            reality = add_x(2)
            # my_expectation = 2
            # my_expectation = 3
            # my_expectation = 4
            my_expectation = 5
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 3
            # reality = 2 + 3
            reality = add_x(3)
            # my_expectation = 3
            # my_expectation = 4
            # my_expectation = 5
            my_expectation = 6
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 4
            # reality = 2 + 4
            reality = add_x(4)
            # my_expectation = 4
            # my_expectation = 5
            # my_expectation = 6
            my_expectation = 7
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 5
            # reality = 2 + 5
            reality = add_x(5)
            # my_expectation = 5
            # my_expectation = 6
            # my_expectation = 7
            my_expectation = 8
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 6
            # reality = 2 + 6
            reality = add_x(6)
            # my_expectation = 6
            # my_expectation = 7
            # my_expectation = 8
            my_expectation = 9
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 7
            # reality = 2 + 7
            reality = add_x(7)
            # my_expectation = 7
            # my_expectation = 8
            # my_expectation = 9
            my_expectation = 10
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 8
            # reality = 2 + 8
            reality = add_x(8)
            # my_expectation = 8
            # my_expectation = 9
            # my_expectation = 10
            my_expectation = 11
            self.assertEqual(reality, my_expectation)

            # reality = 1 + 9
            # reality = 2 + 9
            reality = add_x(9)
            # my_expectation = 9
            # my_expectation = 10
            # my_expectation = 11
            my_expectation = 12
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit --all --message 'extract add_x function'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can use a function to remove repetition<test_why_use_a_function>`. Is there :ref:`a better way to handle the changing results?<a better way to handle the results changing>`

----

*********************************************************************************
test_making_a_function_w_pass
*********************************************************************************

I can make a :ref:`function<what is a function?>` with the pass_ keyword

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a new test to ``test_functions.py`` in the :ref:`editor<2 editors>`

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 10-11

            # reality = 1 + 9
            # reality = 2 + 9
            reality = add_x(9)
            # my_expectation = 9
            # my_expectation = 10
            # my_expectation = 11
            my_expectation = 12
            self.assertEqual(reality, my_expectation)

        def test_making_a_function_w_pass(self):
            self.assertIs(src.functions.w_pass(), None)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block::

    NameError: name 'src' is not defined

  because Python_ does not know what I mean by ``src`` since I do not have a definition for it in ``test_functions.py``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add :ref:`NameError<test_catching_name_error_in_tests>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 3
    :emphasize-text: NameError

    # Exceptions seen
    # AssertionError
    # NameError

* I add an `import statement`_ at the top of the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.functions
    import unittest


    class TestFunctions(unittest.TestCase):

  - ``import src.functions`` brings in an :ref:`object<what is a class?>` that represents the ``functions.py`` :ref:`module<what is a module?>` from the ``src`` folder_ so I can use it in ``test_functions.py``
  - I like to sort my `import statements`_ alphabetically
  - the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

    .. code-block:: shell

      AttributeError: module 'src.functions'
                    has no attribute 'w_pass'

    because ``functions.py`` in the ``src`` folder_ does not have anything named ``w_pass`` inside it

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 107
    :emphasize-lines: 4
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError

* I use the :ref:`Explorer<explorer on left>` to open ``functions.py`` from the ``src`` folder in the :ref:`editor<2 editors>`

* I delete the text in the file_ then add a :ref:`function definition<how to make a function>` to ``functions.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def w_pass():
        pass

  * the :ref:`assertion<what is an assertion?>` - ``self.assertIs(src.functions.w_pass(), None)`` checks if the result of a call to ``w_pass`` in ``functions.py`` in the ``src`` folder_ also known as ``src.functions.w_pass``, is the same :ref:`object<what is a class?>` as :ref:`None<what is None?>`

  * the :ref:`function definition<how to make a function>` simply says pass_ and the test passes.
  * pass_ is a special keyword that allows the :ref:`function definition<how to make a function>` to follow Python_ language rules (the :ref:`function<what is a function?>` must have a body)
  * the test passes because :ref:`all functions return None by default, as if they have an invisible line that says return None<test_making_a_function_w_return_none>`, which leads me to the next test, but first git_ business

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_making_a_function_w_pass'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can make a function with pass.<test_making_a_function_w_pass>`

----

*********************************************************************************
test_making_a_function_w_return
*********************************************************************************

I can also make a function with a `return statement`_

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a new failing test to ``test_functions.py``

  .. code-block:: python
    :lineno-start: 103
    :emphasize-lines: 4-5

        def test_making_a_function_w_pass(self):
            self.assertIs(src.functions.w_pass(), None)

        def test_making_a_function_w_return(self):
            self.assertIs(src.functions.w_return(), None)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.functions'
                    has no attribute 'w_return'

  because ``functions.py`` in the ``src`` folder_ does not have anything with the name ``w_return`` in it

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add the new :ref:`function<what is a function?>` with the pass_ keyword to ``functions.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 5-6

  def w_pass():
      pass


  def w_return():
      pass

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change pass_ to a `return statement`_

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2-3

    def w_return():
        # pass
        return

  * the :ref:`assertion<what is an assertion?>` - ``self.assertIs(src.functions.w_return(), None)`` checks if the result of a call to ``w_return`` in ``functions.py`` in the ``src`` folder_ also known as ``src.functions.w_return``, is the same :ref:`object<what is a class?>` as :ref:`None<what is None?>`
  * the :ref:`function definition<how to make a function>` simply says return_ and the test passes.
  * return_ is a special keyword that is used to send output from a :ref:`function<what is a function?>`.
  * the test is still green because :ref:`all functions return None by default, as if they have an invisible line that says return None<test_making_a_function_w_return_none>`

* I remove the commented line

  .. code-block:: python
    :lineno-start: 5

    def w_return():
        return

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_making_a_function_w_return'

  the terminal_ shows a summary of the changes then goes back to the command line.

I have two :ref:`functions<what is a function?>` with different statements, and the tests show that they both return :ref:`None<what is None?>`

.. code-block:: python

  src.functions.w_pass()
  pass

.. code-block:: python

  src.functions.w_return()
  return

their contents are different, their results are the same because ":ref:`all functions return None by default, as if they have an invisible line that says return None<test_making_a_function_w_return_none>`", which leads me to the next test.

:ref:`I can make a function with a return statement<test_making_a_function_w_return>`

----

*********************************************************************************
test_making_a_function_w_return_none
*********************************************************************************

I can make a :ref:`function<what is a function?>` with a `return statement`_ that says exactly what the :ref:`function<what is a function?>` returns

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add another failing test to ``test_functions.py``

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 4-7

        def test_making_a_function_w_return(self):
            self.assertIs(src.functions.w_return(), None)

        def test_making_a_function_w_return_none(self):
            self.assertIs(
                src.functions.w_return_none(), None
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.functions'
                    has no attribute 'w_return_none'

  because ``w_return_none`` is not defined in ``functions.py`` in the ``src`` folder_

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a :ref:`function definition<how to make a function>` to ``functions.py``

.. code-block:: python
  :lineno-start: 5
  :emphasize-lines: 5-6

  def w_return():
      return


  def w_return_none():
      return

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add :ref:`None<what is None?>` to the `return statement`_

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2-3
    :emphasize-text: None

    def w_return_none():
        # return
        return None

  the test is still green.

* I change :ref:`None<what is None?>` to ``'something'``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 3-4
    :emphasize-text: something

    def w_return_none():
        # return
        # return None
        return 'something'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'something' is not None

  because the :ref:`assertion<what is an assertion?>` expects :ref:`None<what is None?>` and the :ref:`function<what is a function?>` returns ``'something'``

* I undo the change

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 3-4

    def w_return_none():
        # return
        return None
        # return 'something'

  the test is green again.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 9

    def w_return_none():
        return None

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_making_a_function_w_return_none'

  the terminal_ shows a summary of the changes then goes back to the command line.

I have three :ref:`functions<what is a function?>` with different statements, and the tests show that they all return :ref:`None<what is None?>`

.. code-block:: python

  src.functions.w_pass()
  pass

.. code-block:: python

  src.functions.w_return()
  return

.. code-block:: python

  src.functions.w_return_none()
  return None

their contents are different, their results are the same because ":ref:`all functions return None by default, as if they have an invisible line that says ...<test_making_a_function_w_return_none>`"

I like to write my :ref:`functions<what is a function?>` with ``return None``, so that anyone can see what the :ref:`function<what is a function?>` returns without having to think about it.

:ref:`I can make a function with return None.<test_making_a_function_w_return_none>`

----

*********************************************************************************
test_what_happens_after_functions_return
*********************************************************************************

The `return statement`_ is the last thing to run in a :ref:`function<what is a function?>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a test to ``test_functions.py``

  .. code-block:: python
    :lineno-start: 109
    :emphasize-lines: 6-9

        def test_making_a_function_w_return_none(self):
            self.assertIs(
                src.functions.w_return_none(), None
            )

        def test_what_happens_after_functions_return(self):
            self.assertIs(
                src.functions.return_is_last(), None
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.functions'
                    has no attribute 'return_is_last'

  because ``functions.py`` does not have a definition for it, yet

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a :ref:`function<what is a function?>` to ``functions.py``

.. code-block:: python
  :lineno-start: 9
  :emphasize-lines: 5-6

  def w_return_none():
      return None


  def return_is_last():
      return None

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a `return statement`_

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2-3

    def return_is_last():
        return 'something'
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'something' is not None

  - because the :ref:`assertion<what is an assertion?>` expects :ref:`None<what is None?>` and the :ref:`function<what is a function?>` returns ``'something'``
  - the :ref:`function<what is a function?>` does not run the second `return statement`_   because the `return statement`_ is the last thing to run in a :ref:`function<what is a function?>`, which means the second `return statement`_ will never run. It is not reachable (this is called dead code).

  .. tip::

    The `Integrated Development Environment (IDE)`_ shows that the second return statement will not run by graying it out

* I move ``return None``, to make it the first `return statement`_

  .. tip:: In `Visual Studio Code`_ I can move lines I select or where the cursor is, with :kbd:`alt/option+Up` on the keyboard to move lines up or :kbd:`alt/option+Down` to move lines down

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2-3
    :emphasize-text: None

    def return_is_last():
        return None
        return 'something'

  the test is green again

* I change the second `return statement`_ as a reminder

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 3
    :emphasize-text: will never run

    def return_is_last():
        return None
        return 'will NEVER run'

  the second `return statement`_ is now like a comment, and the test is still green because :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_what_happens_after_functions_return'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*********************************************************************************
test_constant_function
*********************************************************************************

constant functions_ always return the same thing when they are called

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a test to ``test_functions.py``

  .. code-block:: python
    :lineno-start: 114
    :emphasize-lines: 6-9

        def test_what_happens_after_a_function_returns(self):
            self.assertIs(
                src.functions.return_is_last(), None
            )

        def test_constant_function(self):
            reality = src.functions.constant()
            my_expectation = 'the same thing'
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.functions'
                    has no attribute 'constant'

  because I have not added a definition for ``constant`` in ``functions.py`` in the ``src`` folder_

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the :ref:`function<what is a function?>` to ``functions.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 6-7

    def return_is_last():
        return None
        return 'will never run'


    def constant():
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None != 'the same thing'

  because the :ref:`assertion<what is an assertion?>` expects ``'the same thing'`` and the :ref:`function<what is a function?>` returns :ref:`None<what is None?>`

* I change the `return statement`_ to give the test what it wants

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 2-3

    def constant():
        # return None
        return 'the same thing'

  the test passes.

* I remove the commented line

  .. code-block:: python
    :lineno-start: 18

    def constant():
        return 'the same thing'

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit --all --message 'add test_constant_function'

  the terminal_ shows a summary of the changes then goes back to the command line.

A constant :ref:`function<what is a function?>` always returns the same thing when called, I can use them in place of :ref:`variables<what is a variable?>`, though the number of cases where they are faster than :ref:`variables<what is a variable?>` is pretty small. It is something like if the :ref:`function<what is a function?>` is called less than 10 times (who's counting?)

:ref:`a constant function always returns the same thing.<test_constant_function>`

----

*********************************************************************************
test_identity_function
*********************************************************************************

The identity :ref:`function<what is a function?>` returns its input as output, it is also in the :ref:`Truth Table<truth table>` chapter in :ref:`test_logical_identity`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a failing test to ``test_functions.py``

  .. code-block:: python
    :lineno-start: 119
    :emphasize-lines: 6-9

        def test_constant_function(self):
            reality = src.functions.constant()
            my_expectation = 'the same thing'
            self.assertEqual(reality, my_expectation)

        def test_identity_function(self):
            reality = src.functions.identity(None)
            my_expectation = None
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.functions'
                    has no attribute 'identity'

  is it because ``functions.py`` has no ``identity``?

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`function<what is a function?>` for ``identity`` to ``functions.py``

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 5-6

    def constant():
        return 'the same thing'


    def identity():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: identity() takes 0 positional arguments
               but 1 was given

  because the :ref:`definition<how to make a function>` for ``identity`` does not allow calling it with inputs and the test sends :ref:`None<what is None?>` as input

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 130
    :emphasize-lines: 5
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* I add a name in parentheses for the ``identity`` :ref:`function<what is a function?>` to take input, in ``functions.py``

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 1-2

    # def identity():
    def identity(the_input):
        return None

  the test passes. I am genius.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

The requirement for the :ref:`identity function<test_logical_identity>` is that it returns the same thing it is given, this test passes when :ref:`None<what is None?>` is given as input.

Does it pass when another value is given or does it always return :ref:`None<what is None?>`? Time to test it

* I add a new :ref:`assertion<what is an assertion?>` to :ref:`test_identity_function` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 124
    :emphasize-lines: 6-8

        def test_identity_function(self):
            reality = src.functions.identity(None)
            my_expectation = None
            self.assertEqual(reality, my_expectation)

            reality = src.functions.identity(object)
            my_expectation = object
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None != <class 'object'>

  because the :ref:`function<what is a function?>` always returns :ref:`None<what is None?>` not ``<class 'object'>`` or what it receives as input. I am not all the way genius, yet

* I make the ``identity`` :ref:`function<what is a function?>` in ``functions.py`` return what it gets

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 3-4

    # def identity():
    def identity(the_input):
        # return None
        return the_input

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 22

    def identity(the_input):
        return the_input

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit --all --message 'add test_identity_function'

  the terminal_ shows a summary of the changes then goes back to the command line.

I sometimes use the :ref:`Identity Function<test_identity_function>` when I am testing, to see if my test is connected to what I am testing. If I can send something (input) and get it back, I can start making changes to see how it affects the output.

:ref:`The Identity Function returns its input as output.<test_identity_function>`

----

*********************************************************************************
test_functions_w_positional_arguments
*********************************************************************************

So far, the :ref:`functions<what is a function?>` take no input or one input, the next tests use functions_ that take more than one input.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a failing test to ``test_functions.py``

  .. code-block:: python
    :lineno-start: 129
    :emphasize-lines: 5-10

            reality = src.functions.identity(object)
            my_expectation = object
            self.assertEqual(reality, my_expectation)

        def test_functions_w_positional_arguments(self):
            reality = src.functions.w_positional_arguments(
                'first', 'last',
            )
            my_expectation = ('first', 'last')
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.functions'
                    has no attribute 'w_positional_arguments'

  because ...

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the :ref:`function<what is a function?>` to ``functions.py``

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 5-6

    def identity(the_input):
        return the_input


    def w_positional_arguments():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: w_positional_arguments() takes
               0 positional arguments but 2 were given

  because the :ref:`definition<how to make a function>` for ``w_positional_arguments`` does not allow inputs and the test sends two in the call (``'first'`` and ``'last'``)

* I make the :ref:`function<what is a function?>` take input by adding a name in parentheses

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 1-2

    # def w_positional_arguments():
    def w_positional_arguments(first_input):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: w_positional_arguments() takes
               1 positional argument but 2 were given

  because the :ref:`definition<how to make a function>` for ``w_positional_arguments`` now allows only one input and the test sends two in the call (``'first'`` and ``'last'``)

* I make ``w_positional_arguments`` take another input by adding another name in parentheses

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 2-3

    # def w_positional_arguments():
    # def w_positional_arguments(first_input):
    def w_positional_arguments(first_input, last_input):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None != ('first', 'last')

  because the :ref:`function<what is a function?>` returns :ref:`None<what is None?>` and the :ref:`assertion<what is an assertion?>` expects ``('first', 'last')``

* I change the `return statement`_ to make the :ref:`function<what is a function?>` return its inputs as output

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 4-5

    # def w_positional_arguments():
    # def w_positional_arguments(first_input):
    def w_positional_arguments(first_input, last_input):
        # return None
        return first_input, last_input

  the test passes, because the :ref:`function<what is a function?>` always returns ``first_input, last_input`` and the call in the test sends ``'first'`` as ``first_input`` and ``'last'`` as ``last_input``, which is equal to ``my_expectation``

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 22

    def identity(the_input):
        return the_input


    def w_positional_arguments(first_input, last_input):
        return first_input, last_input

* The problem with giving arguments this way is that they always have to be in the order the :ref:`function<what is a function?>` expects or I get something different. I add an :ref:`assertion<what is an assertion?>` to show this in  :ref:`test_functions_w_positional_arguments` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 8-12

        def test_functions_w_positional_arguments(self):
            reality = src.functions.w_positional_arguments(
                'first', 'last',
            )
            my_expectation = ('first', 'last')
            self.assertEqual(reality, my_expectation)

            reality = src.functions.w_positional_arguments(
                'last', 'first',
            )
            my_expectation = ('first', 'last')
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: Tuples differ: ('last', 'first')
                                != ('first', 'last')

  because the :ref:`function<what is a function?>` always returns ``first_input, last_input`` and the call in this test sends ``'last'`` as ``first_input`` and ``'first'`` as ``last_input``

* I change ``my_expectation`` to match ``reality``

  .. code-block:: python
    :lineno-start: 140
    :emphasize-lines: 4-5
    :emphasize-text: last

            reality = src.functions.w_positional_arguments(
                'last', 'first',
            )
            # my_expectation = ('first', 'last')
            my_expectation = ('last', 'first')
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* I add :ref:`variables<what is a variable?>` to use them to remove repetition of ``'first'`` and ``'last'``

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 2

        def test_functions_w_positional_arguments(self):
            first, last = 'first', 'last'

            reality = src.functions.w_positional_arguments(
                'first', 'last',
            )
            my_expectation = ('first', 'last')
            self.assertEqual(reality, my_expectation)

* I use the new :ref:`variables<what is a variable?>` to remove repetition of ``'first'`` and ``'last'``

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 5-6, 8-9, 13-14, 18-19

        def test_functions_w_positional_arguments(self):
            first, last = 'first', 'last'

            reality = src.functions.w_positional_arguments(
                # 'first', 'last',
                first, last,
            )
            # my_expectation = ('first', 'last')
            my_expectation = (first, last)
            self.assertEqual(reality, my_expectation)

            reality = src.functions.w_positional_arguments(
                # 'last', 'first',
                last, first,
            )
            # my_expectation = ('first', 'last')
            # my_expectation = ('last', 'first')
            my_expectation = (last, first)
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test is still green.

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 144
    :emphasize-lines: 10-15

            reality = src.functions.w_positional_arguments(
                # 'last', 'first',
                last, first,
            )
            # my_expectation = ('first', 'last')
            # my_expectation = ('last', 'first')
            my_expectation = (last, first)
            self.assertEqual(reality, my_expectation)

            first_number, second_number = 0, 1
            reality = src.functions.w_positional_arguments(
                first_number, second_number,
            )
            my_expectation = (second_number, first_number)
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Tuples differ: (0, 1) != (1, 0)

  because the :ref:`function<what is a function?>` always returns ``first_input, last_input`` and the call in this test sends ``0`` as ``first_input`` and ``1`` as ``last_input``

* I change ``my_expectation`` to match ``reality``

  .. code-block:: python
    :lineno-start: 153
    :emphasize-lines: 5

            first_number, second_number = 0, 1
            reality = src.functions.w_positional_arguments(
                first_number, second_number,
            )
            # my_expectation = (second_number, first_number)
            my_expectation = (first_number, second_number)
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* I add one more :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 153
    :emphasize-lines: 9-15

            first_number, second_number = 0, 1
            reality = src.functions.w_positional_arguments(
                first_number, second_number,
            )
            # my_expectation = (second_number, first_number)
            my_expectation = (first_number, second_number)
            self.assertEqual(reality, my_expectation)

            a_tuple = (1, 2, 3, 'n')
            a_list = [1, 2, 3, 'n']
            reality = src.functions.w_positional_arguments(
                a_list, a_tuple,
            )
            my_expectation = (a_tuple, a_list)
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Tuples differ:
            ((1, 2, 3, 'n'), [1, 2, 3, 'n'])
         != ([1, 2, 3, 'n'], (1, 2, 3, 'n'))

  because the :ref:`function<what is a function?>` always returns ``first_input, last_input`` and the call in this test sends ``(1, 2, 3, 'n')`` as ``first_input`` and ``[1, 2, 3, 'n']`` as ``last_input``

* I change ``reality`` to match ``my_expectation``

  .. code-block:: python
    :lineno-start: 161
    :emphasize-lines: 4-5

            a_tuple = (1, 2, 3, 'n')
            a_list = [1, 2, 3, 'n']
            reality = src.functions.w_positional_arguments(
                # a_list, a_tuple,
                a_tuple, a_list,
            )
            my_expectation = (a_tuple, a_list)
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 133

        def test_functions_w_positional_arguments(self):
            first, last = 'first', 'last'

            reality = src.functions.w_positional_arguments(
                first, last,
            )
            my_expectation = (first, last)
            self.assertEqual(reality, my_expectation)

            reality = src.functions.w_positional_arguments(
                last, first,
            )
            my_expectation = (last, first)
            self.assertEqual(reality, my_expectation)

            first_number, second_number = 0, 1
            reality = src.functions.w_positional_arguments(
                first_number, second_number,
            )
            my_expectation = (first_number, second_number)
            self.assertEqual(reality, my_expectation)

            a_tuple = (1, 2, 3, 'n')
            a_list = [1, 2, 3, 'n']
            reality = src.functions.w_positional_arguments(
                a_tuple, a_list,
            )
            my_expectation = (a_tuple, a_list)
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_functions_w_positional_arguments'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can call functions with positional arguments<test_functions_w_positional_arguments>`

----

*********************************************************************************
test_functions_w_keyword_arguments
*********************************************************************************

The tests show that positional arguments must always be given in the right order. What if I forget the order? What if there are many inputs?

I can use `Keyword Arguments`_ to make sure the :ref:`function<what is a function?>` always gets the values for the inputs it expects, that way it does what I want even when I send inputs out of order.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a new test to ``test_functions.py``

  .. code-block:: python
    :lineno-start: 155
    :emphasize-lines: 9-14

            a_tuple = (1, 2, 3, 'n')
            a_list = [1, 2, 3, 'n']
            reality = src.functions.w_positional_arguments(
                a_tuple, a_list,
            )
            my_expectation = (a_tuple, a_list)
            self.assertEqual(reality, my_expectation)

        def test_functions_w_keyword_arguments(self):
            reality = src.functions.w_keyword_arguments(
                first_input='first', last_input='last',
            )
            my_expectation = ('first', 'last')
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.functions'
                    has no attribute 'w_keyword_arguments'

  because ``functions.py`` in the ``src`` folder_ does not have a definition for ``w_keyword_arguments``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`function definition<how to make a function>` to ``functions.py``

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 5-6

    def w_positional_arguments(first_input, last_input):
        return first_input, last_input


    def w_keyword_arguments():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: w_keyword_arguments() got
               an unexpected keyword argument 'first_input'

  because the :ref:`definition<how to make a function>` for ``w_keyword_arguments`` does not allow inputs and the test uses two in the call (``first_input`` and ``last_input``)

* I add the name of the unexpected argument_ in parentheses

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 1-2

    # def w_keyword_arguments():
    def w_keyword_arguments(first_input):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: w_keyword_arguments() got
               an unexpected keyword argument 'last_input'.
               Did you mean 'first_input'?

  because the :ref:`definition<how to make a function>` for ``w_keyword_arguments`` allows one input (``first_input``) and the test uses two in the call (``first_input`` and ``last_input``)

* I add a name for the second argument_ in parentheses

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 2-3

    # def w_keyword_arguments():
    # def w_keyword_arguments(first_input):
    def w_keyword_arguments(first_input, second_input):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: none

    TypeError: w_keyword_arguments() got
               an unexpected keyword argument 'last_input'.
               Did you mean 'first_input'?

  because the :ref:`definition<how to make a function>` for ``w_keyword_arguments`` allows two inputs with the names ``first_input`` and ``second_input``, and the test calls the :ref:`function<what is a function?>` with ``first_input`` and ``last_input``, the names must match when I am using :ref:`keyword arguments<test_functions_w_keyword_arguments>`

* I change the name of the second argument to match the name used in the call

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 3-4
    :emphasize-text: last

    # def w_keyword_arguments():
    # def w_keyword_arguments(first_input):
    # def w_keyword_arguments(first_input, second_input):
    def w_keyword_arguments(first_input, last_input):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None != ('first', 'last')

  because the :ref:`function<what is a function?>` returns :ref:`None<what is None?>` and the :ref:`assertion<what is an assertion?>` expects ``('first', 'last')``

* I change the `return statement`_ to make the :ref:`function<what is a function?>` return its inputs

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 5-6

    # def w_keyword_arguments():
    # def w_keyword_arguments(first_input):
    # def w_keyword_arguments(first_input, second_input):
    def w_keyword_arguments(first_input, last_input):
        # return None
        return first_input, last_input

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 26

    def w_positional_arguments(first_input, last_input):
        return first_input, last_input


    def w_keyword_arguments(first_input, last_input):
        return first_input, last_input

* I add another :ref:`assertion<what is an assertion?>` with the `keyword arguments`_ given out of order in :ref:`test_functions_w_keyword_arguments` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 163
    :emphasize-lines: 8-12

        def test_functions_w_keyword_arguments(self):
            reality = src.functions.w_keyword_arguments(
                first_input='first', last_input='last',
            )
            my_expectation = ('first', 'last')
            self.assertEqual(reality, my_expectation)

            reality = src.functions.w_keyword_arguments(
                last_input='last', first_input='first',
            )
            my_expectation = ('last', 'first')
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: Tuples differ: ('first', 'last')
                                != ('last', 'first')

  the order the :ref:`function<what is a function?>` returns the values stayed the same this time, because it always returns ``first_input, last_input``.

  Compare this call that uses :ref:`positional arguments<test_functions_w_positional_arguments>` and its result

  .. code-block:: python

    src.functions.w_positional_arguments('last', 'first')
    ('last', 'first')

  with this call that uses :ref:`keyword arguments<test_functions_w_keyword_arguments>` and its result

  .. code-block:: python

    src.functions.w_keyword_arguments(
        last_input='last', first_input='first',
    )
    ('first', 'last')

  in both cases the :ref:`function<what is a function?>` returns ``first_input, last_input``

* I change ``my_expectation`` to match ``reality``

  .. code-block:: python
    :lineno-start: 170
    :emphasize-lines: 4-5
    :emphasize-text: last

            reality = src.functions.w_keyword_arguments(
                last_input='last', first_input='first',
            )
            # my_expectation = ('last', 'first')
            my_expectation = ('first', 'last')
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes. The order does not matter when I use `keyword arguments`_.

* I add :ref:`variables<what is a variable?>` to use them to remove repetition of ``'first'`` and ``'last'`` from the test

  .. code-block:: python
    :lineno-start: 163
    :emphasize-lines: 2

        def test_functions_w_keyword_arguments(self):
            first, last = 'first', 'last'

            reality = src.functions.w_keyword_arguments(
                first_input='first', last_input='last',
            )
            my_expectation = ('first', 'last')
            self.assertEqual(reality, my_expectation)

* I use the new :ref:`variables<what is a variable?>` to remove repetition of ``'first'`` and ``'last'`` from the test

  .. code-block:: python
    :lineno-start: 163
    :emphasize-lines: 5-6, 8-9, 13-14, 17-18

        def test_functions_w_keyword_arguments(self):
            first, last = 'first', 'last'

            reality = src.functions.w_keyword_arguments(
                # first_input='first', last_input='last',
                first_input=first, last_input=last,
            )
            # my_expectation = ('first', 'last')
            my_expectation = (first, last)
            self.assertEqual(reality, my_expectation)

            reality = src.functions.w_keyword_arguments(
                # last_input='last', first_input='first',
                last_input=last, first_input=first,
            )
            # my_expectation = ('last', 'first')
            # my_expectation = ('first', 'last')
            my_expectation = (first, last)
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test is still green.

* I can still call the :ref:`function<what is a function?>` the same way I did in :ref:`test_functions_w_positional_arguments` (without using the names). I add an :ref:`assertion<what is an assertion?>` to show this

  .. code-block:: python
    :lineno-start: 174
    :emphasize-lines: 10-14

            reality = src.functions.w_keyword_arguments(
                # last_input='last', first_input='first',
                last_input=last, first_input=first,
            )
            # my_expectation = ('last', 'first')
            # my_expectation = ('first', 'last')
            my_expectation = (first, last)
            self.assertEqual(reality, my_expectation)

            reality = src.functions.w_keyword_arguments(
                last, first,
            )
            my_expectation = (first, last)
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: Tuples differ: ('last', 'first')
                                != ('first', 'last')

  because the :ref:`function<what is a function?>` uses the order (positions) when I do not use the names

* I change ``my_expectation`` to match ``reality``

  .. code-block:: python
    :lineno-start: 183
    :emphasize-lines: 4-5
    :emphasize-text: first

            reality = src.functions.w_keyword_arguments(
                last, first,
            )
            # my_expectation = (first, last)
            my_expectation = (last, first)
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 183
    :emphasize-lines: 8-13

            reality = src.functions.w_keyword_arguments(
                last, first,
            )
            # my_expectation = (first, last)
            my_expectation = (last, first)
            self.assertEqual(reality, my_expectation)

            zero, one = 0, 1
            reality = src.functions.w_keyword_arguments(
                last_input=zero, first_input=one,
            )
            my_expectation = (zero, one)
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Tuples differ: (1, 0) != (0, 1)

* I change ``my_expectation`` to match ``reality``

  .. code-block:: python
    :lineno-start: 190
    :emphasize-lines: 5-6

            zero, one = 0, 1
            reality = src.functions.w_keyword_arguments(
                last_input=zero, first_input=one,
            )
            # my_expectation = (zero, one)
            my_expectation = (one, zero)
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 190
    :emphasize-lines: 9-16

            zero, one = 0, 1
            reality = src.functions.w_keyword_arguments(
                last_input=zero, first_input=one,
            )
            # my_expectation = (zero, one)
            my_expectation = (one, zero)
            self.assertEqual(reality, my_expectation)

            a_set = {1, 2, 3, 'n'}
            a_dictionary = {'key': 'value'}
            reality = src.functions.w_keyword_arguments(
                first_input=a_dictionary,
                last_input=a_set,
            )
            my_expectation = (a_set, a_dictionary)
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Tuples differ:
            ({'key': 'value'}, {1, 2, 3, 'n'})
         != ({1, 2, 3, 'n'}, {'key': 'value'})

* I change ``reality`` to match ``my_expectation``

  .. code-block:: python
    :lineno-start: 198
    :emphasize-lines: 4-7

            a_set = {1, 2, 3, 'n'}
            a_dictionary = {'key': 'value'}
            reality = src.functions.w_keyword_arguments(
                # first_input=a_dictionary,
                # last_input=a_set,
                first_input=a_set,
                last_input=a_dictionary,
            )
            my_expectation = (a_set, a_dictionary)
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* ``w_keyword_arguments`` and ``w_positional_arguments`` are the same functions_, they always

  .. code-block:: python

        return first_input, last_input

  Their names are different

  .. code-block:: python
    :emphasize-text: positional keyword

    def w_positional_arguments(first_input, last_input):
    def w_keyword_arguments(first_input, last_input):

  The difference that matters in the tests is how I call the functions_

  - I have to give the input in order when I use :ref:`positional arguments<test_functions_w_positional_arguments>`

    .. code-block:: python
      :emphasize-text: first

      w_positional_arguments('first', 'last')
      return ('first', 'last')

    .. code-block:: python
      :emphasize-text: first

      w_positional_arguments('last', 'first')
      return ('last', 'first')

    .. code-block:: python
      :emphasize-text: first

      w_positional_arguments(0, 1)
      return (0, 1)

    .. code-block:: python
      :emphasize-text: first

      w_positional_arguments((1, 2, 3, 'n'), [1, 2, 3, 'n'])
      return ((1, 2, 3, 'n'), [1, 2, 3, 'n'])

    .. code-block:: python
      :emphasize-text: first

      w_keyword_arguments('last', 'first')
      return ('last', 'first')

  - I can give the input in any order when I use `keyword arguments`_ because I use the names from the :ref:`function definition<how to make a function>` when I call it

    .. code-block:: python
      :emphasize-text: first

      w_keyword_arguments(
          first_input='first', last_input='last',
      )
      return ('first', 'last')

    .. code-block:: python
      :emphasize-text: first

      w_keyword_arguments(
          last_input='last', first_input='first',
      )
      return ('first', 'last')

    .. code-block:: python
      :emphasize-text: first

      w_keyword_arguments(last_input=0, first_input=1,)
      return (1, 0)

    .. code-block:: python
      :emphasize-text: first

      w_keyword_arguments(
          first_input={'key': 'value'},
          last_input={1, 2, 3, 'n'},
      )
      return ({'key': 'value'}, {1, 2, 3, 'n'})

  I add another :ref:`assertion<what is an assertion?>` to show that the two :ref:`functions<what is a function?>` are the same, by calling the ``w_positional_arguments`` :ref:`function<what is a function?>` with :ref:`keyword arguments<test_functions_w_keyword_arguments>`

  .. code-block:: python
    :lineno-start: 198
    :emphasize-lines: 12-20
    :emphasize-text: positional

            a_set = {1, 2, 3, 'n'}
            a_dictionary = {'key': 'value'}
            reality = src.functions.w_keyword_arguments(
                # first_input=a_dictionary,
                # last_input=a_set,
                first_input=a_set,
                last_input=a_dictionary,
            )
            my_expectation = (a_set, a_dictionary)
            self.assertEqual(reality, my_expectation)

            a_tuple = (1, 2, 3, 'n')
            a_list = [1, 2, 3, 'n']
            reality = src.functions.w_positional_arguments(
                first_input=a_tuple,
                last_input=a_list,
            )
            my_expectation = (a_list, a_tuple)
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Tuples differ:
            ((1, 2, 3, 'n'), [1, 2, 3, 'n'])
         != ([1, 2, 3, 'n'], (1, 2, 3, 'n'))

  because these two calls are the same

  .. code-block:: python

    src.functions.w_positional_arguments(
        first_input=a_tuple,
        last_input=a_list,
    )
    src.functions.w_positional_arguments(
        a_tuple,
        a_list,
    )

* I change ``reality`` to match my ``expectation``

  .. code-block:: python
    :lineno-start: 209
    :emphasize-lines: 4-7

            a_tuple = (1, 2, 3, 'n')
            a_list = [1, 2, 3, 'n']
            reality = src.functions.w_positional_arguments(
                # first_input=a_tuple,
                # last_input=a_list,
                first_input=a_list,
                last_input=a_tuple,
            )
            my_expectation = (a_list, a_tuple)
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 163

        def test_functions_w_keyword_arguments(self):
            first, last = 'first', 'last'

            reality = src.functions.w_keyword_arguments(
                first_input=first, last_input=last,
            )
            my_expectation = (first, last)
            self.assertEqual(reality, my_expectation)

            reality = src.functions.w_keyword_arguments(
                last_input=last, first_input=first,
            )
            my_expectation = (first, last)
            self.assertEqual(reality, my_expectation)

            reality = src.functions.w_keyword_arguments(
                last, first,
            )
            my_expectation = (last, first)
            self.assertEqual(reality, my_expectation)

            zero, one = 0, 1
            reality = src.functions.w_keyword_arguments(
                last_input=zero, first_input=one,
            )
            my_expectation = (one, zero)
            self.assertEqual(reality, my_expectation)

            a_set = {1, 2, 3, 'n'}
            a_dictionary = {'key': 'value'}
            reality = src.functions.w_keyword_arguments(
                first_input=a_set,
                last_input=a_dictionary,
            )
            my_expectation = (a_set, a_dictionary)
            self.assertEqual(reality, my_expectation)

            a_tuple = (1, 2, 3, 'n')
            a_list = [1, 2, 3, 'n']
            reality = src.functions.w_positional_arguments(
                first_input=a_list,
                last_input=a_tuple,
            )
            my_expectation = (a_list, a_tuple)
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_functions_w_keyword_arguments'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can call a function with keyword arguments<test_functions_w_keyword_arguments>`

----

*********************************************************************************
test_functions_w_positional_and_keyword_args
*********************************************************************************

I can write functions_ that take both :ref:`positional<test_functions_w_positional_arguments>` and :ref:`keyword arguments<test_functions_w_keyword_arguments>`, which is useful when I want some arguments to be required and some to be optional.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a failing test to ``test_functions.py``

  .. code-block:: python
    :lineno-start: 152
    :emphasize-lines: 9-16
    :emphasize-text: first

            a_tuple, a_list = (1, 2, 3, 'n'), [1, 2, 3, 'n']
            reality = src.functions.w_positional_arguments(
                first_input=a_list,
                last_input=a_tuple,
            )
            my_expectation = (a_list, a_tuple)
            self.assertEqual(reality, my_expectation)

        def test_functions_w_positional_and_keyword_args(self):
            reality = (
                src.functions.w_positional_and_keyword_args(
                    last_input='last', 'first',
                )
            )
            my_expectation = ('first', 'last')
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: shell

    SyntaxError: positional argument follows keyword argument

  because I cannot put :ref:`keyword arguments<test_functions_w_keyword_arguments>` before :ref:`positional arguments<test_functions_w_positional_arguments>`. The `Integrated Development Environment (IDE)`_ also shows the error with a red squiggly line under ``'first'``.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add SyntaxError_ to the list of :ref:`Exceptions<errors>` seen, in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 170
    :emphasize-lines: 6
    :emphasize-text: SyntaxError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # SyntaxError

* I change the order of the arguments to follow Python_ rules

  .. code-block:: python
    :lineno-start: 143
    :emphasize-lines: 4
    :emphasize-text: first

        def test_functions_w_positional_and_keyword_args(self):
            reality = (
                src.functions.w_positional_and_keyword_args(
                    'first', last_input='last',
                )
            )
            my_expectation = ('first', 'last')
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.functions'
                    has no attribute 'w_positional_and_keyword_args'

  because ``functions.py`` does not have anything named ``w_positional_and_keyword_args``

* I add a :ref:`function<what is a function?>` to ``functions.py``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 5-6

    def w_keyword_arguments(first_input, last_input):
        return first_input, last_input


    def w_positional_and_keyword_args():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: w_positional_and_keyword_args() got
               an unexpected keyword argument 'last_input'

  because the :ref:`definition<how to make a function>` for ``w_positional_and_keyword_args`` does not allow inputs and the test called the :ref:`function<what is a function?>` with a :ref:`keyword argument<test_functions_w_keyword_arguments>` (``last_input``)

* I add the name to the :ref:`function definition<how to make a function>` in parentheses, in ``functions.py``

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 1
    :emphasize-text: last_input

    def w_positional_and_keyword_args(last_input):
        return None

  the terminal_ is my friend, and shows

  .. code-block:: shell

    TypeError: w_positional_and_keyword_args() got
               multiple values for argument 'last_input'

  because the :ref:`definition<how to make a function>` for ``w_positional_and_keyword_args`` takes one argument, and the test calls the :ref:`function<what is a function?>` with two arguments ``('first', last_input='last')``. How does Python_ know which value to use for ``last_input`` if I use the :ref:`position<test_functions_w_positional_arguments>` and the :ref:`keyword<test_functions_w_keyword_arguments>`?

* I add another name in parentheses to make it clearer

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 1
    :emphasize-text: first_input

    def w_positional_and_keyword_args(last_input, first_input):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: w_positional_and_keyword_args() got
               multiple values for argument 'last_input'

  because I have not fixed the problem, I gave confusing values in the call. Python_ still cannot tell the difference between the two values because I gave a positional value which according to the :ref:`function definition<how to make a function>` is ``last_input`` and I gave a value with the name ``last_input``.

* How does it know what value to use for ``last_input``? The call tells it that the values for ``last_input`` are both ``'first'`` and ``'last'``, it would be like defining the :ref:`function<what is a function?>` with the same name twice

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 1

    def w_positional_and_keyword_args(last_input, last_input):
        return None

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: duplicate argument 'last_input'
                 in function definition

* I change the order of the names in parentheses

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 1
    :emphasize-text: first_input

    def w_positional_and_keyword_args(first_input, last_input):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None != ('first', 'last')

  because the :ref:`function<what is a function?>` returns :ref:`None<what is None?>` and the :ref:`assertion<what is an assertion?>` expects ``('first', 'last')``

* I change the `return statement`_ to give the test what it wants

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 4

    def w_positional_and_keyword_args(first_input, last_input):
        return first_input, last_input

  the test passes.

* I add :ref:`variables<what is a variable?>` to use them to remove the repetition of ``'first'`` and ``'last'`` in :ref:`test_functions_w_positional_and_keyword_args` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 160
    :emphasize-lines: 2

        def test_functions_w_positional_and_keyword_args(self):
            first, last = 'first', 'last'
            reality = (
                src.functions.w_positional_and_keyword_args(
                    'first', last_input='last',
                )
            )
            my_expectation = ('first', 'last')
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

* I use the new :ref:`variables<what is a variable?>` to remove repetition of ``'first'`` and ``'last'``

  .. code-block:: python
    :lineno-start: 160
    :emphasize-lines: 5-6, 9-10

        def test_functions_w_positional_and_keyword_args(self):
            first, last = 'first', 'last'
            reality = (
                src.functions.w_positional_and_keyword_args(
                    # 'first', last_input='last',
                    first, last_input=last,
                )
            )
            # my_expectation = ('first', 'last')
            my_expectation = (first, last)
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 160

        def test_functions_w_positional_and_keyword_args(self):
            first, last = 'first', 'last'
            reality = (
                src.functions.w_positional_and_keyword_args(
                    first, last_input=last,
                )
            )
            my_expectation = (first, last)
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_functions_w_positional_and_keyword_args'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can call a function with positional and keyword arguments<test_functions_w_positional_and_keyword_args>`

----

*********************************************************************************
test_functions_w_optional_arguments
*********************************************************************************

I can use :ref:`positional<test_functions_w_positional_arguments>` and :ref:`keyword arguments<test_functions_w_keyword_arguments>` when I want some arguments to be required and some to be optional.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a failing test to ``test_functions.py``

  .. code-block:: python
    :lineno-start: 160
    :emphasize-lines: 11-17

        def test_functions_w_positional_and_keyword_args(self):
            first, last = 'first', 'last'
            reality = (
                src.functions.w_positional_and_keyword_args(
                    first, last_input=last,
                )
            )
            my_expectation = (first, last)
            self.assertEqual(reality, my_expectation)

        def test_functions_w_optional_arguments(self):
            first_name, last_name = 'jane', 'doe'
            reality = src.functions.w_optional_arguments(
                first_name, last_input=last_name,
            )
            my_expectation = (first_name, last_name)
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.functions'
                    has no attribute 'w_optional_arguments'.
                    Did you mean: 'w_positional_arguments'?

  because ``functions.py`` does not have a definition for ``w_optional_arguments``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a :ref:`function<what is a function?>` named ``w_optional_arguments`` to ``functions.py``

.. code-block:: python
  :lineno-start: 34
  :emphasize-lines: 5-6

    def w_positional_and_keyword_args(first_input, last_input):
        return first_input, last_input


    def w_optional_arguments(first_input, last_input):
        return first_input, last_input

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove ``last_input=last_name`` from the call to ``w_optional_arguments`` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 170
    :emphasize-lines: 4

        def test_functions_w_optional_arguments(self):
            first_name, last_name = 'jane', 'doe'
            reality = src.functions.w_optional_arguments(
                first_name,
            )
            my_expectation = (first_name, last_name)
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: w_optional_arguments()
               missing 1 required positional argument: 'last_input'

  because the ``last_input`` argument MUST be given when this :ref:`function<what is a function?>` is called, it is required.

* I make the argument optional by giving it a default value in ``functions.py``

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 1

    def w_optional_arguments(first_input, last_input='doe'):
        return first_input, last_input

  the test passes since I do not need to give a value for the ``last_input`` parameter in the call to ``src.functions.w_optional_arguments`` because the :ref:`default value<test_functions_w_optional_arguments>` for the ``last_input`` parameter of the :ref:`function<what is a function?>` is ``doe``. This means that

  .. code-block:: python

    src.functions.w_optional_arguments('jane')

  is the same as

  .. code-block:: python

    src.functions.w_optional_arguments('jane', last_input='doe')

  is the same as

  .. code-block:: python

    return 'jane', 'doe'

  because ``w_optional_arguments`` will always

  .. code-block:: python

    return first_input, last_input

  :ref:`A function uses the default value for a parameter when it is called without the parameter<test_functions_w_optional_arguments>`.

* I add another :ref:`assertion<what is an assertion?>` to ``test_functions.py`` to show that I can still call the :ref:`function<what is a function?>` with different values

  .. code-block:: python
    :lineno-start: 170
    :emphasize-lines: 9-14

        def test_functions_w_optional_arguments(self):
            first_name, last_name = 'jane', 'doe'
            reality = src.functions.w_optional_arguments(
                first_name,
            )
            my_expectation = (first_name, last_name)
            self.assertEqual(reality, my_expectation)

            first_name, blow = 'joe', 'blow'
            reality = src.functions.w_optional_arguments(
                first_name, blow,
            )
            my_expectation = ()
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: Tuples differ: ('joe', 'blow') != ()

* I change ``my_expectation`` to match ``reality``

  .. code-block:: python
    :lineno-start: 178
    :emphasize-lines: 5

            first_name, blow = 'joe', 'blow'
            reality = src.functions.w_optional_arguments(
                first_name, blow,
            )
            my_expectation = (first_name, blow)
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 178
    :emphasize-lines: 8-13

            first_name, blow = 'joe', 'blow'
            reality = src.functions.w_optional_arguments(
                first_name, blow,
            )
            my_expectation = (first_name, blow)
            self.assertEqual(reality, my_expectation)

            first_name = 'john'
            reality = src.functions.w_optional_arguments(
                first_input=first_name
            )
            my_expectation = ()
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Tuples differ: ('john', 'doe') != ()

* I change ``my_expectation`` to match ``reality``

  .. code-block:: python
    :lineno-start: 185
    :emphasize-lines: 5

            first_name = 'john'
            reality = src.functions.w_optional_arguments(
                first_input=first_name
            )
            my_expectation = (first_name, last_name)
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes since I do not need to give a value for the ``last_input`` parameter in the call to ``src.functions.w_optional_arguments`` because the :ref:`default value<test_functions_w_optional_arguments>` for the ``last_input`` parameter of the ``w_optional_arguments`` :ref:`function<what is a function?>` is ``doe``. This means that

  .. code-block:: python

    src.functions.w_optional_arguments(first_input='john')

  is the same as

  .. code-block:: python

    src.functions.w_optional_arguments(
        first_input='john', last_input='doe',
    )

  is the same as

  .. code-block:: python

    return 'john', 'doe'

  because ``w_optional_arguments`` will always

  .. code-block:: python

    return first_input, last_input

  :ref:`A function uses the default value for a parameter when it is called without the parameter<test_functions_w_optional_arguments>`.

* I add one more :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 185
    :emphasize-lines: 8-13

            first_name = 'john'
            reality = src.functions.w_optional_arguments(
                first_input=first_name
            )
            my_expectation = (first_name, last_name)
            self.assertEqual(reality, my_expectation)

            last_name = 'smith'
            reality = src.functions.w_optional_arguments(
                last_input=last_name, first_input=first_name,
            )
            my_expectation = (last_name, first_name)
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Tuples differ: ('john', 'smith')
                                != ('smith', 'john')

* I change ``my_expectation`` to match ``reality``

  .. code-block:: python
    :lineno-start: 192
    :emphasize-lines: 5

            last_name = 'smith'
            reality = src.functions.w_optional_arguments(
                last_input=last_name, first_input=first_name,
            )
            my_expectation = (first_name, last_name)
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_functions_w_optional_arguments'

  the terminal_ shows a summary of the changes then goes back to the command line.

.. note::

  these four :ref:`functions<what is a function?>`

  * ``w_keyword_arguments``
  * ``w_positional_arguments``
  * ``w_positional_and_keyword_args``
  * ``w_optional_arguments``

  are the same, they always ``return first_input, last_input``, their names are different.

  .. code-block:: python
    :emphasize-text: positional keyword default

    def w_positional_arguments(first_input, last_input):
    def w_keyword_arguments(first_input, last_input):
    def w_positional_and_keyword_args(first_input, last_input):
    def w_optional_arguments(first_input, last_input='doe'):

  ``first_input`` and ``last_input`` are also names (:ref:`variables<what is a variable?>`), they can be any names. The difference that matters in the tests is how I call the functions_

  .. code-block:: python
    :emphasize-text: last

    w_positional_arguments('first', 'last')
    return 'first', 'last'

  .. code-block:: python
    :emphasize-text: last

    w_positional_arguments('last', 'first')
    return 'last', 'first'

  .. code-block:: python
    :emphasize-text: last

    w_positional_arguments(
        first_input=[1, 2, 3, 'n'], last_input=(1, 2, 3, 'n')
    )
    return [1, 2, 3, 'n'], (1, 2, 3, 'n')

  .. code-block:: python
    :emphasize-text: last

    w_keyword_arguments(first_input='first', last_input='last')
    return 'first', 'last'

  .. code-block:: python
    :emphasize-text: last

    w_keyword_arguments(last_input='last', first_input='first')
    return 'first', 'last'

  .. code-block:: python
    :emphasize-text: last

    w_keyword_arguments('last', 'first')
    return 'last', 'first'

  .. code-block:: python
    :emphasize-text: last

    w_positional_and_keyword_args('first', last_input='last')
    return 'first', 'last'

  .. code-block:: python
    :emphasize-text: last

    w_optional_arguments('jane', last_input='doe')
    return 'jane', 'doe'

  .. code-block:: python
    :emphasize-text: last

    w_optional_arguments('jane')
    return 'jane', 'doe'

  .. code-block:: python
    :emphasize-text: last

    w_optional_arguments('joe', 'blow')
    return 'joe', 'blow'

  .. code-block:: python
    :emphasize-text: last

    w_optional_arguments(first_input='john', last_input='smith')
    return 'john', 'smith'

.. tip::

  as a rule of thumb I use :ref:`keyword arguments<test_functions_w_keyword_arguments>` when I have 2 or more inputs so I do not have to remember the order

----

*********************************************************************************
test_functions_w_unknown_arguments
*********************************************************************************

I can make functions_ that take any number of :ref:`positional<test_functions_w_positional_arguments>` and :ref:`keyword<test_functions_w_keyword_arguments>` arguments. This means I do not need to know how many inputs the :ref:`function<what is a function?>` should take when it is called.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a new test to ``test_functions.py``

  .. code-block:: python
    :lineno-start: 192
    :emphasize-lines: 8-13

            last_name = 'smith'
            reality = src.functions.w_optional_arguments(
                last_input=last_name, first_input=first_name,
            )
            my_expectation = (first_name, last_name)
            self.assertEqual(reality, my_expectation)

        def test_functions_w_unknown_arguments(self):
            reality = src.functions.w_unknown_arguments(
                0, 1, a=2, b=3,
            )
            my_expectation = None
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.functions'
                    has no attribute 'w_unknown_arguments'.
                    Did you mean: 'w_keyword_arguments'?

  because ``functions.py`` does not have ``w_unknown_arguments``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`function<what is a function?>` to ``functions.py``

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 5-6

    def w_optional_arguments(first_input, last_input='doe'):
        return first_input, last_input


    def w_unknown_arguments():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: w_unknown_arguments() got
               an unexpected keyword argument 'a'

* I add the name to the :ref:`function definition<how to make a function>`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 1

    def w_unknown_arguments(a):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: w_unknown_arguments() got
               multiple values for argument 'a'

  I had this same problem in :ref:`test_functions_w_positional_and_keyword_args`. Python_ cannot tell if ``a`` is a :ref:`positional<test_functions_w_positional_arguments>` or :ref:`keyword argument<test_functions_w_keyword_arguments>` based on my :ref:`function definition<how to make a function>`

----

=================================================================================
double starred expressions
=================================================================================

----

* Python_ has a way for a :ref:`function<what is a function?>` to take any number of :ref:`keyword arguments<test_functions_w_keyword_arguments>` without knowing how many they are. I use it to replace ``a`` in the parentheses

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 1

    def w_unknown_arguments(**kwargs):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: w_unknown_arguments() takes 0 positional arguments
               but 2 were given

* I add a name for the first :ref:`positional argument<test_functions_w_positional_arguments>`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 1
    :emphasize-text: x

    def w_unknown_arguments(**kwargs, x):
        return None

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: shell

    SyntaxError: arguments cannot follow var-keyword argument

  a reminder that I cannot put :ref:`positional arguments<test_functions_w_positional_arguments>` after :ref:`keyword arguments<test_functions_w_keyword_arguments>`

* I change the order of the inputs in ``w_unknown_arguments`` in ``functions.py``

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 1
    :emphasize-text: x

    def w_unknown_arguments(x, **kwargs):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: w_unknown_arguments() takes 1 positional argument
               but 4 were given

* I add a name for the other :ref:`positional argument<test_functions_w_positional_arguments>`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 1

    def w_unknown_arguments(x, y, **kwargs):
        return None

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` to see what happens if I call the :ref:`function<what is a function?>` with 3 :ref:`keyword arguments<test_functions_w_keyword_arguments>`

  .. code-block:: python
    :lineno-start: 199
    :emphasize-lines: 8-12

        def test_functions_w_unknown_arguments(self):
            reality = src.functions.w_unknown_arguments(
                0, 1, a=2, b=3,
            )
            my_expectation = None
            self.assertEqual(reality, my_expectation)

            reality = src.functions.w_unknown_arguments(
                0, 1, a=2, b=3, c=4,
            )
            my_expectation = ()
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != ()

* I change ``my_expectation`` to match ``reality``

  .. code-block:: python
    :lineno-start: 206
    :emphasize-lines: 4

            reality = src.functions.w_unknown_arguments(
                0, 1, a=2, b=3, c=4,
            )
            my_expectation = None
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes because the :ref:`function<what is a function?>` can take any number of :ref:`keyword arguments<test_functions_w_keyword_arguments>` without knowing how many are in the call.

* I add an :ref:`assertion<what is an assertion?>` to see what happens when I call the :ref:`function<what is a function?>` with 3 :ref:`positional arguments<test_functions_w_positional_arguments>`

  .. code-block:: python
    :lineno-start: 206
    :emphasize-lines: 7-11

            reality = src.functions.w_unknown_arguments(
                0, 1, a=2, b=3, c=4,
            )
            my_expectation = None
            self.assertEqual(reality, my_expectation)

            reality = src.functions.w_unknown_arguments(
                0, 1, 2, a=3, b=4, c=5,
            )
            my_expectation = None
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: w_unknown_arguments() takes 2 positional arguments
               but 3 were given

  the :ref:`function definition<how to make a function>` only allows two :ref:`positional arguments<test_functions_w_positional_arguments>`

* I change the definition of the ``w_unknown_arguments`` :ref:`function<what is a function?>` to make it take three :ref:`positional arguments<test_functions_w_positional_arguments>`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 1

    def w_unknown_arguments(x, y, z, **kwargs):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: w_unknown_arguments() missing
               1 required positional argument: 'z'

  because the previous :ref:`assertion<what is an assertion?>` calls the :ref:`function<what is a function?>` with two :ref:`positional arguments<test_functions_w_positional_arguments>` and it now requires three

----

=================================================================================
starred expressions
=================================================================================

----

* Python_ also has a way to handle any number of :ref:`positional arguments<test_functions_w_positional_arguments>`. I use it

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 1

    def w_unknown_arguments(*args, **kwargs):
        return None

  the test passes.

* ``*args, **kwargs`` is :ref:`Python convention<conventions>`. I change the names to make it clearer

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 1-3

    def w_unknown_arguments(
            *positional_arguments, **keyword_arguments
        ):
        return None

  the test is still green.

* I change the `return statement`_ because I want the :ref:`function<what is a function?>` to return its input (remember the :ref:`identity function<test_identity_function>`?)

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 4

    def w_unknown_arguments(
            *positional_arguments, **keyword_arguments
        ):
        return positional_arguments, keyword_arguments

  the terminal_ is my friend, and shows

  .. code-block:: shell

    AssertionError: ((0, 1), {'a': 2, 'b': 3}) != None

  I get a tuple_ that has another tuple_ and a :ref:`dictionary<what is a dictionary?>`

* I change ``my_expectation`` to match ``reality`` in the first :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 199
    :emphasize-lines: 5

        def test_functions_w_unknown_arguments(self):
            reality = src.functions.w_unknown_arguments(
                0, 1, a=2, b=3,
            )
            my_expectation = ((0, 1), {'a': 2, 'b': 3})
            self.assertEqual(reality, my_expectation)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: ((0, 1), {'a': 2, 'b': 3, 'c': 4}) != None

* I change ``my_expectation`` to match ``reality`` in the second :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 199
    :emphasize-lines: 11-13

        def test_functions_w_unknown_arguments(self):
            reality = src.functions.w_unknown_arguments(
                0, 1, a=2, b=3,
            )
            my_expectation = ((0, 1), {'a': 2, 'b': 3})
            self.assertEqual(reality, my_expectation)

            reality = src.functions.w_unknown_arguments(
                0, 1, a=2, b=3, c=4,
            )
            my_expectation = (
                (0, 1), {'a': 2, 'b': 3, 'c': 4}
            )
            self.assertEqual(reality, my_expectation)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: ((0, 1, 2), {'a': 3, 'b': 4, 'c': 5}) != None

* I change ``my_expectation`` to match ``reality`` in the last :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 199
    :emphasize-lines: 19-21

        def test_functions_w_unknown_arguments(self):
            reality = src.functions.w_unknown_arguments(
                0, 1, a=2, b=3,
            )
            my_expectation = ((0, 1), {'a': 2, 'b': 3})
            self.assertEqual(reality, my_expectation)

            reality = src.functions.w_unknown_arguments(
                0, 1, a=2, b=3, c=4,
            )
            my_expectation = (
                (0, 1), {'a': 2, 'b': 3, 'c': 4}
            )
            self.assertEqual(reality, my_expectation)

            reality = src.functions.w_unknown_arguments(
                0, 1, 2, a=3, b=4, c=5,
            )
            my_expectation = (
                (0, 1, 2), {'a': 3, 'b': 4, 'c': 5}
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* I add :ref:`variables<what is a variable?>` to use them to remove repetition of the tuple_ and :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 199
    :emphasize-lines: 2

        def test_functions_w_unknown_arguments(self):
            a_tuple, a_dictionary = (0, 1), {'a': 2, 'b': 3}
            reality = src.functions.w_unknown_arguments(
                0, 1, a=2, b=3,
            )
            my_expectation = ((0, 1), {'a': 2, 'b': 3})
            self.assertEqual(reality, my_expectation)

* I use the :ref:`variables<what is a variable?>` to remove repetition of the values

  .. code-block:: python
    :lineno-start: 199
    :emphasize-lines: 4-5, 7-8

        def test_functions_w_unknown_arguments(self):
            a_tuple, a_dictionary = (0, 1), {'a': 2, 'b': 3}
            reality = src.functions.w_unknown_arguments(
                # 0, 1, a=2, b=3,
                a_tuple, a_dictionary
            )
            # my_expectation = ((0, 1), {'a': 2, 'b': 3})
            my_expectation = (a_tuple, a_dictionary)
            self.assertEqual(reality, my_expectation)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Tuples differ: (((0, 1), {'a': 2, 'b': 3}), {})
                                != ((0, 1), {'a': 2, 'b': 3})

  because passing in the values this way means I am sending in two :ref:`positional arguments<test_functions_w_positional_arguments>`

* I change the inputs with ``*`` and ``**`` so that Python_ breaks up the contents, allowing them to be used as separate arguments

  .. code-block:: python
    :lineno-start: 199
    :emphasize-lines: 5

        def test_functions_w_unknown_arguments(self):
            a_tuple, a_dictionary = (0, 1), {'a':'2', 'b':'3'}
            reality = src.functions.w_unknown_arguments(
                # 0, 1, a=2, b=3,
                *a_tuple, **a_dictionary
            )
            # my_expectation = ((0, 1), {'a': 2, 'b': 3})
            my_expectation = (a_tuple, a_dictionary)
            self.assertEqual(reality, my_expectation)

  the test passes.

* I add :ref:`variables<what is a variable?>` to the next :ref:`assertion<what is an assertion?>` to use them to remove repetition of the tuple_ and :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 199
    :emphasize-lines: 11-12

        def test_functions_w_unknown_arguments(self):
            a_tuple, a_dictionary = (0, 1), {'a': 2, 'b': 3}
            reality = src.functions.w_unknown_arguments(
                # 0, 1, a=2, b=3,
                *a_tuple, **a_dictionary
            )
            # my_expectation = ((0, 1), {'a': 2, 'b': 3})
            my_expectation = (a_tuple, a_dictionary)
            self.assertEqual(reality, my_expectation)

            a_tuple = (0, 1)
            a_dictionary = {'a': 2, 'b': 3, 'c': 4}
            reality = src.functions.w_unknown_arguments(
                0, 1, a=2, b=3, c=4,
            )
            my_expectation = (
                (0, 1), {'a': 2, 'b': 3, 'c': 4}
            )
            self.assertEqual(reality, my_expectation)

* I use the :ref:`variables<what is a variable?>` to remove repetition of the tuple_ and :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 199
    :emphasize-lines: 14-15, 18-19

        def test_functions_w_unknown_arguments(self):
            a_tuple, a_dictionary = (0, 1), {'a': 2, 'b': 3}
            reality = src.functions.w_unknown_arguments(
                # 0, 1, a=2, b=3,
                *a_tuple, **a_dictionary
            )
            # my_expectation = ((0, 1), {'a': 2, 'b': 3})
            my_expectation = (a_tuple, a_dictionary)
            self.assertEqual(reality, my_expectation)

            a_tuple = (0, 1)
            a_dictionary = {'a': 2, 'b': 3, 'c': 4}
            reality = src.functions.w_unknown_arguments(
                # 0, 1, a=2, b=3, c=4,
                a_tuple, a_dictionary
            )
            my_expectation = (
                # (0, 1), {'a': 2, 'b': 3, 'c': 4}
                a_tuple, a_dictionary
            )
            self.assertEqual(reality, my_expectation)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Tuples differ: (((0, 1), {'a': 2, 'b': 3, 'c': 4}), {})
                                != ((0, 1), {'a': 2, 'b': 3, 'c': 4})

  because passing in the values this way means I am sending in two :ref:`positional arguments<test_functions_w_positional_arguments>`

* I change the inputs with ``*`` and ``**`` so that Python_ breaks up the contents, allowing them to be used as separate arguments

  .. code-block:: python
    :lineno-start: 199
    :emphasize-lines: 15

        def test_functions_w_unknown_arguments(self):
            a_tuple, a_dictionary = (0, 1), {'a': 2, 'b': 3}
            reality = src.functions.w_unknown_arguments(
                # 0, 1, a=2, b=3,
                *a_tuple, **a_dictionary
            )
            # my_expectation = ((0, 1), {'a': 2, 'b': 3})
            my_expectation = (a_tuple, a_dictionary)
            self.assertEqual(reality, my_expectation)

            a_tuple = (0, 1)
            a_dictionary = {'a': 2, 'b': 3, 'c': 4}
            reality = src.functions.w_unknown_arguments(
                # 0, 1, a=2, b=3, c=4,
                *a_tuple, **a_dictionary
            )
            my_expectation = (
                # (0, 1), {'a': 2, 'b': 3, 'c': 4}
                a_tuple, a_dictionary
            )
            self.assertEqual(reality, my_expectation)

  the test passes.

* I add :ref:`variables<what is a variable?>` to the third :ref:`assertion<what is an assertion?>` to use them to remove repetition of the tuple_ and :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 199
    :emphasize-lines: 23-24

        def test_functions_w_unknown_arguments(self):
            a_tuple, a_dictionary = (0, 1), {'a': 2, 'b': 3}
            reality = src.functions.w_unknown_arguments(
                # 0, 1, a=2, b=3,
                *a_tuple, **a_dictionary
            )
            # my_expectation = ((0, 1), {'a': 2, 'b': 3})
            my_expectation = (a_tuple, a_dictionary)
            self.assertEqual(reality, my_expectation)

            a_tuple = (0, 1)
            a_dictionary = {'a': 2, 'b': 3, 'c': 4}
            reality = src.functions.w_unknown_arguments(
                # 0, 1, a=2, b=3, c=4,
                *a_tuple, **a_dictionary
            )
            my_expectation = (
                # (0, 1), {'a': 2, 'b': 3, 'c': 4}
                a_tuple, a_dictionary
            )
            self.assertEqual(reality, my_expectation)

            a_tuple = (0, 1, 2)
            a_dictionary = {'a': 3, 'b': 4, 'c': 5}
            reality = src.functions.w_unknown_arguments(
                0, 1, 2, a=3, b=4, c=5,
            )
            my_expectation = (
                (0, 1, 2), {'a': 3, 'b': 4, 'c': 5}
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

* I use the :ref:`variables<what is a variable?>` to remove repetition of the tuple_ and :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 221
    :emphasize-lines: 4-5, 8-9

            a_tuple = (0, 1, 2)
            a_dictionary = {'a': 3, 'b': 4, 'c': 5}
            reality = src.functions.w_unknown_arguments(
                # 0, 1, 2, a=3, b=4, c=5,
                a_tuple, a_dictionary
            )
            my_expectation = (
                # (0, 1, 2), {'a': 3, 'b': 4, 'c': 5}
                a_tuple, a_dictionary
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Tuples differ: (((0, 1, 2), {'a': 3, 'b': 4, 'c': 5}), {})
                                != ((0, 1, 2), {'a': 3, 'b': 4, 'c': 5})

  because passing in the values this way means I am sending in two :ref:`positional arguments<test_functions_w_positional_arguments>`

* I change the inputs with ``*`` and ``**`` so that Python_ breaks up the contents, allowing them to be used as separate arguments

  .. code-block:: python
    :lineno-start: 221
    :emphasize-lines: 5

            a_tuple = (0, 1, 2)
            a_dictionary = {'a': 3, 'b': 4, 'c': 5}
            reality = src.functions.w_unknown_arguments(
                # 0, 1, 2, a=3, b=4, c=5,
                *a_tuple, **a_dictionary
            )
            my_expectation = (
                # (0, 1, 2), {'a': 3, 'b': 4, 'c': 5}
                a_tuple, a_dictionary
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 199

        def test_functions_w_unknown_arguments(self):
            a_tuple, a_dictionary = (0, 1), {'a': 2, 'b': 3}
            reality = src.functions.w_unknown_arguments(
                *a_tuple, **a_dictionary
            )
            my_expectation = (a_tuple, a_dictionary)
            self.assertEqual(reality, my_expectation)

            a_tuple = (0, 1)
            a_dictionary = {'a': 2, 'b': 3, 'c': 4}
            reality = src.functions.w_unknown_arguments(
                *a_tuple, **a_dictionary
            )
            my_expectation = (
                a_tuple, a_dictionary
            )
            self.assertEqual(reality, my_expectation)

            a_tuple = (0, 1, 2)
            a_dictionary = {'a': 3, 'b': 4, 'c': 5}
            reality = src.functions.w_unknown_arguments(
                *a_tuple, **a_dictionary
            )
            my_expectation = (
                a_tuple, a_dictionary
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

----

*********************************************************************************
how Python reads positional arguments
*********************************************************************************

I add an :ref:`assertion<what is an assertion?>` to see what happens when I call ``w_unknown_arguments`` with ONLY :ref:`positional arguments<test_functions_w_positional_arguments>`.

.. code-block:: python
  :lineno-start: 217
  :emphasize-lines: 11-14

            a_tuple = (0, 1, 2)
            a_dictionary = {'a': 3, 'b': 4, 'c': 5}
            reality = src.functions.w_unknown_arguments(
                *a_tuple, **a_dictionary
            )
            my_expectation = (
                a_tuple, a_dictionary
            )
            self.assertEqual(reality, my_expectation)

            a_tuple = (0, 1, 2, 3)
            reality = src.functions.w_unknown_arguments(*a_tuple)
            my_expectation = ()
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: Tuples differ: ((0, 1, 2, 3), {}) != ()

I change ``my_expectation`` to match ``reality``

.. code-block:: python
  :lineno-start: 227
  :emphasize-lines: 3

          a_tuple = (0, 1, 2, 3)
          reality = src.functions.w_unknown_arguments(*a_tuple)
          my_expectation = (a_tuple, {})
          self.assertEqual(reality, my_expectation)


  # Exceptions seen

the test passes. The :ref:`function<what is a function?>` gives me back the :ref:`positional arguments<test_functions_w_positional_arguments>` in a tuple_ (things in parentheses (``()``) separated by commas) and gives me an empty :ref:`dictionary<what is a dictionary?>` (any :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` in curly braces ``{ }`` separated by a comma) for the :ref:`keyword arguments<test_functions_w_keyword_arguments>` because I did not give any in the call.

----

*********************************************************************************
how Python reads keyword arguments
*********************************************************************************

I add another :ref:`assertion<what is an assertion?>` to see what happens when I call the :ref:`function<what is a function?>` with ONLY :ref:`keyword arguments<test_functions_w_keyword_arguments>`

.. code-block:: python
  :lineno-start: 227
  :emphasize-lines: 6-11

          a_tuple = (0, 1, 2, 3)
          reality = src.functions.w_unknown_arguments(*a_tuple)
          my_expectation = (a_tuple, {})
          self.assertEqual(reality, my_expectation)

          a_dictionary = {'a': 4, 'b': 5, 'c': 6, 'd': 7}
          reality = src.functions.w_unknown_arguments(
              **a_dictionary
          )
          my_expectation = ()
          self.assertEqual(reality, my_expectation)


  # Exceptions seen

the terminal_ is my friend, and shows

.. code-block:: python

  AssertionError: Tuples differ:
                  ((), {'a': 4, 'b': 5, 'c': 6, 'd': 7}) != ()

I change ``my_expectation`` to match ``reality``

.. code-block:: python
  :lineno-start: 232
  :emphasize-lines: 5

          a_dictionary = {'a': 4, 'b': 5, 'c': 6, 'd': 7}
          reality = src.functions.w_unknown_arguments(
              **a_dictionary
          )
          my_expectation = ((), a_dictionary)
          self.assertEqual(reality, my_expectation)


  # Exceptions seen

the test passes. The :ref:`function<what is a function?>` gives me back the :ref:`positional arguments<test_functions_w_positional_arguments>` as an empty tuple_ (things in parentheses (``()``) separated by commas) because I did not give any in the call, it gives me a :ref:`dictionary<what is a dictionary?>` (any :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` in curly braces ``{ }`` separated by a comma) of the :ref:`keyword arguments<test_functions_w_keyword_arguments>`.

----

*********************************************************************************
how Python reads positional and keyword arguments
*********************************************************************************

* I add one more :ref:`assertion<what is an assertion?>` to see what happens when I call the :ref:`function<what is a function?>` with no inputs

  .. code-block:: python
    :lineno-start: 232
    :emphasize-lines: 8-10

            a_dictionary = {'a': 4, 'b': 5, 'c': 6, 'd': 7}
            reality = src.functions.w_unknown_arguments(
                **a_dictionary
            )
            my_expectation = ((), a_dictionary)
            self.assertEqual(reality, my_expectation)

            reality = src.functions.w_unknown_arguments()
            my_expectation = TypeError
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: ((), {}) != <class 'TypeError'>

* I change the ``my_expectation`` to match ``reality``

  .. code-block:: python
    :lineno-start: 199
    :emphasize-lines: 42

        def test_functions_w_unknown_arguments(self):
            a_tuple, a_dictionary = (0, 1), {'a': 2, 'b': 3}
            reality = src.functions.w_unknown_arguments(
                *a_tuple, **a_dictionary
            )
            my_expectation = (a_tuple, a_dictionary)
            self.assertEqual(reality, my_expectation)

            a_tuple = (0, 1)
            a_dictionary = {'a': 2, 'b': 3, 'c': 4}
            reality = src.functions.w_unknown_arguments(
                *a_tuple, **a_dictionary
            )
            my_expectation = (
                a_tuple, a_dictionary
            )
            self.assertEqual(reality, my_expectation)

            a_tuple = (0, 1, 2)
            a_dictionary = {'a': 3, 'b': 4, 'c': 5}
            reality = src.functions.w_unknown_arguments(
                *a_tuple, **a_dictionary
            )
            my_expectation = (
                a_tuple, a_dictionary
            )
            self.assertEqual(reality, my_expectation)

            a_tuple = (0, 1, 2, 3)
            reality = src.functions.w_unknown_arguments(*a_tuple)
            my_expectation = (a_tuple, {})
            self.assertEqual(reality, my_expectation)

            a_dictionary = {'a': 4, 'b': 5, 'c': 6, 'd': 7}
            reality = src.functions.w_unknown_arguments(
                **a_dictionary
            )
            my_expectation = ((), a_dictionary)
            self.assertEqual(reality, my_expectation)

            reality = src.functions.w_unknown_arguments()
            my_expectation = ((), {})
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_functions_w_unknown_arguments'

  the terminal_ shows a summary of the changes then goes back to the command line.

.. note::

  these statements are the same

  .. code-block:: python

    w_unknown_arguments(0, 1, 2, 3, a=4, b=5, c=6, d=7)
    w_unknown_arguments(
        *(0, 1, 2, 3), **{'a': 4, 'b': 5, 'c': 6, 'd': 7}
    )

  because ``w_unknown_arguments`` in ``functions.py`` in the ``src`` folder will always

  .. code-block:: python

    return positional_arguments, keyword_arguments

  in this case

  .. code-block:: python

    0, 1, 2, 3
    *(0, 1, 2, 3)

  are :ref:`positional arguments<test_functions_w_positional_arguments>` which are taken as a tuple_ and

  .. code-block:: python

    a=4, b=5, c=6, d=7
    **{'a': 4, 'b': 5, 'c': 6, 'd': 7}

  are :ref:`keyword arguments<test_functions_w_keyword_arguments>` which are taken as a :ref:`dictionary<what is a dictionary?>`.

  The :ref:`function<what is a function?>` reads :ref:`positional arguments<test_functions_w_positional_arguments>` as tuples_, and :ref:`keyword arguments<test_functions_w_keyword_arguments>` as :ref:`dictionaries<what is a dictionary?>`.

  Is this why the :ref:`update method of dictionaries<test_update_a_dictionary>` can take a :ref:`dictionary<what is a dictionary?>` as input?

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_functions.py`` and ``functions.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_ where the tests are running, then use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``functions``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_

----

*********************************************************************************
review
*********************************************************************************

I ran tests to show that I can make functions_ with

* the def_ keyword
* :ref:`positional arguments<test_functions_w_positional_arguments>`
* :ref:`keyword arguments<test_functions_w_keyword_arguments>`
* :ref:`positional and keyword arguments<test_functions_w_positional_and_keyword_args>`
* :ref:`default values<test_functions_w_optional_arguments>`
* :ref:`can take any number of inputs<test_functions_w_unknown_arguments>`

as a reminder

* :ref:`I can use '*args' when I do not know how many positional arguments the function has to take<test_functions_w_unknown_arguments>`
* :ref:`positional arguments are taken as a tuple<how Python reads positional arguments>`
* :ref:`positional arguments must come before keyword arguments<test_functions_w_optional_arguments>`
* :ref:`I can use '**kwargs' when I do not know how many keyword arguments the function has to take<test_functions_w_unknown_arguments>`
* :ref:`keyword arguments are taken as a dictionary<how Python reads keyword arguments>`
* :ref:`the identity function returns its input<test_identity_function>`
* :ref:`constant functions always return the same thing<test_constant_function>`
* :ref:`nothing runs after the return statement in a function<test_what_happens_after_functions_return>`
* :ref:`functions return None by default<test_making_a_function_w_return_none>`

:ref:`How many questions can you answer about functions?<questions about functions>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<functions: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

you have covered a bit so far and know

* :ref:`how to make a Python test driven development environment manually<how to make a Python test driven development environment>`
* :ref:`how to raise AssertionError<what causes AssertionError?>` and
* :ref:`how to make functions<what is a function?>`

:ref:`Would you like to test how to pass values from tests to functions with assert methods?<telephone>`

----

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