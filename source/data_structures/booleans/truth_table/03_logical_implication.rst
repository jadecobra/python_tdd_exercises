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

----

*********************************************************************************
review
*********************************************************************************

----

:doc:`/code/code_truth_table`