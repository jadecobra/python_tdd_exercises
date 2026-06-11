.. meta::
  :description: Master Python's truthiness and falsiness rules through Test Driven Development (TDD). This step-by-step tutorial uses unittest.assertTrue and assertFalse to explore why 0, 0.0, None, and empty collections (strings, lists, tuples, sets, and dicts) are False, while non-zero numbers and populated collections are True. Includes instructions for setting up a Python project with uv and automating tests with pytest-watcher.
  :keywords: Jacob Itegboje, Python booleans for beginners, Python truthiness and falsiness, what is False Python unittest assertTrue, Python unittest assertFalse, TDD Red Green Refactor tutorial, Python bool type explained, is empty list True or False, is 0.0 False is None False or True, testing Python data structures, python uv init, pytest-watcher tutorial, boolean logic in programming, truthy and falsy values list, python empty string boolean, python empty dict truthiness, python zero-based indexing, python unit testing tutorial

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

I want to test what groups the :ref:`Python basic data structures<data structures>` seen so far - :ref:`None<what is None?>`, integers_, floats_, strings_, tuples_, :ref:`lists`, sets_ and :ref:`dictionaries<what is a dictionary?>`, would fall into when we divide them into two groups - :ref:`False<test_what_is_false>` and :ref:`True<test_what_is_true>`. What do you think will happen?

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

Questions to think about as we divide :ref:`Python's basic data structures<data structures>` into  :ref:`False<test_what_is_false>` and :ref:`True<test_what_is_true>`

* :ref:`what is False?<test_what_is_false>`
* :ref:`what is True?<test_what_is_true>`
* :ref:`Is None grouped as False or True?<test_is_none_falsy_or_truthy>`
* :ref:`Is an integer grouped as False or True?<test_is_an_integer_falsy_or_truthy>`
* :ref:`Is a float grouped as False or True?<test_is_a_float_falsy_or_truthy>`
* :ref:`Is a string grouped as False or True?<test_is_a_string_falsy_or_truthy>`
* :ref:`Is a tuple grouped as False or True?<test_is_a_tuple_falsy_or_truthy>`
* :ref:`Is a list grouped as False or True?<is_a_list_falsy_or_truthy>`
* :ref:`Is a set grouped as False or True?<is_a_set_falsy_or_truthy>`
* :ref:`Is a dictionary grouped as False or True?<is_a_dictionary_falsy_or_truthy>`

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

    echo "pytest-watcher" > requirements.txt

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
    * if you ran ``echo "pytest-watcher" > requirements.txt``, to add ``pytest-watcher`` to the requirements file_

    fix those errors and try to run ``uv run pytest-watcher . --now`` again

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

* then I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

  the test passes.

----

*********************************************************************************
test_what_is_false
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change :ref:`test_failure` to :ref:`test_what_is_false`, then use the :ref:`assertNotIsInstance method<another way to test if something is NOT an instance of a class>` I learned from :ref:`everything is an object` to check if False_ is :ref:`an instance (a copy)<how to test if something is an instance of a class>` of the :ref:`bool class<what are booleans?>`

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

I change :ref:`assertNotIsInstance<another way to test if something is NOT an instance of a class>` to the :ref:`assertIsInstance method<another way to test if something is an instance of a class>`

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
how to test if something should be grouped as False
*********************************************************************************

----

I can test if I should group an :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>` with the `bool built-in function`_ from `The Python Standard Library`_. It checks if Python_ groups the thing in parentheses as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`.

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

  which raises :ref:`AssertionError<what causes AssertionError?>` since :ref:`False<test_what_is_false>`, which is the result of ``bool(False)`` is not equal to :ref:`True<test_what_is_true>`.

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
another way to test if something should be grouped as False
*********************************************************************************

----

The `unittest.TestCase class`_ has a :ref:`method<what is a method?>` I can use to test if the result of calling the `bool built-in function`_ with an :ref:`object<what is a class?>` is :ref:`False<test_what_is_false>` - assertFalse_, it was in :ref:`the first failing test<test_failure>`

.. code-block:: python

  self.assertFalse(True)

which is like

.. code-block:: python

  self.assertEqual(bool(True), False)

it raises :ref:`AssertionError<what causes AssertionError?>` if the :ref:`object<what is a class?>` in parentheses is grouped as :ref:`True<test_what_is_true>`.

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

    # Exceptions seen
    # AssertionError

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

* It turns out that I can skip bool_ and get the same result. I add another call to the `assertFalse method`_

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

  The `assertFalse method`_ raises :ref:`AssertionError<what causes AssertionError?>` if the result of a call to the `bool built-in function`_ with an :ref:`object<what is a class?>` is :ref:`True<test_what_is_true>`.

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

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for :ref:`True<test_what_is_true>` with the :ref:`assertNotIsInstance method<another way to test if something is NOT an instance of a class>` I learned from :ref:`everything is an object` to check if True_ is :ref:`an instance (a copy)<how to test if something is an instance of a class>` of the :ref:`bool class<what are booleans?>`

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

I change :ref:`assertNotIsInstance<another way to test if something is NOT an instance of a class>` to the :ref:`assertIsInstance method<another way to test if something is an instance of a class>`

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

    # Exceptions seen
    # AssertionError

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
how to test if something should be grouped as True
*********************************************************************************

----

I will use the `bool built-in function`_ from `The Python Standard Library`_ to test if I should group an :ref:`object<what is a class?>` as :ref:`True<test_what_is_true>` since It checks if Python_ groups the :ref:`object<what is a class?>` in parentheses as :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`.

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

  which raises :ref:`AssertionError<what causes AssertionError?>` since :ref:`True<test_what_is_true>`, which is the result of ``bool(True)`` is not equal to :ref:`False<test_what_is_false>`.

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
another way to test if something should be grouped as True
*********************************************************************************

----

The `unittest.TestCase class`_ has a :ref:`method<what is a method?>` I can use to test if the result of calling the `bool built-in function`_ with an :ref:`object<what is a class?>` is :ref:`True<test_what_is_true>` - assertTrue_. It raises :ref:`AssertionError<what causes AssertionError?>` if the :ref:`object<what is a class?>` in parentheses is grouped as :ref:`False<test_what_is_false>`.

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

    # Exceptions seen
    # AssertionError

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

* I can skip bool_ and get the same result. I add another call to the `assertTrue method`_

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

  The `assertTrue method`_ raises :ref:`AssertionError<what causes AssertionError?>` if the result of a call to the `bool built-in function`_ with an :ref:`object<what is a class?>` is :ref:`False<test_what_is_false>`.

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

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests
* I add a test to see if :ref:`None<what is None?>` should be grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

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

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests
* I add a test for if an integer_ (a whole number without decimals) should be grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

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
  - negative integers_ are grouped as :ref:`True<test_what_is_true>`
  - :ref:`an integer is not the same object as True<test_assertion_error_w_true>`

* I add an :ref:`assertion<what is an assertion?>` to test if ``0`` should be grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 6

        def test_is_an_integer_falsy_or_truthy(self):
            # self.assertFalse(bool(-1))
            self.assertTrue(bool(-1))
            # self.assertFalse(-1)
            self.assertTrue(-1)
            self.assertTrue(bool(0))


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  because the result of ``bool(0)`` is :ref:`False<test_what_is_false>`.

* I change assertTrue_ to assertFalse_

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 6-7

        def test_is_an_integer_falsy_or_truthy(self):
            # self.assertFalse(bool(-1))
            self.assertTrue(bool(-1))
            # self.assertFalse(-1)
            self.assertTrue(-1)
            # self.assertTrue(bool(0))
            self.assertFalse(bool(0))


    # NOTES

  the test passes.

* I add a comment

  .. code-block:: python
    :lineno-start: 33
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
    :lineno-start: 24
    :emphasize-lines: 8

        def test_is_an_integer_falsy_or_truthy(self):
            # self.assertFalse(bool(-1))
            self.assertTrue(bool(-1))
            # self.assertFalse(-1)
            self.assertTrue(-1)
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
    :lineno-start: 24
    :emphasize-lines: 8-9

        def test_is_an_integer_falsy_or_truthy(self):
            # self.assertFalse(bool(-1))
            self.assertTrue(bool(-1))
            # self.assertFalse(-1)
            self.assertTrue(-1)
            # self.assertTrue(bool(0))
            self.assertFalse(bool(0))
            # self.assertTrue(0)
            self.assertFalse(0)


    # NOTES

  - the test passes because the result of ``bool(0)`` is :ref:`False<test_what_is_false>`
  - :ref:`an integer is not the same object as False<test_assertion_error_w_false>`

* I add an :ref:`assertion<what is an assertion?>` to test if ``1`` should be grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 10

        def test_is_an_integer_falsy_or_truthy(self):
            # self.assertFalse(bool(-1))
            self.assertTrue(bool(-1))
            # self.assertFalse(-1)
            self.assertTrue(-1)
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
    :lineno-start: 24
    :emphasize-lines: 10-11

        def test_is_an_integer_falsy_or_truthy(self):
            # self.assertFalse(bool(-1))
            self.assertTrue(bool(-1))
            # self.assertFalse(-1)
            self.assertTrue(-1)
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
    :lineno-start: 37
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
    :lineno-start: 24
    :emphasize-lines: 12

        def test_is_an_integer_falsy_or_truthy(self):
            # self.assertFalse(bool(-1))
            self.assertTrue(bool(-1))
            # self.assertFalse(-1)
            self.assertTrue(-1)
            # self.assertTrue(bool(0))
            self.assertFalse(bool(0))
            # self.assertTrue(0)
            self.assertFalse(0)
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
    :lineno-start: 24
    :emphasize-lines: 12-13

        def test_is_an_integer_falsy_or_truthy(self):
            # self.assertFalse(bool(-1))
            self.assertTrue(bool(-1))
            # self.assertFalse(-1)
            self.assertTrue(-1)
            # self.assertTrue(bool(0))
            self.assertFalse(bool(0))
            # self.assertTrue(0)
            self.assertFalse(0)
            # self.assertFalse(bool(1))
            self.assertTrue(bool(1))
            # self.assertFalse(1)
            self.assertTrue(1)


    # NOTES

  - the test passes because the result of ``bool(1)`` is :ref:`True<test_what_is_true>`
  - positive integers_ are grouped as :ref:`True<test_what_is_true>`
  - :ref:`an integer is not the same object as True<test_assertion_error_w_true>`

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 24

        def test_is_an_integer_falsy_or_truthy(self):
            self.assertTrue(bool(-1))
            self.assertTrue(-1)

            self.assertFalse(bool(0))
            self.assertFalse(0)

            self.assertTrue(bool(1))
            self.assertTrue(1)


    # NOTES

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_is_an_integer_falsy_or_truthy'

* :ref:`'0' is grouped as False, and positive and negative integers are grouped as True<test_is_an_integer_falsy_or_truthy>`
* :ref:`None is grouped as False<test_is_none_falsy_or_truthy>`

----

*********************************************************************************
test_is_a_float_falsy_or_truthy
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests
* I add a test for if a float_ (binary floating point decimal number) should be grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 11-12

        def test_is_an_integer_falsy_or_truthy(self):
            self.assertTrue(bool(-1))
            self.assertTrue(-1)

            self.assertFalse(bool(0))
            self.assertFalse(0)

            self.assertTrue(bool(1))
            self.assertTrue(1)

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
  :lineno-start: 34
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
    :lineno-start: 39
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
    :lineno-start: 34
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
    :lineno-start: 34
    :emphasize-lines: 4-5

        def test_is_a_float_falsy_or_truthy(self):
            # self.assertFalse(bool(-0.1))
            self.assertTrue(bool(-0.1))
            # self.assertFalse(-0.1)
            self.assertTrue(-0.1)


    # NOTES

  - the test passes because the result of ``bool(-0.1)`` is :ref:`True<test_what_is_true>`
  - negative floats_ are grouped as :ref:`True<test_what_is_true>`
  - :ref:`a float is not the same object as True<test_assertion_error_w_true>`

* I add an :ref:`assertion<what is an assertion?>` to test if ``0.0`` should be grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 6

        def test_is_a_float_falsy_or_truthy(self):
            # self.assertFalse(bool(-0.1))
            self.assertTrue(bool(-0.1))
            # self.assertFalse(-0.1)
            self.assertTrue(-0.1)
            self.assertTrue(bool(0.0))


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  because the result of ``bool(0.0)`` is :ref:`False<test_what_is_false>`.

* I change assertTrue_ to assertFalse_

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 6-7

        def test_is_a_float_falsy_or_truthy(self):
            # self.assertFalse(bool(-0.1))
            self.assertTrue(bool(-0.1))
            # self.assertFalse(-0.1)
            self.assertTrue(-0.1)
            # self.assertTrue(bool(0.0))
            self.assertFalse(bool(0.0))


    # NOTES

  the test passes.

* I add a comment

  .. code-block:: python
    :lineno-start: 43
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
    :lineno-start: 34
    :emphasize-lines: 8

        def test_is_a_float_falsy_or_truthy(self):
            # self.assertFalse(bool(-0.1))
            self.assertTrue(bool(-0.1))
            # self.assertFalse(-0.1)
            self.assertTrue(-0.1)
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
    :lineno-start: 34
    :emphasize-lines: 8-9

        def test_is_a_float_falsy_or_truthy(self):
            # self.assertFalse(bool(-0.1))
            self.assertTrue(bool(-0.1))
            # self.assertFalse(-0.1)
            self.assertTrue(-0.1)
            # self.assertTrue(bool(0.0))
            self.assertFalse(bool(0.0))
            # self.assertTrue(0.0)
            self.assertFalse(0.0)


    # NOTES

  - the test passes because the result of ``bool(0.0)`` is :ref:`False<test_what_is_false>`
  - :ref:`a float is not the same object as False<test_assertion_error_w_false>`

* I add an :ref:`assertion<what is an assertion?>` to test if ``0.1`` should be grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 10

        def test_is_a_float_falsy_or_truthy(self):
            # self.assertFalse(bool(-0.1))
            self.assertTrue(bool(-0.1))
            # self.assertFalse(-0.1)
            self.assertTrue(-0.1)
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
    :lineno-start: 34
    :emphasize-lines: 10-11

        def test_is_a_float_falsy_or_truthy(self):
            # self.assertFalse(bool(-0.1))
            self.assertTrue(bool(-0.1))
            # self.assertFalse(-0.1)
            self.assertTrue(-0.1)
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
    :lineno-start: 37
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
    :lineno-start: 34
    :emphasize-lines: 12

        def test_is_a_float_falsy_or_truthy(self):
            # self.assertFalse(bool(-0.1))
            self.assertTrue(bool(-0.1))
            # self.assertFalse(-0.1)
            self.assertTrue(-0.1)
            # self.assertTrue(bool(0.0))
            self.assertFalse(bool(0.0))
            # self.assertTrue(0.0)
            self.assertFalse(0.0)
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
    :lineno-start: 34
    :emphasize-lines: 12-13

        def test_is_a_float_falsy_or_truthy(self):
            # self.assertFalse(bool(-0.1))
            self.assertTrue(bool(-0.1))
            # self.assertFalse(-0.1)
            self.assertTrue(-0.1)
            # self.assertTrue(bool(0.0))
            self.assertFalse(bool(0.0))
            # self.assertTrue(0.0)
            self.assertFalse(0.0)
            # self.assertFalse(bool(0.1))
            self.assertTrue(bool(0.1))
            # self.assertFalse(0.1)
            self.assertTrue(0.1)


    # NOTES

  - the test passes because the result of ``bool(0.1)`` is :ref:`True<test_what_is_true>`
  - positive floats_ are grouped as :ref:`True<test_what_is_true>`
  - :ref:`a float is not the same object as True<test_assertion_error_w_true>`

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 34

        def test_is_a_float_falsy_or_truthy(self):
            self.assertTrue(bool(-0.1))
            self.assertTrue(-0.1)

            self.assertFalse(bool(0.0))
            self.assertFalse(0.0)

            self.assertTrue(bool(0.1))
            self.assertTrue(0.1)


    # NOTES

* I make the new comments simpler because floats_ and integers_ are numbers and ``0.0`` is the same as ``0`` even though they are different types_

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2-3, 7

    # NOTES
    # bool(positive number) is True
    # bool(negative number) is True
    # True is NOT False
    # True is NOT equal to False
    # True is a boolean
    # bool(zero) is False
    # bool(None) is False
    # False is NOT True
    # False is NOT equal to True
    # False is a boolean

    # Exceptions seen
    # AssertionError

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_is_a_float_falsy_or_truthy'


* :ref:`'0.0' is grouped as False, and positive and negative floats are grouped as True<test_is_a_float_falsy_or_truthy>`.
* :ref:`'0' is grouped as False, and positive and negative integers are grouped as True<test_is_an_integer_falsy_or_truthy>`
* :ref:`None is grouped as False<test_is_none_falsy_or_truthy>`


-----

*********************************************************************************
test_is_a_string_falsy_or_truthy
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests
* I add a test for if a string_ (anything in :ref:`quotes`) should be grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 34
  :emphasize-lines: 11-12

      def test_is_a_float_falsy_or_truthy(self):
          self.assertTrue(bool(-0.1))
          self.assertTrue(-0.1)

          self.assertFalse(bool(0.0))
          self.assertFalse(0.0)

          self.assertTrue(bool(0.1))
          self.assertTrue(0.1)

      def test_is_string_falsy_or_truthy(self):
          self.assertTrue(bool(str()))


  # NOTES

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: False is not true

* because the result of ``bool(str())`` is :ref:`False<test_what_is_false>`
* ``str()`` is another way to write ``''`` or ``""`` or ``''''''`` or ``""""""`` (the empty string_)

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change assertTrue_ to assertFalse_

.. code-block:: python
  :lineno-start: 44
  :emphasize-lines: 2-3

      def test_is_string_falsy_or_truthy(self):
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
    :lineno-start: 49
    :emphasize-lines: 7

    # NOTES
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
    :lineno-start: 44
    :emphasize-lines: 4

        def test_is_string_falsy_or_truthy(self):
            # self.assertTrue(bool(str()))
            self.assertFalse(bool(str()))
            self.assertTrue(str())


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: '' is not true

  because the result of ``bool(str())`` which is ``bool('')`` is :ref:`False<test_what_is_false>`.

* I change assertTrue_ to assertFalse_

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 4-5

        def test_is_string_falsy_or_truthy(self):
            # self.assertTrue(bool(str()))
            self.assertFalse(bool(str()))
            # self.assertTrue(str())
            self.assertFalse(str())


    # NOTES

  - the test passes because the result of ``bool(str())`` is :ref:`False<test_what_is_false>`
  - the empty string_ is grouped as :ref:`True<test_what_is_true>`
  - :ref:`a string is not the same object as False<test_assertion_error_w_false>`

* I add an :ref:`assertion<what is an assertion?>` to test if a string_ with things should be grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 6

        def test_is_string_falsy_or_truthy(self):
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
    :lineno-start: 44
    :emphasize-lines: 6-7

        def test_is_string_falsy_or_truthy(self):
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
    :lineno-start: 53
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
    :lineno-start: 44
    :emphasize-lines: 8

        def test_is_string_falsy_or_truthy(self):
            # self.assertTrue(bool(str()))
            self.assertFalse(bool(str()))
            # self.assertTrue(str())
            self.assertFalse(str())
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
    :lineno-start: 34
    :emphasize-lines: 8-9

        def test_is_string_falsy_or_truthy(self):
            # self.assertTrue(bool(str()))
            self.assertFalse(bool(str()))
            # self.assertTrue(str())
            self.assertFalse(str())
            # self.assertFalse(bool("a string with things"))
            self.assertTrue(bool("a string with things"))
            # self.assertFalse("a string with things")
            self.assertTrue("a string with things")


    # NOTES

  - the test passes because the result of ``bool("a string with things")`` is :ref:`True<test_what_is_true>`
  - strings_ with things are grouped as :ref:`True<test_what_is_true>`
  - :ref:`a string is not the same object as True<test_assertion_error_w_true>`

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 44

        def test_is_string_falsy_or_truthy(self):
            self.assertFalse(bool(str()))
            self.assertFalse(str())

            self.assertTrue(bool("a string with things"))
            self.assertTrue("a string with things")


    # NOTES

* I change the new comments to make them clearer

  .. code-block:: python
    :lineno-start: 52
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

* :ref:`the empty string is grouped as False and a string with things is grouped as  True<test_is_a_string_falsy_or_truthy>`
* :ref:`zero is grouped as False, and positive and negative numbers are grouped as True<test_is_an_integer_falsy_or_truthy>`
* :ref:`None is grouped as False<test_is_none_falsy_or_truthy>`

* I go back to the terminal_ that is running the tests

----

*********************************************************************************
test_is_a_tuple_falsy_or_truthy
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add an :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_true` to test if a tuple_ (anything in parentheses (``()``) separated by commas) should be grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 14
  :emphasize-lines: 9

      def test_what_is_true(self):
          self.assertIsInstance(True, bool)
          self.assertTrue(True)
          self.assertTrue(-1)
          self.assertTrue(1)
          self.assertTrue(-0.1)
          self.assertTrue(0.1)
          self.assertTrue("a string with things")
          self.assertTrue(tuple())


  # NOTES

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: () is not true

:ref:`the empty tuple is not True<test_is_a_tuple_falsy_or_truthy>`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the `assert method`_

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 1

            self.assertFalse(tuple())

  the test passes.

* I add a comment

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 7

    # NOTES
    # a string with things is True
    # positive and negative numbers are True
    # True is True
    # True is not false
    # True is a boolean
    # the empty tuple is False
    # the empty string is False
    # 0 is False
    # None is False
    # False is False
    # False is not true
    # False is a boolean

* I move the :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_false`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 8

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(None)
            self.assertFalse(0)
            self.assertFalse(0.0)
            self.assertFalse(str())
            self.assertFalse(tuple())

        def test_what_is_true(self):

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_false` to test if a tuple_ with things should be grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 4

            self.assertFalse(0.0)
            self.assertFalse(str())
            self.assertFalse(tuple())
            self.assertFalse((1, 2, 3, 'n'))

        def test_what_is_true(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (1, 2, 3, 'n') is not false

  :ref:`a tuple with things is NOT False<test_is_a_tuple_falsy_or_truthy>`

* I change the :ref:`method<what is a method?>`

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 1

            self.assertTrue((1, 2, 3, 'n'))

  the test passes.

* I add a comment

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 2

    # NOTES
    # a tuple with things is True
    # a string with things is True
    # positive and negative numbers are True
    # True is True
    # True is not false
    # True is a boolean
    # the empty tuple is False
    # the empty string is False
    # 0 is False
    # None is False
    # False is False
    # False is not true
    # False is a boolean

* I move the :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_true`



  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 12

            self.assertFalse(str())
            self.assertFalse(tuple())

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)
            self.assertTrue(-1)
            self.assertTrue(1)
            self.assertTrue(-0.1)
            self.assertTrue(0.1)
            self.assertTrue("a string with things")
            self.assertTrue((1, 2, 3, 'n'))


    # NOTES

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add '

* I go back to the terminal_ that is running the tests

:ref:`the empty tuple is False and a tuple with things is True<test_is_a_tuple_falsy_or_truthy>`

----

*********************************************************************************
is_a_list_falsy_or_truthy
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add an :ref:`assertion<what is an assertion?>` to test if a :ref:`list<lists>` (anything in square brackets (``[]``)) should be grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 15
  :emphasize-lines: 10

      def test_what_is_true(self):
          self.assertIsInstance(True, bool)
          self.assertTrue(True)
          self.assertTrue(-1)
          self.assertTrue(1)
          self.assertTrue(-0.1)
          self.assertTrue(0.1)
          self.assertTrue("a string with things")
          self.assertTrue((1, 2, 3, 'n'))
          self.assertTrue(list())


  # NOTES

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: [] is not true

:ref:`the empty list is NOT True<is_a_list_falsy_or_truthy>`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the :ref:`method<what is a method?>`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 1

            self.assertFalse(list())

  the test passes.

* I add a comment

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 8

    # NOTES
    # a tuple with things is True
    # a string with things is True
    # positive and negative numbers are True
    # True is True
    # True is not false
    # True is a boolean
    # the empty list is False
    # the empty tuple is False
    # the empty string is False
    # 0 is False
    # None is False
    # False is False
    # False is not true
    # False is a boolean

* I move the :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_false`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 9

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(None)
            self.assertFalse(0)
            self.assertFalse(0.0)
            self.assertFalse(str())
            self.assertFalse(tuple())
            self.assertFalse(list())

        def test_what_is_true(self):

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_false` to test if a :ref:`list<lists>` with things should be grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 4

            self.assertFalse(str())
            self.assertFalse(tuple())
            self.assertFalse(list())
            self.assertFalse([1, 2, 3, 'n'])

        def test_what_is_true(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: [1, 2, 3, 'n'] is not false

* I change the :ref:`method<what is a method?>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 1

            self.assertTrue([1, 2, 3, 'n'])

  the test passes.

* I add a comment

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 2

    # NOTES
    # a list with things is True
    # a tuple with things is True
    # a string with things is True
    # positive and negative numbers are True
    # True is True
    # True is not false
    # True is a boolean
    # the empty list is False
    # the empty tuple is False
    # the empty string is False
    # 0 is False
    # None is False
    # False is False
    # False is not true
    # False is a boolean

* I move the :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_true`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 13

            self.assertFalse(tuple())
            self.assertFalse(list())

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)
            self.assertTrue(-1)
            self.assertTrue(1)
            self.assertTrue(-0.1)
            self.assertTrue(0.1)
            self.assertTrue("a string with things")
            self.assertTrue((1, 2, 3, 'n'))
            self.assertTrue([1, 2, 3, 'n'])


    # NOTES

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add '

* I go back to the terminal_ that is running the tests

:ref:`the empty list is False and a list with things is True<is_a_list_falsy_or_truthy>`. I can see a pattern.

-----

*********************************************************************************
is_a_set_falsy_or_truthy
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add an :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_true` to test if a set_ should be grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 23
  :emphasize-lines: 4

          self.assertTrue("a string with things")
          self.assertTrue((1, 2, 3, 'n'))
          self.assertTrue([1, 2, 3, 'n'])
          self.assertTrue(set())


  # NOTES

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: set() is not true

:ref:`the empty set is NOT True<is_a_set_falsy_or_truthy>`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the :ref:`method<what is a method?>`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 1

            self.assertFalse(set())

  the test passes.

* I add a comment

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 9

    # NOTES
    # a list with things is True
    # a tuple with things is True
    # a string with things is True
    # positive and negative numbers are True
    # True is True
    # True is not false
    # True is a boolean
    # the empty set is False
    # the empty list is False
    # the empty tuple is False
    # the empty string is False
    # 0 is False
    # None is False
    # False is False
    # False is not true
    # False is a boolean

* I move the :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_false`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 10

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(None)
            self.assertFalse(0)
            self.assertFalse(0.0)
            self.assertFalse(str())
            self.assertFalse(tuple())
            self.assertFalse(list())
            self.assertFalse(set())

        def test_what_is_true(self):

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_false` to test if a set_ with things should be grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 5

            self.assertFalse(str())
            self.assertFalse(tuple())
            self.assertFalse(list())
            self.assertFalse(set())
            self.assertFalse({1, 2, 3, 'n'})

        def test_what_is_true(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: {1, 2, 3, 'n'} is not false

  :ref:`a set with things is NOT False<is_a_set_falsy_or_truthy>`

* I change the :ref:`method<what is a method?>`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 1

            self.assertTrue({1, 2, 3, 'n'})

  the test passes.

* I add a comment

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 2

    # NOTES
    # a set with things is True
    # a list with things is True
    # a tuple with things is True
    # a string with things is True
    # positive and negative numbers are True
    # True is True
    # True is not false
    # True is a boolean
    # the empty set is False
    # the empty list is False
    # the empty tuple is False
    # the empty string is False
    # 0 is False
    # None is False
    # False is False
    # False is not true
    # False is a boolean

* I move the :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_true`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 15

            self.assertFalse(tuple())
            self.assertFalse(list())
            self.assertFalse(set())

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)
            self.assertTrue(-1)
            self.assertTrue(1)
            self.assertTrue(-0.1)
            self.assertTrue(0.1)
            self.assertTrue("a string with things")
            self.assertTrue((1, 2, 3, 'n'))
            self.assertTrue([1, 2, 3, 'n'])
            self.assertTrue({1, 2, 3, 'n'})


    # NOTES

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add '

* I go back to the terminal_ that is running the tests

:ref:`the empty set is False and a set with things is True<is_a_set_falsy_or_truthy>`

----

*********************************************************************************
is_a_dictionary_falsy_or_truthy
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add an :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_true` to test if a :ref:`dictionary<what is a dictionary?>` should be grouped as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 17
  :emphasize-lines: 12

      def test_what_is_true(self):
          self.assertIsInstance(True, bool)
          self.assertTrue(True)
          self.assertTrue(-1)
          self.assertTrue(1)
          self.assertTrue(-0.1)
          self.assertTrue(0.1)
          self.assertTrue("a string with things")
          self.assertTrue((1, 2, 3, 'n'))
          self.assertTrue([1, 2, 3, 'n'])
          self.assertTrue({1, 2, 3, 'n'})
          self.assertTrue(dict())


  # NOTES

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: {} is not true

:ref:`the empty dictionary is NOT True<is_a_dictionary_falsy_or_truthy>`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change assertTrue_ to assertFalse_

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 1

            self.assertFalse(dict())

  the test passes.

* I add a comment

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 10

    # NOTES
    # a set with things is True
    # a list with things is True
    # a tuple with things is True
    # a string with things is True
    # positive and negative numbers are True
    # True is True
    # True is not false
    # True is a boolean
    # the empty dictionary is False
    # the empty set is False
    # the empty list is False
    # the empty tuple is False
    # the empty string is False
    # 0 is False
    # None is False
    # False is False
    # False is not true
    # False is a boolean

* I move the :ref:`assertion<what is an assertion?>` to the :ref:`test_what_is_false method<test_what_is_false>`



  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 11

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(None)
            self.assertFalse(0)
            self.assertFalse(0.0)
            self.assertFalse(str())
            self.assertFalse(tuple())
            self.assertFalse(list())
            self.assertFalse(set())
            self.assertFalse(dict())

        def test_what_is_true(self):

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another :ref:`assertion<what is an assertion?>` to test if a :ref:`dictionary<what is a dictionary?>` with things is also False_

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 4

            self.assertFalse(list())
            self.assertFalse(set())
            self.assertFalse(dict())
            self.assertFalse({'key': 'value'})

        def test_what_is_true(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: {'key': 'value'} is not false

  :ref:`a dictionary with things is NOT False<is_a_dictionary_falsy_or_truthy>`

* I change assertFalse_ to assertTrue_

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 1

            self.assertTrue({'key': 'value'})

  the test passes.

* I add the last comment

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 2

    # NOTES
    # a dictionary with things is True
    # a set with things is True
    # a list with things is True
    # a tuple with things is True
    # a string with things is True
    # positive and negative numbers are True
    # True is True
    # True is not false
    # True is a boolean
    # the empty dictionary is False
    # the empty set is False
    # the empty list is False
    # the empty tuple is False
    # the empty string is False
    # 0 is False
    # None is False
    # False is False
    # False is not true
    # False is a boolean


    # Exceptions seen
    # AssertionError

* I move the :ref:`assertion<what is an assertion?>` to the :ref:`test_what_is_true method<test_what_is_true>`



  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 24

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(None)
            self.assertFalse(0)
            self.assertFalse(0.0)
            self.assertFalse(str())
            self.assertFalse(tuple())
            self.assertFalse(list())
            self.assertFalse(set())
            self.assertFalse(dict())

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)
            self.assertTrue(-1)
            self.assertTrue(1)
            self.assertTrue(-0.1)
            self.assertTrue(0.1)
            self.assertTrue("a string with things")
            self.assertTrue((1, 2, 3, 'n'))
            self.assertTrue([1, 2, 3, 'n'])
            self.assertTrue({1, 2, 3, 'n'})
            self.assertTrue({'key': 'value'})


    # NOTES

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add '

* I go back to the terminal_ that is running the tests

:ref:`the empty dictionary is False, and a dictionary with things is True<is_a_dictionary_falsy_or_truthy>`

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

  I am back in the ``pumping_python`` directory_

----

*********************************************************************************
review
*********************************************************************************

From the tests I know that in Python_

* an empty container (strings_, tuples_, :ref:`lists<what is a list?>`, sets_, :ref:`dictionaries<what is a dictionary?>`) is False_
* ``0`` is False_
* :reF:`None<what is None?>` is False_
* False_ is not True_
* a container with things is True_
* positive and negative numbers are True_
* True_ is not False_
* True_ and False_ are booleans_

these things come in handy when I want :ref:`programs to make decisions<if statements>`, because they can choose what to do based on if the :ref:`data<data structures>` is False_ (``0``, empty or :ref:`None<what is None?>` ) or is True_ (positive and negative numbers or has something in it).

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

* :ref:`how to make a Python test driven development environment manually<how to make a Python test driven development environment>`
* :ref:`what causes AssertionError?`
* :ref:`how to make functions<what is a function?>`
* :ref:`what causes AttributeError<what causes AttributeError?>`
* :ref:`how to pass values from tests to functions<telephone>`
* :ref:`what None is<what is None?>`
* :ref:`what is True and False in Python<what are booleans?>`

:ref:`Would you like to test the truth table?<truth table>` It will help you understand writing programs_ that make decisions based on :ref:`conditions<if statements>`

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