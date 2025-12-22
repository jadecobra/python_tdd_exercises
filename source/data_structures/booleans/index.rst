.. meta::
  :description: Learn how Python's boolean data type, operators (and, or, not), and truthiness work in conditional statements to control program_ flow. Watch the tutorial!
  :keywords: Jacob Itegboje, python boolean tutorial for beginners, python boolean operators and or not, python if statement with boolean, python truthiness and falsiness explained, what is boolean in python with example, how to use bool() in python, python boolean return function, common python boolean mistakes, python boolean best practices

.. include:: ../../links.rst

.. _booleans: https://docs.python.org/3/library/functions.html#bool

#################################################################################
booleans
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/6r3QcYN0wxQ?si=cQaK63rwX3f9PGX6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

*********************************************************************************
what are booleans?
*********************************************************************************

There are only 2 booleans_ - True_ and False_. I can use the `assertFalse`_ and `assertTrue`_ :ref:`methods<functions>` to test which of the :ref:`basic data structures<data structures>` seen so far - integers_, floats_, strings_, tuples_, :ref:`lists`, sets_ and :ref:`dictionaries`, are True_ or False_ in Python_

*********************************************************************************
preview
*********************************************************************************

Here are the tests I have by the end of the chapter

.. literalinclude:: ../../code/tests/test_booleans.py
  :language: python
  :linenos:

*********************************************************************************
questions about Booleans
*********************************************************************************

Here are the questions you can answer after going through this chapter

* :ref:`What is False?<test_what_is_false>`
* :ref:`What is True?<test_what_is_true>`
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

* I pick ``booleans`` as the name of this project
* I open a terminal_
* then I `make a directory`_ for the project

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir booleans

  the terminal_ goes back to the command line

  .. code-block:: shell

    .../pumping_python

* I `change directory`_ to the project

  .. code-block:: shell
    :emphasize-lines: 1

    cd booleans

  the terminal_ shows I am now in the ``booleans`` folder_

  .. code-block:: shell

    .../pumping_python/booleans

* I `make a folder`_ for the source code

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir src

  the terminal_ goes back to the command line

  .. code-block:: shell

    .../pumping_python/booleans

* I use touch_ to make an empty file_ for the program_ in the ``src`` folder_

  .. code-block:: shell
    :emphasize-lines: 1

    touch src/booleans.py

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use ``New-Item src/booleans.py`` instead of ``touch src/booleans.py``

    .. code-block:: shell
      :emphasize-lines: 1

      New-Item src/booleans.py

  the terminal_ goes back to the command line

  .. code-block:: shell

    .../pumping_python/booleans

* I `make a directory`_ for the tests

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir tests

  the terminal_ goes back to the command line

* I use touch_ to make an empty file_ in the ``tests`` folder_ to tell Python_ that it is a `Python package`_

  .. ATTENTION:: use 2 underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``

  .. code-block:: shell
    :emphasize-lines: 1

    touch tests/__init__.py

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use ``New-Item tests/__init__.py`` instead of ``touch tests/__init__.py``

    .. code-block:: shell
      :emphasize-lines: 1

      New-Item tests/__init__.py

  the terminal_ goes back to the command line

* I make an empty file_ for the actual test

  .. code-block:: shell
    :emphasize-lines: 1

    touch tests/test_booleans.py

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use ``New-Item tests/test_booleans.py`` instead of ``touch tests/test_booleans.py``

    .. code-block:: shell
      :emphasize-lines: 1

      New-Item tests/test_booleans.py

  the terminal_ goes back to the command line

* I open ``test_booleans.py`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_

  .. TIP:: I can open a file_ from the terminal_ in `Visual Studio Code`_ by typing ``code`` and the name of the file_ with

    .. code-block:: shell
      :emphasize-lines: 1

      code tests/test_booleans.py

    ``test_booleans.py`` opens up in the :ref:`editor<2 editors>`

* I add :ref:`the first failing test<test_failure>` to ``test_booleans.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-7

    import unittest


    class TestBooleans(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

* I make a `virtual environment`_ in the terminal_

  .. code-block:: shell
    :emphasize-lines: 1

    python3 -m venv .venv

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use ``python3 -m venv .venv`` instead of ``python3 -m venv .venv``

    .. code-block:: shell
      :emphasize-lines: 1

      python -m venv .venv

  the terminal_ takes some time then goes back to the command line

* I activate the `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    source .venv/bin/activate

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use ``.venv/bin/activate.ps1`` instead of ``source .venv/bin/activate``

    .. code-block:: shell
      :emphasize-lines: 1

      .venv/scripts/activate.ps1

  the terminal_ shows

  .. code-block:: shell

    (.venv) .../pumping_python/booleans

* I upgrade the `Python package manager (pip)`_ to the latest version

  .. code-block:: shell
    :emphasize-lines: 1

    python3 -m pip install --upgrade pip

  the terminal_ shows pip_ being uninstalled then installs the latest version or shows that it is already the latest version

* I make a ``requirements.txt`` file for the `Python programs`_ my project needs

  .. code-block:: shell
    :emphasize-lines: 1

    echo "pytest-watch" > requirements.txt

  the terminal_ goes back to the command line

* I use pip_ to use the requirements file_ to install ``pytest-watch``

  .. code-block:: shell
    :emphasize-lines: 1

    python3 -m pip install --requirement requirements.txt

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use ``python -m pip install --requirement requirements.txt`` instead of ``python3 -m pip install --requirement requirements.txt``

    .. code-block:: shell
      :emphasize-lines: 1

      python -m pip install --requirement requirements.txt

  the terminal_ shows pip_ downloads and installs the `Python programs`_ that `pytest-watch`_ needs to run

* I run `pytest-watch`_

  .. code-block:: shell
    :emphasize-lines: 1

    pytest-watch

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 8, 10

    ================================ FAILURES ================================
    ______________________ TestBooleans.test_failure ________________________

    self = <tests.test_booleans.TestBooleans testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_booleans.py:7: AssertionError
    ======================== short test summary info =========================
    FAILED tests/test_booleans.py::TestBooleans::test_failure - AssertionError: True is not false
    =========================== 1 failed in X.YZs ============================

* I hold :kbd:`ctrl` (Windows_/Linux_) or ``option or command`` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_booleans.py:7`` to open it in the :ref:`editor<2 editors>`

* I add :ref:`AssertionError` to the list of :ref:`Exceptions<errors>` seen in ``test_booleans.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4-5

            self.assertFalse(True)


    # Exceptions seen
    # AssertionError

* then I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the :ref:`assertion<AssertionError>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

  the test passes

----

*********************************************************************************
test_what_is_false
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

* I change ``test_failure`` to ``test_what_is_false``, then use the `assertNotIsInstance method`_ from :ref:`testing None<None>` to check if False_ is a child/instance of the bool_ :ref:`class<classes>` expecting a failure

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    import unittest


    class TestBooleans(unittest.TestCase):

        def test_what_is_false(self):
            self.assertNotIsInstance(False, bool)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: False is an instance of <class 'bool'>

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change assertNotIsInstance_ to assertIsInstance_

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 1

          self.assertIsInstance(False, bool)

the test passes and I add a note

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 1-2

  # NOTES
  # False is a boolean


  # Exceptions seen

so far this is going over what I already know from :ref:`testing None<None>`

----

*********************************************************************************
test_what_is_true
*********************************************************************************

I do the same thing with True_

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add another failing test

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 4-5

      def test_what_is_false(self):
          self.assertIsInstance(False, bool)

      def test_what_is_true(self):
          self.assertNotIsInstance(True, bool)


  # NOTES

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

    AssertionError: True is an instance of <class 'bool'>

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I change the `assert method`_

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 1

            self.assertIsInstance(True, bool)

  the test passes

* I add another note

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

    # NOTES
    # True is a boolean
    # False is a boolean


    # Exceptions seen

----

*********************************************************************************
:yellow:`REFACTOR`: make it better
*********************************************************************************

* I add a failing line to ``test_what_is_true``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 3

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(False)


    # NOTES

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: False is not true

* I change assertTrue_ to assertFalse_

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 3

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertFalse(False)

  the test passes

* I add a note

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 3

    # NOTES
    # True is a boolean
    # False is not true
    # False is a boolean


    # Exceptions seen
    # AssertionError

* I move the line from ``test_what_is_true`` to the ``test_what_is_false`` :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 3

      def test_what_is_false(self):
          self.assertIsInstance(False, bool)
          self.assertFalse(False)

      def test_what_is_true(self):
          self.assertIsInstance(True, bool)

  .. TIP:: You do not need to copy and paste to move a line. If you are using `Visual Studio Code`_ you can use :kbd:`alt` (Windows_/Linux_) or :kbd:`option` (MacOS_) with the up/down arrows on the keyboard to move a line up or down

* I add a note

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 3

    # NOTES
    # True is a boolean
    # False is false
    # False is not true
    # False is a boolean


    # Exceptions seen

* I add a failing line to ``test_what_is_false``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 4

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(True)

  the terminal_ shows :ref:`AssertionError`

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

  the test passes

* I add a note

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

* I move the line from ``test_what_is_false`` to the ``test_what_is_true`` :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 7

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)

* I add another note

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

All of this is still a repetition of what I did with :ref:`AssertionError`. Next up, I test the other Python_ basic data types_ to see which of are False_ or True_

* is :ref:`None` False_ or True_?
* is an integer_ False_ or True_?
* is a float_ False_ or True_?
* is a string_ False_ or True_?
* is a tuple_ False_ or True_?
* is a :ref:`list <lists>` False_ or True_?
* is a set_ False_ or True_?
* is a :ref:`dictionary <dictionaries>` False_ or True_?

----

*****************************************************************************************
is None False or True?
*****************************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a line in ``test_what_is_true`` to test if :ref:`None` is True_

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 4

      def test_what_is_true(self):
          self.assertIsInstance(True, bool)
          self.assertTrue(True)
          self.assertTrue(None)

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: None is not true

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change the :ref:`method<functions>`

.. code-block:: python
  :lineno-start: 13
  :emphasize-lines: 1

          self.assertFalse(None)

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

I move the line from ``test_what_is_true`` to ``test_what_is_false``

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

I add a note

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

:ref:`None` is False_ though I learned in :ref:`test_assertion_error_w_false` that False_ is not :ref:`None`

----

*********************************************************************************
is an integer False or True?
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a failing line ``test_what_is_false`` to see if an integer_ (a whole number) is False_

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 5

      def test_what_is_false(self):
          self.assertIsInstance(False, bool)
          self.assertFalse(False)
          self.assertFalse(None)
          self.assertFalse(-1)

      def test_what_is_true(self):

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: -1 is not false

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change the :ref:`method<functions>`

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 1

          self.assertTrue(-1)

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I move the line from ``test_what_is_false`` to ``test_what_is_true``

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

  I use ``-1`` for all the integers_ (whole numbers) that are smaller than ``0``. Negative integers_ are True_ in Python_

* I add a new failing line to ``test_what_is_true`` to see if ``0`` is True_

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 2

            self.assertTrue(-1)
            self.assertTrue(0)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 0 is not true

* I change the :ref:`method<functions>` to assertFalse_

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 1

            self.assertFalse(0)

  the test passes

* I move the line to ``test_what_is_false``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4

            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(None)
            self.assertFalse(0)

        def test_what_is_true(self):

  ``0`` is False_ in Python_

* I add another failing line to ``test_what_is_false`` to see if ``1`` is False

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 2

            self.assertFalse(0)
            self.assertFalse(1)

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 1 is not false

* I change the :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 1

            self.assertTrue(1)

  the test passes

* I move the line to ``test_what_is_true``

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 7

            self.assertFalse(0)

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)
            self.assertTrue(-1)
            self.assertTrue(1)

  I use ``1`` for all the integers_ (whole numbers) that are bigger than ``0``. Positive and negative integers_ are True_ in Python_

* I add notes

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

-----

*********************************************************************************
is a float False or True?
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a line to test if floats_ (binary floating point decimal numbers) are False_ in ``test_what_is_false``

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 2

          self.assertFalse(0)
          self.assertFalse(-0.1)

      def test_what_is_true(self):

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: -0.1 is not false

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I change the :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 1

            self.assertTrue(-0.1)

  the test passes

* I move the line to ``test_what_is_true``

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 4

            self.assertTrue(True)
            self.assertTrue(-1)
            self.assertTrue(1)
            self.assertTrue(-0.1)

  I use ``-0.1`` for all the floating point numbers that are smaller than ``0.0``. Negative floats_ are True_ in Python_

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add another failing line to ``test_what_is_true`` to see if ``0.0`` is True_

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 2

            self.assertTrue(-0.1)
            self.assertTrue(0.0)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 0.0 is not true

  I change the :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 1

            self.assertFalse(0.0)

  the test passes

* I move the line to ``test_what_is_false``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 6

        def test_what_is_false(self):
            self.assertIsInstance(False, bool)
            self.assertFalse(False)
            self.assertFalse(None)
            self.assertFalse(0)
            self.assertFalse(0.0)

        def test_what_is_true(self):

  ``0.0`` is False_ in Python_

* I add another line to ``test_what_is_false`` to see if ``0.1`` is False_ in Python_

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 2

            self.assertFalse(0.0)
            self.assertFalse(0.1)

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 0.1 is not false

* I change the :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 1

            self.assertTrue(0.1)

  the test passes

* I move the line to ``test_what_is_true``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 9

            self.assertFalse(0.0)

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)
            self.assertTrue(True)
            self.assertTrue(-1)
            self.assertTrue(1)
            self.assertTrue(-0.1)
            self.assertTrue(0.1)


    # NOTES

  I use ``0.1`` for all the floating point numbers that are bigger than ``0.0``. Positive and negative floats_ are also True_ in Python_

* I add notes

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

* I make the new notes simpler because floats_ and integers_ are numbers and ``0.0`` is the same as ``0`` even though they are different types_

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 2, 5

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

-----

*********************************************************************************
is a string False or True?
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a failing line to ``test_what_is_true`` to test if a string_ (anything in :ref:`quotes`) is True_

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

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: '' is not true

the empty string_ ('') is not True_

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change the :ref:`method<functions>`

.. code-block:: python
  :lineno-start: 20
  :emphasize-lines: 1

          self.assertFalse(str())

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I move the line to ``test_what_is_false``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 2

            self.assertFalse(0.0)
            self.assertTrue(str())

        def test_what_is_true(self):

  the empty string_ ('') is not False_

* I add a failing line to ``test_what_is_false``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3

            self.assertFalse(0.0)
            self.assertFalse(str())
            self.assertFalse('text')

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 'text' is not false

  I change the :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 1

            self.assertTrue('text')

  the test passes

* I move the line to ``test_what_is_true``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 10

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

* I add notes

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


    # Exceptions seen
    # AssertionError

----

*********************************************************************************
is a tuple False or True?
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a line to ``test_what_is_true`` to see if a tuple_ (anything in parentheses (``()``)) is True_

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

The terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: () is not true

the empty tuple_ is not True_

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I change the `assert method`_

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 1

            self.assertFalse(tuple())

  the test passes

* I move the line to ``test_what_is_false``

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

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add another line to ``test_what_is_false`` to see if a tuple_ with things is False_

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

            self.assertFalse(tuple())
            self.assertFalse((1, 2, 3, 'n'))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (1, 2, 3, 'n') is not false

  a tuple_ with things is NOT False_

* I change the :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 1

            self.assertTrue((1, 2, 3, 'n'))

  the test passes

* I move the line to ``test_what_is_true``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 11

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

* I add notes

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

----

*********************************************************************************
is a list False or True?
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a line to test if a :ref:`list<lists>` (anything in square brackets (``[]``)) is True_

.. code-block:: python
  :lineno-start: 23
  :emphasize-lines: 2

      self.assertTrue((1, 2, 3, 'n'))
      self.assertTrue(list())

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: [] is not true

the empty :ref:`list<lists>` is NOT True_

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I change the :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 1

            self.assertFalse(list())

  the test passes

* I move the line to ``test_what_is_false``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

            self.assertFalse(tuple())
            self.assertFalse(list())

        def test_what_is_true(self):

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add another line to ``test_what_is_false`` to see if a :ref:`list<lists>` with things is False_

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 2

            self.assertFalse(list())
            self.assertFalse([1, 2, 3, 'n'])

        def test_what_is_true(self):
            self.assertIsInstance(True, bool)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: [1, 2, 3, 'n'] is not false

* I change the :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 1

            self.assertTrue([1, 2, 3, 'n'])

  the test passes

* I move the line to ``test_what_is_true``

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 12

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

* I add notes

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


    # Exceptions seen
    # AssertionError

I can see a pattern forming

-----

*********************************************************************************
is a set False or True?
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a line to in ``test_what_is_true`` to see if a set_ is True_

.. code-block:: python
  :lineno-start: 25
  :emphasize-lines: 2

          self.assertTrue([1, 2, 3, 'n'])
          self.assertTrue(set())


  # NOTES

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: set() is not true

the empty set_ is NOT True_

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I change the :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 1

            self.assertFalse(set())

  the test passes

* I move the line to ``test_what_is_false``

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 2

            self.assertFalse(list())
            self.assertFalse(set())

        def test_what_is_true(self):

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add another line to ``test_what_is_false`` to see if a set_ with things is False_

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 2

            self.assertFalse(set())
            self.assertFalse({1, 2, 3, 'n'})

        def test_what_is_true(self):

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {1, 2, 3, 'n'} is not false

  a set_ with things is NOT False_

* I change the :ref:`method<functions>`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 1

            self.assertTrue({1, 2, 3, 'n'})

  the test passes

* I move the line to ``test_what_is_true``

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 13

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

* I add to the notes

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

----

*********************************************************************************
is a dictionary False or True?
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a line to ``test_what_is_true`` to test if a :ref:`dictionary <dictionaries>` is True_

.. code-block:: python
  :lineno-start: 27
  :emphasize-lines: 2

          self.assertTrue({1, 2, 3, 'n'})
          self.assertTrue(dict())


  # NOTES

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: {} is not true

the empty :ref:`dictionary <dictionaries>` is NOT True_

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I change assertTrue_ to assertFalse_

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 1

            self.assertFalse(dict())

  the test passes

* I move the line to the ``test_what_is_false`` :ref:`method<functions>`

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

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add another line to test if a :ref:`dictionary <dictionaries>` with things is also False_

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 4

            self.assertFalse(list())
            self.assertFalse(set())
            self.assertFalse(dict())
            self.assertFalse({'key': 'value'})

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: {'key': 'value'} is not false

  a :ref:`dictionary<dictionaries>` with things is NOT False_

* I change assertFalse_ to assertTrue_

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 1

            self.assertTrue({'key': 'value'})

  the test passes

* I move the line to the ``test_what_is_true`` :ref:`method<functions>`

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

* I add the last 2 notes

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

----

*********************************************************************************
close the project
*********************************************************************************

* I close the file(s) I had open in the :ref:`editor(s)<2 editors>`
* I exit the tests in the terminal_ with :kbd:`ctrl+c` on the keyboard
* I deactivate the `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    deactivate

  the terminal_ goes back to the command line, ``(.venv)`` is no longer on the left side

  .. code-block:: shell

    .../pumping_python/booleans

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

From the tests I can see that in Python_

* a container with things is True_
* an empty container is False_
* positive and negative numbers are True_
* ``0`` is False_
* False_ is not True_
* True_ is not False_
* True_ and False_ are booleans_

these things come in handy when I write :ref:`conditions<if statements (conditionals)>` in programs_, because I can make decisions on whether the :ref:`data<data structures>` is empty or has something in it

:ref:`How many questions can you answer after going through this chapter?<questions about Booleans>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<data structures: booleans: tests>`

----

*********************************************************************************
what is next?
*********************************************************************************

you now know

* :ref:`how to make a test driven development environment`
* :ref:`how to raise AssertionError with assert methods<AssertionError>`
* :ref:`how to write functions<functions>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what None is<None>`
* :ref:`what is True and False in Python<booleans>`

:ref:`Would you like to test the truth table?<booleans: truth table>` It will help you understand writing programs_ that make decisions based on :ref:`conditions<if statements (conditionals)>`

----

*********************************************************************************
please leave a review
*********************************************************************************

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review, if this has been a 5 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->