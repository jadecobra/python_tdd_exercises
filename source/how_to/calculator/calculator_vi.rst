.. meta::
  :description: Learn Test-Driven Development in Python by building a calculator from scratch. This tutorial covers writing tests, handling exceptions, and refactoring.
  :keywords: Jacob Itegboje, python tdd calculator tutorial, test driven development python example, python calculator tutorial for beginners, python tdd workflow, python unit testing tutorial, how to build a calculator 1n python step-by-step, python test driven development with pytest, python programming projects for beginners

.. include:: ../../links.rst

#################################################################################
how to make a calculator 6
#################################################################################

I want to use the things I know to make the :ref:`tests for the calculator program<how to make a calculator 4>` better

----

*********************************************************************************
preview
*********************************************************************************

Here are the tests I have by the end of the chapter

.. literalinclude:: ../../code/calculator/tests/test_calculator_list_comprehensions.py
  :language: python
  :linenos:

----

*********************************************************************************
open the project
*********************************************************************************

* I `change directory`_ to the ``calculator`` folder_

  .. code-block:: shell
    :emphasize-lines: 1

    cd calculator

  the terminal_ shows I am in the ``calculator`` folder_

  .. code-block:: shell

    .../pumping_python/calculator

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

* I use ``pytest-watch`` to run the tests

  .. code-block:: shell
    :emphasize-lines: 1

    pytest-watch

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 4

    rootdir: .../pumping_python/calculator
    collected 7 items

    tests/test_calculator.py .......                                     [100%]

    ============================ 7 passed in X.YZs =============================

* I hold :kbd:`ctrl` on the keyboard and click on ``tests/test_calculator.py`` to open it in the :ref:`editor<2 editors>`

----

*********************************************************************************
how to make sure the calculator tests use new numbers for every test
*********************************************************************************

I used the `setUp method`_ in :ref:`list comprehensions` to make sure that I had a new :ref:`list<lists>` and :ref:`iterable<what is an iterable?>` for every test. I want to do the same thing with the :ref:`calculator<how to make a calculator>`, to make sure that each test uses 2 new different random numbers, not the same random numbers for every test



----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

I add the `setUp method`_ to the ``TestCalculator`` :ref:`class<what is a class?>`

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 3-5

  class TestCalculator(unittest.TestCase):

      def setUp(self):
          self.random_first_number = a_random_number()
          self.random_second_number = a_random_number()

      def test_addition(self):

the test is still green. The `setUp method`_ runs before every test, giving ``random_first_number`` and ``random_second_number`` new random values for each test

----

*************************************************************************************
a better way to test the calculator with inputs that are NOT numbers
*************************************************************************************

I tested the :ref:`calculator functions<how to make a calculator>` with :ref:`None<what is None?>`, strings_ and :ref:`lists`, I want to test them with the other :ref:`basic Python data types<data structures>`: :ref:`booleans<what are booleans?>`, tuples_, sets_ and :ref:`dictionaries`.

Since I know how to use a `for loop`_ and :ref:`list comprehensions`, I can do this with one test for all of them instead of a different test for each :ref:`data type<data structures>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new :ref:`assertion<what is an assertion?>` to ``test_calculator_sends_message_when_input_is_not_a_number``

.. code-block:: python
  :lineno-start: 58
  :emphasize-lines: 4-16

      def test_calculator_sends_message_when_input_is_not_a_number(self):
          error_message = 'Excuse me?! Numbers only! try again...'

          for data in (
              None,
              True, False,
              str(),
              tuple(),
              list(),
              set(),
              dict(),
          ):
              self.assertEqual(
                  src.calculator.add(data, a_random_number()),
                  'BOOM!!!'
              )

          self.assertEqual(
              src.calculator.add(None, None),
              error_message
          )

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: 'Excuse me?! Numbers only! try again...' != 'BOOM!!!'

Lovely! The :ref:`if statement<if statements>` in the ``only_takes_numbers`` :ref:`function<what is a function?>` in ``calculator.py`` is doing its job, the :ref:`calculator<how to make a calculator>` only takes numbers

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 3

                self.assertEqual(
                    src.calculator.add(data, a_random_number()),
                    error_message
                )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: ABC.DEFGHIJKLMNOPQR != 'Excuse me?! Numbers only! try again...'

  there is a problem. One of the :ref:`data types<data structures>` I am testing is being allowed by the :ref:`if statement<if statements>`, which means one of them is also an integer_ or is a float_. I need a way to know which one is causing the problem

* the `unittest.TestCase class`_ has a way to tell which item is causing my failure when I am using a loop, I add it to the test

  .. code-block:: python
    :lineno-start: 68
    :emphasize-lines: 3-7

                dict(),
            ):
                with self.subTest(i=data):
                    self.assertEqual(
                        src.calculator.add(data, a_random_number()),
                        error_message
                    )

            self.assertEqual(
                src.calculator.add(None, None),
                error_message
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for two of the :ref:`data types<data structures>` I am testing

  .. code-block:: python
    :emphasize-lines: 3, 4
    :emphasize-text: SUBFAILED True False

    tests/test_calculator.py:72: AssertionError
    ============= short test summary info ==============
    SUBFAILED(i=True) tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: UVW.XYZABCDEFGHIJKL != 'Excuse ...
    SUBFAILED(i=False) tests/test_calculator.py::TestCalculator::test_calculator_sends_message_when_input_is_not_a_number - AssertionError: MNO.PQRSTUVWXYZABCD != 'Excuse ...
    =========== 2 failed, 7 passed in X.YZs ============

  the `unittest.TestCase.subTest method`_ runs the code in its context as a sub test, showing the values I give in ``i=data`` so that I can see which one caused the error

* I add a :ref:`condition<if statements>` for :ref:`booleans<what are booleans?>` in the ``only_takes_numbers`` :ref:`function<what is a function?>` in ``calculator.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3-4

            error_message = 'Excuse me?! Numbers only! try again...'

            if isinstance(first_input, bool) or isinstance(second_input, bool):
                return error_message
            if not (isinstance(first_input, good_types) and isinstance(second_input, good_types)):

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I can use a `for loop`_ to make the :ref:`if statements` simpler

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-9, 11-13, 15-18

    def only_takes_numbers(function):
        def wrapper(first_input, second_input):
            good_types = (int, float)
            error_message = 'brmph?! Numbers only. Try again...'

            # if isinstance(first_input, bool) or isinstance(second_input, bool):
            #     return error_message
            # if not (isinstance(first_input, good_types) and isinstance(second_input, good_types)):
            #     return error_message

            for value in (first_input, second_input):
                if isinstance(value, bool) or not isinstance(value, good_types):
                    return error_message

            try:
                return function(first_input, second_input)
            except TypeError:
                return error_message
        return wrapper

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def only_takes_numbers(function):
        def wrapper(first_input, second_input):
            good_types = (int, float)
            error_message = 'brmph?! Numbers only. Try again...'

            for value in (first_input, second_input):
                if isinstance(value, bool) or not isinstance(value, good_types):
                    return error_message

            try:
                return function(first_input, second_input)
            except TypeError:
                return error_message
        return wrapper

  still green

* I add another :ref:`assertion<what is an assertion?>` for the :ref:`divide function<test_division>` in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 6-9

                with self.subTest(i=data):
                    self.assertEqual(
                        src.calculator.add(data, a_random_number()),
                        error_message
                    )
                    self.assertEqual(
                        src.calculator.divide(data, a_random_number()),
                        'BOOM!!!'
                    )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for all the :ref:`data types<data structures>` in the test

  .. code-block:: python

    AssertionError: 'Excuse me?! Numbers only! try again...' != 'BOOM!!!'

* I think you can tell what will happen next. I change the expectation to match

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 3

                    self.assertEqual(
                        src.calculator.divide(data, a_random_number()),
                        error_message
                    )

  the test passes

* I add an :ref:`assertion<what is an assertion?>` for :ref:`multiplication<test_multiplication>`

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 5-8

                    self.assertEqual(
                        src.calculator.divide(data, a_random_number()),
                        error_message
                    )
                    self.assertEqual(
                        src.calculator.multiply(data, a_random_number()),
                        'BOOM!!!'
                    )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for each :ref:`data type<data structures>`

  .. code-block:: python

    AssertionError: 'Excuse me?! Numbers only! try again...' != 'BOOM!!!'

* I change the expectation

  .. code-block:: python
    :lineno-start: 79
    :emphasize-lines: 3

                    self.assertEqual(
                        src.calculator.multiply(data, a_random_number()),
                        error_message
                    )

  the test passes

* I add an :ref:`assertion<what is an assertion?>` for :ref:`subtraction<test_subtraction>`

  .. code-block:: python
    :lineno-start: 79
    :emphasize-lines: 5-8

                    self.assertEqual(
                        src.calculator.multiply(data, a_random_number()),
                        error_message
                    )
                    self.assertEqual(
                        src.calculator.subtract(data, a_random_number()),
                        'BOOM!!!'
                    )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for all the :ref:`data types<data structures>` I am testing

  .. code-block:: python

    AssertionError: 'Excuse me?! Numbers only! try again...' != 'BOOM!!!'

* I change the expectation to match

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 3

                    self.assertEqual(
                        src.calculator.subtract(data, a_random_number()),
                        error_message
                    )

  the test passes

* I remove the other :ref:`assertions<what is an assertion?>` in the test because they are now covered by the `for loop`_

  .. code-block:: python
    :lineno-start: 58

        def test_calculator_sends_message_when_input_is_not_a_number(self):
            error_message = 'Excuse me?! Numbers only! try again...'

            for data in (
                None,
                True, False,
                str(),
                tuple(),
                list(),
                set(),
                dict(),
            ):
                with self.subTest(i=data):
                    self.assertEqual(
                        src.calculator.add(data, a_random_number()),
                        error_message
                    )
                    self.assertEqual(
                        src.calculator.divide(data, a_random_number()),
                        error_message
                    )
                    self.assertEqual(
                        src.calculator.multiply(data, a_random_number()),
                        error_message
                    )
                    self.assertEqual(
                        src.calculator.subtract(data, a_random_number()),
                        error_message
                    )

        def test_calculator_w_list_items(self):

  Using a `for loop`_ saved me having to write a lot of tests

* I can add more data to the :ref:`iterable<what is an iterable?>` without having to add more tests

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 7-11

        def test_calculator_sends_message_when_input_is_not_a_number(self):
            error_message = 'Excuse me?! Numbers only! try again...'

            for data in (
                None,
                True, False,
                str(), 'text',
                tuple(), (0, 1, 2, 'n'),
                list(), [0, 1, 2, 'n'],
                set(), {0, 1, 2, 'n'},
                dict(), {'key': 'value'},
            ):
                with self.subTest(i=data):

  the test is still green

* I could also write the test with a :ref:`list comprehension<list comprehensions>`, though it looks ugly

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 11-15

                self.assertEqual(
                    src.calculator.subtract(data, a_random_number()),
                    error_message
                )

        [
            self.assertEqual(
                src.calculator.add(data, a_random_number),
                'BOOM!!!'
            ) for data in (
                None, True, False, str(), 'text',
                tuple(), (0, 1, 2, 'n'),
                list(), [0, 1, 2, 'n'],
                set(), {0, 1, 2, 'n'},
                dict(), {'key': 'value'},
            )
        ]

    def test_calculator_w_list_items(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'Excuse me?! Numbers only! try again...' != 'BOOM!!!'

  There are a few problems with doing it this way

  - I make a :ref:`list<lists>` when I do not need it
  - I would not have been able to tell which data type failed since I cannot use the `subTest method`_ with this
  - I would have to repeat all those lines for each :ref:`function<what is a function?>` in the :ref:`calculator program<how to make a calculator>`

* I remove it from the test and things are green again

:ref:`I know a better way to test the calculator with inputs that are NOT numbers<a better way to test the calculator with inputs that are NOT numbers>`

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_calculator.py`` and ``calculator.py`` in the :ref:`editors<2 editors>`
* I click in the terminal_ and exit the tests with :kbd:`ctrl+c` on the keyboard, the terminal_ shows

  .. code-block:: shell

    (.venv) .../pumping_python/calculator

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

I ran tests to show I can make a :ref:`list<lists>` from an :ref:`iterable<what is an iterable?>` with

* :ref:`the list()<test_making_a_list>`
* :ref:`a for loop<test_making_a_list_w_a_for_loop>`
* :ref:`the extend method<test_making_a_list_w_extend>`
* :ref:`list comprehensions<test_making_a_list_w_a_list_comprehension>` where I can

  - :ref:`filter the list based on a condition<test_making_a_list_w_conditions>`
  - :ref:`transform the list with a process<test_making_a_list_w_processes>`
  - :ref:`transform and filter the list<test_making_a_list_w_processes_and_conditions>`

I can use :ref:`functions<what is a function?>` and :ref:`conditions<test_making_a_list_w_conditions>` with :ref:`list comprehensions` to make a :ref:`list<lists>` with one line. I think of it as ``[process(item) for item in iterable if condition/NOT condition]``

I can also do this with :ref:`dictionaries`, it is called a dict comprehension and the syntax is any mix of the following

.. code-block:: python

  {
      a_process(key): another_process(value)
      for key/value in iterable
      if condition/not condition
  }

----

:ref:`How many questions can you answer after going through this chapter?<questions about list comprehensions>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<data structures: list comprehensions: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

you know

* :ref:`how to make a test driven development environment manually<how to make a test driven development environment>`
* :ref:`how to raise AssertionError with assert methods<what causes AssertionError?>`
* :ref:`how to write functions<what is a function?>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what is None and NOT None<what is None?>`
* :ref:`what is True and False in Python<what are booleans?>`
* :ref:`how to write programs that make decisions<truth table>`
* :ref:`how to make a calculator<how to make a calculator>`
* :ref:`how to test that an Exception is raised with assertRaises<how to test that an Exception is raised>`
* :ref:`how to handle Exceptions in programs with try...except...else<how to handle Exceptions (Errors) in programs>`
* :ref:`how to raise TypeError<TypeError>`
* :ref:`what you can do with Lists<lists>`
* :ref:`how to use list comprehensions<list comprehensions>`

:ref:`Would you like to test if a boolean is an integer or a float?<booleans 2>`

-----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please leave a 5 star review. It helps other people get into the book too

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->