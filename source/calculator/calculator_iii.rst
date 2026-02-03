.. meta::
  :description: Learn Test-Driven Development in Python by building a calculator from scratch. This tutorial covers writing tests, handling exceptions, and refactoring.
  :keywords: Jacob Itegboje, python tdd calculator tutorial, test driven development python example, python calculator tutorial for beginners, python tdd workflow, python unit testing tutorial, how to build a calculator 1n python step-by-step, python test driven development with pytest, python programming projects for beginners

.. include:: ../links.rst

#################################################################################
how to make a calculator 3
#################################################################################

I want the :ref:`divide function<test_division>` in the :ref:`calculator project<how to make a calculator>` to return ``undefined`` when :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>` is raised so that the program_ can continue to work after ``0`` is given as the second number

----

*********************************************************************************
preview
*********************************************************************************

These are the tests I have by the end of the chapter

.. literalinclude:: ../code/calculator/tests/test_calculator_exceptions_programs.py
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

* I use ``pytest-watcher`` to run the tests

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 5

    rootdir: .../pumping_python/calculator
    configfile: pyproject.toml
    collected 4 items

    tests/test_calculator.py ....                                        [100%]

    ======================== 4 passed in X.YZs =========================

* I hold :kbd:`ctrl` on the keyboard and click on ``tests/test_calculator.py`` to open it in the :ref:`editor<2 editors>`

----

*********************************************************************************
test_division_handles_zero_division_error
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change the last :ref:`assertion<what is an assertion?>` in ``test_division``

.. code-block:: python
  :lineno-start: 42
  :emphasize-lines: 9-12

      def test_division(self):
          self.assertEqual(
              src.calculator.divide(
                  self.random_first_number,
                  self.random_second_number
              ),
              self.random_first_number/self.random_second_number
          )
          self.assertEqual(
              src.calculator.divide(self.random_first_number, 0),
              'brmph?! cannot divide by 0. Try again...'
          )


  # Exceptions seen

the terminal_ shows :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>`

.. code-block:: shell

  ZeroDivisionError: float division by zero

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add it to the list of :ref:`Exceptions<errors>` seen in ``test_calculator.py``

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 6

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # ZeroDivisionError

* I open ``calculator.py`` from the ``src`` folder_ in the :ref:`editor<2 editors>`
* I add an :ref:`exception handler<how to use try...except...else>` to the ``divide`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2-5

    def divide(first_input, second_input):
        try:
            return first_input / second_input
        except ZeroDivisionError:
            return 'brmph?! cannot divide by 0. Try again...'

  the test passes.

There is a problem, the test uses random numbers, which means at some point ``random_second_number`` will have a value of ``0`` and the first part of ``test_division`` will raise :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a `return statement`_ to the ``a_random_number`` :ref:`function<what is a function?>` in ``test_calculator.py`` to make it happen

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 2

    def a_random_number():
        return 0
        return random.triangular(-1000.0, 1000.0)

  the terminal_ shows :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>`

  .. code-block:: shell
    :emphasize-lines: 1

    >           self.random_first_number/self.random_second_number
            )
    E       ZeroDivisionError: division by zero

  the expectation calculation in ``test_division`` divides by ``0`` when ``random_second_number`` is ``0`` but the result should be ``'brmph?! cannot divide by 0. Try again...'``

* I add an :ref:`exception handler<how to use try...except...else>` to the test

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 2-14

      def test_division(self):
          try:
              self.assertEqual(
                  src.calculator.divide(
                      self.random_first_number,
                      self.random_second_number
                  ),
                  self.random_first_number/self.random_second_number
              )
          except ZeroDivisionError:
              self.assertEqual(
                  src.calculator.divide(self.random_first_number, 0),
                  'brmph?! cannot divide by 0. Try again...'
              )

  the test passes

* I remove the `return statement`_ from ``a_random_number`` to go back to testing with a range of numbers

  .. code-block:: python
    :linenos:

    import random
    import src.calculator
    import unittest


    def a_random_number():
        return random.triangular(-1000.0, 1000.0)


    class TestCalculator(unittest.TestCase):

  the test is still green

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_calculator.py`` and ``calculator.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_ and use :kbd:`ctrl+c` on the keyboard to leave the tests, the terminal_ shows

  .. code-block:: shell

    (.venv) ...\pumping_python\calculator

* I deactivate the `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    deactivate

  the terminal_ goes back to the command line, ``(.venv)`` is no longer on the left side

  .. code-block:: shell

    ...\pumping_python\calculator

* I `change directory`_ to the parent of ``calculator``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    ...\pumping_python

  I am back in the ``pumping_python`` directory_

----

*********************************************************************************
review
*********************************************************************************

I ran tests to show that

* I can cause any :ref:`Exception<errors>` I want with the raise_ keyword
* I can use the `assertRaises method`_ to catch :ref:`Exceptions<errors>` in tests and tested the following

  - :ref:`ModuleNotFoundError<what is a module?>`
  - :ref:`NameError<test_catching_name_error_in_tests>`
  - :ref:`AttributeError<what causes AttributeError?>`
  - :ref:`TypeError`
  - :ref:`IndexError<test_index_error>`
  - :ref:`KeyError<test_key_error>`
  - :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>`
  - :ref:`The Mother of all Exceptions<test_catching_exceptions_in_tests>`

* I can use assertRaisesRegex_ to catch :ref:`Exceptions<errors>` with messages
* I can use :ref:`try..except...else<how to use try...except...else>` to make programs that can choose what to do when :ref:`Exceptions<errors>` are raised

----

:ref:`How many questions can you answer after going through this chapter?<questions about handling Exceptions>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<how to handle Exceptions (Errors): tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

you know

* :ref:`how to make a test driven development environment manually<how to make a test driven development environment>`
* :ref:`how to raise AssertionError with assert methods<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`what causes AttributeError<what causes AttributeError?>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what is None and NOT None<what is None?>`
* :ref:`what is True and False in Python<what are booleans?>`
* :ref:`how to write programs that make decisions<truth table>`
* :ref:`how to make a calculator<how to make a calculator>`
* :ref:`how to make a Python Test Driven Development environment automatically` or :ref:`how to make a Python Test Driven Development environment automatically on Windows without Windows Subsystem for Linux`
* :ref:`how to test that an Exception is raised with assertRaises<how to test that an Exception is raised>`
* :ref:`how to handle Exceptions in programs with try...except...else<how to handle Exceptions (Errors) in programs>`

:ref:`Would you like to test TypeError?<TypeError>`

-----

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