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
      return p or not q

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: True is not false

I add an `if statement`_

.. code-block:: python

  def negate_second(p, q):
      if p and q:
          return False
      return p or not q

the test passes

refactor: make it better
#################################################################################

* I add the next case

  .. code-block:: python

    def test_negate_second(self):
        self.assertFalse(src.truth_table.negate_second(True, True))
        self.assertTrue(src.truth_table.negate_second(True, False))

  the test is still green. I add an `if statement`_

  .. code-block:: python

    def negate_second(p, q):
        if p and not q:
            return False
        if p and q:
            return False
        return p or not q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I change the statement

  .. code-block:: python

    def negate_second(p, q):
        if p and not q:
            return True
        if p and q:
            return False
        return p or not q

  the test is green again

* I add the third case

  .. code-block:: python

    def test_negate_second(self):
        self.assertFalse(src.truth_table.negate_second(True, True))
        self.assertTrue(src.truth_table.negate_second(True, False))
        self.assertFalse(src.truth_table.negate_second(False, True))

  the test is still passing. I add an `if statement`_

  .. code-block:: python

    def negate_second(p, q):
        if not p and q:
            return True
        if p and not q:
            return True
        if p and q:
            return False
        return p or not q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I fix the line

  .. code-block:: python

    def negate_second(p, q):
        if not p and q:
            return False
        if p and not q:
            return True
        if p and q:
            return False
        return p or not q

  and the test passes

* then I add another case

  .. code-block:: python

    def test_negate_second(self):
        self.assertFalse(src.truth_table.negate_second(True, True))
        self.assertTrue(src.truth_table.negate_second(True, False))
        self.assertFalse(src.truth_table.negate_second(False, True))
        self.assertTrue(src.truth_table.negate_second(False, False))

  the test is still green. I add an `if statement`_

  .. code-block:: python

    def negate_second(p, |q):
        if not p and not q:
            return False
        if not p and q:
            return False
        if p and not q:
            return True
        if p and q:
            return False
        return p or not q|

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I fix the `return statement`_ and remove ``return p or not q``

  .. code-block:: python

    def negate_second(p, q):
        if not p and not q:
            return True
        if not p and q:
            return False
        if p and not q:
            return True
        if p and q:
            return False

  the test is green again

* This test expects :ref:`True<test_what_is_true>` in 2 of the cases and :ref:`False<test_what_is_false>` in the other 2. The 2 `if statements`_ that return :ref:`True<test_what_is_true>` have ``not q``, so I write a `conditional expression`_ with it

  .. code-block:: python

    def negate_second(p, q):
        return not q
        if not p and not q:
            return True
        if not p and q:
            return False
        if p and not q:
            return True
        if p and q:
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
      return not q

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
        return not q

  the test passes

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

  still green

* I add an `if statement`_ with an else_ clause for the last case which returns :ref:`True<test_what_is_true>`

  .. code-block:: python

    def logical_nor(p, q):
        if not p and not q:
            return True
        else:
            return False
        if p and not q:
            return False
        return not q

  the terminal still shows green, I remove the other statements and rewrite the `if statement`_ to factor out not_ since it happens 2 times

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
            return True
        else:
            return False

  still green, I remove the other statements

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
      return not (p or q)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: False is not true

I add an `if statement`_

.. code-block:: python

  def logical_equality(p, q):
      if p and q:
          return True
      return not (p or q)

the test passes

refactor: make it better
#################################################################################

* I add the next case

  .. code-block:: python

    def test_logical_equality(self):
        self.assertTrue(src.truth_table.logical_equality(True, True))
        self.assertFalse(src.truth_table.logical_equality(True, False))

  the test is still green

* I add another case

  .. code-block:: python

    def test_logical_equality(self):
        self.assertTrue(src.truth_table.logical_equality(True, True))
        self.assertFalse(src.truth_table.logical_equality(True, False))
        self.assertFalse(src.truth_table.logical_equality(False, True))

  the terminal still shows green

* I add the last case

  .. code-block:: python

    def test_logical_equality(self):
        self.assertTrue(src.truth_table.logical_equality(True, True))
        self.assertFalse(src.truth_table.logical_equality(True, False))
        self.assertFalse(src.truth_table.logical_equality(False, True))
        self.assertTrue(src.truth_table.logical_equality(False, False))

  and the test is still green

* This test expects :ref:`True<test_what_is_true>` in 2 of the cases and :ref:`False<test_what_is_false>`  in the other 2. I add an `if statement`_ for the other case where :ref:`True<test_what_is_true>` is expected

  .. code-block:: python

    def logical_equality(p, q):
        if not p and not q:
            return False
        if p and q:
            return True
        return not (p or q)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I fix the `return statement`_

  .. code-block:: python

    def logical_equality(p, q):
        if not p and not q:
            return True
        if p and q:
            return True
        return not (p or q)

  the test is green again. I factor out not_ like I did in :ref:`Negate Second <test_negate_second>` since it happens 2 times in this statement

  .. code-block:: python

    def logical_equality(p, q):
        if not (p or q):
        # if not p and not q:
            return True
        if p and q:
            return True
        return not (p or q)

  the terminal still shows green

* I use or_ to make 1 `if statement`_ for these 2 cases

  .. code-block:: python

    def logical_equality(p, q):
        if not (p or q) or (p and q):
            return True
        else:
            return False
        if not (p or q):
            return True
        if p and q:
            return True
        return not (p or q)

  still green. I remove the other statements and use a `conditional expression`_

  .. code-block:: python

    def logical_equality(p, q):
        return not (p or q) or (p and q)
        if not (p or q) or (p and q):
            return True
        else:
            return False

  the terminal shows green. I remove the other statements

  .. code-block:: python

    def logical_equality(p, q):
        return (p and q) or not (p or q)

  and all tests are still passing. All of this could have been done with the ``==`` symbol, since the 2 cases where :ref:`True<test_what_is_true>` is the result are cases where ``p`` and ``q`` are the same

  .. code-block:: python

    def logical_equality(p, q):
        if p == q:
            return True
        else:
            return False

  which is the same as the `conditional expression`_

  .. code-block:: python

    def logical_equality(p, q):
        return p == q

----

*********************************************************************************
test_logical_or_material_implication
*********************************************************************************

red: make it fail
#################################################################################

I add a new test

.. code-block:: python

  def test_logical_equality(self):
      ...

  def test_logical_or_material_implication(self):
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
      return not (p or q) or (p and q)


  def logical_implication(p, q):
      return p == q

the test passes

refactor: make it better
#################################################################################

* I add the next case

  .. code-block:: python

    def test_logical_or_material_implication(self):
        self.assertTrue(src.truth_table.logical_implication(True, True))
        self.assertFalse(src.truth_table.logical_implication(True, False))

  the terminal shows green again

* I add the next case

  .. code-block:: python

    def test_logical_or_material_implication(self):
        self.assertTrue(src.truth_table.logical_implication(True, True))
        self.assertFalse(src.truth_table.logical_implication(True, False))
        self.assertTrue(src.truth_table.logical_implication(False, True))

  the terminal shows shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I add an `if statement`_

  .. code-block:: python

    def logical_implication(p, q):
        if not p and q:
            return True
        return p == q

  the test is green again

* I add the fourth case

  .. code-block:: python

    def test_logical_or_material_implication(self):
        self.assertTrue(src.truth_table.logical_implication(True, True))
        self.assertFalse(src.truth_table.logical_implication(True, False))
        self.assertTrue(src.truth_table.logical_implication(False, True))
        self.assertTrue(src.truth_table.logical_implication(False, False))

  the terminal shows green

* I add an `if statement`_ with an else_ clause for the case where the result is :ref:`False<test_what_is_false>`

  .. code-block:: python

    def logical_implication(p, q):
        if p and not q:
            return False
        else:
            return True
        if not p and q:
            return True
        return p == q

  the terminal still shows green. I rewrite the else_ block as the :ref:`logical negation<test_logical_negation>` of the `if statement`_

  .. code-block:: python

    def logical_implication(p, q):
        if p and not q:
            return False
        if not (p and not q):
        # else:
            return True

  still green. I move the `if statement`_ that returns :ref:`True <test_what_is_true>` to the top then change the second statement to an else_ clause

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

  - not_ not_ cancels out
  - not_ and_ is or_

  .. code-block:: python

    def logical_implication(p, q):
        if not p or q:
        # if not p not and not not q:
        # if not (p and not q):
            return True
        else:
            return False

  the test is passing again. I use a `ternary operator`_

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

* :ref:`Logical or Material Implication  <test_logical_or_material_implication>` returns ``not p or q``
* :ref:`Logical Equality <test_logical_equality>` is ``==``
* :ref:`Logical NOR <test_logical_nor>` returns ``not (p or q)``
* :ref:`Negate Second <test_negate_second>` always returns ``not q``
*  :ref:`Converse Implication <test_converse_implication>` returns ``p or not q``
* :ref:`Project First <test_project_first>` always returns ``p``
* :ref:`Material NonImplication <test_material_non_implication>` returns ``p and not q``
* :ref:`Exclusive Disjunction <test_exclusive_disjunction>` is ``!=``, or the :ref:`Logical Negation<test_logical_negation>` of :ref:`Logical Equality <test_logical_equality>`
* :ref:`Logical Disjunction <test_logical_disjunction>` returns ``p or q``
* :ref:`Tautology <test_tautology>` always returns :ref:`True<test_what_is_true>`
* :ref:`Logical NAND <test_logical_nand>` returns ``not (p and q)``
* :ref:`Negate First<test_negate_first>` always returns ``not p``
* :ref:`Converse NonImplication <test_converse_non_implication>` returns ``not p and q``
* :ref:`Project Second <test_project_second>` always returns ``q``
* :ref:`Logical Conjunction <test_logical_conjunction>` returns ``p and q``
* :ref:`Contradiction <test_contradiction>` always returns :ref:`False<test_what_is_false>`

Would you like to :ref:`test the truth table tests?<test_truth_table_tests>`

----

:doc:`/code/code_truth_table`