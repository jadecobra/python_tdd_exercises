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
      self.assertTrue(src.truth_table.tautology(True, False))
      self.assertTrue(src.truth_table.tautology(False, True))
      self.assertTrue(src.truth_table.tautology(False, False))

the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'tautology'

green: make it pass
#################################################################################

I add a :ref:`function<functions>` definition

.. code-block:: python

  def project_second(p, q):
      return q


  def tautology(p, q):
      return q

refactor: make it better
#################################################################################

* I add the next case

  .. code-block:: python

    def test_tautology(self):
        self.assertTrue(src.truth_table.tautology(True, True))
        self.assertTrue(src.truth_table.tautology(True, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I add an `if statement`_

  .. code-block:: python

    def tautology(p, q):
        if p and not q:
            return True
        return q

  the test passes

* I add another case

  .. code-block:: python

    def test_tautology(self):
        self.assertTrue(src.truth_table.tautology(True, True))
        self.assertTrue(src.truth_table.tautology(True, False))
        self.assertTrue(src.truth_table.tautology(False, True))

  the test is still green

* I add the last case

  .. code-block:: python

    def test_tautology(self):
        self.assertTrue(src.truth_table.tautology(True, True))
        self.assertTrue(src.truth_table.tautology(True, False))
        self.assertTrue(src.truth_table.tautology(False, True))
        self.assertTrue(src.truth_table.tautology(False, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  there is only one result for this operation, it is a :ref:`singleton function<test_singleton_functions>`

  .. code-block:: python

    def tautology(p, q):
        return True
        if p and not q:
            return True
        return q

  the test passes and I remove the other statements

  .. code-block:: python

    def tautology(p, q):
        return True

----

*********************************************************************************
test_logical_equality
*********************************************************************************

red: make it fail
#################################################################################

I add a new test

.. code-block:: python

  def test_converse_implication(self):
      ...

  def test_logical_equality(self):
      self.assertTrue(src.truth_table.logical_equality(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python
  :force:

  AttributeError: module 'src.truth_table' has no attribute 'logical_equality'. Did you mean: 'logical_identity'?

green: make it pass
#################################################################################

* I add a :ref:`function<functions>` definition

  .. code-block:: python

    def converse_implication(p, q):
        return p or not q


    def logical_equality(p, q):
        return p or not q

  the terminal shows green

refactor: make it better
#################################################################################

* I add the next case

  .. code-block:: python

    def test_logical_equality(self):
        self.assertTrue(src.truth_table.logical_equality(True, True))
        self.assertFalse(src.truth_table.logical_equality(True, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I add an `if statement`_

  .. code-block:: python

    def logical_equality(p, q):
        if p == True and q == False:
            return False
        return p or not q

  the terminal shows green again

* I add another case

  .. code-block:: python

    def test_logical_equality(self):
        self.assertTrue(src.truth_table.logical_equality(True, True))
        self.assertFalse(src.truth_table.logical_equality(True, False))
        self.assertFalse(src.truth_table.logical_equality(False, True))

  the terminal still shows green. I add an `if statement`_ to make sure

  .. code-block:: python

    def logical_equality(p, q):
        if p == False and q == True:
            return True
        if p == True and q == False:
            return False
        return p or not q

  which gives me :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I change the `return statement`_

  .. code-block:: python

    def logical_equality(p, q):
        if p == False and q == True:
            return False
        if p == True and q == False:
            return False
        return p or not q

  the test passes

* I add the last case

  .. code-block:: python

    def test_logical_equality(self):
        self.assertTrue(src.truth_table.logical_equality(True, True))
        self.assertFalse(src.truth_table.logical_equality(True, False))
        self.assertFalse(src.truth_table.logical_equality(False, True))
        self.assertTrue(src.truth_table.logical_equality(False, False))

  and the test is still green. I add an `if statement`

  .. code-block:: python

    def logical_equality(p, q):
        if p == False and q == False:
            return False
        if p == False and q == True:
            return False
        if p == True and q == False:
            return False
        return p or not q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I fix the line then add an `if statement` for the first case

  .. code-block:: python

    def logical_equality(p, q):
        if p == False and q == False:
            return True
        if p == False and q == True:
            return False
        if p == True and q == False:
            return False
        if p == True and q == True:
            return False
        return p or not q

  which gives me :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I fix the `return statement`_ and remove ``return p or not q``

  .. code-block:: python

    def logical_equality(p, q):
        if p == False and q == False:
            return True
        if p == False and q == True:
            return False
        if p == True and q == False:
            return False
        if p == True and q == True:
            return True

  the test is green again

* There are still only two results, this time :ref:`True<test_what_is_true>` happens in two of the cases and :ref:`False<test_what_is_false>` happens in the other two. I move the `if statement`_ for the first case to the top so I have the two cases that return :ref:`True<test_what_is_true>` together

  .. code-block:: python

    def logical_equality(p, q):
        if p == True and q == True:
            return True
        if p == False and q == False:
            return True
        if p == False and q == True:
            return False
        if p == True and q == False:
            return False

  still green. I rewrite the first line

  .. code-block:: python

    def logical_equality(p, q):
        if bool(p) and bool(q):
        # if p == True and q == True:
            return True
        if p == False and q == False:
            return True
        if p == False and q == True:
            return False
        if p == True and q == False:
            return False

  the terminal still shows green. I make the line simpler

  .. code-block:: python

    def logical_equality(p, q):
        if p and q:
        # if bool(p) and bool(q):
            return True
        if p == False and q == False:
            return True
        if p == False and q == True:
            return False
        if p == True and q == False:
            return False

  I rewrite the second `if statement`_ in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python

    def logical_equality(p, q):
        if p and q:
            return True
        if p != True and q != True:
        # if p == False and q == False:
            return True
        if p == False and q == True:
            return False
        if p == True and q == False:
            return False

  the terminal still shows green. I rewrite it with bool_

  .. code-block:: python

    def logical_equality(p, q):
        if p and q:
            return True
        if not bool(p) and not bool(q):
        # if p != True and q != True:
            return True
        if p == False and q == True:
            return False
        if p == True and q == False:
            return False

  still green, I make the line simpler

  .. code-block:: python

    def logical_equality(p, q):
        if p and q:
            return True
        if not p and not q:
        # if not bool(p) and not bool(q):
            return True
        if p == False and q == True:
            return False
        if p == True and q == False:
            return False

  the terminal still shows green. not_ happens twice on this line, I try to factor it out like in Algebra_

  .. code-block:: python

    def logical_equality(p, q):
        if p and q:
            return True
        if not (p and q):
        # if not p and not q:
            return True
        if p == False and q == True:
            return False
        if p == True and q == False:
            return False

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I made a mistake. I "multiply" out the statement to check what I wrote

  .. code-block:: python

    def logical_equality(p, q):
        if p and q:
            return True
        if not (p and q):
        if not p not and not q:
        # if not p and not q:
            return True
        if p == False and q == True:
            return False
        if p == True and q == False:
            return False

  the mistake is that ``not and`` is or_, I need something that multiplies out to ``if not p not or not q``. I change the statement

  .. code-block:: python

    def logical_equality(p, q):
        if p and q:
            return True
        if not (p or q):
        # if not p not or not q:
        # if not p and not q:
            return True
        if p == False and q == True:
            return False
        if p == True and q == False:
            return False

  green again

* I can use or_ to put the two cases that are :ref:`True<test_what_is_true>` together

  .. code-block:: python

    def logical_equality(p, q):
        if (p and q) or not (p or q):
            return True
        else:
            return False
        if p and q:
            return True
        if not (p or q):
            return True
        if p == False and q == True:
            return False
        if p == True and q == False:
            return False

  still green. I remove the other statements then use a `conditional expression`_

  .. code-block:: python

    def logical_equality(p, q):
        return True if (p and q) or not (p or q) else False
        if (p and q) or not (p or q):
            return True
        else:
            return False

  the terminal shows green. I remove the other statements and make it simpler

  .. code-block:: python

    def logical_equality(p, q):
        return (p and q) or not (p or q)
        return True if (p and q) or not (p or q) else False

  still green. I remove the second `return statement`_

  .. code-block:: python

    def logical_equality(p, q):
        return (p and q) or not (p or q)

  and all tests are still passing. All of this could have been done with the ``==`` symbol, since the two cases where :ref:`True<test_what_is_true>` is the result are cases where ``p`` and ``q`` are the same

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

----

*********************************************************************************
test_negate_second
*********************************************************************************

red: make it fail
#################################################################################

I add a test

.. code-block:: python

  def test_negate_second(self):
      self.assertFalse(src.truth_table.negate_second(True, True))

and the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'negate_second'

green: make it pass
#################################################################################

I add a :ref:`function<functions>` definition to ``truth_table.py``

.. code-block:: python

  def contradiction(p, q):
      return False


  def negate_second(p, q):
      return False

the test passes

refactor: make it better
#################################################################################

* I add the next case

  .. code-block:: python

    def test_negate_second(self):
        self.assertFalse(src.truth_table.negate_second(True, True))
        self.assertTrue(src.truth_table.negate_second(True, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I add an `if statement`_

  .. code-block:: python

    def negate_second(p, q):
        if p and not q:
            return True
        return False

  the test passes

* I add the third case

  .. code-block:: python

    def test_negate_second(self):
        self.assertFalse(src.truth_table.negate_second(True, True))
        self.assertTrue(src.truth_table.negate_second(True, False))
        self.assertFalse(src.truth_table.negate_second(False, True))

  the test is still passing

* I add another case

  .. code-block:: python

    def test_negate_second(self):
        self.assertFalse(src.truth_table.negate_second(True, True))
        self.assertTrue(src.truth_table.negate_second(True, False))
        self.assertFalse(src.truth_table.negate_second(False, True))
        self.assertTrue(src.truth_table.negate_second(False, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I add another `if statement`_

  .. code-block:: python

  the test is green again

* The two `if statements`_ that return :ref:`True<test_what_is_true>` have ``not q``, so I write and `if statement`_ with it

  .. code-block:: python

    def negate_second(p, q):
        if not q:
            return True
        else:
            return False
        if not p and not q:
            return True
        if p and not q:
            return True
        return False

  the terminal still shows green. I use a `ternary operator`_

  .. code-block:: python

    def negate_second(p, q):
        return not q
        if not q:
            return True
        else:
            return False

  still green. I remove the other statements

  .. code-block:: python

    def negate_second(p, q):
        return not q

----

*********************************************************************************
review
*********************************************************************************

From the tests I know that

* :ref:`Contradiction <test_contradiction>` always returns :ref:`False<test_what_is_false>`
* :ref:`Tautology <test_tautology>` always returns :ref:`True<test_what_is_true>`
* :ref:`Negate Second <test_negate_second>` always returns ``not q``
* :ref:`Project Second <test_project_second>` always returns ``q``
* :ref:`Negate First<test_negate_first>` always returns ``not p``
* :ref:`Project First <test_project_first>` always returns ``p``
* :ref:`Logical Equality <test_logical_equality>` is ``==``
*  :ref:`Converse Implication <test_converse_implication>` returns ``p or not q``
* :ref:`Logical or Material Implication  <test_logical_implication>` returns ``not p or q``
* :ref:`Logical Disjunction <test_logical_disjunction>` is or_
* :ref:`Logical Conjunction <test_logical_conjunction>` is and_
* :ref:`Logical Negation<test_logical_negation>` is not_


do you want to test more :ref:`more binary operations? <truth table: Binary Operations III>`

----

:doc:`/code/code_truth_table`