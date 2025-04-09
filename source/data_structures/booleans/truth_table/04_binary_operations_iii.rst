.. include:: ../../../links.rst

.. _binary_operations_iii:

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

  def test_logical_disjunction(self):
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

  def logical_disjunction(p, q):
      return p or q


  def exclusive_disjunction(p, q):
      return p or q

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: True is not false

I add an `if statement`_

.. code-block:: python

    def exclusive_disjunction(p, q):
        if p and q:
            return False
        return p or q

the test passes

refactor: make it better
#################################################################################

* I add the next case

  .. code-block:: python

    def test_exclusive_disjunction(self):
        self.assertFalse(src.truth_table.exclusive_disjunction(True, True))
        self.assertTrue(src.truth_table.exclusive_disjunction(True, False))

  the terminal still shows green. I add an `if statement`_ to see it fail

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p and not q:
            return False
        if p and q:
            return False
        return p or q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I change the `return statement`_

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p and not q:
            return True
        if p and q:
            return False
        return p or q

  the test is green again

* I add the next case

  .. code-block:: python

    def test_exclusive_disjunction(self):
        self.assertFalse(src.truth_table.exclusive_disjunction(True, True))
        self.assertTrue(src.truth_table.exclusive_disjunction(True, False))
        self.assertTrue(src.truth_table.exclusive_disjunction(False, True))

  the test is still green. I add another `if statement`_

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if not p and q:
            return False
        if p and not q:
            return True
        if p and q:
            return False
        return p or q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I change the `return statement`_

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if not p and q:
            return True
        if p and not q:
            return True
        if p and q:
            return False
        return p or q

  the test is green

* I add the last case

  .. code-block:: python

    def test_exclusive_disjunction(self):
        self.assertFalse(src.truth_table.exclusive_disjunction(True, True))
        self.assertTrue(src.truth_table.exclusive_disjunction(True, False))
        self.assertTrue(src.truth_table.exclusive_disjunction(False, True))
        self.assertFalse(src.truth_table.exclusive_disjunction(False, False))

  and the terminal still shows green. I add an `if statement`_

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if not p and not q:
            return True
        if not p and q:
            return True
        if p and not q:
            return True
        if p and q:
            return False
        return p or q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I fix the line and remove ``return p or q``

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

  the test is green again

* There are 2 cases where the result is :ref:`False<test_what_is_false>` and 2 where the result is :ref:`True<test_what_is_true>`. I move the top `if statement`_ to the bottom to have the 2 that return :ref:`True<test_what_is_true>` together

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

  I use or_ to make one `if statement`_ that puts the 2 that return :ref:`True<test_what_is_true>` together

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

  still green. I remove the other statements and use a `ternary operator`_

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

* This :ref:`function<functions>` returns :ref:`True<test_what_is_true>` in the 2 cases when ``p`` and ``q`` are NOT the same, it could also be written as

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p != q:
            return True
        else:
            return False
        return (not p and q) or (p and not q)

  or

  .. code-block:: python

    def exclusive_disjunction(p, q):
        return not (p == q)
        return (not p and q) or (p and not q)

  or

  .. code-block:: python

    def exclusive_disjunction(p, q):
        return p != q
        return not (p == q)
        return (not p and q) or (p and not q)

----

*********************************************************************************
test_material_non_implication
*********************************************************************************

red: make it fail
#################################################################################

I add another test

.. code-block:: python

    def test_exclusive_disjunction(self):
        ...

    def test_material_non_implication(self):
        self.assertFalse(src.truth_table.material_non_implication(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python
  :force:

  AttributeError: module 'src.truth_table' has no attribute 'material_non_implication'. Did you mean: 'converse_non_implication'?

green: make it pass
#################################################################################

I add a :ref:`function<functions>`

.. code-block:: python

  def exclusive_disjunction(p, q):
      return p != q
      return (not p and q) or (p and not q)


  def material_non_implication(p, q):
      return p != q

the test passes

refactor: make it better
#################################################################################

* I add another case

  .. code-block:: python

    def test_material_non_implication(self):
        self.assertFalse(src.truth_table.material_non_implication(True, True))
        self.assertTrue(src.truth_table.material_non_implication(True, False))

  the test is still green, I add an `if statement`_

  .. code-block:: python

    def material_non_implication(p, q):
        if p and not q:
            return False
        return p != q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I fix the statement

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
        return p != q

  the test passes

* I add the last case

  .. code-block:: python

    def test_material_non_implication(self):
        self.assertFalse(src.truth_table.material_non_implication(True, True))
        self.assertTrue(src.truth_table.material_non_implication(True, False))
        self.assertFalse(src.truth_table.material_non_implication(False, True))
        self.assertFalse(src.truth_table.material_non_implication(False, False))

  the terminal shows green. I add an `if statement`_

  .. code-block:: python

    def material_non_implication(p, q):
        if not p and not q:
            return True
        if not p and q:
            return False
        if p and not q:
            return True
        return p != q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I change the line to fix it

  .. code-block:: python

    def material_non_implication(p, q):
        if not p and not q:
            return False
        if not p and q:
            return False
        if p and not q:
            return True
        return p != q

  the test is green again

* I move the `if statement`_ for the case where the result is :ref:`True<test_what_is_true>` to the top of the :ref:`function<functions>` then add an else_ clause

  .. code-block:: python

    def material_non_implication(p, q):
        if p and not q:
            return True
        else:
            return False
        if not p and not q:
            return False
        if not p and q:
            return False
        return p != q

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
test_project_first
*********************************************************************************

red: make it fail
#################################################################################

I add a new test

.. code-block:: python

  def test_material_non_implication(self):
      ...

  def test_project_first(self):
      self.assertTrue(src.truth_table.project_first(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'project_first'

green: make it pass
#################################################################################

I add the a :ref:`function<functions>` definition for it in ``truth_table.py``

.. code-block:: python

  def material_non_implication(p, q):
      return p and not q


  def project_first(p, q):
      return p and not q

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: False is not true

I add an `if statement`_

.. code-block:: python

  def project_first(p, q):
      if p and q:
          return True
      return p and not q

the test passes

refactor: make it better
#################################################################################

* I add the next case

  .. code-block:: python

    def test_project_first(self):
        self.assertTrue(src.truth_table.project_first(True, True))
        self.assertTrue(src.truth_table.project_first(True, False))

  the test is still green. I still add an `if statement`_

  .. code-block:: python

    def project_first(p, q):
        if p and not q:
            return False
        if p and q:
            return True
        return p and not q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I fix the statement

  .. code-block:: python

    def project_first(p, q):
        if p and not q:
            return True
        if p and q:
            return True
        return p and not q

  the test is green again. These 2 statements both return :ref:`True<test_what_is_true>` and ``p`` is the same in both cases. I rewrite the `if statements`_ with an else_ clause since most of the operations so far only have 2 results

  .. code-block:: python

    def project_first(p, q):
        if p:
            return True
        else:
            return False
        if p and not q:
            return True
        if p and q:
            return True
        return p and not q

  the test is still green and I remove the other statements

* on to the next case

  .. code-block:: python

    def test_project_first(self):
        self.assertTrue(src.truth_table.project_first(True, True))
        self.assertTrue(src.truth_table.project_first(True, False))
        self.assertFalse(src.truth_table.project_first(False, True))

  the terminal still shows green. I do not add another `if statement`_ since I have a `return statement`_ for each expected result

* I add the next case

  .. code-block:: python

    def test_project_first(self):
        self.assertTrue(src.truth_table.project_first(True, True))
        self.assertTrue(src.truth_table.project_first(True, False))
        self.assertFalse(src.truth_table.project_first(False, True))
        self.assertFalse(src.truth_table.project_first(False, False))

  still green

* I use a `conditional expression`_

  .. code-block:: python

    def project_first(p, q):
        return p
        if p:
            return True
        else:
            return False

  still green. I remove the other statements

  .. code-block:: python

    def project_first(p, q):
        return p

----

*********************************************************************************
test_converse_implication
*********************************************************************************

red: make it fail
#################################################################################

I add a new test

.. code-block:: python

  def test_project_first(self):
      ...

  def test_converse_implication(self):
      self.assertTrue(src.truth_table.converse_implication(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python
  :force:

  AttributeError: module 'src.truth_table' has no attribute 'converse_implication'. Did you mean: 'converse_non_implication'?

green: make it pass
#################################################################################

I add a :ref:`function<functions>` definition to ``truth_table.py``

.. code-block:: python

  def project_first(p, q):
      return p


  def converse_implication(p, q):
      return p

the test passes

refactor: make it better
#################################################################################

* I add the second case

  .. code-block:: python

    def test_converse_implication(self):
        self.assertTrue(src.truth_table.converse_implication(True, True))
        self.assertTrue(src.truth_table.converse_implication(True, False))

  the test is still green

* time for the next case

  .. code-block:: python

    def test_converse_implication(self):
        self.assertTrue(src.truth_table.converse_implication(True, True))
        self.assertTrue(src.truth_table.converse_implication(True, False))
        self.assertFalse(src.truth_table.converse_implication(False, True))

  the test is still green

* I add the last case

  .. code-block:: python

    def test_converse_implication(self):
        self.assertTrue(src.truth_table.converse_implication(True, True))
        self.assertTrue(src.truth_table.converse_implication(True, False))
        self.assertFalse(src.truth_table.converse_implication(False, True))
        self.assertTrue(src.truth_table.converse_implication(False, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I add an `if statement`_ for it

  .. code-block:: python

    def converse_implication(p, q):
        if not p and not q:
            return True
        return p

  the test passes

* I add an `if statement`_ for the one case that returns :ref:`False<test_what_is_false>` then add an else_ clause

  .. code-block:: python

    def converse_implication(p, q):
        if not p and q:
            return False
        else:
            return True
        if not p and not q:
            return True
        return p

  the terminal shows green and I remove the other statements, then write the opposite of the `if statement`_ to replace else_

  .. code-block:: python

    def converse_implication(p, q):
        if not p and q:
            return False
        if not (not p and q):
        # else:
            return True

  the terminal still shows green. I move the new `if statement`_ to the top of the :ref:`function<functions>` then add a new else_ clause

  .. code-block:: python

    def converse_implication(p, q):
        if not (not p and q):
            return True
        else:
        # if not p and q:
            return False

  still green. I "multiply" the not_ by each symbol in the parentheses

  .. code-block:: python

    def converse_implication(p, q):
        if not not p not and not q:
        # if not (not p and q):
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

    def converse_implication(p, q):
        if p or not q:
        # if not not p not and not q:
        # if not (not p and q):
            return True
        else:
            return False

  back to green. I use a `conditional expression`_

  .. code-block:: python

    def converse_implication(p, q):
        return p or not q
        if p or not q:
            return True
        else:
            return False

  all the tests are still green. I remove the other statements

  .. code-block:: python

    def converse_implication(p, q):
        return p or not q

----

*********************************************************************************
review
*********************************************************************************

From the tests I know that

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

do you want to :ref:`test more binary operations? <binary_operations_iv>`

----

:doc:`/code/code_truth_table`