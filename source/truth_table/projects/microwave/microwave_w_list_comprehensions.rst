.. REDO::


.. meta::
  :description:
  :keywords:

.. include:: ../../links.rst

.. _microwave with loops:

#################################################################################
test microwave with list comprehensions
#################################################################################

I want to use :ref:`for loops<what is a for loop?>` in the :ref:`microwave` project. It has tests for a **Microwave** with these inputs:

* is the **Microwave** door closed?
* is the timer set?
* is the **Microwave** too hot?
* was the start button pressed?

the inputs gave me this :ref:`truth table`

=============== ==============  ==================  ==================  =============
door            timer           start button        too hot             output
=============== ==============  ==================  ==================  =============
:green:`closed` :green:`set`    :green:`pressed`    :green:`too hot`    :red:`False`
:green:`closed` :green:`set`    :green:`pressed`    :red:`NOT too hot`  :green:`True`
:green:`closed` :green:`set`    :red:`NOT pressed`  :green:`too hot`    :red:`False`
:green:`closed` :green:`set`    :red:`NOT pressed`  :red:`NOT too hot`  :red:`False`
=============== ==============  ==================  ==================  =============

=============== ==============  ==================  ==================  =============
door            timer           start button        too hot             output
=============== ==============  ==================  ==================  =============
:green:`closed` :red:`NOT set`  :green:`pressed`    :green:`too hot`    :red:`False`
:green:`closed` :red:`NOT set`  :green:`pressed`    :red:`NOT too hot`  :red:`False`
:green:`closed` :red:`NOT set`  :red:`NOT pressed`  :green:`too hot`    :red:`False`
:green:`closed` :red:`NOT set`  :red:`NOT pressed`  :red:`NOT too hot`  :red:`False`
=============== ==============  ==================  ==================  =============

=============== ==============  ==================  ==================  =============
door            timer           start button        too hot             output
=============== ==============  ==================  ==================  =============
:red:`open`     :green:`set`    :green:`pressed`    :green:`too hot`    :red:`False`
:red:`open`     :green:`set`    :green:`pressed`    :red:`NOT too hot`  :red:`False`
:red:`open`     :green:`set`    :red:`NOT pressed`  :green:`too hot`    :red:`False`
:red:`open`     :green:`set`    :red:`NOT pressed`  :red:`NOT too hot`  :red:`False`
=============== ==============  ==================  ==================  =============

=============== ==============  ==================  ==================  =============
door            timer           start button        too hot             output
=============== ==============  ==================  ==================  =============
:red:`open`     :red:`NOT set`  :green:`pressed`    :green:`too hot`    :red:`False`
:red:`open`     :red:`NOT set`  :green:`pressed`    :red:`NOT too hot`  :red:`False`
:red:`open`     :red:`NOT set`  :red:`NOT pressed`  :green:`too hot`    :red:`False`
:red:`open`     :red:`NOT set`  :red:`NOT pressed`  :red:`NOT too hot`  :red:`False`
=============== ==============  ==================  ==================  =============

The only time this **Microwave** :green:`heats` up food is when the **Microwave** door is :green:`closed` AND the timer is :green:`set` AND the **Microwave** temperature is :red:`NOT too hot` AND the start button is :green:`pressed`.

*********************************************************************************
preview
*********************************************************************************

These is the test I have at the end of the chapter

.. literalinclude:: ../../../code/microwave/tests/test_microwave_w_loops.py
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
extract test_microwave
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test with :ref:`for loops<what is a for loop?>` for the sixteen cases

.. code-block:: python
  :caption: microwave/tests/test_microwave.py
  :lineno-start: 5
  :emphasize-lines: 3-14

  class TestMicrowave(unittest.TestCase):

      def test_microwave(self):
          booleans = (False, True)
          for closed_door in booleans:
              for timer_set in booleans:
                  for pressed_start in booleans:
                      for too_hot in booleans:
                          with self.subTest(
                              closed_door=closed_door,
                              timer_set=timer_set,
                              pressed_start=pressed_start,
                              too_hot=too_hot,
                          ):

.. code-block:: python
  :caption: microwave/tests/test_microwave.py
  :lineno-start: 19
  :emphasize-lines: 1-7

                              result = src.microwave.microwave(
                                  closed_door=closed_door,
                                  timer_set=timer_set,
                                  pressed_start=pressed_start,
                                  too_hot=too_hot,
                              )
                              self.assertEqual(result, 'BOOM!!!')

      def test_too_hot_w_timer_set_closed_door_pressed_start(self):

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for all sixteen cases.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change ``self.assertEqual(result, 'BOOM!!!')`` to handle all the fifteen cases where the :ref:`microwave` does :red:`NOT heat` up food

  .. code-block:: python
    :caption: microwave/tests/test_microwave.py
    :lineno-start: 19
    :emphasize-lines: 7

                                result = src.microwave.microwave(
                                    closed_door=closed_door,
                                    timer_set=timer_set,
                                    pressed_start=pressed_start,
                                    too_hot=too_hot,
                                )
                                self.assertFalse(result)

        def test_too_hot_w_timer_set_closed_door_pressed_start(self):

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>` for the one case where the :ref:`microwave` will :green:`heat` up food

* I move the :ref:`assertion<what is an assertion?>` into a :ref:`try statement<how to handle Exceptions>` for it

  .. code-block:: python
    :caption: microwave/tests/test_microwave.py
    :lineno-start: 19
    :emphasize-lines: 7-10

                                result = src.microwave.microwave(
                                    closed_door=closed_door,
                                    timer_set=timer_set,
                                    pressed_start=pressed_start,
                                    too_hot=too_hot,
                                )
                                try:
                                    self.assertFalse(result)
                                except AssertionError:
                                    self.assertTrue(result)

        def test_too_hot_w_timer_set_closed_door_pressed_start(self):

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove all the other tests because they are now covered by :ref:`test_microwave<extract test_microwave>`

  .. code-block:: python
    :caption: microwave/tests/test_microwave.py
    :lineno-start: 25

                                try:
                                    self.assertFalse(result)
                                except AssertionError:
                                    self.assertTrue(result)


    # Exceptions seen

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    git commit -am 'extract test_microwave'

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``tests/test_microwave.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests
* I `change directory`_ back to the parent of :ref:`microwave`

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    cd ..

----

*************************************************************************************
review
*************************************************************************************

Another test with nested :ref:`for loops<what is for loop?>`, :ref:`there has to be a better way<test microwave with list comprehensions>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<Microwave: tests and solutions>`

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
* :ref:`I know how Python groups objects into False or True<what are booleans?>`
* :ref:`I know how to make a Python Test Driven Development environment automatically<how to make a Python Test Driven Development environment automatically>`
* :ref:`I know how to write programs that make decisions<truth table>`

:ref:`Would you like to test making a Car starter?<car>`

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