.. meta::
  :description:
  :keywords:

.. include:: ../../../links.rst

.. _test traffic_light with dictionaries:

#################################################################################
test traffic_light with dictionaries
#################################################################################

----

I want to use a :ref:`generator<generator expressions>` in the :ref:`traffic_light` project.

*********************************************************************************
preview
*********************************************************************************

These are the tests I have at the end of the chapter

.. literalinclude:: ../../../code/traffic_light/tests/test_traffic_light_w_dictionaries.py
  :caption: traffic_light/tests/test_traffic_light.py
  :language: python
  :linenos:
  :lines: 1-7

.. literalinclude:: ../../../code/traffic_light/tests/test_traffic_light_w_dictionaries.py
  :caption: traffic_light/tests/test_traffic_light.py
  :language: python
  :lineno-start: 10
  :lines: 10-44

.. literalinclude:: ../../../code/traffic_light/tests/test_traffic_light_w_dictionaries.py
  :caption: traffic_light/tests/test_traffic_light.py
  :language: python
  :lineno-start: 46
  :lines: 46-

----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I `change directory`_ to the :ref:`traffic_light folder<Traffic Light>` in the ``pumping_python`` folder_

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    cd traffic_light

* I open ``test_traffic_light.py`` from the ``tests`` folder_
* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    uv run pytest-watcher . --now --patterns "**/*.py"

----

*********************************************************************************
refactor test_traffic_light_control
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change the :ref:`for loop<what is a for loop?>` in :ref:`test_traffic_light_control` to use names instead of :ref:`list indexes<test_index_returns_first_position_of_item_in_a_list>`

.. code-block:: python
  :caption: traffic_light/tests/test_traffic_light.py
  :lineno-start: 11
  :emphasize-lines: 2-5

      def test_traffic_light_control(self):
          for (
              red_phase, current_parallel,
              current_cross, timer_done, expectation
          ) in (
              ('cross', GREEN, RED, False, (GREEN, RED, WALK)),
              ('cross', GREEN, RED, True, (YELLOW, RED, NOT_WALK)),
              ('cross', YELLOW, RED, False, (YELLOW, RED, NOT_WALK)),

the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

.. code-block:: python
  :caption: terminal

  NameError: name 'row' is not defined

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I comment out the :ref:`variables<what is a variable?>` that use :ref:`list indexes<test_index_returns_first_position_of_item_in_a_list>`

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 26
    :emphasize-lines: 5-8

                ('parallel', RED, YELLOW, True, (RED, RED, NOT_WALK)),
                ('parallel', RED, RED, False, (RED, RED, NOT_WALK)),
                ('parallel', RED, RED, True, (GREEN, RED, WALK)),
            ):
                # red_phase = row[0]
                # current_parallel = row[1]
                # current_cross = row[2]
                # timer_done = row[3]

                with self.subTest(
                    red_phase=red_phase,
                    current_parallel=current_parallel,
                    current_cross=current_cross,
                    timer_done=timer_done,
                ):

  the terminal_ still shows :ref:`NameError<test_catching_name_error>`, this time for twelve sub tests.

* I change ``row[4]`` to ``expectation`` to use the name instead

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 35
    :emphasize-lines: 14

                with self.subTest(
                    red_phase=red_phase,
                    current_parallel=current_parallel,
                    current_cross=current_cross,
                    timer_done=timer_done,
                ):
                    self.assertEqual(
                        src.traffic_light.control(
                            red_phase=red_phase,
                            current_parallel=current_parallel,
                            current_cross=current_cross,
                            timer_done=timer_done,
                        ),
                        expectation
                    )

        def test_traffic_light_failsafe(self):

  the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I remove the commented lines

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 26

            ('parallel', RED, YELLOW, True, (RED, RED, NOT_WALK)),
            ('parallel', RED, RED, False, (RED, RED, NOT_WALK)),
            ('parallel', RED, RED, True, (GREEN, RED, WALK)),
        ):
            with self.subTest(
                red_phase=red_phase,
                current_parallel=current_parallel,
                current_cross=current_cross,
                timer_done=timer_done,
            ):

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'use names with test_traffic_light_control'

----

*********************************************************************************
test_traffic_light_failsafe with dictionaries
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`generator expression<generator expressions>` for the :ref:`for loops<what is a for loop?>` in :ref:`test_traffic_light_failsafe`

.. code-block:: python
  :caption: traffic_light/tests/test_traffic_light.py
  :lineno-start: 45
  :emphasize-lines: 3-16

      def test_traffic_light_failsafe(self):
          inputs = (GREEN, YELLOW, 'bad input')
          # for red_phase in ('cross', 'parallel', 'bad input'):
          #     for current_parallel in inputs:
          #         for current_cross in inputs:
          #             for timer_done in (False, True):
          for (
              red_phase, current_parallel,
              current_cross, timer_done
          ) in (
              (_, _, _, _)
              for _ in ('cross', 'parallel', 'bad input')
              for _ in inputs
              for _ in inputs
              for timer_done in (False, True)
          ):

.. code-block:: python
  :caption: traffic_light/tests/test_traffic_light.py
  :lineno-start: 61
  :emphasize-lines: 7

                          with self.subTest(
                              red_phase=red_phase,
                              current_parallel=current_parallel,
                              current_cross=current_cross,
                              timer_done=timer_done,
                          ):
                              raise Exception
                              self.assertEqual(
                                  src.traffic_light.control(
                                      red_phase=red_phase,
                                      current_parallel=current_parallel,
                                      current_cross=current_cross,
                                      timer_done=timer_done,
                                  ),
                                  (RED, RED, NOT_WALK)
                              )

the terminal_ is my friend, and shows :ref:`Exception<how to raise an Exception>` for fifty four sub tests.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I remove the :ref:`Exception<how to raise an Exception>`

.. code-block:: python
  :caption: traffic_light/tests/test_traffic_light.py
  :lineno-start: 61

                          with self.subTest(
                              red_phase=red_phase,
                              current_parallel=current_parallel,
                              current_cross=current_cross,
                              timer_done=timer_done,
                          ):
                              self.assertEqual(
                                  src.traffic_light.control(
                                      red_phase=red_phase,
                                      current_parallel=current_parallel,
                                      current_cross=current_cross,
                                      timer_done=timer_done,
                                  ),
                                  (RED, RED, NOT_WALK)
                              )

the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I use :ref:`itertools.product<another way to make a generator for nested loops>` for the :ref:`generator expression<generator expressions>`

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 45
    :emphasize-lines: 7-16

        def test_traffic_light_failsafe(self):
            inputs = (GREEN, YELLOW, 'bad input')
            # for red_phase in ('cross', 'parallel', 'bad input'):
            #     for current_parallel in inputs:
            #         for current_cross in inputs:
            #             for timer_done in (False, True):
            # for (
            #     red_phase, current_parallel,
            #     current_cross, timer_done
            # ) in (
            #     (_, _, _, _)
            #     for _ in ('cross', 'parallel', 'bad input')
            #     for _ in inputs
            #     for _ in inputs
            #     for timer_done in (False, True)
            # ):

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 61
    :emphasize-lines: 1-7

            for (
                red_phase, current_parallel,
                current_cross, timer_done
            ) in itertools.product(
                ('cross', 'parallel', 'bad input'),
                inputs, inputs, (False, True),
            ):
                            with self.subTest(
                                red_phase=red_phase,
                                current_parallel=current_parallel,
                                current_cross=current_cross,
                                timer_done=timer_done,
                            ):

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: shell
    :caption: terminal

    NameError: name 'itertools' is not defined.
               Did you forget to import 'itertools'?

* I add an `import statement`_ for the `itertools library`_

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :linenos:
    :emphasize-lines: 1

    import itertools
    import src.traffic_light
    import unittest

  the test is green again.

* I remove the commented lines, then fix indentation in :ref:`test_traffic_light_failsafe`

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'test_traffic_light_failsafe with dictionaries'

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``tests/test_traffic_light.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests
* I `change directory`_ to the parent of :ref:`traffic_light`

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

:ref:`Do you want to see all the CODE I typed in this chapter?<test traffic_light with dictionaries: tests>`

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
* :ref:`I know to use dictionaries<what is a dictionary?>`.

:ref:`Would you like to test binary operations from the truth_table project with dictionaries?<truth table: test binary operations with dictionaries>`

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