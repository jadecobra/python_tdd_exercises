.. meta::
  :description: Master Python's truthiness and falsiness rules through Test Driven Development (TDD). This step-by-step tutorial uses unittest.assertTrue and assertFalse to explore why 0, 0.0, None, and empty collections (strings, lists, tuples, sets, and dicts) are False, while non-zero numbers and populated collections are True. Includes instructions for setting up a Python project with uv and automating tests with pytest-watcher.
  :keywords: Jacob Itegboje, Python booleans for beginners, Python truthiness and falsiness, what is False in Python, Python unittest assertTrue, Python unittest assertFalse, TDD Red Green Refactor tutorial, Python bool type explained, is empty list True or False, is 0.0 False in Python, is None False or True, testing Python data structures, python uv init, pytest-watcher tutorial, boolean logic in programming, truthy and falsy values list, python empty string boolean, python empty dict truthiness, python zero-based indexing, python unit testing tutorial

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
* :ref:`Is None False or True?<should I group None as False or True?>`
* :ref:`Is an integer False or True?<should I group an integer as False or True?>`
* :ref:`Is a float False or True?<should I group a float as False or True?>`
* :ref:`Is a string False or True?<should I group a string as False or True?>`
* :ref:`Is a tuple False or True?<should I group a tuple as False or True?>`
* :ref:`Is a list False or True?<should I group a list as False or True?>`
* :ref:`Is a set False or True?<should I group a set as False or True?>`
* :ref:`Is a dictionary False or True?<should I group a dictionary as False or True?>`

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

I change ``test_failure`` to :ref:`test_what_is_false`, then use the :ref:`assertNotIsInstance method<another way to test if something is NOT an instance of a class>` I learned from :ref:`everything is an object` to check if False_ is :ref:`an instance (a copy)<how to test if something is an instance of a class>` of the :ref:`bool class<what are booleans?>`

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

  I already know this from :ref:`testing None<what is None?>`.

* I use the :ref:`assertIsNot method<another way to test if something is NOT the same object as False>` like I did in :ref:`test_assertion_error_w_false`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 4

        def test_what_is_false(self):
            # self.assertNotIsInstance(False, bool)
            self.assertIsInstance(False, bool)
            self.assertIsNot(False, False)


    # NOTES

  the terminal_ is my friend, and shows :ref:`ASsertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: unexpectedly identical: False

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

=================================================================================
how to test if something should be grouped as False or True
=================================================================================

----

I can test if I should group an :ref:`object<what is a class?>` as :ref:`False<test_what_is_false>` with the `bool built-in function`_ from `The Python Standard Library`_. It checks if Python_ groups the thing in parentheses as :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>`.

* I add an :ref:`assertion<what is an assertion?>` with a call to bool_ in

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

  because this is what happens when ``self.assertEqual(bool(False), True)`` runs

  .. code-block:: python

    self.assertEqual(bool(False), True)
    self.assertEqual(False      , True)

  which raises :ref:`AssertionError<what causes AssertionError?>` since :ref:`False<test_what_is_false>` which is the result of ``bool(False)`` is not equal to :ref:`True<test_what_is_true>`.

* I add a comment

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 2

    # NOTES
    # False is NOT equal to True
    # False is a boolean

    # Exceptions seen
    # AssertionError

* I change the expectation of the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

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

  the test passes because ``bool(False) == False``.

----

=================================================================================
another way to test if something should be grouped as False
=================================================================================

----

The `unittest.TestCase class`_ has a :ref:`method<what is a method?>` I can also use to test if the result of calling the :ref:`bool<how to test if something should be grouped as False or True>` with the :ref:`object<what is a class?>` is :ref:`False<test_what_is_false>` - assertFalse_, it was in :ref:`the first failing test<test_failure>`

  .. code-block:: python

    self.assertFalse(True)

  which checks is the same as ``self.assertEqual(bool(True), False)``

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

  because this is what happens when ``self.assertEqual(bool(False), True)`` runs

  .. code-block:: python

    self.assertFalse(bool(True))
    self.assertFalse(True)

  which raises :ref:`AssertionError<what causes AssertionError?>` since

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

* I add a test for True_

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 4-5

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)

        def test_what_is_true(self):
            self.assertNotIsInstance(True, bool)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

      AssertionError: True is an instance of <class 'bool'>

* I add a comment

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

    # NOTES
    # True is a boolean
    # False is a boolean


    # Exceptions seen
    # AssertionError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the `assert method`_

.. code-block:: python
  :lineno-start: 9
  :emphasize-lines: 2

      def test_what_is_true(self):
          self.assertIsInstance(True, bool)


  # NOTES

the test passes. :ref:`True is a boolean<test_what_is_true>`

----

*********************************************************************************
:yellow:`REFACTOR`: make it better
*********************************************************************************

* I add a failing :ref:`assertion<what is an assertion?>`, to the :ref:`test_what_is_true method<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 3

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(False)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

* I add a comment

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 3

    # NOTES
    # True is a boolean
    # False is not true
    # False is a boolean


    # Exceptions seen
    # AssertionError

* I change assertTrue_ to assertFalse_

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 3

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertFalse(False)


    # NOTES

  the test passes.

* I add a comment

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 3

    # NOTES
    # True is a boolean
    # False is False
    # False is not true
    # False is a boolean


    # Exceptions seen

* I move the :ref:`assertion<what is an assertion?>` from :ref:`test_what_is_true` to the :ref:`test_what_is_false method<test_what_is_false>`

  .. tip:: In `Visual Studio Code`_ I can move lines I select or where the cursor is, with :kbd:`alt/option+Up` on the keyboard to move lines up or :kbd:`alt/option+Down` to move lines down

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 5

    class TestBooleans(unittest.TestCase):

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)


    # NOTES

* I add a failing :ref:`assertion<what is an assertion?>`, to the :ref:`test_what_is_false method<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 4

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(True)

        def test_what_is_true(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

* I add a comment

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 2

    # NOTES
    # True is not false
    # True is a boolean
    # False is False
    # False is not true
    # False is a boolean


    # Exceptions seen

* I change assertFalse_ to assertTrue_

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 4

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertTrue(True)

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)


    # NOTES

  the test passes.

* I add a comment

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 2


    # NOTES
    # True is True
    # True is not false
    # True is a boolean
    # False is False
    # False is not true
    # False is a boolean


    # Exceptions seen
    # AssertionError

* I move the :ref:`assertion<what is an assertion?>` from :ref:`test_what_is_false` to the :ref:`test_what_is_true method<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 7

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)


    # NOTES

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add '


All of these are still statements from the :ref:`AssertionError<what causes AssertionError?>` and :ref:`None<what is None?>` chapters.

Next up, I test the other :ref:`Python basic data structures<data structures>` to see which ones are False_ or True_. What do you think?

* :ref:`should I group None as False or True?`
* :ref:`should I group an integer as False or True?`
* :ref:`should I group a float as False or True?`
* :ref:`should I group a string as False or True?`
* :ref:`should I group a tuple as False or True?`
* :ref:`should I group a list as False or True?`
* :ref:`should I group a set as False or True?`
* :ref:`should I group a dictionary as False or True?`

----

*****************************************************************************************
should I group None as False or True?
*****************************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests
I add an :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_true` to test if :ref:`None<what is None?>` is True_

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 4

      def test_what_is_true(self):
          self.assertIsInstance(True, bool)
          self.assertTrue(True)
          self.assertTrue(None)


  # NOTES

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: None is not true

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the :ref:`method<what is a method?>`

.. code-block:: python
  :lineno-start: 13
  :emphasize-lines: 1

          self.assertFalse(None)

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a comment

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 5


    # NOTES
    # True is True
    # True is not false
    # True is a boolean
    # None is False
    # False is False
    # False is not true
    # False is a boolean


    # Exceptions seen

* I move the :ref:`assertion<what is an assertion?>` from :ref:`test_what_is_true` to :ref:`test_what_is_false`

  .. tip:: In `Visual Studio Code`_ I can move lines I select or where the cursor is, with :kbd:`alt/option+Up` on the keyboard to move lines up or :kbd:`alt/option+Down` to move lines down

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 4

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(None)

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)


    # NOTES

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add '

* I go back to the terminal_ that is running the tests

:ref:`None is False<should I group None as False or True?>` and I learned from :ref:`the AssertionError chapter<what causes AssertionError?>` that :ref:`False is not None<test_assertion_error_w_false>`

----

*********************************************************************************
should I group an integer as False or True?
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a failing :ref:`assertion<what is an assertion?>` to the :ref:`test_what_is_false method<test_what_is_false>` to see if an integer_ (a whole number) is False_

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 5

      def test_what_is_false(self):
          self.assertIsInstance(False, bool)
          self.assertFalse(False)
          self.assertFalse(None)
          self.assertFalse(-1)

      def test_what_is_true(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: -1 is not false

I use ``-1`` for all the integers_ (whole numbers) that are smaller than ``0``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the :ref:`method<what is a method?>`

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 1

          self.assertTrue(-1)

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a comment

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 2

    # NOTES
    # negative integers are True
    # True is True
    # True is not false
    # True is a boolean
    # None is False
    # False is False
    # False is not true
    # False is a boolean

* I move the :ref:`assertion<what is an assertion?>` from :ref:`test_what_is_false` to :ref:`test_what_is_true`

  .. tip:: In `Visual Studio Code`_ I can move lines I select or where the cursor is, with :kbd:`alt/option+Up` on the keyboard to move lines up or :kbd:`alt/option+Down` to move lines down

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 9

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(None)

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)
            self.assertTrue(-1)


    # NOTES

  :ref:`negative integers are True in Python<should I group an integer as False or True?>`

* I add a new failing line to :ref:`test_what_is_true` to see if ``0`` is True_

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 5

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)
            self.assertTrue(-1)
            self.assertTrue(0)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 0 is not true

* I change the :ref:`method<what is a method?>` to assertFalse_

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 1

            self.assertFalse(0)

  the test passes.

* I add a comment

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 6

    # NOTES
    # negative integers are True
    # True is True
    # True is not false
    # True is a boolean
    # 0 is False
    # None is False
    # False is False
    # False is not true
    # False is a boolean

* I move the :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_false`

  .. tip:: In `Visual Studio Code`_ I can move lines I select or where the cursor is, with :kbd:`alt/option+Up` on the keyboard to move lines up or :kbd:`alt/option+Down` to move lines down

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 5

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(None)
            self.assertFalse(0)

        def test_what_is_true(self):

  :ref:`0 is False in Python<should I group an integer as False or True?>`

* I add another failing line to :ref:`test_what_is_false` to see if ``1`` is False

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 6

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(None)
            self.assertFalse(0)
            self.assertFalse(1)

        def test_what_is_true(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 1 is not false

  I use ``1`` for all the integers_ (whole numbers) that are bigger than ``0``

* I change the :ref:`method<what is a method?>`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 1

            self.assertTrue(1)

  the test passes.

* I add to the comment about negative integers

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 2

    # NOTES
    # positive and negative integers are True
    # True is True
    # True is not false
    # True is a boolean
    # 0 is False
    # None is False
    # False is False
    # False is not true
    # False is a boolean

* I move the :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_true`

  .. tip:: In `Visual Studio Code`_ I can move lines I select or where the cursor is, with :kbd:`alt/option+Up` on the keyboard to move lines up or :kbd:`alt/option+Down` to move lines down

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 11

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(None)
            self.assertFalse(0)

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)
            self.assertTrue(-1)
            self.assertTrue(1)


    # NOTES

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add '

* I go back to the terminal_ that is running the tests

:ref:`in Python 0 is False, and positive and negative integers are True<should I group an integer as False or True?>`

-----

*********************************************************************************
should I group a float as False or True?
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add an :ref:`assertion<what is an assertion?>` to test if floats_ (binary floating point decimal numbers) are False_ in :ref:`test_what_is_false`

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 6

      def test_what_is_false(self):
          self.assertIsInstance(False, bool)
          self.assertFalse(False)
          self.assertFalse(None)
          self.assertFalse(0)
          self.assertFalse(-0.1)

      def test_what_is_true(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: -0.1 is not false

I use ``-0.1`` for all the `binary floating point numbers`_ that are smaller than ``0.0``.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the :ref:`method<what is a method?>`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 1

            self.assertTrue(-0.1)

  the test passes.

* I add comments

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 2

    # NOTES
    # negative floats are True
    # positive and negative integers are True
    # True is True
    # True is not false
    # True is a boolean
    # 0 is False
    # None is False
    # False is False
    # False is not true
    # False is a boolean

* I move the :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_true`

  .. tip:: In `Visual Studio Code`_ I can move lines I select or where the cursor is, with :kbd:`alt/option+Up` on the keyboard to move lines up or :kbd:`alt/option+Down` to move lines down

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 9

            self.assertFalse(None)
            self.assertFalse(0)

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)
            self.assertTrue(-1)
            self.assertTrue(1)
            self.assertTrue(-0.1)


    # NOTES

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add '

* I go back to the terminal_ that is running the tests

:ref:`Negative floats are True in Python<should I group a float as False or True?>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another failing line to :ref:`test_what_is_true` to see if ``0.0`` is True_

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 7

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)
            self.assertTrue(-1)
            self.assertTrue(1)
            self.assertTrue(-0.1)
            self.assertTrue(0.0)


    # NOTES

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 0.0 is not true

* I change the :ref:`method<what is a method?>`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 1

            self.assertFalse(0.0)

  the test passes.

* I add a comment

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 7

    # NOTES
    # negative floats are True
    # positive and negative integers are True
    # True is True
    # True is not false
    # True is a boolean
    # 0.0 is False
    # 0 is False
    # None is False
    # False is False
    # False is not true
    # False is a boolean

* I move the :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_false`

  .. tip:: In `Visual Studio Code`_ I can move lines I select or where the cursor is, with :kbd:`alt/option+Up` on the keyboard to move lines up or :kbd:`alt/option+Down` to move lines down

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 6

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(None)
            self.assertFalse(0)
            self.assertFalse(0.0)

        def test_what_is_true(self):

  :ref:`0.0 is False in Python<should I group a float as False or True?>`

* I add another :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_false` to see if ``0.1`` is False_

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 7

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(None)
            self.assertFalse(0)
            self.assertFalse(0.0)
            self.assertFalse(0.1)

        def test_what_is_true(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 0.1 is not false

  I use ``0.1`` for all the `binary floating point numbers`_ that are bigger than ``0.0``.

* I change the :ref:`method<what is a method?>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 1

            self.assertTrue(0.1)

  the test passes.

* I add to the comment about negative floats

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 2

    # NOTES
    # positive and negative floats are True
    # positive and negative integers are True
    # True is True
    # True is not false
    # True is a boolean
    # 0.0 is False
    # 0 is False
    # None is False
    # False is False
    # False is not true
    # False is a boolean

* I move the :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_true`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 10

            self.assertFalse(0)
            self.assertFalse(0.0)

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)
            self.assertTrue(-1)
            self.assertTrue(1)
            self.assertTrue(-0.1)
            self.assertTrue(0.1)


    # NOTES

* I make the new comments simpler because floats_ and integers_ are numbers and ``0.0`` is the same as ``0`` even though they are different types_

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 2, 6

    # NOTES
    # positive and negative numbers are True
    # True is True
    # True is not false
    # True is a boolean
    # 0 is False
    # None is False
    # False is False
    # False is not true
    # False is a boolean

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add '

* I go back to the terminal_ that is running the tests

:ref:`in Python, 0.0 is False and positive and negative floats are True<should I group a float as False or True?>`

-----

*********************************************************************************
should I group a string as False or True?
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a failing :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_true` to test if a string_ (anything in :ref:`quotes`) is True_

.. code-block:: python
  :lineno-start: 13
  :emphasize-lines: 8

      def test_what_is_true(self):
          self.assertIsInstance(True, bool)
          self.assertTrue(True)
          self.assertTrue(-1)
          self.assertTrue(1)
          self.assertTrue(-0.1)
          self.assertTrue(0.1)
          self.assertTrue(str())


  # NOTES

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: '' is not true

:ref:`the empty string ('') is not True<should I group a string as False or True?>`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the :ref:`method<what is a method?>`

.. code-block:: python
  :lineno-start: 20
  :emphasize-lines: 1

          self.assertFalse(str())

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a comment

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 6

    # NOTES
    # positive and negative numbers are True
    # True is True
    # True is not false
    # True is a boolean
    # the empty string is False
    # 0 is False
    # None is False
    # False is False
    # False is not true
    # False is a boolean

* I move the :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_false`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 7

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(None)
            self.assertFalse(0)
            self.assertFalse(0.0)
            self.assertFalse(str())

        def test_what_is_true(self):

* I add a failing :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_false`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3

            self.assertFalse(0.0)
            self.assertFalse(str())
            self.assertFalse("text")

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 'text' is not false

* I change the :ref:`method<what is a method?>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 1

            self.assertTrue("text")

  the test passes.

* I add a comment

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 2

    # NOTES
    # a string with things is True
    # positive and negative numbers are True
    # True is True
    # True is not false
    # True is a boolean
    # the empty string is False
    # 0 is False
    # None is False
    # False is False
    # False is not true
    # False is a boolean

* I move the :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_true`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 11

            self.assertFalse(0.0)
            self.assertFalse(str())

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)
            self.assertTrue(-1)
            self.assertTrue(1)
            self.assertTrue(-0.1)
            self.assertTrue(0.1)
            self.assertTrue("text")


    # NOTES

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add '

* I go back to the terminal_ that is running the tests

:ref:`in Python, the empty string is False and a string with things is True<should I group a string as False or True?>`

----

*********************************************************************************
should I group a tuple as False or True?
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add an :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_true` to see if a tuple_ (anything in parentheses (``()``) separated by commas) is True_

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
          self.assertTrue("text")
          self.assertTrue(tuple())


  # NOTES

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: () is not true

:ref:`the empty tuple is not True<should I group a tuple as False or True?>`

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

* I add another :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_false` to see if a tuple_ with things is False_

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

  :ref:`a tuple with things is NOT False<should I group a tuple as False or True?>`

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

  .. tip:: In `Visual Studio Code`_ I can move lines I select or where the cursor is, with :kbd:`alt/option+Up` on the keyboard to move lines up or :kbd:`alt/option+Down` to move lines down

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
            self.assertTrue("text")
            self.assertTrue((1, 2, 3, 'n'))


    # NOTES

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add '

* I go back to the terminal_ that is running the tests

:ref:`in Python, the empty tuple is False and a tuple with things is True<should I group a tuple as False or True?>`

----

*********************************************************************************
should I group a list as False or True?
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add an :ref:`assertion<what is an assertion?>` to test if a :ref:`list<lists>` (anything in square brackets (``[]``)) is True_

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
          self.assertTrue("text")
          self.assertTrue((1, 2, 3, 'n'))
          self.assertTrue(list())


  # NOTES

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: [] is not true

:ref:`the empty list is NOT True<should I group a list as False or True?>`

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

* I add another :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_false` to see if a :ref:`list<lists>` with things is False_

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
            self.assertTrue("text")
            self.assertTrue((1, 2, 3, 'n'))
            self.assertTrue([1, 2, 3, 'n'])


    # NOTES

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add '

* I go back to the terminal_ that is running the tests

:ref:`in Python, the empty list is False and a list with things is True<should I group a list as False or True?>`. I can see a pattern.

-----

*********************************************************************************
should I group a set as False or True?
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add an :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_true` to see if a set_ is True_

.. code-block:: python
  :lineno-start: 23
  :emphasize-lines: 4

          self.assertTrue("text")
          self.assertTrue((1, 2, 3, 'n'))
          self.assertTrue([1, 2, 3, 'n'])
          self.assertTrue(set())


  # NOTES

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: set() is not true

:ref:`the empty set is NOT True<should I group a set as False or True?>`

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

* I add another :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_false` to see if a set_ with things is False_

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

  :ref:`a set with things is NOT False<should I group a set as False or True?>`

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
            self.assertTrue("text")
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

:ref:`in Python, the empty set is False and a set with things is True<should I group a set as False or True?>`

----

*********************************************************************************
should I group a dictionary as False or True?
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add an :ref:`assertion<what is an assertion?>` to :ref:`test_what_is_true` to test if a :ref:`dictionary<what is a dictionary?>` is True_

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
          self.assertTrue("text")
          self.assertTrue((1, 2, 3, 'n'))
          self.assertTrue([1, 2, 3, 'n'])
          self.assertTrue({1, 2, 3, 'n'})
          self.assertTrue(dict())


  # NOTES

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: {} is not true

:ref:`the empty dictionary is NOT True<should I group a dictionary as False or True?>`

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

  .. tip:: In `Visual Studio Code`_ I can move lines I select or where the cursor is, with :kbd:`alt/option+Up` on the keyboard to move lines up or :kbd:`alt/option+Down` to move lines down

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

  :ref:`a dictionary with things is NOT False<should I group a dictionary as False or True?>`

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

  .. tip:: In `Visual Studio Code`_ I can move lines I select or where the cursor is, with :kbd:`alt/option+Up` on the keyboard to move lines up or :kbd:`alt/option+Down` to move lines down

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
            self.assertTrue("text")
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

:ref:`in Python, the empty dictionary is False, and a dictionary with things is True<should I group a dictionary as False or True?>`

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