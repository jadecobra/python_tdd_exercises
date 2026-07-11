.. meta::
  :description: Master Python's truthiness and falsiness rules through Test Driven Development (TDD) in the "booleans" project. Step-by-step red-green-refactor with unittest.TestCase.assertTrue, assertFalse, bool(), assertIsInstance, assertIs and assertEqual. Tests the False and True singletons themselves (showing they are bool instances, identical only to themselves, and not equal to None or 0), then exhaustively groups the prior data structures: None (falsy), negative/zero/positive integers, negative/0.0/positive floats, empty vs populated strings/tuples/lists/sets/dicts. Demonstrates repeated real AssertionError messages from the terminal ("AssertionError: False is not true", "AssertionError: True is not false", "AssertionError: 0 is not true", "AssertionError: 1 is not false", "AssertionError: {} is not true", "AssertionError: False is not true" and equivalents for other empties). Uses local variables inside test methods (no setUp), "I remove the commented lines" after each GREEN, accumulating # NOTES list of every bool() fact at the bottom, "the terminal is my friend", uv init booleans, tests/ package with __init__.py, pytest-watcher, per-test git commits. Builds directly on AssertionError (assertIs for True/False identity) and None chapters. "I have these tests by the end of the chapter" preview via literalinclude. Part of Jacob Itegboje's Pumping Python TDD series for beginners.
  :keywords: Jacob Itegboje, Pumping Python, Python booleans for beginners, Python truthiness and falsiness, unittest assertTrue, unittest assertFalse, assertTrue assertFalse, TDD Red Green Refactor, bool built-in function, is empty list True or False, is 0.0 False, is None False or True, 0 is not False, empty string is not False, empty list is not False, empty dict is not False, AssertionError: False is not true, AssertionError: True is not false, AssertionError: 0 is not true, AssertionError: 1 is not false, AssertionError: {} is not true, bool(0) is False, bool(None) is False, bool('') is False, bool([]) is False, bool({}) is False, truthy non-zero non-empty, falsy values 0 0.0 None empty container, testing Python basic objects, python uv init booleans, pytest-watcher, remove the commented lines, the terminal is my friend, I have these tests by the end of the chapter, test_what_is_false, test_is_an_integer_falsy_or_truthy, test_is_a_dictionary_falsy_or_truthy, python unit testing tutorial, python bool type, boolean logic TDD, data structures booleans chapter

.. include:: ../../links.rst
.. _bool: https://docs.python.org/3/library/functions.html#bool
.. _bool class: bool_
.. _bool built-in function: bool_
.. _booleans: bool_
.. _assertFalse: https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertFalse
.. _assertFalse method: assertFalse_
.. _assertTrue: https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertTrue
.. _assertTrue method: assertTrue_
.. _unittest.TestCase.assertFalse: assertFalse_
.. _unittest.TestCase.assertTrue: assertTrue_

#################################################################################
booleans: only two
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/6r3QcYN0wxQ?si=cQaK63rwX3f9PGX6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

I want to test what groups the :ref:`objects<everything is an object>` seen so far - :ref:`None<what is None?>`, integers_, floats_, strings_, tuples_, :ref:`lists`, sets_ and :ref:`dictionaries<what is a dictionary?>`, fall into Python_ divides them into two groups - :ref:`False<test_what_is_false>` and :ref:`True<test_what_is_true>`. What do you think will happen?

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/booleans/test_booleans.py
  :language: python
  :linenos:

*********************************************************************************
questions about Booleans
*********************************************************************************

Questions to think about as we divide :ref:`Python's basic data structures<basic objects>` into  :ref:`False<test_what_is_false>` and :ref:`True<test_what_is_true>`

* :ref:`what is False?<test_what_is_false>`
* :ref:`what is True?<test_what_is_true>`
* :ref:`Is None grouped as False or True?<test_is_none_falsy_or_truthy>`
* :ref:`Is an integer grouped as False or True?<test_is_an_integer_falsy_or_truthy>`
* :ref:`Is a float grouped as False or True?<test_is_a_float_falsy_or_truthy>`
* :ref:`Is a string grouped as False or True?<test_is_a_string_falsy_or_truthy>`
* :ref:`Is a tuple grouped as False or True?<test_is_a_tuple_falsy_or_truthy>`
* :ref:`Is a list grouped as False or True?<test_is_a_list_falsy_or_truthy>`
* :ref:`Is a set grouped as False or True?<test_is_a_set_falsy_or_truthy>`
* :ref:`Is a dictionary grouped as False or True?<test_is_a_dictionary_falsy_or_truthy>`

----

*********************************************************************************
start the project
*********************************************************************************

* I name this project ``booleans``
* I open a terminal_
* I use uv_ to make a directory_ for the project and initialize it

  .. code-block:: python
    :emphasize-lines: 1

    uv init booleans

  the terminal_ shows

  .. code-block:: shell

    Initialized project `booleans`
    at `.../pumping_python/booleans`

  then goes back to the command line.

* I change directory_ to the project

  .. code-block:: shell
    :emphasize-lines: 1

    cd booleans

  the terminal_ shows I am in the ``booleans`` folder_

  .. code-block:: shell

    .../pumping_python/booleans

* I `make a directory`_ for the tests

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir tests

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

* I use the `mv program`_ to change the name of ``main.py`` to ``test_booleans.py`` and move it to the ``tests`` folder_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 1

        mv main.py tests/test_booleans.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        Move-Item main.py tests/test_booleans.py

  the terminal_ goes back to the command line.

* I open ``test_booleans.py``

* I add :ref:`the first failing test<test_failure>` to ``test_booleans.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-7

    import unittest


    class TestBooleans(unittest.TestCase):

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

    git commit -all --message 'setup project'

  the terminal_ shows a summary of the changes then goes back to the command line.

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 8, 10


    ======================== FAILURES ========================
    _______________ TestBooleans.test_failure ________________

    self = <tests.test_booleans.TestBooleans testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_booleans.py:7: AssertionError
    ================ short test summary info =================
    FAILED tests/test_booleans.py::TestBooleans::test_failure - AssertionError: True is not false
    =================== 1 failed in X.YZs ====================

  .. admonition:: if the terminal_ does not show the same error, then check

    * if your ``tests/__init__.py`` has two underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``
    * if you ran ``echo "pytest-watcher" >> requirements.txt``, to add ``pytest-watcher`` to the requirements file_

    and try ``uv run pytest-watcher . --now`` again

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_booleans.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7-8
    :emphasize-text: AssertionError

    class TestBooleans(unittest.TestCase):

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
test_what_is_false
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change :ref:`test_failure` to :ref:`test_what_is_false`, then use the :ref:`assertNotIsInstance method<test_assert_not_is_instance>` I learned from :ref:`everything is an object` to check if :ref:`False<test_what_is_false>` is :ref:`an instance (a copy)<how to test if something is an instance>` of the :ref:`bool class<what are booleans?>`

.. code-block:: python
  :linenos:
  :emphasize-lines: 6-7

  import unittest


  class TestBooleans(unittest.TestCase):

      def test_what_is_false(self):
          self.assertNotIsInstance(False, bool)


  # Exceptions seen
  # AssertionError

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: False is an instance of <class 'bool'>

this was also in :ref:`test_is_none_a_boolean`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`assertNotIsInstance<test_assert_not_is_instance>` to the :ref:`assertIsInstance method<test_assert_is_instance>`

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 2-3

      def test_what_is_false(self):
          # self.assertNotIsInstance(False, bool)
          self.assertIsInstance(False, bool)


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a comment

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 6-7

        def test_what_is_false(self):
            # self.assertNotIsInstance(False, bool)
            self.assertIsInstance(False, bool)


    # NOTES
    # False is a boolean


    # Exceptions seen
    # AssertionError

  I know this from :ref:`testing None<what is None?>`.

* I use the :ref:`assertIsNot method<another way to test if something is NOT the same object as False>` like I did in :ref:`test_assertion_error_w_false`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 4

        def test_what_is_false(self):
            # self.assertNotIsInstance(False, bool)
            self.assertIsInstance(False, bool)
            self.assertIsNot(False, False)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: unexpectedly identical: False

  because :ref:`False is False<test_what_is_false>`.

* I change :ref:`assertIsNot<another way to test if something is NOT the same object as False>` to :ref:`assertIs<another way to test if something is the same object as False>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 4-5

        def test_what_is_false(self):
            # self.assertNotIsInstance(False, bool)
            self.assertIsInstance(False, bool)
            # self.assertIsNot(False, False)
            self.assertIs(False, False)


    # NOTES

  the test passes. I know this from :ref:`test_assertion_error_w_false`.

----

*********************************************************************************
how to test if something is grouped as False
*********************************************************************************

----

I can test if Python_ groups an :ref:`object<everything is an object>` as :ref:`False<test_what_is_false>` with the `bool built-in function`_ from `The Python Standard Library`_.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` with a call to bool_

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 6

        def test_what_is_false(self):
            # self.assertNotIsInstance(False, bool)
            self.assertIsInstance(False, bool)
            # self.assertIsNot(False, False)
            self.assertIs(False, False)
            self.assertEqual(bool(False), True)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False != True

  because this happens when ``self.assertEqual(bool(False), True)`` runs

  .. code-block:: python

    self.assertEqual(bool(False), True)
    self.assertEqual(False      , True)

  - which raises :ref:`AssertionError<what causes AssertionError?>` since :ref:`False<test_what_is_false>`, which is the result of ``bool(False)`` is not equal to :ref:`True<test_what_is_true>`
  - ``bool(anything)`` returns :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>` for the thing in parentheses

* I add a comment

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 2

    # NOTES
    # False is NOT equal to True
    # False is a boolean


    # Exceptions seen
    # AssertionError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the expectation of the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 6-7

      def test_what_is_false(self):
          # self.assertNotIsInstance(False, bool)
          self.assertIsInstance(False, bool)
          # self.assertIsNot(False, False)
          self.assertIs(False, False)
          # self.assertEqual(bool(False), True)
          self.assertEqual(bool(False), False)


  # NOTES

the test passes because ``bool(False)`` is equal to :ref:`False<test_what_is_false>`.

----

*********************************************************************************
another way to test if something is grouped as False
*********************************************************************************

----

The :ref:`unittest.TestCase class<test_dir_unittest_testcase>` has a :ref:`method<what is a method?>` I can use to test if the result of calling the `bool built-in function`_ with an :ref:`object<everything is an object>` is :ref:`False<test_what_is_false>` - assertFalse_, it was in :ref:`the first failing test<test_failure>`

.. code-block:: python

  self.assertFalse(True)

which is like

.. code-block:: python

  self.assertEqual(bool(True), False)

it raises :ref:`AssertionError<what causes AssertionError?>` if the :ref:`object<everything is an object>` in parentheses is grouped as :ref:`True<test_what_is_true>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add assertFalse_ to the test

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 8

        def test_what_is_false(self):
            # self.assertNotIsInstance(False, bool)
            self.assertIsInstance(False, bool)
            # self.assertIsNot(False, False)
            self.assertIs(False, False)
            # self.assertEqual(bool(False), True)
            self.assertEqual(bool(False), False)
            self.assertFalse(bool(True))


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  because this happens when ``self.assertEqual(bool(False), True)`` runs

  .. code-block:: python

    self.assertFalse(bool(True))
    self.assertFalse(True)

  which raises :ref:`AssertionError<what causes AssertionError?>` since the result of ``bool(True)`` is :ref:`True<test_what_is_true>`.

* I add a comment

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 2

    # NOTES
    # True is NOT False
    # False is NOT equal to True
    # False is a boolean

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in parentheses

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 8-9

      def test_what_is_false(self):
          # self.assertNotIsInstance(False, bool)
          self.assertIsInstance(False, bool)
          # self.assertIsNot(False, False)
          self.assertIs(False, False)
          # self.assertEqual(bool(False), True)
          self.assertEqual(bool(False), False)
          # self.assertFalse(bool(True))
          self.assertFalse(bool(False))


  # NOTES

the test passes because ``bool(False)`` is equal to :ref:`False<test_what_is_false>`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* It turns out that I can skip bool_ and get the same result. I add a :ref:`call<how to call a function with input>` to the `assertFalse method`_

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 10

        def test_what_is_false(self):
            # self.assertNotIsInstance(False, bool)
            self.assertIsInstance(False, bool)
            # self.assertIsNot(False, False)
            self.assertIs(False, False)
            # self.assertEqual(bool(False), True)
            self.assertEqual(bool(False), False)
            # self.assertFalse(bool(True))
            self.assertFalse(bool(False))
            self.assertFalse(True)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  because ``bool(True)`` is :ref:`True<test_what_is_true>`.

* I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the parentheses

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 10-11

        def test_what_is_false(self):
            # self.assertNotIsInstance(False, bool)
            self.assertIsInstance(False, bool)
            # self.assertIsNot(False, False)
            self.assertIs(False, False)
            # self.assertEqual(bool(False), True)
            self.assertEqual(bool(False), False)
            # self.assertFalse(bool(True))
            self.assertFalse(bool(False))
            # self.assertFalse(True)
            self.assertFalse(False)


    # NOTES

  the test passes because ``bool(False)`` is equal to :ref:`False<test_what_is_false>`.

  The `assertFalse method`_ raises :ref:`AssertionError<what causes AssertionError?>` if the result of a call to the `bool built-in function`_ with an :ref:`object<everything is an object>` is :ref:`True<test_what_is_true>`.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 6

    class TestBooleans(unittest.TestCase):

            def test_what_is_false(self):
                self.assertIsInstance(False, bool)
                self.assertIs(False, False)
                self.assertEqual(bool(False), False)
                self.assertFalse(bool(False))
                self.assertFalse(False)


        # NOTES

* I open a new terminal_, then add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit --all --message 'add test_what_is_false'

:ref:`False is a boolean<test_what_is_false>`.

----

*********************************************************************************
test_what_is_true
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test for :ref:`True<test_what_is_true>` with the :ref:`assertNotIsInstance method<test_assert_not_is_instance>` I learned from :ref:`everything is an object` to check if :ref:`True<test_what_is_true>` is :ref:`an instance (a copy)<how to test if something is an instance>` of the :ref:`bool class<what are booleans?>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 8-9

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertIs(False, False)
            self.assertEqual(bool(False), False)
            self.assertFalse(bool(False))
            self.assertFalse(False)

        def test_what_is_true(self):
            self.assertNotIsInstance(True, bool)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is an instance of <class 'bool'>

  this was also in :ref:`test_is_none_a_boolean`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`assertNotIsInstance<test_assert_not_is_instance>` to the :ref:`assertIsInstance method<test_assert_is_instance>`

.. code-block:: python
  :lineno-start: 13
  :emphasize-lines: 2-3

        def test_what_is_true(self):
            # self.assertNotIsInstance(True, bool)
            self.assertIsInstance(True, bool)


    # NOTES

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a comment

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 3

    # NOTES
    # True is NOT False
    # True is a boolean
    # False is NOT equal to True
    # False is a boolean

  I know this also from :ref:`testing None<what is None?>`.

* I use the :ref:`assertIsNot method<another way to test if something is NOT the same object as True>` like I did in :ref:`test_assertion_error_w_true`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 4

        def test_what_is_true(self):
            # self.assertNotIsInstance(True, bool)
            self.assertIsInstance(True, bool)
            self.assertIsNot(True, True)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: unexpectedly identical: True

  because :ref:`True is True<test_what_is_true>`.

* I change :ref:`assertIsNot<another way to test if something is NOT the same object as True>` to :ref:`assertIs<another way to test if something is the same object as True>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 4-5

        def test_what_is_true(self):
            # self.assertNotIsInstance(True, bool)
            self.assertIsInstance(True, bool)
            # self.assertIsNot(True, True)
            self.assertIs(True, True)


    # NOTES

  the test passes. This was also in :ref:`test_assertion_error_w_true`.

----

*********************************************************************************
how to test if something is grouped as True
*********************************************************************************

----

I will use the `bool built-in function`_ from `The Python Standard Library`_ to test if Python_ groups an :ref:`object<everything is an object>` as :ref:`True<test_what_is_true>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` with a call to bool_

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 6

        def test_what_is_true(self):
            # self.assertNotIsInstance(True, bool)
            self.assertIsInstance(True, bool)
            # self.assertIsNot(True, True)
            self.assertIs(True, True)
            self.assertEqual(bool(True), False)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True != False

  because this happens when ``self.assertEqual(bool(True), False)`` runs

  .. code-block:: python

    self.assertEqual(bool(True), False)
    self.assertEqual(True      , False)

  - which raises :ref:`AssertionError<what causes AssertionError?>` since :ref:`True<test_what_is_true>`, which is the result of ``bool(True)`` is not equal to :ref:`False<test_what_is_false>`
  - ``bool(anything)`` returns :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>` for the thing in parentheses

* I add a comment

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 3

    # NOTES
    # True is NOT False
    # True is NOT equal to False
    # True is a boolean
    # False is NOT equal to True
    # False is a boolean


    # Exceptions seen
    # AssertionError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the expectation of the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 13
  :emphasize-lines: 6-7

      def test_what_is_true(self):
          # self.assertNotIsInstance(True, bool)
          self.assertIsInstance(True, bool)
          # self.assertIsNot(True, True)
          self.assertIs(True, True)
          # self.assertEqual(bool(True), False)
          self.assertEqual(bool(True), True)


  # NOTES

the test passes because ``bool(True)`` is equal to :ref:`True<test_what_is_true>`.

----

*********************************************************************************
another way to test if something is grouped as True
*********************************************************************************

----

The :ref:`unittest.TestCase class<test_dir_unittest_testcase>` has a :ref:`method<what is a method?>` I can use to test if the result of calling the `bool built-in function`_ with an :ref:`object<everything is an object>` is :ref:`True<test_what_is_true>` - assertTrue_. It raises :ref:`AssertionError<what causes AssertionError?>` if the :ref:`object<everything is an object>` in parentheses is grouped as :ref:`False<test_what_is_false>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add assertTrue_ to the test

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 8

        def test_what_is_true(self):
            # self.assertNotIsInstance(True, bool)
            self.assertIsInstance(True, bool)
            # self.assertIsNot(True, True)
            self.assertIs(True, True)
            # self.assertEqual(bool(True), False)
            self.assertEqual(bool(True), True)
            self.assertTrue(bool(False))


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  because this happens when ``self.assertEqual(bool(True), False)`` runs

  .. code-block:: python

    self.assertTrue(bool(False))
    self.assertTrue(False)

  which raises :ref:`AssertionError<what causes AssertionError?>` since the result of ``bool(False)`` is :ref:`False<test_what_is_false>`.

* I add a comment

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 5

    # NOTES
    # True is NOT False
    # True is NOT equal to False
    # True is a boolean
    # False is NOT True
    # False is NOT equal to True
    # False is a boolean

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`False<test_what_is_false>` to :ref:`True<test_what_is_true>` in parentheses

.. code-block:: python
  :lineno-start: 13
  :emphasize-lines: 8-9

      def test_what_is_true(self):
          # self.assertNotIsInstance(True, bool)
          self.assertIsInstance(True, bool)
          # self.assertIsNot(True, True)
          self.assertIs(True, True)
          # self.assertEqual(bool(True), False)
          self.assertEqual(bool(True), True)
          # self.assertTrue(bool(False))
          self.assertTrue(bool(True))


  # NOTES

the test passes because ``bool(True)`` is equal to :ref:`True<test_what_is_true>`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I can skip bool_ and get the same result. I add a :ref:`call<how to call a function with input>` to the `assertTrue method`_

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 10

        def test_what_is_true(self):
            # self.assertNotIsInstance(True, bool)
            self.assertIsInstance(True, bool)
            # self.assertIsNot(True, True)
            self.assertIs(True, True)
            # self.assertEqual(bool(True), False)
            self.assertEqual(bool(True), True)
            # self.assertTrue(bool(False))
            self.assertTrue(bool(True))
            self.assertTrue(False)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  because ``bool(False)`` is :ref:`False<test_what_is_false>`.

* I change :ref:`False<test_what_is_false>` to :ref:`True<test_what_is_true>` in the parentheses

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 10-11

        def test_what_is_true(self):
            # self.assertNotIsInstance(True, bool)
            self.assertIsInstance(True, bool)
            # self.assertIsNot(True, True)
            self.assertIs(True, True)
            # self.assertEqual(bool(True), False)
            self.assertEqual(bool(True), True)
            # self.assertTrue(bool(False))
            self.assertTrue(bool(True))
            # self.assertTrue(False)
            self.assertTrue(True)


    # NOTES

  the test passes because ``bool(True)`` is equal to :ref:`True<test_what_is_true>`.

  The `assertTrue method`_ raises :ref:`AssertionError<what causes AssertionError?>` if the result of a call to the `bool built-in function`_ with an :ref:`object<everything is an object>` is :ref:`False<test_what_is_false>`.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 13

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertIs(True, True)
            self.assertEqual(bool(True), True)
            self.assertTrue(bool(True))
            self.assertTrue(True)


    # NOTES

* I open a new terminal_, then add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit --all --message 'add test_what_is_true'

:ref:`True is a boolean<test_what_is_true>`.

----

*****************************************************************************************
test_is_none_falsy_or_truthy
*****************************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test to see if :ref:`None<what is None?>` is grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 8-9

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertIs(True, True)
            self.assertEqual(bool(True), True)
            self.assertTrue(bool(True))
            self.assertTrue(True)

        def test_is_none_falsy_or_truthy(self):
            self.assertTrue(bool(None))


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  because the result of ``bool(None)`` is :ref:`False<test_what_is_false>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change assertTrue_ to assertFalse_

.. code-block:: python
  :lineno-start: 20
  :emphasize-lines: 2-3

      def test_is_none_falsy_or_truthy(self):
          # self.assertTrue(bool(None))
          self.assertFalse(bool(None))


  # NOTES

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a comment

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 5

    # NOTES
    # True is NOT False
    # True is NOT equal to False
    # True is a boolean
    # bool(None) is False
    # False is NOT True
    # False is NOT equal to True
    # False is a boolean

* I add an :ref:`assertion<what is an assertion?>` without bool_

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 4

        def test_is_none_falsy_or_truthy(self):
            # self.assertTrue(bool(None))
            self.assertFalse(bool(None))
            self.assertTrue(None)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None is not true

  I know this from :ref:`test_assertion_error_w_true`.

* I change assertTrue_ to assertFalse_

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 4-5

        def test_is_none_falsy_or_truthy(self):
            # self.assertTrue(bool(None))
            self.assertFalse(bool(None))
            # self.assertTrue(None)
            self.assertFalse(None)


    # NOTES

  - the test passes because the result of ``bool(None)`` is not :ref:`True<test_what_is_true>`
  - :ref:`None is not the same object as False<test_assertion_error_w_false>`.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 20

        def test_is_none_falsy_or_truthy(self):
            self.assertFalse(bool(None))
            self.assertFalse(None)


    # NOTES

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_is_none_falsy_or_truthy'

:ref:`None is grouped as False<test_is_none_falsy_or_truthy>`. :ref:`The AssertionError chapter<what causes AssertionError?>` showed that :ref:`None is not False<test_assertion_error_w_false>` and :ref:`False is not None<test_assertion_error_w_none>`.

----

*********************************************************************************
test_is_an_integer_falsy_or_truthy
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test for if an integer_ (a whole number without decimals) is grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 5-6

        def test_is_none_falsy_or_truthy(self):
            self.assertFalse(bool(None))
            self.assertFalse(None)

        def test_is_an_integer_falsy_or_truthy(self):
            self.assertFalse(bool(-1))


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  - because the result of ``bool(-1)`` is :ref:`True<test_what_is_true>`
  - I use ``-1`` for all the integers_ (whole numbers without decimals) that are smaller than ``0``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change assertFalse_ to assertTrue_

.. code-block:: python
  :lineno-start: 24
  :emphasize-lines: 2-3

      def test_is_an_integer_falsy_or_truthy(self):
          # self.assertFalse(bool(-1))
          self.assertTrue(bool(-1))


  # NOTES

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a comment

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2

    # NOTES
    # bool(-1) is True
    # True is NOT False
    # True is NOT equal to False
    # True is a boolean
    # bool(None) is False
    # False is NOT True
    # False is NOT equal to True
    # False is a boolean

* I add an :ref:`assertion<what is an assertion?>` without bool_

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 4

        def test_is_an_integer_falsy_or_truthy(self):
            # self.assertFalse(bool(-1))
            self.assertTrue(bool(-1))
            self.assertFalse(-1)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: -1 is not false

  because the result of ``bool(-1)`` is :ref:`True<test_what_is_true>`.

* I change assertFalse_ to assertTrue_

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 4-5

        def test_is_an_integer_falsy_or_truthy(self):
            # self.assertFalse(bool(-1))
            self.assertTrue(bool(-1))
            # self.assertFalse(-1)
            self.assertTrue(-1)


    # NOTES

  - the test passes because the result of ``bool(-1)`` is :ref:`True<test_what_is_true>`
  - a negative integer_ is grouped as :ref:`True<test_what_is_true>`
  - :ref:`an integer is not the same object as True<test_assertion_error_w_true>`

* I add a :ref:`variable<what is a variable?>` for ``-1``

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 2

        def test_is_an_integer_falsy_or_truthy(self):
            a_negative_integer = -1
            # self.assertFalse(bool(-1))
            self.assertTrue(bool(-1))
            # self.assertFalse(-1)
            self.assertTrue(-1)


    # NOTES

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``-1``

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 4-5, 7-8

        def test_is_an_integer_falsy_or_truthy(self):
            a_negative_integer = -1
            # self.assertFalse(bool(-1))
            # self.assertTrue(bool(-1))
            self.assertTrue(bool(a_negative_integer))
            # self.assertFalse(-1)
            # self.assertTrue(-1)
            self.assertTrue(a_negative_integer)


    # NOTES

  the test is still green.

* I add an :ref:`assertion<what is an assertion?>` to test if ``0`` is grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 10

        def test_is_an_integer_falsy_or_truthy(self):
            a_negative_integer = -1
            # self.assertFalse(bool(-1))
            # self.assertTrue(bool(-1))
            self.assertTrue(bool(a_negative_integer))
            # self.assertFalse(-1)
            # self.assertTrue(-1)
            self.assertTrue(a_negative_integer)

            self.assertTrue(bool(0))


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  because the result of ``bool(0)`` is :ref:`False<test_what_is_false>`.

* I change assertTrue_ to assertFalse_

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 10-11

        def test_is_an_integer_falsy_or_truthy(self):
            a_negative_integer = -1
            # self.assertFalse(bool(-1))
            # self.assertTrue(bool(-1))
            self.assertTrue(bool(a_negative_integer))
            # self.assertFalse(-1)
            # self.assertTrue(-1)
            self.assertTrue(a_negative_integer)

            # self.assertTrue(bool(0))
            self.assertFalse(bool(0))


    # NOTES

  the test passes.

* I add a comment

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 6

    # NOTES
    # bool(-1) is True
    # True is NOT False
    # True is NOT equal to False
    # True is a boolean
    # bool(0) is False
    # bool(None) is False
    # False is NOT True
    # False is NOT equal to True
    # False is a boolean

* I add an :ref:`assertion<what is an assertion?>` without bool_

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 3

            # self.assertTrue(bool(0))
            self.assertFalse(bool(0))
            self.assertTrue(0)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0 is not true

  because the result of ``bool(0)`` is :ref:`False<test_what_is_false>`.

* I change assertTrue_ to assertFalse_

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 3-4

            # self.assertTrue(bool(0))
            self.assertFalse(bool(0))
            # self.assertTrue(0)
            self.assertFalse(0)


    # NOTES

  - the test passes because the result of ``bool(0)`` is :ref:`False<test_what_is_false>`
  - :ref:`an integer is not the same object as False<test_assertion_error_w_false>`

* I add an :ref:`assertion<what is an assertion?>` to test if ``1`` is grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 6

            # self.assertTrue(bool(0))
            self.assertFalse(bool(0))
            # self.assertTrue(0)
            self.assertFalse(0)

            self.assertFalse(bool(1))


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  - because the result of ``bool(1)`` is :ref:`True<test_what_is_true>`
  - I use ``1`` for all the integers_ (whole numbers without decimals) that are bigger than ``0``

* I change assertFalse_ to assertTrue_

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 6-7

            # self.assertTrue(bool(0))
            self.assertFalse(bool(0))
            # self.assertTrue(0)
            self.assertFalse(0)

            # self.assertFalse(bool(1))
            self.assertTrue(bool(1))


    # NOTES

  the test passes.

* I add a comment

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 2

    # NOTES
    # bool(1) is True
    # bool(-1) is True
    # True is NOT False
    # True is NOT equal to False
    # True is a boolean
    # bool(0) is False
    # bool(None) is False
    # False is NOT True
    # False is NOT equal to True
    # False is a boolean

* I add an :ref:`assertion<what is an assertion?>` without bool_

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 3

            # self.assertFalse(bool(1))
            self.assertTrue(bool(1))
            self.assertFalse(1)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 1 is not false

  because the result of ``bool(1)`` is :ref:`True<test_what_is_true>`.

* I change assertFalse_ to assertTrue_

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 3-4

            # self.assertFalse(bool(1))
            self.assertTrue(bool(1))
            # self.assertFalse(1)
            self.assertTrue(1)


    # NOTES

  - the test passes because the result of ``bool(1)`` is :ref:`True<test_what_is_true>`
  - a positive integer_ is grouped as :ref:`True<test_what_is_true>`
  - :ref:`an integer is not the same object as True<test_assertion_error_w_true>`

* I add a :ref:`variable<what is a variable?>` for ``1``

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 6

            # self.assertTrue(bool(0))
            self.assertFalse(bool(0))
            # self.assertTrue(0)
            self.assertFalse(0)

            a_positive_integer = 1
            # self.assertFalse(bool(1))
            self.assertTrue(bool(1))
            # self.assertFalse(1)
            self.assertTrue(1)

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``1``

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 3-4, 6-7

            a_positive_integer = 1
            # self.assertFalse(bool(1))
            # self.assertTrue(bool(1))
            self.assertTrue(bool(a_positive_integer))
            # self.assertFalse(1)
            # self.assertTrue(1)
            self.assertTrue(a_positive_integer)


    # NOTES

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 24

        def test_is_an_integer_falsy_or_truthy(self):
            a_negative_integer = -1
            self.assertTrue(bool(a_negative_integer))
            self.assertTrue(a_negative_integer)

            self.assertFalse(bool(0))
            self.assertFalse(0)

            a_positive_integer = 1
            self.assertTrue(bool(a_positive_integer))
            self.assertTrue(a_positive_integer)


    # NOTES

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_is_an_integer_falsy_or_truthy'

* :ref:`'0' is grouped as False, positive and negative integers are grouped as True<test_is_an_integer_falsy_or_truthy>`
* :ref:`None is grouped as False<test_is_none_falsy_or_truthy>`

----

*********************************************************************************
test_is_a_float_falsy_or_truthy
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test for if a float_ (binary floating point decimal number) is grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 3
    :emphasize-lines: 5-6

            a_positive_integer = 1
            self.assertTrue(bool(a_positive_integer))
            self.assertTrue(a_positive_integer)

        def test_is_a_float_falsy_or_truthy(self):
            self.assertFalse(bool(-0.1))


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  - because the result of ``bool(-0.1)`` is :ref:`True<test_what_is_true>`
  - I use ``-0.1`` for all the floats_ (binary floating point decimal numbers) that are smaller than ``0.0``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change assertFalse_ to assertTrue_

.. code-block:: python
  :lineno-start: 36
  :emphasize-lines: 2-3

      def test_is_a_float_falsy_or_truthy(self):
          # self.assertFalse(bool(-0.1))
          self.assertTrue(bool(-0.1))


  # NOTES

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a comment

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 2

    # NOTES
    # bool(-0.1) is True
    # bool(1) is True
    # bool(-1) is True
    # True is NOT False
    # True is NOT equal to False
    # True is a boolean
    # bool(0) is False
    # bool(None) is False
    # False is NOT True
    # False is NOT equal to True
    # False is a boolean

* I add an :ref:`assertion<what is an assertion?>` without bool_

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 4

        def test_is_a_float_falsy_or_truthy(self):
            # self.assertFalse(bool(-0.1))
            self.assertTrue(bool(-0.1))
            self.assertFalse(-0.1)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: -0.1 is not false

  because the result of ``bool(-0.1)`` is :ref:`True<test_what_is_true>`.

* I change assertFalse_ to assertTrue_

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 4-5

        def test_is_a_float_falsy_or_truthy(self):
            # self.assertFalse(bool(-0.1))
            self.assertTrue(bool(-0.1))
            # self.assertFalse(-0.1)
            self.assertTrue(-0.1)


    # NOTES

  - the test passes because the result of ``bool(-0.1)`` is :ref:`True<test_what_is_true>`
  - a negative float_ is grouped as :ref:`True<test_what_is_true>`
  - :ref:`a float is not the same object as True<test_assertion_error_w_true>`

* I add a :ref:`variable<what is a variable?>` for ``-0.1``

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 2

        def test_is_a_float_falsy_or_truthy(self):
            a_negative_float = -0.1
            # self.assertFalse(bool(-0.1))
            self.assertTrue(bool(-0.1))
            # self.assertFalse(-0.1)
            self.assertTrue(-0.1)


    # NOTES

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``-0.1``

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 4-5, 7-8

        def test_is_a_float_falsy_or_truthy(self):
            a_negative_float = -0.1
            # self.assertFalse(bool(-0.1))
            # self.assertTrue(bool(-0.1))
            self.assertTrue(bool(a_negative_float))
            # self.assertFalse(-0.1)
            # self.assertTrue(-0.1)
            self.assertTrue(a_negative_float)


    # NOTES

  the test is still green.

* I add an :ref:`assertion<what is an assertion?>` to test if ``0.0`` is grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 10

        def test_is_a_float_falsy_or_truthy(self):
            a_negative_float = -0.1
            # self.assertFalse(bool(-0.1))
            # self.assertTrue(bool(-0.1))
            self.assertTrue(bool(a_negative_float))
            # self.assertFalse(-0.1)
            # self.assertTrue(-0.1)
            self.assertTrue(a_negative_float)

            self.assertTrue(bool(0.0))


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  because the result of ``bool(0.0)`` is :ref:`False<test_what_is_false>`.

* I change assertTrue_ to assertFalse_

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 10-11

        def test_is_a_float_falsy_or_truthy(self):
            a_negative_float = -0.1
            # self.assertFalse(bool(-0.1))
            # self.assertTrue(bool(-0.1))
            self.assertTrue(bool(a_negative_float))
            # self.assertFalse(-0.1)
            # self.assertTrue(-0.1)
            self.assertTrue(a_negative_float)

            # self.assertTrue(bool(0.0))
            self.assertFalse(bool(0.0))


    # NOTES

  the test passes.

* I add a comment

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 8

    # NOTES
    # bool(-0.1) is True
    # bool(1) is True
    # bool(-1) is True
    # True is NOT False
    # True is NOT equal to False
    # True is a boolean
    # bool(0.0) is False
    # bool(0) is False
    # bool(None) is False
    # False is NOT True
    # False is NOT equal to True
    # False is a boolean

* I add an :ref:`assertion<what is an assertion?>` without bool_

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 3

            # self.assertTrue(bool(0.0))
            self.assertFalse(bool(0.0))
            self.assertTrue(0.0)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0.0 is not true

  because the result of ``bool(0.0)`` is :ref:`False<test_what_is_false>`.

* I change assertTrue_ to assertFalse_

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 3-4

            # self.assertTrue(bool(0.0))
            self.assertFalse(bool(0.0))
            # self.assertTrue(0.0)
            self.assertFalse(0.0)


    # NOTES

  - the test passes because the result of ``bool(0.0)`` is :ref:`False<test_what_is_false>`
  - :ref:`a float is not the same object as False<test_assertion_error_w_false>`

* I add an :ref:`assertion<what is an assertion?>` to test if ``0.1`` is grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 6

            # self.assertTrue(bool(0.0))
            self.assertFalse(bool(0.0))
            # self.assertTrue(0.0)
            self.assertFalse(0.0)

            self.assertFalse(bool(0.1))


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  - because the result of ``bool(0.1)`` is :ref:`True<test_what_is_true>`
  - I use ``0.1`` for all the floats_ (binary floating point decimal numbers) that are bigger than ``0.0``

* I change assertFalse_ to assertTrue_

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 6-7

            # self.assertTrue(bool(0.0))
            self.assertFalse(bool(0.0))
            # self.assertTrue(0.0)
            self.assertFalse(0.0)

            # self.assertFalse(bool(0.1))
            self.assertTrue(bool(0.1))


    # NOTES

  the test passes.

* I add a comment

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 2

    # NOTES
    # bool(0.1) is True
    # bool(-0.1) is True
    # True is NOT False
    # True is NOT equal to False
    # True is a boolean
    # bool(0.0) is False
    # bool(None) is False
    # False is NOT True
    # False is NOT equal to True
    # False is a boolean

* I add an :ref:`assertion<what is an assertion?>` without bool_

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 3

            # self.assertFalse(bool(0.1))
            self.assertTrue(bool(0.1))
            self.assertFalse(0.1)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0.1 is not false

  because the result of ``bool(0.1)`` is :ref:`True<test_what_is_true>`.

* I change assertTrue_ to assertFalse_

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 3-4

            # self.assertFalse(bool(0.1))
            self.assertTrue(bool(0.1))
            # self.assertFalse(0.1)
            self.assertTrue(0.1)


    # NOTES

  - the test passes because the result of ``bool(0.1)`` is :ref:`True<test_what_is_true>`
  - a positive float_ is grouped as :ref:`True<test_what_is_true>`
  - :ref:`a float is not the same object as True<test_assertion_error_w_true>`

* I add a :ref:`variable<what is a variable?>` for ``0.1``

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 6

            # self.assertTrue(bool(0.0))
            self.assertFalse(bool(0.0))
            # self.assertTrue(0.0)
            self.assertFalse(0.0)

            a_positive_float = 0.1
            # self.assertFalse(bool(0.1))
            self.assertTrue(bool(0.1))
            # self.assertFalse(0.1)
            self.assertTrue(0.1)


    # NOTES

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``0.1``

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 3-4, 6-7

            a_positive_float = 0.1
            # self.assertFalse(bool(0.1))
            # self.assertTrue(bool(0.1))
            self.assertTrue(bool(a_positive_float))
            # self.assertFalse(0.1)
            # self.assertTrue(0.1)
            self.assertTrue(0.1)


    # NOTES

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 36

        def test_is_a_float_falsy_or_truthy(self):
            negative_float = -0.1
            self.assertTrue(bool(negative_float))
            self.assertTrue(negative_float)

            self.assertFalse(bool(0.0))
            self.assertFalse(0.0)

            a_positive_float = 0.1
            self.assertTrue(bool(a_positive_float))
            self.assertTrue(0.1)


    # NOTES

* I make the new comments simpler because floats_ and integers_ are numbers and ``0.0`` is the same as ``0`` even though they are different types_

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2-3, 7

    # NOTES
    # bool(a positive number) is True
    # bool(a negative number) is True
    # True is NOT False
    # True is NOT equal to False
    # True is a boolean
    # bool(zero) is False
    # bool(None) is False
    # False is NOT True
    # False is NOT equal to True
    # False is a boolean

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_is_a_float_falsy_or_truthy'


* :ref:`'0.0' is grouped as False, positive and negative floats are grouped as True<test_is_a_float_falsy_or_truthy>`.
* :ref:`'0' is grouped as False, positive and negative integers are grouped as True<test_is_an_integer_falsy_or_truthy>`
* :ref:`None is grouped as False<test_is_none_falsy_or_truthy>`

-----

*********************************************************************************
test_is_a_string_falsy_or_truthy
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test for if a string_ (anything in :ref:`quotes`) is grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 5-6

            a_positive_float = 0.1
            self.assertTrue(bool(a_positive_float))
            self.assertTrue(0.1)

        def test_is_a_string_falsy_or_truthy(self):
            self.assertTrue(bool(str()))


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  because the result of ``bool(str())`` is :ref:`False<test_what_is_false>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change assertTrue_ to assertFalse_

.. code-block:: python
  :lineno-start: 48
  :emphasize-lines: 2-3

      def test_is_a_string_falsy_or_truthy(self):
          # self.assertTrue(bool(str()))
          self.assertFalse(bool(str()))


  # NOTES

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a comment

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 7

    # NOTES
    # bool(a positive number) is True
    # bool(a negative number) is True
    # True is NOT False
    # True is NOT equal to False
    # True is a boolean
    # bool(str()) is False
    # bool(zero) is False
    # bool(None) is False
    # False is NOT True
    # False is NOT equal to True
    # False is a boolean

* I add an :ref:`assertion<what is an assertion?>` without bool_

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 4

        def test_is_a_string_falsy_or_truthy(self):
            # self.assertTrue(bool(str()))
            self.assertFalse(bool(str()))
            self.assertTrue(str())


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '' is not true

  - because the result of ``bool(str())`` which is ``bool('')`` is :ref:`False<test_what_is_false>`
  - ``str()`` is another way to write ``''`` or ``""`` or ``''''''`` or ``""""""`` (the empty string_)

* I change assertTrue_ to assertFalse_

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 4-5

        def test_is_a_string_falsy_or_truthy(self):
            # self.assertTrue(bool(str()))
            self.assertFalse(bool(str()))
            # self.assertTrue(str())
            self.assertFalse(str())


    # NOTES

  - the test passes because the result of ``bool(str())`` is :ref:`False<test_what_is_false>`
  - the empty string_ is grouped as :ref:`True<test_what_is_true>`
  - :ref:`a string is not the same object as False<test_assertion_error_w_false>`

* I add an :ref:`assertion<what is an assertion?>` to test if a string_ with things is grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 7

        def test_is_a_string_falsy_or_truthy(self):
            # self.assertTrue(bool(str()))
            self.assertFalse(bool(str()))
            # self.assertTrue(str())
            self.assertFalse(str())

            self.assertFalse(bool("a string with things"))


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  because the result of ``bool("a string with things")`` is :ref:`True<test_what_is_true>`.

* I change assertFalse_ to assertTrue_

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 7-8

        def test_is_a_string_falsy_or_truthy(self):
            # self.assertTrue(bool(str()))
            self.assertFalse(bool(str()))
            # self.assertTrue(str())
            self.assertFalse(str())

            # self.assertFalse(bool("a string with things"))
            self.assertTrue(bool("a string with things"))


    # NOTES

  the test passes.

* I add a comment

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 2

    # NOTES
    # bool("a string with things") is True
    # bool(positive number) is True
    # bool(negative number) is True
    # True is NOT False
    # True is NOT equal to False
    # True is a boolean
    # bool(str()) is False
    # bool(zero) is False
    # bool(None) is False
    # False is NOT True
    # False is NOT equal to True
    # False is a boolean

* I add an :ref:`assertion<what is an assertion?>` without bool_

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 3

            # self.assertFalse(bool("a string with things"))
            self.assertTrue(bool("a string with things"))
            self.assertFalse("a string with things")


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'a string with things' is not false

  because the result of ``bool("a string with things")`` is :ref:`True<test_what_is_true>`.

* I change assertFalse_ to assertTrue_

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 3-4

            # self.assertFalse(bool("a string with things"))
            self.assertTrue(bool("a string with things"))
            # self.assertFalse("a string with things")
            self.assertTrue("a string with things")


    # NOTES

  - the test passes because the result of ``bool("a string with things")`` is :ref:`True<test_what_is_true>`
  - a string_ with things is grouped as :ref:`True<test_what_is_true>`
  - :ref:`a string is not the same object as True<test_assertion_error_w_true>`

* I add a :ref:`variable<what is a variable?>` for ``"a string with things"``

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 7

        def test_is_a_string_falsy_or_truthy(self):
            # self.assertTrue(bool(str()))
            self.assertFalse(bool(str()))
            # self.assertTrue(str())
            self.assertFalse(str())

            a_string = "a string with things"
            # self.assertFalse(bool("a string with things"))
            self.assertTrue(bool("a string with things"))
            # self.assertFalse("a string with things")
            self.assertTrue("a string with things")


    # NOTES

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``"a string with things"``

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 3-4, 6-7

            a_string = "a string with things"
            # self.assertFalse(bool("a string with things"))
            # self.assertTrue(bool("a string with things"))
            self.assertTrue(bool(a_string))
            # self.assertFalse("a string with things")
            # self.assertTrue("a string with things")
            self.assertTrue(a_string)


    # NOTES

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 48

        def test_is_a_string_falsy_or_truthy(self):
            self.assertFalse(bool(str()))
            self.assertFalse(str())

            a_string = "a string with things"
            self.assertTrue(bool(a_string))
            self.assertTrue(a_string)


    # NOTES

* I change the new comments to make them clearer

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 2, 8

    # NOTES
    # bool(a string with things) is True
    # bool(positive number) is True
    # bool(negative number) is True
    # True is NOT False
    # True is NOT equal to False
    # True is a boolean
    # bool(the empty string) is False
    # bool(zero) is False
    # bool(None) is False
    # False is NOT True
    # False is NOT equal to True
    # False is a boolean

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_is_a_string_falsy_or_truthy'

* :ref:`the empty string is grouped as False, a string with things is grouped as True<test_is_a_string_falsy_or_truthy>`
* :ref:`zero is grouped as False, and positive and negative numbers are grouped as True<test_is_a_float_falsy_or_truthy>`
* :ref:`None is grouped as False<test_is_none_falsy_or_truthy>`

-----

*********************************************************************************
test_is_a_tuple_falsy_or_truthy
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test for if a tuple_ (anything in parentheses ``( )`` separated by a comma) is grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 5-6

            a_string = "a string with things"
            self.assertTrue(bool(a_string))
            self.assertTrue(a_string)

        def test_is_a_tuple_falsy_or_truthy(self):
            self.assertTrue(bool(tuple()))


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  because the result of ``bool(tuple())`` is :ref:`False<test_what_is_false>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change assertTrue_ to assertFalse_

.. code-block:: python
  :lineno-start: 56
  :emphasize-lines: 2-3

      def test_is_a_tuple_falsy_or_truthy(self):
          # self.assertTrue(bool(tuple()))
          self.assertFalse(bool(tuple()))


  # NOTES

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a comment

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 8

    # NOTES
    # bool(a string with things) is True
    # bool(a positive number) is True
    # bool(a negative number) is True
    # True is NOT False
    # True is NOT equal to False
    # True is a boolean
    # bool(the empty tuple) is False
    # bool(the empty string) is False
    # bool(zero) is False
    # bool(None) is False
    # False is NOT True
    # False is NOT equal to True
    # False is a boolean

* I add an :ref:`assertion<what is an assertion?>` without bool_

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 4

        def test_is_a_tuple_falsy_or_truthy(self):
            # self.assertTrue(bool(tuple()))
            self.assertFalse(bool(tuple()))
            self.assertTrue(tuple())


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: () is not true

  - because the result of ``bool(tuple())`` which is ``bool(())`` is :ref:`False<test_what_is_false>`
  - ``tuple()`` is another way to write ``()`` (the empty tuple_)

* I change assertTrue_ to assertFalse_

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 4-5

        def test_is_a_tuple_falsy_or_truthy(self):
            # self.assertTrue(bool(tuple()))
            self.assertFalse(bool(tuple()))
            # self.assertTrue(tuple())
            self.assertFalse(tuple())


    # NOTES

  - the test passes because the result of ``bool(tuple())`` is :ref:`False<test_what_is_false>`
  - the empty tuple_ is grouped as :ref:`True<test_what_is_true>`
  - :ref:`a tuple is not the same object as False<test_assertion_error_w_false>`

* I add an :ref:`assertion<what is an assertion?>` to test if a tuple_ with things is grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 7

        def test_is_a_tuple_falsy_or_truthy(self):
            # self.assertTrue(bool(tuple()))
            self.assertFalse(bool(tuple()))
            # self.assertTrue(tuple())
            self.assertFalse(tuple())

            self.assertFalse(bool((0, 1, 2, 'n')))


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  because the result of ``bool((0, 1, 2, 'n'))`` is :ref:`True<test_what_is_true>`.

* I change assertFalse_ to assertTrue_

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 1-2

            # self.assertFalse(bool((0, 1, 2, 'n')))
            self.assertTrue(bool((0, 1, 2, 'n')))


    # NOTES

  the test passes.

* I add a comment

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 2

    # NOTES
    # bool(a tuple with things) is True
    # bool(a string with things) is True
    # bool(a positive number) is True
    # bool(a negative number) is True
    # True is NOT False
    # True is NOT equal to False
    # True is a boolean
    # bool(the empty tuple) is False
    # bool(the empty string) is False
    # bool(zero) is False
    # bool(None) is False
    # False is NOT True
    # False is NOT equal to True
    # False is a boolean

* I add an :ref:`assertion<what is an assertion?>` without bool_

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 3

            # self.assertFalse(bool((0, 1, 2, 'n')))
            self.assertTrue(bool((0, 1, 2, 'n')))
            self.assertFalse((0, 1, 2, 'n'))


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (0, 1, 2, 'n') is not false

  because the result of ``bool((0, 1, 2, 'n'))`` is :ref:`True<test_what_is_true>`.

* I change assertFalse_ to assertTrue_

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 3-4

            # self.assertFalse(bool((0, 1, 2, 'n')))
            self.assertTrue(bool((0, 1, 2, 'n')))
            # self.assertFalse((0, 1, 2, 'n'))
            self.assertTrue((0, 1, 2, 'n'))


    # NOTES

  - the test passes because the result of ``bool((0, 1, 2, 'n'))`` is :ref:`True<test_what_is_true>`
  - a tuple_ with things is grouped as :ref:`True<test_what_is_true>`
  - :ref:`a tuple is not the same object as True<test_assertion_error_w_true>`

* I add a :ref:`variable<what is a variable?>` for ``(0, 1, 2, 'n')``

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 7

        def test_is_a_tuple_falsy_or_truthy(self):
            # self.assertTrue(bool(tuple()))
            self.assertFalse(bool(tuple()))
            # self.assertTrue(tuple())
            self.assertFalse(tuple())

            a_tuple = (0, 1, 2, 'n')
            # self.assertFalse(bool((0, 1, 2, 'n')))
            self.assertTrue(bool((0, 1, 2, 'n')))
            # self.assertFalse((0, 1, 2, 'n'))
            self.assertTrue((0, 1, 2, 'n'))


    # NOTES

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``(0, 1, 2, 'n')``

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 3-4, 6-7

            a_tuple = (0, 1, 2, 'n')
            # self.assertFalse(bool((0, 1, 2, 'n')))
            # self.assertTrue(bool((0, 1, 2, 'n')))
            self.assertTrue(bool(a_tuple))
            # self.assertFalse((0, 1, 2, 'n'))
            # self.assertTrue((0, 1, 2, 'n'))
            self.assertTrue(a_tuple)


    # NOTES

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 56

        def test_is_a_tuple_falsy_or_truthy(self):
            self.assertFalse(bool(tuple()))
            self.assertFalse(tuple())

            a_tuple = (0, 1, 2, 'n')
            self.assertTrue(bool(a_tuple))
            self.assertTrue(a_tuple)


    # NOTES

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_is_a_tuple_falsy_or_truthy'

* :ref:`the empty tuple is grouped as False, a tuple with things is grouped as True<test_is_a_tuple_falsy_or_truthy>`
* :ref:`the empty string is grouped as False, a string with things is grouped as True<test_is_a_string_falsy_or_truthy>`
* :ref:`zero is grouped as False, and positive and negative numbers are grouped as True<test_is_a_float_falsy_or_truthy>`
* :ref:`None is grouped as False<test_is_none_falsy_or_truthy>`

-----

*********************************************************************************
test_is_a_list_falsy_or_truthy
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test for if a :ref:`list (anything in square brackets '[ ]')<what is a list?>` is grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 5-6

            a_tuple = (0, 1, 2, 'n')
            self.assertTrue(bool(a_tuple))
            self.assertTrue(a_tuple)

        def test_is_a_list_falsy_or_truthy(self):
            self.assertTrue(bool(list()))


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  because the result of ``bool(list())`` is :ref:`False<test_what_is_false>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change assertTrue_ to assertFalse_

.. code-block:: python
  :lineno-start: 64
  :emphasize-lines: 2-3

      def test_is_a_list_falsy_or_truthy(self):
          # self.assertTrue(bool(list()))
          self.assertFalse(bool(list()))


  # NOTES

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a comment

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 9

    # NOTES
    # bool(a tuple with things) is True
    # bool(a string with things) is True
    # bool(a positive number) is True
    # bool(a negative number) is True
    # True is NOT False
    # True is NOT equal to False
    # True is a boolean
    # bool(the empty list) is False
    # bool(the empty tuple) is False
    # bool(the empty string) is False
    # bool(zero) is False
    # bool(None) is False
    # False is NOT True
    # False is NOT equal to True
    # False is a boolean

* I add an :ref:`assertion<what is an assertion?>` without bool_

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 4

        def test_is_a_list_falsy_or_truthy(self):
            # self.assertTrue(bool(list()))
            self.assertFalse(bool(list()))
            self.assertTrue(list())


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: [] is not true

  - because the result of ``bool(list())`` which is ``bool([])`` is :ref:`False<test_what_is_false>`
  - ``list()`` is another way to write ``[]`` (the empty :ref:`list<what is a list?>`)

* I change assertTrue_ to assertFalse_

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 4-5

        def test_is_a_list_falsy_or_truthy(self):
            # self.assertTrue(bool(list()))
            self.assertFalse(bool(list()))
            # self.assertTrue(list())
            self.assertFalse(list())


    # NOTES

  - the test passes because the result of ``bool(list())`` is :ref:`False<test_what_is_false>`
  - the empty :ref:`list (anything in square brackets '[ ]')<what is a list?>` is grouped as :ref:`True<test_what_is_true>`
  - :ref:`a list is not the same object as False<test_assertion_error_w_false>`

* I add an :ref:`assertion<what is an assertion?>` to test if a :ref:`list (anything in square brackets '[ ]')<what is a list?>` with things is grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 7

        def test_is_a_list_falsy_or_truthy(self):
            # self.assertTrue(bool(list()))
            self.assertFalse(bool(list()))
            # self.assertTrue(list())
            self.assertFalse(list())

            self.assertFalse(bool([0, 1, 2, 'n']))


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  because the result of ``bool([0, 1, 2, 'n'])`` is :ref:`True<test_what_is_true>`.

* I change assertFalse_ to assertTrue_

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 1-2

            # self.assertFalse(bool([0, 1, 2, 'n']))
            self.assertTrue(bool([0, 1, 2, 'n']))


    # NOTES

  the test passes.

* I add a comment

  .. code-block:: python
    :lineno-start: 74
    :emphasize-lines: 2

    # NOTES
    # bool(a list with things) is True
    # bool(a tuple with things) is True
    # bool(a string with things) is True
    # bool(a positive number) is True
    # bool(a negative number) is True
    # True is NOT False
    # True is NOT equal to False
    # True is a boolean
    # bool(the empty list) is False
    # bool(the empty tuple) is False
    # bool(the empty string) is False
    # bool(zero) is False
    # bool(None) is False
    # False is NOT True
    # False is NOT equal to True
    # False is a boolean

* I add an :ref:`assertion<what is an assertion?>` without bool_

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 3

            # self.assertFalse(bool([0, 1, 2, 'n']))
            self.assertTrue(bool([0, 1, 2, 'n']))
            self.assertFalse([0, 1, 2, 'n'])


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: [0, 1, 2, 'n'] is not false

  because the result of ``bool([0, 1, 2, 'n'])`` is :ref:`True<test_what_is_true>`.

* I change assertFalse_ to assertTrue_

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 3-4

            # self.assertFalse(bool([0, 1, 2, 'n']))
            self.assertTrue(bool([0, 1, 2, 'n']))
            # self.assertFalse([0, 1, 2, 'n'])
            self.assertTrue([0, 1, 2, 'n'])


    # NOTES

  - the test passes because the result of ``bool([0, 1, 2, 'n'])`` is :ref:`True<test_what_is_true>`
  - a :ref:`list<what is a list?>` with things is grouped as :ref:`True<test_what_is_true>`
  - :ref:`a list is not the same object as True<test_assertion_error_w_true>`

* I add a :ref:`variable<what is a variable?>` for ``[0, 1, 2, 'n']``

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 7

        def test_is_a_list_falsy_or_truthy(self):
            # self.assertTrue(bool(list()))
            self.assertFalse(bool(list()))
            # self.assertTrue(list())
            self.assertFalse(list())

            a_list = [0, 1, 2, 'n']
            # self.assertFalse(bool([0, 1, 2, 'n']))
            self.assertTrue(bool([0, 1, 2, 'n']))
            # self.assertFalse([0, 1, 2, 'n'])
            self.assertTrue([0, 1, 2, 'n'])


    # NOTES

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``[0, 1, 2, 'n']``

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 3-4, 6-7

            a_list = [0, 1, 2, 'n']
            # self.assertFalse(bool([0, 1, 2, 'n']))
            # self.assertTrue(bool([0, 1, 2, 'n']))
            self.assertTrue(bool(a_list))
            # self.assertFalse([0, 1, 2, 'n'])
            # self.assertTrue([0, 1, 2, 'n'])
            self.assertTrue(a_list)


    # NOTES

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 64

        def test_is_a_list_falsy_or_truthy(self):
            self.assertFalse(bool(list()))
            self.assertFalse(list())

            a_list = [0, 1, 2, 'n']
            self.assertTrue(bool(a_list))
            self.assertTrue(a_list)


    # NOTES

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_is_a_list_falsy_or_truthy'

* :ref:`the empty list is grouped as False, a list with things is grouped as True<test_is_a_list_falsy_or_truthy>`
* :ref:`the empty tuple is grouped as False, a tuple with things is grouped as True<test_is_a_tuple_falsy_or_truthy>`
* :ref:`the empty string is grouped as False, a string with things is grouped as True<test_is_a_string_falsy_or_truthy>`
* :ref:`zero is grouped as False, and positive and negative numbers are grouped as True<test_is_a_float_falsy_or_truthy>`
* :ref:`None is grouped as False<test_is_none_falsy_or_truthy>`

-----

*********************************************************************************
test_is_a_set_falsy_or_truthy
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test for if a set_ (anything in curly braces ``{ }``, not :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`) is grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 68
    :emphasize-lines: 5-6

            a_list = [0, 1, 2, 'n']
            self.assertTrue(bool(a_list))
            self.assertTrue(a_list)

        def test_is_a_set_falsy_or_truthy(self):
            self.assertTrue(bool(set()))


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  because the result of ``bool(set())`` is :ref:`False<test_what_is_false>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change assertTrue_ to assertFalse_

.. code-block:: python
  :lineno-start: 72
  :emphasize-lines: 2-3

      def test_is_a_set_falsy_or_truthy(self):
          # self.assertTrue(bool(set()))
          self.assertFalse(bool(set()))


  # NOTES

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a comment

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 10

    # NOTES
    # bool(a list with things) is True
    # bool(a tuple with things) is True
    # bool(a string with things) is True
    # bool(a positive number) is True
    # bool(a negative number) is True
    # True is NOT False
    # True is NOT equal to False
    # True is a boolean
    # bool(the empty set) is False
    # bool(the empty list) is False
    # bool(the empty tuple) is False
    # bool(the empty string) is False
    # bool(zero) is False
    # bool(None) is False
    # False is NOT True
    # False is NOT equal to True
    # False is a boolean

* I add an :ref:`assertion<what is an assertion?>` without bool_

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 4

        def test_is_a_set_falsy_or_truthy(self):
            # self.assertTrue(bool(set()))
            self.assertFalse(bool(set()))
            self.assertTrue(set())


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: set() is not true

  because the result of ``bool(set())`` is :ref:`False<test_what_is_false>`.

* I change assertTrue_ to assertFalse_

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 4-5

        def test_is_a_set_falsy_or_truthy(self):
            # self.assertTrue(bool(set()))
            self.assertFalse(bool(set()))
            # self.assertTrue(set())
            self.assertFalse(set())


    # NOTES

  - the test passes because the result of ``bool(set())`` is :ref:`False<test_what_is_false>`
  - the empty set_ (anything in curly braces ``{ }``, not :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`) is grouped as :ref:`True<test_what_is_true>`
  - :ref:`a set is not the same object as False<test_assertion_error_w_false>`

* I add an :ref:`assertion<what is an assertion?>` to test if a set_ (anything in curly braces ``{ }``, not :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`) with things is grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 7

        def test_is_a_set_falsy_or_truthy(self):
            # self.assertTrue(bool(set()))
            self.assertFalse(bool(set()))
            # self.assertTrue(set())
            self.assertFalse(set())

            self.assertFalse(bool({0, 1, 2, 'n'}))


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  because the result of ``bool({0, 1, 2, 'n'})`` is :ref:`True<test_what_is_true>`.

* I change assertFalse_ to assertTrue_

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 1-2

            # self.assertFalse(bool({0, 1, 2, 'n'}))
            self.assertTrue(bool({0, 1, 2, 'n'}))


    # NOTES

  the test passes.

* I add a comment

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 2

    # NOTES
    # bool(a set with things) is True
    # bool(a list with things) is True
    # bool(a tuple with things) is True
    # bool(a string with things) is True
    # bool(a positive number) is True
    # bool(a negative number) is True
    # True is NOT False
    # True is NOT equal to False
    # True is a boolean
    # bool(the empty set) is False
    # bool(the empty list) is False
    # bool(the empty tuple) is False
    # bool(the empty string) is False
    # bool(zero) is False
    # bool(None) is False
    # False is NOT True
    # False is NOT equal to True
    # False is a boolean

* I add an :ref:`assertion<what is an assertion?>` without bool_

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 3

            # self.assertFalse(bool({0, 1, 2, 'n'}))
            self.assertTrue(bool({0, 1, 2, 'n'}))
            self.assertFalse({0, 1, 2, 'n'})


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {0, 1, 2, 'n'} is not false

  because the result of ``bool({0, 1, 2, 'n'})`` is :ref:`True<test_what_is_true>`.

* I change assertFalse_ to assertTrue_

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 3-4

            # self.assertFalse(bool({0, 1, 2, 'n'}))
            self.assertTrue(bool({0, 1, 2, 'n'}))
            # self.assertFalse({0, 1, 2, 'n'})
            self.assertTrue({0, 1, 2, 'n'})


    # NOTES

  - the test passes because the result of ``bool({0, 1, 2, 'n'})`` is :ref:`True<test_what_is_true>`
  - a set_ with things is grouped as :ref:`True<test_what_is_true>`
  - :ref:`a set is not the same object as True<test_assertion_error_w_true>`

* I add a :ref:`variable<what is a variable?>` for ``{0, 1, 2, 'n'}``

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 7

        def test_is_a_set_falsy_or_truthy(self):
            # self.assertTrue(bool(set()))
            self.assertFalse(bool(set()))
            # self.assertTrue(set())
            self.assertFalse(set())

            a_set = {0, 1, 2, 'n'}
            # self.assertFalse(bool({0, 1, 2, 'n'}))
            self.assertTrue(bool({0, 1, 2, 'n'}))
            # self.assertFalse({0, 1, 2, 'n'})
            self.assertTrue({0, 1, 2, 'n'})


    # NOTES

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``{0, 1, 2, 'n'}``

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 3-4, 6-7

            a_set = {0, 1, 2, 'n'}
            # self.assertFalse(bool({0, 1, 2, 'n'}))
            # self.assertTrue(bool({0, 1, 2, 'n'}))
            self.assertTrue(bool(a_set))
            # self.assertFalse({0, 1, 2, 'n'})
            # self.assertTrue({0, 1, 2, 'n'})
            self.assertTrue(a_set)


    # NOTES

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 72

        def test_is_a_set_falsy_or_truthy(self):
            self.assertFalse(bool(set()))
            self.assertFalse(set())

            a_set = {0, 1, 2, 'n'}
            self.assertTrue(bool(a_set))
            self.assertTrue(a_set)


    # NOTES

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_is_a_set_falsy_or_truthy'

* :ref:`the empty set is grouped as False, a set with things is grouped as True<test_is_a_set_falsy_or_truthy>`
* :ref:`the empty list is grouped as False, a list with things is grouped as True<test_is_a_list_falsy_or_truthy>`
* :ref:`the empty tuple is grouped as False, a tuple with things is grouped as True<test_is_a_tuple_falsy_or_truthy>`
* :ref:`the empty string is grouped as False, a string with things is grouped as True<test_is_a_string_falsy_or_truthy>`
* :ref:`zero is grouped as False, and positive and negative numbers are grouped as True<test_is_a_float_falsy_or_truthy>`
* :ref:`None is grouped as False<test_is_none_falsy_or_truthy>`

-----

*********************************************************************************
test_is_a_dictionary_falsy_or_truthy
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test for if a :ref:`dictionary (any key-value pairs in curly braces '{ }' separated by commas)<what is a dictionary?>` is grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 5-6

            a_set = {0, 1, 2, 'n'}
            self.assertTrue(bool(a_set))
            self.assertTrue(a_set)

        def test_is_a_dictionary_falsy_or_truthy(self):
            self.assertTrue(bool(dict()))


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  because the result of ``bool(dict())`` is :ref:`False<test_what_is_false>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change assertTrue_ to assertFalse_

.. code-block:: python
  :lineno-start: 80
  :emphasize-lines: 2-3

      def test_is_a_dictionary_falsy_or_truthy(self):
          # self.assertTrue(bool(dict()))
          self.assertFalse(bool(dict()))


  # NOTES

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a comment

  .. code-block:: python
    :lineno-start: 85
    :emphasize-lines: 11

    # NOTES
    # bool(a set with things) is True
    # bool(a list with things) is True
    # bool(a tuple with things) is True
    # bool(a string with things) is True
    # bool(a positive number) is True
    # bool(a negative number) is True
    # True is NOT False
    # True is NOT equal to False
    # True is a boolean
    # bool(the empty dictionary) is False
    # bool(the empty set) is False
    # bool(the empty list) is False
    # bool(the empty tuple) is False
    # bool(the empty string) is False
    # bool(zero) is False
    # bool(None) is False
    # False is NOT True
    # False is NOT equal to True
    # False is a boolean

* I add an :ref:`assertion<what is an assertion?>` without bool_

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 4

        def test_is_a_dictionary_falsy_or_truthy(self):
            # self.assertTrue(bool(dict()))
            self.assertFalse(bool(dict()))
            self.assertTrue(dict())


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {} is not true

  - because the result of ``bool(dict())`` is :ref:`False<test_what_is_false>`
  - ``dict()`` is another way to write ``{}`` (the empty :ref:`dictionary<what is a dictionary?>`)

* I change assertTrue_ to assertFalse_

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 4-5

        def test_is_a_dictionary_falsy_or_truthy(self):
            # self.assertTrue(bool(dict()))
            self.assertFalse(bool(dict()))
            # self.assertTrue(dict())
            self.assertFalse(dict())


    # NOTES

  - the test passes because the result of ``bool(dict())`` is :ref:`False<test_what_is_false>`
  - the empty :ref:`dictionary<what is a dictionary?>` is grouped as :ref:`True<test_what_is_true>`
  - :ref:`a dictionary is not the same object as False<test_assertion_error_w_false>`

* I add an :ref:`assertion<what is an assertion?>` to test if a :ref:`dictionary<what is a dictionary?>` with things is grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 7

        def test_is_a_dictionary_falsy_or_truthy(self):
            # self.assertTrue(bool(dict()))
            self.assertFalse(bool(dict()))
            # self.assertTrue(dict())
            self.assertFalse(dict())

            self.assertFalse(bool({'key': 'value'}))


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  because the result of ``bool({'key': 'value'})`` is :ref:`True<test_what_is_true>`.

* I change assertFalse_ to assertTrue_

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 1-2

            # self.assertFalse(bool({'key': 'value'}))
            self.assertTrue(bool({'key': 'value'}))


    # NOTES

  the test passes.

* I add a comment

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 2

    # NOTES
    # bool(a dictionary with things) is True
    # bool(a set with things) is True
    # bool(a list with things) is True
    # bool(a tuple with things) is True
    # bool(a string with things) is True
    # bool(a positive number) is True
    # bool(a negative number) is True
    # True is NOT False
    # True is NOT equal to False
    # True is a boolean
    # bool(the empty dictionary) is False
    # bool(the empty set) is False
    # bool(the empty list) is False
    # bool(the empty tuple) is False
    # bool(the empty string) is False
    # bool(zero) is False
    # bool(None) is False
    # False is NOT True
    # False is NOT equal to True
    # False is a boolean


    # Exceptions seen
    # AssertionError

* I add an :ref:`assertion<what is an assertion?>` without bool_

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 3

            # self.assertFalse(bool({'key': 'value'}))
            self.assertTrue(bool({'key': 'value'}))
            self.assertFalse({'key': 'value'})


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: {'key': 'value'} is not false

  because the result of ``bool({'key': 'value'})`` is :ref:`True<test_what_is_true>`.

* I change assertFalse_ to assertTrue_

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 3-4

            # self.assertFalse(bool({'key': 'value'}))
            self.assertTrue(bool({'key': 'value'}))
            # self.assertFalse({'key': 'value'})
            self.assertTrue({'key': 'value'})


    # NOTES

  - the test passes because the result of ``bool({'key': 'value'})`` is :ref:`True<test_what_is_true>`
  - a :ref:`dictionary<what is a dictionary?>` with things is grouped as :ref:`True<test_what_is_true>`
  - :ref:`a dictionary is not the same object as True<test_assertion_error_w_true>`

* I add a :ref:`variable<what is a variable?>` for ``{'key': 'value'}``

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 7

        def test_is_a_dictionary_falsy_or_truthy(self):
            # self.assertTrue(bool(dict()))
            self.assertFalse(bool(dict()))
            # self.assertTrue(dict())
            self.assertFalse(dict())

            a_dictionary = {'key': 'value'}
            # self.assertFalse(bool({'key': 'value'}))
            self.assertTrue(bool({'key': 'value'}))
            # self.assertFalse({'key': 'value'})
            self.assertTrue({'key': 'value'})


    # NOTES

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``{'key': 'value'}``

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 3-4, 6-7

            a_dictionary = {'key': 'value'}
            # self.assertFalse(bool({'key': 'value'}))
            # self.assertTrue(bool({'key': 'value'}))
            self.assertTrue(bool(a_dictionary))
            # self.assertFalse({'key': 'value'})
            # self.assertTrue({'key': 'value'})
            self.assertTrue(a_dictionary)


    # NOTES

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 80

        def test_is_a_dictionary_falsy_or_truthy(self):
            self.assertFalse(bool(dict()))
            self.assertFalse(dict())

            a_dictionary = {'key': 'value'}
            self.assertTrue(bool(a_dictionary))
            self.assertTrue(a_dictionary)


    # NOTES

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_is_a_dictionary_falsy_or_truthy'

* :ref:`the empty dictionary is grouped as False and a set with things is grouped as True<test_is_a_dictionary_falsy_or_truthy>`
* :ref:`the empty set is grouped as False and a set with things is grouped as True<test_is_a_set_falsy_or_truthy>`
* :ref:`the empty list is grouped as False and a list with things is grouped as True<test_is_a_list_falsy_or_truthy>`
* :ref:`the empty tuple is grouped as False and a tuple with things is grouped as True<test_is_a_tuple_falsy_or_truthy>`
* :ref:`the empty string is grouped as False and a string with things is grouped as True<test_is_a_string_falsy_or_truthy>`
* :ref:`zero is grouped as False, and positive and negative numbers are grouped as True<test_is_a_float_falsy_or_truthy>`
* :ref:`None is grouped as False<test_is_none_falsy_or_truthy>`

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_booleans.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``booleans``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

----

*********************************************************************************
review
*********************************************************************************

I know from the tests, that :ref:`True<test_what_is_true>` and :ref:`False<test_what_is_false>` are different and are both :ref:`booleans<what are booleans?>`. In Python_ the following :ref:`objects<everything is an object>` are grouped as

* :ref:`False<test_what_is_false>`

  * an empty container (strings_, tuples_, :ref:`lists<what is a list?>`, sets_, :ref:`dictionaries<what is a dictionary?>`)
  * ``0``
  * ``0.0``
  * :ref:`None<what is None?>`

* :ref:`True<test_what_is_true>`

  * a container with things is :ref:`True<test_what_is_true>`
  * positive and negative numbers are :ref:`True<test_what_is_true>`

These things come in handy when I want :ref:`programs to make decisions<if statements>`, because they can choose what to do based on if the :ref:`data<basic objects>` is grouped as :ref:`False<test_what_is_false>` (``0``, empty or :ref:`None<what is None?>` ) or is grouped as :ref:`True<test_what_is_true>` (positive and negative numbers or has something in it).

:ref:`How many questions can you answer after going through this chapter?<questions about Booleans>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<booleans: tests>`

----

*************************************************************************************
what is next?
*************************************************************************************

you now know

* :ref:`how to make a Python test driven development environment manually`
* :ref:`what an assertion is<what is an assertion?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to pass values from tests to functions<telephone>`
* :ref:`how to make dictionaries with functions<how to make a person>`
* :ref:`how to make classes<classes>`
* :ref:`how to use class attributes to remove repetition<AssertionError 2: use class attributes>`
* :ref:`what happens when classes have one or more parents<family ties>`
* :ref:`what causes AttributeError<what causes AttributeError?>`
* :ref:`what None is and is not<what is None?>`
* :ref:`how to use the assertIsNotNone and assertIsNone methods<test AssertionError with assertIsNotNone and assertIsNone>`
* :ref:`what booleans are<what are booleans?>`

:ref:`Would you like to test the truth table?<truth table>` It will help you understand writing programs_ that make decisions based on :ref:`conditions<if statements>`.

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