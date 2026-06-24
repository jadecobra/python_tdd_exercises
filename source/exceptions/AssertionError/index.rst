.. meta::
  :description: Step-by-step beginner Python TDD tutorial that teaches AssertionError by deliberately triggering it with bare `assert`. See exactly why a bare comparison like `1 + 1 == 11` (or reality == my expectation) does not fail the test or raise an error—Python just evaluates it and continues—while `assert` turns a false result into AssertionError and stops. Understand the pytest output beginners actually see on bare asserts ("E   assert False is True", "E       assert 0 != 0.0", collection ERROR vs FAILED, and "no tests ran" when there are no `test_*` functions yet). Master `=` (assignment) vs `==` (equality) and especially `is` / `is not` (identity, same object) vs `==` / `!=` (value equality). Concrete examples with None, True, False, 0 vs 0.0 (0 == 0.0 is True but 0 is not 0.0), strings, lists, dicts, sets, tuples using only bare `assert`. Learn to group assertions in functions so pytest names the tests and gives clear failure messages instead of "no tests ran". Full project setup with `uv init`, `tests/__init__.py` package, `uv add --requirement requirements.txt` (pytest + pytest-watcher), `uv run pytest-watcher . --now`, `git add` + `git commit --all --message` after every change, and the complete red-green-refactor cycle (including "remove the commented lines" and turning top-level asserts into `def test_*`). Perfect for absolute beginners learning Python testing, why bare expressions are ignored, pytest collection rules, None/True/False/0 identity gotchas, and how assertions control test outcomes.
  :keywords: Jacob Itegboje, Pumping Python, python assertionerror, AssertionError python, what causes AssertionError in python, python assert statement, assert statement python for beginners, how does assert work python, python assert tutorial, TDD for beginners python, red green refactor python, red green refactor cycle, uv pytest-watcher, pytest-watcher uv, uv run pytest-watcher . --now, difference between = and == python, assignment vs equality python, python is vs ==, object identity vs value equality python, python is not vs !=, is None vs == None python, python None identity, python is not None, unexpectedly identical None, AssertionError unexpectedly identical, AssertionError True is not false, True is not false python, assert 0 is 0.0, 0 is not 0.0 python, why is 0 == 0.0 but 0 is not 0.0, 0 == 0.0 is True python, python 0 is not False, an integer is not False, python 0 is not True, testing None True False python, bare comparison does not fail test, reality == my_expectation still green, why doesn't == fail my python test, python assert makes test fail, python assert "DO NOT CONTINUE if false", setting up tests directory python, tests __init__.py python, python tests package structure, common python beginner AssertionError, AssertionError 0 == 0.0, assert 0 != 0.0, python tdd None, python singleton is, python falsy is not False, a list is not None, a dict is not False, python test driven development assert, how to cause AssertionError, python assertions expectations vs reality, what is an assertion python, common python test gotchas None True False, python 0 == 0.0 identity equality, python why does my test not fail when I write ==, python bare expression vs assert, python assert turns false into error, python tdd uv init, pytest-watcher, python None is not False, True is not None test, will_not_run, test_failure, no tests ran pytest, collected items pytest, functions for tests pytest, test_ prefix pytest, python identity vs equality tutorial

.. include:: ../../links.rst

.. _AssertionError: https://docs.python.org/3/library/exceptions.html?highlight=AssertionError#AssertionError
.. _assert: https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement
.. _assert statement: assert_
.. _assertion: assert_
.. _assertions: assert_
.. _assert statements: assert_
.. _assert keyword: assert_
.. _assert method: https://docs.python.org/3/library/unittest.html#assert-methods
.. _assert methods: `assert method`_

#################################################################################
what is an assertion?
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/jxbttz7R0ho?si=Oiv1Y0WPwQhlw5i9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

An :ref:`assertion<what is an assertion?>` or `assert statement`_ is a way for me to tell Python_, "DO NOT CONTINUE, if this statement is False", or said a different way "GO TO THE NEXT LINE, ONLY if this statement is True".

I use assertions_ in tests when making a program_ to make sure something is :ref:`True<test_what_is_true>` about the program_ before I continue building. I use them to test ideas, without worrying about if I will remember the ideas later. I use them to test how programs_ behave, for example when given inputs.

Assertions_ can help catch things that make tests that were passing, start failing when I add new lines of code. They help me answer 2 questions

* what is the same?
* what is different?

The difference between my expectations (tests and ideas) and reality (what happens when the program_ runs), tells me what to change to make them match. The closer my program_ is to reality, the better.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/assertion_error/test_assertion_error.py
  :language: python
  :linenos:

*********************************************************************************
questions about AssertionError
*********************************************************************************

Questions to think about as I go through the chapter

* :ref:`what is an assertion?<what is an assertion?>`
* :ref:`what causes AssertionError?<what causes AssertionError?>`
* :ref:`how can I test if something is NOT the same object as None?<test_assertion_error_w_none>`
* :ref:`how can I test if something is the same object as None?<test_assertion_error_w_none>`
* :ref:`how can I test if something is the same object as False?<test_assertion_error_w_false>`
* :ref:`how can I test if something is NOT the same object as False?<test_assertion_error_w_false>`
* :ref:`how can I test if something is the same object as True?<test_assertion_error_w_true>`
* :ref:`how can I test if something is NOT the same object as True?<test_assertion_error_w_true>`
* :ref:`how can I test if two things are not equal?<test_assertion_error_w_equality>`
* :ref:`how can I test if two things are equal?<test_assertion_error_w_equality>`
* :ref:`what is the difference between is and equal<test_assertion_error_w_is_vs_equal>`

----

*********************************************************************************
start the project
*********************************************************************************

* I name this project ``assertion_error``
* I open a terminal_
* I `change directory`_ to the ``assertion_error`` folder_ in the ``pumping_python`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd assertion_error

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: assertion_error

  there is no folder_ with the name ``assertion_error`` in this folder_.

* I use uv_ to make a directory_ for the project and initialize it

  .. code-block:: python
    :emphasize-lines: 1

    uv init assertion_error

  the terminal_ shows

  .. code-block:: shell

    Initialized project `assertion-error`
    at `.../pumping_python/assertion_error`

  then goes back to the command line.

* I change directory_ to the project

  .. code-block:: python
    :emphasize-lines: 1

    cd assertion_error

  the terminal_ shows I am in the ``assertion_error`` folder_

  .. code-block:: python

    .../pumping_python/assertion_error

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

      .. code-block:: shell
        :emphasize-lines: 1

        touch tests/__init__.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        New-Item tests/__init__.py

  the terminal_ goes back to the command line.

* I use the `mv program`_ to change the name of ``main.py`` to ``test_assertion_error.py`` and move it to the ``tests`` folder_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 1

        mv main.py tests/test_assertion_error.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        Move-Item main.py tests/test_assertion_error.py

  the terminal_ goes back to the command line.

* I open ``test_assertion_error.py``

* I delete the text in the file_ then add :ref:`the first failing test<test_failure>` to ``test_assertion_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

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

* I add the new files_ and folder_ to git_ for tracking

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
     create mode 100644 tests/test_assertion_error.py
     create mode 100644 uv.lock

  then goes back to the command line.

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-lines: 5, 7

    ========================== ERRORS ==========================
    ______ ERROR collecting tests/test_assertion_error.py ______
    tests/test_assertion_error.py:2: in <module>
        assert False is True
    E   assert False is True
    ================= short test summary info ==================
    ERROR tests/test_assertion_error.py - assert False is True
    !!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!
    ===================== 1 error in I.JKs =====================

  because :ref:`True<test_what_is_true>` is NOT :ref:`False<test_what_is_false>`

  .. admonition:: if the terminal_ does not show the same error, then check

    * if your ``tests/__init__.py`` has two underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``
    * if you ran ``echo "pytest-watcher" >> requirements.txt``, to add ``pytest-watcher`` to the requirements file_

    fix those errors and try to run ``uv run pytest-watcher . --now`` again

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_assertion_error.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5
    :emphasize-text: AssertionError

    assert False is True


    # Exceptions seen
    # AssertionError

* I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    # assert False is True
    assert False is False


    # Exceptions seen
    # AssertionError

  the test passes.

----

*********************************************************************************
the assert keyword
*********************************************************************************

We know that the result of ``1 + 1`` is ``2``. What if I said that the result of ``'1' + '1'`` is ``'11'``, would you agree?

I can use :ref:`assertions<what is an assertion?>` to make the computer check if these statements are :ref:`True<test_what_is_true>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I remove :ref:`the first failing assertion<test_failure>` then add the first statement

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    1 + 1 == 2


    # Exceptions seen
    # AssertionError

  - the test is still passing
  - ``==`` is two equal signs on the keyboard (:kbd:`=+=`) and means ``is equal`` which makes this statement read as ``1 + 1 is equal to 2``

* I change the result of the equation

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    # 1 + 1 == 2
    1 + 1 == 11


    # Exceptions seen
    # AssertionError

  the test is still passing. Why is it still passing? ``1 + 1`` cannot be both ``2`` and ``11``, is Python_ broken?

* I want the test to fail if I write a statement that is NOT :ref:`True<test_what_is_true>`. I change it to an `assert statement`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    # 1 + 1 == 2
    # 1 + 1 == 11
    assert 1 + 1 == 11


    # Exceptions seen
    # AssertionError

  the terminal_ is my friend, and shows

  .. code-block:: python

    E   assert (1 + 1) == 11

  because Python_ does not care if the statement is :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>` as long as it follows the rules. Once I make it an :ref:`assertion<what is an assertion?>` with `the assert keyword`_ it tells the computer ``DO NOT CONTINUE, if "1 + 1 == 11" is False``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the result back to make the statement :ref:`True<test_what_is_true>`

.. code-block:: python
  :linenos:
  :emphasize-lines: 3-4

  # 1 + 1 == 2
  # 1 + 1 == 11
  # assert 1 + 1 == 11
  assert 1 + 1 == 2


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the other statement (``'1' + '1' == '11'``)

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6

    # 1 + 1 == 2
    # 1 + 1 == 11
    # assert 1 + 1 == 11
    assert 1 + 1 == 2

    '1' + '1' == '2'


    # Exceptions seen

  the terminal_ still shows ``no tests ran`` because the statement is not an assertion_.

* I add assert_ before the statement to make it an assertion_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7


    # 1 + 1 == 2
    # 1 + 1 == 11
    # assert 1 + 1 == 11
    assert 1 + 1 == 2

    # '1' + '1' == '2'
    assert '1' + '1' == '2'


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E   AssertionError: assert ('1' + '1') == '2'

  because the assert_ before the statement makes it a command to Python_ - ``DO NOT CONTINUE if "'1' + '1' == '2'" is False``

----

*********************************************************************************
what causes AssertionError?
*********************************************************************************

AssertionError_ is raised if the statement after `the assert keyword`_ is :ref:`False<test_what_is_false>`. It was in :ref:`the first failing assertion<test_failure>`

.. code-block:: python

  assert False is True

With this statement, I tell Python_ - "DO NOT CONTINUE, if :ref:`False<test_what_is_false>` is the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>`", or said a different way "GO TO THE NEXT LINE, ONLY if :ref:`False<test_what_is_false>` is the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>`".

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 2-3

    # '1' + '1' == '2'
    # assert '1' + '1' == '2'
    assert '1' + '1' == '11'


    # Exceptions seen

  the test passes because the statement is now :ref:`True<test_what_is_true>`, ``'1' + '1'`` is equal to ``'11'``

* These two statements are NOT the same

  - ``1 + 1 == 2`` checks if the result of :ref:`adding<test_addition>` two numbers is equal to the number on the right side of the equality symbol (``==``).
  - ``'1' + '1' == '11'`` checks if the result of "adding" 2 strings_ is equal to the string_ on the right side of the equality symbol (``==``). A string_ is anything inside :ref:`quotes`.

  I add another statement to show how ``'1' + '1' == '11'``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 5

    # '1' + '1' == '2'
    # assert '1' + '1' == '2'
    assert '1' + '1' == '11'

    'I am' + ' alive' == '11'


    # Exceptions seen

  the test is still green because ``'I am' + ' alive' == '11'`` is just a statement. Python_ does not care whether it is :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>` and the statement follows Python_ rules.

* I change the statement to an :ref:`assertion<what is an assertion?>` with `the assert keyword`_

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 5-6

    # '1' + '1' == '2'
    # assert '1' + '1' == '2'
    assert '1' + '1' == '11'

    # 'I am' + ' alive' == '11'
    assert 'I am' + ' alive' == '11'


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 3-4

    E   AssertionError: assert ('I am' + ' alive') == '11'

  because the assert_ before the statement makes it a command to Python_ - ``DO NOT CONTINUE if "'I am' + ' alive' == '11'" is False``

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 2-3

    # 'I am' + ' alive' == '11'
    # assert 'I am' + ' alive' == '11'
    assert 'I am' + ' alive' == 'I am alive'


    # Exceptions seen

  - the test passes.
  - the terminal_ shows ``no tests ran`` which is confusing since the only way I know the test passed, is because I saw it fail. :ref:`There has to be a better way<a better way to organize tests>`.

* I remove the commented lines

  .. code-block:: python
    :linenos:

    assert 1 + 1 == 2

    assert '1' + '1' == '11'

    assert 'I am' + ' alive' == 'I am alive'


    # Exceptions seen
    # AssertionError

* I open a new terminal_ then change directories to ``assertion_error``

  .. code-block:: python
    :emphasize-lines: 1

    cd assertion_error

  the terminal_ shows I am in the ``assertion_error`` folder_

  .. code-block:: python

    .../pumping_python/assertion_error

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'test the assert keyword'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*********************************************************************************
test AssertionError with None
*********************************************************************************

:ref:`None<what is None?>` is used when there is no value. I can use :ref:`assertions<what is an assertion?>` to test if something is the same :ref:`object<everything is an object>` as :ref:`None<what is None?>`, this is useful if I want to check what value I get from a process.

For example, if I have people fill a form and I want a test for when they leave something blank, I can use an :ref:`assertion<what is an assertion?>` to make sure that the value is :ref:`None<what is None?>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a new statement to ``test_assertion_error.py``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3

    assert 'I am' + ' alive' == 'I am alive'

    None is not None

    # Exceptions seen

  the test is still passing

* I add :ref:`the assert keyword`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3-4

    assert 'I am' + ' alive' == 'I am alive'

    # None is not None
    assert None is not None

    # Exceptions seen

  the terminal_ is my friend, and shows AssertionError_

  .. code-block:: python

    E       assert None is not None

  because ``None is not None`` is :ref:`False<test_what_is_false>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the statement to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 2-3

    # None is not None
    # assert None is not None
    assert None is None

    # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a note with what I learned from the experiment

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 6-7

    # None is not None
    # assert None is not None
    assert None is None


    # NOTES
    # None is None

    # Exceptions seen
    # AssertionError

----

* I add a new :ref:`assertion<what is an assertion?>` to compare :ref:`None<what is None?>` with :ref:`False<test_what_is_false>`.

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 5

    # None is not None
    # assert None is not None
    assert None is None

    assert False is None


    # NOTES

  the terminal_ shows

  .. code-block:: python

    E    assert False is None

* I change the `assert statement`_ to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 5-6

    # None is not None
    # assert None is not None
    assert None is None

    # assert False is None
    assert False is not None


    # NOTES

  the test passes.

* I add a note about :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 6

    # assert False is None
    assert False is not None


    # NOTES
    # False is not None
    # None is None

    # Exceptions seen

----

* I add an :ref:`assertion<what is an assertion?>` to compare :ref:`None<what is None?>` with :ref:`True<test_what_is_true>`.

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 4

    # assert False is None
    assert False is not None

    assert True is None


    # NOTES

  the terminal_ shows

  .. code-block:: python

    E    assert True is None

* I change the `assert statement`_ to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 4-5

    # assert False is None
    assert False is not None

    # assert True is None
    assert True is not None


    # NOTES

  the test passes.

* I add a note about :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 2

    # NOTES
    # True is not None
    # False is not None
    # None is None

    # Exceptions seen
    # AssertionError

----

* I add an `assert statement`_ for an integer_ (a whole number without decimals)

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 4

    # assert True is None
    assert True is not None

    assert 0 is None


    # NOTES

  the terminal_ shows

  .. code-block:: python

    E       assert 0 is None

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 4-5

    # assert True is None
    assert True is not None

    # assert 0 is None
    assert 0 is not None


    # NOTES

  the test passes.

* I add a note about integers_

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2

    # NOTES
    # an integer is not None
    # True is not None
    # False is not None
    # None is None


    # Exceptions seen
    # AssertionError

----

* I add an `assert statement`_ for a float_ (binary floating point decimal number)

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 4

    # assert 0 is None
    assert 0 is not None

    assert 0.0 is None


    # NOTES

  the terminal_ shows

  .. code-block:: python

    E       assert 0.0 is None

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 4-5

    # assert 0 is None
    assert 0 is not None

    # assert 0.0 is None
    assert 0.0 is not None


    # NOTES

  the test passes.

* I add a note about floats_

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 2

    # NOTES
    # a float is not None
    # an integer is not None
    # True is not None
    # False is not None
    # None is None


    # Exceptions seen
    # AssertionError

----

* I add an `assert statement`_ for a string_ (anything in :ref:`quotes`)

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 4

    # assert 0.0 is None
    assert 0.0 is not None

    assert '' is None


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E   AssertionError: assert '' is None

  because a string_ is not the same :ref:`object<what is a class?>` as :ref:`None<what is None?>`.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 4-5

    # assert 0.0 is None
    assert 0.0 is not None

    # assert '' is None
    assert '' is not None


    # NOTES

  the test passes because a string_ is not the same :ref:`object<what is a class?>` as :ref:`None<what is None?>`.

* I add a note about strings_

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 2

    # NOTES
    # a string is not None
    # a float is not None
    # an integer is not None
    # True is not None
    # False is not None
    # None is None


    # Exceptions seen
    # AssertionError

----

* I add an `assert statement`_ for a tuple_ (anything in parentheses ``( )`` separated by a comma)

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 4

    # assert '' is None
    assert '' is not None

    assert () is None


    # NOTES

  the terminal_ shows

  .. code-block:: python

    E   assert {} is None

  because a tuple_ is not the same :ref:`object<what is a class?>` :ref:`None<what is None?>`.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 4-5

    # assert '' is None
    assert '' is not None

    # assert () is None
    assert () is not None


    # NOTES

  the test passes because a tuple_ is not the same :ref:`object<what is a class?>` :ref:`None<what is None?>`.

* I add a note about tuples_

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 2

    # NOTES
    # a tuple is not None
    # a string is not None
    # a float is not None
    # an integer is not None
    # True is not None
    # False is not None
    # None is None


    # Exceptions seen
    # AssertionError

----

* I add an `assert statement`_ for a :ref:`list<what is a list?>` (anything in square brackets ``[ ]``)

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 4

    # assert () is None
    assert () is not None

    assert [] is None


    # NOTES

  the terminal_ shows

  .. code-block:: python

    E   assert [] is None

  because a :ref:`list<what is a list?>` is not the same :ref:`object<what is a class?>` as :ref:`None<what is None?>`.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 4-5

    # assert () is None
    assert () is not None

    # assert [] is None
    assert [] is not None


    # NOTES

  the test passes because a :ref:`list<what is a list?>` is not the same :ref:`object<what is a class?>` as :ref:`None<what is None?>`.

* I add a note about :ref:`lists<what is a list?>`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2

    # NOTES
    # a list is not None
    # a tuple is not None
    # a string is not None
    # a float is not None
    # an integer is not None
    # True is not None
    # False is not None
    # None is None


    # Exceptions seen
    # AssertionError

----

* I add an `assert statement`_ for a set_

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 4

    # assert [] is None
    assert [] is not None

    assert set() is None


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E   assert set() is None

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 4-5

    # assert [] is None
    assert [] is not None

    # assert set() is None
    assert set() is not None


    # NOTES

  the test passes.

* I add a note about sets_

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 2

    # NOTES
    # a set is not None
    # a list is not None
    # a tuple is not None
    # a string is not None
    # a float is not None
    # an integer is not None
    # True is not None
    # False is not None
    # None is None


    # Exceptions seen
    # AssertionError

----

* I add an `assert statement`_ for a :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 4

    # assert set() is None
    assert set() is not None

    assert {} is None


    # NOTES

  the terminal_ shows

  .. code-block:: python

    E   assert {} is None

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 4-5

    # assert set() is None
    assert set() is not None

    # assert {} is None
    assert {} is not None


    # NOTES

  the test passes.

* I add a note about :ref:`dictionaries<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 2

    # NOTES
    # a dictionary is not None
    # a set is not None
    # a list is not None
    # a tuple is not None
    # a string is not None
    # a float is not None
    # an integer is not None
    # True is not None
    # False is not None
    # None is None


    # Exceptions seen
    # AssertionError

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 5

    assert 'I am' + ' alive' == 'I am alive'

    assert None is None

    assert False is not None

    assert True is not None

    assert 0 is not None

    assert 0.0 is not None

    assert '' is not None

    assert () is not None

    assert [] is not None

    assert set() is not None

    assert {} is not None


    # NOTES

* I add comments to group the :ref:`assertions<what is an assertion?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 9

    # test assert keyword
    assert 1 + 1 == 2

    assert '1' + '1' == '11'

    assert 'I am' + ' alive' == 'I am alive'


    # test AssertionError with None
    assert None is None

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test AssertionError with None'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can use assertions to test if something is None<test AssertionError with None>`.

----

*********************************************************************************
test AssertionError with False
*********************************************************************************

:ref:`False<test_what_is_false>` is one of the two :ref:`booleans<what are booleans?>` and ``assert False is not None`` shows that :ref:`False<test_what_is_false>` is NOT :ref:`None<what is None?>`. :ref:`is None False?<test_is_none_falsy_or_truthy>`

I can use :ref:`assertions<what is an assertion?>` to test if something is the same :ref:`object<everything is an object>` as :ref:`False<test_what_is_false>` or not.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a new statement to ``test_assertion_error.py`` with a comment to group these new statements

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 4-5

    assert {} is not None


    # test AssertionError with False
    None is False


    # NOTES

  the test is still passing.

* I add :ref:`the assert keyword`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 2-3

    # test AssertionError with False
    # None is False
    assert None is False


    # NOTES

  the terminal_ is my friend, and shows

  .. code-block:: python

    E       assert None is False

  because :ref:`None<what is None?>` is not the same :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 31
  :emphasize-lines: 3-4

    # test AssertionError with False
    # None is False
    # assert None is False
    assert None is not False


    # NOTES

the test passes because :ref:`None<what is None?>` is not the same :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a note about :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 11

    # NOTES
    # a dictionary is not None
    # a set is not None
    # a list is not None
    # a tuple is not None
    # a string is not None
    # a float is not None
    # an integer is not None
    # True is not None
    # False is not None
    # None is not False
    # None is None

----

* I add a failing `assert statement`_ about :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 6

    # test AssertionError with False
    # None is False
    # assert None is False
    assert None is not False

    assert False is not False


    # NOTES

  the terminal_ shows

  .. code-block:: python

    E       assert False is not False

  because :ref:`False is False<test_what_is_false>`.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 6-7

    # test AssertionError with False
    # None is False
    # assert None is False
    assert None is not False

    # assert False is not False
    assert False is False


    # NOTES

  the test passes because :ref:`False is False<test_what_is_false>`.

* I add a note about :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 10

    # NOTES
    # a dictionary is not None
    # a set is not None
    # a list is not None
    # a tuple is not None
    # a string is not None
    # a float is not None
    # an integer is not None
    # True is not None
    # False is False
    # False is not None
    # None is not False
    # None is None

----

* I add an `assert statement`_ to see if :ref:`True<test_what_is_true>` is the same :ref:`object<everything is an object>` as :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 4

    # assert False is not False
    assert False is False

    assert True is False


    # NOTES

  the terminal_

  .. code-block:: python

    E       assert True is False

  because :ref:`True<test_what_is_true>` is not the same :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>`.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 4-5

    # assert False is not False
    assert False is False

    # assert True is False
    assert True is not False


    # NOTES

  the test passes because :ref:`True<test_what_is_true>` is not the same :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>`.

* I add a note about :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 9

    # NOTES
    # a dictionary is not None
    # a set is not None
    # a list is not None
    # a tuple is not None
    # a string is not None
    # a float is not None
    # an integer is not None
    # True is not False
    # True is not None
    # False is False
    # False is not None
    # None is not False
    # None is None

----

* I add an `assert statement`_ to see if an integer_ (a whole number without decimals) is the same :ref:`object<everything is an object>` as :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 4

    # assert True is False
    assert True is not False

    assert 0 is False


    # NOTES

  the terminal_ shows

  .. code-block:: python

    E       assert 0 is False

  because an integer_ is not the same :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>`.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 4-5

    # assert True is False
    assert True is not False

    # assert 0 is False
    assert 0 is not False


    # NOTES

  the test passes because an integer_ is not the same :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>`.

* I add a note about integers_

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 8

    # NOTES
    # a dictionary is not None
    # a set is not None
    # a list is not None
    # a tuple is not None
    # a string is not None
    # a float is not None
    # an integer is not False
    # an integer is not None
    # True is not False
    # True is not None
    # False is False
    # False is not None
    # None is not False
    # None is None

----

* I add an `assert statement`_ to see if a float_ (binary floating point decimal number) is the same :ref:`object<everything is an object>` as :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 4

    # assert 0 is False
    assert 0 is not False

    assert 0.0 is False


    # NOTES

  the terminal_ shows

  .. code-block:: python

    E       assert 0.0 is False

  because a float_ is not the same :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>`.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 4-5

    # assert 0 is False
    assert 0 is not False

    # assert 0.0 is False
    assert 0.0 is not False


    # NOTES

  the test passes because a float_ is not the same :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>`.

* I add a note about floats_

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 7

    # NOTES
    # a dictionary is not None
    # a set is not None
    # a list is not None
    # a tuple is not None
    # a string is not None
    # a float is not False
    # a float is not None
    # an integer is not False
    # an integer is not None
    # True is not False
    # True is not None
    # False is False
    # False is not None
    # None is not False
    # None is None

----

* I add an `assert statement`_ to see if a string_ (anything in :ref:`quotes`) is the same :ref:`object<everything is an object>` as :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 4

    # assert 0.0 is False
    assert 0.0 is not False

    assert '' is False


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert '' is False

  because a string_ is not the same :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>`.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 4-5


    # assert 0.0 is False
    assert 0.0 is not False

    # assert '' is False
    assert '' is not False


    # NOTES

  the test passes because a string_ is not the same :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>`.

* I add a note about strings_

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 6

    # NOTES
    # a dictionary is not None
    # a set is not None
    # a list is not None
    # a tuple is not None
    # a string is not False
    # a string is not None
    # a float is not False
    # a float is not None
    # an integer is not False
    # an integer is not None
    # True is not False
    # True is not None
    # False is False
    # False is not None
    # None is not False
    # None is None

----

* I add an `assert statement`_ to see if a tuple_ (anything in parentheses ``( )`` separated by a comma) is the same :ref:`object<everything is an object>` as :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 4

    # assert '' is False
    assert '' is not False

    assert () is False


    # NOTES

  the terminal_ shows

  .. code-block:: python

    E   assert () is False

  because a tuple_ is not the same :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>`.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 4-5

    # assert '' is False
    assert '' is not False

    # assert () is False
    assert () is not False


    # NOTES

  the test passes because a tuple_ is not the same :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>`.

* I add a note about tuples_

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 5

    # NOTES
    # a dictionary is not None
    # a set is not None
    # a list is not None
    # a tuple is not False
    # a tuple is not None
    # a string is not False
    # a string is not None
    # a float is not False
    # a float is not None
    # an integer is not False
    # an integer is not None
    # True is not False
    # True is not None
    # False is False
    # False is not None
    # None is not False
    # None is None

----

* I add an `assert statement`_ to see if a :ref:`list<what is a list?>` (anything in square brackets ``[ ]``) is the same :ref:`object<everything is an object>` as :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 4

    # assert () is False
    assert () is not False

    assert [] is False


    # NOTES

  the terminal_ shows

  .. code-block:: python

    E   assert [] is False

  because a :ref:`list<what is a list?>` is not the same :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>`.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 4-5

    # assert () is False
    assert () is not False

    # assert [] is False
    assert [] is not False


    # NOTES

  the test passes because a :ref:`list<what is a list?>` is not the same :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>`.

* I add a note about :ref:`lists<what is a list?>`

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 4

    # NOTES
    # a dictionary is not None
    # a set is not None
    # a list is not False
    # a list is not None
    # a tuple is not False
    # a tuple is not None
    # a string is not False
    # a string is not None
    # a float is not False
    # a float is not None
    # an integer is not False
    # an integer is not None
    # True is not False
    # True is not None
    # False is False
    # False is not None
    # None is not False
    # None is None

----

* I add an `assert statement`_ to see if a set_ is the same :ref:`object<everything is an object>` as :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 4

    # assert [] is False
    assert [] is not False

    assert set() is False


    # NOTES

  the terminal_ shows

  .. code-block:: python

    E   assert set() is False

  because a set_ is not the same :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>`.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 4-5

    # assert [] is False
    assert [] is not False

    # assert set() is False
    assert set() is not False


    # NOTES

  the test passes because a set_ is not the same :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>`.
* I add a note about sets_

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 3

    # NOTES
    # a dictionary is not None
    # a set is not False
    # a set is not None
    # a list is not False
    # a list is not None
    # a tuple is not False
    # a tuple is not None
    # a string is not False
    # a string is not None
    # a float is not False
    # a float is not None
    # an integer is not False
    # an integer is not None
    # True is not False
    # True is not None
    # False is False
    # False is not None
    # None is not False
    # None is None

-----

* I add an `assert statement`_ to see if a :ref:`dictionary<what is a dictionary?>` is the same :ref:`object<everything is an object>` as :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 4

    # assert set() is False
    assert set() is not False

    assert {} is False


    # NOTES

  the terminal_ shows

  .. code-block:: python

    E   assert {} is False

  because a :ref:`dictionary<what is a dictionary?>` is not the same :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>`.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 4-5

    # assert set() is False
    assert set() is not False

    # assert {} is False
    assert {} is not False


    # NOTES

  the test passes because a :ref:`dictionary<what is a dictionary?>` is not the same :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>`.

* I add a note about :ref:`dictionaries<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 2

    # NOTES
    # a dictionary is not False
    # a dictionary is not None
    # a set is not False
    # a set is not None
    # a list is not False
    # a list is not None
    # a tuple is not False
    # a tuple is not None
    # a string is not False
    # a string is not None
    # a float is not False
    # a float is not None
    # an integer is not False
    # an integer is not None
    # True is not False
    # True is not None
    # False is False
    # False is not None
    # None is not False
    # None is None


    # Exceptions seen
    # AssertionError

* I remove the commented :ref:`assertions<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 31

    # test AssertionError with False
    assert None is not False

    assert False is False

    assert True is not False

    assert 0 is not False

    assert 0.0 is not False

    assert '' is not False

    assert () is not False

    assert [] is not False

    assert set() is not False

    assert {} is not False


    # NOTES

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test AssertionError with False'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*********************************************************************************
test AssertionError with True
*********************************************************************************

:ref:`True<test_what_is_true>` is the other :ref:`boolean<what are booleans?>` and is NOT :ref:`None<what is None?>`. I can use :ref:`assertions<what is an assertion?>` to test if something is the same :ref:`object<everything is an object>` as :ref:`True<test_what_is_true>` or not.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a new statement to ``test_assertion_error.py`` with a comment to group these new statements

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 4-5

    assert {} is not False


    # test AssertionError with True
    None is True


    # NOTES

  the test is still passing.

* I add :ref:`the assert keyword`

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 2-3

    # test AssertionError with True
    # None is True
    assert None is True


    # NOTES

  the terminal_ is my friend, and shows

  .. code-block:: python

    E       assert None is True

  because :ref:`None<what is None?>` is not the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the statement to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 53
  :emphasize-lines: 3-4

  # test AssertionError with True
  # None is True
  # assert None is True
  assert None is not True


  # NOTES

the test passes because :ref:`None<what is None?>` is not the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a note about :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 20

    # NOTES
    # a dictionary is not False
    # a dictionary is not None
    # a set is not False
    # a set is not None
    # a list is not False
    # a list is not None
    # a tuple is not False
    # a tuple is not None
    # a string is not False
    # a string is not None
    # a float is not False
    # a float is not None
    # an integer is not False
    # an integer is not None
    # True is not False
    # True is not None
    # False is False
    # False is not None
    # None is not True
    # None is not False
    # None is None

----

* I add an `assert statement`_ to see if :ref:`False<test_what_is_false>` is the same :ref:`object<everything is an object>` as :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 6

    # test AssertionError with True
    # None is True
    # assert None is True
    assert None is not True

    assert False is True


    # NOTES

  the terminal_ shows

  .. code-block:: python

    E       assert False is True

  because :ref:`False<test_what_is_false>` is not the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>`.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 6-7

    # test AssertionError with True
    # None is True
    # assert None is True
    assert None is not True

    # assert False is True
    assert False is not True


    # NOTES

  the test passes because :ref:`False<test_what_is_false>` is not the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>`.

* I add a note about :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 18

    # NOTES
    # a dictionary is not False
    # a dictionary is not None
    # a set is not False
    # a set is not None
    # a list is not False
    # a list is not None
    # a tuple is not False
    # a tuple is not None
    # a string is not False
    # a string is not None
    # a float is not False
    # a float is not None
    # an integer is not False
    # an integer is not None
    # True is not False
    # True is not None
    # False is not True
    # False is False
    # False is not None
    # None is not True
    # None is not False
    # None is None

----

* I add an `assert statement`_ about :ref:`True<test_what_is_true>`, that will fail

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 4

    # assert False is True
    assert False is not True

    assert True is not True


    # NOTES

  the terminal_ shows

  .. code-block:: python

    E       assert True is not True

  because :ref:`True is True<test_what_is_true>`.

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 4-5

    # assert False is True
    assert False is not True

    # assert True is not True
    assert True is True


    # NOTES

  the test passes because :ref:`True is True<test_what_is_true>`.

* I add a note about :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 16

    # NOTES
    # a dictionary is not False
    # a dictionary is not None
    # a set is not False
    # a set is not None
    # a list is not False
    # a list is not None
    # a tuple is not False
    # a tuple is not None
    # a string is not False
    # a string is not None
    # a float is not False
    # a float is not None
    # an integer is not False
    # an integer is not None
    # True is True
    # True is not False
    # True is not None
    # False is not True
    # False is False
    # False is not None
    # None is not True
    # None is not False
    # None is None

----

* I add an `assert statement`_ to see if an integer_ (a whole number without decimals) is the same :ref:`object<everything is an object>` as :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 4

    # assert True is not True
    assert True is True

    assert 0 is True


    # NOTES

  the terminal_ shows

  .. code-block:: python

    E       assert 0 is True

  because an integer_ is not the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>`.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 4-5

    # assert True is not True
    assert True is True

    # assert 0 is True
    assert 0 is not True


    # NOTES

  the test passes because an integer_ is not the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>`.

* I add a note about integers_

  .. code-block:: python
    :lineno-start: 68
    :emphasize-lines: 14

    # NOTES
    # a dictionary is not False
    # a dictionary is not None
    # a set is not False
    # a set is not None
    # a list is not False
    # a list is not None
    # a tuple is not False
    # a tuple is not None
    # a string is not False
    # a string is not None
    # a float is not False
    # a float is not None
    # an integer is not True
    # an integer is not False
    # an integer is not None
    # True is True
    # True is not False
    # True is not None
    # False is not True
    # False is False
    # False is not None
    # None is not True
    # None is not False
    # None is None

----

* I add an `assert statement`_ to see if a float_ (binary floating point decimal number) is the same :ref:`object<everything is an object>` as :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 4

    # assert 0 is True
    assert 0 is not True

    assert 0.0 is True


    # NOTES

  the terminal_ shows

  .. code-block:: python

    E       assert 0.0 is True

  because a float_ is not the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>`.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 4-5

    # assert 0 is True
    assert 0 is not True

    # assert 0.0 is True
    assert 0.0 is not True


    # NOTES

  the test passes because a float_ is not the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>`.

* I add a note about floats_

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 12

    # NOTES
    # a dictionary is not False
    # a dictionary is not None
    # a set is not False
    # a set is not None
    # a list is not False
    # a list is not None
    # a tuple is not False
    # a tuple is not None
    # a string is not False
    # a string is not None
    # a float is not True
    # a float is not False
    # a float is not None
    # an integer is not True
    # an integer is not False
    # an integer is not None
    # True is True
    # True is not False
    # True is not None
    # False is not True
    # False is False
    # False is not None
    # None is not True
    # None is not False
    # None is None

----

* I add an `assert statement`_ to see if a string_ (anything in :ref:`quotes`) is the same :ref:`object<everything is an object>` as :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 4

    # assert 0.0 is True
    assert 0.0 is not True

    assert '' is True


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert '' is True

  because a string_ is not the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>`.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 4-5

    # assert 0.0 is True
    assert 0.0 is not True

    # assert '' is True
    assert '' is not True


    # NOTES

  the test passes because a string_ is not the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>`.

* I add a note about strings_

  .. code-block:: python
    :lineno-start: 74
    :emphasize-lines: 10

    # NOTES
    # a dictionary is not False
    # a dictionary is not None
    # a set is not False
    # a set is not None
    # a list is not False
    # a list is not None
    # a tuple is not False
    # a tuple is not None
    # a string is not True
    # a string is not False
    # a string is not None
    # a float is not True
    # a float is not False
    # a float is not None
    # an integer is not True
    # an integer is not False
    # an integer is not None
    # True is True
    # True is not False
    # True is not None
    # False is not True
    # False is False
    # False is not None
    # None is not True
    # None is not False
    # None is None

----

* I add an `assert statement`_ to see if a tuple_ (anything in parentheses ``( )`` separated by a comma) is the same :ref:`object<everything is an object>` as :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start:
    :emphasize-lines: 4

    # assert '' is True
    assert '' is not True

    assert () is True


    # NOTES

  the terminal_ shows

  .. code-block:: python

    E   assert () is True

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 4-5

    # assert '' is True
    assert '' is not True

    # assert () is True
    assert () is not True


    # NOTES

  the test passes.

* I add a note about tuples_

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 8

    # NOTES
    # a dictionary is not False
    # a dictionary is not None
    # a set is not False
    # a set is not None
    # a list is not False
    # a list is not None
    # a tuple is not True
    # a tuple is not False
    # a tuple is not None
    # a string is not True
    # a string is not False
    # a string is not None
    # a float is not True
    # a float is not False
    # a float is not None
    # an integer is not True
    # an integer is not False
    # an integer is not None
    # True is True
    # True is not False
    # True is not None
    # False is not True
    # False is False
    # False is not None
    # None is not True
    # None is not False
    # None is None

----

* I add an `assert statement`_ to see if a :ref:`list<what is a list?>` (anything in square brackets ``[ ]``) is the same :ref:`object<everything is an object>` as :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 4

    # assert () is True
    assert () is not True

    assert [] is True


    # NOTES

  the terminal_ shows

  .. code-block:: python

    E   assert [] is True

  because a :ref:`list<what is a list?>` is not the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>`.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 4-5

    # assert () is True
    assert () is not True

    # assert [] is True
    assert [] is not True


    # NOTES

  the test passes because a :ref:`list<what is a list?>` is not the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>`.

* I add a note about :ref:`lists<what is a list?>`

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 6

    # NOTES
    # a dictionary is not False
    # a dictionary is not None
    # a set is not False
    # a set is not None
    # a list is not True
    # a list is not False
    # a list is not None
    # a tuple is not True
    # a tuple is not False
    # a tuple is not None
    # a string is not True
    # a string is not False
    # a string is not None
    # a float is not True
    # a float is not False
    # a float is not None
    # an integer is not True
    # an integer is not False
    # an integer is not None
    # True is True
    # True is not False
    # True is not None
    # False is not True
    # False is False
    # False is not None
    # None is not True
    # None is not False
    # None is None

----

* I add an `assert statement`_ to see if a set_ is the same :ref:`object<everything is an object>` as :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 4

    # assert [] is True
    assert [] is not True

    assert set() is True


    # NOTES

  the terminal_ shows

  .. code-block:: python

    E   assert set() is True

  because a set_ is not the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>`.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 4-5

    # assert [] is True
    assert [] is not True

    # assert set() is True
    assert set() is not True


    # NOTES

  the test passes because a set_ is not the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>`.

* I add a note about sets_

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 4

    # NOTES
    # a dictionary is not False
    # a dictionary is not None
    # a set is not True
    # a set is not False
    # a set is not None
    # a list is not True
    # a list is not False
    # a list is not None
    # a tuple is not True
    # a tuple is not False
    # a tuple is not None
    # a string is not True
    # a string is not False
    # a string is not None
    # a float is not True
    # a float is not False
    # a float is not None
    # an integer is not True
    # an integer is not False
    # an integer is not None
    # True is True
    # True is not False
    # True is not None
    # False is not True
    # False is False
    # False is not None
    # None is not True
    # None is not False
    # None is None

-----

* I add an `assert statement`_ to see if a :ref:`dictionary<what is a dictionary?>` is the same :ref:`object<everything is an object>` as :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 79
    :emphasize-lines: 4

    # assert set() is True
    assert set() is not True

    assert {} is True


    # NOTES

  the terminal_ shows

  .. code-block:: python

    E   assert {} is True

  because a :ref:`dictionary<what is a dictionary?>` is not the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>`.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 79
    :emphasize-lines: 4-5

    # assert set() is True
    assert set() is not True

    # assert {} is True
    assert {} is not True


    # NOTES

  the test passes because a :ref:`dictionary<what is a dictionary?>` is not the same :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>`.

* I add a note about :ref:`dictionaries<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 2

    # NOTES
    # a dictionary is not True
    # a dictionary is not False
    # a dictionary is not None
    # a set is not True
    # a set is not False
    # a set is not None
    # a list is not True
    # a list is not False
    # a list is not None
    # a tuple is not True
    # a tuple is not False
    # a tuple is not None
    # a string is not True
    # a string is not False
    # a string is not None
    # a float is not True
    # a float is not False
    # a float is not None
    # an integer is not True
    # an integer is not False
    # an integer is not None
    # True is True
    # True is not False
    # True is not None
    # False is not True
    # False is False
    # False is not None
    # None is not True
    # None is not False
    # None is None


    # Exceptions seen
    # AssertionError

* I remove the commented :ref:`assertions<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 53

    # test AssertionError with True
    assert None is not True

    assert False is not True

    assert True is True

    assert 0 is not True

    assert 0.0 is not True

    assert '' is not True

    assert () is not True

    assert [] is not True

    assert set() is not True

    assert {} is not True


    # NOTES

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'test AssertionError with True'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can use assertions to test if something is the same object as True or NOT<test AssertionError with True>`.

----

*********************************************************************************
test AssertionError with equality
*********************************************************************************

All the :ref:`assertions<what is an assertion?>` I have typed so far show that :ref:`True<test_what_is_true>`, :ref:`False<test_what_is_false>` and :ref:`None<what is None?>` are different. They give me a basic expectation of Python_ because I can compare things with them.

I can also use :ref:`assertions<what is an assertion?>` to test if two things are equal, like I did when I :ref:`test the assert keyword<the assert keyword>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a new statement to ``test_assertion_error.py`` with a comment to group these new statements

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 4-5

    assert {} is not True


    # test AssertionError with equality
    None != None


    # NOTES

  the test is still passing.

* I add :ref:`the assert keyword`

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 2-3

    # test AssertionError with equality
    # None != None
    assert None != None


    # NOTES

  the terminal_ is my friend, and shows

  .. code-block:: python

    E   assert None != None

  - because :ref:`None is equal to None<what is None?>`.
  - ``==`` is two equal signs on the keyboard (:kbd:`=+=`) and means ``is equal`` which makes this statement read as ``None is equal to None``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the statement to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 75
  :emphasize-lines: 3-4

  # test AssertionError with equality
  # None != None
  # assert None != None
  assert None == None


  # NOTES

- the test passes because :ref:`None is equal to None<what is None?>`
- ``==`` is two equal signs on the keyboard (:kbd:`=+=`) and means ``is equal`` which makes this statement read as ``1 + 1 is equal to 2``

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add to the ``None is None`` note

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 31

    # NOTES
    # a dictionary is not True
    # a dictionary is not False
    # a dictionary is not None
    # a set is not True
    # a set is not False
    # a set is not None
    # a list is not True
    # a list is not False
    # a list is not None
    # a tuple is not True
    # a tuple is not False
    # a tuple is not None
    # a string is not True
    # a string is not False
    # a string is not None
    # a float is not True
    # a float is not False
    # a float is not None
    # an integer is not True
    # an integer is not False
    # an integer is not None
    # True is True
    # True is not False
    # True is not None
    # False is not True
    # False is False
    # False is not None
    # None is not True
    # None is not False
    # None is None and equal to None

* I add an :ref:`assertion<what is an assertion?>` to compare :ref:`False<test_what_is_false>` with :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 6

    # test AssertionError with equality
    # None != None
    # assert None != None
    assert None == None

    assert False == None


    # NOTES

  the terminal_ is my friend, and shows

  .. code-block:: python

    E    assert False == None

  because :ref:`False<test_what_is_false>` is NOT equal to :ref:`None<what is None?>` and :ref:`None<what is None?>` is NOT equal to :ref:`False<test_what_is_false>`.

* I change the `assert statement`_ to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 6-7

    # test AssertionError with equality
    # None != None
    # assert None != None
    assert None == None

    # assert False == None
    assert False != None


    # NOTES

  the test passes because :ref:`False<test_what_is_false>` is NOT equal to :ref:`None<what is None?>` and :ref:`None<what is None?>` is NOT equal to :ref:`False<test_what_is_false>`.

* I add to the ``False is not None`` and ``None is not False`` notes because equality goes both ways

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 28, 30

    # NOTES
    # a dictionary is not True
    # a dictionary is not False
    # a dictionary is not None
    # a set is not True
    # a set is not False
    # a set is not None
    # a list is not True
    # a list is not False
    # a list is not None
    # a tuple is not True
    # a tuple is not False
    # a tuple is not None
    # a string is not True
    # a string is not False
    # a string is not None
    # a float is not True
    # a float is not False
    # a float is not None
    # an integer is not True
    # an integer is not False
    # an integer is not None
    # True is True
    # True is not False
    # True is not None
    # False is not True
    # False is False
    # False is not None and NOT equal to None
    # None is not True
    # None is not False and NOT equal to False
    # None is None and equal to None

* I add an :ref:`assertion<what is an assertion?>` to compare :ref:`False<test_what_is_false>` with :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 4

    # assert False == None
    assert False != None

    assert False == True


    # NOTES

  the terminal_ is my friend, and shows

  .. code-block:: python

    E       assert False == True

  because :ref:`False<test_what_is_false>` is NOT equal to :ref:`True<test_what_is_true>` and :ref:`True<test_what_is_true>` is NOT equal to :ref:`False<test_what_is_false>`.

* I change the `assert statement`_ to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 4-5

    # assert False == None
    assert False != None

    # assert False == True
    assert False != True


    # NOTES

  the test passes because :ref:`False<test_what_is_false>` is NOT equal to :ref:`True<test_what_is_true>` and :ref:`True<test_what_is_true>` is NOT equal to :ref:`False<test_what_is_false>`.

* I add to the ``False is not True`` and ``True is not False`` notes because equality goes both ways

  .. code-block:: python
    :lineno-start: 87
    :emphasize-lines: 24, 26

    # NOTES
    # a dictionary is not True
    # a dictionary is not False
    # a dictionary is not None
    # a set is not True
    # a set is not False
    # a set is not None
    # a list is not True
    # a list is not False
    # a list is not None
    # a tuple is not True
    # a tuple is not False
    # a tuple is not None
    # a string is not True
    # a string is not False
    # a string is not None
    # a float is not True
    # a float is not False
    # a float is not None
    # an integer is not True
    # an integer is not False
    # an integer is not None
    # True is True
    # True is not False and NOT equal to False
    # True is not None
    # False is not True and NOT equal to True
    # False is False
    # False is not None and NOT equal to None
    # None is not True
    # None is not False and NOT equal to False
    # None is None and equal to None

* I add an :ref:`assertion<what is an assertion?>` to compare :ref:`False<test_what_is_false>` with itself

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 4

    # assert False == True
    assert False != True

    assert False != False


    # NOTES

  the terminal_ is my friend, and shows

  .. code-block:: python

    E    assert False != False

  because :ref:`False is equal to False<test_what_is_false>`.

* I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 4-5

    # assert False == True
    assert False != True

    # assert False != False
    assert False == False


    # NOTES

  the test passes because :ref:`False is equal to False<test_what_is_false>`.

* I add to the ``False is False`` note

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 27

    # NOTES
    # a dictionary is not True
    # a dictionary is not False
    # a dictionary is not None
    # a set is not True
    # a set is not False
    # a set is not None
    # a list is not True
    # a list is not False
    # a list is not None
    # a tuple is not True
    # a tuple is not False
    # a tuple is not None
    # a string is not True
    # a string is not False
    # a string is not None
    # a float is not True
    # a float is not False
    # a float is not None
    # an integer is not True
    # an integer is not False
    # an integer is not None
    # True is True
    # True is not False and NOT equal to False
    # True is not None
    # False is not True and NOT equal to True
    # False is False and equal to False
    # False is not None and NOT equal to None
    # None is not True
    # None is not False and NOT equal to False
    # None is None and equal to None

----

* I add a new failing :ref:`assertion<what is an assertion?>` to compare :ref:`True<test_what_is_true>` with :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 4

    # assert False != False
    assert False == False

    assert True == None


    # NOTES

  the terminal_ is my friend, and shows

  .. code-block:: python

    E    assert True == None

  because :ref:`True<test_what_is_true>` is NOT equal :ref:`None<what is None?>` and :ref:`None<what is None?>` is NOT equal to :ref:`True<test_what_is_true>`.

* I change the `assert statement`_ to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 4-5

    # assert False != False
    assert False == False

    # assert True == None
    assert True != None


    # NOTES

  the test passes because :ref:`True<test_what_is_true>` is NOT equal :ref:`None<what is None?>` and :ref:`None<what is None?>` is NOT equal to :ref:`True<test_what_is_true>`.

* I add to the ``True is not None`` and ``None is not True`` notes because equality goes both ways

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 25, 29

    # NOTES
    # a dictionary is not True
    # a dictionary is not False
    # a dictionary is not None
    # a set is not True
    # a set is not False
    # a set is not None
    # a list is not True
    # a list is not False
    # a list is not None
    # a tuple is not True
    # a tuple is not False
    # a tuple is not None
    # a string is not True
    # a string is not False
    # a string is not None
    # a float is not True
    # a float is not False
    # a float is not None
    # an integer is not True
    # an integer is not False
    # an integer is not None
    # True is True
    # True is not False and NOT equal to False
    # True is not None and NOT equal to None
    # False is not True and NOT equal to True
    # False is False and equal to False
    # False is not None and NOT equal to None
    # None is not True and NOT equal to True
    # None is not False and NOT equal to False
    # None is None and equal to None

* I add an :ref:`assertion<what is an assertion?>` to compare :ref:`True<test_what_is_true>` with itself

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 4

    # assert True == None
    assert True != None

    assert True != True


    # NOTES

  the terminal_ is my friend, and shows

  .. code-block:: python

    E    assert True != True

  because :ref:`True is equal to True<test_what_is_true>`.

* I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 4-5

    # assert True == None
    assert True != None

    # assert True != True
    assert True == True


    # NOTES

  the test passes because :ref:`True is equal to True<test_what_is_true>`.

* I add to the ``True is True`` note

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 23

    # NOTES
    # a dictionary is not True
    # a dictionary is not False
    # a dictionary is not None
    # a set is not True
    # a set is not False
    # a set is not None
    # a list is not True
    # a list is not False
    # a list is not None
    # a tuple is not True
    # a tuple is not False
    # a tuple is not None
    # a string is not True
    # a string is not False
    # a string is not None
    # a float is not True
    # a float is not False
    # a float is not None
    # an integer is not True
    # an integer is not False
    # an integer is not None
    # True is True and equal to True
    # True is not False and NOT equal to False
    # True is not None and NOT equal to None
    # False is not True and NOT equal to True
    # False is False and equal to False
    # False is not None and NOT equal to None
    # None is not True and NOT equal to True
    # None is not False and NOT equal to False
    # None is None and equal to None


    # Exceptions seen
    # AssertionError

* I remove the commented :ref:`assertions<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 75

    # test AssertionError with equality
    assert None == None

    assert False != None

    assert False != True

    assert False == False

    assert True != None

    assert True == True


    # NOTES

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test AssertionError with equality'

  the terminal_ shows a summary of the changes then goes back to the command line.

:ref:`I can use assertions to test if two things are equal<test AssertionError with equality>`.

----

*********************************************************************************
test AssertionError with is vs equal
*********************************************************************************

Some of the tests I have written use ``is`` and some use ``==``, if they mean the same thing, why do I use different symbols? What is the difference between ``is`` and ``==``?

In Python_ they do not mean the same thing

* ``x is y`` states that ``x`` is the same exact :ref:`object<everything is an object>` as ``y``
* ``x == y`` states that ``x`` is equal to ``y`` according to a rule or instruction programmed in Python_
* ``x is not y`` states that ``x`` is NOT the same exact :ref:`object<everything is an object>` as ``y``
* ``x != y`` states that ``x`` is NOT equal to ``y`` according to a rule or instruction programmed in Python_

This means that things can be equal without being the same exact :ref:`object<everything is an object>`. For example, an integer_ (a whole number without decimals) can be equal to a float_ (binary floating point decimal numbers) and they are NOT the same :ref:`object<everything is an object>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add statements to show this

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 4-5

    assert True == True


    # test AssertionError with is vs equal
    0 is 0.0


    # NOTES

  the test is still passing.

* I add :ref:`the assert keyword`

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 2-3

    # test AssertionError with is vs equal
    # 0 is 0.0
    assert 0 is 0.0


    # NOTES

  the terminal_ is my friend, and shows

  .. code-block:: python

    E   assert 0 is 0.0

  because an integer_ is not the same :ref:`object<what is a class?>` as a float_.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the :ref:`assertion<what is an assertion?>` to make the statement :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 89
  :emphasize-lines: 3-4

    # test AssertionError with is vs equal
    # 0 is 0.0
    # assert 0 is 0.0
    assert 0 is not 0.0


    # NOTES

the test passes because an integer_ is not the same :ref:`object<what is a class?>` as a float_.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another :ref:`assertion<what is an assertion?>`, this time with ``!=``

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 6

    # test AssertionError with is vs equal
    # 0 is 0.0
    # assert 0 is 0.0
    assert 0 is not 0.0

    assert 0 != 0.0


    # NOTES

  the terminal_ is my friend, and shows

  .. code-block:: python

    E       assert 0 != 0.0

  because ``0`` and ``0.0`` are equal, they are both zero.

* I change the :ref:`assertion<what is an assertion?>` to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 6-7

    # test AssertionError with is vs equal
    # 0 is 0.0
    # assert 0 is 0.0
    assert 0 is not 0.0

    # assert 0 != 0.0
    assert 0 == 0.0


    # NOTES

  the test passes because ``0`` and ``0.0`` are equal, they are both zero.

* I remove the commented :ref:`assertions<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 89

    # test AssertionError with is vs equal
    assert 0 is not 0.0

    assert 0 == 0.0


    # NOTES

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'test AssertionError with is vs equal'

  the terminal_ shows a summary of the changes then goes back to the command line.

The tests show that an integer_ can be ``EQUAL`` to a float_ but an integer_ ``IS`` NOT a float_.

----

*********************************************************************************
a better way to organize tests
*********************************************************************************

I used comments to group the :ref:`assertions<what is an assertion?>` by what I was testing, and each time I made an :ref:`assertion<what is an assertion?>` :ref:`True<test_what_is_true>`, the terminal_ showed a confusing message (``no tests ran``).

Since I am using `pytest-watcher`_ which uses pytest_ to run the test, I can group the :ref:`assertions<what is an assertion?>` with :ref:`functions<what is a function?>` instead.

A :ref:`function<what is a function?>` is code that is callable_, this means I can write code to do something one time, and call the name for it to do that thing at a different time from when I write it.

:ref:`functions<what is a function?>` are made with

* the def_ keyword
* a name
* parentheses and a colon at the end
* the code that makes up the :ref:`function<what is a function?>` (its body) comes after the colon

.. code-block:: python

  def name_of_function():
      the body of the function
      ...

----

=================================================================================
test_assertion_error_w_is_vs_equal
=================================================================================

----

* I add a :ref:`function<what is a function?>` for the ``# test AssertionError with is vs equal`` group of :ref:`assertions<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 4

    assert True == True


    def assertion_error_w_is_vs_equal():
    # test AssertionError with is vs equal
    assert 0 is not 0.0

    assert 0 == 0.0

  the terminal_ is my friend, and shows IndentationError_

  .. code-block:: python

    IndentationError: expected an indented block
                      after function definition on line 89

  because in Python_ the body of a :ref:`function<what is a function?>` is indented under the name.

* I indent the :ref:`assertions<what is an assertion?>` with four spaces to make them the body of the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 5-6, 8

    assert True == True


    def assertion_error_w_is_vs_equal():
        # test AssertionError with is vs equal
        assert 0 is not 0.0

        assert 0 == 0.0


    # NOTES

  the test passes and the terminal_ still shows ``no tests ran``

* I add ``test_`` to the name of the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 4-5

    assert True == True


    # def assertion_error_w_is_vs_equal():
    def test_assertion_error_w_is_vs_equal():
        # test AssertionError with is vs equal
        assert 0 is not 0.0

        assert 0 == 0.0


    # NOTES

  the terminal_ shows :green:`green` and the name of the test file_ with a better message

  .. code-block:: python
    :emphasize-lines: 7, 9

    ================== test session starts ===================
    platform linux -- Python 3.X.Y, pytest-Z.A.B, pluggy-C.D.E
    rootdir: /.../pumping_python/assertion_error
    configfile: pyproject.toml
    collected 1 item

    tests/test_assertion_error.py .                     [100%]

    =================== 1 passed in F.GHs ====================
    [pytest-watcher]
    Current runner args: []
    Press w to show menu

  fantastic! pytest_ only calls the :ref:`function<what is a function?>` if the name starts with ``test``.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 86

    assert True == True


    def test_assertion_error_w_is_vs_equal():
        assert 0 is not 0.0

        assert 0 == 0.0


    # NOTES

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_assertion_error_w_is_vs_equal'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

=================================================================================
test_assertion_error_w_equality
=================================================================================

----

* I add a :ref:`function<what is a function?>` for the ``# test AssertionError with equality`` group of :ref:`assertions<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 4

    assert {} is not True


    def assertion_error_w_equality():
    # test AssertionError with equality
    assert None == None

  the terminal_ is my friend, and shows IndentationError_

  .. code-block:: python

    IndentationError: expected an indented block
                      after function definition on line 75

  because in Python_ the body of a :ref:`function<what is a function?>` is indented under the name.

* I indent the :ref:`assertions<what is an assertion?>` with four spaces to make them the body of the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 5-6, 8, 10, 12, 14, 16

    assert {} is not True


    def assertion_error_w_equality():
        # test AssertionError with equality
        assert None == None

        assert False != None

        assert False != True

        assert False == False

        assert True != None

        assert True == True


    def test_assertion_error_w_is_vs_equal():

  the terminal_ shows

  .. code-block:: python

    =================== 1 passed in L.MNs ====================

  I have two :ref:`functions<what is a function?>` with :ref:`assertions<what is an assertion?>` and it only recognizes one.

* I add ``test_`` to the name of the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 4-5

    assert {} is not True


    # def assertion_error_w_equality():
    def test_assertion_error_w_equality():
        # test AssertionError with equality
        assert None == None

        assert False != None

  the terminal_ shows

  .. code-block:: python

    =================== 2 passed in O.PQs ====================

  because pytest_ only calls the :ref:`function<what is a function?>` if the name starts with ``test``

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 72

    assert {} is not True


    def test_assertion_error_w_equality():
        assert None == None

        assert False != None

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_assertion_error_w_equality'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

=================================================================================
test_assertion_error_w_true
=================================================================================

----

* I add a :ref:`function<what is a function?>` for the ``# test AssertionError with True`` group of :ref:`assertions<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 4

    assert {} is not False


    def assertion_error_w_true():
    # test AssertionError with True
    assert None is not True

  the terminal_ is my friend, and shows IndentationError_

  .. code-block:: python

    IndentationError: expected an indented block
                      after function definition on line 53

  because in Python_ the body of a :ref:`function<what is a function?>` is indented under the name.

* I indent the :ref:`assertions<what is an assertion?>` with four spaces to make them the body of the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 5-6, 8, 10, 12, 14, 16, 18, 20, 22, 24

    assert {} is not False


    def assertion_error_w_true():
        # test AssertionError with True
        assert None is not True

        assert False is not True

        assert True is True

        assert 0 is not True

        assert 0.0 is not True

        assert '' is not True

        assert () is not True

        assert [] is not True

        assert set() is not True

        assert {} is not True


    def test_assertion_error_w_equality():

  the terminal_ shows

  .. code-block:: python

    =================== 2 passed in R.STs ====================

  I have three :ref:`functions<what is a function?>` with :ref:`assertions<what is an assertion?>` and it only recognizes two.

* I add ``test_`` to the name of the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 4-5

    assert {} is not False


    # def assertion_error_w_true():
    def test_assertion_error_w_true():
        # test AssertionError with True
        assert None is not True

        assert False is not True

  the terminal_ shows

  .. code-block:: python

    =================== 3 passed in U.VWs ====================

  because pytest_ only calls the :ref:`function<what is a function?>` if the name starts with ``test``

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 50

    assert {} is not False


    def test_assertion_error_w_true():
        assert None is not True

        assert False is not True

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_assertion_error_w_true'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

=================================================================================
test_assertion_error_w_false
=================================================================================

----

* I add a :ref:`function<what is a function?>` for the ``# test AssertionError with False`` group of :ref:`assertions<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 4

    assert {} is not None


    def assertion_error_w_false():
    # test AssertionError with False
    assert None is not False

  the terminal_ is my friend, and shows IndentationError_

  .. code-block:: python

    IndentationError: expected an indented block
                      after function definition on line 31

  because in Python_ the body of a :ref:`function<what is a function?>` is indented under the name.

* I indent the :ref:`assertions<what is an assertion?>` with four spaces to make them the body of the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 5-6, 8, 10, 12, 14, 16, 18, 20, 22, 24

    assert {} is not None


    def assertion_error_w_false():
        # test AssertionError with False
        assert None is not False

        assert False is False

        assert True is not False

        assert 0 is not False

        assert 0.0 is not False

        assert '' is not False

        assert () is not False

        assert [] is not False

        assert set() is not False

        assert {} is not False


    def test_assertion_error_w_true():


  the terminal_ shows

  .. code-block:: python

    =================== 3 passed in X.YZs ====================

  I have four :ref:`functions<what is a function?>` with :ref:`assertions<what is an assertion?>` and it only recognizes three.

* I add ``test_`` to the name of the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 4-5

    assert {} is not None


    # def assertion_error_w_false():
    def test_assertion_error_w_false():
        # test AssertionError with False
        assert None is not False

        assert False is False

  the terminal_ shows

  .. code-block:: python

    =================== 4 passed in A.BCs ====================

  because pytest_ only calls the :ref:`function<what is a function?>` if the name starts with ``test``

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 28

    assert {} is not None


    def test_assertion_error_w_false():
        assert None is not False

        assert False is False

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_assertion_error_w_false'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

=================================================================================
test_assertion_error_w_none
=================================================================================

----

* I add a :ref:`function<what is a function?>` for the ``# test AssertionError with None`` group of :ref:`assertions<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 4

    assert 'I am' + ' alive' == 'I am alive'


    def assertion_error_w_none():
    # test AssertionError with None
    assert None is None

  the terminal_ is my friend, and shows IndentationError_

  .. code-block:: python

    IndentationError: expected an indented block
                      after function definition on line 9

  because in Python_ the body of a :ref:`function<what is a function?>` is indented under the name.

* I indent the :ref:`assertions<what is an assertion?>` with four spaces to make them the body of the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 5-6, 8, 10, 12, 14, 16, 18, 20, 22, 24

    assert 'I am' + ' alive' == 'I am alive'


    def assertion_error_w_none():
        # test AssertionError with None
        assert None is None

        assert False is not None

        assert True is not None

        assert 0 is not None

        assert 0.0 is not None

        assert '' is not None

        assert () is not None

        assert [] is not None

        assert set() is not None

        assert {} is not None


    def test_assertion_error_w_false():

  the terminal_ shows

  .. code-block:: python

    =================== 4 passed in D.EFs ====================

  I have five :ref:`functions<what is a function?>` with :ref:`assertions<what is an assertion?>` and it only recognizes four.

* I add ``test_`` to the name of the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 4-5

    assert 'I am' + ' alive' == 'I am alive'


    # def assertion_error_w_none():
    def test_assertion_error_w_none():
        # test AssertionError with None
        assert None is None

        assert False is not None

  the terminal_ shows

  .. code-block:: python

    =================== 5 passed in G.HIs ====================

  because pytest_ only calls the :ref:`function<what is a function?>` if the name starts with ``test``

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 6

    assert 'I am' + ' alive' == 'I am alive'


    def test_assertion_error_w_none():
        assert None is None

        assert False is not None

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_assertion_error_w_none'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

=================================================================================
test_assert_keyword
=================================================================================

----

* I add a :ref:`function<what is a function?>` for the ``# test the assert keyword``  group of :ref:`assertions<what is an assertion?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def assert_keyword():
    # test the assert keyword
    assert 1 + 1 == 2

  the terminal_ is my friend, and shows IndentationError_

  .. code-block:: python

    IndentationError: expected an indented block
                      after function definition on line 1

  because in Python_ the body of a :ref:`function<what is a function?>` is indented under the name.

* I indent the :ref:`assertions<what is an assertion?>` with four spaces to make them the body of the :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3, 5, 7

    def assert_keyword():
        # test the assert keyword
        assert 1 + 1 == 2

        assert '1' + '1' == '11'

        assert 'I am' + ' alive' == 'I am alive'


    def test_assertion_error_w_none():

  the terminal_ shows

  .. code-block:: python

    =================== 5 passed in J.KLs ====================

  I have six :ref:`functions<what is a function?>` with :ref:`assertions<what is an assertion?>` and it only recognizes four.

* I add ``test_`` to the name of the :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    # def assert_keyword():
    def test_assert_keyword():
        # test the assert keyword
        assert 1 + 1 == 2

        assert '1' + '1' == '11'

        assert 'I am' + ' alive' == 'I am alive'


    def test_assertion_error_w_none():

  the terminal_ shows

  .. code-block:: python

    =================== 6 passed in M.NOs ====================

  because pytest_ only calls the :ref:`function<what is a function?>` if the name starts with ``test``

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def test_assert_keyword():
        assert 1 + 1 == 2

        assert '1' + '1' == '11'

        assert 'I am' + ' alive' == 'I am alive'


    def test_assertion_error_w_none():

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_assert_keyword'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

=================================================================================
pytest only calls the function if the name starts with test
=================================================================================

----

* I add a :ref:`function<what is a function?>` to show that pytest_ only calls the :ref:`function<what is a function?>` if the name starts with ``test``

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 7-8

    def test_assertion_error_w_is_vs_equal():
        assert 0 is not 0.0

        assert 0 == 0.0


    def will_not_run():
        assert False == True


    # NOTES

  the terminal_ still shows

  .. code-block:: python

    =================== 6 passed in P.QRs ====================

* I add a :ref:`function<what is a function?>` that starts with ``test`` with the same :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 5-6

    def will_not_run():
        assert False == True


    def test_failure():
        assert False == True


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 7, 10, 12, 14, 16, -18-19

    ================== test session starts ===================
    platform linux -- Python 3.X.Y, pytest-Z.A.B, pluggy-C.D.E
    rootdir: /.../pumping_python/assertion_error
    configfile: pyproject.toml
    collected 7 items

    tests/test_assertion_error.py ......F               [100%]

    ======================== FAILURES ========================
    ______________________ test_failure ______________________

        def test_failure():
    >       assert False == True
    E       assert False == True

    tests/test_assertion_error.py:102: AssertionError
    ============== short test summary info ===================
    FAILED tests/test_assertion_error.py::test_failure -
        assert False == True
    ============== 1 failed, 6 passed in T.UVs ===============
    [pytest-watcher]
    Current runner args: []
    Press w to show menu

  - because pytest_ only calls the :ref:`function<what is a function?>` if the name starts with ``test``
  - this has more details than when I write the :ref:`assertions<what is an assertion?>` without a :ref:`function<what is a function?>`.

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 99
    :emphasize-lines: 2-3

    def test_failure():
        # assert False == True
        assert False == False


    # NOTES

  the test passes.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_failure'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_assertion_error.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``assertion_error``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ is my friend, and shows

  .. code-block:: python

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

----

*********************************************************************************
review
*********************************************************************************

* I can use :ref:`assert statements<what is an assertion?>` to test

  * if something is :ref:`None or NOT None<test_assertion_error_w_none>`
  * if something is :ref:`False or NOT False<test_assertion_error_w_false>`
  * if something is :ref:`True or NOT True<test_assertion_error_w_true>`
  * if two things are :ref:`NOT equal or equal<test_assertion_error_w_equality>`

* I can use :ref:`functions<what is a function?>` to group :ref:`assertions<what is an assertion?>` and get better error messages from pytest_

The tests show that

* :ref:`True<test_what_is_true>`, :ref:`False<test_what_is_false>` and :ref:`None<what is None?>` are different
* ``is`` and ``==`` are different

:ref:`How many questions can you answer about AssertionError?<questions about AssertionError>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<AssertionError: tests>`

----

*************************************************************************************
what is next?
*************************************************************************************

Congratulations! You now know

* :ref:`how to make a Python test driven development environment manually`
* :ref:`what a Python module is<what is a module?>`
* :ref:`how to run tests automatically`
* :ref:`what causes AssertionError<what causes AssertionError?>`

:ref:`Would you like to test functions?<what is a function?>`

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