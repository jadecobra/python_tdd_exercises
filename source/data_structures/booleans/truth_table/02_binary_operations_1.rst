.. meta::
  :description: Master Python truth tables for binary operations. This guide simplifies 'if' statements with clear, step-by-step Python code examples. Watch the tutorial!
  :keywords: Jacob Itegboje, python truth table for if statements, python truth table generator from expression, python logical operators truth table, python truth table for two variables, how to make a truth table in python, python contradiction function, python logical conjunction truth table

.. include:: ../../../links.rst

.. _binary_operations_i:

#################################################################################
truth table: Binary Operations part 1
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/Q_jhE204MoE?si=m9_EvOX-4lrmSzo7" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

There are 16 binary operations, they all take 2 inputs and each of the inputs can be :ref:`True <test_what_is_true>` or :ref:`False <test_what_is_false>`. This gives four cases or ways the inputs can be given to the operation

* :ref:`True <test_what_is_true>`, :ref:`True <test_what_is_true>`
* :ref:`True <test_what_is_true>`, :ref:`False <test_what_is_false>`
* :ref:`False <test_what_is_false>`, :ref:`True <test_what_is_true>`
* :ref:`False <test_what_is_false>`, :ref:`False <test_what_is_false>`

*********************************************************************************
requirements
*********************************************************************************

:ref:`truth table: Nullary and Unary Operations`

----

*********************************************************************************
test_contradiction
*********************************************************************************
=================================================================================
RED: make it fail
=================================================================================

I add a new TestCase_ to ``test_truth_table.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 25, 27-28

  import unittest
  import src.truth_table


  class TestNullaryOperations(unittest.TestCase):

      def test_logical_true(self):
          self.assertTrue(src.truth_table.logical_true())

      def test_logical_false(self):
          self.assertFalse(src.truth_table.logical_false())


  class TestUnaryOperations(unittest.TestCase):

      def test_logical_identity(self):
          self.assertTrue(src.truth_table.logical_identity(True))
          self.assertFalse(src.truth_table.logical_identity(False))

      def test_logical_negation_aka_not(self):
          self.assertFalse(src.truth_table.logical_negation(True))
          self.assertTrue(src.truth_table.logical_negation(False))


  class TestBinaryOperations(unittest.TestCase):

      def test_contradiction(self):
          self.assertFalse(src.truth_table.contradiction(True, True))


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'contradiction'
=================================================================================
GREEN: make it pass
=================================================================================

I add a :ref:`function<functions>` definition to ``truth_table.py``

.. code-block:: python
  :lineno-start: 13
  :emphasize-lines: 5-6

  def logical_negation(the_input):
      return not the_input


  def contradiction(the_input):
      return not the_input

the terminal_ shows :ref:`TypeError`

.. code-block:: shell

  TypeError: contradiction() takes 1 positional argument but 2 were given

I add ``q`` as the second name in parentheses then change ``argument`` to ``p`` for the first input given when the :ref:`function<functions>` is called by the test

.. code-block:: python
  :lineno-start: 17
  :emphasize-lines: 1-2

  def contradiction(first_input, second_input):
      return not first_input

the test passes
=================================================================================
REFACTOR: make it better
=================================================================================

* I add the second case to ``test_contradiction`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 3

        def test_contradiction(self):
            self.assertFalse(src.truth_table.contradiction(True, True))
            self.assertFalse(src.truth_table.contradiction(True, False))

  the test is still green

* I add the next case

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 4


        def test_contradiction(self):
            self.assertFalse(src.truth_table.contradiction(True, True))
            self.assertFalse(src.truth_table.contradiction(True, False))
            self.assertFalse(src.truth_table.contradiction(False, True))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: True is not false

  all three cases of the test expect :ref:`False<test_what_is_false>`

* I change the `return statement`_ in the ``contradiction`` :ref:`function<functions>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 2

    def contradiction(first_input, second_input):
        return False

  the test is green again

* I add the fourth case to ``test_contradiction`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 5

        def test_contradiction(self):
            self.assertFalse(src.truth_table.contradiction(True, True))
            self.assertFalse(src.truth_table.contradiction(True, False))
            self.assertFalse(src.truth_table.contradiction(False, True))
            self.assertFalse(src.truth_table.contradiction(False, False))


    # Exceptions Encountered

  the test is still green! :ref:`Contradiction<test_contradiction>` always returns :ref:`False<test_what_is_false>`

----

*********************************************************************************
test_logical_conjunction
*********************************************************************************
=================================================================================
RED: make it fail
=================================================================================

I add a new test in ``test_truth_table.py``

.. code-block:: python
  :lineno-start: 30
  :emphasize-lines: 4-5

            self.assertFalse(src.truth_table.contradiction(False, True))
            self.assertFalse(src.truth_table.contradiction(False, False))

        def test_logical_conjunction(self):
            self.assertTrue(src.truth_table.logical_conjunction(True, True))


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'logical_conjunction'. Did you mean: 'logical_negation'?
=================================================================================
GREEN: make it pass
=================================================================================

I add the :ref:`function<functions>` in ``truth_table.py``

.. code-block:: python
  :lineno-start: 17
  :emphasize-lines: 5-6

  def contradiction(first_input, second_input):
      return False


  def logical_conjunction(first_input, second_input):
      return True

the test passes
=================================================================================
REFACTOR: make it better
=================================================================================

* I add the next case to ``test_logical_conjunction`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 3

        def test_logical_conjunction(self):
            self.assertTrue(src.truth_table.logical_conjunction(True, True))
            self.assertFalse(src.truth_table.logical_conjunction(True, False))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: True is not false

* I make the ``logical_conjunction`` :ref:`function<functions>` in ``truth_table.py`` return :ref:`False <test_what_is_false>`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2

    def logical_conjunction(first_input, second_input):
        return False
        return True

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: False is not true

  The line that was passing before is now failing

* ``logical_conjunction`` has to choose whether to return :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>` based on the inputs. I can make it do that with `if statements`_

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2-4

    def logical_conjunction(first_input, second_input):
        if first_input == True:
            if second_input == False:
                return False
        return True

  the test passes.  The :ref:`function<functions>` returns :ref:`False<test_what_is_false>` when ``p`` is :ref:`True<test_what_is_true>` and ``q`` is :ref:`False<test_what_is_false>`,  otherwise it returns :ref:`True<test_what_is_true>`

* I add the next case to ``test_logical_conjunction`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 4

        def test_logical_conjunction(self):
            self.assertTrue(src.truth_table.logical_conjunction(True, True))
            self.assertFalse(src.truth_table.logical_conjunction(True, False))
            self.assertFalse(src.truth_table.logical_conjunction(False, True))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: True is not false

  I add another `if statement`_ to ``logical_conjunction`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2-4

    def logical_conjunction(first_input, second_input):
        if first_input == False:
            if second_input == True:
                return False
        if first_input == True:
            if second_input == False:
                return False
        return True

  the test passes

* I add the last case to ``test_logical_conjunction`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 5

        def test_logical_conjunction(self):
            self.assertTrue(src.truth_table.logical_conjunction(True, True))
            self.assertFalse(src.truth_table.logical_conjunction(True, False))
            self.assertFalse(src.truth_table.logical_conjunction(False, True))
            self.assertFalse(src.truth_table.logical_conjunction(False, False))


    # Exceptions Encountered

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: True is not false

* I add an `if statement`_ for the new case to ``logical_conjunction`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 3-4

    def logical_conjunction(first_input, second_input):
        if first_input == False:
            if second_input == False:
                return False
            if second_input == True:
                return False
        if first_input == True:
            if second_input == False:
                return False
        return True

  the test passes

* I add an `if statement`_ for the first case

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 10-11

    def logical_conjunction(first_input, second_input):
        if first_input == False:
            if second_input == False:
                return False
            if second_input == True:
                return False
        if first_input == True:
            if second_input == False:
                return False
            if second_input == True:
                return True

* there are only 2 results for this operation, in the first case the :ref:`function<functions>` returns :ref:`True <test_what_is_true>` and in the other 3 cases it returns :ref:`False <test_what_is_false>`. I use an `if statement`_ for the case where the result is :ref:`True <test_what_is_true>` and an else_ clause for the other cases

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2-5

    def logical_conjunction(first_input, second_input):
        if first_input == True and second_input == True:
            return True
        else:
            return False
        if first_input == False:
            if second_input == False:
                return False
            if second_input == True:
                return False
        if first_input == True:
            if second_input == False:
                return False
            if second_input == True:
                return True

  the test is still green

* I remove the other `if statements`_ then change the first statement with bool_

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2-3

    def logical_conjunction(first_input, second_input):
        if bool(first_input) and bool(second_input):
        # if first_input == True and second_input == True:
            return True
        else:
            return False

  still green. ``bool(x)`` checks if ``x`` is :ref:`True <test_what_is_true>`

* I remove the commented line then change the first line to make it simpler

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2-3

    def logical_conjunction(first_input, second_input):
        if first_input and second_input:
        # if bool(first_input) and bool(second_input):
            return True
        else:
            return False

  the test is still green. With ``if first_input and second_input``,  Python_ tests if ``p`` and ``q`` are :ref:`True<test_what_is_true>` in the background. I remove the commented line

* Python_ has `ternary operators`_ or `conditional expressions`_ which allow me to write the `if statement`_ and the else_ clause as one line

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2

    def logical_conjunction(first_input, second_input):
        return True if first_input and second_input else False
        if first_input and second_input:
            return True
        else:
            return False

  the terminal_ shows green, I remove the other `if statements`_

* I change the `return statement`_ to a simpler statement

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2

    def logical_conjunction(first_input, second_input):
        return first_input and second_input
        return True if first_input and second_input else False

  still green!

* I remove the second `return statement`_

  .. code-block:: python
    :lineno-start: 21

    def logical_conjunction(first_input, second_input):
        return first_input and second_input

----

*********************************************************************************
test_project_second
*********************************************************************************
=================================================================================
RED: make it fail
=================================================================================

I add a test for another Binary Operation in ``test_truth_table.py``

.. code-block:: python
  :lineno-start: 37
  :emphasize-lines: 3-4

          self.assertFalse(src.truth_table.logical_conjunction(False, False))

      def test_project_second(self):
          self.assertTrue(src.truth_table.project_second(True, True))


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'project_second'
=================================================================================
GREEN: make it pass
=================================================================================

I add a definition for the :ref:`function<functions>` in ``truth_table.py``

.. code-block:: python
  :lineno-start: 21
  :emphasize-lines: 5-6

  def logical_conjunction(first_input, second_input):
      return first_input and second_input


  def project_second(first_input, second_input):
      return True

the test passes
=================================================================================
REFACTOR: make it better
=================================================================================

* I add the second case to ``test_project_second`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 3

        def test_project_second(self):
            self.assertTrue(src.truth_table.project_second(True, True))
            self.assertFalse(src.truth_table.project_second(True, False))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: True is not false

* I add an `if statement`_ to ``project_second`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 2-4

    def project_second(first_input, second_input):
        if first_input == True:
            if second_input == False:
                return False
        return True

  the test passes

* I add the next case to ``test_project_second`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 4

        def test_project_second(self):
            self.assertTrue(src.truth_table.project_second(True, True))
            self.assertFalse(src.truth_table.project_second(True, False))
            self.assertTrue(src.truth_table.project_second(False, True))

  the test is still green

* I add the last case

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 5

        def test_project_second(self):
            self.assertTrue(src.truth_table.project_second(True, True))
            self.assertFalse(src.truth_table.project_second(True, False))
            self.assertTrue(src.truth_table.project_second(False, True))
            self.assertFalse(src.truth_table.project_second(False, False))


    # Exceptions Encountered

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: True is not false

* I add another `if statement`_ to ``project_second`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 2-4

    def project_second(first_input, second_input):
        if first_input == False:
            if second_input == False:
                return False
        if first_input == True:
            if second_input == False:
                return False
        return True

  the test passes

* ``project_second`` returns :ref:`False<test_what_is_false>` when ``q`` is :ref:`False<test_what_is_false>` and returns :ref:`True<test_what_is_true>` when ``q`` is :ref:`True<test_what_is_true>`. I add a new `return statement`_ to show this

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 2

    def project_second(first_input, second_input):
        return second_input
        if first_input == False:
            if second_input == False:
                return False
        if first_input == True:
            if second_input == False:
                return False
        return True

  the test is still green

* I remove the other statements

  .. code-block:: python
    :lineno-start: 25

    def project_second(first_input, second_input):
        return second_input

----

*********************************************************************************
test_converse_non_implication
*********************************************************************************
=================================================================================
RED: make it fail
=================================================================================

I add another test for a new Binary Operation in ``test_truth_table.py``

.. code-block:: python
  :lineno-start: 43
  :emphasize-lines: 3-4

          self.assertFalse(src.truth_table.project_second(False, False))

      def test_converse_non_implication(self):
          self.assertFalse(src.truth_table.converse_non_implication(True, True))


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'converse_non_implication'
=================================================================================
GREEN: make it pass
=================================================================================

I add the :ref:`function<functions>` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 25
  :emphasize-lines: 5-6

  def project_second(first_input, second_input):
      return second_input


  def converse_non_implication(first_input, second_input):
      return False

the test passes
=================================================================================
REFACTOR: make it better
=================================================================================

* I add another case to ``test_converse_non_implication`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 3

        def test_converse_non_implication(self):
            self.assertFalse(src.truth_table.converse_non_implication(True, True))
            self.assertFalse(src.truth_table.converse_non_implication(True, False))

  the test is still green

* I add the third case

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 4

        def test_converse_non_implication(self):
            self.assertFalse(src.truth_table.converse_non_implication(True, True))
            self.assertFalse(src.truth_table.converse_non_implication(True, False))
            self.assertTrue(src.truth_table.converse_non_implication(False, True))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: False is not true

* I add an `if statement`_ to ``converse_non_implication`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2-4

    def converse_non_implication(first_input, second_input):
        if first_input == False:
            if second_input == True:
                return True
        return False

  the test is green again

* I add the next case to ``test_converse_non_implication`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 5

        def test_converse_non_implication(self):
            self.assertFalse(src.truth_table.converse_non_implication(True, True))
            self.assertFalse(src.truth_table.converse_non_implication(True, False))
            self.assertTrue(src.truth_table.converse_non_implication(False, True))
            self.assertFalse(src.truth_table.converse_non_implication(False, False))


    # Exceptions Encountered

  the test is still passing

* I use ``and`` to put the two `if statements`_ together in ``converse_non_implication`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: -4

    def converse_non_implication(first_input, second_input):
        if first_input == False and second_input == True:
        # if first_input == False:
        #    if second_input == True:
                return True
        return False

  the terminal_ still shows green

* I remove the commented lines then change the first line with :ref:`logical negation<test_logical_negation>` and bool_

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2-4

    def converse_non_implication(first_input, second_input):
        if not first_input == True and bool(second_input):
        # if first_input == False and second_input == True:
            return True
        return False

  still green

* I add an else_ clause

  .. code-block:: python

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 4-5

    def converse_non_implication(first_input, second_input):
        if not first_input == True and bool(second_input):
        # if first_input == False and second_input == True:
            return True
        else:
            return False

  the test is still green

* I remove the comment and change the first line again to make it simpler

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2-3

    def converse_non_implication(first_input, second_input):
        if not bool(first_input) and second_input:
        # if not first_input == True and bool(second_input):
            return True
        else:
            return False

  the test is still green

* I remove the commented line and make the `if statement`_ simpler

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2-3

    def converse_non_implication(first_input, second_input):
        if not first_input and second_input:
        # if not bool(first_input) and second_input:
            return True
        else:
            return False

  the terminal_ still shows green

* I use a `conditional expression`_

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2

    def converse_non_implication(first_input, second_input):
        return True if not first_input and second_input else False
        if not first_input and second_input:
            return True
        else:
            return False

  still green

* I use the simpler `return statement`_

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2

    def converse_non_implication(first_input, second_input):
        return not first_input and second_input
        return True if not first_input and second_input else False

  all tests are still passing

* I remove the second `return statement`_

  .. code-block:: python
    :lineno-start: 29

    def converse_non_implication(first_input, second_input):
        return not first_input and second_input

----

*********************************************************************************
review
*********************************************************************************

Binary Operations take 2 inputs, each input can be :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`, if we name the first input ``p`` and the second ``q``, the tests show that

* :ref:`Converse NonImplication <test_converse_non_implication>` returns ``not first_input and second_input``
* :ref:`Project Second <test_project_second>` always returns ``q``
* :ref:`Logical Conjunction <test_logical_conjunction>` returns ``first_input and second_input``
* :ref:`Contradiction <test_contradiction>` always returns :ref:`False<test_what_is_false>`

and

* :ref:`Logical Disjunction <test_logical_disjunction>` is "or_"
* :ref:`Logical Conjunction <test_logical_conjunction>` is "and_"
* :ref:`Logical Negation <test_logical_negation>` is "not_"

do you want to :ref:`test more binary operations? <binary_operations_ii>`

----

:ref:`truth table: tests and solutions`

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">Click Here to leave a 5 star review on TrustPilot, if you found this helpful</a>
  </div>
  <!-- End TrustBox widget -->