.. include:: ../../../links.rst

#################################################################################
truth table: Binary Operations III
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
      if p and q:
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
        if p and not q:
            return True
        if p and q:
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
        if not p and q:
            return True
        if p and not q:
            return True
        if p and q:
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
        if not p and not q:
            return False
        if not p and q:
            return True
        if p and not q:
            return True
        if p and q:
            return False
        return p == q

  the terminal shows green

* I remove ``return p == q`` and move the last case to the bottom to put the two cases that return :ref:`True<test_what_is_true>` together

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if not p and q:
            return True
        if p and not q:
            return True
        if p and q:
            return False
        if not p and not q:
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
        if p and q:
            return False
        if not p and not q:
            return False

  the terminal still shows green. I remove the other `if statements`_ and use a `conditional expression`_

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

* since the :ref:`function<functions>` returns :ref:`True<test_what_is_true>` in the two cases when ``p`` and ``q`` are NOT the same, it could also be written as

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
test_converse_non_implication
*********************************************************************************

red: make it fail
#################################################################################

I add a new test

.. code-block:: python

    def test_exclusive_disjunction(self):
        ...

    def test_converse_non_implication(self):
        self.assertFalse(src.truth_table.converse_non_implication(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python
  :force:

  AttributeError: module 'src.truth_table' has no attribute 'converse_non_implication'. Did you mean: 'converse_implication'?

green: make it pass
#################################################################################

I add the :ref:`function<functions>`

.. code-block:: python

  def exclusive_disjunction(p, q):
      return p != q
      return not (p == q)
      return (not p and q) or (p and not q)


  def converse_non_implication(p, q):
      return p != q

the terminal shows green

refactor: make it better
#################################################################################

* I add the second case

  .. code-block:: python

    def test_converse_non_implication(self):
        self.assertFalse(src.truth_table.converse_non_implication(True, True))
        self.assertFalse(src.truth_table.converse_non_implication(True, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I add an `if statement`_

  .. code-block:: python

    def converse_non_implication(p, q):
        if p and not q:
            return False
        return p != q

  the test passes

* I add the third case

  .. code-block:: python

    def test_converse_non_implication(self):
        self.assertFalse(src.truth_table.converse_non_implication(True, True))
        self.assertFalse(src.truth_table.converse_non_implication(True, False))
        self.assertTrue(src.truth_table.converse_non_implication(False, True))

  the test is still green

* I add the fourth case

  .. code-block:: python

    def test_converse_non_implication(self):
        self.assertFalse(src.truth_table.converse_non_implication(True, True))
        self.assertFalse(src.truth_table.converse_non_implication(True, False))
        self.assertTrue(src.truth_table.converse_non_implication(False, True))
        self.assertFalse(src.truth_table.converse_non_implication(False, False))

  the terminal still shows green

* I add an `if statement`_ with an else_ clause for the case where the result is :ref:`True<test_what_is_true>`

  .. code-block:: python

    def converse_non_implication(p, q):
        if not p and q:
            return True
        else:
            return False
        if p and not q:
            return False
        return p != q

  the terminal still shows green. I use a `conditional expression`

  .. code-block:: python

    def converse_non_implication(p, q):
        return not p and q
        if not p and q:
            return True
        else:
            return False

  still green. I remove the other statements

  .. code-block:: python

    def converse_non_implication(p, q):
        return not p and q

----

*********************************************************************************
test_material_non_implication
*********************************************************************************

red: make it fail
#################################################################################

I add another test

.. code-block:: python

    def test_converse_non_implication(self):
        ...

    def test_material_non_implication(self):
        self.assertFalse(src.truth_table.material_non_implication(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'material_non_implication'

green: make it pass
#################################################################################

I add a :ref:`function<functions>`

.. code-block:: python

  def converse_non_implication(p, q):
      return not p and q


  def material_non_implication(p, q):
      return not p and q

the test passes

refactor: make it better
#################################################################################

* I add another case

  .. code-block:: python

    def test_material_non_implication(self):
        self.assertFalse(src.truth_table.material_non_implication(True, True))
        self.assertTrue(src.truth_table.material_non_implication(True, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I add an `if statement`_ for it

  .. code-block:: python

    def material_non_implication(p, q):
        if p and not q:
            return True
        return not p and q

  the test passes

* I add the next case

  .. code-block:: python

    def test_material_non_implication(self):
        self.assertFalse(src.truth_table.material_non_implication(True, True))
        self.assertTrue(src.truth_table.material_non_implication(True, False))
        self.assertFalse(src.truth_table.material_non_implication(False, True))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I add another `if statement`_

  .. code-block:: python

    def material_non_implication(p, q):
        if not p and q:
            return False
        if p and not q:
            return True
        return not p and q

* I add the last case

  .. code-block:: python

    def test_material_non_implication(self):
        self.assertFalse(src.truth_table.material_non_implication(True, True))
        self.assertTrue(src.truth_table.material_non_implication(True, False))
        self.assertFalse(src.truth_table.material_non_implication(False, True))
        self.assertFalse(src.truth_table.material_non_implication(False, False))

  the terminal shows green

* I move the `if statement`_ for the case where the result is :ref:`True<test_what_is_true>` to the top of the :ref:`function<functions>` then add an else_ clause

  .. code-block:: python

    def material_non_implication(p, q):
        if p and not q:
            return True
        else:
            return False
        if not p and q:
            return False
        return not p and q

  still green. I use a `conditional expression`_

  .. code-block:: python

    def material_non_implication(p, q):
        return p and not q
        if p and not q:
            return True
        else:
            return False

  the test is still green. I remove the other statements

  .. code-block:: python

    def material_non_implication(p, q):
        return p and not q

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

  AttributeError: module 'src.truth_table' has no attribute 'logical_nor'. Did you mean: 'logical_true'?

green: make it pass
#################################################################################

I add a :ref:`function<functions>` definition to ``truth_table.py``

.. code-block:: python

  def material_non_implication(p, q):
      return p and not q


  def logical_nor(p, q):
      return p and not q

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
        return p and not q

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

  and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I add an `if statement`_

  .. code-block:: python

    def logical_nor(p, q):
        if not p and not q:
            return True
        if p and not q:
            return False
        return p and not q

  the terminal shows green again

* I add an else_ clause to the last `if statement`_

  .. code-block:: python

    def logical_nor(p, q):
        if not p and not q:
            return True
        else:
            return False
        if p and not q:
            return False
        return p and not q

  the terminal still shows green, I remove the other statements and rewrite the `if statement`_ to factor out not_ since it happens two times

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
test_logical_nand
*********************************************************************************

red: make it fail
#################################################################################

I add a test for Logical NAND

.. code-block:: python

  def test_logical_nor(self):
      ...

  def test_logical_nand(self):
      self.assertFalse(src.truth_table.logical_nand(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python
  :force:

  AttributeError: module 'src.truth_table' has no attribute 'logical_nand'. Did you mean: 'logical_nor'?

green: make it pass
#################################################################################

I add a definition for the :ref:`function<functions>`

.. code-block:: python

  def logical_nor(p, q):
      return not (p or q)


  def logical_nand(p, q):
      return not (p or q)

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
        if p and not q:
            return True
        return not (p or q)

  the test passes

* I add another case

  .. code-block:: python

    def test_logical_nand(self):
        self.assertFalse(src.truth_table.logical_nand(True, True))
        self.assertTrue(src.truth_table.logical_nand(True, False))
        self.assertTrue(src.truth_table.logical_nand(False, True))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I add another `if statement`_

  .. code-block:: python

    def logical_nand(p, q):
        if not p and q:
            return True
        if p and not q:
            return True
        return not (p or q)

  green again

* I add the last case

  .. code-block:: python

    def test_logical_nand(self):
        self.assertFalse(src.truth_table.logical_nand(True, True))
        self.assertTrue(src.truth_table.logical_nand(True, False))
        self.assertTrue(src.truth_table.logical_nand(False, True))
        self.assertTrue(src.truth_table.logical_nand(False, False))

  and the test passes

* I add an `if statement`_ for the one case that returns :ref:`False<test_what_is_false>` then add an else_ clause

  .. code-block:: python

    def logical_nand(p, q):
        if p and q:
            return False
        else:
            return True
        if not p and q:
            return True
        if p and not q:
            return True
        return not (p or q)

  the test is still green, I write the opposite of the `if statement`_ for the else_ clause

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
            return False

  I remove the other statements

  .. code-block:: python

    def logical_nand(p, q):
        return not (p and q)

----

*********************************************************************************
review
*********************************************************************************

*YOU DID IT!* You made it to the end of the ``Truth Table`` series. Summarizing what the tests have shown so far, I know that for any boolean operation involving 2 inputs: ``p`` and ``q`` which can take the values :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`

* :ref:`Contradiction <test_contradiction>` always returns :ref:`False<test_what_is_false>`
* :ref:`Tautology <test_tautology>` always returns :ref:`True<test_what_is_true>`
* :ref:`Negate Second <test_negate_second>` always returns ``not q``
* :ref:`Project Second <test_project_second>` always returns ``q``
* :ref:`Negate First<test_negate_first>` always returns ``not p``
* :ref:`Project First <test_project_first>` always returns ``p``
* :ref:`Exclusive Disjunction <test_exclusive_disjunction>` is ``!=`` or the opposite of :ref:`Logical Equality <test_logical_equality>`, I will call it ``Logical Inequality``
* :ref:`Logical Equality <test_logical_equality>` is ``==``
* :ref:`Converse NonImplication <test_converse_non_implication>` returns ``not p and q``
*  :ref:`Converse Implication <test_converse_implication>` returns ``p or not q``
* :ref:`Material NonImplication <test_material_non_implication>` returns ``p and not q``
* :ref:`Logical or Material Implication  <test_logical_implication>` returns ``not p or q``
* :ref:`Logical NOR <test_logical_nor>` returns ``not (p or q)``
* :ref:`Logical Disjunction <test_logical_disjunction>` is or_
* :ref:`Logical NAND <test_logical_nand>` returns ``not (p and q)``
* :ref:`Logical Conjunction <test_logical_conjunction>` is and_
* :ref:`Logical Negation<test_logical_negation>` is not_
* not_ or_ is and_
* not_ and_ is or_
* not_ :ref:`False<test_what_is_false>` is :ref:`True<test_what_is_true>`
* not_ :ref:`True<test_what_is_true>` is :ref:`False<test_what_is_false>`
* :ref:`False<test_what_is_false>` is :ref:`False<test_what_is_false>`
* :ref:`True<test_what_is_true>` is :ref:`True<test_what_is_true>`
* :ref:`True<test_what_is_true>` and :ref:`False<test_what_is_false>` are booleans_

Would you like to :doc:`test lists</data_structures/lists/lists>`?

----

:doc:`/code/code_truth_table`