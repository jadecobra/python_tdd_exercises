.. meta::
  :description: Learn Test-Driven Development in Python by building a calculator from scratch. This tutorial covers writing tests, handling exceptions, and refactoring.
  :keywords: Jacob Itegboje, python tdd calculator tutorial, test driven development python example, python calculator tutorial for beginners, python tdd workflow, python unit testing tutorial, how to build a calculator 1n python step-by-step, python test driven development with pytest, python programming projects for beginners

.. include:: ../../links.rst

#################################################################################
how to make a calculator 8
#################################################################################

I can use the ``__getattribute__`` :ref:`method<what is a function?>` that comes with every Python_ :ref:`object<what is a class?>` in the :ref:`calculator<how to make a calculator>` tests

----

*********************************************************************************
open the project
*********************************************************************************

* I `change directory`_ to the ``calculator`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd calculator

  the terminal_ shows I am in the ``calculator`` folder_

  .. code-block:: python

    .../pumping_python/calculator

* I activate the `virtual environment`_

  .. code-block:: python
    :emphasize-lines: 1

    source .venv/bin/activate

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``.venv/bin/activate.ps1`` NOT ``source .venv/bin/activate``

    .. code-block:: Powershell
      :emphasize-lines: 1

      .venv/scripts/activate.ps1

  the terminal_ shows

  .. code-block:: python

    (.venv) .../pumping_python/calculator

* I use ``pytest-watch`` to run the tests

  .. code-block:: python
    :emphasize-lines: 1

    pytest-watch

  the terminal_ shows

  .. code-block:: python
    :emphasize-lines: 4

    rootdir: .../pumping_python/calculator
    collected 6 items

    tests/test_calculator.py ......                                      [100%]

    ============================ 6 passed in X.YZs =============================

* I hold :kbd:`ctrl` on the keyboard and click on ``tests/test_calculator.py`` to open it in the :ref:`editor<2 editors>`

----

*********************************************************************************
test_calculator_w_getattribute
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a test with a :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 9-14

                'multiplication': {
                    'function': src.calculator.multiply,
                    'expectation': (
                        self.random_first_number*self.random_second_number
                    ),
                },
            }

        def test_calculator_w_getattribute(self):
            calculator_tests = {
                'add': (
                    self.random_first_number+self.random_second_number
                )
            }

        def test_calculator_functions(self):

* I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 7-10

        def test_calculator_w_getattribute(self):
            calculator_tests = {
                'add': (
                    self.random_first_number+self.random_second_number
                )
            }
            self.assertEqual(
                src.calculator.__getattribute__('add'),
                calculator_tests['add']
            )

        def test_calculator_functions(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: <function only_takes_numbers.<locals>.wrapper at 0xffff1a2bc3d4> != ABCD.EFGHIJKLMN

  I have to call the :ref:`function<what is a function?>` after ``__getattribute__`` returns it

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add parentheses after to make it a call

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 2
    :emphasize-text: ( )

            self.assertEqual(
                src.calculator.__getattribute__('add')(),
                calculator_tests['add']
            )

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: only_takes_numbers.<locals>.wrapper() missing 2 required positional arguments: 'first_input' and 'second_input'

  I have to give the inputs to the :ref:`function<what is a function?>`

* I add inputs in the parentheses

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 8-11

        def test_calculator_w_getattribute(self):
            calculator_tests = {
                'add': (
                    self.random_first_number+self.random_second_number
                )
            }
            self.assertEqual(
                src.calculator.__getattribute__('add')(
                    self.random_first_number,
                    self.random_second_number
                ),
                calculator_tests['add']
            )

        def test_calculator_functions(self):

  the test passes

  - ``src.calculator.__getattribute__('add')`` returns ``src.calculator.add``
  - ``calculator_tests['add']`` returns ``self.random_first_number + self.random_second_number``
  - ``object.__getattribute__(something)`` checks if ``something`` is in ``object`` and returns it

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add another operation to the ``calculator_tests`` :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines:

        def test_calculator_w_getattribute(self):
            calculator_tests = {
                'add': (
                    self.random_first_number+self.random_second_number
                ),
                'subtract': (
                    self.random_first_number-self.random_second_number
                )
            }
            self.assertEqual(

* I add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 8-14

            self.assertEqual(
                src.calculator.__getattribute__('add')(
                    self.random_first_number,
                    self.random_second_number
                ),
                calculator_tests['add']
            )
            self.assertEqual(
                src.calculator.__getattribute__('subtract')(
                    self.random_first_number,
                    self.random_second_number
                ),
                calculator_tests['add']
            )

        def test_calculator_functions(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: OPQ.RSTUVWXYZABCDE != FGH.IJKLMNOPQRSTUV

* I change the expectation

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 6

                self.assertEqual(
                    src.calculator.__getattribute__('subtract')(
                        self.random_first_number,
                        self.random_second_number
                    ),
                    calculator_tests['subtract']
                )

  the test passes

* I add a `for loop`_

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 9-17

            self.assertEqual(
                src.calculator.__getattribute__('subtract')(
                    self.random_first_number,
                    self.random_second_number
                ),
                calculator_tests['subtract']
            )

            for operation in calculator_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        src.calculator.__getattribute__(operation)(
                            self.random_first_number,
                            self.random_second_number
                        ),
                        1
                    )

        def test_calculator_functions(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-text: operation add subtract

    SUBFAILED(operation='add') tests/test_calculator.py::TestCalculator::test_calculator_w_getattribute - AssertionError: WXY.ZABCDEFGHIJKL != 1
    SUBFAILED(operation='subtract') tests/test_calculator.py::TestCalculator::test_calculator_w_getattribute - AssertionError: MNO.PQRSTUVWXYZAB != 1

* I change the expectation

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 8

            for operation in calculator_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        src.calculator.__getattribute__(operation)(
                            self.random_first_number,
                            self.random_second_number
                        ),
                        calculator_tests[operation]
                    )

  the test passes

* I remove the other :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 48

        def test_calculator_w_getattribute(self):
            calculator_tests = {
                'add': (
                    self.random_first_number+self.random_second_number
                ),
                'subtract': (
                    self.random_first_number-self.random_second_number
                )
            }

            for operation in calculator_tests:
                with self.subTest(operation=operation):
                    self.assertEqual(
                        src.calculator.__getattribute__(operation)(
                            self.random_first_number,
                            self.random_second_number
                        ),
                        calculator_tests[operation]
                    )

        def test_calculator_functions(self):

  the test is still green

* I add a :ref:`key<test_keys_of_a_dictionary>` for the next operation

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 9

        def test_calculator_w_getattribute(self):
            calculator_tests = {
                'add': (
                    self.random_first_number+self.random_second_number
                ),
                'subtract': (
                    self.random_first_number-self.random_second_number
                ),
                'division': self.division_result,
            }

            for operation in calculator_tests:

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'division'

* I used a name that is not in ``calculator.py``. I change the name

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines:

            calculator_tests = {
                'add': (
                    self.random_first_number+self.random_second_number
                ),
                'subtract': (
                    self.random_first_number-self.random_second_number
                ),
                'divide': self.division_result,
            }

  the test passes

* I add another operation

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 9-11

            calculator_tests = {
                'add': (
                    self.random_first_number+self.random_second_number
                ),
                'subtract': (
                    self.random_first_number-self.random_second_number
                ),
                'divide': self.division_result,
                'multiplication': (
                    self.random_first_number*self.random_second_number
                ),
            }

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.calculator' has no attribute 'multiplication'

* I change the name

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 9

            calculator_tests = {
                'add': (
                    self.random_first_number+self.random_second_number
                ),
                'subtract': (
                    self.random_first_number-self.random_second_number
                ),
                'divide': self.division_result,
                'multiply': (
                    self.random_first_number*self.random_second_number
                ),
            }

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_calculator.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_ and exit the tests with :kbd:`ctrl+c` on the keyboard, the terminal_ shows

  .. code-block:: python

    (.venv) .../pumping_python/calculator

* I deactivate the `virtual environment`_

  .. code-block:: python
    :emphasize-lines: 1

    deactivate

  the terminal_ goes back to the command line, ``(.venv)`` is no longer on the left side

  .. code-block:: python

    .../pumping_python/calculator

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

I added the following tests for the :ref:`calculator program<how to make a calculator 5>` with :ref:`dictionaries` which made testing the program easier

* :ref:`test_calculator_w_dictionary_items`
* :ref:`test_calculator_functions` which replaced

  - :ref:`test_addition`
  - :ref:`test_subtraction`
  - :ref:`test_multiplication`
  - :ref:`test_division`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<data structures: dictionaries: tests>`

----

*************************************************************************************
what is next?
*************************************************************************************

you have gone through a lot of things and know

* :ref:`how to make a test driven development environment manually<how to make a test driven development environment>`
* :ref:`how to raise AssertionError with assert methods<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
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
* :ref:`how to make dictionaries with functions<how to make a person>`
* :ref:`what you can do with dictionaries<dictionaries>`
* :ref:`what you can do with classes<what is a class?>`

:ref:`Would you like to know what causes ModuleNotFoundError?<what is a module?>`

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