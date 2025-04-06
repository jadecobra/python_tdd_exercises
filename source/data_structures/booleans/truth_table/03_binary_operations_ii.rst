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
test_project_first
*********************************************************************************

red: make it fail
#################################################################################

I add a new test

.. code-block:: python

  def test_logical_equality(self):
      ...

  def test_project_first(self):
      self.assertTrue(src.truth_table.project_first(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'project_first'

green: make it pass
#################################################################################

I add the :ref:`function<functions>`

.. code-block:: python

  def logical_equality(p, q):
      return p == q
      return (p and q) or not (p or q)


  def project_first(p, q):
      return p == q

the test passes

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

I ran tests for

* :ref:`Logical Negation <test_logical_negation>` which is not_
* :ref:`Logical Conjunction <test_logical_conjunction>` which is and_ as well as :ref:`Logical NAND <test_logical_nand>`
* :ref:`Logical Disjunction <test_logical_disjunction>` which is or_ as well as :ref:`Logical NOR <test_logical_nor>`
* :ref:`Logical Implication aka Material Implication<test_logical_implication>` and :ref:`Material NonImplication <test_material_non_implication>`
* :ref:`Converse NonImplication <test_converse_non_implication>` and :ref:`Converse Implication <test_converse_implication>`
* :ref:`Logical Equality <test_logical_equality>` and :ref:`Exclusive Disjunction <test_exclusive_disjunction>`

do you want more :ref:`more binary operations? <truth table: Binary Operations III>`

----

:doc:`/code/code_truth_table`