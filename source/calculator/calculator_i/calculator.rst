.. meta::
  :description: Learn Test-Driven Development in Python by building a calculator from scratch. This tutorial covers writing tests, handling exceptions, and refactoring.
  :keywords: Jacob Itegboje, python tdd calculator tutorial, test driven development python example, python calculator tutorial for beginners, python tdd workflow, python unit testing tutorial, how to build a calculator 1n python step-by-step, python test driven development with pytest, python programming projects for beginners

.. include:: ../../links.rst

.. _variable: https://grokipedia.com/page/Variable_symbol
.. _variables: variable_
.. _Substitution: https://grokipedia.com/page/Substitution_(logic)#substitution-logic
.. _unittest.TestCase assert methods: `assert methods`_

#################################################################################
how to make a calculator 1
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/i8fGEqdH3yk?si=eBow2hwdlh01aVUF" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

*********************************************************************************
preview
*********************************************************************************

These are the tests I have by the end of the chapter

.. literalinclude:: ../../code/calculator/tests/test_calculator.py
  :language: python
  :linenos:

----

*********************************************************************************
start the project
*********************************************************************************

* I name this project ``calculator``
* I open a terminal_
* I make a directory_ for the project

  .. code-block:: python
    :emphasize-lines: 1

    mkdir calculator

  the terminal_ goes back to the command line

* I change directory_ to the project

  .. code-block:: python
    :emphasize-lines: 1

    cd calculator

  the terminal_ shows I am in the ``calculator`` folder_

  .. code-block:: python

    .../pumping_python/calculator

* I make a directory_ for the source code

  .. code-block:: python
    :emphasize-lines: 1

    mkdir src

  the terminal_ goes back to the command line

* I make a :ref:`Python file<what is a module?>` to hold the source code in the ``src`` directory_

  .. code-block:: python
    :emphasize-lines: 1

    touch src/calculator.py

  .. NOTE::

    on Windows_ without `Windows Subsystem for Linux`_ use ``New-Item src/calculator.py`` instead of ``touch src/calculator.py``

    .. code-block:: python
      :emphasize-lines: 1

      New-Item src/calculator.py

  the terminal_ goes back to the command line

* I `make a directory`_ for the tests

  .. code-block:: python
    :emphasize-lines: 1

    mkdir tests

  the terminal_ goes back to the command line

* I make the ``tests`` directory_ a `Python package`_

  .. DANGER:: use 2 underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``

  .. code-block:: python
    :emphasize-lines: 1

    touch tests/__init__.py

  .. NOTE::

    on Windows_ without `Windows Subsystem for Linux`_ use ``New-Item tests/__init__.py`` instead of ``touch tests/__init__.py``

    .. code-block:: python
      :emphasize-lines: 1

      New-Item tests/__init__.py

  the terminal_ goes back to the command line

* I make a :ref:`Python file<what is a module?>` for the tests in the ``tests`` directory_

  .. code-block:: python
    :emphasize-lines: 1

    touch tests/test_calculator.py

  .. NOTE::

    on Windows_ without `Windows Subsystem for Linux`_ use ``New-Item tests/test_calculator.py`` instead of ``touch tests/test_calculator.py``

    .. code-block:: python
      :emphasize-lines: 1

      New-Item tests/test_calculator.py

  the terminal_ goes back to the command line

* I open ``test_calculator.py`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_

  .. TIP::

    I can open a file_ from the terminal_ in the `Integrated Development Environment (IDE)`_ with the name of the program and the name of the file_. That means if I type this in the terminal_

    .. code-block:: python
      :emphasize-lines: 1

      code tests/test_calculator.py

    `Visual Studio Code`_ opens ``test_calculator.py`` in the :ref:`editor<2 editors>`

* I add :ref:`the first failing test<test_failure>` to ``test_calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-7

    import unittest


    class TestCalculator(unittest.TestCase):

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

    Initialized project `calculator`

* I remove ``main.py`` from the project because I do not use it

  .. code-block:: python
    :emphasize-lines: 1

    rm main.py

  the terminal_ goes back to the command line

* I install the Python packages I gave in the requirements file_

  .. code-block:: python
    :emphasize-lines: 1

    uv add --requirement requirements.txt

  the terminal shows it installed the `Python packages`_

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: python
    :emphasize-lines: 8, 10

    ================================ FAILURES ================================
    _____________________ TestCalculator.test_failure ________________________

    self = <tests.test_calculator.TestCalculator testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_calculator.py:7: AssertionError
    ======================== short test summary info =========================
    FAILED tests/test_calculator.py::TestCalculator::test_failure - AssertionError: True is not false
    =========================== 1 failed in X.YZs ============================

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option/command` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_calculator.py:7`` to put the cursor on line 7 in the :ref:`editor<2 editors>`

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7-8
    :emphasize-text: AssertionError

    class TestCalculator(unittest.TestCase):

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

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I change ``test_failure`` to ``test_addition`` then change `assertFalse`_ to `assertEqual`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    import unittest


    class TestCalculator(unittest.TestCase):

        def test_addition(self):
            self.assertEqual(src.calculator.add(0, 1), 1)

  - the `assertEqual method`_ from :ref:`AssertionError<what causes AssertionError?>` checks if the 2 things in parentheses are the same. It is like the statement ``assert x == y`` or asking ``is x equal to y?``

  - I think of

    .. code-block:: python

      self.assertEqual(src.calculator.add(0, 1), 1)

    as

    .. code-block:: python

      self.assertEqual(reality, my_expectation)

    where

    - ``reality`` is ``src.calculator.add(0, 1)``
    - ``my_expectation`` is ``1`` because ``0 + 1`` is ``1``

    in other words, ``self.assertEqual(src.calculator.add(0, 1), 1)`` checks if the result of calling ``src.calculator.add`` with ``0`` and ``1`` as input is equal to ``1``

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'src' is not defined

  because I do not have a definition for ``src`` in ``test_calculator.py``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add :ref:`NameError<test_catching_name_error_in_tests>` to the list of :ref:`Exceptions<errors>` seen in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 3
    :emphasize-text: NameError

    # Exceptions seen
    # AssertionError
    # NameError

* I add an `import statement`_ at the top of the file_ for the ``calculator`` :ref:`module<what is a module?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.calculator
    import unittest


    class TestCalculator(unittest.TestCase):

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'add'

  I think of ``src.calculator.add`` as an address, ``add`` is something (:ref:`an attribute<what causes AttributeError?>`) in the empty ``calculator.py`` file_ from the ``src`` folder_

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 4
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError

* I open ``calculator.py`` from the ``src`` folder in the :ref:`editor<2 editors>`, then add the name

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    add

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'add' is not defined

  I have to tell Python_ what the name ``add`` means

* I point it to :ref:`None<what is None?>` to define it

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    add = None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  because the ``add`` :ref:`variable<what is a variable?>` is now a name for :ref:`None<what is None?>`, and :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`

* I add :ref:`TypeError` to the list of :ref:`Exceptions<errors>` seen in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 5
    :emphasize-text: TypeError

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

  .. code-block:: python

    TypeError: add() takes 0 positional arguments but 2 were given

  the definition of ``add`` does not allow it take input, but 2 were given in the call - ``0`` and ``1``

* I add names in the parentheses to make the :ref:`function<what is a function?>` take 2 inputs

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def add(first_input, second_input):
        return None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != 1

  the ``add`` :ref:`function<what is a function?>` returns :ref:`None<what is None?>`, the test expects ``1``

* I make the `return statement`_ give the test what it wants

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def add(first_input, second_input):
        return 1

  the test passes, time for a victory lap!

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

The ``add`` :ref:`function<what is a function?>` passes the test but does not do what I actually want because it always returns ``1``. I want it to return the result of a calculation with the inputs


* I add another :ref:`assertion<what is an assertion?>` to show the problem with the :ref:`function<what is a function?>` in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 3

        def test_addition(self):
            self.assertEqual(src.calculator.add(0, 1), 1)
            self.assertEqual(src.calculator.add(0, 2), 2)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 1 != 2

  the :ref:`function<what is a function?>` returns ``1``, the test expects ``2``

* I change the `return statement`_ in ``calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def add(first_input, second_input):
        return 2

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 2 != 1

  this makes the :ref:`assertion<what is an assertion?>` that was passing before - ``src.calculator.add(0, 1)`` fail. If the test sends

  - ``0`` and ``2`` to ``src.calculator.add`` it returns ``2``
  - ``0`` and ``1`` to ``src.calculator.add`` it returns ``2``

  I need a solution that can make the two tests pass. The :ref:`function<what is a function?>` should return

  - ``2`` if the test sends ``0`` and ``2`` to ``src.calculator.add`` because ``0 + 2 == 2``
  - ``1`` if the test sends ``0`` and ``1`` to ``src.calculator.add`` because ``0 + 1 == 1``

* I make the :ref:`function<what is a function?>` return the result of adding the two inputs

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def add(first_input, second_input):
        return first_input + second_input

  the two tests are passing

* I add another test to make sure the :ref:`function<what is a function?>` works for other numbers in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4

        def test_addition(self):
            self.assertEqual(src.calculator.add(0, 1), 1)
            self.assertEqual(src.calculator.add(0, 2), 2)
            self.assertEqual(src.calculator.add(0, 3), 2)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 3 != 2

* I change the expectation in the test

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 1

            self.assertEqual(src.calculator.add(0, 3), 3)

  the test passes

* I add another test with a different number for the first input

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 5

        def test_addition(self):
            self.assertEqual(src.calculator.add(0, 1), 1)
            self.assertEqual(src.calculator.add(0, 2), 2)
            self.assertEqual(src.calculator.add(0, 3), 3)
            self.assertEqual(src.calculator.add(1, 3), 3)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 4 != 3

* I change the expectation to match reality

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 1

            self.assertEqual(src.calculator.add(1, 3), 4)

  the test passes. The ``add`` :ref:`function<what is a function?>` looks good so far.

* I add an :ref:`assertion<what is an assertion?>` with bigger numbers

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 6

        def test_addition(self):
            self.assertEqual(src.calculator.add(0, 1), 1)
            self.assertEqual(src.calculator.add(0, 2), 2)
            self.assertEqual(src.calculator.add(0, 3), 3)
            self.assertEqual(src.calculator.add(1, 3), 4)
            self.assertEqual(src.calculator.add(123456, 789012), 4)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 912468 != 4

* I change the expectation to match reality

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 1

            self.assertEqual(src.calculator.add(123456, 789012), 912468)

  the test passes

* I add another :ref:`assertion<what is an assertion?>` with a negative number

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 7

        def test_addition(self):
            self.assertEqual(src.calculator.add(0, 1), 1)
            self.assertEqual(src.calculator.add(0, 2), 2)
            self.assertEqual(src.calculator.add(0, 3), 3)
            self.assertEqual(src.calculator.add(1, 3), 4)
            self.assertEqual(src.calculator.add(123456, 789012), 912468)
            self.assertEqual(src.calculator.add(-1, 0), 912468)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: -1 != 912468

* I change the expectation to match reality

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 1

            self.assertEqual(src.calculator.add(-1, 0), -1)

  the test passes

* I try another :ref:`assertion<what is an assertion?>` with two negative numbers

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 4

            self.assertEqual(src.calculator.add(1, 3), 4)
            self.assertEqual(src.calculator.add(123456, 789012), 912468)
            self.assertEqual(src.calculator.add(-1, 0), -1)
            self.assertEqual(src.calculator.add(-2, -3), -1)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: -5 != -1

* I make the expectation match reality

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 1

            self.assertEqual(src.calculator.add(-2, -3), -5)

  the test passes. The ``add`` :ref:`function<what is a function?>` can handle positive and negative whole numbers

* I add an :ref:`assertion<what is an assertion?>` with floats_ (binary floating point decimal numbers)

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 4

            self.assertEqual(src.calculator.add(123456, 789012), 912468)
            self.assertEqual(src.calculator.add(-1, 0), -1)
            self.assertEqual(src.calculator.add(-2, -3), -5)
            self.assertEqual(src.calculator.add(0.1, 1), -5)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 1.1 != -5

* I change the expectation

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 1

            self.assertEqual(src.calculator.add(0.1, 1), 1.1)

  the test passes

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 4

            self.assertEqual(src.calculator.add(-1, 0), -1)
            self.assertEqual(src.calculator.add(-2, -3), -5)
            self.assertEqual(src.calculator.add(0.1, 1), 1.1)
            self.assertEqual(src.calculator.add(0.1, 0.2), 1.1)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0.30000000000000004 != 1.1

  whoa!

* I change the expectation

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 1-4

            self.assertEqual(
                src.calculator.add(0.1, 0.2),
                0.30000000000000004
            )


  the test passes. `Why is the result "0.30000000000000004" and not "0.3"? <https://docs.python.org/3/tutorial/stdlib2.html#decimal-floating-point-arithmetic>`_

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 7-10

            self.assertEqual(src.calculator.add(-2, -3), -5)
            self.assertEqual(src.calculator.add(0.1, 1), 1.1)
            self.assertEqual(
                src.calculator.add(0.1, 0.2),
                0.30000000000000004
            )
            self.assertEqual(
                src.calculator.add(0.1234, -5.6789),
                0.30000000000000004
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: -5.555499999999999 != -5

  whaaaaat?!

* I change the expectation

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 16

        def test_addition(self):
            self.assertEqual(src.calculator.add(0, 1), 1)
            self.assertEqual(src.calculator.add(0, 2), 2)
            self.assertEqual(src.calculator.add(0, 3), 3)
            self.assertEqual(src.calculator.add(1, 3), 4)
            self.assertEqual(src.calculator.add(123456, 789012), 912468)
            self.assertEqual(src.calculator.add(-1, 0), -1)
            self.assertEqual(src.calculator.add(-2, -3), -5)
            self.assertEqual(src.calculator.add(0.1, 1), 1.1)
            self.assertEqual(
                src.calculator.add(0.1, 0.2),
                0.30000000000000004
            )
            self.assertEqual(
                src.calculator.add(0.1234, -5.6789),
                -5.555499999999999
            )


    # TODO

  the test passes. `Why is the result "-5.555499999999999" not "-5.5555"? <https://docs.python.org/3/tutorial/stdlib2.html#decimal-floating-point-arithmetic>`_

----

*********************************************************************************
what is a variable?
*********************************************************************************

I just did the same kind of calculation 10 times, there is a better way to do this thanks to Substitution_. I can use a letter or a name for the numbers, so that I can have one test for all possible numbers, it is called a variable_.

A variable_ is a name that is used for values that change. For example, in the tests so far, I have

.. code-block:: python

  src.calculator.add(0, 1) is 0 + 1 is 1
  src.calculator.add(0, 2) is 0 + 2 is 2
  src.calculator.add(0, 3) is 0 + 3 is 3
  src.calculator.add(1, 3) is 1 + 3 is 4
  src.calculator.add(123456, 789012)  is 123456 +789012 is 912468
  src.calculator.add(-2, -3) is -2 + -3 is -5
  src.calculator.add(-1, 0) is -1 + 0 is -1
  src.calculator.add(0.1, 1) is 0.1 + 1 is 1.1
  src.calculator.add(0.1, 0.2) is 0.1 + 0.2 is 0.30000000000000004
  src.calculator.add(0.1234, -5.6789) is 0.1234 + -5.6789 is -5.555499999999999

all of these lines can be written using ``x`` as the name of the first number and ``y`` as the name for the second number, like this

.. code-block:: python

  src.calculator.add(x, y) is x + y is x + y

* I add names to the first :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2-7

        def test_addition(self):
            first_number = 0
            second_number = 1
            self.assertEqual(
                src.calculator.add(first_number, second_number),
                first_number+second_number
            )
            self.assertEqual(src.calculator.add(0, 2), 2)

  the test is still green

* I do the same thing to the next :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 9-14

        def test_addition(self):
            first_number = 0
            second_number = 1
            self.assertEqual(
                src.calculator.add(first_number, second_number),
                first_number+second_number
            )

            first_number = 0
            second_number = 2
            self.assertEqual(
                src.calculator.add(first_number, second_number),
                first_number+second_number
            )

  still green

* I do the next one

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 8-13

            first_number = 0
            second_number = 2
            self.assertEqual(
                src.calculator.add(first_number, second_number),
                first_number+second_number
            )

            first_number = 0
            second_number = 3
            self.assertEqual(
                src.calculator.add(first_number, second_number),
                first_number+second_number
            )

  green

* then the next one

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 8-13

            first_number = 0
            second_number = 3
            self.assertEqual(
                src.calculator.add(first_number, second_number),
                first_number+second_number
            )

            first_number = 1
            second_number = 3
            self.assertEqual(
                src.calculator.add(first_number, second_number),
                first_number+second_number
            )

  still green

* then the next

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 8-13

            first_number = 1
            second_number = 3
            self.assertEqual(
                src.calculator.add(first_number, second_number),
                first_number+second_number
            )

            first_number = 123456
            second_number = 789012
            self.assertEqual(
                src.calculator.add(first_number, second_number),
                first_number+second_number
            )

  the test is still green

* on to the next :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 8-13

            first_number = 123456
            second_number = 789012
            self.assertEqual(
                src.calculator.add(first_number, second_number),
                first_number+second_number
            )

            first_number = -1
            second_number = 0
            self.assertEqual(
                src.calculator.add(first_number, second_number),
                first_number+second_number
            )

  still green

* and the next

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 8-13

            first_number = -1
            second_number = 0
            self.assertEqual(
                src.calculator.add(first_number, second_number),
                first_number+second_number
            )

            first_number = -2
            second_number = -3
            self.assertEqual(
                src.calculator.add(first_number, second_number),
                first_number+second_number
            )

  green

* more?

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 8-13

            first_number = -2
            second_number = -3
            self.assertEqual(
                src.calculator.add(first_number, second_number),
                first_number+second_number
            )

            first_number = 0.1
            second_number = 1
            self.assertEqual(
                src.calculator.add(first_number, second_number),
                first_number+second_number
            )

  still green

* I add variables_ to the next :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 8-9, 11-12

            first_number = 0.1
            second_number = 1
            self.assertEqual(
                src.calculator.add(first_number, second_number),
                first_number+second_number
            )

            first_number = 0.1
            second_number = 0.2
            self.assertEqual(
                src.calculator.add(first_number, second_number),
                first_number+second_number
            )

  the test is still green

* ah, the last one

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 8-9, 11-12

            first_number = 0.1
            second_number = 0.2
            self.assertEqual(
                src.calculator.add(first_number, second_number),
                first_number+second_number
            )

            first_number = 0.1234
            second_number = -5.6789
            self.assertEqual(
                src.calculator.add(first_number, second_number),
                first_number+second_number
            )


    # TODO

  still green

----

*********************************************************************************
how to use random numbers
*********************************************************************************

All the :ref:`assertions<what is an assertion?>` in :ref:`test_addition` do the same thing

- point ``first_number`` to a value
- point ``second_number`` to a value
- call ``src.calculator.add`` with ``first_number`` and ``second_number`` as input
- check if the result of ``src.calculator.add(first_number, second_number)`` is the same as ``first_number + second_number``

I want to use random numbers for ``first_number`` and ``second_number`` to make sure that the ``add`` :ref:`function<what is a function?>` always returns the result of adding the two numbers without knowing what the numbers are.

I can do this with the `random module`_ from the `Python standard library`_, it is a :ref:`module<what is a module?>` from the `Python standard library`_ that is used to make fake random numbers


* I add an `import statement`_ for the `random module`_ at the top of ``test_calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import random
    import src.calculator
    import unittest

* I use a random value for ``first_number`` in the first :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 2-3

        def test_addition(self):
            # first_number = 0
            first_number = random.triangular(-0.1, 1.0)
            second_number = 1
            self.assertEqual(
                src.calculator.add(first_number, second_number),
                first_number+second_number
            )

  green. `random.triangular`_ returns a random float_ that could be any number from ``-0.1`` to ``1.0`` in this case, I can also use `random.randint`_ if I want a random integer_

* I want to see the test fail to be sure everything works as expected. I change the expectation in the first :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 7

        def test_addition(self):
            # first_number = 0
            first_number = random.triangular(-0.1, 1.0)
            second_number = 1
            self.assertEqual(
                src.calculator.add(first_number, second_number),
                first_number+first_number
            )

  I use (:kbd:`ctrl+s` (Windows_/Linux_) or :kbd:`command+s` (MacOS_)) a few times in the :ref:`editor<2 editors>` to run the tests and the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` with random values that look like this

  .. code-block:: python

    AssertionError: -X.YZABCDEFGHIJKLM != A.BCDEFGHIJKLMNOPQ

  the letters are for random numbers

* I change the expectation of the :ref:`assertion<what is an assertion?>` back to the right calculation

  .. code-block:: python
    :lineno-start: 12
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

* I use the ``Rename Symbol`` feature to change the name of variables_ to say what they are

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

  green

* There is some duplication, If I want to use a different range of random numbers for the test, I have to make a change in more than one place. For example

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 2-3

        def test_addition(self):
            random_first_number = random.triangular(-10.0, 10.0)
            random_second_number = random.triangular(-10.0, 10.0)

  still green

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

* I use the new :ref:`function<what is a function?>` to get random values for the ``random_first_number`` and ``random_second_number`` :ref:`variables<what is a variable?>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 2-5

        def test_addition(self):
            # random_first_number = random.triangular(-10.0, 10.0)
            random_first_number = a_random_number()
            # random_second_number = random.triangular(-10.0, 10.0)
            random_second_number = a_random_number()

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 12

        def test_addition(self):
            random_first_number = a_random_number()
            random_second_number = a_random_number()

* I change the expectation in the :ref:`assertion<what is an assertion?>` to make sure the test works

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 6

            self.assertEqual(
                src.calculator.add(
                    random_first_number,
                    random_second_number
                ),
                random_second_number+random_second_number
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: R.STUVWXYZABCDEFG != H.IJKLMNOPQRSTUVWX

* I undo the change

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 10

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


    # TODO

  the test is green again

* I now only need to change the range of random numbers for the test in one place

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 2

    def a_random_number():
        return random.triangular(-10000.0, 10000.0)

  the test is still green

* I can use any range of numbers the computer can handle, for example

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 2

    def a_random_number():
        return random.triangular(-10.0**100000, 10.0**100000)

  the terminal_ shows OverflowError_

  .. code-block:: python

    OverflowError: (34, 'Numerical result out of range')

  because the numbers are too big

  - ``**`` is the symbol for raise to the power (exponents)
  - ``10.0**100000`` is how to write ``10.0`` raised to the power of ``100,000``

  I make the range smaller

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 2

    def a_random_number():
        return random.triangular(-1000.0, 1000.0)

  the test is still green, though the test takes a little longer to run

* I remove ``test addition`` from the TODO list

  .. code-block:: python
    :lineno-start: 22

    # TODO
    # test subtraction
    # test multiplication
    # test division


    # Exceptions seen

:ref:`I can use a variable to remove duplication<what is a variable?>`

----

*********************************************************************************
test_subtraction
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

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

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: python

  AttributeError: module 'src.calculator' has no attribute 'subtract'

``calculator.py`` in the ``src`` folder_ does not have anything named ``subtract`` in it

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the name to ``calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    def add(first_input, second_input):
        return first_input + second_input


    subtract

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'subtract' is not defined

* I point ``subtract`` to :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 1

    subtract = None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  I have seen this before

* I change ``subtract`` to a :ref:`function<what is a function?>` to make it callable_

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 1-2

    def subtract():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: python

    TypeError: subtract() takes 0 positional arguments but 2 were given

* I make ``subtract`` take inputs

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 1

    def subtract(first_input, second_input):
        return None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != XYZ.ABCDEFGHIJKLMNOP

  ``subtract`` returns :ref:`None<what is None?>`, the test expects

  - ``random_first_number-random_second_number`` which is
  - ``first_input-second_input``
  - the difference between the 2 numbers

* I make the ``subtract`` :ref:`function<what is a function?>` return the difference between the inputs

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2

    def subtract(first_input, second_input):
        return first_input - second_input

  the test passes. SUCCESS!

* I remove ``test subtraction`` from the TODO list in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 37

    # TODO
    # test multiplication
    # test division


    # Exceptions seen

----

*********************************************************************************
test_multiplication
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a failing test for multiplication in ``test_calculator.py``

.. code-block:: python
  :lineno-start: 24
  :emphasize-lines: 13-23

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

        def test_multiplication(self):
            random_first_number = a_random_number()
            random_second_number = a_random_number()

            self.assertEqual(
                src.calculator.multiply(
                    random_first_number,
                    random_second_number
                ),
                random_first_number*random_second_number
            )


    # TODO

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: python

  AttributeError: module 'src.calculator' has no attribute 'multiply'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* Using what I know so far, I add a :ref:`function<what is a function?>` to ``calculator.py``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 5-6

    def subtract(first_input, second_input):
        return first_input - second_input


    def multiply(first_input, second_input):
        return first_input * second_input

  the test passes

* I remove ``test_multiplication`` from the TODO list in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 49

    # TODO
    # test division


    # Exceptions seen

.. NOTE::

  * ``*`` is the symbol for multiplication
  * ``**`` is the symbol for raise to the power (exponent)

----

*********************************************************************************
test_division
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

Time for division. I add a new test to ``test_calculator.py``

.. code-block:: python
  :lineno-start: 36
  :emphasize-lines: 13-23

      def test_multiplication(self):
          random_first_number = a_random_number()
          random_second_number = a_random_number()

          self.assertEqual(
              src.calculator.multiply(
                  random_first_number,
                  random_second_number
              ),
              random_first_number*random_second_number
          )

      def test_division(self):
          random_first_number = a_random_number()
          random_second_number = a_random_number()

          self.assertEqual(
              src.calculator.divide(
                  random_first_number,
                  random_second_number
              ),
              random_first_number/random_second_number
          )


  # TODO
  # test division

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: python

  AttributeError: module 'src.calculator' has no attribute 'divide'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the :ref:`function<what is a function?>` to ``calculator.py``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 5-6

    def multiply(first_input, second_input):
        return first_input * second_input


    def divide(first_input, second_input):
        return first_input / second_input

  the test passes

* I remove the TODO list from ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 48

        def test_division(self):
            random_first_number = a_random_number()
            random_second_number = a_random_number()

            self.assertEqual(
                src.calculator.divide(
                    random_first_number,
                    random_second_number
                ),
                random_first_number/random_second_number
            )


    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

----

*********************************************************************************
:yellow:`REFACTOR`: make it better
*********************************************************************************

* I have some repetition to remove, the code below happens in every test, that is 4 times in ``test_calculator.py``

  .. code-block:: python

    random_first_number = a_random_number()
    random_second_number = a_random_number()

* I add :ref:`class attributes (variables)<test_attribute_error_w_class_attributes>` to remove the repetition and use the same numbers for all the tests

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 3-4

    class TestCalculator(unittest.TestCase):

        random_first_number = a_random_number()
        random_second_number = a_random_number()

        def test_addition(self):

* I use the new :ref:`class attributes<test_attribute_error_w_class_attributes>` in :ref:`test_addition`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 2-5

        def test_addition(self):
            # random_first_number = a_random_number()
            random_first_number = self.random_first_number
            # random_second_number = a_random_number()
            random_second_number = self.random_second_number

            self.assertEqual(

  the test is still green

* I use the :ref:`class attributes<test_attribute_error_w_class_attributes>` for the :ref:`variables<what is a variable?>` in the call to ``src.calculator.add`` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 3-6

            self.assertEqual(
                src.calculator.add(
                    # random_first_number,
                    self.random_first_number,
                    # random_second_number
                    self.random_second_number
                ),
                random_first_number+random_second_number
            )

  still green

* I use the :ref:`class attributes<test_attribute_error_w_class_attributes>` for the :ref:`variables<what is a variable?>` in the expectation of the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 8-9

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

  green

* I remove the commented lines and the ``random_first_number`` and ``random_second_number`` :ref:`variables<what is a variable?>` from :ref:`test_addition`

  .. code-block:: python
    :lineno-start: 15

        def test_addition(self):
            self.assertEqual(
                src.calculator.add(
                    self.random_first_number,
                    self.random_second_number
                ),
                self.random_first_number+self.random_second_number
            )

        def test_subtraction(self):

  still green

----

* I use the new :ref:`class attributes<test_attribute_error_w_class_attributes>` in :ref:`test_subtraction`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 2-5

        def test_subtraction(self):
            # random_first_number = a_random_number()
            random_first_number = self.random_first_number
            # random_second_number = a_random_number()
            random_second_number = self.random_second_number

            self.assertEqual(

  the test is still green

* I use the :ref:`class attributes<test_attribute_error_w_class_attributes>` for the :ref:`variables<what is a variable?>` in the call to ``src.calculator.subtract`` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 3-6

            self.assertEqual(
                src.calculator.subtract(
                    # random_first_number,
                    self.random_first_number,
                    # random_second_number
                    self.random_second_number
                ),
                random_first_number-random_second_number
            )

  still green

* I use the :ref:`class attributes<test_attribute_error_w_class_attributes>` for the :ref:`variables<what is a variable?>` in the expectation of the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 8-9

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

  green

* I remove the commented lines and the ``random_first_number`` and ``random_second_number`` :ref:`variables<what is a variable?>` from :ref:`test_subtraction`

  .. code-block:: python
    :lineno-start: 24

        def test_subtraction(self):
            self.assertEqual(
                src.calculator.subtract(
                    self.random_first_number,
                    self.random_second_number
                ),
                self.random_first_number-self.random_second_number
            )

        def test_multiplication(self):

  still green

----

* I use the new :ref:`class attributes<test_attribute_error_w_class_attributes>` in :ref:`test_multiplication`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2-5

        def test_multiplication(self):
            # random_first_number = a_random_number()
            random_first_number = self.random_first_number
            # random_second_number = a_random_number()
            random_second_number = self.random_second_number

            self.assertEqual(

  the test is still green

* I use the :ref:`class attributes<test_attribute_error_w_class_attributes>` for the :ref:`variables<what is a variable?>` in the call to ``src.calculator.multiply`` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 3-6

            self.assertEqual(
                src.calculator.multiply(
                    # random_first_number,
                    self.random_first_number,
                    # random_second_number
                    self.random_second_number
                ),
                random_first_number*random_second_number
            )

  still green

* I use the :ref:`class attributes<test_attribute_error_w_class_attributes>` for the :ref:`variables<what is a variable?>` in the expectation of the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 8-9

            self.assertEqual(
                src.calculator.multiply(
                    # random_first_number,
                    self.random_first_number,
                    # random_second_number
                    self.random_second_number
                ),
                # random_first_number*random_second_number
                self.random_first_number*self.random_second_number
            )

  green

* I remove the commented lines and the ``random_first_number`` and ``random_second_number`` :ref:`variables<what is a variable?>` from :ref:`test_multiplication`

  .. code-block:: python
    :lineno-start: 33

        def test_multiplication(self):
            self.assertEqual(
                src.calculator.multiply(
                    self.random_first_number,
                    self.random_second_number
                ),
                self.random_first_number*self.random_second_number
            )

        def test_division(self):

  still green

----

* I use the new :ref:`class attributes<test_attribute_error_w_class_attributes>` in :ref:`test_division`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 2-5

        def test_division(self):
            # random_first_number = a_random_number()
            random_first_number = self.random_first_number
            # random_second_number = a_random_number()
            random_second_number = self.random_second_number

            self.assertEqual(

  the test is still green

* I use the :ref:`class attributes<test_attribute_error_w_class_attributes>` for the :ref:`variables<what is a variable?>` in the call to ``src.calculator.divide`` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 3-6

            self.assertEqual(
                src.calculator.divide(
                    # random_first_number,
                    self.random_first_number,
                    # random_second_number
                    self.random_second_number
                ),
                random_first_number/random_second_number
            )

  still green

* I use the :ref:`class attributes<test_attribute_error_w_class_attributes>` for the :ref:`variables<what is a variable?>` in the expectation of the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 8-9

            self.assertEqual(
                src.calculator.divide(
                    # random_first_number,
                    self.random_first_number,
                    # random_second_number
                    self.random_second_number
                ),
                # random_first_number/random_second_number
                self.random_first_number/self.random_second_number
            )

  green

* I remove the commented lines and the ``random_first_number`` and ``random_second_number`` :ref:`variables<what is a variable?>` from :ref:`test_division`

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

  still green

----

All the tests are passing, though they all look the same, :ref:`there has to be a better way<how to make a calculator 2>`.

The ``random_first_number`` and ``random_second_number`` :ref:`variables<what is a variable?>` are made once as :ref:`class attributes<test_attribute_error_w_class_attributes>` and used later in each test with ``self.random_first_number`` and ``self.random_second_number``, the same way I use `unittest.TestCase assert methods`_ like assertEqual_ with ``self.assertEqual``

----

*********************************************************************************
test_calculator_tests
*********************************************************************************

Since everything is green, I can write the program_ that makes the tests pass without looking at the tests

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I close ``test_calculator.py``
* I delete all the text in ``calculator.py``, the terminal_ shows 4 failures

  .. code-block:: shell

    FAILED ... - AttributeError: module 'src.calculator' has no attribute 'add'
    FAILED ... - AttributeError: module 'src.calculator' has no attribute 'divide'
    FAILED ... - AttributeError: module 'src.calculator' has no attribute 'multiply'
    FAILED ... - AttributeError: module 'src.calculator' has no attribute 'subtract'
    =========================== 4 failed in X.YZs ============================

* I start with the last :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'subtract'

What other :ref:`Exceptions<errors>` do you think are raised as I go along?

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the name to ``calculator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    subtract

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'subtract' is not defined

* I point it to :ref:`None<what is None?>` to define it

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    subtract = None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* I change ``subtract`` to a :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def subtract():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: python

    TypeError: subtract() takes 0 positional arguments but 2 were given

* I add :ref:`positional arguments<test_functions_w_positional_arguments>` to the :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def subtract(first_input, second_input):
        return None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` with random numbers

  .. code-block:: python

    AssertionError: None != XYZ.ABCDEFGHIJKLMN

* I change the `return statement`_ to see the difference between the inputs and expected output, remember the :ref:`identity function?<test_identity_function>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def subtract(first_input, second_input):
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` with random numbers that look like this

  .. code-block:: python

    AssertionError: (XYZ.ABCDEFGHIJKLMN, YZA.BCDEFGHIJKLMNO) != ZAB.CDEFGHIJKLMNOP

  the name of the :ref:`function<what is a function?>` is ``subtract`` and the test expects the difference between the 2 inputs

* I make the `return statement`_ match the expectation

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def subtract(first_input, second_input):
        return first_input - second_input

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'multiply'

----

* I add a :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def subtract(first_input, second_input):
        return first_input - second_input


    def multiply():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: python

    TypeError: multiply() takes 0 positional arguments but 2 were given

  I add 2 names for the :ref:`positional arguments<test_functions_w_positional_arguments>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 1

    def multiply(first_input, second_input):
        return None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != XY.ZABCDEFGHIJKLM

* I change the `return statement`_ to see the difference between the inputs and the expected output, this is the :ref:`identity function<test_identity_function>` again

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2

    def multiply(first_input, second_input):
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` with random numbers that look like this

  .. code-block:: python

    AssertionError: (XYZ.ABCDEFGHIJKLMNO, -YZA.BCDEFGHIJKLMNOPQ) != -ZAB.CDEFGHIJKLMNOPQR

* I change it to the multiplication of the inputs to match the name of the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2

    def multiply(first_input, second_input):
        return first_input * second_input

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'divide'

----

* I add another :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 5-6

    def multiply(first_input, second_input):
        return first_input * second_input


    def divide(first_input, second_input):
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` with random numbers that look like this

  .. code-block:: python

    AssertionError: (-XYZ.ABCDEFGHIJKLMNO, YZA.BCDEFGHIJKLMNOPQ) != -ZAB.CDEFGHIJKLMNOPQR

* I change the `return statement`_ to give the test what it wants

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2

    def divide(first_input, second_input):
        return first_input / second_input

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'add'

----

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

  and all the tests are passing with no random failures, :ref:`or are they?<how to make a calculator 3>`

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``calculator.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_ and use :kbd:`q` on the keyboard to leave the tests and the terminal_ goes back to the command line

* I `change directory`_ to the parent of ``calculator``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python

  I am back in the ``pumping_python`` directory_

----

*********************************************************************************
review
*********************************************************************************

I wrote these tests for a program_ that can :ref:`add<test_addition>`, :ref:`subtract<test_subtraction>`, :ref:`multiply<test_multiplication>` and :ref:`divide<test_division>`

* `test_addition`_
* `test_subtraction`_
* `test_multiplication`_
* `test_division`_

I also saw these :ref:`Exceptions<errors>`

* :ref:`AssertionError<what causes AssertionError?>`
* :ref:`NameError<test_catching_name_error_in_tests>`
* :ref:`AttributeError<what causes AttributeError?>`
* :ref:`TypeError<what causes TypeError?>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<how to make a calculator: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

you know a lot, you know

* :ref:`how to make a test driven development environment manually<how to make a test driven development environment>`
* :ref:`how to raise AssertionError with assert methods<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`what causes AttributeError<what causes AttributeError?>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what is None and NOT None<what is None?>`
* :ref:`what is True and False in Python<what are booleans?>`
* :ref:`how to write programs that make decisions<truth table>`
* :ref:`how to make a calculator<how to make a calculator>`

:ref:`Would you like to see a better way to write test_why_use_a_function?<functions 2>`

-----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->