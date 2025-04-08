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
test_tautology
*********************************************************************************

red: make it fail
#################################################################################

I add a test

.. code-block:: python

  def test_project_second(self):
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


do you want more :ref:`more binary operations? <truth table: Binary Operations III>`

----

:doc:`/code/code_truth_table`