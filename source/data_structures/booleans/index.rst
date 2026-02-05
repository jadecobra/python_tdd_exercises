.. meta::
  :description: Learn how Python's boolean data type, operators (and, or, not), and truthiness work in conditional statements to control program_ flow. Watch the tutorial!
  :keywords: Jacob Itegboje, python boolean tutorial for beginners, python boolean operators and or not, python if statement with boolean, python truthiness and falsiness explained, what is boolean in python with example, how to use bool() in python, python boolean return function, common python boolean mistakes, python boolean best practices

.. include:: ../../links.rst

.. _booleans: bool_

#################################################################################
what are booleans?
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/6r3QcYN0wxQ?si=cQaK63rwX3f9PGX6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

There are only 2 booleans_ - True_ and False_. I can use the `assertFalse`_ and `assertTrue`_ :ref:`methods<what is a function?>` to test which of the :ref:`basic data structures<data structures>` seen so far - integers_, floats_, strings_, tuples_, :ref:`lists`, sets_ and :ref:`dictionaries`, are True_ or False_ in Python_

*********************************************************************************
preview
*********************************************************************************

These are the tests I have by the end of the chapter

.. literalinclude:: ../../code/tests/booleans/test_booleans.py
  :language: python
  :linenos:

*********************************************************************************
questions about Booleans
*********************************************************************************

Here are questions you can answer after going through this chapter

* :ref:`what is False?<test_what_is_false>`
* :ref:`what is True?<test_what_is_true>`
* :ref:`Is None False or True?<is None False or True?>`
* :ref:`Is an integer False or True?<is an integer False or True?>`
* :ref:`Is a float False or True?<is a float False or True?>`
* :ref:`Is a string False or True?<is a string False or True?>`
* :ref:`Is a tuple False or True?<is a tuple False or True?>`
* :ref:`Is a list False or True?<is a list False or True?>`
* :ref:`Is a set False or True?<is a set False or True?>`
* :ref:`Is a dictionary False or True?<is a dictionary False or True?>`

----

*********************************************************************************
start the project
*********************************************************************************

* I name this project ``booleans``
* I open a terminal_
* I make a directory_ for the project

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir booleans

  the terminal_ goes back to the command line

* I change directory_ to the project

  .. code-block:: shell
    :emphasize-lines: 1

    cd booleans

  the terminal_ shows I am in the ``booleans`` folder_

  .. code-block:: shell

    .../pumping_python/booleans

* I make a directory_ for the source code

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir src

  the terminal_ goes back to the command line

* I make a :ref:`Python file<what is a module?>` to hold the source code in the ``src`` directory_

  .. code-block:: shell
    :emphasize-lines: 1

    touch src/booleans.py

  .. NOTE::

    on Windows_ without `Windows Subsystem for Linux`_ use ``New-Item src/booleans.py`` instead of ``touch src/booleans.py``

    .. code-block:: shell
      :emphasize-lines: 1

      New-Item src/booleans.py

  the terminal_ goes back to the command line

* I `make a directory`_ for the tests

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir tests

  the terminal_ goes back to the command line

* I make the ``tests`` directory_ a `Python package`_

  .. DANGER:: use 2 underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``

  .. code-block:: shell
    :emphasize-lines: 1

    touch tests/__init__.py

  .. NOTE::

    on Windows_ without `Windows Subsystem for Linux`_ use ``New-Item tests/__init__.py`` instead of ``touch tests/__init__.py``

    .. code-block:: shell
      :emphasize-lines: 1

      New-Item tests/__init__.py

  the terminal_ goes back to the command line

* I make a :ref:`Python file<what is a module?>` for the tests in the ``tests`` directory_

  .. code-block:: shell
    :emphasize-lines: 1

    touch tests/test_booleans.py

  .. NOTE::

    on Windows_ without `Windows Subsystem for Linux`_ use ``New-Item tests/test_booleans.py`` instead of ``touch tests/test_booleans.py``

    .. code-block:: shell
      :emphasize-lines: 1

      New-Item tests/test_booleans.py

  the terminal_ goes back to the command line

* I open ``test_booleans.py`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_

  .. TIP::

    I can use the terminal_ to open a file_ in the `Integrated Development Environment (IDE)`_ by typing the name of the program and the name of the file_. That means when I type this in the terminal_

    .. code-block:: shell
      :emphasize-lines: 1

      code tests/test_booleans.py

    `Visual Studio Code`_ opens ``test_booleans.py`` in the :ref:`editor<2 editors>`

* I add :ref:`the first failing test<test_failure>` to ``test_booleans.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-7

    import unittest


    class TestBooleans(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

* I make a requirements file_ for the `Python packages`_ I need, in the terminal_

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest" > requirements.txt

  the terminal_ goes back to the command line

* I add `pytest-watcher`_ to the file_

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest-watcher" >> requirements.txt

  the terminal_ goes back to the command line

* I setup the project with uv_

  .. code-block:: python
    :emphasize-lines: 1

    uv init

  the terminal_ shows

  .. code-block:: shell

    Initialized project `booleans`

  then goes back to the command line

* I remove ``main.py`` from the project

  .. code-block:: python
    :emphasize-lines: 1

    rm main.py

  the terminal_ goes back to the command line

* I install the Python packages listed in the requirements file_

  .. code-block:: python
    :emphasize-lines: 1

    uv add --requirement requirements.txt

  the terminal shows it installed the `Python packages`_

* I run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: python
    :emphasize-lines: 8, 10


    ================================ FAILURES ================================
    _______________________ TestBooleans.test_failure ________________________

    self = <tests.test_booleans.TestBooleans testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_booleans.py:7: AssertionError
    ======================== short test summary info =========================
    FAILED tests/test_booleans.py::TestBooleans::test_failure - AssertionError: True is not false
    =========================== 1 failed in X.YZs ============================

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option/command` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_booleans.py:7`` to put the cursor on line 7 in the :ref:`editor<2 editors>`

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

  the test passes

----

*********************************************************************************
test_what_is_false
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I change ``test_failure`` to :ref:`test_what_is_false`, then use the `assertNotIsInstance method`_ from :ref:`testing None<what is None?>` to check if False_ is a child/instance of the `bool class`_, I think this will fail

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    import unittest


    class TestBooleans(unittest.TestCase):

        def test_what_is_false(self):
            self.assertNotIsInstance(False, bool)


    # Exceptions seen
    # AssertionError

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is an instance of <class 'bool'>

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change assertNotIsInstance_ to assertIsInstance_

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertIsInstance(False, bool)

  the test passes

* I add a comment

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7-8

    class TestBooleans(unittest.TestCase):

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)


    # NOTES
    # False is a boolean


    # Exceptions seen
    # AssertionError

  so far this is something I already know from :ref:`testing None<what is None?>`

:ref:`False is a boolean<test_what_is_false>`

----

*********************************************************************************
test_what_is_true
*********************************************************************************

I do the same thing with True_

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add another failing test

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 4-5

      def test_what_is_false(self):
          self.assertIsInstance(False, bool)

      def test_what_is_true(self):
          self.assertNotIsInstance(True, bool)


  # NOTES

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

    AssertionError: True is an instance of <class 'bool'>

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the `assert method`_

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)


    # NOTES

  the test passes

* I add another comment

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

    # NOTES
    # True is a boolean
    # False is a boolean


    # Exceptions seen

:ref:`True is a boolean<test_what_is_true>`

----

*********************************************************************************
:yellow:`REFACTOR`: make it better
*********************************************************************************

* I add a failing line to the :ref:`test_what_is_true method<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 3

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(False)


    # NOTES

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

* I change assertTrue_ to assertFalse_

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 3

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertFalse(False)


    # NOTES

  the test passes

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

* I move the line from :ref:`test_what_is_true` to the :ref:`test_what_is_false method<test_what_is_false>`

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

  .. TIP:: If you are using `Visual Studio Code`_ you can use :kbd:`alt` (Windows_/Linux_) or :kbd:`option` (MacOS_) with the up/down arrows on the keyboard to move a line up or down

* I add a comment

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 3

    # NOTES
    # True is a boolean
    # False is false
    # False is not true
    # False is a boolean


    # Exceptions seen

* I add a failing line to the :ref:`test_what_is_false method<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 4

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(True)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

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

  the test passes

* I add a comment

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 2

    # NOTES
    # True is not false
    # True is a boolean
    # False is false
    # False is not true
    # False is a boolean


    # Exceptions seen

* I move the line from :ref:`test_what_is_false` to the :ref:`test_what_is_true method<test_what_is_true>`

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

* I add another comment

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 2


    # NOTES
    # True is true
    # True is not false
    # True is a boolean
    # False is false
    # False is not true
    # False is a boolean


    # Exceptions seen
    # AssertionError

All of these are still statements from the :ref:`AssertionError<what causes AssertionError?>` and :ref:`None<what is None?>` chapters.

Next up, I test the other :ref:`Python basic data structures<data structures>` to see which ones are False_ or True_.

* :ref:`is None False or True?`
* :ref:`is an integer False or True?`
* :ref:`is a float False or True?`
* :ref:`is a string False or True?`
* :ref:`is a tuple False or True?`
* :ref:`is a list False or True?`
* :ref:`is a set False or True?`
* :ref:`is a dictionary False or True?`

----

*****************************************************************************************
is None False or True?
*****************************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a line in :ref:`test_what_is_true` to test if :ref:`None<what is None?>` is True_

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 4

      def test_what_is_true(self):
          self.assertIsInstance(True, bool)
          self.assertTrue(True)
          self.assertTrue(None)

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: None is not true

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the :ref:`method<what is a function?>`

.. code-block:: python
  :lineno-start: 13
  :emphasize-lines: 1

          self.assertFalse(None)

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

I move the line from :ref:`test_what_is_true` to :ref:`test_what_is_false`

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

I add a comment

.. code-block:: python
  :lineno-start: 16
  :emphasize-lines: 5


  # NOTES
  # True is true
  # True is not false
  # True is a boolean
  # None is false
  # False is false
  # False is not true
  # False is a boolean


  # Exceptions seen

:ref:`None is False<is None False or True?>` and I learned from :ref:`the AssertionError chapter<what causes AssertionError?>` that :ref:`False is not None<test_assertion_error_w_false>`

----

*********************************************************************************
is an integer False or True?
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a failing line to the :ref:`test_what_is_false method<test_what_is_false>` to see if an integer_ (a whole number) is False_

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 5

      def test_what_is_false(self):
          self.assertIsInstance(False, bool)
          self.assertFalse(False)
          self.assertFalse(None)
          self.assertFalse(-1)

      def test_what_is_true(self):

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: -1 is not false

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the :ref:`method<what is a function?>`

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 1

          self.assertTrue(-1)

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I move the line from :ref:`test_what_is_false` to :ref:`test_what_is_true`

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

  I use ``-1`` for all the integers_ (whole numbers) that are smaller than ``0``. :ref:`Negative integers are True in Python<is an integer False or True?>`

* I add a new failing line to :ref:`test_what_is_true` to see if ``0`` is True_

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 5

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)
            self.assertTrue(-1)
            self.assertTrue(0)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 0 is not true

* I change the :ref:`method<what is a function?>` to assertFalse_

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 1

            self.assertFalse(0)

  the test passes

* I move the line to :ref:`test_what_is_false`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 5

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(None)
            self.assertFalse(0)

        def test_what_is_true(self):

  :ref:`0 is False in Python<is an integer False or True?>`

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

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 1 is not false

* I change the :ref:`method<what is a function?>`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 1

            self.assertTrue(1)

  the test passes

* I move the line to :ref:`test_what_is_true`

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

  I use ``1`` for all the integers_ (whole numbers) that are bigger than ``0``

* I add comments

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 2, 6

    # NOTES
    # positive and negative integers are true
    # True is true
    # True is not false
    # True is a boolean
    # 0 is false
    # None is false
    # False is false
    # False is not true
    # False is a boolean


    # Exceptions seen
    # AssertionError

:ref:`in Python 0 is False, and positive and negative integers are True<is an integer False or True?>`

-----

*********************************************************************************
is a float False or True?
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a line to test if floats_ (binary floating point decimal numbers) are False_ in :ref:`test_what_is_false`

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

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: -0.1 is not false

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the :ref:`method<what is a function?>`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 1

            self.assertTrue(-0.1)

  the test passes

* I move the line to :ref:`test_what_is_true`

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

  I use ``-0.1`` for all the binary floating point numbers that are smaller than ``0.0``.

:ref:`Negative floats are True in Python<is a float False or True?>`

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

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 0.0 is not true

  I change the :ref:`method<what is a function?>`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 1

            self.assertFalse(0.0)

  the test passes

* I move the line to :ref:`test_what_is_false`

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

  :ref:`0.0 is False in Python<is a float False or True?>`

* I add another line to :ref:`test_what_is_false` to see if ``0.1`` is False_ in Python_

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 3

            self.assertFalse(0)
            self.assertFalse(0.0)
            self.assertFalse(0.1)

        def test_what_is_true(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 0.1 is not false

* I change the :ref:`method<what is a function?>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 1

            self.assertTrue(0.1)

  the test passes

* I move the line to :ref:`test_what_is_true`

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

  I use ``0.1`` for all the binary floating point numbers that are bigger than ``0.0``.

* I add comments

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 2, 7

    # NOTES
    # positive and negative floats are true
    # positive and negative integers are true
    # True is true
    # True is not false
    # True is a boolean
    # 0.0 is false
    # 0 is false
    # None is false
    # False is false
    # False is not true
    # False is a boolean

* I make the new comments simpler because floats_ and integers_ are numbers and ``0.0`` is the same as ``0`` even though they are different types_

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 2, 6

    # NOTES
    # positive and negative numbers are true
    # True is true
    # True is not false
    # True is a boolean
    # 0 is false
    # None is false
    # False is false
    # False is not true
    # False is a boolean


    # Exceptions seen

:ref:`in Python, 0.0 is False and positive and negative floats are True<is a float False or True?>`

-----

*********************************************************************************
is a string False or True?
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a failing line to :ref:`test_what_is_true` to test if a string_ (anything in :ref:`quotes`) is True_

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

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: '' is not true

:ref:`the empty string ('') is not True<is a string False or True?>`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the :ref:`method<what is a function?>`

.. code-block:: python
  :lineno-start: 20
  :emphasize-lines: 1

          self.assertFalse(str())

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I move the line to :ref:`test_what_is_false`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 2

            self.assertFalse(0.0)
            self.assertFalse(str())

        def test_what_is_true(self):

  the empty string_ ('') is not False_

* I add a failing line to :ref:`test_what_is_false`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3

            self.assertFalse(0.0)
            self.assertFalse(str())
            self.assertFalse('text')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 'text' is not false

  I change the :ref:`method<what is a function?>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 1

            self.assertTrue('text')

  the test passes

* I move the line to :ref:`test_what_is_true`

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
            self.assertTrue('text')


    # NOTES

* I add comments

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 2, 7

    # NOTES
    # a string with things is true
    # positive and negative numbers are true
    # True is true
    # True is not false
    # True is a boolean
    # the empty string is false
    # 0 is false
    # None is false
    # False is false
    # False is not true
    # False is a boolean

:ref:`in Python, the empty string is False and a string with things is True<is a string False or True?>`

----

*********************************************************************************
is a tuple False or True?
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a line to :ref:`test_what_is_true` to see if a tuple_ (anything in parentheses (``()``) separated by commas, separated by commas) is True_

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
          self.assertTrue('text')
          self.assertTrue(tuple())


  # NOTES

The terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: () is not true

:ref:`the empty tuple is not True<is a tuple False or True?>`

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

  the test passes

* I move the line to :ref:`test_what_is_false`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3

            self.assertFalse(0.0)
            self.assertFalse(str())
            self.assertFalse(tuple())

        def test_what_is_true(self):

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another line to :ref:`test_what_is_false` to see if a tuple_ with things is False_

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 4

            self.assertFalse(0.0)
            self.assertFalse(str())
            self.assertFalse(tuple())
            self.assertFalse((1, 2, 3, 'n'))

        def test_what_is_true(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (1, 2, 3, 'n') is not false

  a tuple_ with things is NOT False_

* I change the :ref:`method<what is a function?>`

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 1

            self.assertTrue((1, 2, 3, 'n'))

  the test passes

* I move the line to :ref:`test_what_is_true`

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
            self.assertTrue('text')
            self.assertTrue((1, 2, 3, 'n'))


    # NOTES

  .. TIP:: If you are using `Visual Studio Code`_ you can use :kbd:`alt` (Windows_/Linux_) or :kbd:`option` (MacOS_) with the up/down arrows on the keyboard to move a line up or down

* I add comments

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 2, 8


    # NOTES
    # a tuple with things is true
    # a string with things is true
    # positive and negative numbers are true
    # True is true
    # True is not false
    # True is a boolean
    # the empty tuple is false
    # the empty string is false
    # 0 is false
    # None is false
    # False is false
    # False is not true
    # False is a boolean

:ref:`in Python, the empty tuple is False and a tuple with things is True<is a tuple False or True?>`

----

*********************************************************************************
is a list False or True?
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a line to test if a :ref:`list<lists>` (anything in square brackets (``[]``)) is True_

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
          self.assertTrue('text')
          self.assertTrue((1, 2, 3, 'n'))
          self.assertTrue(list())


  # NOTES

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: [] is not true

the empty :ref:`list<lists>` is NOT True_

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the :ref:`method<what is a function?>`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 1

            self.assertFalse(list())

  the test passes

* I move the line to :ref:`test_what_is_false`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 3

            self.assertFalse(str())
            self.assertFalse(tuple())
            self.assertFalse(list())

        def test_what_is_true(self):

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another line to :ref:`test_what_is_false` to see if a :ref:`list<lists>` with things is False_

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 4

            self.assertFalse(str())
            self.assertFalse(tuple())
            self.assertFalse(list())
            self.assertFalse([1, 2, 3, 'n'])

        def test_what_is_true(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: [1, 2, 3, 'n'] is not false

* I change the :ref:`method<what is a function?>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 1

            self.assertTrue([1, 2, 3, 'n'])

  the test passes

* I move the line to :ref:`test_what_is_true`

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
            self.assertTrue('text')
            self.assertTrue((1, 2, 3, 'n'))
            self.assertTrue([1, 2, 3, 'n'])


    # NOTES

* I add comments

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 2, 9

    # NOTES
    # a list with things is true
    # a tuple with things is true
    # a string with things is true
    # positive and negative numbers are true
    # True is true
    # True is not false
    # True is a boolean
    # the empty list is false
    # the empty tuple is false
    # the empty string is false
    # 0 is false
    # None is false
    # False is false
    # False is not true
    # False is a boolean

:ref:`in Python, the empty list is False and a list with things is True<is a list False or True?>`. I can see a pattern.

-----

*********************************************************************************
is a set False or True?
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a line to in :ref:`test_what_is_true` to see if a set_ is True_

.. code-block:: python
  :lineno-start: 23
  :emphasize-lines: 4

          self.assertTrue('text')
          self.assertTrue((1, 2, 3, 'n'))
          self.assertTrue([1, 2, 3, 'n'])
          self.assertTrue(set())


  # NOTES

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: set() is not true

the empty set_ is NOT True_

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the :ref:`method<what is a function?>`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 1

            self.assertFalse(set())

  the test passes

* I move the line to :ref:`test_what_is_false`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 4

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

* I add another line to :ref:`test_what_is_false` to see if a set_ with things is False_

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 5

            self.assertFalse(str())
            self.assertFalse(tuple())
            self.assertFalse(list())
            self.assertFalse(set())
            self.assertFalse({1, 2, 3, 'n'})

        def test_what_is_true(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: {1, 2, 3, 'n'} is not false

  a set_ with things is NOT False_

* I change the :ref:`method<what is a function?>`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 1

            self.assertTrue({1, 2, 3, 'n'})

  the test passes

* I move the line to :ref:`test_what_is_true`

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
            self.assertTrue('text')
            self.assertTrue((1, 2, 3, 'n'))
            self.assertTrue([1, 2, 3, 'n'])
            self.assertTrue({1, 2, 3, 'n'})


    # NOTES

* I add to the comments

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 2, 10

    # NOTES
    # a set with things is true
    # a list with things is true
    # a tuple with things is true
    # a string with things is true
    # positive and negative numbers are true
    # True is true
    # True is not false
    # True is a boolean
    # the empty set is false
    # the empty list is false
    # the empty tuple is false
    # the empty string is false
    # 0 is false
    # None is false
    # False is false
    # False is not true
    # False is a boolean


    # Exceptions seen
    # AssertionError

:ref:`in Python, the empty set is False and a set with things is True<is a set False or True?>`

----

*********************************************************************************
is a dictionary False or True?
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a line to :ref:`test_what_is_true` to test if a :ref:`dictionary <dictionaries>` is True_

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
          self.assertTrue('text')
          self.assertTrue((1, 2, 3, 'n'))
          self.assertTrue([1, 2, 3, 'n'])
          self.assertTrue({1, 2, 3, 'n'})
          self.assertTrue(dict())


  # NOTES

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: {} is not true

the empty :ref:`dictionary <dictionaries>` is NOT True_

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

  the test passes

* I move the line to the :ref:`test_what_is_false method<test_what_is_false>`

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

* I add another line to test if a :ref:`dictionary <dictionaries>` with things is also False_

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 4

            self.assertFalse(list())
            self.assertFalse(set())
            self.assertFalse(dict())
            self.assertFalse({'key': 'value'})

        def test_what_is_true(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: {'key': 'value'} is not false

  a :ref:`dictionary<dictionaries>` with things is NOT False_

* I change assertFalse_ to assertTrue_

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 1

            self.assertTrue({'key': 'value'})

  the test passes

* I move the line to the :ref:`test_what_is_true method<test_what_is_true>`

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
            self.assertTrue('text')
            self.assertTrue((1, 2, 3, 'n'))
            self.assertTrue([1, 2, 3, 'n'])
            self.assertTrue({1, 2, 3, 'n'})
            self.assertTrue({'key': 'value'})


    # NOTES

* I add the last 2 comments

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 2, 11

    # NOTES
    # a dictionary with things is true
    # a set with things is true
    # a list with things is true
    # a tuple with things is true
    # a string with things is true
    # positive and negative numbers are true
    # True is true
    # True is not false
    # True is a boolean
    # the empty dictionary is false
    # the empty set is false
    # the empty list is false
    # the empty tuple is false
    # the empty string is false
    # 0 is false
    # None is false
    # False is false
    # False is not true
    # False is a boolean


    # Exceptions seen
    # AssertionError

:ref:`in Python, the empty dictionary is False, and a dictionary with things is True<is a dictionary False or True?>`

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_booleans.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_ and use :kbd:`q` on the keyboard to leave the tests and the terminal_ goes back to the command line

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

* a container (strings_, tuples_, :ref:`lists<what is a list?>`, sets_, :ref:`dictionaries<what is a dictionary?>`) with things is True_
* positive and negative numbers are True_
* an empty container is False_
* ``0`` is False_
* False_ is not True_
* True_ is not False_
* True_ and False_ are booleans_

these things come in handy when I write :ref:`conditions<if statements>` in programs_, because I can make decisions on whether the :ref:`data<data structures>` is empty or has something in it

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

* :ref:`how to make a test driven development environment manually<how to make a test driven development environment>`
* :ref:`how to raise AssertionError with assert methods<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`what causes AttributeError<what causes AttributeError?>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what None is<what is None?>`
* :ref:`what is True and False in Python<what are booleans?>`

:ref:`Would you like to test the truth table?<truth table>` It will help you understand writing programs_ that make decisions based on :ref:`conditions<if statements>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->