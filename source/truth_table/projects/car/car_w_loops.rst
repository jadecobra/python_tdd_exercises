.. meta::
  :description: Pumping Python chapter "test car with loops" by Jacob Itegboje. Continues the Car project: one ``test_car_ignition`` nests four ``for`` loops over ``(False, True)`` for ``start_is_pressed``, ``key_is_close``, ``brake_is_pressed``, and ``in_park``, and names each case with ``unittest`` ``subTest``. ``uv run pytest-watcher . --now`` reports ``SUBFAILED``. ``assertEqual(result, 'BOOM!!!')`` fails all 16 cases: fifteen are ``AssertionError: False != 'BOOM!!!'`` and the all-true case is ``AssertionError: True != 'BOOM!!!'``. ``assertFalse(result)`` leaves one failure, ``AssertionError: True is not false``, when start, key, brake, and park are all true. A ``try`` that catches ``AssertionError`` and then calls ``assertTrue`` makes the loop pass. The other ignition tests are removed because this loop covers them. The review calls the four nested loops ugly and points ahead to fewer loops. Also ``cd car`` and ``git commit -am 'extract test_car_ignition'``.
  :keywords: Jacob Itegboje, Pumping Python, test car with loops, test_car_ignition, nested for loops, unittest subTest, SUBFAILED, assertEqual, BOOM, AssertionError False != 'BOOM!!!', AssertionError True != 'BOOM!!!', True is not false, assertFalse, assertTrue, try except AssertionError, src.car.ignition, start_is_pressed, key_is_close, brake_is_pressed, in_park, pytest-watcher, git commit extract test_car_ignition

.. include:: ../../../links.rst

.. _test car with loops:

#################################################################################
test car with loops
#################################################################################

I want to use :ref:`for loops<what is a for loop?>` in the :ref:`Car` project. It has tests for a :ref:`Car` ignition with these inputs:

* was the start button pressed?
* is the key close to the ignition?
* is the brake being pressed?
* is the car in park?

the inputs gave me this :ref:`truth table`

==============  ==================  ==================  ==================  =============
key             brake               start               gear                output
==============  ==================  ==================  ==================  =============
:green:`close`  :green:`pressed`    :green:`pressed`    :green:`in park`    :green:`True`
:green:`close`  :green:`pressed`    :green:`pressed`    :red:`NOT in park`  :red:`False`
:green:`close`  :red:`NOT pressed`  :green:`pressed`    :green:`in park`    :red:`False`
:green:`close`  :red:`NOT pressed`  :green:`pressed`    :red:`NOT in park`  :red:`False`
==============  ==================  ==================  ==================  =============

================  ==================  ==================  ==================  ============
key               brake               start               gear                output
================  ==================  ==================  ==================  ============
:red:`NOT close`  :green:`pressed`    :green:`pressed`    :green:`in park`    :red:`False`
:red:`NOT close`  :green:`pressed`    :green:`pressed`    :red:`NOT in park`  :red:`False`
:red:`NOT close`  :red:`NOT pressed`  :green:`pressed`    :green:`in park`    :red:`False`
:red:`NOT close`  :red:`NOT pressed`  :green:`pressed`    :red:`NOT in park`  :red:`False`
================  ==================  ==================  ==================  ============

==============  ==================  ==================  ==================  ============
key             brake               start               gear                output
==============  ==================  ==================  ==================  ============
:green:`close`  :green:`pressed`    :red:`NOT pressed`  :green:`in park`    :red:`False`
:green:`close`  :green:`pressed`    :red:`NOT pressed`  :red:`NOT in park`  :red:`False`
:green:`close`  :red:`NOT pressed`  :red:`NOT pressed`  :green:`in park`    :red:`False`
:green:`close`  :red:`NOT pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`False`
==============  ==================  ==================  ==================  ============

================  ==================  ==================  ==================  ============
key               brake               start               gear                output
================  ==================  ==================  ==================  ============
:red:`NOT close`  :green:`pressed`    :red:`NOT pressed`  :green:`in park`    :red:`False`
:red:`NOT close`  :green:`pressed`    :red:`NOT pressed`  :red:`NOT in park`  :red:`False`
:red:`NOT close`  :red:`NOT pressed`  :red:`NOT pressed`  :green:`in park`    :red:`False`
:red:`NOT close`  :red:`NOT pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`False`
================  ==================  ==================  ==================  ============

the only time the :ref:`Car` starts is if the start button is :green:`pressed` AND the key is :green:`close` to the ignition AND the brake is being :green:`pressed` AND the car gear is :green:`in park`.

----

*********************************************************************************
preview
*********************************************************************************

This is the test I have at the end of the chapter

.. literalinclude:: ../../../code/car/tests/test_car_w_loops.py
  :caption: car/tests/test_car_w_loops.py
  :language: python
  :linenos:
  :lines: 1-36

----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I `change directory`_ to the :ref:`car folder<Car>` in the ``pumping_python`` folder_

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    cd car

* I open ``test_car.py`` from the ``tests`` folder_
* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    uv run pytest-watcher . --now

----

*********************************************************************************
extract test_car_ignition
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a test with a :ref:`for loop<what is a for loop?>` for all the cases

  .. code-block:: python
    :caption: car/tests/test_car.py
    :lineno-start: 5
    :emphasize-lines: 3-14

    class TestCar(unittest.TestCase):

        def test_car_ignition(self):
            booleans = (False, True)
            for start_is_pressed in booleans:
                for key_is_close in booleans:
                  for brake_is_pressed in booleans:
                      for in_park in booleans:
                          with self.subTest(
                              start_is_pressed=start_is_pressed,
                              key_is_close=key_is_close,
                              brake_is_pressed=brake_is_pressed,
                              in_park=in_park,
                          ):

  .. code-block:: python
    :caption: car/tests/test_car.py
    :lineno-start: 19
    :emphasize-lines: 1-7

                              result = src.car.ignition(
                                  start_is_pressed=start_is_pressed,
                                  key_is_close=key_is_close,
                                  brake_is_pressed=brake_is_pressed,
                                  in_park=in_park,
                              )
                              self.assertEqual(result, 'BOOM!!!')

        def test_park_w_brake_pressed_key_close_start_pressed(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    SUBFAILED(
        start_is_pressed=False, key_is_close=False,
        brake_is_pressed=False, in_park=False
    ) ... AssertionError: False != 'BOOM!!!'
    SUBFAILED(
        start_is_pressed=False, key_is_close=False,
        brake_is_pressed=False, in_park=True
    ) ... AssertionError: False != 'BOOM!!!'
    SUBFAILED(
        start_is_pressed=False, key_is_close=False,
        brake_is_pressed=True, in_park=False
    ) ... AssertionError: False != 'BOOM!!!'
    SUBFAILED(
        start_is_pressed=False, key_is_close=False,
        brake_is_pressed=True, in_park=True
    ) ... AssertionError: False != 'BOOM!!!'

  .. code-block:: python
    :caption: terminal

    SUBFAILED(
        start_is_pressed=False, key_is_close=True,
        brake_is_pressed=False, in_park=False
    ) ... AssertionError: False != 'BOOM!!!'
    SUBFAILED(
        start_is_pressed=False, key_is_close=True,
        brake_is_pressed=False, in_park=True
    ) ... AssertionError: False != 'BOOM!!!'
    SUBFAILED(
        start_is_pressed=False, key_is_close=True,
        brake_is_pressed=True, in_park=False
    ) ... AssertionError: False != 'BOOM!!!'
    SUBFAILED(
        start_is_pressed=False, key_is_close=True,
        brake_is_pressed=True, in_park=True
    ) ... AssertionError: False != 'BOOM!!!'

  .. code-block:: python
    :caption: terminal

    SUBFAILED(
        start_is_pressed=True, key_is_close=False,
        brake_is_pressed=False, in_park=False
    ) ... AssertionError: False != 'BOOM!!!'
    SUBFAILED(
        start_is_pressed=True, key_is_close=False,
        brake_is_pressed=False, in_park=True
    ) ... AssertionError: False != 'BOOM!!!'
    SUBFAILED(
        start_is_pressed=True, key_is_close=False,
        brake_is_pressed=True, in_park=False
    ) ... AssertionError: False != 'BOOM!!!'
    SUBFAILED(
        start_is_pressed=True, key_is_close=False,
        brake_is_pressed=True, in_park=True
    ) ... AssertionError: False != 'BOOM!!!'

  .. code-block:: python
    :caption: terminal

    SUBFAILED(
        start_is_pressed=True, key_is_close=True,
        brake_is_pressed=False, in_park=False
    ) ... AssertionError: False != 'BOOM!!!'
    SUBFAILED(
        start_is_pressed=True, key_is_close=True,
        brake_is_pressed=False, in_park=True
    ) ... AssertionError: False != 'BOOM!!!'
    SUBFAILED(
        start_is_pressed=True, key_is_close=True,
        brake_is_pressed=True, in_park=False
    ) ... AssertionError: False != 'BOOM!!!'
    SUBFAILED(
        start_is_pressed=True, key_is_close=True,
        brake_is_pressed=True, in_park=True
    ) ... AssertionError: True != 'BOOM!!!'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change ``self.assertEqual(result, 'BOOM!!!')`` to handle the fifteen cases where the ``ignition`` :ref:`function<what is a function?>` returns :red:`False`

  .. code-block:: python
    :caption: car/tests/test_car.py
    :lineno-start: 19
    :emphasize-lines: 7

                              result = src.car.ignition(
                                  start_is_pressed=start_is_pressed,
                                  key_is_close=key_is_close,
                                  brake_is_pressed=brake_is_pressed,
                                  in_park=in_park,
                              )
                              self.assertFalse(result)

        def test_park_w_brake_pressed_key_close_start_pressed(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>` for the one case where the :ref:`Car` starts.

  .. code-block:: python
    :caption: terminal

    SUBFAILED(
        start_is_pressed=True, key_is_close=True,
        brake_is_pressed=True, in_park=True
    ) ... AssertionError: True is not false

* I move the :ref:`assertion<what is an assertion?>` into a :ref:`try statement<how to handle Exceptions>` for it

  .. code-block:: python
    :caption: car/tests/test_car.py
    :lineno-start: 19
    :emphasize-lines: 7-10

                              result = src.car.ignition(
                                  start_is_pressed=start_is_pressed,
                                  key_is_close=key_is_close,
                                  brake_is_pressed=brake_is_pressed,
                                  in_park=in_park,
                              )
                              try:
                                  self.assertFalse(result)
                              except AssertionError:
                                  self.assertTrue(result)

        def test_park_w_brake_pressed_key_close_start_pressed(self):

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove all the other tests because they are now covered by :ref:`test_car_ignition<extract test_car_ignition>`

  .. code-block:: python
    :caption: car/tests/test_car.py
    :lineno-start: 25

                              try:
                                  self.assertFalse(result)
                              except AssertionError:
                                  self.assertTrue(result)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'extract test_car_ignition'

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``tests/test_car.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests
* I `change directory`_ to the parent of :ref:`car`

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    cd ..

----

*************************************************************************************
review
*************************************************************************************

Once again, I used four nested :ref:`for loops<what is a for loop?>` (ugly) to put all the tests together which leaves me with less lines of code and something that is harder to understand.

:ref:`There has to be a better way<test car with list comprehensions>` that does not write this many loops.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<test car with loops: tests>`

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

:ref:`Would you like to test the elevator project with loops?<test elevator with loops>`

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