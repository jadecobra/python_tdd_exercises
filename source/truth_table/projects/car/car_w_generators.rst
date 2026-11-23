.. meta::
  :description: Beginner Python TDD tutorial (Jacob Itegboje, Pumping Python): test car with generators in the car project. Continues the Car truth table (test_car_ignition). Open existing project with uv run pytest-watcher . --now". Refactor four nested for loops over booleans (start_is_pressed, key_is_close, brake_is_pressed, in_park) into a generator expression using placeholder variable _ to unpack tuples. RED: add raise Exception inside with self.subTest to verify all 16 subtests fail. GREEN: remove raise Exception to make tests pass. REFACTOR: replace the generator expression with itertools.product((False, True), repeat=4). Terminal shows NameError: name 'itertools' is not defined (Did you forget to import 'itertools'?). Add import itertools at the top of tests/test_car.py, remove booleans and commented lines, and fix indentation. Git commit 'test_car_ignition with generators'.
  :keywords: Jacob Itegboje, Pumping Python, test car with generators, Car project, test_car_ignition, generator expressions, itertools.product, repeat parameter, nested for loops, subTest, 16 subtests, NameError name itertools is not defined, raise Exception, uv run pytest-watcher, pytest-watcher, python tdd generator, src.car.ignition, truth table, red green refactor

.. include:: ../../../links.rst

.. _test car with generators:

#################################################################################
test car with generators
#################################################################################

I want to use a :ref:`generator<generator expressions>` in the :ref:`Car` project.

----

*********************************************************************************
preview
*********************************************************************************

This is the test I have at the end of the chapter

.. literalinclude:: ../../../code/car/tests/test_car_w_generators.py
  :caption: car/tests/test_car.py
  :language: python
  :linenos:
  :lines: 1-36

----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I `change directory`_ to the :ref:`car folder<Car Ignition>` in the ``pumping_python`` folder_

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    cd car

* I open ``test_car.py`` from the ``tests`` folder_
* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    uv run pytest-watcher . --now"

----

*********************************************************************************
test_car_ignition with generators
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`generator expression<generator expressions>` for the :ref:`for loops<what is a for loop?>` in :ref:`test_car_ignition<extract test_car_ignition>`

.. code-block:: python
  :caption: car/tests/test_car.py
  :lineno-start: 7
  :emphasize-lines: 3-16

      def test_car_ignition(self):
          booleans = (False, True)
          # for start_is_pressed in booleans:
          #     for key_is_close in booleans:
          #       for brake_is_pressed in booleans:
          #           for in_park in booleans:
          for (
              start_is_pressed, key_is_close,
              brake_is_pressed, in_park
          ) in (
              (_, _, _, _)
              for _ in booleans
              for _ in booleans
              for _ in booleans
              for _ in booleans
          ):

.. code-block:: python
  :caption: car/tests/test_car.py
  :lineno-start: 23
  :emphasize-lines: 7

                        with self.subTest(
                            start_is_pressed=start_is_pressed,
                            key_is_close=key_is_close,
                            brake_is_pressed=brake_is_pressed,
                            in_park=in_park,
                        ):
                            raise Exception
                            result = src.car.ignition(
                                start_is_pressed=start_is_pressed,
                                key_is_close=key_is_close,
                                brake_is_pressed=brake_is_pressed,
                                in_park=in_park,
                            )

the terminal_ shows :ref:`Exception<how to raise an Exception>` for sixteen sub tests.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I remove the :ref:`Exception<how to raise an Exception>`

.. code-block:: python
  :caption: car/tests/test_car.py
  :lineno-start: 23

                        with self.subTest(
                            start_is_pressed=start_is_pressed,
                            key_is_close=key_is_close,
                            brake_is_pressed=brake_is_pressed,
                            in_park=in_park,
                        ):
                            result = src.car.ignition(
                                start_is_pressed=start_is_pressed,
                                key_is_close=key_is_close,
                                brake_is_pressed=brake_is_pressed,
                                in_park=in_park,
                            )

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I use :ref:`itertools.product<another way to make a generator for nested loops>` in place of the :ref:`generator expression<generator expressions>`

  .. code-block:: python
    :caption: car/tests/test_car.py
    :lineno-start: 7
    :emphasize-lines: 7-16

        def test_car_ignition(self):
            booleans = (False, True)
            # for start_is_pressed in booleans:
            #     for key_is_close in booleans:
            #       for brake_is_pressed in booleans:
            #           for in_park in booleans:
            # for (
            #     start_is_pressed, key_is_close,
            #     brake_is_pressed, in_park
            # ) in (
            #     (_, _, _, _)
            #     for _ in booleans
            #     for _ in booleans
            #     for _ in booleans
            #     for _ in booleans
            # ):

  .. code-block:: python
    :caption: car/tests/test_car.py
    :lineno-start: 23
    :emphasize-lines: 1-4

            for (
                start_is_pressed, key_is_close,
                brake_is_pressed, in_park
            ) in itertools.product((False, True), repeat=4):
                          with self.subTest(
                              start_is_pressed=start_is_pressed,
                              key_is_close=key_is_close,
                              brake_is_pressed=brake_is_pressed,
                              in_park=in_park,
                          ):

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: shell
    :caption: terminal

     NameError: name 'itertools' is not defined.
                Did you forget to import 'itertools'?

* I add an `import statement`_ at the top of the file_

  .. code-block:: python
    :caption: car/tests/test_car.py
    :linenos:
    :emphasize-lines: 1

    import itertools
    import src.car
    import unittest

  the test is green again.

* I remove the ``booleans`` :ref:`variable<what is a variable?>` and commented lines, then fix indentation in :ref:`test_car_ignition<extract test_car_ignition>`

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'test_car_ignition with generators'

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

I can use a :ref:`generator expression<generator expressions>` or `itertools.product`_ for nested :ref:`for loops<what is a for loop?>`.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<test car with generators: test>`

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

:ref:`Would you like to test the Elevator project with generators?<test elevator with generators>`

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