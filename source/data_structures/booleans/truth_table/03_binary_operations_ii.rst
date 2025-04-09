.. include:: ../../../links.rst

.. _binary_operations_ii:

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
test_negate_first
*********************************************************************************

red: make it fail
#################################################################################

I add a test for negate first to ``TestBinaryOperations`` in ``test_truth_table.py``

.. code-block:: python

  def test_converse_non_implication(self):
      ...

  def test_negate_first(self):
      self.assertFalse(src.truth_table.negate_first(True, True))

and the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'negate_first'

green: make it pass
#################################################################################

I add the :ref:`function<functions>` definition

.. code-block:: python

  def converse_non_implication(p, q):
      return not p and q


  def negate_first(p, q):
      return not p and q

the test passes

refactor: make it better
#################################################################################

* I add the second case

  .. code-block:: python

    def test_negate_first(self):
        self.assertFalse(src.truth_table.negate_first(True, True))
        self.assertFalse(src.truth_table.negate_first(True, False))

  the test is still green. I add an `if statement`_

  .. code-block:: python

    def negate_first(p, q):
        if p == True and q == False:
            return True
        return not p and q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I fix the `return statement`_

  .. code-block:: python

    def negate_first(p, q):
        if p == True and q == False:
            return False
        return not p and q

  the test is green again

* I add the next case

  .. code-block:: python

    def test_negate_first(self):
        self.assertFalse(src.truth_table.negate_first(True, True))
        self.assertFalse(src.truth_table.negate_first(True, False))
        self.assertTrue(src.truth_table.negate_first(False, True))

  the terminal still shows green. I add another `if statement`_

  .. code-block:: python

    def negate_first(p, q):
        if p == False and q == True:
            return False
        if p == True and q == False:
            return False
        return not p and q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I fix the new statement

  .. code-block:: python

    def negate_first(p, q):
        if p == False and q == True:
            return True
        if p == True and q == False:
            return False
        return not p and q

  the test passes

* I add the last case

  .. code-block:: python

    def test_negate_first(self):
        self.assertFalse(src.truth_table.negate_first(True, True))
        self.assertFalse(src.truth_table.negate_first(True, False))
        self.assertTrue(src.truth_table.negate_first(False, True))
        self.assertTrue(src.truth_table.negate_first(False, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    def negate_first(p, q):
        if p == False and q == False:
            return True
        if p == False and q == True:
            return True
        if p == True and q == False:
            return False
        return not p and q

  the terminal shows green again

* The two cases where the :ref:`function<functions>` returns :ref:`True<test_what_is_true>` are when ``p`` is :ref:`False<test_what_is_false>` so I do not need ``q`` for this one, I add a new `if statement`_ with an else_ clause

  .. code-block:: python

    def negate_first(p, q):
        if p == False:
            return True
        else:
            return False
        if p == False and q == False:
            return True
        if p == False and q == True:
            return True
        if p == True and q == False:
            return False
        return not p and q

  the test is still green. I remove the other statements and use bool_

  .. code-block:: python

    def negate_first(p, q):
        if not bool(p):
        # if p == False:
            return True
        else:
            return False

  still green, I remove the commented line and simplify the `if statement`_

  .. code-block:: python

    def negate_first(p, q):
        if not p:
        # if not bool(p):
            return True
        else:
            return False

  the test is still green. I add a `ternary operator`_

  .. code-block:: python

    def negate_first(p, q):
        return True if not p else False
        if not p:
            return True
        else:
            return False

  which is the same as

  .. code-block:: python

    def negate_first(p, q):
        return not p
        return True if not p else False

  all the tests are still passing. I remove the second `return statement`

  .. code-block:: python

    def negate_first(p, q):
        return not p

  ah, just like the name

----

*********************************************************************************
test_logical_nand
*********************************************************************************

red: make it fail
#################################################################################

I add a new test

.. code-block:: python

  def test_negate_first(self):
      ...

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

  def negate_first(p, q):
      return not p


  def logical_nand(p, q):
      return not p

the terminal shows green

refactor: make it better
#################################################################################

* I add the next case

  .. code-block:: python

    def test_logical_nand(self):
        self.assertFalse(src.truth_table.logical_nand(True, True))
        self.assertTrue(src.truth_table.logical_nand(True, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I add an `if statement`_

  .. code-block:: python

    def logical_nand(p, q):
        if p == True and q == False:
            return True
        return not p

  the test passes

* I add another case

  .. code-block:: python

    def test_logical_nand(self):
        self.assertFalse(src.truth_table.logical_nand(True, True))
        self.assertTrue(src.truth_table.logical_nand(True, False))
        self.assertTrue(src.truth_table.logical_nand(False, True))

  the terminal shows green, I add an `if statement`_

  .. code-block:: python

    def logical_nand(p, q):
        if p == False and q == True:
            return False
        if p == True and q == False:
            return True
        return not p

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I change the statement

  .. code-block:: python

    def logical_nand(p, q):
        if p == False and q == True:
            return True
        if p == True and q == False:
            return True
        return not p

  green again

* I add the last case

  .. code-block:: python

    def test_logical_nand(self):
        self.assertFalse(src.truth_table.logical_nand(True, True))
        self.assertTrue(src.truth_table.logical_nand(True, False))
        self.assertTrue(src.truth_table.logical_nand(False, True))
        self.assertTrue(src.truth_table.logical_nand(False, False))

  the test passes. I add an `if statement`_ to see it fail

  .. code-block:: python

    def logical_nand(p, q):
        if p == False and q == False:
            return False
        if p == False and q == True:
            return True
        if p == True and q == False:
            return True
        return not p

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I change the `return statement`_

  .. code-block:: python

    def logical_nand(p, q):
        if p == False and q == False:
            return True
        if p == False and q == True:
            return True
        if p == True and q == False:
            return True
        return not p

* there are still only 2 results - :ref:`True<test_what_is_true>` in 3 cases and :ref:`False<test_what_is_false>` in one case. I add an `if statement`_ for that case with an else_ clause

  .. code-block:: python

    def logical_nand(p, q):
        if p == True and q == True:
            return False
        else:
            return True
        if p == False and q == False:
            return True
        if p == False and q == True:
            return True
        if p == True and q == False:
            return True
        return not p

  I use bool_ to rewrite the first `if statement`_, I did this with :ref:`Logical Conjunction<test_logical_conjunction>`

  .. code-block:: python

    def logical_nand(p, q):
        if bool(p) and bool(q):
        # if p == True and q == True:
            return False
        else:
            return True

  which is the same as

  .. code-block:: python

    def logical_nand(p, q):
        if p and q:
        # if bool(p) and bool(q):
            return False
        else:
            return True

  the test is still green. I want to use a `conditional expression`_, which means I have to rewrite this in terms of :ref:`True<test_what_is_true>`. I write the :ref:`logical negation<test_logical_negation>` of the `if statement`_ for the else_ clause with not_

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
        return True if not (p and q) else False
        if not (p and q):
            return True
        else:
            return False

  still green. I remove the other statements and use the simpler `return statement`

  .. code-block:: python

    def logical_nand(p, q):
        return not (p and q)
        return True if not (p and q) else False

  I remove the second `return statement`_

  .. code-block:: python

    def logical_nand(p, q):
        return not (p and q)

----

*********************************************************************************
test_tautology
*********************************************************************************

red: make it fail
#################################################################################

I add a test

.. code-block:: python

  def test_logical_nand(self):
      ...

  def test_tautology(self):
      self.assertTrue(src.truth_table.tautology(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'tautology'

green: make it pass
#################################################################################

I add a :ref:`function<functions>` definition

.. code-block:: python

  def logical_nand(p, q):
      return not (p and q)


  def tautology(p, q):
      return not (p and q)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: False is not true

I add an `if statement`_

.. code-block:: python

  def tautology(p, q):
      if p and q:
          return True
      return not (p and q)

the test passes

refactor: make it better
#################################################################################

* I add the next case

  .. code-block:: python

    def test_tautology(self):
        self.assertTrue(src.truth_table.tautology(True, True))
        self.assertTrue(src.truth_table.tautology(True, False))

  the terminal shows green. I add an `if statement`_

  .. code-block:: python

    def tautology(p, q):
        if p and not q:
            return False
        if p and q:
            return True
        return not (p and q)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I fix it

  .. code-block:: python

    def tautology(p, q):
        if p and not q:
            return True
        if p and q:
            return True
        return not (p and q)

  the test passes

* I add another case

  .. code-block:: python

    def test_tautology(self):
        self.assertTrue(src.truth_table.tautology(True, True))
        self.assertTrue(src.truth_table.tautology(True, False))
        self.assertTrue(src.truth_table.tautology(False, True))

  the test is still green. I add another `if statement`_

  .. code-block:: python

    def tautology(p, q):
        if not p and q:
            return False
        if p and not q:
            return True
        if p and q:
            return True
        return not (p and q)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I change the `return statement`

  .. code-block:: python

    def tautology(p, q):
        if not p and q:
            return True
        if p and not q:
            return True
        if p and q:
            return True
        return not (p and q)

  the test is green again

* I add the last case

  .. code-block:: python

    def test_tautology(self):
        self.assertTrue(src.truth_table.tautology(True, True))
        self.assertTrue(src.truth_table.tautology(True, False))
        self.assertTrue(src.truth_table.tautology(False, True))
        self.assertTrue(src.truth_table.tautology(False, False))

  still green. I add an `if statement`_

  .. code-block:: python

    def tautology(p, q):
        if not p and not q:
            return False
        if not p and q:
            return True
        if p and not q:
            return True
        if p and q:
            return True
        return not (p and q)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I change :ref:`False<test_what_is_false>` to :ref:`True<test_what_is_true>` in the `return statement`_

  .. code-block:: python

    def tautology(p, q):
        if not p and not q:
            return True
        if not p and q:
            return True
        if p and not q:
            return True
        if p and q:
            return True
        return not (p and q)

  the test is green again

* There is only one result for this operation, it is a :ref:`singleton function<test_singleton_functions>`, I do not need the `if statement`_

  .. code-block:: python

    def tautology(p, q):
        return True
        if not p and not q:
            return True
        if not p and q:
            return True
        if p and not q:
            return True
        if p and q:
            return True
        return not (p and q)

  the test passes and I remove the other statements

  .. code-block:: python

    def tautology(p, q):
        return True

----

*********************************************************************************
test_logical_disjunction
*********************************************************************************

red: make it fail
#################################################################################

I add another test to the ``TestBinaryOperations`` TestCase_

.. code-block:: python

  def test_logical_conjunction(self):
      ...

  def test_logical_disjunction(self):
      self.assertTrue(src.truth_table.logical_disjunction(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python
  :force:

  AttributeError: module 'src.truth_table' has no attribute 'logical_disjunction'. Did you mean: 'logical_conjunction'?

green: make it pass
#################################################################################

I add the :ref:`function<functions>`

.. code-block:: python

  def tautology(p, q):
      return True


  def logical_disjunction(p, q):
      return True

the test passes

refactor: make it better
#################################################################################

* I add the next case

  .. code-block:: python

    def test_logical_disjunction(self):
        self.assertTrue(src.truth_table.logical_disjunction(True, True))
        self.assertTrue(src.truth_table.logical_disjunction(True, False))

  the terminal still shows green which matches the return value of the :ref:`function<functions>`

* I add the next case

  .. code-block:: python

    def test_logical_disjunction(self):
        self.assertTrue(src.truth_table.logical_disjunction(True, True))
        self.assertTrue(src.truth_table.logical_disjunction(True, False))
        self.assertTrue(src.truth_table.logical_disjunction(False, True))

  the test is still green

* I add the fourth case

  .. code-block:: python

    def test_logical_disjunction(self):
        self.assertTrue(src.truth_table.logical_disjunction(True, True))
        self.assertTrue(src.truth_table.logical_disjunction(True, False))
        self.assertTrue(src.truth_table.logical_disjunction(False, True))
        self.assertFalse(src.truth_table.logical_disjunction(False, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    def logical_disjunction(p, q):
        if not p and not q:
            return False
        return True

  the test passes. I add an else_ clause to make it clearer

  .. code-block:: python

    def logical_disjunction(p, q):
        if not p and not q:
            return False
        else:
            return True

  the terminal still shows green

* I rewrite the else_ clause using not_ with the `if statement`_

  .. code-block:: python

    def logical_disjunction(p, q):
        if not p and not q:
            return False
        if not (not p and not q):
        # else:
            return True

  still green. I move the first two lines to the bottom then add an else_ clause

  .. code-block:: python

    def logical_disjunction(p, q):
        if not (not p and not q):
            return True
        else:
        # if not p and not q:
            return False

  the test is still green. I "multiply" not_ by each symbol in the parentheses to make it simpler

  .. code-block:: python

    def logical_disjunction(p, q):
        if not not p not and not not q:
        # if not (not p and not q):
            return True
        else:
            return False


  the terminal shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  I add it to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # AttributeError
    # TypeError
    # SyntaxError

  then I fix the line

  - not_ not_ cancels out
  - not_ and_ is or_

  .. code-block:: python

    def logical_disjunction(p, q):
        if p or q:
        # if not not p not and not not q:
        # if not (not p and not q):
            return True
        else:
            return False


  the test passes. I rewrite the statements as a `conditional expression`_

  .. code-block:: python

    def logical_disjunction(p, q):
        return p or q
        if p or q:
            return True
        else:
            return False


  the test is still green. I remove the `if statements`_

  .. code-block:: python

    def logical_disjunction(p, q):
        return p or q

----

*********************************************************************************
review
*********************************************************************************

From the tests I know that

* :ref:`Logical Disjunction <test_logical_disjunction>` returns ``p or q``
* :ref:`Tautology <test_tautology>` always returns :ref:`True<test_what_is_true>`
* :ref:`Logical NAND <test_logical_nand>` returns ``not (p and q)``
* :ref:`Negate First<test_negate_first>` always returns ``not p``
* :ref:`Converse NonImplication <test_converse_non_implication>` returns ``not p and q``
* :ref:`Project Second <test_project_second>` always returns ``q``
* :ref:`Logical Conjunction <test_logical_conjunction>` returns ``p and q``
* :ref:`Contradiction <test_contradiction>` always returns :ref:`False<test_what_is_false>`

do you want to test more :ref:`more binary operations? <truth table: Binary Operations III>`

----

:doc:`/code/code_truth_table`