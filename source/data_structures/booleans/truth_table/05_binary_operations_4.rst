.. include:: ../../../links.rst

.. _binary_operations_iv:

#################################################################################
truth table: Binary Operations part 4
#################################################################################

.. contents:: table of contents
  :local:
  :depth: 1

----

*********************************************************************************
requirements
*********************************************************************************

:ref:`Binary Operations part 3<truth table: Binary Operations part 3>`

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

    def negate_second(p, q):
        if not p and not q:
            return True
        if p and not q:
            return True
        return False

  the test is green again

* this :ref:`function<functions>` returns :ref:`True<test_what_is_true>` in the two cases where ``q`` is :ref:`False<test_what_is_false>`, I add a `return statement`_

  .. code-block:: python

    def negate_second(p, q):
        return not q
        if not p and not q:
            return True
        if p and not q:
            return True
        return False

  the test is still green. I remove the other statements

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

the terminal shows :ref:`AttributeError`

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

  this is the only case that returns :ref:`True<test_what_is_true>`, I add a `return statement`_ for it

  .. code-block:: python

    def logical_nor(p, q):
        return not p and not q
        return False

  the test passes

* I want to factor out not_ since it happens 2 times, I rewrite the statement in terms of not_

  .. code-block:: python

    def logical_nor(p, q):
        return not p not or not q
        return not p and not q

  the terminal shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  I comment out the line then add the correct statement

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

* I use or_ to put the 2 statements that return :ref:`False<test_what_is_false>` together

  .. code-block:: python

    def logical_equality(p, q):
        if (not p and q) or (p and not q):
            return False
        if not p and q:
            return False
        if p and not q:
            return False
        return True

  still green. I remove the other `if statements`_ then write a new `return statement`_

  .. code-block:: python

    def logical_equality(p, q):
        return not ((not p and q) or (p and not q)):
        if (not p and q) or (p and not q):
            return False
        return True

  the test is still green. I "multiply" not_ by every symbol in the parentheses

  .. code-block:: python

    def logical_equality(p, q):
        return (not not p not and not q) not or (not p not and not not q)
        return not ((not p and q) or (p and not q):)

  the terminal shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  I change not_ and_ to or_ in both parentheses and not_ or_ to and_ in between them

  .. code-block:: python

    def logical_equality(p, q):
        return (not not p or not q) and (not p or not not q)
        return not ((not p and q) or (p and not q))

  the test is green again. I remove not_ not_ from both parentheses

  .. code-block:: python

    def logical_equality(p, q):
        return (p or not q) and (not p or q)
        return not ((not p and q) or (p and not q))

  the terminal shows green. I remove the other line

  .. code-block:: python

    def logical_equality(p, q):
        return (p or not q) and (not p or q)

  all the tests are still passing.

* The 2 cases where :ref:`True<test_what_is_true>` is the result are cases where ``p`` and ``q`` are the same, which means I can write a simpler `return statement`_

  .. code-block:: python

    def logical_equality(p, q):
        return p == q
        return (p or not q) and (not p or q)

  the test is still green

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
      self.assertTrue(src.truth_table.material_implication(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python
  :force:

  AttributeError: module 'src.truth_table' has no attribute 'material_implication'

green: make it pass
#################################################################################

I add the :ref:`method<functions>`

.. code-block:: python

  def logical_equality(p, q):
      return p == q
      return (p or not q) and (not p or q)


  def material_implication(p, q):
      return True

the test passes

refactor: make it better
#################################################################################

* I add the next case

  .. code-block:: python

    def test_material_implication(self):
        self.assertTrue(src.truth_table.material_implication(True, True))
        self.assertFalse(src.truth_table.material_implication(True, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I add an `if statement`_

  .. code-block:: python

    def material_implication(p, q):
        if p and not q:
            return False
        return True

  the terminal shows green

* I add the next case

  .. code-block:: python

    def test_material_implication(self):
        self.assertTrue(src.truth_table.material_implication(True, True))
        self.assertFalse(src.truth_table.material_implication(True, False))
        self.assertTrue(src.truth_table.material_implication(False, True))

  the test is still green

* I add the fourth case

  .. code-block:: python

    def test_material_implication(self):
        self.assertTrue(src.truth_table.material_implication(True, True))
        self.assertFalse(src.truth_table.material_implication(True, False))
        self.assertTrue(src.truth_table.material_implication(False, True))
        self.assertTrue(src.truth_table.material_implication(False, False))

  the test is still passing

* there is only one case where this :ref:`function<functions>` returns :ref:`False<test_what_is_false>`, I add a `return statement`_ for it

  .. code-block:: python

    def material_implication(p, q):
        return not (p and not q)
        if p and not q:
            return False
        return True

  the test is still green, I "multiply" not_ by the symbols in the parentheses

  .. code-block:: python

    def material_implication(p, q):
        return not p not and not not q
        return not (p and not q)

  the terminal shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  I change not_ and_ to or_

  .. code-block:: python

    def material_implication(p, q):
        return not p or not not q
        return not (p and not q)

  the test is green again. I remove not_ not_

  .. code-block:: python

    def material_implication(p, q):
        return not p or q
        return not (p and not q)

  all tests are still passing. I remove the other statement

  .. code-block:: python

    def material_implication(p, q):
        return not p or q

----

*********************************************************************************
review
*********************************************************************************

Binary Operations take 2 inputs, each of the inputs can be :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`, if we name the first input ``p`` and the second one ``q``, the tests show that

* :ref:`Material Implication  <test_material_implication>` returns ``not p or q``
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

Would you like to :ref:`test the truth table tests?<test_truth_table_tests>`

----

:doc:`/code/code_truth_table`