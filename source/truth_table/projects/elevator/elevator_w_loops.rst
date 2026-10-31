:orphan:

.. meta::
  :description: Build an elevator controller with Python TDD (Red-Green-Refactor): translate a four-input truth table (floor button pushed, doors closed, above weight limit, emergency) into ``src.elevator.controller`` that returns True only when the button is pushed AND doors are closed AND not above weight AND emergency is not pushed. Beginners use uv, unittest, and pytest-watcher; hit NameError, AttributeError, TypeError (unexpected keywords / missing args), SyntaxError (non-default after default), and AssertionError; learn default parameters, keyword calls, nested if / Logical Negation (NOT) / Logical Conjunction (AND), and assertTrue/assertFalse until only that one row of the 16-row table moves the elevator.
  :keywords: Jacob Itegboje, Python elevator controller project, TDD Red Green Refactor, truth table to code, unittest assertTrue assertFalse, uv package manager, pytest-watcher, number_pushed, doors_closed, above_weight, emergency, default parameters, keyword arguments, SyntaxError parameter without a default, TypeError unexpected keyword argument, NameError src not defined, AttributeError, Logical Negation NOT, Logical Conjunction AND, if statements, failsafe logic, pumping python

.. include:: ../../../links.rst

.. _elevator:

#################################################################################
test elevator with loops
#################################################################################

I want to use :ref:`for loops<what is a for loop?>` in the :ref:`elevator` project. It has tests for an **Elevator Controller** that will :green:`MOVE` the **Elevator Car** to a floor when I push a button for the floor based on these inputs:

* was the number for a floor pushed?
* are the doors closed?
* is it above the weight limit?
* was the emergency button pushed?

the inputs gave me this :ref:`truth table`

=================  ===============  ============== =================  =============
floor button       doors            weight limit   emergency button   output
=================  ===============  ============== =================  =============
:green:`pushed`    :green:`closed`  :green:`above` :green:`pushed`    :red:`False`
:green:`pushed`    :green:`closed`  :green:`above` :red:`NOT pushed`  :red:`False`
:green:`pushed`    :green:`closed`  :red:`below`   :green:`pushed`    :red:`False`
:green:`pushed`    :green:`closed`  :red:`below`   :red:`NOT pushed`  :green:`True`
=================  ===============  ============== =================  =============

=================  ===============  ============== =================  =============
floor button       doors            weight limit   emergency button   output
=================  ===============  ============== =================  =============
:green:`pushed`    :red:`open`      :green:`above` :green:`pushed`    :red:`False`
:green:`pushed`    :red:`open`      :green:`above` :red:`NOT pushed`  :red:`False`
:green:`pushed`    :red:`open`      :red:`below`   :green:`pushed`    :red:`False`
:green:`pushed`    :red:`open`      :red:`below`   :red:`NOT pushed`  :red:`False`
=================  ===============  ============== =================  =============

=================  ===============  ============== =================  =============
floor button       doors            weight limit   emergency button   output
=================  ===============  ============== =================  =============
:red:`NOT pushed`  :green:`closed`  :green:`above` :green:`pushed`    :red:`False`
:red:`NOT pushed`  :green:`closed`  :green:`above` :red:`NOT pushed`  :red:`False`
:red:`NOT pushed`  :green:`closed`  :red:`below`   :green:`pushed`    :red:`False`
:red:`NOT pushed`  :green:`closed`  :red:`below`   :red:`NOT pushed`  :red:`False`
=================  ===============  ============== =================  =============

=================  ===============  ============== =================  =============
floor button       doors            weight limit   emergency button   output
=================  ===============  ============== =================  =============
:red:`NOT pushed`  :red:`open`      :green:`above` :green:`pushed`    :red:`False`
:red:`NOT pushed`  :red:`open`      :green:`above` :red:`NOT pushed`  :red:`False`
:red:`NOT pushed`  :red:`open`      :red:`below`   :green:`pushed`    :red:`False`
:red:`NOT pushed`  :red:`open`      :red:`below`   :red:`NOT pushed`  :red:`False`
=================  ===============  ============== =================  =============

The only time this elevator :green:`moves` up or down is when the button for a floor is :green:`pushed` AND the doors are :green:`closed` AND the **Elevator** is :red:`NOT above` the weight limit, and the emergency button is :red:`NOT pushed`.

*********************************************************************************
preview
*********************************************************************************

These is the test I have at the end of the chapter

.. literalinclude:: ../../../code/elevator/tests/test_elevator_w_loops.py
  :caption: elevator/tests/test_elevator.py
  :language: python
  :linenos:

----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I `change directory`_ to the :ref:`elevator folder<elevator>` in the ``pumping_python`` folder_

  .. code-block:: python
    :caption: terminal
    emphasize-lines: 1

    cd elevator

* I open ``test_elevator.py`` from the ``tests`` folder_
* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    uv run pytest-watcher . --now

----

*********************************************************************************
extract test_elevator_controller
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test with a :ref:`for loop<what is a for loop?>` for all the cases

.. code-block:: python
  :caption: elevator/tests/test_elevator.py
  :lineno-start: 5
  :emphasize-lines: 3-12

  class TestElevator(unittest.TestCase):

      def test_elevator_controller(self):
          booleans = (False, True)
          for number_pushed in booleans:
              for doors_closed in booleans:
                  for above_weight in booleans:
                      for emergency in booleans:
                          with self.subTest(
                              number_pushed=number_pushed,
                              doors_closed=doors_closed,
                              above_weight=above_weight,
                              emergency=emergency,
                          ):

.. code-block:: python
  :caption: elevator/tests/test_elevator.py
  :lineno-start: 5
  :emphasize-lines: 1-7

                              result = src.elevator.controller(
                                  number_pushed=number_pushed,
                                  doors_closed=doors_closed,
                                  above_weight=above_weight,
                                  emergency=emergency,
                              )
                              self.assertEqual(result, 'BOOM!!!')

      def test_above_weight_doors_closed_number_pushed(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  SUBFAILED(
      number_pushed=False, doors_closed=False,
      above_weight=False, emergency=False
  ) ... AssertionError: False != 'BOOM!!!'
  SUBFAILED(
      number_pushed=False, doors_closed=False,
      above_weight=False, emergency=True
  ) ... AssertionError: False != 'BOOM!!!'
  SUBFAILED(
      number_pushed=False, doors_closed=False,
      above_weight=True, emergency=False
  ) ... AssertionError: False != 'BOOM!!!'
  SUBFAILED(
      number_pushed=False, doors_closed=False,
      above_weight=True, emergency=True
  ) ... AssertionError: False != 'BOOM!!!'

.. code-block:: python
  :caption: terminal

  SUBFAILED(
      number_pushed=False, doors_closed=True,
      above_weight=False, emergency=False
  ) ... AssertionError: False != 'BOOM!!!'
  SUBFAILED(
      number_pushed=False, doors_closed=True,
      above_weight=False, emergency=True
  ) ... AssertionError: False != 'BOOM!!!'
  SUBFAILED(
      number_pushed=False, doors_closed=True,
      above_weight=True, emergency=False
  ) ... AssertionError: False != 'BOOM!!!'
  SUBFAILED(
      number_pushed=False, doors_closed=True,
      above_weight=True, emergency=True
  ) ... AssertionError: False != 'BOOM!!!'

.. code-block:: python
  :caption: terminal

  SUBFAILED(
      number_pushed=True, doors_closed=False,
      above_weight=False, emergency=False
  ) ... AssertionError: False != 'BOOM!!!'
  SUBFAILED(
      number_pushed=True, doors_closed=False,
      above_weight=False, emergency=True
  ) ... AssertionError: False != 'BOOM!!!'
  SUBFAILED(
      number_pushed=True, doors_closed=False,
      above_weight=True, emergency=False
  ) ... AssertionError: False != 'BOOM!!!'
  SUBFAILED(
      number_pushed=True, doors_closed=False,
      above_weight=True, emergency=True
  ) ... AssertionError: False != 'BOOM!!!'

.. code-block:: python
  :caption: terminal

  SUBFAILED(
      number_pushed=True, doors_closed=True,
      above_weight=False, emergency=False
  ) ... AssertionError: True != 'BOOM!!!'
  SUBFAILED(
      number_pushed=True, doors_closed=True,
      above_weight=False, emergency=True
  ) ... AssertionError: False != 'BOOM!!!'
  SUBFAILED(
      number_pushed=True, doors_closed=True,
      above_weight=True, emergency=False
  ) ... AssertionError: False != 'BOOM!!!'
  SUBFAILED(
      number_pushed=True, doors_closed=True,
      above_weight=True, emergency=True
  ) ... AssertionError: False != 'BOOM!!!'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change ``self.assertEqual(result, 'BOOM!!!')`` to handle the fifteen cases where the ``controller`` :ref:`functions<what is a function?>` returns :red:`False`

  .. code-block:: python
    :caption: elevator/tests/test_elevator.py
    :lineno-start: 19
    :emphasize-lines: 7

                                result = src.elevator.controller(
                                    number_pushed=number_pushed,
                                    doors_closed=doors_closed,
                                    above_weight=above_weight,
                                    emergency=emergency,
                                )
                                self.assertFalse(result)

        def test_above_weight_doors_closed_number_pushed(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    SUBFAILED(
        number_pushed=True, doors_closed=True,
        above_weight=False, emergency=False
    ) ... AssertionError: True is not false

* I move the :ref:`assertion<what is an assertion?>` into a :ref:`try statement<how to handle Exceptions>` for it

  .. code-block:: python
    :caption: elevator/tests/test_elevator.py
    :lineno-start: 19
    :emphasize-lines: 7-10

                              result = src.elevator.controller(
                                  number_pushed=number_pushed,
                                  doors_closed=doors_closed,
                                  above_weight=above_weight,
                                  emergency=emergency,
                              )
                              try:
                                  self.assertFalse(result)
                              except AssertionError:
                                  self.assertTrue(result)

      def test_above_weight_doors_closed_number_pushed(self):

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove all the other tests because they are now covered by :ref:`test_elevator_controller<extract test_elevator_controller>`

  .. code-block:: python
    :caption: elevator/tests/test_elevator.py
    :lineno-start: 25

                                try:
                                    self.assertFalse(result)
                                except AssertionError:
                                    self.assertTrue(result)


    # Exceptions seen

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'extract test_elevator_controller'

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``tests/test_elevator.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests
* I `change directory`_ to the parent of :ref:`elevator`

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    cd ..

----

*************************************************************************************
review
*************************************************************************************

I also used four nested :ref:`for loops<what is a for loop?>` to make one test for all sixteen cases. :ref:`There has to be a better way<test elevator with list comprehensions>` that looks better.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<test elevator with loops: test>`

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
* :ref:`I know that everything in Python is an object<everything is an object>`.
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

:ref:`Would you like to test the functions project with loops?<test functions with loops>`

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