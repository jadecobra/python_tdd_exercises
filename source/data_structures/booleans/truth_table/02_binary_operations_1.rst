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

There are 16 binary operations, they all take 2 inputs and each of the inputs can be :ref:`True <test_what_is_true>` or :ref:`False <test_what_is_false>`. This gives four cases

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

red: make it fail
#################################################################################

I add a new TestCase_ to ``test_truth_table.py``

.. code-block:: python

      def test_logical_negation_aka_not(self):
          ...


  class TestBinaryOperations(unittest.TestCase):

      def test_contradiction(self):
          self.assertFalse(src.truth_table.contradiction(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'contradiction'

green: make it pass
#################################################################################

I add a :ref:`function<functions>` definition to ``truth_table.py``

.. code-block:: python

  def logical_negation(argument):
      return not argument


  def contradiction(argument):
      return not argument

the terminal shows :ref:`TypeError`

.. code-block:: python

  TypeError: contradiction() takes 1 positional argument but 2 were given

I change the signature to make it take 2 inputs

.. code-block:: python

  def contradiction(p, q):
      return not p

the test passes

refactor: make it better
#################################################################################

* I add the second case

  .. code-block:: python

    def test_contradiction(self):
        self.assertFalse(src.truth_table.contradiction(True, True))
        self.assertFalse(src.truth_table.contradiction(True, False))

  the test is still green

* I add the next case

  .. code-block:: python

    def test_contradiction(self):
        self.assertFalse(src.truth_table.contradiction(True, True))
        self.assertFalse(src.truth_table.contradiction(True, False))
        self.assertFalse(src.truth_table.contradiction(False, True))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  all three cases of the test expect :ref:`False<test_what_is_false>`. I change the `return statement`_

  .. code-block:: python

    def contradiction(p, q):
        return False

  the test is green again

* I add the fourth case

  .. code-block:: python

    def test_contradiction(self):
        self.assertFalse(src.truth_table.contradiction(True, True))
        self.assertFalse(src.truth_table.contradiction(True, False))
        self.assertFalse(src.truth_table.contradiction(False, True))
        self.assertFalse(src.truth_table.contradiction(False, False))

  the test is still green! :ref:`Contradiction<test_contradiction>` always returns :ref:`False<test_what_is_false>`

----

*********************************************************************************
test_logical_conjunction
*********************************************************************************

red: make it fail
#################################################################################

I add the next test

.. code-block:: python

  def test_contradiction(self):
      ...

  def test_logical_conjunction(self):
      self.assertTrue(src.truth_table.logical_conjunction(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python
  :force:

  AttributeError: module 'src.truth_table' has no attribute 'logical_conjunction'. Did you mean: 'logical_negation'?

green: make it pass
#################################################################################

I add the :ref:`function<functions>`

.. code-block:: python

  def contradiction(p, q):
      return False


  def logical_conjunction(p, q):
      return True

the test passes

refactor: make it better
#################################################################################

* I add the next case

  .. code-block:: python

    def test_logical_conjunction(self):
        self.assertTrue(src.truth_table.logical_conjunction(True, True))
        self.assertFalse(src.truth_table.logical_conjunction(True, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I make the :ref:`function<functions>` return :ref:`False <test_what_is_false>`

  .. code-block:: python

    def logical_conjunction(p, q):
        return False
        return True

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  The line that was passing before is now failing. ``logical_conjunction`` has to choose whether to return :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>` based on the inputs. I can make it do that with `if statements`_

  .. code-block:: python

    def logical_conjunction(p, q):
        if p == True:
            if q == False:
                return False
        return True

  the test passes.  The :ref:`function<functions>` returns :ref:`False<test_what_is_false>` when ``p`` is :ref:`True<test_what_is_true>` and ``q`` is :ref:`False<test_what_is_false>`,  otherwise it returns :ref:`True<test_what_is_true>`

* I add the next case

  .. code-block:: python

    def test_logical_conjunction(self):
        self.assertTrue(src.truth_table.logical_conjunction(True, True))
        self.assertFalse(src.truth_table.logical_conjunction(True, False))
        self.assertFalse(src.truth_table.logical_conjunction(False, True))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I add another `if statement`_

  .. code-block:: python

    def logical_conjunction(p, q):
        if p == False:
            if q == True:
                return False
        if p == True:
            if q == False:
                return False
        return True

  the test passes

* I add the last case

  .. code-block:: python

    def test_logical_conjunction(self):
        self.assertTrue(src.truth_table.logical_conjunction(True, True))
        self.assertFalse(src.truth_table.logical_conjunction(True, False))
        self.assertFalse(src.truth_table.logical_conjunction(False, True))
        self.assertFalse(src.truth_table.logical_conjunction(False, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I add an `if statement`_ for it

  .. code-block:: python

    def logical_conjunction(p, q):
        if p == False:
            if q == False:
                return False
            if q == True:
                return False
        if p == True:
            if q == False:
                return False
        return True

  the test passes

* I add an `if statement`_ for the first case

  .. code-block:: python

    def logical_conjunction(p, q):
        if p == False:
            if q == False:
                return False
            if q == True:
                return False
        if p == True:
            if q == False:
                return False
            if q == True:
                return True

* There are only 2 results for this operation, in the first case the :ref:`function<functions>` returns :ref:`True <test_what_is_true>` and in the other 3 cases it returns :ref:`False <test_what_is_false>`. I can use an `if statement`_ for the case where the result is :ref:`True <test_what_is_true>` and an else_ clause for the other cases

  .. code-block:: python

    def logical_conjunction(p, q):
        if p == True and q == True:
            return True
        else:
            return False
        if p == False:
            if q == False:
                return False
            if q == True:
                return False
        if p == True:
            if q == False:
                return False
            if q == True:
                return True

  the test is still green. I remove the other `if statements`_ then change the first statement with bool_

  .. code-block:: python

    def logical_conjunction(p, q):
        if bool(p) and bool(q):
        # if p == True and q == True:
            return True
        else:
            return False

  still green. ``bool(x)`` checks if ``x`` is :ref:`True <test_what_is_true>`. I remove the commented line then change the first line to make it simpler

  .. code-block:: python

    def logical_conjunction(p, q):
        if p and q:
        # if bool(p) and bool(q):
            return True
        else:
            return False

  the test is still green, Python_ tests if ``p`` and ``q`` are :ref:`True<test_what_is_true>` in the background, I remove the commented line

* Python_ has `ternary operators`_ or `conditional expressions`_ which allow me to write the `if statement`_ and the else_ clause as one line

  .. code-block:: python

    def logical_conjunction(p, q):
        return True if p and q else False
        if p and q:
            return True
        else:
            return False

  the terminal shows green, I remove the other `if statements`_ then use a simpler statement

  .. code-block:: python

    def logical_conjunction(p, q):
        return p and q
        return True if p and q else False

  still green! I remove the second `return statement`_

  .. code-block:: python

    def logical_conjunction(p, q):
        return p and q

----

*********************************************************************************
test_project_second
*********************************************************************************

red: make it fail
#################################################################################

I add another test

.. code-block:: python

  def test_logical_conjunction(self):
      ...

  def test_project_second(self):
      self.assertTrue(src.truth_table.project_second(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'project_second'

green: make it pass
#################################################################################

When I add a :ref:`function<functions>` definition for it

.. code-block:: python

  def logical_conjunction(p, q):
      return p and q


  def project_second(p, q):
      return True

the test passes

refactor: make it better
#################################################################################

* I add the second case

  .. code-block:: python

    def test_project_second(self):
        self.assertTrue(src.truth_table.project_second(True, True))
        self.assertFalse(src.truth_table.project_second(True, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I add an `if statement`_

  .. code-block:: python

    def project_second(p, q):
        if p == True:
            if q == False:
                return False
        return True

  the test passes

* I add the next case

  .. code-block:: python

    def test_project_second(self):
        self.assertTrue(src.truth_table.project_second(True, True))
        self.assertFalse(src.truth_table.project_second(True, False))
        self.assertTrue(src.truth_table.project_second(False, True))

  the test is still green

* I add the last case

  .. code-block:: python

    def test_project_second(self):
        self.assertTrue(src.truth_table.project_second(True, True))
        self.assertFalse(src.truth_table.project_second(True, False))
        self.assertTrue(src.truth_table.project_second(False, True))
        self.assertFalse(src.truth_table.project_second(False, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I add another `if statement`_

  .. code-block:: python

    def project_second(p, q):
        if p == False:
            if q == False:
                return False
        if p == True:
            if q == False:
                return False
        return True

  the test passes

* This :ref:`function<functions>` returns :ref:`False<test_what_is_false>` when ``q`` is :ref:`False<test_what_is_false>` and returns :ref:`True<test_what_is_true>` when ``q`` is :ref:`True<test_what_is_true>`. I add a new statement to show this

  .. code-block:: python

    def project_second(p, q):
        return q
        if p == False:
            if q == False:
                return False
        if p == True:
            if q == False:
                return False
        return True

  the test is still green, I remove the other statements

  .. code-block:: python

    def project_second(p, q):
        return q

----

*********************************************************************************
test_converse_non_implication
*********************************************************************************

red: make it fail
#################################################################################

I add another test

.. code-block:: python

  def test_project_second(self):
      ...

  def test_converse_non_implication(self):
      self.assertFalse(src.truth_table.converse_non_implication(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'converse_non_implication'

green: make it pass
#################################################################################

I add the :ref:`function<functions>`

.. code-block:: python

  def project_second(p, q):
      return q


  def converse_non_implication(p, q):
      return False

the test passes

refactor: make it better
#################################################################################

* I add another case

  .. code-block:: python

    def test_converse_non_implication(self):
        self.assertFalse(src.truth_table.converse_non_implication(True, True))
        self.assertFalse(src.truth_table.converse_non_implication(True, False))

  the test is still green

* I add the third case

  .. code-block:: python

    def test_converse_non_implication(self):
        self.assertFalse(src.truth_table.converse_non_implication(True, True))
        self.assertFalse(src.truth_table.converse_non_implication(True, False))
        self.assertTrue(src.truth_table.converse_non_implication(False, True))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I add an `if statement`_

  .. code-block:: python

    def converse_non_implication(p, q):
        if p == False:
            if q == True:
                return True
        return False

  the test is green again

* I add the next case

  .. code-block:: python

    def test_converse_non_implication(self):
        self.assertFalse(src.truth_table.converse_non_implication(True, True))
        self.assertFalse(src.truth_table.converse_non_implication(True, False))
        self.assertTrue(src.truth_table.converse_non_implication(False, True))
        self.assertFalse(src.truth_table.converse_non_implication(False, False))

  the test is still passing

* I can use ``and`` to put the two `if statements`_ together

  .. code-block:: python

    def converse_non_implication(p, q):
        if p == False and q == True:
        # if p == False:
        #    if q == True:
                return True
        return False

  the terminal still shows green. I remove the other statements then change the first line with :ref:`logical negation<test_logical_negation>` and bool_

  .. code-block:: python

    def converse_non_implication(p, q):
        if not p == True and bool(q):
        # if p == False and q == True:
            return True
        else:
            return False

  still green. I remove the comment and change the line again

  .. code-block:: python

    def converse_non_implication(p, q):
        if not bool(p) and q:
        # if not p == True and bool(q):
            return True
        else:
            return False

  the test is still green. I remove the commented line and make the `if statement`_ simpler

  .. code-block:: python

    def converse_non_implication(p, q):
        if not p and q:
        # if not bool(p) and q:
            return True
        else:
            return False

  the test is still green. I use a `conditional expression`_

  .. code-block:: python

    def converse_non_implication(p, q):
        return True if not p and q else False
        if not p and q:
            return True
        else:
            return False

  still green. I use the simpler `return statement`_

  .. code-block:: python

    def converse_non_implication(p, q):
        return not p and q
        return True if not p and q else False

  all tests are still passing. I remove the second `return statement`_

  .. code-block:: python

    def converse_non_implication(p, q):
        return not p and q

----

*********************************************************************************
review
*********************************************************************************

Binary Operations take 2 inputs, each of which could be :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`, if we name the first input ``p`` and the second ``q``, the tests show that

* :ref:`Converse NonImplication <test_converse_non_implication>` returns ``not p and q``
* :ref:`Project Second <test_project_second>` always returns ``q``
* :ref:`Logical Conjunction <test_logical_conjunction>` returns ``p and q``
* :ref:`Contradiction <test_contradiction>` always returns :ref:`False<test_what_is_false>`

do you want to :ref:`test more binary operations? <binary_operations_ii>`

----

:ref:`truth table: tests and solutions`