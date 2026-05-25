.. meta::
  :description: Learn Python TDD by building a project with uv and pytest-watcher. Master passing 9 data types—strings, None, booleans, integers, floats, tuples, lists, dictionaries, and classes—to functions, and learn to debug AssertionError, NameError, AttributeError, and TypeError step-by-step.
  :keywords: Jacob Itegboje, Python TDD tutorial, red green refactor practical example, uv init python project, pytest-watcher automatic testing, passing arguments in python, python pass None to function, python pass list to function, python pass dictionary to function, python pass tuple vs list, python pass class as argument, TypeError: 'NoneType' object is not callable, TypeError: takes 0 positional arguments but 1 was given, NameError: name is not defined python, AttributeError: module has no attribute, assertEqual reality vs expectation, python string interpolation f-string, python unit testing for beginners, python project structure src tests, how to write a failing test first, test driven development python step by step

.. include:: ../links.rst

.. _f-string: https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals
.. _f-strings: `f-string`_git config
.. _string interpolation: https://peps.python.org/pep-0498/

#################################################################################
telephone
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/QEiyAO7aEVQ?si=gN_vRO0VrSyWR7R6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Part of `Computer Programming`_ is sending :ref:`input data<data structures>` to a process and getting :ref:`output data<data structures>` back

.. code-block:: python

    input_data -> process -> output_data

I send things (:ref:`input data<data structures>`) to a program_ to test it, and check if what I think will happen (my expectation) is the same as the results I get (reality). This helps me answer two questions:

* what is the same?
* what is different?

The difference helps me know what to change to get what I want. I do this with the `assertEqual method`_, which takes 2 inputs and checks if they are the same

.. code-block:: python

  self.assertEqual(reality, my_expectation)

where

* ``reality`` is what happens when I do something with code
* ``my_expectation`` is what I think will happen when I do something with code

The exercises in this chapter to show how I can pass :ref:`input data<data structures>` from a test to a :ref:`function<what is a function?>` in a :ref:`module<what is a module?>`.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../code/tests/test_telephone.py
  :language: python
  :linenos:

----

*********************************************************************************
start the project
*********************************************************************************

* I name this project ``telephone``
* I open a terminal_
* I use uv_ to make a directory_ for the project and initialize it

  .. code-block:: python
    :emphasize-lines: 1

    uv init telephone

  the terminal_ shows

  .. code-block:: shell

    Initialized project `telephone`
    at `.../pumping_python/telephone`

  then goes back to the command line.

* I change directory_ to the project

  .. code-block:: shell
    :emphasize-lines: 1

    cd telephone

  the terminal_ shows I am in the ``telephone`` folder_

  .. code-block:: shell

    .../pumping_python/telephone

* I make a directory_ for the source code

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir src

  the terminal_ goes back to the command line.

* I use the `mv program`_ to change the name of ``main.py`` to ``telephone.py`` and move it to the ``src`` folder_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 1

        mv main.py src/telephone.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        Move-Item main.py src/telephone.py

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

        touch tests/test_telephone.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        New-Item tests/test_telephone.py

  the terminal_ goes back to the command line.

* I open ``test_telephone.py`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_

  .. tip::

    I can open a file_ from the terminal_ in the `Integrated Development Environment (IDE)`_ with the name of the program_ and the name of the file_. That means if I type this in the terminal_

    .. code-block:: shell
      :emphasize-lines: 1

      code tests/test_telephone.py

    `Visual Studio Code`_ opens ``test_telephone.py`` in the :ref:`editor<2 editors>`

* I add :ref:`the first failing test<test_failure>` to ``test_telephone.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-7

    import unittest


    class TestTelephone(unittest.TestCase):

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
     create mode 100644 src/telephone.py
     create mode 100644 tests/__init__.py
     create mode 100644 tests/test_telephone.py
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
    ______________________ TestTelephone.test_failure ________________________

    self = <tests.test_telephone.TestTelephone testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_telephone.py:7: AssertionError
    ======================== short test summary info =========================
    FAILED tests/test_telephone.py::TestTelephone::test_failure - AssertionError: True is not false
    =========================== 1 failed in X.YZs ============================

  because :ref:`True<test_what_is_true>` is NOT :ref:`False<test_what_is_false>`

  .. admonition:: if the terminal_ does not show the same error, then check

    * if your ``tests/__init__.py`` has two underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``
    * if you ran ``echo "pytest-watcher" >> requirements.txt``, to add ``pytest-watcher`` to the requirements file_

    fix those errors and try to run ``uv run pytest-watcher . --now`` again

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_telephone.py`` in the :ref:`editor<2 editors>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7-8
    :emphasize-text: AssertionError

    class TestTelephone(unittest.TestCase):

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
test_passing_a_string
*********************************************************************************

I can pass a string_ from a test to a :ref:`function<what is a function?>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change ``test_failure`` to ``test_passing_a_string``

.. code-block:: python
  :lineno-start: 4
  :emphasize-lines: 3-6

  class TestTelephone(unittest.TestCase):

      def test_passing_a_string(self):
          reality = src.telephone.text('hello')
          my_expectation = 'I got: hello'
          self.assertEqual(reality, my_expectation)


  # Exceptions seen
  # AssertionError

the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

.. code-block:: shell

  NameError: name 'src' is not defined

because there is no definition for ``src`` in ``test_telephone.py``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add :ref:`NameError<test_catching_name_error_in_tests>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 3
    :emphasize-text: NameError

    # Exceptions seen
    # AssertionError
    # NameError

* I add an `import statement`_ for the ``telephone`` :ref:`module<what is a module?>` from the ``src`` folder_, at the top of the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.telephone
    import unittest


    class TestTelephone(unittest.TestCase):

  - ``import src.telephone`` brings in an :ref:`object (everything in Python is an object)<what is a class?>` that represents the ``telephone.py`` :ref:`module<what is a module?>` from the ``src`` folder_ so I can use it in ``test_telephone.py``
  - the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

    .. code-block:: shell

      AttributeError: module 'src.telephone'
                      has no attribute 'text'

    because there is no definition for ``text`` in ``telephone.py`` in the ``src`` folder_

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_telephone.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 4
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError

* I use the :ref:`Explorer<explorer on left>` to open ``telephone.py`` from the ``src`` folder in the :ref:`editor<2 editors>`

* I delete the text, then add a name to ``telephone.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    text

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'text' is not defined

  because the name is in the file_, and I have not told Python_ what it means

* I point ``text`` to :ref:`None<what is None?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    text = None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

  because :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_telephone.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 5
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* I change ``text`` to a :ref:`function<what is a function?>` in ``telephone.py`` to make it callable_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def text():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: text() takes 0 positional arguments
               but 1 was given

  because the definition for ``src.telephone.text`` does not allow calling it with inputs and the test sends ``'hello'`` as input - the parentheses are empty.

* I make the :ref:`function<what is a function?>` take input

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def text(the_input):
        return None

  - ``the_input`` is the name I used for the input, I can use any name I want.
  - the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

    .. code-block:: shell

      AssertionError: None != 'I got: hello'

    because the :ref:`assertion<what is an assertion?>` expects ``'I got: hello'`` and the ``text`` :ref:`function<what is a function?>` returns :ref:`None<what is None?>`.

* I copy the string_ from the terminal_ and paste it in the `return statement`_ to replace :ref:`None<what is None?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def text(the_input):
        return 'I got: hello'

  the test passes!

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

The problem with this solution is that the ``text`` :ref:`function<what is a function?>` does not care about what it gets, it always returns ``'I got: hello'`` when called. I want it to return the value it gets as part of the message.

* I add a new :ref:`assertion<what is an assertion?>` to ``test_passing_a_string`` in ``test_telephone.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 6-8

        def test_passing_a_string(self):
            reality = src.telephone.text('hello')
            my_expectation = 'I got: hello'
            self.assertEqual(reality, my_expectation)

            reality = src.telephone.text('yes')
            my_expectation = 'I got: yes'
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 'I got: hello' != 'I got: yes'

  because the ``text`` :ref:`function<what is a function?>` always returns ``'I got: hello'`` and this :ref:`assertion<what is an assertion?>` expects ``'I got: yes'``

* I change the `return statement`_ in ``telephone.py`` to match

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def text(the_input):
        return 'I got: yes'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 'I got: yes' != 'I got: hello'

  it did not work, my change broke the :ref:`assertion<what is an assertion?>` that was passing before. The `return statement`_ has to use the input it gets as part of the output.

----

*********************************************************************************
what is string interpolation?
*********************************************************************************

* I use an `f-string`_ which lets me add any :ref:`variables<what is a variable?>` I want to a string_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def text(the_input):
        return f'I got: {the_input}'

  the test passes.

  This is called `string interpolation`_, I can use it to put values in strings_. A string_ is anything inside :ref:`quotes` e.g.

  - ``'single quotes'``
  - ``'''triple single quotes'''``
  - ``"double quotes"``
  - ``"""triple double quotes"""``

* I add a :ref:`variable<what is a variable?>` to use the remove repetition of ``'hello'`` from the test in ``test_telephone.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2

        def test_passing_a_string(self):
            a_string = 'hello'
            reality = src.telephone.text('hello')
            my_expectation = 'I got: hello'
            self.assertEqual(reality, my_expectation)

* I use the new :ref:`variable<what is a variable?>` and `string interpolation`_ to remove repetition of ``'hello'`` from the test

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 3-6

        def test_passing_a_string(self):
            a_string = 'hello'
            # reality = src.telephone.text('hello')
            reality = src.telephone.text(a_string)
            # my_expectation = 'I got: hello'
            my_expectation = f'I got: {a_string}'
            self.assertEqual(reality, my_expectation)

  the test is still green.

* I add a :ref:`variable<what is a variable?>` to use the remove repetition of ``'yes'`` from the test

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 9

        def test_passing_a_string(self):
            a_string = 'hello'
            # reality = src.telephone.text('hello')
            reality = src.telephone.text(a_string)
            # my_expectation = 'I got: hello'
            my_expectation = f'I got: {a_string}'
            self.assertEqual(reality, my_expectation)

            a_string = 'yes'
            reality = src.telephone.text('yes')
            my_expectation = 'I got: yes'
            self.assertEqual(reality, my_expectation)

* I use the new :ref:`variable<what is a variable?>` and `string interpolation`_ to remove repetition of ``'yes'`` from the test

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 2-5

            a_string = 'yes'
            # reality = src.telephone.text('yes')
            reality = src.telephone.text(a_string)
            # my_expectation = 'I got: yes'
            my_expectation = f'I got: {a_string}'
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 7

        def test_passing_a_string(self):
            a_string = 'hello'
            reality = src.telephone.text(a_string)
            my_expectation = f'I got: {a_string}'
            self.assertEqual(reality, my_expectation)

            a_string = 'yes'
            reality = src.telephone.text(a_string)
            my_expectation = f'I got: {a_string}'
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

* I open a new terminal_ then change directories to ``telephone``

  .. code-block:: python
    :emphasize-lines: 1

    cd telephone

  the terminal_ shows I am in the ``telephone`` folder_

  .. code-block:: python

    .../pumping_python/telephone

* I add a git_ commit message in the new terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_passing_a_string'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can pass a string from a test to a function<test_passing_a_string>`.

----

*********************************************************************************
test_passing_none
*********************************************************************************

I can pass :ref:`None<what is None?>` from a test to a :ref:`function<what is a function?>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a failing test for :ref:`None<what is None?>` (the simplest :ref:`Python data structure<data structures>`) to ``test_telephone.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 12-15

        def test_passing_a_string(self):
            a_string = 'hello'
            reality = src.telephone.text(a_string)
            my_expectation = f'I got: {a_string}'
            self.assertEqual(reality, my_expectation)

            a_string = 'yes'
            reality = src.telephone.text(a_string)
            my_expectation = f'I got: {a_string}'
            self.assertEqual(reality, my_expectation)

        def test_passing_none(self):
            reality = src.telephone.text(None)
            my_expectation = 'I got: "None"'
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 'I got: None' != "I got: 'None'"

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I remove the :ref:`quotes` around :ref:`None<what is None?>` in ``my_expectation``

.. code-block:: python
  :lineno-start: 18
  :emphasize-lines: 3

      def test_passing_none(self):
          reality = src.telephone.text(None)
          my_expectation = 'I got: None'
          self.assertEqual(reality, my_expectation)


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 2

        def test_passing_none(self):
            none = None
            reality = src.telephone.text(None)
            my_expectation = 'I got: None'
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

* I use the :ref:`variable<what is a variable?>` with an `f-string`_ to remove repetition of :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 3-6

        def test_passing_none(self):
            none = None
            # reality = src.telephone.text(None)
            reality = src.telephone.text(none)
            # my_expectation = 'I got: None'
            my_expectation = f'I got: {none}'
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test is still green.

* I remove the comments

  .. code-block:: python
    :lineno-start: 18

        def test_passing_none(self):
            none = None
            reality = src.telephone.text(none)
            my_expectation = f'I got: {none}'
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit --all --message 'add test_passing_none'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can pass None from a test to a function<test_passing_none>`.

----

*********************************************************************************
test_passing_booleans
*********************************************************************************

I can pass :ref:`booleans<what are booleans?>` from a test to a :ref:`function<what is a function?>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a test for :ref:`booleans<what are booleans?>`, first with an :ref:`assertion<what is an assertion?>` for :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 7-10
    :emphasize-text: "

        def test_passing_none(self):
            none = None
            reality = src.telephone.text(none)
            my_expectation = f'I got: {none}'
            self.assertEqual(reality, my_expectation)

        def test_passing_booleans(self):
            reality = src.telephone.text(False)
            my_expectation = 'I got: "False"'
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 'I got: False' != 'I got: "False"'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I remove the :ref:`quotes` around :ref:`False<test_what_is_false>` in ``my_expectation``

.. code-block:: python
  :lineno-start: 24
  :emphasize-lines: 3

      def test_passing_booleans(self):
          reality = src.telephone.text(False)
          my_expectation = 'I got: False'
          self.assertEqual(reality, my_expectation)


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 6-8
    :emphasize-text: "

        def test_passing_booleans(self):
            reality = src.telephone.text(False)
            my_expectation = 'I got: False'
            self.assertEqual(reality, my_expectation)

            reality = src.telephone.text(True)
            my_expectation = 'I got: "True"'
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 'I got: True' != 'I got: "True"'

I remove the :ref:`quotes` around :ref:`True<test_what_is_true>` in ``my_expectation``

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2

            reality = src.telephone.text(True)
            my_expectation = 'I got: True'
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 2

        def test_passing_booleans(self):
            false = False
            reality = src.telephone.text(False)
            my_expectation = 'I got: False'
            self.assertEqual(reality, my_expectation)

* I use the :ref:`variable<what is a variable?>` with a `string interpolation`_ to remove repetition of :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 3-6

        def test_passing_booleans(self):
            false = False
            # reality = src.telephone.text(False)
            reality = src.telephone.text(false)
            # my_expectation = 'I got: False'
            my_expectation = f'I got: {false}'
            self.assertEqual(reality, my_expectation)

  the test is still green.

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 9

        def test_passing_booleans(self):
            false = False
            # reality = src.telephone.text(False)
            reality = src.telephone.text(false)
            # my_expectation = 'I got: False'
            my_expectation = f'I got: {false}'
            self.assertEqual(reality, my_expectation)

            true = True
            reality = src.telephone.text(True)
            my_expectation = 'I got: True'
            self.assertEqual(reality, my_expectation)

* I use the :ref:`variable<what is a variable?>` with an `f-string`_ to remove repetition of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 3-6

            true = True
            # reality = src.telephone.text(True)
            reality = src.telephone.text(true)
            # my_expectation = 'I got: True'
            my_expectation = f'I got: {true}'
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  still green.

* I remove the comments

  .. code-block:: python
    :lineno-start: 24

        def test_passing_booleans(self):
            false = False
            reality = src.telephone.text(false)
            my_expectation = f'I got: {false}'
            self.assertEqual(reality, my_expectation)

            true = True
            reality = src.telephone.text(true)
            my_expectation = f'I got: {true}'
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_passing_booleans'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can pass booleans from a test to a function<test_passing_booleans>`.

----

*********************************************************************************
test_passing_an_integer
*********************************************************************************

I can pass an integer_ (a whole number with no decimals) from a test to a :ref:`function<what is a function?>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a test for an integer_

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 6-9
    :emphasize-text: "

            true = True
            reality = src.telephone.text(true)
            my_expectation = f'I got: {true}'
            self.assertEqual(reality, my_expectation)

        def test_passing_an_integer(self):
            reality = src.telephone.text(1234)
            my_expectation = 'I got: "1234"'
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 'I got: 1234' != "I got: '1234'"

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I remove the :ref:`quotes` around the integer_ in ``my_expectation``

.. code-block:: python
  :lineno-start: 35
  :emphasize-lines: 3

      def test_passing_an_integer(self):
          reality = src.telephone.text(1234)
          my_expectation = 'I got: 1234'
          self.assertEqual(reality, my_expectation)


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``1234``

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 2

        def test_passing_an_integer(self):
            an_integer = 1234
            reality = src.telephone.text(1234)
            my_expectation = 'I got: 1234'
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

* I use the :ref:`variable<what is a variable?>` with `string interpolation`_ to remove repetition of ``1234``

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 3-6

        def test_passing_an_integer(self):
            an_integer = 1234
            # reality = src.telephone.text(1234)
            reality = src.telephone.text(an_integer)
            # my_expectation = 'I got: 1234'
            my_expectation = f'I got: {an_integer}'
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test is still green.

* I remove the comments

  .. code-block:: python
    :lineno-start: 35

        def test_passing_an_integer(self):
            an_integer = 1234
            reality = src.telephone.text(an_integer)
            my_expectation = f'I got: {an_integer}'
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_passing_an_integer'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can pass an integer from a test to a function<test_passing_an_integer>`.

----

*********************************************************************************
test_passing_a_float
*********************************************************************************

I can pass a float_ (binary floating point decimal number) from a test to a :ref:`function<what is a function?>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests
* I add a test for a float_ (binary floating point decimal numbers)

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 7-10
    :emphasize-text: "

        def test_passing_an_integer(self):
            an_integer = 1234
            reality = src.telephone.text(an_integer)
            my_expectation = f'I got: {an_integer}'
            self.assertEqual(reality, my_expectation)

        def test_passing_a_float(self):
            reality = src.telephone.text(1.234)
            my_expectation = 'I got: "1.234"'
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 'I got: 1.234' != 'I got: "1.234"'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I remove the :ref:`quotes` around the float_ in ``my_expectation``

.. code-block:: python
  :lineno-start: 41
  :emphasize-lines: 3

      def test_passing_a_float(self):
          reality = src.telephone.text(1.234)
          my_expectation = 'I got: 1.234'
          self.assertEqual(reality, my_expectation)


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``1.234``

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 2

        def test_passing_a_float(self):
            a_float = 1.234
            reality = src.telephone.text(1.234)
            my_expectation = 'I got: "1.234"'
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

* I use the :ref:`variable<what is a variable?>` with an `f-string`_ to remove repetition of ``1.234``

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 3-6

        def test_passing_a_float(self):
            a_float = 1.234
            # reality = src.telephone.text(1.234)
            reality = src.telephone.text(a_float)
            # my_expectation = 'I got: "1.234"'
            my_expectation = f'I got: {a_float}'
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test is still green.

* I remove the comments

  .. code-block:: python
    :lineno-start: 41

        def test_passing_a_float(self):
            a_float = 1.234
            reality = src.telephone.text(a_float)
            my_expectation = f'I got: {a_float}'
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit --all --message 'add test_passing_a_float'

  the terminal_ shows a summary of the changes then goes back to the command line.


:ref:`I can pass a float from a test to a function<test_passing_a_float>`.

----

*********************************************************************************
test_passing_a_tuple
*********************************************************************************

I can pass a tuple_ (anything in parentheses ``( )`` separated by a comma) from a test to a :ref:`function<what is a function?>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a test for a tuple_

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 7-10
    :emphasize-text: "

        def test_passing_a_float(self):
            a_float = 1.234
            reality = src.telephone.text(a_float)
            my_expectation = f'I got: {a_float}'
            self.assertEqual(reality, my_expectation)

        def test_passing_a_tuple(self):
            reality = src.telephone.text((1, 2, 3, 'n'))
            my_expectation = 'I got: (1, 2, 3, n)'
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: "I got: (1, 2, 3, 'n')"
                 != 'I got: "(1, 2, 3, n)"'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the tuple_ in ``my_expectation`` to match ``reality``

.. code-block:: python
  :lineno-start: 47
  :emphasize-lines: 3
  :emphasize-text: "

      def test_passing_a_tuple(self):
          reality = src.telephone.text((1, 2, 3, 'n'))
          my_expectation = "I got: (1, 2, 3, 'n')"
          self.assertEqual(reality, my_expectation)


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of the tuple_

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 2

        def test_passing_a_tuple(self):
            a_tuple = (1, 2, 3, 'n')
            reality = src.telephone.text((1, 2, 3, 'n'))
            my_expectation = "I got: (1, 2, 3, 'n')"
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

* I use the :ref:`variable<what is a variable?>` with `string interpolation`_ to remove repetition of the tuple_

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 3-6

        def test_passing_a_tuple(self):
            a_tuple = (1, 2, 3, 'n')
            # reality = src.telephone.text((1, 2, 3, 'n'))
            reality = src.telephone.text(a_tuple)
            # my_expectation = "I got: (1, 2, 3, 'n')"
            my_expectation = f"I got: {a_tuple}"
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test is still green.

* I remove the comments

  .. code-block:: python
    :lineno-start: 47

        def test_passing_a_tuple(self):
            a_tuple = (1, 2, 3, 'n')
            reality = src.telephone.text(a_tuple)
            my_expectation = f"I got: {a_tuple}"
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_passing_a_tuple'

  the terminal_ shows a summary of the changes then goes back to the command line.


:ref:`I can pass a tuple from a test to a function<test_passing_a_tuple>`.

----

*********************************************************************************
test_passing_a_list
*********************************************************************************

I can pass a :ref:`list<what is a list?>` (anything in square brackets ``[ ]``) from a test to a :ref:`function<what is a function?>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a test for a :ref:`list <lists>`

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 7-10
    :emphasize-text: '

        def test_passing_a_tuple(self):
            a_tuple = (1, 2, 3, 'n')
            reality = src.telephone.text(a_tuple)
            my_expectation = f"I got: {a_tuple}"
            self.assertEqual(reality, my_expectation)

        def test_passing_a_list(self):
            reality = src.telephone.text([1, 2, 3, 'n'])
            my_expectation = 'I got: [1, 2, 3, "n"]'
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: "I got: [1, 2, 3, 'n']"
                 != "I got: '[1, 2, 3, n]'"

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the :ref:`list<what is a list?>` in ``my_expectation`` to match ``reality``

.. code-block:: python
  :lineno-start: 53
  :emphasize-lines: 3
  :emphasize-text: " '

      def test_passing_a_list(self):
          reality = src.telephone.text([1, 2, 3, "n"])
          my_expectation = "I got: [1, 2, 3, 'n']"
          self.assertEqual(reality, my_expectation)


  # Exceptions seen

the test passes. Python_ changed the :ref:`double quotes<quotes>` (``"``) in the :ref:`list<what is a list?>` to a :ref:`single quote<quotes>` (``'``).

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of the :ref:`list<what is a list?>`

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 2

        def test_passing_a_list(self):
            a_list = [1, 2, 3, 'n']
            reality = src.telephone.text([1, 2, 3, 'n'])
            my_expectation = "I got: [1, 2, 3, 'n']"
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

* I use the :ref:`variable<what is a variable?>` with an `f-string`_ to remove repetition of the :ref:`list<what is a list?>`

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 3-6

        def test_passing_a_list(self):
            a_list = [1, 2, 3, 'n']
            # reality = src.telephone.text([1, 2, 3, 'n'])
            reality = src.telephone.text(a_list)
            # my_expectation = "I got: [1, 2, 3, 'n']"
            my_expectation = f"I got: {a_list}"
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test is still green.

* I remove the comments

  .. code-block:: python
    :lineno-start: 53

        def test_passing_a_list(self):
            a_list = [1, 2, 3, 'n']
            reality = src.telephone.text(a_list)
            my_expectation = f"I got: {a_list}"
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit --all --message 'add test_passing_a_list'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can pass a list from a test to a function<test_passing_a_list>`.

----

*********************************************************************************
test_passing_a_dictionary
*********************************************************************************

I can pass a :ref:`dictionary<what is a dictionary?>` (anything in curly braces ``{ }`` separated by a comma) from a test to a :ref:`function<what is a function?>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a test for a :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 7-18
    :emphasize-text: "

        def test_passing_a_list(self):
            a_list = [1, 2, 3, 'n']
            reality = src.telephone.text(a_list)
            my_expectation = f"I got: {a_list}"
            self.assertEqual(reality, my_expectation)

        def test_passing_a_dictionary(self):
            reality = src.telephone.text(
                {
                    'key1': 'value1',
                    'keyN': [0, 1, 2, 'n'],
                }
            )
            my_expectation = (
                "I got: "
                "{key1: value1, keyN: [0, 1, 2, n]}"
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        "I got: {'key1': 'value1', 'keyN': [0, 1, 2, 'n']}"
     != 'I got: { key1:   value1 ,  keyN : [0, 1, 2,  n ]}'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change ``my_expectation`` to match ``reality``

.. code-block:: python
  :lineno-start: 59
  :emphasize-lines: 10-11
  :emphasize-text: '

      def test_passing_a_dictionary(self):
          reality = src.telephone.text(
              {
                  'key1': 'value1',
                  'keyN': [0, 1, 2, 'n'],
              }
          )
          my_expectation = (
              "I got: "
              "{'key1': 'value1', "
              "'keyN': [0, 1, 2, 'n']}"
          )
          self.assertEqual(reality, my_expectation)


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of the :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 2-5

        def test_passing_a_dictionary(self):
            a_dictionary = {
                'key1': 'value1',
                'keyN': [0, 1, 2, 'n'],
            }
            reality = src.telephone.text(
                {
                    'key1': 'value1',
                    'keyN': [0, 1, 2, 'n'],
                }
            )
            my_expectation = (
                "I got: "
                "{'key1': 'value1', 'keyN': [0, 1, 2, 'n']}"
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

* I use the :ref:`variable<what is a variable?>` with `string interpolation`_ to remove repetition of the :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 6-17

        def test_passing_a_dictionary(self):
            a_dictionary = {
                'key1': 'value1',
                'keyN': [0, 1, 2, 'n'],
            }
            # reality = src.telephone.text(
            #     {
            #         'key1': 'value1',
            #         'keyN': [0, 1, 2, 'n'],
            #     }
            # )
            reality = src.telephone.text(a_dictionary)
            # my_expectation = (
            #     "I got: "
            #     "{'key1': 'value1', 'keyN': [0, 1, 2, 'n']}"
            # )
            my_expectation = f'I got: {a_dictionary}'
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test is still green.

* I remove the comments

  .. code-block:: python
    :lineno-start: 59

        def test_passing_a_dictionary(self):
            a_dictionary = {
                'key1': 'value1',
                'keyN': [0, 1, 2, 'n'],
            }
            reality = src.telephone.text(a_dictionary)
            my_expectation = f'I got: {a_dictionary}'
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_passing_a_dictionary'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can pass a dictionary from a test to a function<test_passing_a_dictionary>`.

----

*********************************************************************************
test_passing_a_class
*********************************************************************************

I can pass an :ref:`object<what is a class?>` from a test to a :ref:`function<what is a function?>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a failing test to see what happens when I pass a :ref:`class <what is a class?>` from a test to the ``text`` :ref:`function<what is a function?>`, in ``test_telephone.py``

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 10-13

        def test_passing_a_dictionary(self):
            a_dictionary = {
                'key1': 'value1',
                'keyN': [0, 1, 2, 'n'],
            }
            reality = src.telephone.text(a_dictionary)
            my_expectation = f'I got: {a_dictionary}'
            self.assertEqual(reality, my_expectation)

        def test_passing_a_class(self):
            reality = src.telephone.text(object)
            my_expectation = 'I got: object'
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: "I got: <class 'object'>"
                 != 'I got:         object'

  :ref:`object<what is a class?>` is the :ref:`mother class<what is a class?>` that all :ref:`Python classes<what is a class?>` come from, and everything in Python_ is an :ref:`object<what is a class?>`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change ``my_expectation`` to match ``reality``

.. code-block:: python
  :lineno-start: 68
  :emphasize-lines: 3
  :emphasize-text: " '

      def test_passing_a_class(self):
          reality = src.telephone.text(object)
          my_expectation = "I got: <class 'object'>"
          self.assertEqual(reality, my_expectation)


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another :ref:`assertion<what is an assertion?>` with the ``TestTelephone`` :ref:`class<what is a class?>` to ``test_passing_a_class`` in ``test_telephone.py``

  .. code-block:: python
    :lineno-start: 68
    :emphasize-lines: 6-8

        def test_passing_a_class(self):
            reality = src.telephone.text(object)
            my_expectation = "I got: <class 'object'>"
            self.assertEqual(reality, my_expectation)

            reality = src.telephone.text(TestTelephone)
            my_expectation = "I got: <class 'object'>"
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        "I got: <class 'tests.test_telephone.TestTelephone'>"
     != "I got: <class 'object'>"

* I change ``my_expectation`` to match ``reality``

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 2-5
    :emphasize-text: '

            reality = src.telephone.text(TestTelephone)
            my_expectation = (
                "I got: <class "
                "'tests.test_telephone.TestTelephone'>"
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes. What does ``tests.test_telephone.TestTelephone`` point to?

  - ``tests`` is the folder_
  - ``test_telephone`` is ``test_telephone.py`` in the ``tests`` folder_
  - ``TestTelephone`` is the :ref:`class (object)<what is a class?>` that is defined on line 5 of ``test_telephone.py`` in the ``tests`` folder_

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 8-10

            reality = src.telephone.text(TestTelephone)
            my_expectation = (
                "I got: <class "
                "'tests.test_telephone.TestTelephone'>"
            )
            self.assertEqual(reality, my_expectation)

            reality = src.telephone.text(self)
            my_expectation = "I got: self"
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        'I got: test_passing_a_class (
            tests.test_telephone
                 .TestTelephone.test_passing_a_class
        )'
        != 'I got: self'

* I change ``my_expectation`` to match ``reality``

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 2-6

            reality = src.telephone.text(self)
            my_expectation = (
                "I got: test_passing_a_class "
                "(tests.test_telephone.TestTelephone"
                ".test_passing_a_class)"
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit --all --message 'add test_passing_a_class'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can pass an object from a test to a function<test_passing_a_class>`.

----

*********************************************************************************
test_telephone
*********************************************************************************

Time to write the program_ that makes the tests pass without looking at ``test_telephone.py``

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I close ``test_telephone.py`` in the :ref:`editor<2 editors>`

* I delete the text in ``telephone.py`` and the terminal_ shows 9 failures. I start with the last :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    FAILED ...test_passing_a_class - AttributeError:
            module 'src.telephone' has no attribute 'text'
    FAILED ...test_passing_a_dictionary - AttributeError:
            module 'src.telephone' has no attribute 'text'
    FAILED ...test_passing_a_float - AttributeError:
            module 'src.telephone' has no attribute 'text'
    FAILED ...test_passing_a_list - AttributeError:
            module 'src.telephone' has no attribute 'text'
    FAILED ...test_passing_a_string - AttributeError:
            module 'src.telephone' has no attribute 'text'
    FAILED ...test_passing_a_tuple - AttributeError:
            module 'src.telephone' has no attribute 'text'
    FAILED ...test_passing_an_integer - AttributeError:
            module 'src.telephone' has no attribute 'text'
    FAILED ...test_passing_booleans - AttributeError:
            module 'src.telephone' has no attribute 'text'
    FAILED ...test_passing_none - AttributeError:
            module 'src.telephone' has no attribute 'text'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the name to ``telephone.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    text

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'text' is not defined

* I point it to :ref:`None<what is None?>` to define it

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    text = None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

* I make ``text`` a :ref:`function<what is a function?>` to make it callable_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def text():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: text() takes 0 positional arguments
               but 1 was given

* I make the :ref:`function<what is a function?>` take input

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def text(value):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None != 'I got: None'

* I copy the string_ from the terminal_ and paste it in the `return statement`_ to match the expectation of the test

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def text(value):
        return 'I got: None'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 'I got: None' != 'I got: False'

* I add a `return statement`_ to see the difference between the input and the expected output (remember :ref:`the identity function?<test_identity_function>`)

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def text(value):
        return value
        return 'I got: None'

  the test summary info shows that every test has :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-text: I got:

    AssertionError:
        <class 'object'> != "I got: <class 'object'>"
    AssertionError:
                 {'key1': 'value1', 'keyN': [0, 1, 2, 'n']}
      != "I got: {'key1': 'value1', 'keyN': [0, 1, 2, 'n']}"
    AssertionError:
        1.234 != 'I got: 1.234'
    AssertionError:
        [1, 2, 3, 'n'] != "I got: [1, 2, 3, 'n']"
    AssertionError:
        'hello' != 'I got: hello'
    AssertionError:
        (1, 2, 3, 'n') != "I got: (1, 2, 3, 'n')"
    AssertionError:
        1234 != 'I got: 1234'
    AssertionError:
        False != 'I got: False'
    AssertionError:
        None != 'I got: None'

  they all expect the input (``value``) as part of the message

* I remove the first `return statement`_ then make the second one use an `f-string`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def text(value):
        return f'I got: {value}'

  and all the tests are passing! I am a programmer!!

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``telephone.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_ where the tests are running, then use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``telephone``

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

Here are the tests I ran to see what happens when I pass :ref:`Python basic data structures<data structures>` from a test to a program_ and place them in an `f-string`_ which is one way to do :ref:`string interpolation<what is string interpolation?>`

* `test_passing_a_string`_
* `test_passing_none`_
* `test_passing_booleans`_
* `test_passing_an_integer`_
* `test_passing_a_float`_
* `test_passing_a_tuple`_
* `test_passing_a_list`_
* `test_passing_a_dictionary`_
* `test_passing_a_class`_

I also saw these :ref:`Exceptions<errors>`

* :ref:`AssertionError<what causes AssertionError?>`
* :ref:`NameError<test_catching_name_error_in_tests>`
* :ref:`AttributeError<what causes AttributeError?>`
* :ref:`TypeError<what causes TypeError?>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<how to pass values: tests and solution>`

----

*************************************************************************************
what is next?
*************************************************************************************

You now know:

* :ref:`how to make a Python test driven development environment manually<how to make a Python test driven development environment>`
* :ref:`how to raise AssertionError<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to pass values from tests to functions<telephone>`

:ref:`would you like to test using dictionaries and functions to make a person?<how to make a person>`

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