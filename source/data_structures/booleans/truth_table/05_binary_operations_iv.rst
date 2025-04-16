.. include:: ../../../links.rst

.. _binary_operations_iv:

#################################################################################
truth table: Binary Operations IV
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
test_negate_second
*********************************************************************************

red: make it fail
#################################################################################

I add a test

.. code-block:: python

  def test_converse_implication(self):
      ...

  def test_negate_second(self):
      self.assertFalse(src.truth_table.negate_second(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'negate_second'

green: make it pass
#################################################################################

I add a :ref:`function<functions>` definition to ``truth_table.py``

.. code-block:: python

  def converse_implication(p, q):
      return p or not q


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

* then I add another case

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

    def negate_second(p, q):
        if not p and not q:
            return True
        if p and not q:
            return True
        return False


  the test is green again

* the :ref:`function<functions>` returns :ref:`True<test_what_is_true>` when ``q`` is :ref:`False<test_what_is_false>` so I write a `conditional expression`_ with it

  .. code-block:: python

    def negate_second(p, q):
        return not q
        if not p and not q:
            return True
        if p and not q:
            return True
        return False


  the terminal still shows green. I remove the other statements

  .. code-block:: python

    def negate_second(p, q):
        return not q

----

*********************************************************************************
test_logical_nor
*********************************************************************************

red: make it fail
#################################################################################

I add another test

.. code-block:: python

    def test_material_non_implication(self):
        ...

    def test_logical_nor(self):
        self.assertFalse(src.truth_table.logical_nor(True, True))

and the terminal shows :ref:`AttributeError`

.. code-block:: python
  :force:

  AttributeError: module 'src.truth_table' has no attribute 'logical_nor'. Did you mean: 'logical_nand'?

green: make it pass
#################################################################################

I add a :ref:`function<functions>`

.. code-block:: python

  def negate_second(p, q):
      return not q


  def logical_nor(p, q):
      return False

the test passes

refactor: make it better
#################################################################################

* I add the next case

  .. code-block:: python

    def test_logical_nor(self):
        self.assertFalse(src.truth_table.logical_nor(True, True))
        self.assertFalse(src.truth_table.logical_nor(True, False))

  the terminal still shows green

* on to the next case

  .. code-block:: python

    def test_logical_nor(self):
        self.assertFalse(src.truth_table.logical_nor(True, True))
        self.assertFalse(src.truth_table.logical_nor(True, False))
        self.assertFalse(src.truth_table.logical_nor(False, True))

  the test is still green

* I add the last case

  .. code-block:: python

    def test_logical_nor(self):
        self.assertFalse(src.truth_table.logical_nor(True, True))
        self.assertFalse(src.truth_table.logical_nor(True, False))
        self.assertFalse(src.truth_table.logical_nor(False, True))
        self.assertTrue(src.truth_table.logical_nor(False, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I add a `conditional expression`_

  .. code-block:: python

    def logical_nor(p, q):
        return not p and not q
        return False

* I want to factor out not_ since it happens 2 times

  .. code-block:: python

    def logical_nor(p, q):
        return not p not and not q
        return not p and not q

  the terminal shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  I fix the line - not_ and_ is or_

  .. code-block:: python

    def logical_nor(p, q):
        return not p or not q
        return not p and not q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I made a mistake with my "factoring", I should have used ``not or`` to replace ``and``. I try again

  .. code-block:: python

    def logical_nor(p, q):
        return not p not or not q
        return not p and not q

  the terminal shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  I factor out the not_

  .. code-block:: python

    def logical_nor(p, q):
        return not (p or q)
        # return not p not or not q
        return not p and not q

  green again, I remove the other statements

  .. code-block:: python

    def logical_nor(p, q):
        return not (p or q)

----

*********************************************************************************
test_logical_equality
*********************************************************************************

red: make it fail
#################################################################################

I add a new test

.. code-block:: python

  def test_logical_nor(self):
      ...

  def test_logical_equality(self):
      self.assertTrue(src.truth_table.logical_equality(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python
  :force:

  AttributeError: module 'src.truth_table' has no attribute 'logical_equality'. Did you mean: 'logical_identity'?

green: make it pass
#################################################################################

I add a :ref:`function<functions>` definition

.. code-block:: python

  def logical_nor(p, q):
      return not (p or q)


  def logical_equality(p, q):
      return True

the test passes

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
        if p and not q:
            return False
        return True

  the test passes

* I add another case

  .. code-block:: python

    def test_logical_equality(self):
        self.assertTrue(src.truth_table.logical_equality(True, True))
        self.assertFalse(src.truth_table.logical_equality(True, False))
        self.assertFalse(src.truth_table.logical_equality(False, True))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I add another `if statement`_

  .. code-block:: python

    def logical_equality(p, q):
        if not p and q:
            return False
        if p and not q:
            return False
        return True

  the test passes

* I add the last case

  .. code-block:: python

    def test_logical_equality(self):
        self.assertTrue(src.truth_table.logical_equality(True, True))
        self.assertFalse(src.truth_table.logical_equality(True, False))
        self.assertFalse(src.truth_table.logical_equality(False, True))
        self.assertTrue(src.truth_table.logical_equality(False, False))

  and the test is still green

* This test expects :ref:`True<test_what_is_true>` in 2 of the cases and :ref:`False<test_what_is_false>`  in the other 2. I use or_ to put the 2 statements that return :ref:`False<test_what_is_false>` together

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
        return True

  still green. I use not_ to write another `if statement`_

  .. code-block:: python

    def logical_equality(p, q):
        if (not p and q) or (p and not q):
            return False
        if not ((not p and q) or (p and not q)):
        # else:
            return True

  still green. I change the order

  .. code-block:: python

    def logical_equality(p, q):
        if not ((not p and q) or (p and not q)):
            return True
        else:
        # if (not p and q) or (p and not q):
            return False

  the test is still green. I multiply not_ by every symbol in the parentheses

  .. code-block:: python

    def logical_equality(p, q):
        if not (not p and q) not or not (p and not q):
        # if not ((not p and q) or (p and not q)):
            return True
        else:
            return False

  the terminal shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  I fix the line - not_ or_ is and_

  .. code-block:: python

    def logical_equality(p, q):
        if not (not p and q) and not (p and not q):
        # if not (not p and q) not or not (p and not q):
        # if not ((not p and q) or (p and not q)):
            return True
        else:
            return False

  the test is green again. I "multiply" not_ by each symbol in the parentheses

  .. code-block:: python

    def logical_equality(p, q):
        if (not not p not and not q) and (not p not and not not q):
        # if not (not p and q) and not (p and not q):
            return True
        else:
            return False

  the terminal shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  I fix the line

  - not_ not_ cancels out
  - not_ and_ is or

  .. code-block:: python

    def logical_equality(p, q):
        if (p or not q) and (not p or q):
        # if (not not p not and not q) and (not p not and not not q):
        # if not (not p and q) and not (p and not q):
            return True
        else:
            return False

  the test is green again. I remove the other statements and use a `conditional expression`_

  .. code-block:: python

    def logical_equality(p, q):
        return (p or not q) and (not p or q)
        if (p or not q) and (not p or q):
            return True
        else:
            return False

  the terminal shows green. I remove the other statements

  .. code-block:: python

    def logical_equality(p, q):
        return (p or not q) and (not p or q)

  and all tests are still passing.

* All of this could have been done with the ``==`` symbol, since the 2 cases where :ref:`True<test_what_is_true>` is the result are cases where ``p`` and ``q`` are the same

  .. code-block:: python

    def logical_equality(p, q):
        if p == q:
            return True
        else:
            return False
        return (p or not q) and (not p or q)

  which is the same as the `conditional expression`_

  .. code-block:: python

    def logical_equality(p, q):
        return p == q
        if p == q:
            return True
        else:
            return False
        return (p or not q) and (not p or q)

  I remove the other statements

  .. code-block:: python

    def logical_equality(p, q):
        return p == q
        return (p or not q) and (not p or q)

----

*********************************************************************************
test_material_implication
*********************************************************************************

red: make it fail
#################################################################################

I add a new test

.. code-block:: python

  def test_logical_equality(self):
      ...

  def test_material_implication(self):
      self.assertTrue(src.truth_table.logical_implication(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python
  :force:

  AttributeError: module 'src.truth_table' has no attribute 'logical_implication'. Did you mean: 'logical_disjunction'?

green: make it pass
#################################################################################

I add the :ref:`method<functions>`

.. code-block:: python

  def logical_equality(p, q):
      return p == q
      return (p or not q) and (not p or q)


  def logical_implication(p, q):
      return True

the test passes

refactor: make it better
#################################################################################

* I add the next case

  .. code-block:: python

    def test_material_implication(self):
        self.assertTrue(src.truth_table.logical_implication(True, True))
        self.assertFalse(src.truth_table.logical_implication(True, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I add `if statement`_

  .. code-block:: python

    def logical_implication(p, q):
        if p and not q:
            return False
        return True

  the terminal shows green

* I add the next case

  .. code-block:: python

    def test_material_implication(self):
        self.assertTrue(src.truth_table.logical_implication(True, True))
        self.assertFalse(src.truth_table.logical_implication(True, False))
        self.assertTrue(src.truth_table.logical_implication(False, True))

  the test is still green

* I add the fourth case

  .. code-block:: python

    def test_material_implication(self):
        self.assertTrue(src.truth_table.logical_implication(True, True))
        self.assertFalse(src.truth_table.logical_implication(True, False))
        self.assertTrue(src.truth_table.logical_implication(False, True))
        self.assertTrue(src.truth_table.logical_implication(False, False))

  the test is still passing

* I use not_ to add another `if statement`_ for the other cases

  .. code-block:: python

    def logical_implication(p, q):
        if p and not q:
            return False
        if not (p and not q):
            return True

  I change the order then add an else_ clause

  .. code-block:: python

    def logical_implication(p, q):
        if not (p and not q):
            return True
        else:
        # if p and not q:
            return False

  still green, I "multiply" not_ by every symbol in the parentheses

  .. code-block:: python

    def logical_implication(p, q):
        if not p not and not not q:
        # if not (p and not q):
            return True
        else:
            return False

  the terminal shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  I fix the line

  - not_ and_ is or_
  - not_ not_ cancels out

  .. code-block:: python

    def logical_implication(p, q):
        if not p or q:
        # if not p not and not not q:
        # if not (p and not q):
            return True
        else:
            return False

  the test is passing again. I add a simple `return statement`_

  .. code-block:: python

    def logical_implication(p, q):
        return not p or q
        if not p or q:
            return True
        else:
            return False

  and all tests are still passing. I remove the rest of the statements

  .. code-block:: python

    def logical_implication(p, q):
        return not p or q

----

*********************************************************************************
review
*********************************************************************************

From the tests I know that

* :ref:`Logical or Material Implication  <test_material_implication>` returns ``not p or q``
* :ref:`Logical Equality <test_logical_equality>` returns ``p == q``
* :ref:`Logical NOR <test_logical_nor>` returns ``not (p or q)``
* :ref:`Negate Second <test_negate_second>` always returns ``not q``
*  :ref:`Converse Implication <test_converse_implication>` returns ``p or not q``
* :ref:`Project First <test_project_first>` always returns ``p``
* :ref:`Material NonImplication <test_material_non_implication>` returns ``p and not q``
* :ref:`Exclusive Disjunction <test_exclusive_disjunction>` returns ``p != q``
* :ref:`Logical Disjunction <test_logical_disjunction>` returns ``p or q``
* :ref:`Tautology <test_tautology>` always returns :ref:`True<test_what_is_true>`
* :ref:`Logical NAND <test_logical_nand>` returns ``not (p and q)``
* :ref:`Negate First<test_negate_first>` always returns ``not p``
* :ref:`Converse NonImplication <test_converse_non_implication>` returns ``not p and q``
* :ref:`Project Second <test_project_second>` always returns ``q``
* :ref:`Logical Conjunction <test_logical_conjunction>` returns ``p and q``
* :ref:`Contradiction <test_contradiction>` always returns :ref:`False<test_what_is_false>`
* :ref:`Logical Negation<test_logical_negation>` is not_

Would you like to :ref:`test the truth table tests?<test_truth_table_tests>`

----

:doc:`/code/code_truth_table`