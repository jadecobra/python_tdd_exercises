.. meta::
  :description:
  :keywords:

.. include:: ../../links.rst

#################################################################################
test telephone with loops
#################################################################################

I want to use the :ref:`for loops<what is a for loop?>` in the :ref:`telephone` project.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/telephone/tests/test_telephone_w_loops.py
  :caption: telephone/tests/test_telephone.py
  :language: python
  :linenos:
  :lines: 1-5

.. literalinclude:: ../../code/telephone/tests/test_telephone_w_loops.py
  :caption: telephone/tests/test_telephone.py
  :language: python
  :lineno-start: 8
  :lines: 8-25

.. literalinclude:: ../../code/telephone/tests/test_telephone_w_loops.py
  :caption: telephone/tests/test_telephone.py
  :language: python
  :lineno-start: 27
  :lines: 27-

----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I change directory_ to the project

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    cd telephone

* I open ``test_telephone.py`` from the ``tests`` folder_
* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    uv run pytest-watcher . --now

----

*********************************************************************************
test_passing_values
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test with a :ref:`for loop<what is a for loop?>` for each one of the values in the tests except :ref:`test_passing_an_object` in ``tests/telephone.py``

.. code-block:: python
  :caption: telephone/tests/test_telephone.py
  :lineno-start: 8
  :emphasize-lines: 4-13

  class TestTelephone(unittest.TestCase):

      def test_passing_values(self):
          for value in (
              None, False, True,
              1234, 5.678, 'hello',
              (0, 1, 2, 'n'), [0, 1, 2, 'n'],
              {0, 1, 2, 'n'},
              {
                  'key0': 'value0',
                  'keyN': [0, 1, 2, 'n'],
              }
          ):

.. code-block:: python
  :caption: telephone/tests/test_telephone.py
  :lineno-start: 21
  :emphasize-lines: 1-5

              with self.subTest(value):
                  self.assertEqual(
                      text(value),
                      f'I got {value}'
                  )

      def test_passing_none(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  SUBFAILED[None] ...
      AssertionError: 'I got: None' != 'I got None'
  SUBFAILED[False] ...
      AssertionError: 'I got: False' != 'I got False'
  SUBFAILED[True] ...
      AssertionError: 'I got: True' != 'I got True'
  SUBFAILED[1234] ...
      AssertionError: 'I got: 1234' != 'I got 1234'
  SUBFAILED[5.678] ...
      AssertionError: 'I got: 5.678' != 'I got 5.678'
  SUBFAILED[hello] ...
      AssertionError: 'I got: hello' != 'I got hello'
  SUBFAILED[(0, 1, 2, 'n')] ...
      AssertionError: "I got: (0, 1, 2, 'n')"
                   != "I got (0, 1, 2, 'n')"
  SUBFAILED[[0, 1, 2, 'n']] ...
      AssertionError: "I got: [0, 1, 2, 'n']"
                   != "I got [0, 1, 2, 'n']"
  SUBFAILED[{0, 1, 2, 'n'}] ...
      AssertionError: "I got: {0, 1, 2, 'n'}"
                   != "I got {0, 1, 2, 'n'}"
  SUBFAILED[{'key0': 'value0', 'keyN': [0, 1, 2, 'n']}] ...
      AssertionError: "I got: {'key0': 'value0', 'keyN': [0, 1, 2, 'n']}"
                   != "I got {'key0': 'value0', 'keyN': [0, 1, 2, 'n']}"

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the expectation of the :ref:`assertion<what is an assertion?>`

.. code-block:: python
  :caption: telephone/tests/test_telephone.py
  :lineno-start: 21
  :emphasize-lines: 4

              with self.subTest(value):
                  self.assertEqual(
                      text(value),
                      f'I got: {value}'
                  )

      def test_passing_none(self):

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the other tests except :ref:`test_passing_an_object` because they are now covered by :ref:`test_passing_values`

  .. code-block:: python

  .. code-block:: python
    :caption: telephone/tests/test_telephone.py
    :lineno-start: 21

                with self.subTest(value):
                    self.assertEqual(
                        text(value),
                        f'I got: {value}'
                    )

        def test_passing_an_object(self):

* I add a git_ commit message in the new terminal_

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'extract test_passing_values'

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_telephone.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests
* I `change directory`_ to the parent of ``telephone``

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    cd ..

----

*********************************************************************************
review
*********************************************************************************

I can use :ref:`for loops<what is a for loop>` to remove repetition.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<test telephone with loops: tests>`

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

:ref:`Would you like to test the traffic_light project with loops?<test traffic_light with loops>`

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