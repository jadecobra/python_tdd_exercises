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
    collected 7 items

    tests/test_calculator.py .......                                     [100%]

    ============================ 7 passed in X.YZs =============================

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

* I add a test with a :ref:`dictionary<what is a dictionary>`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 9-14

                'exponent': {
                    'function': src.calculator.square,
                    'expectation': (
                        self.random_first_number**self.random_second_number
                    )
                },
            }

        def test_calculator_w_getattribute(self):
            calculator_tests = {
                'add': (
                    self.random_first_number+self.random_second_number
                )
            }

        def test_calculator_functions(self):

* I add 

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

If this has been a 7 star experience for you, please leave a 5 star review. It helps other people get into the book too

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->