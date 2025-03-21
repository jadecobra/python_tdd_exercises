.. include:: ../../../links.rst

#################################################################################
truth table: Logical Implication and Logical Equality
#################################################################################

.. contents:: table of contents
  :local:
  :depth: 1

----

*********************************************************************************
requirements
*********************************************************************************

:doc:`how to make a python test driven development environment </how_to/make_tdd_environment>` with ``truth_table`` as the name of the project

*********************************************************************************
test_logical_implication
*********************************************************************************

red: make it fail
#################################################################################

I add a test

.. code-block:: python

    def test_logical_or_material_implication(self):
        self.assertTrue(src.truth_table.logical_implication(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'logical_implication'. Did you mean: 'logical_disjunction'?

green: make it pass
#################################################################################

I add the :ref:`method<functions>`

.. code-block:: python

  def logical_implication(p, q):
      return p or q

the terminal shows green

refactor: make it better
#################################################################################


* I add the next case

  .. code-block:: python

    def test_logical_or_material_implication(self):
        self.assertTrue(src.truth_table.logical_implication(True, True))
        self.assertFalse(src.truth_table.logical_implication(True, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I add an `if statement`_

  .. code-block:: python

    def logical_implication(p, q):
        if p == True:
            if q == False:
                return False
        return p or q

  the terminal shows green again

* I add the next case

  .. code-block:: python

    def test_logical_or_material_implication(self):
        self.assertTrue(src.truth_table.logical_implication(True, True))
        self.assertFalse(src.truth_table.logical_implication(True, False))
        self.assertTrue(src.truth_table.logical_implication(False, True))

  the terminal shows green, I add an `if statement`_ to make sure it is right

  .. code-block:: python

    def logical_implication(p, q):
        if p == True:
            if q == False:
                return False
        if p == False:
            if q == True:
                return False
        return p or q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  when I change :ref:`False<test_what_is_false>` to :ref:`True<test_what_is_true>` in the `return statement`_

  .. code-block:: python

    def logical_implication(p, q):
        if p == True:
            if q == False:
                return False
        if p == False:
            if q == True:
                return True
        return p or q

  the test is green again

* I add the last case

  .. code-block:: python

    def test_logical_or_material_implication(self):
        self.assertTrue(src.truth_table.logical_implication(True, True))
        self.assertFalse(src.truth_table.logical_implication(True, False))
        self.assertTrue(src.truth_table.logical_implication(False, True))
        self.assertTrue(src.truth_table.logical_implication(False, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I add an `if statement`_

  .. code-block:: python

    def logical_implication(p, q):
        if p == True:
            if q == False:
                return False
        if p == False:
            if q == True:
                return True
            if q == False:
                return True
        return p or q

  the test passes

* I add a condition for the first case to make it clearer

  .. code-block:: python

    def logical_implication(p, q):
        if p == True:
            if q == True:
                return False
            if q == False:
                return False
        if p == False:
            if q == True:
                return True
            if q == False:
                return True
        return p or q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I change the `return statement`_

  .. code-block:: python

    def logical_implication(p, q):
        if p == True:
            if q == True:
                return True
            if q == False:
                return False
        if p == False:
            if q == True:
                return True
            if q == False:
                return True
        return p or q

  and the test passes

* I comment out ``return p or q``

  .. code-block:: python

    def logical_implication(p, q):
        if p == True:
            if q == True:
                return True
            if q == False:
                return False
        if p == False:
            if q == True:
                return True
            if q == False:
                return True
        # return p or q

  the terminal still shows green, so I remove the line

* I write an `if statement` for the one case where the outcome is :ref:`False <test_what_is_false>`

  .. code-block:: python

    def logical_implication(p, q):
        if p == True and q == False:
            return False
        else:
            return True
        if p == True:
            if q == True:
                return True
            if q == False:
                return False
        if p == False:
            if q == True:
                return True
            if q == False:
                return True

  the terminal still shows green. I remove the other `if statements`_

  .. code-block:: python

    def logical_implication(p, q):
        if p == True and q == False:
            return False
        else:
            return True

  I can rewrite the first line in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python

    def logical_implication(p, q):
        if p == True and q != True:
        # if p == True and q == False:
            return False
        else:
            return True

  the terminal shows green. I remove the commented line and rewrite the first line with bool_

  .. code-block:: python

    def logical_implication(p, q):
        if bool(p) == True and bool(q) != True:
        # if p == True and q != True:
            return False
        else:
            return True

  the tests are still passing. I remove the commented line and rewrite the first line again using not_

  .. code-block:: python

    def logical_implication(p, q):
        if bool(p) == True and not bool(q) == True:
        # if bool(p) == True and bool(q) != True:
            return False
        else:
            return True

  the test is still green, I remove the commented line then remove the repetition

  .. code-block:: python

    def logical_implication(p, q):
        if bool(p) and not bool(q):
        # if bool(p) == True and not bool(q) == True:
            return False
        else:
            return True

  still green, I remove the commented line and remove bool_

  .. code-block:: python

    def logical_implication(p, q):
        if p and not q:
        # if bool(p) and not bool(q):
            return False
        else:
            return True

  the test is still green. I remove the commented line and rewrite the else_ statement with the opposite `if statement`_

  .. code-block:: python

    def logical_implication(p, q):
        if p and not q:
            return False
        if not (p and not q):
            return True

  the terminal shows green. I move the first two lines to the bottom and rewrite the `if statement`_ with an else_ clause

  .. code-block:: python

    def logical_implication(p, q):
        if not (p and not q):
            return True
        else:
        # if p and not q:
            return False

  the test is still green, I remove the commented line and "multiply" out the first statement since it has not_ twice

  .. code-block:: python

    def logical_implication(p, q):
        if not p not and not not q:
        if not (p and not q):
            return True
        else:
            return False

  ``not and`` is or_ and ``not not`` cancels out

  .. code-block:: python

    def logical_implication(p, q):
        if not p or q:
        # if not (p and not q):
            return True
        else:
            return False

  the terminal still shows green, I remove the comment and rewrite the statement as a `conditional expression`_

  .. code-block:: python

    def logical_implication(p, q):
        return True if not p or q else False
        if not p or q:
            return True
        else:
            return False

  still green, I remove the rest of the lines and make the `return statement`_ simpler

  .. code-block:: python

    def logical_implication(p, q):
        return not p or q
        return True if not p or q else False

  the test is still green. I remove the second `return statement`_

  .. code-block:: python

    def logical_implication(p, q):
        return not p or q

  and all tests are still passing

----

*********************************************************************************
test_logical_equality
*********************************************************************************

red: make it fail
#################################################################################

I add a new test

.. code-block:: python

  def test_logical_equality_or_biconditional(self):
      self.assertTrue(src.truth_table.logical_equality(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'logical_equality'. Did you mean: 'logical_identity'?

green: make it pass
#################################################################################

* I add a definition

  .. code-block:: python

    def logical_equality(p, q):
        return not p or q

  the terminal shows green

refactor: make it better
#################################################################################

* I add the next case

  .. code-block:: python

    def test_logical_equality_or_biconditional(self):
        self.assertTrue(src.truth_table.logical_equality(True, True))
        self.assertFalse(src.truth_table.logical_equality(True, False))

  the terminal still shows green. Should I be worried?


* I add another case

  .. code-block:: python

    def test_logical_equality_or_biconditional(self):
        self.assertTrue(src.truth_table.logical_equality(True, True))
        self.assertFalse(src.truth_table.logical_equality(True, False))
        self.assertFalse(src.truth_table.logical_equality(False, True))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  Phew! The tests still work. I add an `if statement`_

  .. code-block:: python

    def logical_equality(p, q):
        if p == False:
            if q == True:
                return False
        return not p or q

  the test passes

* I add the last case

  .. code-block:: python

    def test_logical_equality_or_biconditional(self):
        self.assertTrue(src.truth_table.logical_equality(True, True))
        self.assertFalse(src.truth_table.logical_equality(True, False))
        self.assertFalse(src.truth_table.logical_equality(False, True))
        self.assertTrue(src.truth_table.logical_equality(False, False))

  and the test is still green. There are still only two results but this time :ref:`True<test_what_is_true>` happens in two of the cases and  :ref:`False<test_what_is_false>` happens in the other two.

* I add an `if statement`_ for the last case

  .. code-block:: python

    def logical_equality(p, q):
        if p == False:
            if q == False:
                return False
            if q == True:
                return False
        return not p or q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I fix the line to make it pass, then add a statement for the first case

  .. code-block:: python

    def logical_equality(p, q):
        if p == True:
            if q == True:
                return False
        if p == False:
            if q == False:
                return True
            if q == True:
                return False
        return not p or q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I fix the line then add an `if statement`_ for the secibd case

  .. code-block:: python

    def logical_equality(p, q):
        if p == True:
            if q == False:
                return True
            if q == True:
                return True
        if p == False:
            if q == False:
                return True
            if q == True:
                return False
        return not p or q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the `return statement`_ and comment out ``return not p or q``

  .. code-block:: python

    def logical_equality(p, q):
        if p == True:
            if q == False:
                return False
            if q == True:
                return True
        if p == False:
            if q == False:
                return True
            if q == True:
                return False
        # return not p or q

  the terminal shows green again

* I simplify the `if statements`

  .. code-block:: python

    def logical_equality(p, q):
        if p == True and q == False:
            return False
        if p == True and q == True:
            return True
        if p == False and q == False:
            return True
        if p == False and q == True:
            return False
        # if p == True:
        #     if q == False:
        #         return False
        #     if q == True:
        #         return True
        # if p == False:
        #     if q == False:
        #         return True
        #     if q == True:
        #         return False

  I remove the commented lines then change the order of statements

  .. code-block:: python

    def logical_equality(p, q):
        if p == False and q == True:
            return False
        if p == True and q == False:
            return False
        if p == True and q == True:
            return True
        if p == False and q == False:
            return True

  the terminal still shows green. I rewrite the first `if statement`_ in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python

    def logical_equality(p, q):
        if p != True and q == True:
        # if p == False and q == True:
            return False
        if p == True and q == False:
            return False
        if p == True and q == True:
            return True
        if p == False and q == False:
            return True

  the test is still green, I do the same thing with the second statement

  .. code-block:: python

    def logical_equality(p, q):
        if p != True and q == True:
            return False
        if p == True and q != True:
        # if p == True and q == False:
            return False
        if p == True and q == True:
            return True
        if p == False and q == False:
            return True

  still green, I do the next statement

  .. code-block:: python

    def logical_equality(p, q):
        if p != True and q == True:
            return False
        if p == True and q != True:
            return False
        if p == True and q == True:
            return True
        if p != True and q != True:
        # if p == False and q == False:
            return True

  the terminal is green. I rewrite the statements using hidden truth value testing

  .. code-block:: python

    def logical_equality(p, q):
        if not p and q:
        # if p != True and q == True:
            return False
        if p == True and q != True:
            return False
        if p == True and q == True:
            return True
        if p != True and q != True:
            return True

  still green, I do it with the next line

  .. code-block:: python

    def logical_equality(p, q):
        if not p and q:
            return False
        if p and not q:
        # if p == True and q != True:
            return False
        if p == True and q == True:
            return True
        if p != True and q != True:
            return True

  the terminal shows green, I do the next line

  .. code-block:: python

    def logical_equality(p, q):
        if not p and q:
            return False
        if p and not q:
            return False
        if p and q:
        # if p == True and q == True:
            return True
        if p != True and q != True:
            return True

  still green. I do the last line

  .. code-block:: python

    def logical_equality(p, q):
        if not p and q:
            return False
        if p and not q:
            return False
        if p and q:
            return True
        if not p and not q:
        # if p != True and q != True:
            return True

  the terminal shows green

* the two cases that are :ref:`False<test_what_is_false>` can be combined using or_

  .. code-block:: python

    def logical_equality(p, q):
        if (not p and q) or (p and not q):
            return False
        else:
            return True
        if not p and q:
            return False
        if p and not q:
            return False
        if p and q:
            return True
        if not p and not q:
            return True

  green again. I remove the other `if statements`_ and replace the else_ clause with the opposite statement

  .. code-block:: python

    def logical_equality(p, q):
        if (not p and q) or (p and not q):
            return False
        if not ((not p and q) or (p and not q)):
        # else:
            return True

  the terminal still shows green. I change the order then add an else_ clause

  .. code-block:: python

    def logical_equality(p, q):
        if not ((not p and q) or (p and not q)):
            return True
        else:
        # if (not p and q) or (p and not q):
            return False

  still green. I try to "multiply" out the first statement

  .. code-block:: python

    def logical_equality(p, q):
        if (not (not p and q)) and (not (p and not q)):
        # if not ((not p and q) or (p and not q)):
            return True
        else:
            return False

  this is getting confusing. I try to "multiply" out the first group in the statement

  .. code-block:: python

    def logical_equality(p, q):
        if (not not p not and not q) and (not (p and not q)):
        # if (not (not p and q)) and (not (p and not q)):
            return True
        else:
            return False

  ``not and`` is or_

  .. code-block:: python

    def logical_equality(p, q):
        if (p or not q) and (not (p and not q)):
        # if (not (not p and q)) and (not (p and not q)):
            return True
        else:
            return False

  the terminal shows green. I do the second part

  .. code-block:: python

    def logical_equality(p, q):
        if (p or not q) and (not p not and not not q):
        # if (p or not q) and (not (p and not q)):
            return True
        else:
            return False

  using the correct terms

  .. code-block:: python

    def logical_equality(p, q):
        if (p or not q) and (not p or q):
        # if (p or not q) and (not (p and not q)):
            return True
        else:
            return False

  still green. I add a `conditional expression`_ (`ternary operator`_)

  .. code-block:: python

    def logical_equality(p, q):
        return True if (p or not q) and (not p or q) else False
        if (p or not q) and (not p or q):
            return True
        else:
            return False

  the terminal shows green. I remove the other `if statements`_ and use implicit truth value testing

  .. code-block:: python

    def logical_equality(p, q):
        return (p or not q) and (not p or q)
        return True if (p or not q) and (not p or q) else False

  still green. I remove the second `return statement`_ and all tests are still passing

----

*********************************************************************************
review
*********************************************************************************

The funny thing is all this work could have been achieved by using the ``==`` symbol, since the two cases where :ref:`True<test_what_is_true>` is the result are cases where ``p`` and ``q`` are the same

.. code-block:: python

  def logical_equality(p, q):
      if p == q:
          return True
      else:
          return False

or a `conditional expression`_

.. code-block:: python

  def logical_equality(p, q):
      return p == q


:ref:`Exclusive Disjunction and Logical NAND<truth table: Exclusive Disjunction and Logical NAND>` are next

----

:doc:`/code/code_truth_table`