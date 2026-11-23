.. meta::
  :description: Beginner Python TDD tutorial (Jacob Itegboje, Pumping Python): test atm with dictionaries in the atm project. Continues the Automated Teller Machine truth table from test atm with generators. Open existing project with uv run pytest-watcher . --now. Add a denials dictionary mapping card_expired, above_daily_limit, not_right_pin, and not_enough_cash to their denial messages in test_atm. RED: set expectation from denials[...] or 'CASH' in each if/elif/else branch and add self.assertEqual(result, 'BOOM!!!'); terminal shows AssertionError for all 16 subtests. GREEN: change 'BOOM!!!' to expectation so the test passes. REFACTOR: remove the per-branch self.assertEqual calls so one self.assertEqual(result, expectation) covers all 16 cases; observe the test is slower due to dictionary lookup. Git commit 'test_atm with dictionaries'.
  :keywords: Jacob Itegboje, Pumping Python, test atm with dictionaries, Automated Teller Machine, ATM project, Python dictionary, dict lookup, denials dictionary, expectation variable, itertools.product, subTest, 16 subtests, AssertionError, unittest assertEqual, uv run pytest-watcher, pytest-watcher, withdraw, truth table, red green refactor

.. include:: ../../../links.rst

.. _test atm with dictionaries:

#################################################################################
test atm with dictionaries
#################################################################################


I want to use a :ref:`dictionary<what is a dictionary?>` in the :ref:`atm<Automated Teller Machine>` project.

----

*********************************************************************************
preview
*********************************************************************************

This is the test I have at the end of the chapter

.. literalinclude:: ../../../code/atm/tests/test_atm_w_dictionaries.py
  :caption: atm/tests/test_atm.py
  :language: python
  :linenos:
  :lines: 1-51

----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I `change directory`_ to the :ref:`atm folder<Automated Teller Machine>` in the ``pumping_python`` folder_

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    cd atm

* I open ``test_atm.py`` from the ``tests`` folder_
* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    uv run pytest-watcher . --now

----

*********************************************************************************
test_atm with dictionaries
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a :ref:`dictionary<what is a dictionary?>` for the denials to :ref:`test_atm<extract test_atm>`

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 8
    :emphasize-lines: 2-7

        def test_atm(self):
            denials = {
                'card_expired': 'DENIED: Card Expired',
                'above_daily_limit': 'DENIED: Exceeded daily withdrawal limit',
                'not_right_pin': 'DENIED: Wrong PIN. Try again...',
                'not_enough_cash': 'DENIED: Not enough CASH in Account',
            }

            for (
                right_pin, enough_cash,
                above_daily_limit, card_expired
            ) in itertools.product((False, True), repeat=4):

* I add :ref:`assertions<what is an assertion?>` for the :ref:`values<test_values_of_a_dictionary>` of the ``denials`` :ref:`dictionary<what is a dictionary?>`

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 32
    :emphasize-lines: 2, 8

                      if card_expired:
                          expectation = denials['card_expired']
                          self.assertEqual(
                              result,
                              'DENIED: Card Expired'
                          )
                      elif above_daily_limit:
                          expectation = denials['above_daily_limit']
                          self.assertEqual(
                              result,
                              'DENIED: Exceeded daily withdrawal limit'
                          )

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 44
    :emphasize-lines: 2, 8

                      elif not right_pin:
                          expectation = denials['not_right_pin']
                          self.assertEqual(
                              result,
                              'DENIED: Wrong PIN. Try again...'
                          )
                      elif not enough_cash:
                          expectation = denials['not_enough_cash']
                          self.assertEqual(
                              result,
                              'DENIED: '
                              'Not enough CASH in Account'
                          )

  .. code-block:: python
    :lineno-start: 57
    :caption: atm/tests/test_atm.py
    :emphasize-lines: 2, 7

                      else:
                          expectation = 'CASH'
                          self.assertEqual(
                              result,
                              'CASH'
                          )
                      self.assertEqual(result, 'BOOM!!!')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>` for sixteen sub tests.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the expectation of the new :ref:`assertion<what is an assertion?>` to the new :ref:`variable<what is a variable?>`

.. code-block:: python
  :caption: atm/tests/test_atm.py
  :lineno-start: 57
  :emphasize-lines: 7

                    else:
                        expectation = 'CASH'
                        self.assertEqual(
                            result,
                            'CASH'
                        )
                    self.assertEqual(result, expectation)


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the other :ref:`assertions<what is an assertion?>` because they are now covered by the new :ref:`variable<what is a variable?>`

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 32

                      if card_expired:
                          expectation = denials['card_expired']
                      elif above_daily_limit:
                          expectation = denials['above_daily_limit']
                      elif not right_pin:
                          expectation = denials['not_right_pin']
                      elif not enough_cash:
                          expectation = denials['not_enough_cash']
                      else:
                          expectation = 'CASH'

                      self.assertEqual(result, expectation)


    # Exceptions seen

  the test passes and is slower than when I did not have a :ref:`dictionary<what is a dictionary?>` to check for the values of the denial message.

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'test_atm with dictionaries'

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``tests/test_atm.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests
* I `change directory`_ to the parent of :ref:`atm`

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    cd ..

----

*************************************************************************************
review
*************************************************************************************

In this case adding a :ref:`dictionary<what is a dictionary?>` makes the test slower than what I had before because it adds an extra step to the process - it has to look up the :ref:`value<test_values_of_a_dictionary>` of a denial.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<test atm with dictionaries: test>`

----

*************************************************************************************
what is next?
*************************************************************************************

* :ref:`I know how to make a Python Test Driven Development environment manually<how to make a Python Test Driven Development environment manually>`.
* :ref:`I know what a Python module is<what is a module?>`.
* :ref:`I know how to run tests automatically<how to run tests automatically>`.
* :ref:`I know what an assertion is<what is an assertion?>`.
* :ref:`I know how to make functions<what is a function?>`.
* :ref:`I know how to make a person with strings<how to make a person with strings>`.
* :ref:`I know how to make functions that take input<functions that take input>`.
* :ref:`I know what causes TypeError<what causes TypeError?>`.
* :ref:`I know how to place values in strings<telephone>`.
* :ref:`I know how to make a person say hello with f-strings<how to make a person with f-strings>`.
* :ref:`I know how to separate tests from solutions<separate and equal>`.
* :ref:`I know what causes AttributeError<what causes AttributeError?>`.
* :ref:`I know how to make a person with an object<how to make a person with an object>`.
* :ref:`I know that everything in Python is an object<what is an object?>`.
* :ref:`I know how to use the unittest library<another way to write tests>`.
* :ref:`I know how to use the datetime library<test person with datetime>`.
* :ref:`I know what None is<what is None?>`.
* :ref:`I know how to make a person with conditions<how to make a person with conditions>`.
* :ref:`I know how Python groups objects into False or True<what are booleans?>`.
* :ref:`I know how to make a Python Test Driven Development environment automatically<how to make a Python Test Driven Development environment automatically>`.
* :ref:`I know how to write programs that make decisions<truth table>`.
* :ref:`I know how to make a Python Test Driven Development environment automatically with variables<how to make a Python Test Driven Development environment automatically with variables>`.
* :ref:`I know how to make a person with Exceptions<how to make a person with Exceptions>`.
* :ref:`I know how to test that an Exception is raised<how to test that an Exception is raised>`.
* :ref:`I know how to use Exception handlers in programs<how to handle Exceptions in programs>`.
* :ref:`I know how to make a person with loops<how to make a person with loops>`.
* :ref:`I know how to use lists<what is a list?>`.
* :ref:`I know how to use list comprehensions<what is a list comprehension?>`.
* :ref:`I know how to use dictionaries<what is a dictionary?>`.

:ref:`Would you like to use a dictionary in the person project?<test microwave with dictionaries>`

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