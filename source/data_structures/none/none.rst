.. meta::
  :description: Beginner Python TDD tutorial on None — the simplest data structure / singleton. Step-by-step red-green-refactor with unittest: test_what_is_none using assertIs / assertIsNone / assertIsNotNone, then exhaustive "is None a boolean / int / float / str / tuple / list / set / dict?" tests using assertIsNotNone + assertIsInstance + assertNotIsInstance. Learn exactly why None is not False, not 0, not '', not [], not {}, not 0.0; identity ("is") vs equality ("=="); common None gotchas; and how to test for absence of value. Reproduces real AssertionError messages including "unexpectedly identical: None", "unexpectedly None", and "X is not None". Builds directly on the AssertionError chapters (bare assert, assertIs, test_failure patterns) before booleans/truthiness. Full uv init + pytest-watcher + git workflow. Part of Jacob Itegboje's Pumping Python series.
  :keywords: Jacob Itegboje, Pumping Python, python None, what is None python, NoneType, python None vs False, python None vs 0, python None vs empty list, python None vs empty dict, is None vs == None, assertIsNone, assertIsNotNone, assertIs, assertIsNot, assertIsInstance, assertNotIsInstance, testing for None, None singleton, None identity, None in unittest, TDD None, None is not False, unexpectedly identical None, AssertionError unexpectedly None, False is not None, 0 is not None, simplest data structure python, python data structures TDD, red green refactor None, python None best practices, None vs falsy values, uv pytest-watcher none project

.. include:: ../../links.rst

.. _None: https://docs.python.org/3/library/constants.html?highlight=none#None
.. _assertIsNone: https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertIsNone
.. _assertIsNone method: assertIsNone_
.. _assertIsNotNone: https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertIsNotNone
.. _assertIsNotNone method: assertIsNotNone_
.. _unittest.TestCase.assertIsNone: assertIsNone_
.. _unittest.TestCase.assertIsNotNone: assertIsNotNone_

#################################################################################
None (the simplest object)
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/NKvM2yqyIrQ?si=rXBUptys2D9ns9d8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

I want to use `assert methods`_ to compare :ref:`None<what is None?>` with the other :ref:`Python data structures<data structures>` to see what it is and what it is not.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/tests/test_none.py
  :language: python
  :linenos:

*********************************************************************************
questions about None
*********************************************************************************

Questions to think about as I go through the chapter

* :ref:`what is None?<test_what_is_none>`
* :ref:`Is None a boolean?<test_is_none_a_boolean>`
* :ref:`Is None an integer?<test_is_none_an_integer>`
* :ref:`Is None a float?<test_is_none_a_float>`
* :ref:`Is None a string?<test_is_none_a_string>`
* :ref:`Is None a tuple?<test_is_none_a_tuple>`
* :ref:`Is None a list?<test_is_none_a_list>`
* :ref:`Is None a set?<test_is_none_a_set>`
* :ref:`Is None a dictionary?<test_is_none_a_dictionary>`
* :ref:`how can I test if something is the same object as None?<one more way to test if something is None>`
* :ref:`how can I test if something is NOT the same object as None?<one more way to test if something is NOT None>`

----

*********************************************************************************
requirements
*********************************************************************************

* I name this project ``none``
* I open a terminal_
* I use uv_ to make a directory_ for the project and initialize it

  .. code-block:: python
    :emphasize-lines: 1

    uv init none

  the terminal_ shows

  .. code-block:: shell

    Initialized project `none`
    at `.../pumping_python/none`

  then goes back to the command line.

* I change directory_ to the project

  .. code-block:: python
    :emphasize-lines: 1

    cd none

  the terminal_ shows I am in the ``none`` folder_

  .. code-block:: python

    .../pumping_python/none

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

* I use the `mv program`_ to change the name of ``main.py`` to ``test_none.py`` and move it to the ``tests`` folder_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        mv main.py tests/test_none.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        Move-Item main.py tests/test_none.py

  the terminal_ goes back to the command line.

* I delete the text in the file_ then add :ref:`the first failing test<test_failure>` to ``test_none.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-7

    import unittest


    class TestNone(unittest.TestCase):

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

    git commit -am 'setup project'

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 8, 10

    ======================== FAILURES ========================
    _____________________ TestNone.test_failure ______________________

    self = <tests.test_none.TestNone testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_none.py:7: AssertionError
    ================ short test summary info =================
    FAILED tests/test_none.py::TestNone::test_failure - AssertionError: True is not false
    =================== 1 failed in X.YZs ====================

  because :ref:`True<test_what_is_true>` is NOT :ref:`False<test_what_is_false>`

  .. admonition:: if the terminal_ does not show the same error, then check

    * if your ``tests/__init__.py`` has two underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``
    * if you ran ``echo "pytest-watcher" >> requirements.txt``, to add ``pytest-watcher`` to the requirements file_

    fix those errors and try to run ``uv run pytest-watcher . --now`` again

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_none.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7-8
    :emphasize-text: AssertionError

    class TestNone(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions seen
    # AssertionError

* I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

  the test passes.

----

*********************************************************************************
test_what_is_none
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I change :ref:`test_failure` to ``test_what_is_none``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3-4
    :emphasize-text: Not

    class TestNone(unittest.TestCase):

        def test_what_is_none(self):
            self.assertIsNot(None, None)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: unexpectedly identical: None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`assertIsNot<another way to test if something is NOT the same object as None>` to :ref:`assertIs<another way to test if something is the same object as None>`

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 2-3

      def test_what_is_none(self):
          # self.assertIsNot(None, None)
          self.assertIs(None, None)


  # Exceptions seen

the test passes. So far this is the same as :ref:`test_assertion_error_w_none`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

I can also use another `assert method`_ from the `unittest.TestCase class`_ to test if something is NOT the same :ref:`object<everything is an object>` as :ref:`None<what is None?>`.

----

---------------------------------------------------------------------------------
one more way to test if something is NOT None
---------------------------------------------------------------------------------

----

* I add an :ref:`assertion<what is an assertion?>` with the `assertIsNotNone method`_

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 4

        def test_what_is_none(self):
            # self.assertIsNot(None, None)
            self.assertIs(None, None)
            self.assertIsNotNone(None)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: unexpectedly None

  because :ref:`assertIsNotNone<one more way to test if something is NOT None>` raises :ref:`AssertionError<what causes AssertionError?>` if the :ref:`object<everything is an object>` given in parentheses is :ref:`None<what is None?>`.

----

---------------------------------------------------------------------------------
one more way to test if something is None
---------------------------------------------------------------------------------

----

* I change :ref:`assertIsNotNone<one more way to test if something is NOT None>` to the `assertIsNone method`_

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 4-5

        def test_what_is_none(self):
            # self.assertIsNot(None, None)
            self.assertIs(None, None)
            # self.assertIsNotNone(None)
            self.assertIsNone(None)


    # Exceptions seen

  the test passes because :ref:`None is None<what is None?>` and :ref:`assertIsNotNone<one more way to test if something is NOT None>` raises :ref:`AssertionError<what causes AssertionError?>` if the :ref:`object<everything is an object>` given in parentheses is NOT :ref:`None<what is None?>`.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 6

        def test_what_is_none(self):
            self.assertIs(None, None)
            self.assertIsNone(None)


    # Exceptions seen
    # AssertionError

* I add comments

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 8-9

    class TestNone(unittest.TestCase):

        def test_what_is_none(self):
            self.assertIs(None, None)
            self.assertIsNone(None)


    # NOTES
    # None is None


    # Exceptions seen
    # AssertionError

  this is the same comment from :ref:`the assertion_error chapter<what is an assertion?>`

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_what_is_none'


:ref:`None is None<test_what_is_none>`.

----

*********************************************************************************
test_is_none_a_boolean
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test to see if :ref:`None<what is None?>` is a :ref:`boolean<what are booleans?>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 5-6

        def test_what_is_none(self):
            self.assertIs(None, None)
            self.assertIsNone(None)

        def test_is_none_a_boolean(self):
            self.assertIsNone(False)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I make the :ref:`assertion<what is an assertion?>` :ref:`True<test_what_is_true>` with the `assertIsNotNone method`_

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 2-3

      def test_is_none_a_boolean(self):
          # self.assertIsNone(False)
          self.assertIsNotNone(False)


  # NOTES

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a comment

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 2

    # NOTES
    # False is NOT None
    # None is None


    # Exceptions seen
    # AssertionError

  another comment from :ref:`the assertion_error chapter<what is an assertion?>`.

* I add an :ref:`assertion<what is an assertion?>` for the other :ref:`boolean<what are booleans?>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 4
    :emphasize-text: True

        def test_is_none_a_boolean(self):
            # self.assertIsNone(False)
            self.assertIsNotNone(False)
            self.assertIsNone(True)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not None

* I make the :ref:`assertion<what is an assertion?>` :ref:`True<test_what_is_true>` with :ref:`assertIsNotNone<one more way to test if something is NOT None>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 4-5
    :emphasize-text: Not

        def test_is_none_a_boolean(self):
            # self.assertIsNone(False)
            self.assertIsNotNone(False)
            # self.assertIsNone(True)
            self.assertIsNotNone(True)


    # NOTES

  the test passes.

* I add a comment

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 2

    # NOTES
    # True is NOT None
    # False is NOT None
    # None is None

  also a comment from :ref:`the assertion_error chapter<what is an assertion?>`

* I add a call to the :ref:`assertNotIsInstance method<another way to test if something is NOT an instance of a class>` to test if :ref:`False<test_what_is_false>` is :ref:`an instance<how to test if something is an instance of a class>` of the :ref:`bool class<what are booleans?>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 6
    :emphasize-text: assertNotIsInstance

        def test_is_none_a_boolean(self):
            # self.assertIsNone(False)
            self.assertIsNotNone(False)
            # self.assertIsNone(True)
            self.assertIsNotNone(True)
            self.assertNotIsInstance(False, bool)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is an instance of <class 'bool'>

  because :ref:`False<test_what_is_false>` is :ref:`an instance<how to test if something is an instance of a class>` of the :ref:`bool class<what are booleans?>`.

* I change :ref:`assertNotIsInstance<another way to test if something is NOT an instance of a class>` to the :ref:`assertIsInstance method<another way to test if something is an instance of a class>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 6-7

        def test_is_none_a_boolean(self):
            # self.assertIsNone(False)
            self.assertIsNotNone(False)
            # self.assertIsNone(True)
            self.assertIsNotNone(True)
            # self.assertNotIsInstance(False, bool)
            self.assertIsInstance(False, bool)


    # NOTES

  the test passes.

* I add a failing line for the other :ref:`boolean<what are booleans?>` with :ref:`assertNotIsInstance<another way to test if something is NOT an instance of a class>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 8
    :emphasize-text: assertNotIsInstance

        def test_is_none_a_boolean(self):
            # self.assertIsNone(False)
            self.assertIsNotNone(False)
            # self.assertIsNone(True)
            self.assertIsNotNone(True)
            # self.assertNotIsInstance(False, bool)
            self.assertIsInstance(False, bool)
            self.assertNotIsInstance(True, bool)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is an instance of <class 'bool'>

  because :ref:`True<test_what_is_true>` is :ref:`an instance<how to test if something is an instance of a class>` of the :ref:`bool class<what are booleans?>`.

* I make the statement :ref:`True<test_what_is_true>` with :ref:`assertIsInstance<another way to test if something is an instance of a class>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 8-9

        def test_is_none_a_boolean(self):
            # self.assertIsNone(False)
            self.assertIsNotNone(False)
            # self.assertIsNone(True)
            self.assertIsNotNone(True)
            # self.assertNotIsInstance(False, bool)
            self.assertIsInstance(False, bool)
            # self.assertNotIsInstance(True, bool)
            self.assertIsInstance(True, bool)


    # NOTES

  the test passes.

* I add :ref:`assertIsInstance<another way to test if something is an instance of a class>` to test if :ref:`None<what is None?>` is :ref:`an instance (a copy)<how to test if something is an instance of a class>` of the :ref:`bool class<what are booleans?>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 10

        def test_is_none_a_boolean(self):
            # self.assertIsNone(False)
            self.assertIsNotNone(False)
            # self.assertIsNone(True)
            self.assertIsNotNone(True)
            # self.assertNotIsInstance(False, bool)
            self.assertIsInstance(False, bool)
            # self.assertNotIsInstance(True, bool)
            self.assertIsInstance(True, bool)
            self.assertIsInstance(None, bool)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'bool'>

  because :ref:`None<what is None?>` is NOT a :ref:`boolean<what are booleans?>`.

* I make the line :ref:`True<test_what_is_true>` with :ref:`assertNotIsInstance<another way to test if something is NOT an instance of a class>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 10-11

        def test_is_none_a_boolean(self):
            # self.assertIsNone(False)
            self.assertIsNotNone(False)
            # self.assertIsNone(True)
            self.assertIsNotNone(True)
            # self.assertNotIsInstance(False, bool)
            self.assertIsInstance(False, bool)
            # self.assertNotIsInstance(True, bool)
            self.assertIsInstance(True, bool)
            # self.assertIsInstance(None, bool)
            self.assertNotIsInstance(None, bool)


    # NOTES

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 10

        def test_is_none_a_boolean(self):
            self.assertIsNotNone(False)
            self.assertIsNotNone(True)
            self.assertIsInstance(False, bool)
            self.assertIsInstance(True, bool)
            self.assertNotIsInstance(None, bool)


    # NOTES

* I change the last 2 comments I added (``True is NOT None`` and ``False is NOT None``), since this is about :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 2

    # NOTES
    # None is NOT a boolean
    # None is None


    # Exceptions seen
    # AssertionError

  Okay, this is new, not something from :ref:`the assertion_error chapter<what is an assertion?>`.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_is_none_a_boolean'

:ref:`None is NOT a boolean<test_is_none_a_boolean>`.

I know two new `assert methods`_

* :ref:`assertIsNotNone<one more way to test if something is NOT None>` to test if something is NOT :ref:`None<what is None?>`
* :ref:`assertIsNone<one more way to test if something is None>` to test if something is :ref:`None<what is None?>`

.. caution:: the names of the `assert methods`_ can be confusing,

  * there is ``assertIsNotNone`` where ``Not`` comes after ``Is``

  * then there is ``assertNotIsInstance`` where ``Is`` comes after ``Not``

  Would ``assertIsNotInstance`` be better than ``assertNotIsInstance``, since ``assertNotIsNone`` does not sound better than ``assertIsNotNone``? In this case no, because the names of the `assert methods`_ match the assert statements they replace

  * ``assertIsNotNone(x)`` for ``assert x is not None``
  * ``assertNotIsInstance(x, y)`` for ``assert not isinstance(x, y)``

----

*********************************************************************************
test_is_none_an_integer
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test to see if :ref:`None<what is None?>` is an integer_ (a whole number)

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 8-9

        def test_is_none_a_boolean(self):
            self.assertIsNotNone(False)
            self.assertIsNotNone(True)
            self.assertIsInstance(False, bool)
            self.assertIsInstance(True, bool)
            self.assertNotIsInstance(None, bool)

        def test_is_none_an_integer(self):
            self.assertIsNone(-1)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: -1 is not None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I make the statement :ref:`True<test_what_is_true>` with :ref:`assertIsNotNone<one more way to test if something is NOT None>`

.. code-block:: python
  :lineno-start: 17
  :emphasize-lines: 2-3

      def test_is_none_an_integer(self):
          # self.assertIsNone(-1)
          self.assertIsNotNone(-1)


  # NOTES

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a new failing line with :ref:`assertIsNotNone<one more way to test if something is NOT None>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 4

        def test_is_none_an_integer(self):
            # self.assertIsNone(-1)
            self.assertIsNotNone(-1)
            self.assertIsNone(0)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0 is not None

* I make the statement :ref:`True<test_what_is_true>` with :ref:`assertIsNotNone<one more way to test if something is NOT None>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 4-5

        def test_is_none_an_integer(self):
            # self.assertIsNone(-1)
            self.assertIsNotNone(-1)
            # self.assertIsNone(0)
            self.assertIsNotNone(0)


    # NOTES

  the test passes.

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 6

        def test_is_none_an_integer(self):
            # self.assertIsNone(-1)
            self.assertIsNotNone(-1)
            # self.assertIsNone(0)
            self.assertIsNotNone(0)
            self.assertIsNone(1)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 1 is not None

* I change the line to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 6-7

        def test_is_none_an_integer(self):
            # self.assertIsNone(-1)
            self.assertIsNotNone(-1)
            # self.assertIsNone(0)
            self.assertIsNotNone(0)
            # self.assertIsNone(1)
            self.assertIsNotNone(1)


    # NOTES

  the test passes.

* I add a new failing line with :ref:`assertNotIsInstance<another way to test if something is NOT an instance of a class>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 8

        def test_is_none_an_integer(self):
            # self.assertIsNone(-1)
            self.assertIsNotNone(-1)
            # self.assertIsNone(0)
            self.assertIsNotNone(0)
            # self.assertIsNone(1)
            self.assertIsNotNone(1)
            self.assertNotIsInstance(-1, int)


    # NOTES

  - int_ is the :ref:`class<what is a class?>` for integers_
  - the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

    .. code-block:: shell

      AssertionError: -1 is an instance of <class 'int'>

    because ``-1`` is an integer_

  - I use ``-1`` for all the integers_ (whole numbers) that are smaller than ``0``

* I make the line :ref:`True<test_what_is_true>` with :ref:`assertIsInstance<another way to test if something is an instance of a class>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 8-9

        def test_is_none_an_integer(self):
            # self.assertIsNone(-1)
            self.assertIsNotNone(-1)
            # self.assertIsNone(0)
            self.assertIsNotNone(0)
            # self.assertIsNone(1)
            self.assertIsNotNone(1)
            # self.assertNotIsInstance(-1, int)
            self.assertIsInstance(-1, int)


    # NOTES

  the test passes.

* I add another failing line with :ref:`assertNotIsInstance<another way to test if something is NOT an instance of a class>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 10

        def test_is_none_an_integer(self):
            # self.assertIsNone(-1)
            self.assertIsNotNone(-1)
            # self.assertIsNone(0)
            self.assertIsNotNone(0)
            # self.assertIsNone(1)
            self.assertIsNotNone(1)
            # self.assertNotIsInstance(-1, int)
            self.assertIsInstance(-1, int)
            self.assertNotIsInstance(0, int)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 0 is an instance of <class 'int'>

  because ``0`` is an integer_.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 10-11

        def test_is_none_an_integer(self):
            # self.assertIsNone(-1)
            self.assertIsNotNone(-1)
            # self.assertIsNone(0)
            self.assertIsNotNone(0)
            # self.assertIsNone(1)
            self.assertIsNotNone(1)
            # self.assertNotIsInstance(-1, int)
            self.assertIsInstance(-1, int)
            # self.assertNotIsInstance(0, int)
            self.assertIsInstance(0, int)


    # NOTES

  the test passes.

* I add another failing line with :ref:`assertNotIsInstance<another way to test if something is NOT an instance of a class>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 12

        def test_is_none_an_integer(self):
            # self.assertIsNone(-1)
            self.assertIsNotNone(-1)
            # self.assertIsNone(0)
            self.assertIsNotNone(0)
            # self.assertIsNone(1)
            self.assertIsNotNone(1)
            # self.assertNotIsInstance(-1, int)
            self.assertIsInstance(-1, int)
            # self.assertNotIsInstance(0, int)
            self.assertIsInstance(0, int)
            self.assertNotIsInstance(1, int)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 1 is an instance of <class 'int'>

  - because ``1`` is an integer_
  - I use ``1`` for all the integers_ (whole numbers) that are bigger than ``0``

* I make the failing line :ref:`True<test_what_is_true>` with :ref:`assertIsInstance<another way to test if something is an instance of a class>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 12-13

        def test_is_none_an_integer(self):
            # self.assertIsNone(-1)
            self.assertIsNotNone(-1)
            # self.assertIsNone(0)
            self.assertIsNotNone(0)
            # self.assertIsNone(1)
            self.assertIsNotNone(1)
            # self.assertNotIsInstance(-1, int)
            self.assertIsInstance(-1, int)
            # self.assertNotIsInstance(0, int)
            self.assertIsInstance(0, int)
            # self.assertNotIsInstance(1, int)
            self.assertIsInstance(1, int)


    # NOTES

  the test passes.

* I add one more failing line to test if :ref:`None<what is None?>` is an integer_ with :ref:`assertIsInstance<another way to test if something is an instance of a class>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 14

        def test_is_none_an_integer(self):
            # self.assertIsNone(-1)
            self.assertIsNotNone(-1)
            # self.assertIsNone(0)
            self.assertIsNotNone(0)
            # self.assertIsNone(1)
            self.assertIsNotNone(1)
            # self.assertNotIsInstance(-1, int)
            self.assertIsInstance(-1, int)
            # self.assertNotIsInstance(0, int)
            self.assertIsInstance(0, int)
            # self.assertNotIsInstance(1, int)
            self.assertIsInstance(1, int)
            self.assertIsInstance(None, int)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'int'>

* I make the line :ref:`True<test_what_is_true>` with :ref:`assertNotIsInstance<another way to test if something is NOT an instance of a class>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 14-15

        def test_is_none_an_integer(self):
            # self.assertIsNone(-1)
            self.assertIsNotNone(-1)
            # self.assertIsNone(0)
            self.assertIsNotNone(0)
            # self.assertIsNone(1)
            self.assertIsNotNone(1)
            # self.assertNotIsInstance(-1, int)
            self.assertIsInstance(-1, int)
            # self.assertNotIsInstance(0, int)
            self.assertIsInstance(0, int)
            # self.assertNotIsInstance(1, int)
            self.assertIsInstance(1, int)
            # self.assertIsInstance(None, int)
            self.assertNotIsInstance(None, int)


    # NOTES

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 17

        def test_is_none_an_integer(self):
            self.assertIsNotNone(-1)
            self.assertIsNotNone(0)
            self.assertIsNotNone(1)
            self.assertIsInstance(-1, int)
            self.assertIsInstance(0, int)
            self.assertIsInstance(1, int)
            self.assertNotIsInstance(None, int)


    # NOTES

* I add a new comment

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 2

    # NOTES
    # None is NOT an integer
    # None is NOT a boolean
    # None is None


    # Exceptions seen
    # AssertionError

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_is_none_an_integer'

:ref:`None is NOT an integer<test_is_none_an_integer>`.

----

*********************************************************************************
test_is_none_a_float
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test to see if :ref:`None<what is None?>` is a float_ (binary floating point decimal number)

.. code-block:: python
  :lineno-start: 17
  :emphasize-lines: 10-11

      def test_is_none_an_integer(self):
          self.assertIsNotNone(-1)
          self.assertIsNotNone(0)
          self.assertIsNotNone(1)
          self.assertIsInstance(-1, int)
          self.assertIsInstance(0, int)
          self.assertIsInstance(1, int)
          self.assertNotIsInstance(None, int)

      def test_is_none_a_float(self):
          self.assertIsNone(-0.1)


  # NOTES

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: -0.1 is not None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I make the statement :ref:`True<test_what_is_true>` with :ref:`assertIsNotNone<one more way to test if something is NOT None>`

.. code-block:: python
  :lineno-start: 26
  :emphasize-lines: 2-3

      def test_is_none_a_float(self):
          # self.assertIsNone(-0.1)
          self.assertIsNotNone(-0.1)


  # NOTES

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a call to :ref:`assertIsNone<one more way to test if something is None>`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 4

        def test_is_none_a_float(self):
            # self.assertIsNone(-0.1)
            self.assertIsNotNone(-0.1)
            self.assertIsNone(0.0)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0.0 is not None

* I make the statement :ref:`True<test_what_is_true>` with :ref:`assertIsNotNone<one more way to test if something is NOT None>`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 4-5

        def test_is_none_a_float(self):
            # self.assertIsNone(-0.1)
            self.assertIsNotNone(-0.1)
            # self.assertIsNone(0.0)
            self.assertIsNotNone(0.0)


    # NOTES

  the test passes.

* I add another call to :ref:`assertIsNone<one more way to test if something is None>`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 6

        def test_is_none_a_float(self):
            # self.assertIsNone(-0.1)
            self.assertIsNotNone(-0.1)
            # self.assertIsNone(0.0)
            self.assertIsNotNone(0.0)
            self.assertIsNone(0.1)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0.1 is not None

* I make the statement :ref:`True<test_what_is_true>` with :ref:`assertIsNotNone<one more way to test if something is NOT None>`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 6-7

        def test_is_none_a_float(self):
            # self.assertIsNone(-0.1)
            self.assertIsNotNone(-0.1)
            # self.assertIsNone(0.0)
            self.assertIsNotNone(0.0)
            # self.assertIsNone(0.1)
            self.assertIsNotNone(0.1)


    # NOTES

  the test passes. Time for :ref:`instance tests<how to test if something is an instance of a class>`.

* I add a failing line with :ref:`assertNotIsInstance<another way to test if something is NOT an instance of a class>`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 8

        def test_is_none_a_float(self):
            # self.assertIsNone(-0.1)
            self.assertIsNotNone(-0.1)
            # self.assertIsNone(0.0)
            self.assertIsNotNone(0.0)
            # self.assertIsNone(0.1)
            self.assertIsNotNone(0.1)
            self.assertNotIsInstance(-0.1, float)


    # NOTES

  float_ is the :ref:`class<what is a class?>` for binary floating point numbers. the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: -0.1 is an instance of <class 'float'>

  - because ``-0.1`` is a float_
  - I use ``-0.1`` for all the binary floating point numbers that are smaller than ``0.0``

* I make the statement :ref:`True<test_what_is_true>` with :ref:`assertIsInstance<another way to test if something is an instance of a class>`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 8-9

        def test_is_none_a_float(self):
            # self.assertIsNone(-0.1)
            self.assertIsNotNone(-0.1)
            # self.assertIsNone(0.0)
            self.assertIsNotNone(0.0)
            # self.assertIsNone(0.1)
            self.assertIsNotNone(0.1)
            # self.assertNotIsInstance(-0.1, float)
            self.assertIsInstance(-0.1, float)


    # NOTES

  the test passes.

* I add the next :ref:`instance test<how to test if something is an instance of a class>` with :ref:`assertNotIsInstance<another way to test if something is NOT an instance of a class>`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 10

        def test_is_none_a_float(self):
            # self.assertIsNone(-0.1)
            self.assertIsNotNone(-0.1)
            # self.assertIsNone(0.0)
            self.assertIsNotNone(0.0)
            # self.assertIsNone(0.1)
            self.assertIsNotNone(0.1)
            # self.assertNotIsInstance(-0.1, float)
            self.assertIsInstance(-0.1, float)
            self.assertNotIsInstance(0.0, float)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 0.0 is an instance of <class 'float'>

  because ``0.0`` is a binary floating point number

* I make the statement :ref:`True<test_what_is_true>` with :ref:`assertIsInstance<another way to test if something is an instance of a class>`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 10-11

        def test_is_none_a_float(self):
            # self.assertIsNone(-0.1)
            self.assertIsNotNone(-0.1)
            # self.assertIsNone(0.0)
            self.assertIsNotNone(0.0)
            # self.assertIsNone(0.1)
            self.assertIsNotNone(0.1)
            # self.assertNotIsInstance(-0.1, float)
            self.assertIsInstance(-0.1, float)
            # self.assertNotIsInstance(0.0, float)
            self.assertIsInstance(0.0, float)


    # NOTES

  the test passes.

* I add a failing line with :ref:`assertNotIsInstance<another way to test if something is NOT an instance of a class>`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 12

        def test_is_none_a_float(self):
            # self.assertIsNone(-0.1)
            self.assertIsNotNone(-0.1)
            # self.assertIsNone(0.0)
            self.assertIsNotNone(0.0)
            # self.assertIsNone(0.1)
            self.assertIsNotNone(0.1)
            # self.assertNotIsInstance(-0.1, float)
            self.assertIsInstance(-0.1, float)
            # self.assertNotIsInstance(0.0, float)
            self.assertIsInstance(0.0, float)
            self.assertNotIsInstance(0.1, float)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 0.1 is an instance of <class 'float'>

  - because ``0.1`` is a float_
  - I use ``0.1`` for all the binary floating point numbers that are bigger than ``0.0``

* I make the statement :ref:`True<test_what_is_true>` with :ref:`assertIsInstance<another way to test if something is an instance of a class>`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 12-13

        def test_is_none_a_float(self):
            # self.assertIsNone(-0.1)
            self.assertIsNotNone(-0.1)
            # self.assertIsNone(0.0)
            self.assertIsNotNone(0.0)
            # self.assertIsNone(0.1)
            self.assertIsNotNone(0.1)
            # self.assertNotIsInstance(-0.1, float)
            self.assertIsInstance(-0.1, float)
            # self.assertNotIsInstance(0.0, float)
            self.assertIsInstance(0.0, float)
            # self.assertNotIsInstance(0.1, float)
            self.assertIsInstance(0.1, float)


    # NOTES

  the test passes.

* I add one more failing line with the :ref:`assertIsInstance method<another way to test if something is an instance of a class>`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 14

        def test_is_none_a_float(self):
            # self.assertIsNone(-0.1)
            self.assertIsNotNone(-0.1)
            # self.assertIsNone(0.0)
            self.assertIsNotNone(0.0)
            # self.assertIsNone(0.1)
            self.assertIsNotNone(0.1)
            # self.assertNotIsInstance(-0.1, float)
            self.assertIsInstance(-0.1, float)
            # self.assertNotIsInstance(0.0, float)
            self.assertIsInstance(0.0, float)
            # self.assertNotIsInstance(0.1, float)
            self.assertIsInstance(0.1, float)
            self.assertIsInstance(None, float)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'float'>

  because :ref:`None<what is None?>` is not a :ref:`boolean<what are booleans?>`.

* I make the statement :ref:`True<test_what_is_true>` with the :ref:`assertNotIsInstance method<another way to test if something is NOT an instance of a class>`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 14-15

        def test_is_none_a_float(self):
            # self.assertIsNone(-0.1)
            self.assertIsNotNone(-0.1)
            # self.assertIsNone(0.0)
            self.assertIsNotNone(0.0)
            # self.assertIsNone(0.1)
            self.assertIsNotNone(0.1)
            # self.assertNotIsInstance(-0.1, float)
            self.assertIsInstance(-0.1, float)
            # self.assertNotIsInstance(0.0, float)
            self.assertIsInstance(0.0, float)
            # self.assertNotIsInstance(0.1, float)
            self.assertIsInstance(0.1, float)
            # self.assertIsInstance(None, float)
            self.assertNotIsInstance(None, float)


    # NOTES

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 26

        def test_is_none_a_float(self):
            self.assertIsNotNone(-0.1)
            self.assertIsNotNone(0.0)
            self.assertIsNotNone(0.1)
            self.assertIsInstance(-0.1, float)
            self.assertIsInstance(0.0, float)
            self.assertIsInstance(0.1, float)
            self.assertNotIsInstance(None, float)


    # NOTES

* I add a new comment

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 2

    # NOTES
    # None is NOT a float
    # None is NOT an integer
    # None is NOT a boolean
    # None is None


    # Exceptions seen
    # AssertionError

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_is_none_a_float'

:ref:`None is NOT a float<test_is_none_a_float>`.

----

*********************************************************************************
test_is_none_a_string
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test to see if :ref:`None<what is None?>` is a string_ (anything inside :ref:`quotes`)

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 10-11

        def test_is_none_a_float(self):
            self.assertIsNotNone(-0.1)
            self.assertIsNotNone(0.0)
            self.assertIsNotNone(0.1)
            self.assertIsInstance(-0.1, float)
            self.assertIsInstance(0.0, float)
            self.assertIsInstance(0.1, float)
            self.assertNotIsInstance(None, float)

        def test_is_none_a_string(self):
            self.assertIsNone('')


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '' is not None

  because the empty string_ (``''``) is NOT :ref:`None<what is None?>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I make the statement :ref:`True<test_what_is_true>` with :ref:`assertIsNotNone<one more way to test if something is NOT None>`

.. code-block:: python
  :lineno-start: 35
  :emphasize-lines: 2-3

      def test_is_none_a_string(self):
          # self.assertIsNone('')
          self.assertIsNotNone('')


  # NOTES

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a call to :ref:`assertIsNone<one more way to test if something is None>`

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 4

        def test_is_none_a_string(self):
            # self.assertIsNone('')
            self.assertIsNotNone('')
            self.assertIsNone("characters")

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'text' is not None

* I change the `assert method`_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 4-5

        def test_is_none_a_string(self):
            # self.assertIsNone('')
            self.assertIsNotNone('')
            # self.assertIsNone("characters")
            self.assertIsNotNone("characters")


    # NOTES

  the test passes.

* I add a failing line with :ref:`assertNotIsInstance<another way to test if something is NOT an instance of a class>`

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 6

        def test_is_none_a_string(self):
            # self.assertIsNone('')
            self.assertIsNotNone('')
            # self.assertIsNone("characters")
            self.assertIsNotNone("characters")
            self.assertNotIsInstance('', str)


    # NOTES

  - str_ is the :ref:`class<what is a class?>` for strings_
  - the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

    .. code-block:: shell

      AssertionError: '' is an instance of <class 'str'>

    because anything in :ref:`quotes` is a string_

* I change the `assert method`_

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 6-7

        def test_is_none_a_string(self):
            # self.assertIsNone('')
            self.assertIsNotNone('')
            # self.assertIsNone("characters")
            self.assertIsNotNone("characters")
            # self.assertNotIsInstance('', str)
            self.assertIsInstance('', str)


    # NOTES

  the test passes.

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 8

        def test_is_none_a_string(self):
            # self.assertIsNone('')
            self.assertIsNotNone('')
            # self.assertIsNone("characters")
            self.assertIsNotNone("characters")
            # self.assertNotIsInstance('', str)
            self.assertIsInstance('', str)
            self.assertNotIsInstance("characters", str)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 'text' is an instance of <class 'str'>

  because anything in :ref:`quotes` is a string_.

* I change the `assert method`_

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 8-9

        def test_is_none_a_string(self):
            # self.assertIsNone('')
            self.assertIsNotNone('')
            # self.assertIsNone("characters")
            self.assertIsNotNone("characters")
            # self.assertNotIsInstance('', str)
            self.assertIsInstance('', str)
            # self.assertNotIsInstance("characters", str)
            self.assertIsInstance("characters", str)


    # NOTES

  the test passes.

* I add another failing line with :ref:`assertIsInstance<another way to test if something is an instance of a class>`

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 10

        def test_is_none_a_string(self):
            # self.assertIsNone('')
            self.assertIsNotNone('')
            # self.assertIsNone("characters")
            self.assertIsNotNone("characters")
            # self.assertNotIsInstance('', str)
            self.assertIsInstance('', str)
            # self.assertNotIsInstance("characters", str)
            self.assertIsInstance("characters", str)
            self.assertIsInstance(None, str)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'str'>

* I change the `assert method`_

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 10-11

        def test_is_none_a_string(self):
            # self.assertIsNone('')
            self.assertIsNotNone('')
            # self.assertIsNone("characters")
            self.assertIsNotNone("characters")
            # self.assertNotIsInstance('', str)
            self.assertIsInstance('', str)
            # self.assertNotIsInstance("characters", str)
            self.assertIsInstance("characters", str)
            # self.assertIsInstance(None, str)
            self.assertNotIsInstance(None, str)


    # NOTES

  the test passes because :ref:`None<what is None?>` is not a string_.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 35

        def test_is_none_a_string(self):
            self.assertIsNotNone('')
            self.assertIsNotNone("characters")
            self.assertIsInstance('', str)
            self.assertIsInstance("characters", str)
            self.assertNotIsInstance(None, str)


    # NOTES

* I add a comment

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 2

    # NOTES
    # None is NOT a string
    # None is NOT a float
    # None is NOT an integer
    # None is NOT a boolean
    # None is None


    # Exceptions seen
    # AssertionError

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_is_none_a_string'

:ref:`None is NOT a string<test_is_none_a_string>`.

----

*********************************************************************************
test_is_none_a_tuple
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test to see if :ref:`None<what is None?>` is a tuple_ (anything in parentheses (``( )``) separated by commas), pronounced ``two-pull``

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 8-9

        def test_is_none_a_string(self):
            self.assertIsNotNone('')
            self.assertIsNotNone("characters")
            self.assertIsInstance('', str)
            self.assertIsInstance("characters", str)
            self.assertNotIsInstance(None, str)

        def test_is_none_a_tuple(self):
            self.assertIsNone(())


    # NOTES

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: () is not None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I make the statement :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 42
  :emphasize-lines: 2-3
  :emphasize-text: Not

      def test_is_none_a_tuple(self):
          # self.assertIsNone(())
          self.assertIsNotNone(())


  # NOTES

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a failing :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 4

        def test_is_none_a_tuple(self):
            # self.assertIsNone(())
            self.assertIsNotNone(())
            self.assertIsNone((0, 1, 2, 'n'))


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (0, 1, 2, 'n') is not None

* I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 4-5
    :emphasize-text: Not

        def test_is_none_a_tuple(self):
            # self.assertIsNone(())
            self.assertIsNotNone(())
            # self.assertIsNone((0, 1, 2, 'n'))
            self.assertIsNotNone((0, 1, 2, 'n'))


    # NOTES

  the test passes.

* I add a failing line with :ref:`assertNotIsInstance<another way to test if something is NOT an instance of a class>`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 6

        def test_is_none_a_tuple(self):
            # self.assertIsNone(())
            self.assertIsNotNone(())
            # self.assertIsNone((0, 1, 2, 'n'))
            self.assertIsNotNone((0, 1, 2, 'n'))
            self.assertNotIsInstance((), tuple)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: () is an instance of <class 'tuple'>

  because in Python_ anything in parentheses (``( )``) separated by commas is a tuple_.

* I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 6-7

        def test_is_none_a_tuple(self):
            # self.assertIsNone(())
            self.assertIsNotNone(())
            # self.assertIsNone((0, 1, 2, 'n'))
            self.assertIsNotNone((0, 1, 2, 'n'))
            # self.assertNotIsInstance((), tuple)
            self.assertIsInstance((), tuple)


    # NOTES

  the test passes.

* I add another failing line

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 8

        def test_is_none_a_tuple(self):
            # self.assertIsNone(())
            self.assertIsNotNone(())
            # self.assertIsNone((0, 1, 2, 'n'))
            self.assertIsNotNone((0, 1, 2, 'n'))
            # self.assertNotIsInstance((), tuple)
            self.assertIsInstance((), tuple)
            self.assertNotIsInstance((0, 1, 2, 'n'), tuple)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (0, 1, 2, 'n') is an instance of <class 'tuple'>

  because in Python_ anything in parentheses (``( )``) separated by commas is a tuple_.

* I change the `assert method`_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 8-9

        def test_is_none_a_tuple(self):
            # self.assertIsNone(())
            self.assertIsNotNone(())
            # self.assertIsNone((0, 1, 2, 'n'))
            self.assertIsNotNone((0, 1, 2, 'n'))
            # self.assertNotIsInstance((), tuple)
            self.assertIsInstance((), tuple)
            # self.assertNotIsInstance((0, 1, 2, 'n'), tuple)
            self.assertIsInstance((0, 1, 2, 'n'), tuple)


    # NOTES

  the test passes.

* I add one more :ref:`instance test<how to test if something is an instance of a class>`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 10

        def test_is_none_a_tuple(self):
            # self.assertIsNone(())
            self.assertIsNotNone(())
            # self.assertIsNone((0, 1, 2, 'n'))
            self.assertIsNotNone((0, 1, 2, 'n'))
            # self.assertNotIsInstance((), tuple)
            self.assertIsInstance((), tuple)
            # self.assertNotIsInstance((0, 1, 2, 'n'), tuple)
            self.assertIsInstance((0, 1, 2, 'n'), tuple)
            self.assertIsInstance(None, tuple)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'tuple'>

  because :ref:`None<what is None?>` is not a tuple_.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 10-11

        def test_is_none_a_tuple(self):
            # self.assertIsNone(())
            self.assertIsNotNone(())
            # self.assertIsNone((0, 1, 2, 'n'))
            self.assertIsNotNone((0, 1, 2, 'n'))
            # self.assertNotIsInstance((), tuple)
            self.assertIsInstance((), tuple)
            # self.assertNotIsInstance((0, 1, 2, 'n'), tuple)
            self.assertIsInstance((0, 1, 2, 'n'), tuple)
            # self.assertIsInstance(None, tuple)
            self.assertNotIsInstance(None, tuple)


    # NOTES

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 42

        def test_is_none_a_tuple(self):
            self.assertIsNotNone(())
            self.assertIsNotNone((0, 1, 2, 'n'))
            self.assertIsInstance((), tuple)
            self.assertIsInstance((0, 1, 2, 'n'), tuple)
            self.assertNotIsInstance(None, tuple)


    # NOTES

* I add a comment

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 2

    # NOTES
    # None is NOT a tuple
    # None is NOT a string
    # None is NOT a float
    # None is NOT an integer
    # None is NOT a boolean
    # None is None


    # Exceptions seen
    # AssertionError

  it looks like :ref:`None is None<what is None?>` and not anything else.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_is_none_a_tuple'


:ref:`None is NOT a tuple<test_is_none_a_tuple>`.

----

*********************************************************************************
test_is_none_a_list
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a new test to see if :ref:`None<what is None?>` is a :ref:`list<lists>` (anything in square brackets (``[ ]``))

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 8-9

        def test_is_none_a_tuple(self):
            self.assertIsNotNone(())
            self.assertIsNotNone((0, 1, 2, 'n'))
            self.assertIsInstance((), tuple)
            self.assertIsInstance((0, 1, 2, 'n'), tuple)
            self.assertNotIsInstance(None, tuple)

        def test_is_none_a_list(self):
            self.assertIsNone([])


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: [] is not None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the :ref:`assertion<what is an assertion?>` to make the statement :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 49
  :emphasize-lines: 2-3
  :emphasize-text: Not

      def test_is_none_a_list(self):
          # self.assertIsNone([])
          self.assertIsNotNone([])


  # NOTES

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another failing line

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 4

        def test_is_none_a_list(self):
            # self.assertIsNone([])
            self.assertIsNotNone([])
            self.assertIsNone([0, 1, 2, 'n'])

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: [0, 1, 2, 'n'] is not None

* I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 4-5
    :emphasize-text: Not

        def test_is_none_a_list(self):
            # self.assertIsNone([])
            self.assertIsNotNone([])
            # self.assertIsNone([0, 1, 2, 'n'])
            self.assertIsNotNone([0, 1, 2, 'n'])


    # NOTES

  the test passes.

* I add a failing :ref:`instance test<how to test if something is an instance of a class>`

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 6

        def test_is_none_a_list(self):
            # self.assertIsNone([])
            self.assertIsNotNone([])
            # self.assertIsNone([0, 1, 2, 'n'])
            self.assertIsNotNone([0, 1, 2, 'n'])
            self.assertNotIsInstance([], list)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: [] is an instance of <class 'list'>

  because in Python_ anything in square brackets (``[ ]``) is a :ref:`list<what is a list?>`.

* I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 6-7

        def test_is_none_a_list(self):
            # self.assertIsNone([])
            self.assertIsNotNone([])
            # self.assertIsNone([0, 1, 2, 'n'])
            self.assertIsNotNone([0, 1, 2, 'n'])
            # self.assertNotIsInstance([], list)
            self.assertIsInstance([], list)


    # NOTES

  the test passes.

* I add another failing line with :ref:`assertNotIsInstance<another way to test if something is NOT an instance of a class>`

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 8

        def test_is_none_a_list(self):
            # self.assertIsNone([])
            self.assertIsNotNone([])
            # self.assertIsNone([0, 1, 2, 'n'])
            self.assertIsNotNone([0, 1, 2, 'n'])
            # self.assertNotIsInstance([], list)
            self.assertIsInstance([], list)
            self.assertNotIsInstance([0, 1, 2, 'n'], list)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: [0, 1, 2, 'n'] is an instance of <class 'list'>

  because in Python_ anything in square brackets (``[ ]``) is a :ref:`list<what is a list?>`.

* I change the `assert method`_

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 8-9

        def test_is_none_a_list(self):
            # self.assertIsNone([])
            self.assertIsNotNone([])
            # self.assertIsNone([0, 1, 2, 'n'])
            self.assertIsNotNone([0, 1, 2, 'n'])
            # self.assertNotIsInstance([], list)
            self.assertIsInstance([], list)
            # self.assertNotIsInstance([0, 1, 2, 'n'], list)
            self.assertIsInstance([0, 1, 2, 'n'], list)


    # NOTES

  the test passes.

* I add one more failing line with the :ref:`assertIsInstance method<another way to test if something is an instance of a class>`

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 10

        def test_is_none_a_list(self):
            # self.assertIsNone([])
            self.assertIsNotNone([])
            # self.assertIsNone([0, 1, 2, 'n'])
            self.assertIsNotNone([0, 1, 2, 'n'])
            # self.assertNotIsInstance([], list)
            self.assertIsInstance([], list)
            # self.assertNotIsInstance([0, 1, 2, 'n'], list)
            self.assertIsInstance([0, 1, 2, 'n'], list)
            self.assertIsInstance(None, list)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'list'>

  because :ref:`None<what is None?>` is not a :ref:`list<what is a list?>`.

* I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 10-11

        def test_is_none_a_list(self):
            # self.assertIsNone([])
            self.assertIsNotNone([])
            # self.assertIsNone([0, 1, 2, 'n'])
            self.assertIsNotNone([0, 1, 2, 'n'])
            # self.assertNotIsInstance([], list)
            self.assertIsInstance([], list)
            # self.assertNotIsInstance([0, 1, 2, 'n'], list)
            self.assertIsInstance([0, 1, 2, 'n'], list)
            # self.assertIsInstance(None, list)
            self.assertNotIsInstance(None, list)


    # NOTES

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 49

        def test_is_none_a_list(self):
            self.assertIsNotNone([])
            self.assertIsNotNone([0, 1, 2, 'n'])
            self.assertIsInstance([], list)
            self.assertIsInstance([0, 1, 2, 'n'], list)
            self.assertNotIsInstance(None, list)


    # NOTES

* I add a new comment

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 2

    # NOTES
    # None is NOT a list
    # None is NOT a tuple
    # None is NOT a string
    # None is NOT a float
    # None is NOT an integer
    # None is NOT a boolean
    # None is None


    # Exceptions seen
    # AssertionError

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_is_none_a_list'

:ref:`None is NOT a list<test_is_none_a_list>`.

----

*********************************************************************************
test_is_none_a_set
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I want to test if :ref:`None<what is None?>` is a set_ (anything in curly braces ``{ }``, not :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`)

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 8-9

        def test_is_none_a_list(self):
            self.assertIsNotNone([])
            self.assertIsNotNone([0, 1, 2, 'n'])
            self.assertIsInstance([], list)
            self.assertIsInstance([0, 1, 2, 'n'], list)
            self.assertNotIsInstance(None, list)

        def test_is_none_a_set(self):
            self.assertIsNone(set())


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: set() is not None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I make the statement :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 56
  :emphasize-lines: 2-3
  :emphasize-text: Not

      def test_is_none_a_set(self):
          # self.assertIsNone(set())
          self.assertIsNotNone(set())


  # NOTES

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 4

        def test_is_none_a_set(self):
            # self.assertIsNone(set())
            self.assertIsNotNone(set())
            self.assertIsNone({0, 1, 2, 'n'})


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {0, 1, 2, 'n'} is not None

* I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 4-5
    :emphasize-text: Not

        def test_is_none_a_set(self):
            # self.assertIsNone(set())
            self.assertIsNotNone(set())
            # self.assertIsNone({0, 1, 2, 'n'})
            self.assertIsNotNone({0, 1, 2, 'n'})


    # NOTES

  the test passes.

* I add an :ref:`instance test<how to test if something is an instance of a class>`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 6

        def test_is_none_a_set(self):
            # self.assertIsNone(set())
            self.assertIsNotNone(set())
            # self.assertIsNone({0, 1, 2, 'n'})
            self.assertIsNotNone({0, 1, 2, 'n'})
            self.assertNotIsInstance({0, 1, 2, 'n'}, set)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: {0, 1, 2, 'n'} is an instance of <class 'set'>

* I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 6-7

        def test_is_none_a_set(self):
            # self.assertIsNone(set())
            self.assertIsNotNone(set())
            # self.assertIsNone({0, 1, 2, 'n'})
            self.assertIsNotNone({0, 1, 2, 'n'})
            # self.assertNotIsInstance({0, 1, 2, 'n'}, set)
            self.assertIsInstance({0, 1, 2, 'n'}, set)


    # NOTES

  the test passes.

* I add another :ref:`instance test<how to test if something is an instance of a class>`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 8

        def test_is_none_a_set(self):
            # self.assertIsNone(set())
            self.assertIsNotNone(set())
            # self.assertIsNone({0, 1, 2, 'n'})
            self.assertIsNotNone({0, 1, 2, 'n'})
            # self.assertNotIsInstance({0, 1, 2, 'n'}, set)
            self.assertIsInstance({0, 1, 2, 'n'}, set)
            self.assertIsInstance(None, set)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'set'>

* I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 8-9

        def test_is_none_a_set(self):
            # self.assertIsNone(set())
            self.assertIsNotNone(set())
            # self.assertIsNone({0, 1, 2, 'n'})
            self.assertIsNotNone({0, 1, 2, 'n'})
            # self.assertNotIsInstance({0, 1, 2, 'n'}, set)
            self.assertIsInstance({0, 1, 2, 'n'}, set)
            # self.assertIsInstance(None, set)
            self.assertNotIsInstance(None, set)


    # NOTES

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 55

        def test_is_none_a_set(self):
            self.assertIsNotNone(set())
            self.assertIsNotNone({0, 1, 2, 'n'})
            self.assertIsInstance({0, 1, 2, 'n'}, set)
            self.assertNotIsInstance(None, set)


    # NOTES

* I add a comment

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 2

    # NOTES
    # None is NOT a set
    # None is NOT a list
    # None is NOT a tuple
    # None is NOT a string
    # None is NOT a float
    # None is NOT an integer
    # None is NOT a boolean
    # None is None

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_is_none_a_set'


:ref:`None is NOT a set<test_is_none_a_set>`

----

*********************************************************************************
test_is_none_a_dictionary
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* One last test, this one for if :ref:`None<what is None?>` is a :ref:`dictionary (key-value pairs in curly braces '{ }' separated by commas)<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 7-8

        def test_is_none_a_set(self):
            self.assertIsNotNone(set())
            self.assertIsNotNone({0, 1, 2, 'n'})
            self.assertIsInstance({0, 1, 2, 'n'}, set)
            self.assertNotIsInstance(None, set)

        def test_is_none_a_dictionary(self):
            self.assertIsNone(dict())


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {} is not None

  wait a minute! Python_ uses ``{}`` for sets_. It also uses them for :ref:`dictionaries<what is a dictionary?>` with a difference.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I make the statement :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 62
  :emphasize-lines: 2-3
  :emphasize-text: Not

      def test_is_none_a_dictionary(self):
          # self.assertIsNone(dict())
          self.assertIsNotNone(dict())


  # NOTES

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another failing line

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 4

        def test_is_none_a_dictionary(self):
            # self.assertIsNone(dict())
            self.assertIsNotNone(dict())
            self.assertIsNone({'key': 'value'})


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {'key': 'value'} is not None

* I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 4-5
    :emphasize-text: Not

        def test_is_none_a_dictionary(self):
            # self.assertIsNone(dict())
            self.assertIsNotNone(dict())
            # self.assertIsNone({'key': 'value'})
            self.assertIsNotNone({'key': 'value'})


    # NOTES

  the test passes.

* I add a failing :ref:`instance test<how to test if something is an instance of a class>`

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 6

        def test_is_none_a_dictionary(self):
            # self.assertIsNone(dict())
            self.assertIsNotNone(dict())
            # self.assertIsNone({'key': 'value'})
            self.assertIsNotNone({'key': 'value'})
            self.assertNotIsInstance({}, dict)


    # NOTES

  - :ref:`dict<dictionaries>` is the :ref:`class<what is a class?>` for :ref:`dictionaries<what is a dictionary?>`
  - the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

    .. code-block:: shell

      AssertionError: {} is an instance of <class 'dict'>

    ``{}`` is the empty :ref:`dictionary<what is a dictionary?>`

* I change the `assert method`_

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 6-7

        def test_is_none_a_dictionary(self):
            # self.assertIsNone(dict())
            self.assertIsNotNone(dict())
            # self.assertIsNone({'key': 'value'})
            self.assertIsNotNone({'key': 'value'})
            # self.assertNotIsInstance({}, dict)
            self.assertIsInstance({}, dict)


    # NOTES

  the test passes.

* I add another :ref:`instance test<how to test if something is an instance of a class>`

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 8-10

        def test_is_none_a_dictionary(self):
            # self.assertIsNone(dict())
            self.assertIsNotNone(dict())
            # self.assertIsNone({'key': 'value'})
            self.assertIsNotNone({'key': 'value'})
            # self.assertNotIsInstance({}, dict)
            self.assertIsInstance({}, dict)
            self.assertNotIsInstance(
                {'key': 'value'}, dict
            )


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        {'key': 'value'} is an instance of <class 'dict'>

* I make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 8-9

        def test_is_none_a_dictionary(self):
            # self.assertIsNone(dict())
            self.assertIsNotNone(dict())
            # self.assertIsNone({'key': 'value'})
            self.assertIsNotNone({'key': 'value'})
            # self.assertNotIsInstance({}, dict)
            self.assertIsInstance({}, dict)
            # self.assertNotIsInstance(
            self.assertIsInstance(
                {'key': 'value'}, dict
            )


    # NOTES

  the test passes.

* I add the last failing :ref:`instance test<how to test if something is an instance of a class>` with :ref:`assertIsInstance<another way to test if something is an instance of a class>`

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 12

        def test_is_none_a_dictionary(self):
            # self.assertIsNone(dict())
            self.assertIsNotNone(dict())
            # self.assertIsNone({'key': 'value'})
            self.assertIsNotNone({'key': 'value'})
            # self.assertNotIsInstance({}, dict)
            self.assertIsInstance({}, dict)
            # self.assertNotIsInstance(
            self.assertIsInstance(
                {'key': 'value'}, dict
            )
            self.assertIsInstance(None, dict)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None is not an instance of <class 'dict'>

  because :ref:`None<what is None?>` is not a :ref:`dictionary<what is a dictionary?>`.

* I make the statement :ref:`True<test_what_is_true>` with :ref:`assertNotIsInstance<another way to test if something is NOT an instance of a class>`

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 12-13

        def test_is_none_a_dictionary(self):
            # self.assertIsNone(dict())
            self.assertIsNotNone(dict())
            # self.assertIsNone({'key': 'value'})
            self.assertIsNotNone({'key': 'value'})
            # self.assertNotIsInstance({}, dict)
            self.assertIsInstance({}, dict)
            # self.assertNotIsInstance(
            self.assertIsInstance(
                {'key': 'value'}, dict
            )
            # self.assertIsInstance(None, dict)
            self.assertNotIsInstance(None, dict)


    # NOTES

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 62

        def test_is_none_a_dictionary(self):
            self.assertIsNotNone(dict())
            self.assertIsNotNone({'key': 'value'})
            self.assertIsInstance({}, dict)
            self.assertIsInstance(
                {'key': 'value'}, dict
            )
            self.assertNotIsInstance(None, dict)


    # NOTES

* I add the last comment

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 2

    # NOTES
    # None is NOT a dictionary
    # None is NOT a set
    # None is NOT a list
    # None is NOT a tuple
    # None is NOT a string
    # None is NOT a float
    # None is NOT an integer
    # None is NOT a boolean
    # None is None


    # Exceptions seen
    # AssertionError

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_is_none_a_dictionary'

:ref:`None is NOT a dictionary<test_is_none_a_dictionary>`.

----

*********************************************************************************
sets vs dictionaries
*********************************************************************************

``{'key': 'value'}`` is a :ref:`dictionary<what is a dictionary?>` with ``:`` separating the :ref:`key<test_keys_of_a_dictionary>` on the left from the :ref:`value<test_values_of_a_dictionary>` on the right.

I can add more :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` separating them with commas, for example

.. code-block:: python

  {
      'key': 'value',
      'another_key': 'another value',
      'one_more_key': 'one more value',
      'magic_key': 'magic value',
      'keyN': [0, 1, 2, 'n'],
  }

sets_ do NOT have key-value pairs.

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_none.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``none``

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

I used `assert methods`_ to test what :ref:`None<what is None?>` is and what it is NOT.

* Two from :ref:`the inheritance chapter<everything is an object>`:

  * :ref:`assertIsInstance<another way to test if something is an instance of a class>` which checks if something is :ref:`an instance of a given class<how to test if something is an instance of a class>`
  * :ref:`assertNotIsInstance<another way to test if something is NOT an instance of a class>` which checks if something is :ref:`NOT an instance of a given class<how to test if something is NOT an instance of a class>`

  to show that :ref:`None<what is None?>` is not an :ref:`instance<how to test if something is an instance of a class>` of the other :ref:`basic types<data structures>`.

* And two new `assert methods`_ for :ref:`None<what is None?>`:

  * :ref:`assertIsNone<one more way to test if something is None>` which raises :ref:`AssertionError<what causes AssertionError?>` if the thing in parentheses is NOT :ref:`None<what is None?>`. It replaced :ref:`assertIs<another way to test if something is the same object as None>` from :ref:`the assertion_error project<what is an assertion?>` except in :ref:`test_what_is_none`
  * :ref:`assertIsNotNone<one more way to test if something is NOT None>` which raises :ref:`AssertionError<what causes AssertionError?>` if the thing in parentheses is :ref:`None<what is None?>`. It replaced :ref:`assertIsNot<another way to test if something is NOT the same object as None>` from :ref:`the assertion_error project<what is an assertion?>`

I also used :ref:`Python's basic data structures<data structures>` in the tests

* :ref:`None<what is None?>` - the simplest
* integers_ - whole numbers, negative and positive, including ``0``
* floats_ - binary floating point decimal numbers, negative and positive including ``0.0``
* strings_ - anything inside :ref:`quotes`
* :ref:`booleans - True and False<what are booleans?>`
* tuples_ - anything in parentheses (``( )``) separated by commas
* :ref:`lists - anything in square brackets ([ ])<what is a list?>`
* sets_ - anything in curly braces (``{ }``) separated by commas and NOT :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`
* :ref:`dictionaries - key-value pairs in curly braces ({ })<what is a dictionary?>`

:ref:`How many questions can you answer after going through this chapter?<questions about None>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<None (the simplest object): tests>`

----

*************************************************************************************
what is next?
*************************************************************************************

so far you have seen

* :ref:`how to make a Python test driven development environment manually`
* :ref:`what causes AssertionError<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to pass values from tests to functions<telephone>`
* :ref:`how to make dictionaries with functions<how to make a person>`
* :ref:`how to make classes<classes>`
* :ref:`how to use class attributes to remove repetition<AssertionError 2: use class attributes>`
* :ref:`what happens when classes have one or more parents<family ties>`
* :ref:`what causes AttributeError<what causes AttributeError?>`
* :ref:`what None is and is not<what is None?>`

:ref:`Would you like to use the assertIsNotNone and assertIsNone methods with the assertion_error project?<AssertionError 3: use assertIsNotNone and assertIsNone>`

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