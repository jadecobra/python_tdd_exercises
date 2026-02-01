.. meta::
  :description: Learn Test-Driven Development in Python by building a calculator from scratch. This tutorial covers writing tests, handling exceptions, and refactoring.
  :keywords: Jacob Itegboje, python tdd calculator tutorial, test driven development python example, python calculator tutorial for beginners, python tdd workflow, python unit testing tutorial, how to build a calculator 1n python step-by-step, python test driven development with pytest, python programming projects for beginners

.. include:: ../links.rst

#################################################################################
how to make a calculator 2
#################################################################################

I want to use assertRaises_ to make sure :ref:`test_division` from the :ref:`calculator project<how to make a calculator>` raises :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>`

*********************************************************************************
preview
*********************************************************************************

These are the tests I have by the end of the chapter

.. literalinclude:: ../code/calculator/tests/test_calculator_exceptions_tests.py
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

    pytest-watcher . --now

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 4

    rootdir: .../pumping_python/calculator
    collected 4 items

    tests/test_calculator.py ....                                        [100%]

    ============================ 4 passed in X.YZs =============================

* I hold :kbd:`ctrl` on the keyboard and click on ``tests/test_calculator.py`` to open it in the :ref:`editor<2 editors>`

*********************************************************************************
test catching ZeroDivisionError in test_calculator.py
*********************************************************************************


----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new :ref:`assertion<what is an assertion?>` to show that the ``divide`` :ref:`function<what is a function?>` raises :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>` in

.. code-block:: python
  :lineno-start: 42
  :emphasize-lines: 9

      def test_division(self):
          self.assertEqual(
              src.calculator.divide(
                  self.random_first_number,
                  self.random_second_number
              ),
              self.random_first_number/self.random_second_number
          )
          src.calculator.divide(self.random_first_number, 0)


  # Exceptions seen

the terminal_ shows :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>`

.. code-block:: shell

  ZeroDivisionError: float division by zero

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add assertRaises_

.. code-block:: python
  :lineno-start: 48
  :emphasize-lines: 3-4

              self.random_first_number/self.random_second_number
          )
          with self.assertRaises(ZeroDivisionError):
              src.calculator.divide(self.random_first_number, 0)


  # Exceptions seen

the test passes

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_calculator.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_ and use :kbd:`ctrl+c` on the keyboard to leave the tests, the terminal_ shows

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

I can use assertRaises_ to catch :ref:`Exceptions<errors>` in tests and tested the following

* :ref:`ModuleNotFoundError<what is a module?>`
* :ref:`NameError<test_catching_name_error_in_tests>`
* :ref:`AttributeError<what causes AttributeError?>`
* :ref:`TypeError`
* :ref:`IndexError<test_index_error>`
* :ref:`KeyError<test_key_error>`
* :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>` and
* :ref:`The Mother of all Exceptions<test_catching_exceptions_in_tests>`

----

:ref:`How many questions can you answer after going through this chapter?<questions about testing Exceptions>`

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
* :ref:`how to make a Python Test Driven Development environment automatically` or :ref:`how to make a Python Test Driven Development environment automatically on Windows without Windows Subsystem for Linux` and
* :ref:`how to test that an Exception is raised with assertRaises<how to test that an Exception is raised>`

:ref:`Would you like to test handling Exceptions in programs?<how to handle Exceptions (Errors) in programs>`

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