.. meta::
  :description:
  :keywords:

.. include:: ../../../links.rst

.. _test microwave with dictionaries:

#################################################################################
test microwave with dictionaries
#################################################################################

I want to use a :ref:`generator<generator expressions>` in the :ref:`microwave` project.

*********************************************************************************
preview
*********************************************************************************

This is the test I have at the end of the chapter

.. literalinclude:: ../../../code/microwave/tests/test_microwave_w_dictionaries.py
  :caption: microwave/tests/test_microwave.py
  :language: python
  :linenos:
  :lines: 1-36

----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I change directory_ to the project

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    cd microwave

* I open ``test_microwave.py`` from the ``tests`` folder_
* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    uv run pytest-watcher . --now --patterns "**/*.py"

----

*********************************************************************************
test_microwave with dictionaries
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`generator expression<generator expressions>` for the nested :ref:`for loops<what is a for loop?>` in :ref:`test_microwave<extract test_microwave>`

.. code-block:: python
  :caption: microwave/tests/test_microwave.py
  :lineno-start: 7
  :emphasize-lines: 3-16

      def test_microwave(self):
          booleans = (False, True)
          # for closed_door in booleans:
          #     for timer_set in booleans:
          #         for pressed_start in booleans:
          #             for too_hot in booleans:
          for (
              closed_door, timer_set,
              pressed_start, too_hot,
          ) in (
              (_, _, _, _)
              for _ in booleans
              for _ in booleans
              for _ in booleans
              for _ in booleans
          ):

.. code-block:: python
  :caption: microwave/tests/test_microwave.py
  :lineno-start: 23
  :emphasize-lines: 7

                          with self.subTest(
                              closed_door=closed_door,
                              timer_set=timer_set,
                              pressed_start=pressed_start,
                              too_hot=too_hot,
                          ):
                              raise Exception
                              result = src.microwave.microwave(
                                  closed_door=closed_door,
                                  timer_set=timer_set,
                                  pressed_start=pressed_start,
                                  too_hot=too_hot,
                              )

the terminal_ is my friend, and shows :ref:`Exception<how to raise an Exception>` for sixteen sub tests.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I remove the :ref:`Exception<how to raise an Exception>`

.. code-block:: python
  :caption: microwave/tests/test_microwave.py
  :lineno-start: 23

                          with self.subTest(
                              closed_door=closed_door,
                              timer_set=timer_set,
                              pressed_start=pressed_start,
                              too_hot=too_hot,
                          ):
                              result = src.microwave.microwave(
                                  closed_door=closed_door,
                                  timer_set=timer_set,
                                  pressed_start=pressed_start,
                                  too_hot=too_hot,
                              )

the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I use :ref:`itertools.product<another way to make a generator for nested loops>` for the :ref:`generator expression<generator expressions>`

  .. code-block:: python
    :caption: microwave/tests/test_microwave.py
    :lineno-start: 7
    :emphasize-lines: 2, 7-16

        def test_microwave(self):
            # booleans = (False, True)
            # for closed_door in booleans:
            #     for timer_set in booleans:
            #         for pressed_start in booleans:
            #             for too_hot in booleans:
            # for (
            #     closed_door, timer_set,
            #     pressed_start, too_hot,
            # ) in (
            #     (_, _, _, _)
            #     for _ in booleans
            #     for _ in booleans
            #     for _ in booleans
            #     for _ in booleans
            # ):

  .. code-block:: python
    :caption: microwave/tests/test_microwave.py
    :lineno-start: 23
    :emphasize-lines: 1-4

            for (
                closed_door, timer_set,
                pressed_start, too_hot,
            ) in itertools.product((False, True), repeat=4):
                            with self.subTest(
                                closed_door=closed_door,
                                timer_set=timer_set,
                                pressed_start=pressed_start,
                                too_hot=too_hot,
                            ):

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: shell
    :caption: terminal

    NameError: name 'itertools' is not defined.
               Did you forget to import 'itertools'?

* I add an `import statement`_ for the `itertools library`_

  .. code-block:: python
    :caption: microwave/tests/test_microwave.py
    :linenos:
    :emphasize-lines: 1

    import itertools
    import src.microwave
    import unittest

  the test is green again.

* I remove the commented lines, then fix indentation in :ref:`test_microwave<extract test_microwave>`

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'test_microwave with dictionaries'

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``tests/test_microwave.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests
* I `change directory`_ to the parent of :ref:`microwave`

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

:ref:`Do you want to see all the CODE I typed in this chapter?<test microwave with dictionaries: test>`

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

:ref:`Would you like to test the traffic_light project with dictionaries?<test traffic_light with dictionaries>`

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