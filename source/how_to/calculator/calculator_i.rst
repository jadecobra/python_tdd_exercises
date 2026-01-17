.. meta::
  :description: Learn Test-Driven Development in Python by building a calculator from scratch. This tutorial covers writing tests, handling exceptions, and refactoring.
  :keywords: Jacob Itegboje, python tdd calculator tutorial, test driven development python example, python calculator tutorial for beginners, python tdd workflow, python unit testing tutorial, how to build a calculator 1n python step-by-step, python test driven development with pytest, python programming projects for beginners

.. include:: ../../links.rst

#################################################################################
how to make a calculator
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/i8fGEqdH3yk?si=eBow2hwdlh01aVUF" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

I want to write a program_ that can ``add``, ``subtract``, ``multiply`` and ``divide``

*********************************************************************************
preview
*********************************************************************************

Here are the tests I have by the end of the chapter

.. literalinclude:: ../../code/calculator/tests/test_calculator.py
  :language: python
  :linenos:

----

*********************************************************************************
start the project
*********************************************************************************

* I name this project ``calculator``
* I open a terminal_
* then I `make a directory`_ for the project

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir calculator

  the terminal_ goes back to the command line

  .. code-block:: shell

    .../pumping_python

* I `change directory`_ to the project

  .. code-block:: shell
    :emphasize-lines: 1

    cd calculator

  the terminal_ shows I am now in the ``calculator`` folder_

  .. code-block:: shell

    .../pumping_python/calculator

* I `make a folder`_ for the source code

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir src

  the terminal_ goes back to the command line

  .. code-block:: shell

    .../pumping_python/calculator

* I use touch_ to make an empty file_ for the program_ in the ``src`` folder_

  .. code-block:: shell
    :emphasize-lines: 1

    touch src/calculator.py

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``New-Item src/calculator.py`` instead of ``touch src/calculator.py``

    .. code-block:: shell
      :emphasize-lines: 1

      New-Item src/calculator.py

  the terminal_ goes back to the command line

  .. code-block:: shell

    .../pumping_python/calculator

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

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``New-Item tests/__init__.py`` instead of ``touch tests/__init__.py``

    .. code-block:: shell
      :emphasize-lines: 1

      New-Item tests/__init__.py

  the terminal_ goes back to the command line

* I make an empty file_ for the actual test

  .. code-block:: shell
    :emphasize-lines: 1

    touch tests/test_calculator.py

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``New-Item tests/test_calculator.py`` instead of ``touch tests/test_calculator.py``

    .. code-block:: shell
      :emphasize-lines: 1

      New-Item tests/test_calculator.py

  the terminal_ goes back to the command line

* I open ``test_calculator.py`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_

  .. TIP:: I can open a file_ from the terminal_ in `Visual Studio Code`_ by typing ``code`` and the name of the file_, for example

    .. code-block:: shell
      :emphasize-lines: 1

      code tests/test_calculator.py

    ``test_calculator.py`` opens up in the :ref:`editor<2 editors>`

* I add :ref:`the first failing test<test_failure>` to ``test_calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-7

    import unittest


    class TestCalculator(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

* I make a `virtual environment`_ in the terminal_

  .. code-block:: shell
    :emphasize-lines: 1

    python3 -m venv .venv

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``python3 -m venv .venv`` instead of ``python3 -m venv .venv``

    .. code-block:: shell
      :emphasize-lines: 1

      python -m venv .venv

  the terminal_ takes some time then goes back to the command line

* I activate the `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    source .venv/bin/activate

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``.venv/bin/activate.ps1`` NOT ``source .venv/bin/activate``

    .. code-block:: shell
      :emphasize-lines: 1

      .venv/scripts/activate.ps1

  the terminal_ shows

  .. code-block:: shell

    (.venv) .../pumping_python/calculator

* I upgrade the `Python package manager (pip)`_ to the latest version

  .. code-block:: shell
    :emphasize-lines: 1

    python3 -m pip install --upgrade pip

  the terminal_ shows pip_ being uninstalled then installs the latest version or shows that it is already the latest version

* I make a ``requirements.txt`` file_ for the `Python programs`_ my project needs

  .. code-block:: shell
    :emphasize-lines: 1

    echo "pytest-watch" > requirements.txt

  the terminal_ goes back to the command line

* I use pip_ to use the requirements file_ to install ``pytest-watch``

  .. code-block:: shell
    :emphasize-lines: 1

    python3 -m pip install --requirement requirements.txt

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``python -m pip install --requirement requirements.txt`` instead of ``python3 -m pip install --requirement requirements.txt``

    .. code-block:: shell
      :emphasize-lines: 1

      python -m pip install --requirement requirements.txt

  the terminal_ shows pip_ downloads and installs the `Python programs`_ that `pytest-watch`_ needs to run

* I use `pytest-watch`_ to run the test

  .. code-block:: shell
    :emphasize-lines: 1

    pytest-watch

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 8, 10

    ================================ FAILURES ================================
    _____________________ TestCalculator.test_failure ________________________

    self = <tests.test_calculator.TestCalculator testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_calculator.py:7: AssertionError
    ========================= short test summary info ==========================
    FAILED tests/test_calculator.py::TestCalculator::test_failure - AssertionError: True is not false
    =========================== 1 failed in X.YZs ============================

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option` or :kbd:`command` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_calculator.py:7`` to open it in the :ref:`editor<2 editors>`

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4-5

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

* I add a TODO list to keep track of the work for the program

  .. code-block:: python
    :linenos:
    :emphasize-lines: 10-14

    import unittest


    class TestCalculator(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(False)


    # TODO
    # test addition
    # test subtraction
    # test multiplication
    # test division


    # Exceptions seen
    # AssertionError

*********************************************************************************
test_addition
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

* I change ``test_failure`` to ``test_addition`` then change `assertFalse`_ to `assertEqual`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-10

    import unittest


    class TestCalculator(unittest.TestCase):

        def test_addition(self):
            self.assertEqual(
                src.calculator.add(0, 1),
                1
            )

  - the `assertEqual method`_ from :ref:`AssertionError<what causes AssertionError?>` checks if the 2 things in parentheses are the same. It is like the statement ``assert x == y`` or asking ``is x equal to y?``
  - the explanation I like from what I have seen is that one of them is

    - ``reality`` - ``src.calculator.add(0, 1)``, and the other is
    - my ``expectation`` - ``1``, because ``0 + 1`` is ``1``
    - in other words is the result ``src.calculator.add(0, 1)`` equal to ``1``?

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'src' is not defined

  because ``src`` is not defined in ``test_calculator.py``

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I add :ref:`NameError<test_catching_name_error_in_tests>` to the list of :ref:`Exceptions<errors>` seen in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 3

    # Exceptions seen
    # AssertionError
    # NameError

* I add an `import statement`_ at the top of the file_ for the ``calculator`` :ref:`module<ModuleNotFoundError>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.calculator
    import unittest


    class TestCalculator(unittest.TestCase):

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.calculator' has no attribute 'add'

  I think of ``src.calculator.add`` as an address, ``add`` is something (an :ref:`attribute<AttributeError>`) in the empty ``calculator.py`` file_ from the ``src`` `folder (directory)`_

* I add :ref:`AttributeError` to the list of :ref:`Exceptions<errors>` seen in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 4

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError

* I open ``calculator.py`` from the ``src`` folder in the :ref:`editor<2 editors>`, and I type the name

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    add

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'add' is not defined

  I have to tell Python_ what the name ``add`` stands for or means

* I point it to :ref:`None<what is None?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    add = None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

  because the ``add`` :ref:`variable<test_attribute_error_w_variables>` is now a name for :ref:`None<what is None?>` which I cannot use like a :ref:`function<what is a function?>`

* I add :ref:`TypeError` to the list of :ref:`Exceptions<errors>` seen in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 5

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* I use the def_ keyword in ``calculator.py`` to make ``add`` a :ref:`function<what is a function?>` so it is callable_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def add():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: add() takes 0 positional arguments but 2 were given

  the definition of ``add`` does not allow it take input, but 2 were given in the call ``src.calculator.add(0, 1)``: ``0`` and ``1``

* I make the ``add`` :ref:`function<what is a function?>` take 2 inputs

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def add(first_input, second_input):
        return None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None != 1

  the ``add`` :ref:`function<what is a function?>` returns :ref:`None<what is None?>`, the test expects ``1``

* I make the `return statement`_ match the expected value

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def add(first_input, second_input):
        return 1

  the test passes, time for a victory lap!

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

The ``add`` :ref:`function<what is a function?>` passes the test but does not meet the actual requirement because it always returns ``1``. I want it to return the result of a calculation with the inputs

---------------------------------------------------------------------------------
:red:`RED`: make it fail
---------------------------------------------------------------------------------

To show the problem with the :ref:`function<what is a function?>`, I add another :ref:`assertion<what is an assertion?>` in ``test_calculator.py``

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 6-9

        def test_addition(self):
            self.assertEqual(
                src.calculator.add(0, 1),
                1
            )
            self.assertEqual(
                src.calculator.add(0, 2),
                2
            )

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  E    AssertionError: 1 != 2

the :ref:`function<what is a function?>` returns ``1``, the test expects ``2``

---------------------------------------------------------------------------------
:green:`GREEN`: make it pass
---------------------------------------------------------------------------------

* when I change the `return statement`_ in ``calculator.py`` to match the expectation

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def add(first_input, second_input):
        return 2

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 2 != 1

  this makes the :ref:`assertion<what is an assertion?>` that was passing before now fail. I need a solution that can make the two tests pass

* I make the :ref:`function<what is a function?>` return the result of adding the two inputs

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def add(first_input, second_input):
        return first_input + second_input

  the test passes. The ``add`` :ref:`function<what is a function?>` passes the two tests

---------------------------------------------------------------------------------
:red:`RED`: make it fail
---------------------------------------------------------------------------------

I add another test to make sure the :ref:`function<what is a function?>` works for other numbers

.. code-block:: python
  :lineno-start: 12
  :emphasize-lines: 5-8

          self.assertEqual(
              src.calculator.add(0, 2),
              2
          )
          self.assertEqual(
              src.calculator.add(0, 3),
              2
          )

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: 3 != 2

---------------------------------------------------------------------------------
:green:`GREEN`: make it pass
---------------------------------------------------------------------------------

I change the expectation in the test

.. code-block:: python
  :lineno-start: 16
  :emphasize-lines: 3

          self.assertEqual(
              src.calculator.add(0, 3),
              3
          )

the test passes

---------------------------------------------------------------------------------
:red:`RED`: make it fail
---------------------------------------------------------------------------------

I add another test with a different number for the first input

.. code-block:: python
  :lineno-start: 16
  :emphasize-lines: 5-8

          self.assertEqual(
              src.calculator.add(0, 3),
              3
          )
          self.assertEqual(
              src.calculator.add(1, 3),
              3
          )

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: 4 != 3

---------------------------------------------------------------------------------
:green:`GREEN`: make it pass
---------------------------------------------------------------------------------

I change the expectation to match reality

.. code-block:: python
  :lineno-start: 20
  :emphasize-lines: 3

          self.assertEqual(
              src.calculator.add(1, 3),
              4
          )

the test passes. The ``add`` :ref:`function<what is a function?>` looks good so far

---------------------------------------------------------------------------------
:red:`RED`: make it fail
---------------------------------------------------------------------------------

I add a test with bigger numbers

.. code-block:: python
  :lineno-start: 20
  :emphasize-lines: 5-8

          self.assertEqual(
              src.calculator.add(1, 3),
              4
          )
          self.assertEqual(
              src.calculator.add(123456, 789012),
              4
          )

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: 912468 != 4

---------------------------------------------------------------------------------
:green:`GREEN`: make it pass
---------------------------------------------------------------------------------

I change the expectation to match reality

.. code-block:: python
  :lineno-start: 24
  :emphasize-lines: 3

          self.assertEqual(
              src.calculator.add(123456, 789012),
              912468
          )

the test passes

---------------------------------------------------------------------------------
:red:`RED`: make it fail
---------------------------------------------------------------------------------

I add another test, this time with a negative number

.. code-block:: python
  :lineno-start: 24
  :emphasize-lines: 5-8

          self.assertEqual(
              src.calculator.add(123456, 789012),
              912468
          )
          self.assertEqual(
              src.calculator.add(-1, 0),
              912468
          )

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: -1 != 912468

---------------------------------------------------------------------------------
:green:`GREEN`: make it pass
---------------------------------------------------------------------------------

I change the expectation to match reality

.. code-block:: python
  :lineno-start: 28
  :emphasize-lines: 3

      self.assertEqual(
          src.calculator.add(-1, 0),
          -1
      )

the test passes

---------------------------------------------------------------------------------
:red:`RED`: make it fail
---------------------------------------------------------------------------------

I try another test with two negative numbers

.. code-block:: python
  :lineno-start: 28
  :emphasize-lines: 5-8

          self.assertEqual(
              src.calculator.add(-1, 0),
              -1
          )
          self.assertEqual(
              src.calculator.add(-2, -3),
              -1
          )

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: -5 != -1

---------------------------------------------------------------------------------
:green:`GREEN`: make it pass
---------------------------------------------------------------------------------

I make the expectation match reality

.. code-block:: python
  :lineno-start: 32
  :emphasize-lines: 3

          self.assertEqual(
              src.calculator.add(-2, -3),
              -5
          )

the test passes. The ``add`` :ref:`function<what is a function?>` can handle positive and negative numbers

---------------------------------------------------------------------------------
:red:`RED`: make it fail
---------------------------------------------------------------------------------

I add another test with floats_ (binary floating point decimal numbers)

.. code-block:: python
  :lineno-start: 32
  :emphasize-lines: 5-8

            self.assertEqual(
                src.calculator.add(-2, -3),
                -5
            )
            self.assertEqual(
                src.calculator.add(0.1234, -5.6789),
                -5
            )

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: -5.555499999999999 != -5

---------------------------------------------------------------------------------
:green:`GREEN`: make it pass
---------------------------------------------------------------------------------

I change the expectation

.. code-block:: python
  :lineno-start: 36
  :emphasize-lines: 3

            self.assertEqual(
                src.calculator.add(0.1234, -5.6789),
                -5.555499999999999
            )

the test passes. `Why is the result -5.555499999999999 instead of 5.5555? <https://docs.python.org/3/tutorial/stdlib2.html#decimal-floating-point-arithmetic>`_

=================================================================================
what is a variable?
=================================================================================

I just did the same kind of calculation 8 times in a row, there is a better way to do this with the Principle of Substitution. I can use a letter or a name for the numbers, that way I can have one test which covers all possible numbers, it is called a variable_.

A variable_ is a name that is used for values that change. For example, in the tests so far, I have

.. code-block:: python

  src.calculator.add(0, 1) is 0+1 is 1
  src.calculator.add(0, 2) is 0+2 is 2
  src.calculator.add(0, 3) is 0+3 is 3
  src.calculator.add(1, 3) is 1+3 is 4
  src.calculator.add(123456, 789012) is 123456+789012 is 912468
  src.calculator.add(-1, 0) is -1+0 is -1
  src.calculator.add(-2, -3) is -2+-3 is -5
  src.calculator.add(0.1234, -5.6789) is 0.1234+-5.6789 is -5.555499999999999

all of these lines can be written using ``first_number`` as the name of the first number and ``second_number`` as the name for the second number, like this

.. code-block:: python

  src.calculator.add(first_number, second_number) is first_number+second_number

* I add a new test at the beginning of ``test_addition`` with names for the values

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 4-7

    class TestCalculator(unittest.TestCase):

        def test_addition(self):
            self.assertEqual(
                src.calculator.add(first_number, second_number),
                first_number+second_number
            )
            self.assertEqual(
                src.calculator.add(0, 1),
                1
            )

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'first_number' is not defined

  I have to tell Python_ what the value of ``first_number`` is

* I point ``first_number`` to ``0`` before the test

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2

        def test_addition(self):
            first_number = 0

            self.assertEqual(
                src.calculator.add(first_number, second_number),
                first_number+second_number
            )

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'second_number' is not defined

  I have to tell Python_ what the value of ``second_number`` is

* I point ``second_number`` to ``1`` before the test

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 3


        def test_addition(self):
            first_number = 0
            second_number = 1

            self.assertEqual(
                src.calculator.add(first_number, second_number),
                first_number+second_number
            )

  the test passes

* I remove the next test since it is now covered by this new :ref:`assertion<what is an assertion?>` that uses a :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 11

        self.assertEqual(
            src.calculator.add(first_number, second_number),
            first_number+second_number
        )
        self.assertEqual(
            src.calculator.add(0, 2),
            2
        )

* I can do the same thing for all the other tests by changing the values for ``first_input`` and ``second_input``, for example

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 2

            first_number = 0
            second_number = 2

  the test is still green

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 1-2

            first_number = 1
            second_number = 3

  still green

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 1-2

            first_number = 123456
            second_number = 789012

  the terminal_ still shows green

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 1-2

            first_number = 0.1234
            second_number = -5.6789

  the test is still passing. The problem with this is I lose the test for the previous number, everytime I change a number. I need a better way

* I want to use random numbers for ``first_input`` and ``second_input`` to make sure that the ``add`` :ref:`function<what is a function?>` always returns the result of adding the two numbers without knowing what the numbers will be. I can do this with the `random module`_ from the `Python standard library`_. I add an `import statement`_ for it at the top of ``test_calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import random
    import src.calculator
    import unittest

  random_ is a :ref:`module<ModuleNotFoundError>` from the `Python standard library`_ that is used to make fake random numbers

* I use a random value for ``first_number``

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 2-3

        def test_addition(self):
            # first_number = 0.1234
            first_number = random.triangular(-0.1, 1.0)
            second_number = -5.6789

  the test is still green. `random.triangular`_ returns a random float_ that could be any number from ``-0.1`` to ``1.0`` in this case

* I want to see the test fail to be sure everything works as expected. I change the expectation in the first :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.add(first_number, second_number),
                first_number+first_number
            )

  I use (:kbd:`ctrl+s` (Windows/Linux) or :kbd:`command+s` (mac)) a few times in the :ref:`editor<2 editors>` to run the tests and the terminal_ :ref:`AssertionError<what causes AssertionError?>` with random values that look like this

  .. code-block:: shell

    AssertionError: -X.YZABCDEFGHIJKLM != A.BCDEFGHIJKLMNOPQ

* I change the expectation of the :ref:`assertion<what is an assertion?>` back to the right calculation

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 3

            self.assertEqual(
                src.calculator.add(first_number, second_number),
                first_number+second_number
            )

  the test is green again

* I remove the commented line then use a random value for ``second_number``

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 2-3

        def test_addition(self):
            first_number = random.triangular(-0.1, 1.0)
            # second_number = -5.6789
            second_number = random.triangular(-0.1, 1.0)

  the test is still green

* I remove the commented line and the other :ref:`assertions<what is an assertion?>` because they are covered by the one that uses random numbers. I do not need them anymore

  .. code-block:: python
    :lineno-start: 8

        def test_addition(self):
            first_number = random.triangular(-0.1, 1.0)
            second_number = random.triangular(-0.1, 1.0)

            self.assertEqual(
                src.calculator.add(first_number, second_number),
                first_number+second_number
            )


    # TODO

  still green

* I change the name of the variables to be more clear

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 2-3, 7-8, 10

    def test_addition(self):
        random_first_number = random.triangular(-0.1, 1.0)
        random_second_number = random.triangular(-0.1, 1.0)

        self.assertEqual(
            src.calculator.add(
                random_first_number,
                random_second_number
            ),
            random_first_number+random_second_number
        )

  the test is still green

* There is some duplication, I have to make a change in more than one place when I want to use a different range of random numbers for the test, for example

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 2-3

        def test_addition(self):
            random_first_number = random.triangular(-10.0, 10.0)
            random_second_number = random.triangular(-10.0, 10.0)

  the test is still green

* I add a :ref:`function<what is a function?>` to remove the repetition

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    import random
    import src.calculator
    import unittest


    def a_random_number():
        return random.triangular(-10.0, 10.0)


    class TestCalculator(unittest.TestCase):

  then I use the new :ref:`function<what is a function?>` to get random values for the ``random_first_number`` and ``random_second_number`` :ref:`variables<what is a variable?>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 2-5

        def test_addition(self):
            # random_first_number = random.triangular(-10.0, 10.0)
            random_first_number = a_random_number()
            # random_second_number = random.triangular(-10.0, 10.0)
            random_second_number = a_random_number()

  the terminal_ still shows green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 2-5

        def test_addition(self):
            random_first_number = a_random_number()
            random_second_number = a_random_number()

* I now only need to change the range of random numbers for the test in one place

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 2

    def a_random_number():
        return random.triangular(-10000.0, 10000.0)

  and the terminal_ still shows green

* I can use any range of numbers the computer can handle, for example

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 2

    def a_random_number():
        return random.triangular(-10.0**100000, 10.0**100000)

  the terminal_ shows OverflowError_

  .. code-block:: python

    OverflowError: (34, 'Numerical result out of range')

  because the numbers are too big to be used

  - ``**`` is the symbol for raise to the power (exponents)
  - ``10.0**100000`` is how to write ``10.0`` raised to the power of ``100,000``

  I make the range smaller

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 2

    def a_random_number():
        return random.triangular(-1000.0, 1000.0)

  the test is still green, though the test takes a little longer to run

* then I remove ``test addition`` from the TODO list

  .. code-block:: python
    :lineno-start: 22

    # TODO
    # test subtraction
    # test multiplication
    # test division

----

*********************************************************************************
test_subtraction
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test for subtraction in ``test_calculator.py``

.. code-block:: python
  :lineno-start: 12
  :emphasize-lines: 13-23

      def test_addition(self):
          random_first_number = a_random_number()
          random_second_number = a_random_number()

          self.assertEqual(
              src.calculator.add(
                  random_first_number,
                  random_second_number
              ),
              random_first_number+random_second_number
          )

      def test_subtraction(self):
          random_first_number = a_random_number()
          random_second_number = a_random_number()

          self.assertEqual(
              src.calculator.subtract(
                  random_first_number,
                  random_second_number
              ),
              random_first_number-random_second_number
          )


  # TODO

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.calculator' has no attribute 'subtract'

``calculator.py`` in the ``src`` folder_ does not have anything named ``subtract`` in it

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I add the name to ``calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    def add(first_input, second_input):
        return first_input + second_input


    subtract

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'subtract' is not defined

  I point ``subtract`` to :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 1

    subtract = None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

  I have seen this before

* I change ``subtract`` to a :ref:`function<what is a function?>` to make it callable_

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 1-2

    def subtract():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: subtract() takes 0 positional arguments but 2 were given

* I make ``subtract`` take inputs

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 1

    def subtract(first_input, second_input):
        return None

  I use (:kbd:`ctrl+s` (Windows/Linux) or :kbd:`command+s` (mac)) a few times in the :ref:`editor<2 editors>` to run the tests and the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` with random values that look like this

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None != XYZ.ABCDEFGHIJKLMNOP

  ``subtract`` returns :ref:`None<what is None?>`, the test expects ``random_first_number-random_second_number`` or ``first_input-second_input`` - the difference between the 2 numbers

* I make the ``subtract`` :ref:`function<what is a function?>` return the difference between the inputs

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2

    def subtract(first_input, second_input):
        return first_input - second_input

  the test passes. SUCCESS!

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I have some duplication to remove, the code below happens twice in ``test_calculator.py``

  .. code-block:: python

    random_first_number = a_random_number()
    random_second_number = a_random_number()

  once in ``test_addition`` and again in ``test_subtraction``

* I add :ref:`class attributes (variables)<test_attribute_error_w_class_attributes>` to remove the duplication and use the same numbers for both tests

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 3-4

    class TestCalculator(unittest.TestCase):

        random_first_number = a_random_number()
        random_second_number = a_random_number()

        def test_addition(self):
            random_first_number = a_random_number()
            random_second_number = a_random_number()

* I use the new :ref:`class attributes<test_attribute_error_w_class_attributes>` in ``test_addition``

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 3, 5

        def test_addition(self):
            # random_first_number = a_random_number()
            random_first_number = self.random_first_number
            # random_second_number = a_random_number()
            random_second_number = self.random_second_number

            self.assertEqual(
                src.calculator.add(
                    random_first_number,
                    random_second_number
                ),
                random_first_number+random_second_number
            )

  and in ``test_subtraction``

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 3, 5

        def test_subtraction(self):
            # random_first_number = a_random_number()
            random_first_number = self.random_first_number
            # random_second_number = a_random_number()
            random_second_number = self.random_second_number

            self.assertEqual(
                src.calculator.subtract(
                    random_first_number,
                    random_second_number
                ),
                random_first_number-random_second_number
            )

  the terminal_ shows the tests are still passing. The ``random_first_number`` and ``random_second_number`` :ref:`variables<what is a variable?>` are made once as :ref:`class attributes<test_attribute_error_w_class_attributes>` and used later in each test with ``self.random_first_number`` and ``self.random_second_number``, the same way I use `unittest.TestCase`_ :ref:`methods<what is a function?>` like assertEqual_ or assertFalse_

* I remove the commented lines in ``test_addition``

  .. code-block:: python
    :lineno-start: 15

        def test_addition(self):
            random_first_number = self.random_first_number
            random_second_number = self.random_second_number

  and do the same thing in ``test_subtraction``

  .. code-block:: python
    :lineno-start: 27

        def test_subtraction(self):
            random_first_number = self.random_first_number
            random_second_number = self.random_second_number

* I can use the :ref:`class attributes<test_attribute_error_w_class_attributes>` directly in ``test_addition``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 3-6, 8

            self.assertEqual(
                src.calculator.add(
                    # random_first_number,
                    self.random_first_number,
                    # random_second_number
                    self.random_second_number
                ),
                # random_first_number+random_second_number
                self.random_first_number+self.random_second_number
            )

  the test is still green. I remove the commented lines

  .. code-block:: python
    :lineno-start: 19

            self.assertEqual(
                src.calculator.add(
                    self.random_first_number,
                    self.random_second_number
                ),
                self.random_first_number+self.random_second_number
            )

* I do the same thing in ``test_subtraction``

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 3-6, 8

            self.assertEqual(
                src.calculator.subtract(
                    # random_first_number,
                    self.random_first_number,
                    # random_second_number
                    self.random_second_number
                ),
                # random_first_number-random_second_number
                self.random_first_number-self.random_second_number
            )

  the test is still passing. I remove the commented lines

  .. code-block:: python
    :lineno-start: 31

            self.assertEqual(
                src.calculator.subtract(
                    self.random_first_number,
                    self.random_second_number
                ),
                self.random_first_number-self.random_second_number
            )

* I remove the ``first_random_number`` and ``second_random_number`` :ref:`variables<what is a variable?>` from ``test_addition`` and ``test_subtraction`` because they are no longer used

  .. code-block:: python
    :lineno-start: 10

    class TestCalculator(unittest.TestCase):

        random_first_number = a_random_number()
        random_second_number = a_random_number()

        def test_addition(self):
            self.assertEqual(
                src.calculator.add(
                    self.random_first_number,
                    self.random_second_number
                ),
                self.random_first_number+self.random_second_number
            )

        def test_subtraction(self):
            self.assertEqual(
                src.calculator.subtract(
                    self.random_first_number,
                    self.random_second_number
                ),
                self.random_first_number-self.random_second_number
            )


    # TODO

  and the tests are still green!

* I remove ``test subtraction`` from the TODO list

  .. code-block:: python
    :lineno-start: 34

    # TODO
    # test multiplication
    # test division


    # Exceptions seen

----

*********************************************************************************
test_multiplication
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a failing test for multiplication in ``test_calculator.py``

.. code-block:: python
  :lineno-start: 24
  :emphasize-lines: 10-17

      def test_subtraction(self):
          self.assertEqual(
              src.calculator.subtract(
                  self.random_first_number,
                  self.random_second_number
              ),
              self.random_first_number-self.random_second_number
          )

      def test_multiplication(self):
          self.assertEqual(
              src.calculator.multiply(
                  self.random_first_number,
                  self.random_second_number
              ),
              self.random_first_number*self.random_second_number
          )


  # TODO

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.calculator' has no attribute 'multiply'

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

using what I know so far, I add a :ref:`function<what is a function?>` to ``calculator.py``

.. code-block:: python
  :lineno-start: 5
  :emphasize-lines: 5-6

  def subtract(first_input, second_input):
      return first_input - second_input


  def multiply(first_input, second_input):
      return first_input * second_input

the test passes! I remove ``test_multiplication`` from the TODO list in ``test_calculator.py``

.. code-block:: python
  :lineno-start: 43


  # TODO
  # test division


  # Exceptions seen

* ``*`` is the symbol for multiplication
* ``**`` is the symbol for raise to the power (exponent)

----

*********************************************************************************
test_division
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

Time for division. I add a new test to ``test_calculator.py``

.. code-block:: python
  :lineno-start: 33
  :emphasize-lines: 10-17

      def test_multiplication(self):
          self.assertEqual(
              src.calculator.multiply(
                  self.random_first_number,
                  self.random_second_number
              ),
              self.random_first_number*self.random_second_number
          )

      def test_division(self):
          self.assertEqual(
              src.calculator.divide(
                  self.random_first_number,
                  self.random_second_number
              ),
              self.random_first_number/self.random_second_number
          )


  # TODO

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.calculator' has no attribute 'divide'

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I add a :ref:`function<what is a function?>` to ``calculator.py``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 5-6

    def multiply(first_input, second_input):
        return first_input * second_input


    def divide(first_input, second_input):
        return first_input / second_input

  the test passes

* I remove the TODO list

  .. code-block:: python
    :lineno-start: 42

        def test_division(self):
            self.assertEqual(
                src.calculator.divide(
                    self.random_first_number,
                    self.random_second_number
                ),
                self.random_first_number/self.random_second_number
            )


    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # ZeroDivisionError

----

*********************************************************************************
test_calculator_tests
*********************************************************************************

Since everything is green, I can write the program_ that makes the tests pass without looking at them

=================================================================================
:red:`RED`: make it fail
=================================================================================

* I close ``test_calculator.py``
* then delete all the text in ``calculator.py``, the terminal_ shows 4 failures, I start with the last :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.calculator' has no attribute 'subtract'

  What other :ref:`Exceptions<errors>` do you think are raised as I go along?

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I add the name to ``calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    subtract

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'subtract' is not defined

  I point it to :ref:`None<what is None?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    subtract = None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

  I change ``subtract`` to a :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def subtract():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: subtract() takes 0 positional arguments but 2 were given

  I add :ref:`positional arguments<test_functions_w_positional_arguments>` to the :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def subtract(first_input, second_input):
        return None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` with random numbers

  .. code-block:: shell

    AssertionError: None != XYZ.ABCDEFGHIJKLMN

* I change the `return statement`_ to see the difference between the inputs and expected output, remember the :ref:`identity function?<test_identity_function>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def subtract(first_input, second_input):
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` with random numbers that look like this

  .. code-block:: shell

    AssertionError: (XYZ.ABCDEFGHIJKLMN, YZA.BCDEFGHIJKLMNO) != ZAB.CDEFGHIJKLMNOP

  the name of the :ref:`function<what is a function?>` is ``subtract`` and the test expects the difference between the 2 inputs

* I make the `return statement`_ match the expectation

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def subtract(first_input, second_input):
        return first_input - second_input

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.calculator' has no attribute 'multiply'

* I add a :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def subtract(first_input, second_input):
        return first_input - second_input


    def multiply():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: multiply() takes 0 positional arguments but 2 were given

  I add 2 :ref:`variables<what is a variable?>` for the positional arguments

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 1

    def multiply(first_input, second_input):
        return None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None != XY.ZABCDEFGHIJKLM

* I change the `return statement`_ to see the difference between the inputs and the expected output, :ref:`identity function again<test_identity_function>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2

    def multiply(first_input, second_input):
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` with random numbers that look like this

  .. code-block:: shell

    AssertionError: (XYZ.ABCDEFGHIJKLMNO, -YZA.BCDEFGHIJKLMNOPQ) != -ZAB.CDEFGHIJKLMNOPQR

  I change it to the multiplication of the inputs to match the name of the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2

    def multiply(first_input, second_input):
        return first_input * second_input

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.calculator' has no attribute 'divide'

* I add another :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 5-6

    def multiply(first_input, second_input):
        return first_input * second_input


    def divide(first_input, second_input):
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` with random numbers that look like this

  .. code-block:: shell

    AssertionError: (-XYZ.ABCDEFGHIJKLMNO, YZA.BCDEFGHIJKLMNOPQ) != -ZAB.CDEFGHIJKLMNOPQR

  when I change the `return statement`_ to match the expectation

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2

    def divide(first_input, second_input):
        return first_input / second_input

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.calculator' has no attribute 'add'

* the `return statement`_ of the last 3 :ref:`functions<what is a function?>` matched their names, I do the same thing for the new one

  .. code-block:: python
    :linenos:
    :emphasize-lines: 13-14

    def subtract(first_input, second_input):
        return first_input - second_input


    def multiply(first_input, second_input):
        return first_input * second_input


    def divide(first_input, second_input):
        return first_input / second_input


    def add(first_input, second_input):
        return first_input + second_input

  and all the tests are passing with no random failures, or are they?

----

*********************************************************************************
close the project
*********************************************************************************

* I close the file(s) I have open in the :ref:`editor(s)<2 editors>`
* I click in the terminal_ and exit the tests with :kbd:`ctrl+c` on the keyboard
* I deactivate the `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    deactivate

  the terminal_ goes back to the command line, ``(.venv)`` is no longer on the left side

  .. code-block:: shell

    .../pumping_python/calculator

* I `change directory`_ to the parent of ``calculator``

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

I wrote the following tests for a program_ that can :ref:`add<test_addition>`, :ref:`subtract<test_subtraction>`, :ref:`multiply<test_multiplication>` and :ref:`divide<test_division>`

* `test_addition`_
* `test_subtraction`_
* `test_multiplication`_
* `test_division`_

I also saw the following :ref:`Exceptions<errors>`

* :ref:`AssertionError<what causes AssertionError?>`
* :ref:`NameError<test_catching_name_error_in_tests>`
* :ref:`AttributeError`
* :ref:`TypeError`
* :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<how to make a calculator: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

you know a lot

* :ref:`how to make a test driven development environment manually<how to make a test driven development environment>`
* :ref:`how to raise AssertionError with assert methods<what causes AssertionError?>`
* :ref:`how to write functions<what is a function?>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what is None and NOT None<what is None?>`
* :ref:`what is True and False in Python<what are booleans?>`
* :ref:`how to write programs that make decisions<truth table>`
* :ref:`how to make a calculator<how to make a calculator>`

There is a problem, I have done the same steps for each of the 8 chapters covered so far

* I give the project a name
* :ref:`I make a directory for the project<how to make a directory for the project>`
* :ref:`I change directory to the project<how to change directory to the project>`
* :ref:`I make a directory for the source code named 'src'<how to make a directory for the source code>`
* :ref:`I make a Python file to hold the source code in the 'src' folder<how to make an empty file>`
* :ref:`I make a directory for the tests<how to make a directory for the tests>`
* :ref:`I make the 'tests' folder a Python package<how to make the tests a Python package>`
* :ref:`I make a Python file to hold the tests in the 'tests' folder<test_failure>`
* :ref:`I add the first failing test to the test file<test_failure>`
* :ref:`I make a virtual environment<how to make a virtual environment>`
* :ref:`I activate the virtual environment<how to activate a virtual environment>`
* :ref:`I upgrade the Python package manager<how to upgrade the Python package manager in a virtual environment>`
* :ref:`I make a requirements file for the needed Python packages<how to write text to a file>`
* :ref:`I install the packages listed in the requirements file<how to install Python packages in a virtual environment>`
* :ref:`I run the tests automatically<how to run the tests automatically in a virtual environment>`
* :ref:`I open the test file in the editor from the terminal<how to open the test file in the editor from the terminal>`
* I make the test pass
* then I start working on the project

I think I know how to make a Python_ :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>`. I am going to :ref:`write a program that will do all the steps for making a project for me<how to make a Python Test Driven Development environment automatically>`, so I never have to do those steps again.

:ref:`Would you like to know how to make a Python Test Driven Development environment automatically?<how to make a test driven development environment 2>`

-----


.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->