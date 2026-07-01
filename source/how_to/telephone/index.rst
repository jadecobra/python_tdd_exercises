.. meta::
  :description: Learn Python TDD with the telephone metaphor: pass input objects (starting with None, then booleans, integers, floats, strings, tuples, lists, sets, dictionaries, classes) to a function and use an f-string to produce output strings like 'I got: None'. Use uv init + pytest-watcher, bare 'reality == my_expectation' asserts with locals in test functions, then separate the solution into src/telephone.py from tests/test_telephone.py. Debug NameError: name 'text' is not defined, TypeError takes 0 positional arguments but 1 was given, TypeError: 'NoneType' object is not callable, ModuleNotFoundError: No module named 'src.telephone', AttributeError: module 'src.telephone' has no attribute 'text', and AssertionError from mismatched expectations. Demonstrates another way to organize tests with separate solution from tests.
  :keywords: Jacob Itegboje, Python TDD tutorial, red green refactor practical example, uv init python project, pytest-watcher automatic testing, passing arguments in python, python pass None to function, python pass list to function, python pass dictionary to function, python pass tuple vs list, python pass class as argument, telephone input process output, separate solution from tests, src/telephone.py, reality == my_expectation bare assert, I got: None, f-string interpolation any object, TypeError: 'NoneType' object is not callable, TypeError: takes 0 positional arguments but 1 was given, NameError: name is not defined python, AttributeError: module has no attribute, ModuleNotFoundError: No module named 'src.telephone', python string interpolation f-string, python unit testing for beginners, python project structure src tests, how to write a failing test first, test driven development python step by step

.. include:: ../../links.rst

.. _f-string: https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals
.. _f-strings: `f-string`_
.. _string interpolation: https://peps.python.org/pep-0498/

#################################################################################
telephone
#################################################################################

Part of `Computer Programming`_ is sending :ref:`input data<data structures>` to a process and getting :ref:`output data<data structures>` back

.. code-block:: python

    input_data -> process -> output_data

I send things (:ref:`input data<data structures>`) to a program_ to test it, and check if what I think will happen (my expectation) is the same as the results I get (reality). This helps me answer two questions:

* what is the same?
* what is different?

The difference helps me know what to change to get what I want. I use :ref:`assertions<what is an assertion?>` to test if the result of a :ref:`call to a function with input<functions that take input>` is the same as my expectation.

.. code-block:: python

  assert reality == my_expectation

where

* reality is what happens when I do something with code
* my expectation is what I think will happen when I do something with code

The exercises in this chapter show how I can pass :ref:`objects<what is a class?>` to a :ref:`function<what is a function?>` and use it to make a string_ (anything in :ref:`quotes`). It will also show :ref:`another way to organize tests<separate and equal>`.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/tests/test_telephone.py
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

  .. code-block:: python
    :emphasize-lines: 1

    cd telephone

  the terminal_ shows I am in the ``telephone`` folder_

  .. code-block:: python

    .../pumping_python/telephone

* I `make a directory`_ for the tests

  .. code-block:: python
    :emphasize-lines: 1

    mkdir tests

  the terminal_ goes back to the command line.

* I make the ``tests`` directory_ a `Python package`_

  .. danger:: use 2 underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        touch tests/__init__.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        New-Item tests/__init__.py

  the terminal_ goes back to the command line.

* I use the `mv program`_ to change the name of ``main.py`` to ``test_telephone.py`` and move it to the ``tests`` folder_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        mv main.py tests/test_telephone.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        Move-Item main.py tests/test_telephone.py

  the terminal_ goes back to the command line.

* I open ``test_telephone.py``

* I delete all the text then add :ref:`the first failing test<test_failure>` to ``test_telephone.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def test_failure():
        assert False is True

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

* I use uv_ to install `pytest-watcher`_ with the requirements file_

  .. code-block:: python
    :emphasize-lines: 1

    uv add --requirement requirements.txt

  the terminal_ shows that it installed `pytest-watcher`_ and its dependencies.

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
     8 files changed, X insertions(+)
     create mode 100644 .gitignore
     create mode 100644 .python-version
     create mode 100644 README.md
     create mode 100644 pyproject.toml
     create mode 100644 requirements.txt
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
    :emphasize-lines: 6, 8, 10

    ======================== FAILURES ========================
    ______________________ test_failure ______________________

        def test_failure():
    >       assert False is True
    E       assert False is True

    test_telephone.py:2: AssertionError
    ================ short test summary info =================
    FAILED test_telephone.py::test_failure - assert False is True
    =================== 1 failed in X.YZs ====================

  because :ref:`True<test_what_is_true>` is NOT :ref:`False<test_what_is_false>`

  .. admonition:: if the terminal_ does not show the same error, then check

    * if your ``tests/__init__.py`` has two underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``
    * if you ran ``echo "pytest-watcher" >> requirements.txt``, to add ``pytest-watcher`` to the requirements file_

    fix those errors and try to run ``uv run pytest-watcher . --now`` again

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_telephone.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6
    :emphasize-text: AssertionError

    def test_failure():
        assert False is True


    # Exceptions seen
    # AssertionError

* I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def test_failure():
        # assert False is True
        assert False is False


    # Exceptions seen
    # AssertionError

  the test passes.

----

*********************************************************************************
test_passing_none
*********************************************************************************

I can pass :ref:`None (the simplest object)<what is None?>` as input to a :ref:`function<what is a function?>`?

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I change ``test_failure`` to :ref:`test_passing_none` with an :ref:`assertion<what is an assertion?>` for a :ref:`function call<how to call a function>` with :ref:`None<what is None?>` (the simplest :ref:`Python data structure<data structures>`) as input, in ``test_telephone.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def test_passing_none():
        assert text(None) == 'I got: None'


    # Exceptions seen
    # AssertionError

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'text' is not defined

  because I have not :ref:`defined the function<how to make a function that takes input>` yet.

* I add :ref:`NameError<test_catching_name_error_in_tests>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3
    :emphasize-text: NameError

    # Exceptions seen
    # AssertionError
    # NameError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def test_passing_none():
        def text():
            return None

        assert text(None) == 'I got: None'


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: test_passing_none.<locals>.text()
               takes 0 positional arguments but 1 was given

  because the :ref:`assertion<what is an assertion?>` called the ``text`` :ref:`function<what is a function?>` which belongs to :ref:`test_passing_none` with input (:ref:`None<what is None?>`) and the :ref:`function definition<how to make a function that takes input>` does not allow any inputs, the parentheses are empty.

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 4
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError

* I add a name to the :ref:`function definition<how to make a function that takes input>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def test_passing_none():
        # def text():
        def text(the_input):
            return None

        assert text(None) == 'I got: None'


    # Exceptions seen

  - ``the_input`` is the name I used for the input, I can use any name I want.
  - the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

    .. code-block:: python

      E       assert None == 'I got: None'

  because the :ref:`assertion<what is an assertion?>` expects ``'I got: None'`` and the ``text`` :ref:`function<what is a function?>` returns :ref:`None<what is None?>`.

* I copy the string_ from the terminal_ and paste it in the :ref:`return statement<the return statement>` to replace :ref:`None<what is None?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    def test_passing_none():
        # def text():
        def text(the_input):
            # return None
            return 'I got: None'

        assert text(None) == 'I got: None'


    # Exceptions seen

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def test_passing_none():
        def text(the_input):
            return 'I got: None'

        assert text(None) == 'I got: None'


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

    git commit -am 'add test_passing_none'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can pass None as input to a function<test_passing_none>`.

The problem with this solution is that the ``text`` :ref:`function<what is a function?>` does not care about what it gets, it always returns ``'I got: None'`` when it is called. I want it to return the :ref:`object<what is a class?>` it gets as part of the string_.

----

*********************************************************************************
test_passing_booleans
*********************************************************************************

I can pass :ref:`booleans<what are booleans?>` from a test to a :ref:`function<what is a function?>.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test for :ref:`booleans (there are only two)<what are booleans?>`, first with an :ref:`assertion<what is an assertion?>` for :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 8-9

    def test_passing_none():
        def text(the_input):
            return 'I got: None'

        assert text(None) == 'I got: None'


    def test_passing_booleans():
        assert text(False) == 'I got: False'


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'text' is not defined

  because the ``text`` :ref:`function<what is a function?>`  belongs to the :ref:`test_passing_none function<test_passing_none>` and I cannot reach it from outside.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I move the ``text`` :ref:`function<what is a function?>` out of :ref:`test_passing_none` so that it can be called from anywhere in the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def text(the_input):
        return 'I got: None'


    def test_passing_none():
        assert text(None) == 'I got: None'


    def test_passing_booleans():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert 'I got: None' == 'I got: False'

  because the ``text`` :ref:`function<what is a function?>` always returns ``'I got: None'`` and this :ref:`assertion<what is an assertion?>` expects ``'I got: False'``

* I change :ref:`the return statement` to give the test what it wants

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def text(the_input):
        # return 'I got: None'
        return 'I got: False'


    def test_passing_none():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert 'I got: False' == 'I got: None'

  - because the ``text`` :ref:`function<what is a function?>` now always returns ``'I got: False'`` and the :ref:`assertion<what is an assertion?>` in :ref:`test_passing_none` expects ``'I got: None'``. My change broke the :ref:`assertion<what is an assertion?>` that was passing before.
  - :ref:`The return statement<the return statement>` has to use the input it gets as part of the output.

----

*********************************************************************************
what is string interpolation?
*********************************************************************************

`String Interpolation`_ is the placing of :ref:`objects<what is a class?>` in strings_. It allows me to make one string_ that can have changing values.

I can use an `f-string`_ (short for formatted string literal) for `string interpolation`_.

A string_ is anything inside :ref:`quotes`, for example

* ``'single quotes'``
* ``'''triple single quotes'''``
* ``"double quotes"``
* ``"""triple double quotes"""``

----

=================================================================================
how to write an f-string
=================================================================================

----

* ``f`` before the opening :ref:`quote<quotes>`
* ``{ }`` around the :ref:`object<what is a class?>` being placed in the string_

.. code-block:: python

  f'characters {object}'


* I change :ref:`the return statement` to an :ref:`f-string<what is string interpolation?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    def text(the_input):
        # return 'I got: None'
        # return 'I got: False'
        return f'I got: {the_input}'


    def test_passing_none():

  the test passes because Python_ uses the string_ representation of the :ref:`object<what is a class?>` in the curly braces ``{ }``

  .. code-block:: python

    text(None)
        text(the_input)
            the_input = None
            return f'I got: {the_input}'
            return  'I got:  None      '

  .. code-block:: python

    text(False)
        text(the_input)
            the_input = False
            return f'I got: {the_input}'
            return  'I got:  False     '

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def text(the_input):
        return f'I got: {the_input}'


    def test_passing_none():

* I add an :ref:`assertion<what is an assertion?>` for :ref:`True (the other boolean)<test_what_is_true>` to :ref:`test_passing_booleans`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2
    :emphasize-text: "

    def test_passing_booleans():
        assert text(False) == 'I got: False'
        assert text(True) == 'I got: "True"'


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert 'I got: True' == 'I got: "True"

* I remove the :ref:`quotes` around :ref:`True<test_what_is_true>` in my expectation

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 3-4

    def test_passing_booleans():
        assert text(False) == 'I got: False'
        # assert text(True) == 'I got: "True"'
        assert text(True) == 'I got: True'


    # Exceptions seen

  the test passes because Python_ uses the string_ representation of the :ref:`object<what is a class?>` in the curly braces ``{ }``

  .. code-block:: python

    text(True)
        text(the_input)
            the_input = True
            return f'I got: {the_input}'
            return  'I got:  True      '

* I remove the commented line

  .. code-block:: python
    :lineno-start: 9

    def test_passing_booleans():
        assert text(False) == 'I got: False'
        assert text(True) == 'I got: True'


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_passing_booleans'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can pass booleans as input to a function<test_passing_booleans>`.

----

*********************************************************************************
test_passing_an_integer
*********************************************************************************

Can I pass an integer_ (a whole number without decimals) as input to a :ref:`function<what is a function?>`?.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test for an integer_

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 6-7
    :emphasize-text: "

    def test_passing_booleans():
        assert text(False) == 'I got: False'
        assert text(True) == 'I got: True'


    def test_passing_an_integer():
        assert text(1234) == 'I got: "1234"'


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert 'I got: 1234' == 'I got: "1234"'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I remove the :ref:`quotes` around the integer_ in my expectation

.. code-block:: python
  :lineno-start: 14
  :emphasize-lines: 2-3

  def test_passing_an_integer():
      # assert text(1234) == 'I got: "1234"'
      assert text(1234) == 'I got: 1234'


  # Exceptions seen

the test passes because Python_ uses the string_ representation of the :ref:`object<what is a class?>` in the curly braces ``{ }``

.. code-block:: python

  text(1234)
      text(the_input)
          the_input = None
          return f'I got: {the_input}'
          return  'I got:  1234      '

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`variable<what is a variable?>` for ``1234``

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 2

    def test_passing_an_integer():
        an_integer = 1234
        # assert text(1234) == 'I got: "1234"'
        assert text(1234) == 'I got: 1234'


    # Exceptions seen

* I use the :ref:`variable<what is a variable?>` and an :ref:`f-string<what is string interpolation?>` to remove repetition of ``1234``

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 4-5

    def test_passing_an_integer():
        an_integer = 1234
        # assert text(1234) == 'I got: "1234"'
        # assert text(1234) == 'I got: 1234'
        assert text(an_integer) == f'I got: {an_integer}'


    # Exceptions seen

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 14

    def test_passing_an_integer():
        an_integer = 1234
        assert text(an_integer) == f'I got: {an_integer}'


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_passing_an_integer'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can pass an integer as input to a function<test_passing_an_integer>`.

----

*********************************************************************************
test_passing_a_float
*********************************************************************************

Can I pass a float_ (binary floating point decimal number) as input to a :ref:`function<what is a function?>`?.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test for a float_ (binary floating point decimal numbers)

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 6-7
    :emphasize-text: "

    def test_passing_an_integer():
        an_integer = 1234
        assert text(an_integer) == f'I got: {an_integer}'


    def test_passing_a_float():
        assert text(5.678) == 'I got: "5.678"'


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert 'I got: 5.678' == 'I got: "5.678"'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I remove the :ref:`quotes` around the float_ in my expectation

.. code-block:: python
  :lineno-start: 19
  :emphasize-lines: 2-3

  def test_passing_a_float():
      # assert text(5.678) == 'I got: "5.678"'
      assert text(5.678) == 'I got: 5.678'


  # Exceptions seen

the test passes because Python_ uses the string_ representation of the :ref:`object<what is a class?>` in the curly braces ``{ }``

.. code-block:: python

  text(5.678)
      text(the_input)
          the_input = 5.678
          return f'I got: {the_input}'
          return  'I got:  5.678     '

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`variable<what is a variable?>` for ``5.678``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 2

    def test_passing_a_float():
        a_float = 5.678
        # assert text(5.678) == 'I got: "5.678"'
        assert text(5.678) == 'I got: 5.678'


    # Exceptions seen

* I use the :ref:`variable<what is a variable?>` and an :ref:`f-string<what is string interpolation?>` to remove repetition of ``5.678``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 4-5

    def test_passing_a_float():
        a_float = 5.678
        # assert text(5.678) == 'I got: "5.678"'
        # assert text(5.678) == 'I got: 5.678'
        assert text(a_float) == f'I got: {a_float}'


    # Exceptions seen

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 19

    def test_passing_a_float():
        a_float = 5.678
        assert text(a_float) == f'I got: {a_float}'


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_passing_a_float'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can pass a float as input to a function<test_passing_a_float>`.

----

*********************************************************************************
test_passing_a_string
*********************************************************************************

Can I pass a string_ as input to a :ref:`function<what is a function?>`?.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test for a string_ (anything in :ref:`quotes`)

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 6-7

    def test_passing_a_float():
        a_float = 5.678
        assert text(a_float) == f'I got: {a_float}'


    def test_passing_a_string():
        assert text('hi') == f'I got: hello'


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert 'I got: hi' == 'I got: hello'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change my expectation to match reality

.. code-block:: python
  :lineno-start: 24
  :emphasize-lines: 2-3

  def test_passing_a_string():
      # assert text('hi') == f'I got: hello'
      assert text('hi') == f'I got: hi'


  # Exceptions seen

the test passes because Python_ uses the string_ representation of the :ref:`object<what is a class?>` in the curly braces ``{ }``

.. code-block:: python

  text(hi)
      text(the_input)
          the_input = hi
          return f'I got: {the_input}'
          return  'I got:  hi        '

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`variable<what is a variable?>` for ``'hi'``

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 2

    def test_passing_a_string():
        a_string = 'hi'
        # assert text('hi') == f'I got: hello'
        assert text('hi') == f'I got: hi'


    # Exceptions seen

* I use the :ref:`variable<what is a variable?>` and an :ref:`f-string<what is string interpolation?>` to remove repetition of ``'hi'``

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 2-5

    def test_passing_a_string():
        a_string = 'hi'
        # assert text('hi') == f'I got: hello'
        # assert text('hi') == f'I got: hi'
        assert text(a_string) == f'I got: {a_string}'


    # Exceptions seen

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 24

    def test_passing_a_string():
        a_string = 'hi'
        assert text(a_string) == f'I got: {a_string}'


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_passing_a_string'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can pass a string as input to a function<test_passing_a_string>`.

----

*********************************************************************************
test_passing_a_tuple
*********************************************************************************

Can I pass a tuple_ (anything in parentheses ``( )`` separated by a comma) as input to a :ref:`function<what is a function?>`?

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test for a tuple_

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 6-7

    def test_passing_a_string():
        a_string = 'hi'
        assert text(a_string) == f'I got: {a_string}'


    def test_passing_a_tuple():
        assert text((0, 1, 2, 'n')) == 'I got: (1, 2, 3, n)'


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert "I got: (0, 1, 2, 'n')"
                == 'I got: (1, 2, 3, n)'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the tuple_ in my expectation to match reality

.. code-block:: python
  :lineno-start: 29
  :emphasize-lines: 2-3
  :emphasize-text: "

  def test_passing_a_tuple():
      # assert text((0, 1, 2, 'n')) == 'I got: (1, 2, 3, n)'
      assert text((0, 1, 2, 'n')) == "I got: (0, 1, 2, 'n')"


  # Exceptions seen

the test passes because Python_ uses the string_ representation of the :ref:`object<what is a class?>` in the curly braces ``{ }``

.. code-block:: python

  text((0, 1, 2, 'n'))
      text(the_input)
          the_input = (0, 1, 2, 'n')
          return f'I got: {the_input    }'
          return  'I got:  (0, 1, 2, 'n')'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`variable<what is a variable?>` for ``(0, 1, 2, 'n')``

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 3-4

    def test_passing_a_tuple():
        a_tuple = (0, 1, 2, 'n')
        # assert text((0, 1, 2, 'n')) == 'I got: (0, 1, 2, 'n')'
        assert text((0, 1, 2, 'n')) == "I got: (0, 1, 2, 'n')"


    # Exceptions seen

* I use the :ref:`variable<what is a variable?>` and an :ref:`f-string<what is string interpolation?>` to remove repetition of ``(0, 1, 2, 'n')``

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 4-5

    def test_passing_a_tuple():
        a_tuple = (0, 1, 2, 'n')
        # assert text((0, 1, 2, 'n')) == 'I got: (0, 1, 2, 'n')'
        # assert text((0, 1, 2, 'n')) == "I got: (0, 1, 2, 'n')"
        assert text(a_tuple) == f'I got: {a_tuple}'


    # Exceptions seen

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 29

    def test_passing_a_tuple():
        a_tuple = (0, 1, 2, 'n')
        assert text(a_tuple) == f'I got: {a_tuple}'


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit --all --message 'add test_passing_a_tuple'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can pass a tuple as input to a function<test_passing_a_tuple>`.

----

*********************************************************************************
test_passing_a_list
*********************************************************************************

Can I pass a :ref:`list<what is a list?>` (anything in square brackets ``[ ]``) from a test to a :ref:`function?<what is a function?>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test for a :ref:`list<what is a list?>`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 6-7
    :emphasize-text: '

    def test_passing_a_tuple():
        a_tuple = (0, 1, 2, 'n')
        assert text(a_tuple) == f'I got: {a_tuple}'


    def test_passing_a_list():
        assert text([0, 1, 2, 'n']) == 'I got: [0, 1, 2, "n"]'


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    assert "I got: [0, 1, 2, 'n']"
        == 'I got: [0, 1, 2, "n"]'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the :ref:`list<what is a list?>` in my expectation to match reality

.. code-block:: python
  :lineno-start: 34
  :emphasize-lines: 2-3
  :emphasize-text: " '

  def test_passing_a_list():
      # assert text([0, 1, 2, 'n']) == 'I got: [0, 1, 2, "n"]'
      assert text([0, 1, 2, 'n']) == "I got: [0, 1, 2, 'n']"


  # Exceptions seen

the test passes because Python_ uses the string_ representation of the :ref:`object<what is a class?>` in the curly braces ``{ }``

.. code-block:: python

  text([0, 1, 2, 'n'])
      text(the_input)
          the_input = [0, 1, 2, 'n']
          return f'I got: {the_input    }'
          return  'I got:  [0, 1, 2, 'n']'

Python_ changed the :ref:`double quotes<quotes>` (``"``) in the :ref:`list<what is a list?>` to a :ref:`single quote<quotes>` (``'``).

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`variable<what is a variable?>` for ``[0, 1, 2, 'n']``

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 2

    def test_passing_a_list():
        a_list = [0, 1, 2, 'n']
        # assert text([0, 1, 2, 'n']) == 'I got: [0, 1, 2, "n"]'
        assert text([0, 1, 2, 'n']) == "I got: [0, 1, 2, 'n']"


    # Exceptions seen

* I use the :ref:`variable<what is a variable?>` and an :ref:`f-string<what is string interpolation?>` to remove repetition of ``[0, 1, 2, 'n']``

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 4-5

    def test_passing_a_list():
        a_list = [0, 1, 2, 'n']
        # assert text([0, 1, 2, 'n']) == 'I got: [0, 1, 2, "n"]'
        # assert text([0, 1, 2, 'n']) == "I got: [0, 1, 2, 'n']"
        assert text(a_list) == f'I got: {a_list}'


    # Exceptions seen

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 50

    def test_passing_a_list():
        a_list = [0, 1, 2, 'n']
        assert text(a_list) == f'I got: {a_list}'


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_passing_a_list'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can pass a list as input to a function<test_passing_a_list>`.

----

*********************************************************************************
test_passing_a_set
*********************************************************************************

Can I pass a set_ (anything in curly braces ``{ }``, not :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`) from a test to a :ref:`function?<what is a function?>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test for a set_

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 6-7
    :emphasize-text: '

    def test_passing_a_list():
        a_list = [0, 1, 2, 'n']
        assert text(a_list) == f'I got: {a_list}'


    def test_passing_a_set():
        assert text({0, 1, 2, 'n'}) == 'I got: {0, 1, 2, "n"}'


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert "I got: {0, 1, 2, 'n'}"
                == 'I got: {0, 1, 2, "n"}'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the set_ in my expectation to match reality

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 2-3
    :emphasize-text: " '

    def test_passing_a_set():
        # assert text({0, 1, 2, 'n'}) == 'I got: {0, 1, 2, "n"}'
        assert text({0, 1, 2, 'n'}) == "I got: {0, 1, 2, 'n'}"


    # Exceptions seen

* I use :kbd:`ctrl/command+s` (Windows_ & Linux_/MacOS_) to run the test a few times

  - if the result of ``text({0, 1, 2, 'n'})`` is equal to ``"I got: {0, 1, 2, 'n'}"`` the test passes because Python_ uses the string_ representation of the :ref:`object<what is a class?>` in the curly braces ``{ }``

    .. code-block:: python

      text({0, 1, 2, 'n'})
          text(the_input)
              the_input = {0, 1, 2, 'n'}
              return f'I got: {the_input    }'
              return  'I got:  {0, 1, 2, 'n'}'

  - if the result of ``text({0, 1, 2, 'n'})`` is NOT equal to ``"I got: {0, 1, 2, 'n'}"``, the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

    .. code-block:: python

      E       assert "I got: {0, 'n', 2, 1}"
                  == "I got: {0, 1, 2, 'n'}"

  Python_ cannot guarantee the order of the things in the set_ and the order matters for the :ref:`assertion<what is an assertion?>` that is comparing the strings_ because

  - these two are the same set

    .. code-block:: python

      {0, 'n', 2, 1} == {0, 1, 2, 'n'}

  - these two are not the same string

    .. code-block:: python

      "{0, 'n', 2, 1}" != "{0, 1, 2, 'n'}"

* I add a :ref:`variable<what is a variable?>` for ``{0, 1, 2, 'n'}``

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 2

    def test_passing_a_set():
        a_set = {0, 1, 2, 'n'}
        # assert text({0, 1, 2, 'n'}) == 'I got: {0, 1, 2, "n"}'
        assert text({0, 1, 2, 'n'}) == "I got: {0, 1, 2, 'n'}"


    # Exceptions seen

* I use the :ref:`variable<what is a variable?>` and an :ref:`f-string<what is string interpolation?>` to remove repetition of ``{0, 1, 2, 'n'}``

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 4-5

    def test_passing_a_set():
        a_set = {0, 1, 2, 'n'}
        # assert text({0, 1, 2, 'n'}) == 'I got: {0, 1, 2, "n"}'
        # assert text({0, 1, 2, 'n'}) == "I got: {0, 1, 2, 'n'}"
        assert text(a_set) == f'I got: {a_set}'


    # Exceptions seen

  - I use :kbd:`ctrl/command+s` (Windows_ & Linux_/MacOS_) to run the test a few times and the test stays green with no random failures because Python_ uses the string_ representation of the :ref:`object<what is a class?>` in the curly braces ``{ }``.
  - It can guarantee the order when I use a :ref:`variable<what is a variable?>` and the :ref:`f-string<what is string interpolation?>` to refer to the same exact set_.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 50

    def test_passing_a_set():
        a_set = {0, 1, 2, 'n'}
        assert text(a_set) == f'I got: {a_set}'


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit --all --message 'add test_passing_a_set'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can pass a set as input to a function<test_passing_a_set>`.

----

*********************************************************************************
test_passing_a_dictionary
*********************************************************************************

Can I pass a :ref:`dictionary (any key-value pairs in curly braces '{ }' separated by commas<what is a dictionary?>` as input to a :ref:`function<what is a function?>`?

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test for a :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 6-15
    :emphasize-text: "

    def test_passing_a_set():
        a_set = {0, 1, 2, 'n'}
        assert text(a_set) == f'I got: {a_set}'


    def test_passing_a_dictionary():
        reality = text({
            'key0': 'value0',
            'keyN': [0, 1, 2, 'n'],
        })
        my_expectation = (
            "I got: "
            "{key0: value0, keyN: [0, 1, 2, n]}"
        )
        assert reality == my_expectation


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    assert "I got: {'key..., 1, 2, 'n']}"
        == 'I got: {key0...[0, 1, 2, n]}'

  I want more detail in my error messages.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change ``my_expectation`` to match ``reality``

.. code-block:: python
  :lineno-start: 44
  :emphasize-lines: 8-9
  :emphasize-text: '

  def test_passing_a_dictionary():
      reality = text({
          'key0': 'value0',
          'keyN': [0, 1, 2, 'n'],
      })
      my_expectation = (
          "I got: "
          # "{key0: value0, keyN: [0, 1, 2, n]}"
          "{'key0': 'value0', 'keyN': [0, 1, 2, 'n']}"
      )
      assert reality == my_expectation


  # Exceptions seen

the test passes because Python_ uses the string_ representation of the :ref:`object<what is a class?>` in the curly braces ``{ }``

.. code-block:: python

  text({'key0': 'value0', 'keyN': [0, 1, 2, 'n'],})
      text(the_input)
          the_input = {'key0': 'value0', 'keyN': [0, 1, 2, 'n']}
          return f'I got: {the_input    }'
          return  "I got: {'key0': 'value0', 'keyN': [0, 1, 2, 'n']}"

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`variable<what is a variable?>` for ``{'key0': 'value0', 'keyN': [0, 1, 2, 'n'],}``

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 2-5

    def test_passing_a_dictionary():
        a_dictionary = {
            'key0': 'value0',
            'keyN': [0, 1, 2, 'n'],
        }
        reality = text({
            'key0': 'value0',
            'keyN': [0, 1, 2, 'n'],
        })
        my_expectation = (
            "I got: "
            # "{key0: value0, keyN: [0, 1, 2, n]}"
            "{'key0': 'value0', 'keyN': [0, 1, 2, 'n']}"
        )
        assert reality == my_expectation


    # Exceptions seen

* I use the :ref:`variable<what is a variable?>` and an :ref:`f-string<what is string interpolation?>` to remove repetition of ``{'key0': 'value0', 'keyN': [0, 1, 2, 'n'],}``

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 6-16

    def test_passing_a_dictionary():
        a_dictionary = {
            'key0': 'value0',
            'keyN': [0, 1, 2, 'n'],
        }
        # reality = text({
        #     'key0': 'value0',
        #     'keyN': [0, 1, 2, 'n'],
        # })
        # my_expectation = (
        #     "I got: "
        #     # "{key0: value0, keyN: [0, 1, 2, n]}"
        #     "{'key0': 'value0', 'keyN': [0, 1, 2, 'n']}"
        # )
        reality = text(a_dictionary)
        my_expectation = f'I got: {a_dictionary}'
        assert reality == my_expectation


    # Exceptions seen

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 56

    def test_passing_a_dictionary():
        a_dictionary = {
            'key0': 'value0',
            'keyN': [0, 1, 2, 'n'],
        }
        reality = text(a_dictionary)
        my_expectation = f'I got: {a_dictionary}'
        assert reality == my_expectation


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_passing_a_dictionary'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can pass a dictionary as input to a function<test_passing_a_dictionary>`.

----

*********************************************************************************
test_passing_a_class
*********************************************************************************

Can I pass any :ref:`object<everything is an object>` as input to a :ref:`function<what is a function?>`?

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a failing test to see what happens when I pass a :ref:`class <what is a class?>` from a test to the ``text`` :ref:`function<what is a function?>`, in ``test_telephone.py``

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 11-12

    def test_passing_a_dictionary():
        a_dictionary = {
            'key0': 'value0',
            'keyN': [0, 1, 2, 'n'],
        }
        reality = text(a_dictionary)
        my_expectation = f'I got: {a_dictionary}'
        assert reality == my_expectation


    def test_passing_a_class():
        assert text(object) == 'I got: object'


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert "I got: <class 'object'>"
                == 'I got: object'

  :ref:`object<everything is an object>` is the :ref:`mother class<what is a class?>` that all :ref:`Python classes<what is a class?>` come from, and :ref:`everything in Python is an object<everything is an object>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change my expectation to match reality

.. code-block:: python
  :lineno-start: 54
  :emphasize-lines: 2-3
  :emphasize-text: " '

  def test_passing_a_class():
      # assert text(object) == 'I got: object'
      assert text(object) == "I got: <class 'object'>"


  # Exceptions seen

the test passes because Python_ uses the string_ representation of the :ref:`object<what is a class?>` in the curly braces ``{ }``

.. code-block:: python

  text(object)
      text(the_input)
          the_input = object
          return f'I got: {the_input       }'
          return  "I got:  <class 'object'> "

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for :ref:`bool (the class for booleans)<what are booleans?>`

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 4

    def test_passing_a_class():
        # assert text(object) == 'I got: object'
        assert text(object) == "I got: <class 'object'>"
        assert text(bool) == 'I got: bool'


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert "I got: <class 'bool'>" == 'I got: bool'

* I change my expectation to match reality

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 4-5

    def test_passing_a_class():
        # assert text(object) == 'I got: object'
        assert text(object) == "I got: <class 'object'>"
        # assert text(bool) == 'I got: bool'
        assert text(bool) == "I got: <class 'bool'>"


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for int_ (the :ref:`class<what is a class?>` for whole numbers without decimals)

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 6

    def test_passing_a_class():
        # assert text(object) == 'I got: object'
        assert text(object) == "I got: <class 'object'>"
        # assert text(bool) == 'I got: bool'
        assert text(bool) == "I got: <class 'bool'>"
        assert text(int) == 'I got: int'


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert "I got: <class 'int'>" == 'I got: int'

* I change my expectation to match reality

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 6-7

    def test_passing_a_class():
        # assert text(object) == 'I got: object'
        assert text(object) == "I got: <class 'object'>"
        # assert text(bool) == 'I got: bool'
        assert text(bool) == "I got: <class 'bool'>"
        # assert text(int) == "I got: int"
        assert text(int) == "I got: <class 'int'>"


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for float_ (the :ref:`class<what is a class?>` for binary floating point decimal numbers)

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 8

    def test_passing_a_class():
        # assert text(object) == 'I got: object'
        assert text(object) == "I got: <class 'object'>"
        # assert text(bool) == 'I got: bool'
        assert text(bool) == "I got: <class 'bool'>"
        # assert text(int) == "I got: int"
        assert text(int) == "I got: <class 'int'>"
        assert text(float) == 'I got: float'


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert "I got: <class 'float'>" == 'I got: float'

* I change my expectation to match reality

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 8-9

    def test_passing_a_class():
        # assert text(object) == 'I got: object'
        assert text(object) == "I got: <class 'object'>"
        # assert text(bool) == 'I got: bool'
        assert text(bool) == "I got: <class 'bool'>"
        # assert text(int) == "I got: int"
        assert text(int) == "I got: <class 'int'>"
        # assert text(float) == 'I got: float'
        assert text(float) == "I got: <class 'float'>"


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for str_ (the :ref:`class<what is a class?>` for anything in :ref:`quotes`)

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 10

    def test_passing_a_class():
        # assert text(object) == 'I got: object'
        assert text(object) == "I got: <class 'object'>"
        # assert text(bool) == 'I got: bool'
        assert text(bool) == "I got: <class 'bool'>"
        # assert text(int) == "I got: int"
        assert text(int) == "I got: <class 'int'>"
        # assert text(float) == 'I got: float'
        assert text(float) == "I got: <class 'float'>"
        assert text(str) == 'I got: str'


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert "I got: <class 'str'>" == 'I got: str'

* I change my expectation to match reality

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 10-11

    def test_passing_a_class():
        # assert text(object) == 'I got: object'
        assert text(object) == "I got: <class 'object'>"
        # assert text(bool) == 'I got: bool'
        assert text(bool) == "I got: <class 'bool'>"
        # assert text(int) == "I got: int"
        assert text(int) == "I got: <class 'int'>"
        # assert text(float) == 'I got: float'
        assert text(float) == "I got: <class 'float'>"
        # assert text(str) == 'I got: str'
        assert text(str) == "I got: <class 'str'>"


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for tuple_ (the :ref:`class<what is a class?>` for anything in parentheses ``( )`` separated by a comma)

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 12

    def test_passing_a_class():
        # assert text(object) == 'I got: object'
        assert text(object) == "I got: <class 'object'>"
        # assert text(bool) == 'I got: bool'
        assert text(bool) == "I got: <class 'bool'>"
        # assert text(int) == "I got: int"
        assert text(int) == "I got: <class 'int'>"
        # assert text(float) == 'I got: float'
        assert text(float) == "I got: <class 'float'>"
        # assert text(str) == 'I got: str'
        assert text(str) == "I got: <class 'str'>"
        assert text(tuple) == 'I got: tuple'


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert "I got: <class 'tuple'>" == 'I got: tuple'

* I change my expectation to match reality

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 12-13

    def test_passing_a_class():
        # assert text(object) == 'I got: object'
        assert text(object) == "I got: <class 'object'>"
        # assert text(bool) == 'I got: bool'
        assert text(bool) == "I got: <class 'bool'>"
        # assert text(int) == "I got: int"
        assert text(int) == "I got: <class 'int'>"
        # assert text(float) == 'I got: float'
        assert text(float) == "I got: <class 'float'>"
        # assert text(str) == 'I got: str'
        assert text(str) == "I got: <class 'str'>"
        # assert text(tuple) == 'I got: tuple'
        assert text(tuple) == "I got: <class 'tuple'>"


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for :ref:`list (the class for anything in square brackets '[ ]')<what is a list?>`

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 14

    def test_passing_a_class():
        # assert text(object) == 'I got: object'
        assert text(object) == "I got: <class 'object'>"
        # assert text(bool) == 'I got: bool'
        assert text(bool) == "I got: <class 'bool'>"
        # assert text(int) == "I got: int"
        assert text(int) == "I got: <class 'int'>"
        # assert text(float) == 'I got: float'
        assert text(float) == "I got: <class 'float'>"
        # assert text(str) == 'I got: str'
        assert text(str) == "I got: <class 'str'>"
        # assert text(tuple) == 'I got: tuple'
        assert text(tuple) == "I got: <class 'tuple'>"
        assert text(list) == 'I got: list'


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert "I got: <class 'tuple'>" == 'I got: tuple'

* I change my expectation to match reality

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 14-15

    def test_passing_a_class():
        # assert text(object) == 'I got: object'
        assert text(object) == "I got: <class 'object'>"
        # assert text(bool) == 'I got: bool'
        assert text(bool) == "I got: <class 'bool'>"
        # assert text(int) == "I got: int"
        assert text(int) == "I got: <class 'int'>"
        # assert text(float) == 'I got: float'
        assert text(float) == "I got: <class 'float'>"
        # assert text(str) == 'I got: str'
        assert text(str) == "I got: <class 'str'>"
        # assert text(tuple) == 'I got: tuple'
        assert text(tuple) == "I got: <class 'tuple'>"
        # assert text(list) == 'I got: list'
        assert text(list) == "I got: <class 'list'>"


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for set_ (the :ref:`class<what is a class?>` anything in curly braces ``{ }``, not :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`)

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 16

    def test_passing_a_class():
        # assert text(object) == 'I got: object'
        assert text(object) == "I got: <class 'object'>"
        # assert text(bool) == 'I got: bool'
        assert text(bool) == "I got: <class 'bool'>"
        # assert text(int) == "I got: int"
        assert text(int) == "I got: <class 'int'>"
        # assert text(float) == 'I got: float'
        assert text(float) == "I got: <class 'float'>"
        # assert text(str) == 'I got: str'
        assert text(str) == "I got: <class 'str'>"
        # assert text(tuple) == 'I got: tuple'
        assert text(tuple) == "I got: <class 'tuple'>"
        # assert text(list) == 'I got: list'
        assert text(list) == "I got: <class 'list'>"
        assert text(set) == 'I got: set'


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert "I got: <class 'set'>" == 'I got: set'

* I change my expectation to match reality

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 16-17

    def test_passing_a_class():
        # assert text(object) == 'I got: object'
        assert text(object) == "I got: <class 'object'>"
        # assert text(bool) == 'I got: bool'
        assert text(bool) == "I got: <class 'bool'>"
        # assert text(int) == "I got: int"
        assert text(int) == "I got: <class 'int'>"
        # assert text(float) == 'I got: float'
        assert text(float) == "I got: <class 'float'>"
        # assert text(str) == 'I got: str'
        assert text(str) == "I got: <class 'str'>"
        # assert text(tuple) == 'I got: tuple'
        assert text(tuple) == "I got: <class 'tuple'>"
        # assert text(list) == 'I got: list'
        assert text(list) == "I got: <class 'list'>"
        # assert text(set) == 'I got: set'
        assert text(set) == "I got: <class 'set'>"


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for :ref:`dict (the class for key-value pairs in curly braces '{ }' separated by commas)<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 18

    def test_passing_a_class():
        # assert text(object) == 'I got: object'
        assert text(object) == "I got: <class 'object'>"
        # assert text(bool) == 'I got: bool'
        assert text(bool) == "I got: <class 'bool'>"
        # assert text(int) == "I got: int"
        assert text(int) == "I got: <class 'int'>"
        # assert text(float) == 'I got: float'
        assert text(float) == "I got: <class 'float'>"
        # assert text(str) == 'I got: str'
        assert text(str) == "I got: <class 'str'>"
        # assert text(tuple) == 'I got: tuple'
        assert text(tuple) == "I got: <class 'tuple'>"
        # assert text(list) == 'I got: list'
        assert text(list) == "I got: <class 'list'>"
        # assert text(set) == 'I got: set'
        assert text(set) == "I got: <class 'set'>"
        assert text(dict) == 'I got: dict'


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert "I got: <class 'dict'>" == 'I got: dict'

* I change my expectation to match reality

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 18-19

    def test_passing_a_class():
        # assert text(object) == 'I got: object'
        assert text(object) == "I got: <class 'object'>"
        # assert text(bool) == 'I got: bool'
        assert text(bool) == "I got: <class 'bool'>"
        # assert text(int) == "I got: int"
        assert text(int) == "I got: <class 'int'>"
        # assert text(float) == 'I got: float'
        assert text(float) == "I got: <class 'float'>"
        # assert text(str) == 'I got: str'
        assert text(str) == "I got: <class 'str'>"
        # assert text(tuple) == 'I got: tuple'
        assert text(tuple) == "I got: <class 'tuple'>"
        # assert text(list) == 'I got: list'
        assert text(list) == "I got: <class 'list'>"
        # assert text(set) == 'I got: set'
        assert text(set) == "I got: <class 'set'>"
        # assert text(dict) == 'I got: dict'
        assert text(dict) == "I got: <class 'dict'>"


    # Exceptions seen

  the test passes because Python_ uses the string_ representation of the :ref:`object<what is a class?>` in the curly braces ``{ }``

  .. code-block:: python

    text(dict)
        text(the_input)
            the_input = dict
            return f'I got: {the_input     }'
            return  "I got:  <class 'dict'> "

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 54

    def test_passing_a_class():
        assert text(object) == "I got: <class 'object'>"
        assert text(bool) == "I got: <class 'bool'>"
        assert text(int) == "I got: <class 'int'>"
        assert text(float) == "I got: <class 'float'>"
        assert text(str) == "I got: <class 'str'>"
        assert text(tuple) == "I got: <class 'tuple'>"
        assert text(list) == "I got: <class 'list'>"
        assert text(set) == "I got: <class 'set'>"
        assert text(dict) == "I got: <class 'dict'>"


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit --all --message 'add test_passing_a_class'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can pass any object as input to a function<test_passing_a_class>`.

----

*********************************************************************************
separate and equal
*********************************************************************************

So far all :ref:`functions<what is a function?>` I have written have been in the same file_ as the tests, some are even in the same :ref:`function<what is a function?>` as the :ref:`assertions<what is an assertion?>` of the tests.

In earlier tests I found it better to keep :ref:`functions<what is a function?>` outside of :ref:`functions<what is a function?>` so that anything could call them from outside.

I can also place them in other :ref:`modules<what is a module?>` then use the `import statement`_ to bring in the :ref:`function<what is a function?>` so I can test it. This helps me keep tests and solutions separate. It also means I can send tests only, solutions only or both.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I change the :ref:`assertion<what is an assertion?>` to call the ``text`` :ref:`function<what is a function?>` of the ``telephone`` :ref:`module<what is a module?>` in the ``src`` folder_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-9

    def text(the_input):
        return f'I got: {the_input}'


    def test_passing_none():
        # assert text(None) == 'I got: None'
        reality = src.telephone.text(None)
        my_expectation = 'I got: None'
        assert reality == my_expectation


    def test_passing_booleans():

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'src' is not defined

  because there is nothing with that name in ``test_telephone.py``.


----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an `import statement`_ at the top of ``test_telephone.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src


    def text(the_input):

  the terminal_ is my friend, and shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

  .. code-block:: python

    E   ModuleNotFoundError: No module named 'src'

  because there is nothing named ``src`` in the project.

* I add :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 5
    :emphasize-text: ModuleNotFoundError

    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # ModuleNotFoundError

* I go to the other terminal_

* I use mkdir_ to make a folder_ named ``src``

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir src

  the terminal_ goes back to the command line.

* I go back to the terminal_ where the tests are running

* I use :kbd:`ctrl/command+s` (Windows_ & Linux_/MacOS_) in ``test_telephone.py`` to run the test again, and the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src' has no attribute 'telephone'

  because there is nothing named ``telephone`` in the ``src`` folder_.

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 6
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # ModuleNotFoundError
    # AttributeError

* I change the `import statement`_ to make it import ``telephone.py`` from the ``src`` folder_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    # import src
    import src.telephone


    def text(the_input):

  the terminal_ is my friend, and shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

  .. code-block:: python

    E   ModuleNotFoundError: No module named 'src.telephone'

  because Python_ cannot find ``telephone.py`` in the ``src`` folder_ since I have not made it yet.

* I go to the other terminal_

* I use touch_ to make ``telephone.py`` in the ``src`` folder_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 1

        touch src/telephone.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        New-Item src/telephone.py

  the terminal_ goes back to the command line.

* I go back to the terminal_ where the tests are running and it shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.telephone' has no attribute 'text'

  because ``telephone.py`` in the ``src`` folder_ does not have anything named ``text`` inside it.

* I open ``telephone.py`` from the ``src`` folder_
* I add a copy of the ``text`` :ref:`function<what is a function?>` to ``telephone.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def text(the_input):
        return f'I got: {the_input}'

  the test passes because

  - when ``import src.telephone`` runs, Python_ brings in an :ref:`object<what is a class?>` for the ``telephone.py`` file_ from the ``src`` folder_ so I can use it in ``test_telephone.py`` as ``src.telephone``
  - when ``src.telephone.text(None)`` runs, Python_ calls the ``text`` :ref:`function<what is a function?>` from the :ref:`object<what is a class?>` it imported for the ``telephone.py`` file_ from the ``src`` folder_ (``src.telephone``)

  I think of ``src.telephone.text`` like an address

  .. code-block:: shell

    src
    └── telephone.py
        └── def text(the_input):
                return f'I got: {the input}'

  - ``text`` is something in ``telephone``, in this case it is a :ref:`function<what is a function?>` in ``telephone``
  - ``telephone`` is something in ``src``, in this case it is ``telephone.py`` (a :ref:`module<what is a module?>`) in the ``src`` folder_
  - ``src`` is something Python_ can import (a :ref:`module<what is a module?>`, `Python package`_ or folder_)


----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines from ``test_telephone.py``

  .. code-block:: python
    :linenos:

    import src.telephone


    def text(the_input):
        return f'I got: {the_input}'


    def test_passing_none():
        reality = src.telephone.text(None)
        my_expectation = 'I got: None'
        assert reality == my_expectation


    def test_passing_booleans():

* I change the call in the first :ref:`assertion<what is an assertion?>` of :ref:`test_passing_booleans` to ``src.telephone.text``

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 2-5

    def test_passing_booleans():
        # assert text(False) == 'I got: False'
        reality = src.telephone.text(False)
        my_expectation = 'I got: False'
        assert reality == my_expectation
        assert text(True) == 'I got: True'


    def test_passing_an_integer():

  the test is still green because when ``src.telephone.text`` is called, Python_ follows this path

  .. code-block:: shell

      src
      └── telephone.py
          └── def text(the_input):
                  return f'I got: {the input}'

  then uses the string_ representation of the :ref:`object<what is a class?>` in the curly braces ``{ }``

  .. code-block:: python

    text(None)
        text(the_input)
            the_input = None
            return f'I got: {the_input}'
            return  'I got:  None      '

* I make the same change for the next :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 6-9

    def test_passing_booleans():
        # assert text(False) == 'I got: False'
        reality = src.telephone.text(False)
        my_expectation = 'I got: False'
        assert reality == my_expectation
        # assert text(True) == 'I got: True'
        reality = src.telephone.text(True)
        my_expectation = 'I got: True'
        assert reality == my_expectation


    def test_passing_an_integer():

  still green.

* I remove the commented lines from :ref:`test_passing_booleans`

  .. code-block:: python
    :lineno-start: 14

    def test_passing_booleans():
        reality = src.telephone.text(False)
        my_expectation = 'I got: False'
        assert reality == my_expectation

        reality = src.telephone.text(True)
        my_expectation = 'I got: True'
        assert reality == my_expectation


    def test_passing_an_integer():

* I change the call in the :ref:`assertion<what is an assertion?>` of :ref:`test_passing_an_integer` to ``src.telephone.text``

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 3-6

    def test_passing_an_integer():
        an_integer = 1234
        # assert text(an_integer) == f'I got: {an_integer}'
        reality = src.telephone.text(an_integer)
        my_expectation = f'I got: {an_integer}'
        assert reality == my_expectation


    def test_passing_a_float():

  green.

* I remove the commented line from :ref:`test_passing_an_integer`

  .. code-block:: python
    :lineno-start: 24

    def test_passing_an_integer():
        an_integer = 1234

        reality = src.telephone.text(an_integer)
        my_expectation = f'I got: {an_integer}'
        assert reality == my_expectation


    def test_passing_a_float():

* I change the call in the :ref:`assertion<what is an assertion?>` of :ref:`test_passing_a_float`

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 3-6

    def test_passing_a_float():
        a_float = 5.678
        # assert text(a_float) == f'I got: {a_float}'
        reality = src.telephone.text(a_float)
        my_expectation = f'I got: {a_float}'
        assert reality == my_expectation


    def test_passing_a_string():

  still green because when ``src.telephone.text`` is called, Python_ follows this path

  .. code-block:: shell

      src
      └── telephone.py
          └── def text(the_input):
                  return f'I got: {the input}'

  then uses the string_ representation of the :ref:`object<what is a class?>` in the curly braces ``{ }``

  .. code-block:: python

    a_float = 5.678

    text(a_float)
        text(the_input)
            the_input = 5.678
            return f'I got: {the_input}'
            return  'I got:  5.678     '

* I remove the commented line

  .. code-block:: python
    :lineno-start: 32

    def test_passing_a_float():
        a_float = 5.678

        reality = src.telephone.text(a_float)
        my_expectation = f'I got: {a_float}'
        assert reality == my_expectation


    def test_passing_a_string():

  the test is still green.

* I change the call in the :ref:`assertion<what is an assertion?>` of :ref:`test_passing_a_string`

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 3-6

    def test_passing_a_string():
        a_string = 'hi'
        # assert text(a_string) == f'I got: {a_string}'
        reality = src.telephone.text(a_string)
        my_expectation = f'I got: {a_string}'
        assert reality == my_expectation


    def test_passing_a_tuple():

* I remove the commented line

  .. code-block:: python
    :lineno-start: 40

    def test_passing_a_string():
        a_string = 'hi'

        reality = src.telephone.text(a_string)
        my_expectation = f'I got: {a_string}'
        assert reality == my_expectation


    def test_passing_a_tuple():

* I change the call in the :ref:`assertion<what is an assertion?>` of :ref:`test_passing_a_tuple`

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 3-6

    def test_passing_a_tuple():
        a_tuple = (0, 1, 2, 'n')
        # assert text(a_tuple) == f'I got: {a_tuple}'
        reality = src.telephone.text(a_tuple)
        my_expectation = f'I got: {a_tuple}'
        assert reality == my_expectation


    def test_passing_a_list():

  still green.

* I remove the commented line

  .. code-block:: python
    :lineno-start: 48

    def test_passing_a_tuple():
        a_tuple = (0, 1, 2, 'n')

        reality = src.telephone.text(a_tuple)
        my_expectation = f'I got: {a_tuple}'
        assert reality == my_expectation


    def test_passing_a_list():

* I change the call in the :ref:`assertion<what is an assertion?>` of :ref:`test_passing_a_list`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 3-6

    def test_passing_a_list():
        a_list = [0, 1, 2, 'n']
        # assert text(a_list) == f'I got: {a_list}'
        reality = src.telephone.text(a_list)
        my_expectation = f'I got: {a_list}'
        assert reality == my_expectation


    def test_passing_a_set():

  green.

* I remove the commented line

  .. code-block:: python
    :lineno-start: 56

    def test_passing_a_list():
        a_list = [0, 1, 2, 'n']

        reality = src.telephone.text(a_list)
        my_expectation = f'I got: {a_list}'
        assert reality == my_expectation


    def test_passing_a_set():

* I change the call in the :ref:`assertion<what is an assertion?>` of :ref:`test_passing_a_set`

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 3-6

    def test_passing_a_set():
        a_set = {0, 1, 2, 'n'}
        # assert text(a_set) == f'I got: {a_set}'
        reality = src.telephone.text(a_set)
        my_expectation = f'I got: {a_set}'
        assert reality == my_expectation


    def test_passing_a_dictionary():

  still green.

* I remove the commented line

  .. code-block:: python
    :lineno-start: 64

    def test_passing_a_set():
        a_set = {0, 1, 2, 'n'}

        reality = src.telephone.text(a_set)
        my_expectation = f'I got: {a_set}'
        assert reality == my_expectation


    def test_passing_a_dictionary():

* I change the call in ``reality`` for :ref:`test_passing_a_dictionary`

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 6-7

    def test_passing_a_dictionary():
        a_dictionary = {
            'key0': 'value0',
            'keyN': [0, 1, 2, 'n'],
        }
        # reality = text(a_dictionary)
        reality = src.telephone.text(a_dictionary)
        my_expectation = f'I got: {a_dictionary}'
        assert reality == my_expectation


    def test_passing_a_class():

  the test is still green because when ``src.telephone.text`` is called, Python_ follows this path

  .. code-block:: shell

      src
      └── telephone.py
          └── def text(the_input):
                  return f'I got: {the input}'

  then uses the string_ representation of the :ref:`object<what is a class?>` in the curly braces ``{ }``

  .. code-block:: python

    a_dictionary = {
        'key0': 'value0',
        'keyN': [0, 1, 2, 'n'],
    }

    text(a_dictionary)
        text(the_input)
            the_input = {
                'key0': 'value0',
                'keyN': [0, 1, 2, 'n'],
            }
            return f'I got: {the_input}'
            return  "I got: {'key0': 'value0', 'keyN': [0, 1, 2, 'n']}"

* I remove the commented line

  .. code-block:: python
    :lineno-start: 72

    def test_passing_a_dictionary():
        a_dictionary = {
            'key0': 'value0',
            'keyN': [0, 1, 2, 'n'],
        }

        reality = src.telephone.text(a_dictionary)
        my_expectation = f'I got: {a_dictionary}'
        assert reality == my_expectation


    def test_passing_a_class():

* I change the calls in the :ref:`assertions<what is an assertion?>` of :ref:`test_passing_a_class`

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 2-5, 7-10, 12-15, 17-20, 22-25, 27-30, 32-35, 37-40, 42-45

    def test_passing_a_class():
        # assert text(object) == "I got: <class 'object'>"
        reality = src.telephone.text(object)
        my_expectation = "I got: <class 'object'>"
        assert reality == my_expectation

        # assert text(bool) == "I got: <class 'bool'>"
        reality = src.telephone.text(bool)
        my_expectation = "I got: <class 'bool'>"
        assert reality == my_expectation

        # assert text(int) == "I got: <class 'int'>"
        reality = src.telephone.text(int)
        my_expectation = "I got: <class 'int'>"
        assert reality == my_expectation

        # assert text(float) == "I got: <class 'float'>"
        reality = src.telephone.text(float)
        my_expectation = "I got: <class 'float'>"
        assert reality == my_expectation

        # assert text(str) == "I got: <class 'str'>"
        reality = src.telephone.text(str)
        my_expectation = "I got: <class 'str'>"
        assert reality == my_expectation

        # assert text(tuple) == "I got: <class 'tuple'>"
        reality = src.telephone.text(tuple)
        my_expectation = "I got: <class 'tuple'>"
        assert reality == my_expectation

        # assert text(list) == "I got: <class 'list'>"
        reality = src.telephone.text(list)
        my_expectation = "I got: <class 'list'>"
        assert reality == my_expectation

        # assert text(set) == "I got: <class 'set'>"
        reality = src.telephone.text(set)
        my_expectation = "I got: <class 'set'>"
        assert reality == my_expectation

        # assert text(dict) == "I got: <class 'dict'>"
        reality = src.telephone.text(dict)
        my_expectation = "I got: <class 'dict'>"
        assert reality == my_expectation


    # Exceptions seen

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start:

    def test_passing_a_class():
        reality = src.telephone.text(object)
        my_expectation = "I got: <class 'object'>"
        assert reality == my_expectation

        reality = src.telephone.text(bool)
        my_expectation = "I got: <class 'bool'>"
        assert reality == my_expectation

        reality = src.telephone.text(int)
        my_expectation = "I got: <class 'int'>"
        assert reality == my_expectation

        reality = src.telephone.text(float)
        my_expectation = "I got: <class 'float'>"
        assert reality == my_expectation

        reality = src.telephone.text(str)
        my_expectation = "I got: <class 'str'>"
        assert reality == my_expectation

        reality = src.telephone.text(tuple)
        my_expectation = "I got: <class 'tuple'>"
        assert reality == my_expectation

        # assert text(list) == "I got: <class 'list'>"
        reality = src.telephone.text(list)
        my_expectation = "I got: <class 'list'>"
        assert reality == my_expectation

        # assert text(set) == "I got: <class 'set'>"
        reality = src.telephone.text(set)
        my_expectation = "I got: <class 'set'>"
        assert reality == my_expectation

        # assert text(dict) == "I got: <class 'dict'>"
        reality = src.telephone.text(dict)
        my_expectation = "I got: <class 'dict'>"
        assert reality == my_expectation


    # Exceptions seen
    # AssertionError
    # NameError
    # ModuleNotFoundError
    # AttributeError

* I remove the ``text`` :ref:`function<what is a function?>` from ``test_telephone.py``

  .. code-block:: python
    :linenos:

    import src.telephone


    def test_passing_none():
        reality = src.telephone.text(None)
        my_expectation = 'I got: None'
        assert reality == my_expectation


    def test_passing_booleans():

  all the tests are still green because all the calls to the ``text`` :ref:`function<what is a function?>` that was in ``test_telephone.py`` are now to the ``text`` :ref:`function<what is a function?>` in ``telephone.py`` in the ``src`` folder_. When ``src.telephone.text`` is called Python_ follows this path

  .. code-block:: shell

      src
      └── telephone.py
          └── def text(the_input):
                  return f'I got: {the input}'

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'separate solution from tests'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can write solutions in a different module from the tests<separate and equal>`.

----

*********************************************************************************
test_telephone
*********************************************************************************

Now that the solution is separate from the tests, I can write the program_ that makes the tests pass without looking at ``test_telephone.py``.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I close ``test_telephone.py``

* I delete the text in ``telephone.py`` and the terminal_ shows 9 failures. I start with the last :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    FAILED ...::test_passing_none -
        AttributeError: module 'src.telephone'
                        has no attribute 'text'
    FAILED ...::test_passing_booleans -
        AttributeError: module 'src.telephone'
                        has no attribute 'text'
    FAILED ...::test_passing_an_integer -
        AttributeError: module 'src.telephone'
                        has no attribute 'text'
    FAILED ...::test_passing_a_float -
        AttributeError: module 'src.telephone'
                        has no attribute 'text'
    FAILED ...::test_passing_a_string -
        AttributeError: module 'src.telephone'
                        has no attribute 'text'
    FAILED ...::test_passing_a_tuple -
        AttributeError: module 'src.telephone'
                        has no attribute 'text'
    FAILED ...::test_passing_a_list -
        AttributeError: module 'src.telephone'
                        has no attribute 'text'
    FAILED ...::test_passing_a_set -
        AttributeError: module 'src.telephone'
                        has no attribute 'text'
    FAILED ...::test_passing_a_dictionary -
        AttributeError: module 'src.telephone'
                        has no attribute 'text'
    FAILED ...::test_passing_a_class -
        AttributeError: module 'src.telephone'
                        has no attribute 'text'
    =================== 10 failed in A.BCs ===================


  Can you make the tests pass without looking at how I solve it below? You can come back to compare solutions when you are done or if you get stuck.

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

  .. code-block:: python

    NameError: name 'text' is not defined

* I point it to :ref:`None (the simplest object)<what is None?>` to define it

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    # text
    text = None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  because ``text`` points to :ref:`None<what is None?>` and :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`.

* I make ``text`` a :ref:`function<what is a function?>` to make it :ref:`callable<how to make a function>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-4

    # text
    # text = None
    def text():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: text() takes 0 positional arguments
               but 1 was given

  because this :ref:`function definition<how to make a function that takes input>` does not allow any inputs, the parentheses are empty.

* I :ref:`make the function take input<how to make a function that takes input>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    # text
    # text = None
    # def text():
    def text(value):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert None == "I got: <class 'object'>"

* I copy the string_ from the terminal_ and paste it in the :ref:`return statement<the return statement>` to match the expectation of the test

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    # text
    # text = None
    # def text():
    def text(value):
        # return None
        return "I got: <class 'object'>"

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert "I got: <class 'object'>"
                == "I got: <class 'bool'>"

* I change the :ref:`return statement<the return statement>` to see the difference between the input and the expected output (remember :ref:`the identity function?<test_identity_function>`)

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    # text
    # text = None
    # def text():
    def text(value):
        # return None
        # return "I got: <class 'object'>"
        return value

  the test summary info shows that every test has :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-text: got:

    FAILED ...::test_passing_none -
        AssertionError: assert None == 'I got: None'
    FAILED ...::test_passing_booleans -
        AssertionError: assert False == 'I got: False'
    FAILED ...::test_passing_an_integer -
        AssertionError: assert 1234 == 'I got: 1234'
    FAILED ...::test_passing_a_float -
        AssertionError: assert 5.678 == 'I got: 5.678'
    FAILED ...::test_passing_a_string -
        AssertionError: assert 'hi' == 'I got: hi'
    FAILED ...::test_passing_a_tuple -
        assert (0, 1, 2, 'n') == "I got: (0, 1, 2, 'n')"
    FAILED ...::test_passing_a_list -
        assert [0, 1, 2, 'n'] == "I got: [0, 1, 2, 'n']"
    FAILED ...::test_passing_a_set -
        assert {0, 1, 2, 'n'} == "I got: {0, 1, 2, 'n'}"
    FAILED ...::test_passing_a_dictionary -
        assert {'key0': 'value0', 'keyN': [0, 1, 2, 'n']}
    == "I got: {'key0': 'value0',...
    FAILED ...::test_passing_a_class -
        assert <class 'object'> == "I got: <class 'object'>"

  they all expect the input (``value``) as part of the message

* I add a :ref:`return statement<the return statement>` with an :ref:`f-string<what is string interpolation?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-8

    # text
    # text = None
    # def text():
    def text(value):
        # return None
        # return "I got: <class 'object'>"
        # return value
        return f'I got: {value}'

  and all the tests are passing! I am a programmer!!

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def text(value):
        return f'I got: {value}'

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit --all --message 'test telephone'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``telephone.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``telephone``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

----

*********************************************************************************
review
*********************************************************************************

Here are the tests I ran to see what happens when I pass :ref:`objects<what is a class?>` from a test to a program_ and place them in an :ref:`f-string<what is string interpolation?>` which is one way to do :ref:`string interpolation<what is string interpolation?>`

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
* :ref:`TypeError<what causes TypeError?>`
* :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`
* :ref:`AttributeError<what causes AttributeError?>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<telephone: tests and solution>`

----

*************************************************************************************
what is next?
*************************************************************************************

You now know:

* :ref:`how to make a Python test driven development environment manually`
* :ref:`what a Python module is<what is a module?>`
* :ref:`how to run tests automatically`
* :ref:`what causes AssertionError<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to make a person with strings`
* :ref:`how to make functions that take input<functions that take input>`
* :ref:`what causes TypeError?`
* :ref:`how to place values in strings<telephone>`

:ref:`would you like to test making a person with f-strings?<how to make a person with f-strings>`

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