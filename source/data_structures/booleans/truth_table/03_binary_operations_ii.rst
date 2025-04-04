.. include:: ../../../links.rst

#################################################################################
truth table: Binary Operations II
#################################################################################

.. contents:: table of contents
  :local:
  :depth: 1

----

*********************************************************************************
requirements
*********************************************************************************

:doc:`how to make a python test driven development environment </how_to/make_tdd_environment>` with ``truth_table`` as the name of the project

----

*********************************************************************************
test_exclusive_disjunction
*********************************************************************************

red: make it fail
#################################################################################

I add a new test

.. code-block:: python

  def test_logical_equality(self):
      ...

  def test_exclusive_disjunction(self):
      self.assertFalse(src.truth_table.exclusive_disjunction(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'exclusive_disjunction'

green: make it pass
#################################################################################

I add the :ref:`function<functions>`

.. code-block:: python

  def logical_equality(p, q):
      return p == q
      return (p and q) or not (p or q)


  def exclusive_disjunction(p, q):
      return p == q

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: True is not false

I add an `if statement`_

.. code-block:: python

  def exclusive_disjunction(p, q):
      if p == True and q == True:
          return False
      return p == q

the test passes

refactor: make it better
#################################################################################

* I add the next case

  .. code-block:: python

    def test_exclusive_disjunction(self):
        self.assertFalse(src.truth_table.exclusive_disjunction(True, True))
        self.assertTrue(src.truth_table.exclusive_disjunction(True, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I add an `if statement`_

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p == True and q == False:
            return True
        if p == True and q == True:
            return False
        return p == q

  the test passes

* I add the next case

  .. code-block:: python

    def test_exclusive_disjunction(self):
        self.assertFalse(src.truth_table.exclusive_disjunction(True, True))
        self.assertTrue(src.truth_table.exclusive_disjunction(True, False))
        self.assertTrue(src.truth_table.exclusive_disjunction(False, True))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I add another `if statement`_

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p == False and q == True:
            return True
        if p == True and q == False:
            return True
        if p == True and q == True:
            return False
        return p == q

  the test passes

* I add the last case

  .. code-block:: python

    def test_exclusive_disjunction(self):
        self.assertFalse(src.truth_table.exclusive_disjunction(True, True))
        self.assertTrue(src.truth_table.exclusive_disjunction(True, False))
        self.assertTrue(src.truth_table.exclusive_disjunction(False, True))
        self.assertFalse(src.truth_table.exclusive_disjunction(False, False))

  and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I add an `if statement`_ for it

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p == False and q == False:
            return False
        if p == False and q == True:
            return True
        if p == True and q == False:
            return True
        if p == True and q == True:
            return False
        return p == q

  the terminal shows green

* I remove ``return p == q`` and move the last case to the bottom to put the two cases that return :ref:`True<test_what_is_true>` together

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p == False and q == True:
            return True
        if p == True and q == False:
            return True
        if p == True and q == True:
            return False
        if p == False and q == False:
            return False

  still green. I rewrite the first statement

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if not p and q:
        # if p == False and q == True:
            return True
        if p == True and q == False:
            return True
        if p == True and q == True:
            return False
        if p == False and q == False:
            return False

  the terminal still shows green. I rewrite the second statement

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if not p and q:
            return True
        if p and not q:
        # if p == True and q == False:
            return True
        if p == True and q == True:
            return False
        if p == False and q == False:
            return False

  still green. I use or_ to put the two statements that return :ref:`True<test_what_is_true>` together

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if (not p and q) or (p and not q):
            return True
        else:
            return False
        if not p and q:
            return True
        if p and not q:
            return True
        if p == True and q == True:
            return False
        if p == False and q == False:
            return False

  the test is still green. I remove the other `if statements`_ and use a `conditional expression`_

  .. code-block:: python

    def exclusive_disjunction(p, q):
        return (not p and q) or (p and not q)
        if (not p and q) or (p and not q):
            return True
        else:
            return False

  the terminal still shows green. I remove the other statements

  .. code-block:: python

    def exclusive_disjunction(p, q):
        return (not p and q) or (p and not q)


* since the :ref:`function<functions>` returns :ref:`True<test_what_is_true>` in the two cases when ``p`` and ``q`` are NOT the same, it could also have been written this way
  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p != q:
            return True
        else:
            return False

  or

  .. code-block:: python

    def exclusive_disjunction(p, q):
        return not (p == q)

  or

  .. code-block:: python

    def exclusive_disjunction(p, q):
        return p != q

----

*********************************************************************************
test_logical_nand
*********************************************************************************

red: make it fail
#################################################################################

I add a test for Logical NAND

.. code-block:: python

  def test_logical_nand(self):
      self.assertFalse(src.truth_table.logical_nand(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python
  :force:

  AttributeError: module 'src.truth_table' has no attribute 'logical_nand'. Did you mean: 'logical_false'?

green: make it pass
#################################################################################

I add a definition for the :ref:`function<functions>`

.. code-block:: python

  def exclusive_disjunction(p, q):
      return p != q
      return not (p == q)
      return (not p and q) or (p and not q)


  def logical_nand(p, q):
      return p != q

the terminal shows green

refactor: make it better
#################################################################################

* I add the next case

  .. code-block:: python

    def test_logical_nand(self):
        self.assertFalse(src.truth_table.logical_nand(True, True))
        self.assertTrue(src.truth_table.logical_nand(True, False))

  the terminal still shows green

* I add another case

  .. code-block:: python

    def test_logical_nand(self):
        self.assertFalse(src.truth_table.logical_nand(True, True))
        self.assertTrue(src.truth_table.logical_nand(True, False))
        self.assertTrue(src.truth_table.logical_nand(False, True))

  still green. I wonder if the test is broken

* I add the last case

  .. code-block:: python

    def test_logical_nand(self):
        self.assertFalse(src.truth_table.logical_nand(True, True))
        self.assertTrue(src.truth_table.logical_nand(True, False))
        self.assertTrue(src.truth_table.logical_nand(False, True))
        self.assertTrue(src.truth_table.logical_nand(False, False))

  which gives me :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  okay! The test still works. I add an `if statement`_

  .. code-block:: python

    def logical_nand(p, q):
        if p == False and q == False:
            return True
        return p != q

* I add an `if statement`_ for the one case that returns :ref:`False<test_what_is_false>`

  .. code-block:: python

    def logical_nand(p, q):
        if p == True and q == True:
            return True
        if p == False and q == False:
            return True
        return p != q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I change the `return statement`_ then add an else_ clause

  .. code-block:: python

    def logical_nand(p, q):
        if p == True and q == True:
            return False
        else:
            return True
        if p == False and q == False:
            return True
        return p != q

  the test is green again, I remove the other statements and rewrite the first line

  .. code-block:: python

    def logical_nand(p, q):
        if p and q:
        # if p == True and q == True:
            return False
        else:
            return True

  then write the opposite of the `if statement`_ for the else_ clause

  .. code-block:: python

    def logical_nand(p, q):
        if p and q:
            return False
        if not (p and q):
        # else:
            return True

  I move the two statements at the bottom to the top then add a new else_ clause

  .. code-block:: python

    def logical_nand(p, q):
        if not (p and q):
            return True
        else:
        # if p and q:
            return False

  the test is still green. I rewrite it as a `conditional expression`_

  .. code-block:: python

    def logical_nand(p, q):
        return not (p and q)
        if not (p and q):
            return True
        else:
        # if p and q:
            return False

  I remove the other statements

  .. code-block:: python

    def logical_nand(p, q):
        return not (p and q)

----

*********************************************************************************
test_logical_nor
*********************************************************************************

red: make it fail
#################################################################################

I add another test

.. code-block:: python

    def test_logical_nand(self):
        ...

    def test_logical_nor(self):
        self.assertFalse(src.truth_table.logical_nor(True, True))

and the terminal shows :ref:`AttributeError`

.. code-block:: python
  :force:

  AttributeError: module 'src.truth_table' has no attribute 'logical_nor'. Did you mean: 'logical_nand'?

green: make it pass
#################################################################################

I add a :ref:`function<functions>` definition to ``truth_table.py``

.. code-block:: python

  def logical_nand(p, q):
      return not (p and q)


  def logical_nor(p, q):
      return not (p and q)

the test passes

refactor: make it better
#################################################################################

* I add the next case

  .. code-block:: python

    def test_logical_nor(self):
        self.assertFalse(src.truth_table.logical_nor(True, True))
        self.assertFalse(src.truth_table.logical_nor(True, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I add an `if statement`_

  .. code-block:: python

    def logical_nor(p, q):
        if p and not q:
            return False
        return not (p and q)

  the test passes

* on to the next case

  .. code-block:: python

    def test_logical_nor(self):
        self.assertFalse(src.truth_table.logical_nor(True, True))
        self.assertFalse(src.truth_table.logical_nor(True, False))
        self.assertFalse(src.truth_table.logical_nor(False, True))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I add another `if statement`

  .. code-block:: python

    def logical_nor(p, q):
        if not p and q:
            return False
        if p and not q:
            return False
        return not (p and q)

  the test passes

* I add the last case

  .. code-block:: python

    def test_logical_nor(self):
        self.assertFalse(src.truth_table.logical_nor(True, True))
        self.assertFalse(src.truth_table.logical_nor(True, False))
        self.assertFalse(src.truth_table.logical_nor(False, True))
        self.assertTrue(src.truth_table.logical_nor(False, False))

  and the test stays green

* I add an `if statement`_ for the one case where the result is :ref:`True<test_what_is_true>` with an else_ clause

  .. code-block:: python

    def logical_nor(p, q):
        if not p and not q:
            return True
        else:
            return False
        if not p and q:
            return False
        if p and not q:
            return False
        return not (p and q)

  the terminal still shows green, I remove the other statements and rewrite the `if statement`_ to factor out not_ since it happens two timems

  .. code-block:: python

    def logical_nor(p, q):
        if not p not or not q:
        # if not p and not q:
            return True
        else:
            return False

  the terminal shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  I fix the line

  .. code-block:: python

    def logical_nor(p, q):
        if not (p or q):
        # if not p not or not q:
        # if not p and not q:
            return True
        else:
            return False

  still green. I rewrite it as a `conditional expression`_

  .. code-block:: python

    def logical_nor(p, q):
        return not (p or q)
        if not (p or q):
        # if not p not or not q:
        # if not p and not q:
            return True
        else:
            return False

  still green, I remove the other statements

  .. code-block:: python

    def logical_nor(p, q):
        return not (p or q)

----

*********************************************************************************
test_converse_non_implication
*********************************************************************************

red: make it fail
#################################################################################

I add a test for converse nonimplication to ``TestBinaryOperations`` in ``test_truth_table.py``

.. code-block:: python

    def test_converse_non_implication(self):
        self.assertFalse(src.truth_table.converse_non_implication(True, True))
        self.assertFalse(src.truth_table.converse_non_implication(True, False))
        self.assertTrue(src.truth_table.converse_non_implication(False, True))
        self.assertFalse(src.truth_table.converse_non_implication(False, False))

the terminal shows :ref:`AttributeError`

green: make it pass
#################################################################################

* I add a :ref:`function<functions>` definition to ``truth_table.py``

  .. code-block:: python

    def converse_non_implication(p, q):
        return False

  since the first two cases pass, the terminal shows :ref:`AssertionError` for the third case
* I add a condition for it

  .. code-block:: python

    def converse_non_implication(p, q):
        if p == False and q == True:
            return True
        return False

  all the tests pass

refactor: make it better
#################################################################################

* I use implied conditional testing with not_ for the first part of the if statement

  .. code-block:: python

    def converse_non_implication(p, q):
        if not p and q  == True:
            return True
        return False

  and the test passes

* I do the same for the second part of the statement

  .. code-block:: python

    def converse_non_implication(p, q):
        if not p and q:
            return True
        return False

* I add an else clause

  .. code-block:: python

    def converse_non_implication(p, q):
        if not p and q:
            return True
        else:
          return False

* then I rewrite as a ``return`` statement

  .. code-block:: python

    def converse_non_implication(p, q):
        return not p and q

  Another success! All tests pass

----

*********************************************************************************
test_material_non_implication
*********************************************************************************

red: make it fail
#################################################################################

I add a test for material non-implication to ``TestBinaryOperations`` in ``test_truth_table.py``

.. code-block:: python

    def test_material_non_implication(self):
        self.assertFalse(src.truth_table.material_non_implication(True, True))
        self.assertTrue(src.truth_table.material_non_implication(True, False))
        self.assertFalse(src.truth_table.material_non_implication(False, True))
        self.assertFalse(src.truth_table.material_non_implication(False, False))

the terminal shows :ref:`AttributeError`

green: make it pass
#################################################################################


* I add a :ref:`function<functions>` definition to ``truth_table.py``

  .. code-block:: python

    def material_non_implication(p, q):
        return False

  the terminal shows :ref:`AssertionError` for the second case
* I add a condition for it

  .. code-block:: python

      def material_non_implication(p, q):
          if p == True and q == False:
              return True
          return False

  and the tests pass

refactor: make it better
#################################################################################


* I use implied conditional testing for the first part of the if statement

  .. code-block:: python

    def material_non_implication(p, q):
        if p and q == False:
            return True
        else:
            return False

  all tests still pass

* then change the second part to use not_

  .. code-block:: python

    def material_non_implication(p, q):
        if p and not q:
            return True
        else:
            return False

* I rewrite with a ``return`` statement

  .. code-block:: python

    def material_non_implication(p, q):
        return p and not q

  and I am still green

----

*********************************************************************************
test_converse_implication
*********************************************************************************

red: make it fail
#################################################################################

I add a test for converse implication to ``TestBinaryOperations`` in ``test_truth_table.py``

.. code-block:: python

    def test_converse_implication(self):
        self.assertTrue(src.truth_table.converse_implication(True, True))
        self.assertTrue(src.truth_table.converse_implication(True, False))
        self.assertFalse(src.truth_table.converse_implication(False, True))
        self.assertTrue(src.truth_table.converse_implication(False, False))

the terminal shows :ref:`AttributeError`

green: make it pass
#################################################################################

* I add a :ref:`function<functions>` definition to ``truth_table.py``

  .. code-block:: python

    def converse_implication(p, q):
        return False

  and the terminal shows :ref:`AssertionError` for the first case
* I make the return value

  .. code-block:: python

    def converse_implication(p, q):
        return True

  the terminal shows :ref:`AssertionError` for the third case
* I add a condition for it and an explicit else_ clause

  .. code-block:: python

    def converse_implication(p, q):
        if p == False and q == True:
            return False
        else:
            return True

  all the tests pass

refactor: make it better
#################################################################################

* I change the ``if`` condition using python's implied conditional testing

  .. code-block:: python

    def converse_implication(p, q):
        if not p and q:
            return False
        else:
            return True

  the tests are still passing
* I make ``else`` to the opposite of the `if statement`_

  .. code-block:: python

    def converse_implication(p, q):
        if not p and q:
            return False
        if not (not p and q):
            return True

* When I "multiply" out the values in the second condition I get

  .. code-block:: python

    def converse_implication(p, q):
        if not p and q:
            return False
        if (not not p) (not and) (not q):
            return True

  the terminal shows a SyntaxError_
* which I fix by canceling out ``not not`` and replacing ``not and`` with or_

  .. code-block:: python

    def converse_implication(p, q):
        if not p and q:
            return False
        if p or not q:
            return True

* then reorder the statements

  .. code-block:: python

    def converse_implication(p, q):
        if p or not q:
            return True
        if not p and q:
            return False

* I change the second condition with ``else``

  .. code-block:: python

    def converse_implication(p, q):
        if p or not q:
            return True
        else:
            return False

* then simplify it to one line

  .. code-block:: python

    def converse_implication(p, q):
        return p or not q

  I win again! All tests pass

----

*********************************************************************************
review
*********************************************************************************


I ran tests for

* :ref:`logical negation<test_logical_negation>` which is not_
* :ref:`logical conjunction <test_logical_conjunction>` which is and_
* :ref:`logical NAND <test_logical_nand>`
* :ref:`logical disjunction <test_logical_disjunction>` which is or_
* :ref:`logical NOR <test_logical_nor>`
* :ref:`logical implication <test_logical_implication>`
* :ref:`converse non implication <test_converse_non_implication>`
* :ref:`logical equality <test_logical_equality>`
* :ref:`exclusive disjunction <test_exclusive_disjunction>`
* :ref:`material non-implication <test_material_non_implication>`
* :ref:`converse implication <test_converse_implication>`

do you want more :ref:`more binary operations? <truth table: Binary Operations III>`

----

:doc:`/code/code_truth_table`