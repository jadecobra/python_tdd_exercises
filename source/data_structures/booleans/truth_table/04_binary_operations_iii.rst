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

* There are two cases where the result is :ref:`False<test_what_is_false>` and two where the result is :ref:`True<test_what_is_true>`. I move the top `if statement`_ to the bottom to have the two that return :ref:`True<test_what_is_true>` together

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

  I use or_ to make one `if statement`_ that puts the two that return :ref:`True<test_what_is_true>` together

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

* This :ref:`function<functions>` returns :ref:`True<test_what_is_true>` in the two cases when ``p`` and ``q`` are NOT the same, it could also be written as

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
test_project_first
*********************************************************************************

red: make it fail
#################################################################################

I add a new TestCase_ to ``test_truth_table.py``

.. code-block:: python

  class TestBinaryOperations(unittest.TestCase):

      def test_project_first(self):
          self.assertTrue(src.truth_table.project_first(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'project_first'

green: make it pass
#################################################################################

I add the a :ref:`function<functions>` definition for it in ``truth_table.py``

.. code-block:: python

  def logical_negation(argument):
      return not argument


  def project_first(argument):
      return not argument

the terminal shows :ref:`TypeError`

.. code-block:: python

  TypeError: project_first() takes 1 positional argument but 2 were given

I change the signature to make it accept two inputs

.. code-block:: python

  def project_first(p, q):
      return not p

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: False is not true

I change the `return statement`_

.. code-block:: python

refactor: make it better
#################################################################################

* I add the next case

  .. code-block:: python

    def test_project_first(self):
        self.assertTrue(src.truth_table.project_first(True, True))
        self.assertTrue(src.truth_table.project_first(True, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I add an `if statement`_

  .. code-block:: python

    def project_first(p, q):
        if p and not q:
            return True
        return p == q

  the test passes

* on to the next case

  .. code-block:: python

    def test_project_first(self):
        self.assertTrue(src.truth_table.project_first(True, True))
        self.assertTrue(src.truth_table.project_first(True, False))
        self.assertFalse(src.truth_table.project_first(False, True))

  the terminal still shows green. I add an `if statement`_ to be sure

  .. code-block:: python

    def project_first(p, q):
        if not p and q:
            return True
        if p and not q:
            return True
        return p == q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I fix the `return statement`_

  .. code-block:: python

    def project_first(p, q):
        if not p and q:
            return False
        if p and not q:
            return True
        return p == q

  the test passes

* I add the next case

  .. code-block:: python

    def test_project_first(self):
        self.assertTrue(src.truth_table.project_first(True, True))
        self.assertTrue(src.truth_table.project_first(True, False))
        self.assertFalse(src.truth_table.project_first(False, True))
        self.assertFalse(src.truth_table.project_first(False, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I add an `if statement`_

  .. code-block:: python

    def project_first(p, q):
        if not p and not q:
            return False
        if not p and q:
            return False
        if p and not q:
            return True
        return p == q

  the test passes

* I add an `if statement`_ for the first case

  .. code-block:: python

    def project_first(p, q):
        if not p and not q:
            return False
        if not p and q:
            return False
        if p and not q:
            return True
        if p and q:
            return False
        return p == q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I fix the line

  .. code-block:: python

    def project_first(p, q):
        if not p and not q:
            return False
        if not p and q:
            return False
        if p and not q:
            return True
        if p and q:
            return True

  the test passes

* this :ref:`function<functions>` returns :ref:`True<test_what_is_true>` when ``p`` is :ref:`True<test_what_is_true>` and returns :ref:`False<test_what_is_false>` when it is not. I add a simpler `if statement`

  .. code-block:: python

    def project_first(p, q):
        if p:
            return True
        else:
            return False
        if not p and not q:
            return False
        if not p and q:
            return False
        if p and not q:
            return True
        if p and q:
            return True

  the test is still green, I remove the other lines and use a `conditional expression`_

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

  the test is still green. I add an `if statement`_ that should cause a failure

  .. code-block:: python

    def logical_nor(p, q):
        if not p and q:
            return True
        if p and not q:
            return False
        return p and not q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the `return statement`_

  .. code-block:: python

    def logical_nor(p, q):
        if not p and q:
            return False
        if p and not q:
            return False
        return p and not q

  and the test is green again

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

  I add another `if statement`_

  .. code-block:: python

    def logical_nor(p, q):
        if not p and not q:
            return True
        if not p and q:
            return False
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
        if not p and q:
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
test_logical_implication
*********************************************************************************

red: make it fail
#################################################################################

I add a new test

.. code-block:: python

  def test_logical_disjunction(self):
      ...

  def test_logical_implication(self):
      self.assertTrue(src.truth_table.logical_implication(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python
  :force:

  AttributeError: module 'src.truth_table' has no attribute 'logical_implication'. Did you mean: 'logical_disjunction'?

green: make it pass
#################################################################################

I add the :ref:`method<functions>`

.. code-block:: python

  def logical_disjunction(p, q):
      return p or q


  def logical_implication(p, q):
      return p or q

the test passes

refactor: make it better
#################################################################################

* I add the next case

  .. code-block:: python

    def test_logical_implication(self):
        self.assertTrue(src.truth_table.logical_implication(True, True))
        self.assertFalse(src.truth_table.logical_implication(True, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I add an `if statement`_

  .. code-block:: python

    def logical_implication(p, q):
        if p == True and q == False:
            return False
        return p or q

  the terminal shows green again

* I add the next case

  .. code-block:: python

    def test_logical_implication(self):
        self.assertTrue(src.truth_table.logical_implication(True, True))
        self.assertFalse(src.truth_table.logical_implication(True, False))
        self.assertTrue(src.truth_table.logical_implication(False, True))

  the terminal shows green, I add an `if statement`_ to make sure it is right

  .. code-block:: python

    def logical_implication(p, q):
        if p == False and q == True:
            return False
        if p == True and q == False:
            return False
        return p or q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  when I change :ref:`False<test_what_is_false>` to :ref:`True<test_what_is_true>` in the `return statement`_

  .. code-block:: python

    def logical_implication(p, q):
        if p == False and q == True:
            return True
        if p == True and q == False:
            return False
        return p or q

  the test is green again

* I add the last case

  .. code-block:: python

    def test_logical_implication(self):
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
        if p == False and q == False:
            return False
        if p == False and q == True:
            return True
        if p == True and q == False:
            return False
        return p or q

  the test passes

* I add a condition for the first case to make it clearer

  .. code-block:: python

    def logical_implication(p, q):
        if p == False and q == False:
            return False
        if p == False and q == True:
            return True
        if p == True and q == False:
            return False
        if p == True and q == True:
            return False
        return p or q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I change the `return statement`_

  .. code-block:: python

    def logical_implication(p, q):
        if p == False and q == False:
            return False
        if p == False and q == True:
            return True
        if p == True and q == False:
            return False
        if p == True and q == True:
            return True
        return p or q

  the test passes and I remove ``return p or q``, then use the one case where the outcome is :ref:`False <test_what_is_false>` with an else_ clause

  .. code-block:: python

    def logical_implication(p, q):
        if p == True and q == False:
            return False
        else:
            return True
        if p == False and q == False:
            return False
        if p == False and q == True:
            return True
        if p == True and q == False:
            return False
        if p == True and q == True:
            return True

  the terminal still shows green. I remove the other `if statements`_

  .. code-block:: python

    def logical_implication(p, q):
        if p == True and q == False:
            return False
        else:
            return True

  I rewrite the else_ block as the opposite of the `if statement`_

  .. code-block:: python

    def logical_implication(p, q):
        if p == True and q == False:
            return False
        if not (p == True and q == False):
        # else:
            return True

  the terminal shows green. I remove the commented line and move the `if statement`_ that returns :ref:`True <test_what_is_true>` to the top then change the second statement to an else_ clause

  .. code-block:: python

    def logical_implication(p, q):
        if not (p == True and q == False):
            return True
        else:
        # if p == True and q == False:
            return False

  still green, I remove the commented line and multiply not_ by each symbol in the parentheses

  .. code-block:: python

    def logical_implication(p, q):
        if not p not == not True not and not q not == not False:
        # if not (p == True and q == False):
            return True
        else:
            return False

  the terminal shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  - not_ ``==`` is ``!=``
  - not_ :ref:`True<test_what_is_true>` is :ref:`False<test_what_is_false>`
  - not_ :ref:`False<test_what_is_false>` is :ref:`True<test_what_is_true>`
  - not_ and_ is or_

  .. code-block:: python

    def logical_implication(p, q):
        if not p != False or not q != True:
        # if not (p == True and q == False):
            return True
        else:
            return False

  the test is still green. I remove the commented line, then rewrite the statement to remove ``!=``

  .. code-block:: python

    def logical_implication(p, q):
        if not p == True or not q == False:
        # if not p != False or not q != True:
            return True
        else:
            return False

  still green. ``not x == False`` is the same as ``x == True``, I rewrite the statement

  .. code-block:: python

    def logical_implication(p, q):
        if not bool(p) or q == True:
        # if not p == True or not q == False:
            return True
        else:
            return False

  the test is still green, I rewrite the statement again

  .. code-block:: python

    def logical_implication(p, q):
        if not p or bool(q):
        # if not bool(p) or q == True:
            return True
        else:
            return False

  still green

  .. code-block:: python

    def logical_implication(p, q):
        if not p or q:
        # if not p or bool(q):
            return True
        else:
            return False

  the terminal still shows green, I remove the commented and rewrite the statement as a `conditional expression`_

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

* I change the name of the test

  .. code-block:: python

    def test_logical_or_material_implication(self):
        self.assertTrue(src.truth_table.logical_implication(True, True))
        self.assertFalse(src.truth_table.logical_implication(True, False))
        self.assertTrue(src.truth_table.logical_implication(False, True))
        self.assertTrue(src.truth_table.logical_implication(False, False))

----

*********************************************************************************
test_converse_implication
*********************************************************************************

red: make it fail
#################################################################################

I add a new test

.. code-block:: python

  def test_logical_or_material_implication(self):
      ...

  def test_converse_implication(self):
      self.assertTrue(src.truth_table.converse_implication(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python
  :force:

  AttributeError: module 'src.truth_table' has no attribute 'converse_implication'. Did you mean: 'logical_implication'?

green: make it pass
#################################################################################

I add a :ref:`function<functions>` definition to ``truth_table.py``

.. code-block:: python

  def logical_implication(p, q):
      return not p or q


  def converse_implication(p, q):
      return not p or q

the test passes

refactor: make it better
#################################################################################

* I add the second case

  .. code-block:: python

    def test_converse_implication(self):
        self.assertTrue(src.truth_table.converse_implication(True, True))
        self.assertTrue(src.truth_table.converse_implication(True, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I add an `if statement`_

  .. code-block:: python

    def converse_implication(p, q):
        if p == True and q == False:
            return True
        return not p or q

  the test passes

* time for the next case

  .. code-block:: python

    def test_converse_implication(self):
        self.assertTrue(src.truth_table.converse_implication(True, True))
        self.assertTrue(src.truth_table.converse_implication(True, False))
        self.assertFalse(src.truth_table.converse_implication(False, True))

  I get :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I add another `if statement`_

  .. code-block:: python

    def converse_implication(p, q):
        if p == False and q == True:
            return False
        if p == True and q == False:
            return True
        return not p or q

  the test passes

* I add the last case

  .. code-block:: python

    def test_converse_implication(self):
        self.assertTrue(src.truth_table.converse_implication(True, True))
        self.assertTrue(src.truth_table.converse_implication(True, False))
        self.assertFalse(src.truth_table.converse_implication(False, True))
        self.assertTrue(src.truth_table.converse_implication(False, False))

  and the test is still green. I add an `if statement`_ for it

  .. code-block:: python

    def converse_implication(p, q):
        if p == False and q == False:
            return False
        if p == False and q == True:
            return False
        if p == True and q == False:
            return True
        return not p or q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  the test passes and I add an `if statement`_ for the first case

  .. code-block:: python

    def converse_implication(p, q):
        if p == False and q == False:
            return True
        if p == False and q == True:
            return False
        if p == True and q == False:
            return True
        if p == True and q == True:
            return False
        return not p or q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I change the `return statement`_

  .. code-block:: python

    def converse_implication(p, q):
        if p == False and q == False:
            return True
        if p == False and q == True:
            return False
        if p == True and q == False:
            return True
        if p == True and q == True:
            return True
        return not p or q

  the test passes and I remove ``return not p or q``

* I use the `if statement`_ that returns :ref:`False<test_what_is_false>` then add an else_ clause

  .. code-block:: python

    def converse_implication(p, q):
        if p == False and q == True:
            return False
        else:
            return True
        if p == False and q == False:
            return True
        if p == False and q == True:
            return False
        if p == True and q == False:
            return True
        if p == True and q == True:
            return True
        return not p or q

  the terminal shows green and I remove the other statements, then write the opposite of the `if statement`_ to replace else_

  .. code-block:: python

    def converse_implication(p, q):
        if p == False and q == True:
            return False
        if not (p == False and q == True):
        # else:
            return True

  the terminal still shows green. I move the new `if statement`_ to the top of the :ref:`function<functions>` then add a new else_ clause

  .. code-block:: python

    def converse_implication(p, q):
        if not (p == False and q == True):
            return True
        else:
        # if p == False and q == True:
            return False

  still green. I "multiply" the not_ by each symbol in the parentheses

  .. code-block:: python

    def converse_implication(p, q):
        if not p not == not False not and not q not == not True:
        # if not (p == False and q == True):
            return True
        else:
            return False


  the terminal shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  - ``not ==`` is ``!=``
  - not_ and_ is or_
  - not_ :ref:`False<test_what_is_false>` is :ref:`True<test_what_is_true>`

  I fix the line

  .. code-block:: python

    def converse_implication(p, q):
        if not p != True or not q != False:
        # if not (p == False and q == True):
            return True
        else:
            return False

  the test is green again. I rewrite the `if statement`_

  .. code-block:: python

    def converse_implication(p, q):
        if not p == False or not q == True:
        # if not p != True or not q != False:
            return True
        else:
            return False

  the terminal still shows green. ``not x == False`` is the same as ``x == True`` and ``not x == True`` is the same as ``x != True``

  .. code-block:: python

    def converse_implication(p, q):
        if p == True or q != True:
        # if not p == False or not q == True:
            return True
        else:
            return False

  still green. I rewrite the statement with bool_

  .. code-block:: python

    def converse_implication(p, q):
        if bool(p) or not bool(q):
        # if p == True or q != True:
            return True
        else:
            return False

  the terminal shows green. I rewrite the statement again

  .. code-block:: python

    def converse_implication(p, q):
        if p or not q:
        # if bool(p) or not bool(q):
            return True
        else:
            return False

  still green. I rewrite it as a `conditional expression`_

  .. code-block:: python

    def converse_implication(p, q):
        return True if p or not q else False
        if p or not q:
            return True
        else:
            return False

  still green. I use the simpler `return statement`_

  .. code-block:: python

    def converse_implication(p, q):
        return p or not q
        return True if p or not q else False

  all the tests are still green. I remove the other statements

  .. code-block:: python

    def converse_implication(p, q):
        return p or not q

----

*********************************************************************************
review
*********************************************************************************

*YOU DID IT!* You made it to the end of the :ref:`Truth Table <truth_table>` series. The tests show that for any Binary Operation involving 2 inputs: ``p`` and ``q`` which can take the values :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`

* :ref:`Contradiction <test_contradiction>` always returns :ref:`False<test_what_is_false>`
* :ref:`Tautology <test_tautology>` always returns :ref:`True<test_what_is_true>`
* :ref:`Negate Second <test_negate_second>` always returns ``not q``
* :ref:`Project Second <test_project_second>` always returns ``q``
* :ref:`Negate First<test_negate_first>` always returns ``not p``
* :ref:`Project First <test_project_first>` always returns ``p``
* :ref:`Exclusive Disjunction <test_exclusive_disjunction>` is ``!=``, or the :ref:`Logical Negation<test_logical_negation>` of :ref:`Logical Equality <test_logical_equality>`
* :ref:`Logical Equality <test_logical_equality>` is ``==``
* :ref:`Converse NonImplication <test_converse_non_implication>` returns ``not p and q``
*  :ref:`Converse Implication <test_converse_implication>` returns ``p or not q``
* :ref:`Material NonImplication <test_material_non_implication>` returns ``p and not q``
* :ref:`Logical or Material Implication  <test_logical_implication>` returns ``not p or q``
* :ref:`Logical NOR <test_logical_nor>` returns ``not (p or q)``
* :ref:`Logical Disjunction <test_logical_disjunction>` returns ``p or q``
* :ref:`Logical NAND <test_logical_nand>` returns ``not (p and q)``
* :ref:`Logical Conjunction <test_logical_conjunction>` returns ``p and q``
* :ref:`Logical Negation<test_logical_negation>` is not_
* not_ or_ is and_
* not_ and_ is or_
* not_ :ref:`False<test_what_is_false>` is :ref:`True<test_what_is_true>`
* not_ :ref:`True<test_what_is_true>` is :ref:`False<test_what_is_false>`
* :ref:`False<test_what_is_false>` is :ref:`False<test_what_is_false>`
* :ref:`True<test_what_is_true>` is :ref:`True<test_what_is_true>`
* :ref:`True<test_what_is_true>` and :ref:`False<test_what_is_false>` are booleans_

do you want to :ref:`test more binary operations? <binary_operations_iv>`

----

:doc:`/code/code_truth_table`