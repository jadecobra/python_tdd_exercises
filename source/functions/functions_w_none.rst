.. meta::
  :description:
  :keywords:

.. include:: ../links.rst

#################################################################################
test functions with assertIsNotNone and assertIsNone
#################################################################################

I want to use the :ref:`assertIsNotNone<another way to test if something is NOT None>` and :ref:`assertIsNone methods<another way to test if something is None>` for the :ref:`assertions<what is a function?>` that check if the result of a :ref:`function call<how to call a function>` is :ref:`None<what is None?>`.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../code/functions/tests/test_functions_w_none.py
  :language: python
  :linenos:

----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I change directory_ to the project

  .. code-block:: python
    :emphasize-lines: 1

    cd functions

  the terminal_ shows I am in the ``functions`` folder_

  .. code-block:: python

    .../pumping_python/functions

* I open ``test_functions.py``

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: python

    test_functions.py ............                      [100%]

    =================== 12 passed in J.KLs ===================

----

*********************************************************************************
test_making_a_function_w_pass with assertIsNone
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`call<how to call a function with input>` to :ref:`assertIsNotNone<another way to test if something is NOT None>` in :ref:`test_making_a_function_w_pass`

.. code-block:: python
  :lineno-start: 5

  class TestFunctions(unittest.TestCase):

      first = 'first'
      last = 'last'
      a_tuple = (0, 1, 2, 'n')
      a_list = [0, 1, 2, 'n']
      a_set = {0, 1, 2, 'n'}
      a_dictionary = {'key': 'value'}

.. code-block:: python
  :lineno-start: 14
  :emphasize-lines: 6

      def test_making_a_function_w_pass(self):
          result = src.functions.w_pass()

          assert result is None
          self.assertIs(result, None)
          self.assertIsNotNone(result)

      def test_making_a_function_w_return(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: unexpectedly None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`assertIsNotNone<another way to test if something is NOT None>` to :ref:`assertIsNone<another way to test if something is None>`

.. code-block:: python
  :lineno-start: 14
  :emphasize-lines: 6-7

      def test_making_a_function_w_pass(self):
          result = src.functions.w_pass()

          assert result is None
          self.assertIs(result, None)
          # self.assertIsNotNone(result)
          self.assertIsNone(result)

      def test_making_a_function_w_return(self):

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line, ``assert result is None`` and ``self.assertIs(result, None)``

  .. code-block:: python
    :lineno-start: 14

        def test_making_a_function_w_pass(self):
            result = src.functions.w_pass()
            self.assertIsNone(result)

        def test_making_a_function_w_return(self):

* I no longer need the ``result`` :ref:`variable<what is a variable?>` since it is only used once. I :ref:`call<how to call a function>` ``src.functions.w_pass`` directly

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 2-4

        def test_making_a_function_w_pass(self):
            # result = src.functions.w_pass()
            # self.assertIsNone(result)
            self.assertIsNone(src.functions.w_pass())

        def test_making_a_function_w_return(self):

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 14

        def test_making_a_function_w_pass(self):
            self.assertIsNone(src.functions.w_pass())

        def test_making_a_function_w_return(self):

----

*********************************************************************************
test_making_a_function_w_return with assertIsNone
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`call<how to call a function with input>` to :ref:`assertIsNotNone<another way to test if something is NOT None>` in :ref:`test_making_a_function_w_return`

.. code-block:: python
  :lineno-start: 17
  :emphasize-lines: 6

      def test_making_a_function_w_return(self):
          result = src.functions.w_return()

          assert result is None
          self.assertIs(result, None)
          self.assertIsNotNone(result)

      def test_making_a_function_w_return_none(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: unexpectedly None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`assertIsNotNone<another way to test if something is NOT None>` to :ref:`assertIsNone<another way to test if something is None>`

.. code-block:: python
  :lineno-start: 17
  :emphasize-lines: 6-7

      def test_making_a_function_w_return(self):
          result = src.functions.w_return()

          assert result is None
          self.assertIs(result, None)
          # self.assertIsNotNone(result)
          self.assertIsNone(result)

      def test_making_a_function_w_return_none(self):

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line, ``assert result is None`` and ``self.assertIs(result, None)``

  .. code-block:: python
    :lineno-start: 17

        def test_making_a_function_w_return(self):
            result = src.functions.w_return()
            self.assertIsNone(result)

        def test_making_a_function_w_return_none(self):

* I :ref:`call<how to call a function>` ``src.functions.w_return`` directly

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 2-4

        def test_making_a_function_w_return(self):
            # result = src.functions.w_return()
            # self.assertIsNone(result)
            self.assertIsNone(src.functions.w_return())

        def test_making_a_function_w_return_none(self):

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 17

        def test_making_a_function_w_return(self):
            self.assertIsNone(src.functions.w_return())

        def test_making_a_function_w_return_none(self):

----

*********************************************************************************
test_making_a_function_w_return_none with assertIsNone
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`call<how to call a function with input>` to :ref:`assertIsNotNone<another way to test if something is NOT None>` in :ref:`test_making_a_function_w_return_none`

.. code-block:: python
  :lineno-start: 20
  :emphasize-lines: 6

      def test_making_a_function_w_return_none(self):
          result = src.functions.w_return_none()

          assert result is None
          self.assertIs(result, None)
          self.assertIsNotNone(result)

      def test_what_happens_after_functions_return(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: unexpectedly None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`assertIsNotNone<another way to test if something is NOT None>` to :ref:`assertIsNone<another way to test if something is None>`

.. code-block:: python
  :lineno-start: 20
  :emphasize-lines: 6-7

      def test_making_a_function_w_return_none(self):
          result = src.functions.w_return_none()

          assert result is None
          self.assertIs(result, None)
          # self.assertIsNotNone(result)
          self.assertIsNone(result)

      def test_what_happens_after_functions_return(self):

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line, ``assert result is None`` and ``self.assertIs(result, None)``

  .. code-block:: python
    :lineno-start: 20

        def test_making_a_function_w_return_none(self):
            result = src.functions.w_return_none()
            self.assertIsNone(result)

        def test_what_happens_after_functions_return(self):

* I no longer need the ``result`` :ref:`variable<what is a variable?>` since it is only used once

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 2-6

        def test_making_a_function_w_return_none(self):
            # result = src.functions.w_return_none()
            # self.assertIsNone(result)
            self.assertIsNone(
                src.functions.w_return_none()
            )

        def test_what_happens_after_functions_return(self):

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 20

        def test_making_a_function_w_return_none(self):
            self.assertIsNone(
                src.functions.w_return_none()
            )

        def test_what_happens_after_functions_return(self):

----

*********************************************************************************
test_what_happens_after_functions_return with assertIsNone
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`call<how to call a function with input>` to :ref:`assertIsNotNone<another way to test if something is NOT None>` in :ref:`test_what_happens_after_functions_return`

.. code-block:: python
  :lineno-start: 25
  :emphasize-lines: 6

      def test_what_happens_after_functions_return(self):
          result = src.functions.return_leaves_the_function()

          assert result is None
          self.assertIs(result, None)
          self.assertIsNotNone(result)

      def test_constant_function(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: unexpectedly None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`assertIsNotNone<another way to test if something is NOT None>` to :ref:`assertIsNone<another way to test if something is None>`

.. code-block:: python
  :lineno-start: 25
  :emphasize-lines: 6-7

      def test_what_happens_after_functions_return(self):
          result = src.functions.return_leaves_the_function()

          assert result is None
          self.assertIs(result, None)
          # self.assertIsNotNone(result)
          self.assertIsNone(result)

      def test_constant_function(self):

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line, ``assert result is None`` and ``self.assertIs(result, None)``

  .. code-block:: python
    :lineno-start: 25

        def test_what_happens_after_functions_return(self):
            result = src.functions.return_leaves_the_function()
            self.assertIsNone(result)

        def test_constant_function(self):

* I no longer need the ``result`` :ref:`variable<what is a variable?>` since it is only used once. I :ref:`call<how to call a function>` ``src.functions.return_leaves_the_function`` directly

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 2-6

        def test_what_happens_after_functions_return(self):
            # result = src.functions.return_leaves_the_function()
            # self.assertIsNone(result)
            self.assertIsNone(
                src.functions.return_leaves_the_function()
            )

        def test_constant_function(self):

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 25

        def test_what_happens_after_functions_return(self):
            self.assertIsNone(
                src.functions.return_leaves_the_function()
            )

        def test_constant_function(self):

----

*********************************************************************************
test identity with assertIsNone
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`call<how to call a function with input>` to :ref:`assertIsNotNone<another way to test if something is NOT None>` in :ref:`test_what_happens_after_functions_return`

.. code-block:: python
  :lineno-start: 25
  :emphasize-lines: 6

      def test_what_happens_after_functions_return(self):
          result = src.functions.return_leaves_the_function()

          assert result is None
          self.assertIs(result, None)
          self.assertIsNotNone(result)

      def test_constant_function(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: unexpectedly None

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`assertIsNotNone<another way to test if something is NOT None>` to :ref:`assertIsNone<another way to test if something is None>`

.. code-block:: python
  :lineno-start: 25
  :emphasize-lines: 6-7

      def test_what_happens_after_functions_return(self):
          result = src.functions.return_leaves_the_function()

          assert result is None
          self.assertIs(result, None)
          # self.assertIsNotNone(result)
          self.assertIsNone(result)

      def test_constant_function(self):

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line, ``assert result is None`` and ``self.assertIs(result, None)``

  .. code-block:: python
    :lineno-start: 25

        def test_what_happens_after_functions_return(self):
            result = src.functions.return_leaves_the_function()
            self.assertIsNone(result)

        def test_constant_function(self):

* I no longer need the ``result`` :ref:`variable<what is a variable?>` since it is only used once. I :ref:`call<how to call a function>` ``src.functions.return_leaves_the_function`` directly

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 2-6

        def test_what_happens_after_functions_return(self):
            # result = src.functions.return_leaves_the_function()
            # self.assertIsNone(result)
            self.assertIsNone(
                src.functions.return_leaves_the_function()
            )

        def test_constant_function(self):

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 25

        def test_what_happens_after_functions_return(self):
            self.assertIsNone(
                src.functions.return_leaves_the_function()
            )

        def test_constant_function(self):

* I open a new terminal_ then change directories to ``functions``

  .. code-block:: python
    :emphasize-lines: 1

    cd functions

* I add a git_ commit message in the new terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'use assertIsNone'

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_functions.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``functions``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

----

*********************************************************************************
review
*********************************************************************************

I can use :ref:`assertIsNone methods<another way to test if something is None>` and :ref:`assertIsNotNone<another way to test if something is NOT None>` for :ref:`assertions<what is an assertion?>` that test if something is :ref:`None<what is None?>` or not - ``assertIs(x, None)`` and ``assertIsNot(x, None)``.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<test functions with assertIsNotNone and assertIsNone: tests>`

----

*************************************************************************************
what is next?
*************************************************************************************

So far, I know

* :ref:`how to make a Python test driven development environment manually`
* :ref:`what a Python module is<what is a module?>`
* :ref:`how to run tests automatically`
* :ref:`what an assertion is<what is an assertion?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to make a person with strings`
* :ref:`how to make functions that take input<functions that take input>`
* :ref:`what causes TypeError<what causes TypeError?>`
* :ref:`how to place values in strings<telephone>`
* :ref:`how to make a person say hello with f-strings<how to make a person with f-strings>`
* :ref:`how to separate tests from solutions<separate and equal>`
* :ref:`what causes AttributeError<what causes AttributeError?>`
* :ref:`how to make a person with a class<how to make a person with a class>`
* :ref:`that everything in Python is an object<everything is an object>`
* :ref:`how to use the unittest library<another way to write tests>`
* :ref:`how to calculate age with the datetime library<test person with datetime>`
* :ref:`what None is<what is None?>`

:ref:`Would you like to test the person project with conditions?<test person with conditions>`

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