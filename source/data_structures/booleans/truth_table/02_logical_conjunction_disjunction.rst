.. include:: ../../../links.rst

#################################################################################
truth table: Logical Conjunction and Logical Disjunction
#################################################################################

.. contents:: table of contents
  :local:
  :depth: 1

----

*********************************************************************************
requirements
*********************************************************************************

:doc:`how to make a python test driven development environment </how_to/make_tdd_environment>` with ``truth_table`` as the name of the project

There are 16 binary operations, they take two inputs that could be either :ref:`True <test_what_is_true>` or :ref:`False <test_what_is_false>`

*********************************************************************************
test_logical_conjunction
*********************************************************************************

red: make it fail
#################################################################################

I add a new TestCase_ to ``test_truth_table.py``

.. code-block:: python

  class TestUnaryOperations(unittest.TestCase):
      ...


  class TestBinaryOperations(unittest.TestCase):

      def test_logical_conjunction(self):
          self.assertTrue(src.truth_table.logical_conjunction(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'logical_conjunction'. Did you mean: 'logical_negation'?


green: make it pass
#################################################################################

I add the :ref:`function<functions>`

.. code-block:: python

  def logical_negation(argument):
      return not argument


  def logical_conjunction(argument):
      return not argument

and the terminal shows :ref:`TypeError`

.. code-block:: python

  TypeError: logical_conjunction() takes 1 positional argument but 2 were given

I change the signature

.. code-block:: python

  def logical_conjunction(p, q):
      return not p

and the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: False is not true

I change ``not p`` to :ref:`True <test_what_is_true>` in the `return statement`_

.. code-block:: python

  def logical_conjunction(p, q):
      return True

and the test passes

refactor: make it better
#################################################################################

* I add the next case

  .. code-block:: python

    def test_logical_conjunction(self):
        self.assertTrue(src.truth_table.logical_conjunction(True, True))
        self.assertFalse(src.truth_table.logical_conjunction(True, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  when I add a `return statement`_ for :ref:`False <test_what_is_true>`

  .. code-block:: python

    def logical_conjunction(p, q):
        return False
        return True

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  for the line that was passing before. ``logical_conjunction`` has to make a decision about what it will return based on its inputs. I can make it do that with `if statements`_

  .. code-block:: python

    def logical_conjunction(p, q):
        if p == True:
            if q == False:
                return False
        return True

  the test passes

* I add the next case

  .. code-block:: python

    def test_logical_conjunction(self):
        self.assertTrue(src.truth_table.logical_conjunction(True, True))
        self.assertFalse(src.truth_table.logical_conjunction(True, False))
        self.assertFalse(src.truth_table.logical_conjunction(False, True))

  and get :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I add more `if statements`_

  .. code-block:: python

    def logical_conjunction(p, q):
        if p == False:
            if q == True:
                return False
        if p == True:
            if q == False:
                return False
        return True

  the test passes

* I add the last case

  .. code-block:: python

    def test_logical_conjunction(self):
        self.assertTrue(src.truth_table.logical_conjunction(True, True))
        self.assertFalse(src.truth_table.logical_conjunction(True, False))
        self.assertFalse(src.truth_table.logical_conjunction(False, True))
        self.assertFalse(src.truth_table.logical_conjunction(False, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I add an `if statement`_ for it

  .. code-block:: python

    def logical_conjunction(p, q):
        if p == False:
            if q == False:
                return False
            if q == True:
                return False
        if p == True:
            if q == False:
                return False
        return True

  the terminal shows green

* I add an `if statement` for the first case to make it clearer

  .. code-block:: python

    def logical_conjunction(p, q):
        if p == False:
            if q == False:
                return False
            if q == True:
                return False
        if p == True:
            if q == False:
                return False
            if q == True:
                return False
        return True

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I change :ref:`False <test_what_is_false>` in the new line and and comment out the last `return statement`_

  .. code-block:: python

    def logical_conjunction(p, q):
        if p == False:
            if q == False:
                return False
            if q == True:
                return False
        if p == True:
            if q == False:
                return False
            if q == True:
                return True
        # return True

  the terminal shows green again. There are only two results for this operation, in the first case the :ref:`function<functions>` returns `True <test_what_is_true>` and in the other 3 cases it returns `False <test_what_is_false>`

* I remove the commented line and rewrite the `if statement`_ for the case where the result is `True <test_what_is_true>` and use an else_ clause for the other cases

  .. code-block:: python

    def logical_conjunction(p, q):
        if p == True and q == True:
            return True
        else:
            return False
        if p == False:
            if q == False:
                return False
            if q == True:
                return False
        if p == True:
            if q == False:
                return False
            if q == True:
                return True

  the test is still green. I remove the other `if statements`_ and rewrite the first statement with bool_

  .. code-block:: python

    def logical_conjunction(p, q):
        if bool(p) == True and bool(q) == True:
        # if p == True and q == True:
            return True
        else:
            return False

  ``bool(x)`` checks if ``x`` is :ref:`True <test_what_is_true>` and the ``== True`` checks if the result of ``bool(x)`` is :ref:`True <test_what_is_true>`, making it a repetition. I remove the commented line and rewrite the first line to remove the duplication

  .. code-block:: python

    def logical_conjunction(p, q):
        if bool(p) and bool(q):
        # if bool(p) == True and bool(q) == True:
            return True
        else:
            return False

  the terminal shows green and I remove the commented line. Python has implicit truth value testing which allows me to rewrite the first line as

  .. code-block:: python

    def logical_conjunction(p, q):
        if p and q:
        # if bool(p) and bool(q):
            return True
        else:
            return False

  the test is still green, I remove the commented line. Python has `conditional expressions`_(`ternary operators`_) which allows me to write the `if statements`_ in a simpler way

  .. code-block:: python

    def logical_conjunction(p, q):
        return True if p and q else False
        if p and q:
            return True
        else:
            return False

  the terminal shows green, I remove the other if statements and rewrite the `return statement`_

  .. code-block:: python

    def logical_conjunction(p, q):
        return p and q
        return True if p and q else False

  still green, I remove the second `return statement`_

  .. code-block:: python

    def logical_conjunction(p, q):
        return p and q

  then I rename the test

  .. code-block:: python

    def test_logical_conjunction_aka_and(self):
        self.assertTrue(src.truth_table.logical_conjunction(True, True))
        self.assertFalse(src.truth_table.logical_conjunction(True, False))
        self.assertFalse(src.truth_table.logical_conjunction(False, True))
        self.assertFalse(src.truth_table.logical_conjunction(False, False))

----

*********************************************************************************
test_logical_disjunction
*********************************************************************************

red: make it fail
#################################################################################

I add a another test to the ``TestBinaryOperations`` TestCase_

.. code-block:: python

  def test_logical_disjunction(self):
      self.assertTrue(src.truth_table.logical_disjunction(True, True))

and the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'logical_disjunction'. Did you mean: 'logical_conjunction'?

green: make it pass
#################################################################################

I add the :ref:`function<functions>`

.. code-block:: python

  def logical_disjunction(p, q):
      return p and q

and the test passes

refactor: make it better
#################################################################################

* I add the next case

  .. code-block:: python

    def test_logical_disjunction(self):
        self.assertTrue(src.truth_table.logical_disjunction(True, True))
        self.assertTrue(src.truth_table.logical_disjunction(True, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I add an `if statement`_

  .. code-block:: python

    def logical_disjunction(p, q):
        if p == True:
            if q == False:
                return True
        return p and q

  the test passes

* I add the next case

  .. code-block:: python

    def test_logical_disjunction(self):
        self.assertTrue(src.truth_table.logical_disjunction(True, True))
        self.assertTrue(src.truth_table.logical_disjunction(True, False))
        self.assertTrue(src.truth_table.logical_disjunction(False, True))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I add an `if statement`_ for it

  .. code-block:: python

    def logical_disjunction(p, q):
        if p == False:
            if q == True:
                return True
        if p == True:
            if q == False:
                return True
        return p and q

  the test passes

* I add the last case

  .. code-block:: python

    def test_logical_disjunction(self):
        self.assertTrue(src.truth_table.logical_disjunction(True, True))
        self.assertTrue(src.truth_table.logical_disjunction(True, False))
        self.assertTrue(src.truth_table.logical_disjunction(False, True))
        self.assertFalse(src.truth_table.logical_disjunction(False, False))

  the terminal shows green, so I add an `if statement`_ to make sure it is right

  .. code-block:: python

    def logical_disjunction(p, q):
        if p == False:
            if q == False:
                return True
            if q == True:
                return True
        if p == True:
            if q == False:
                return True
        return p and q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the `return statement`_ and add an `if statement`_ for the first case

  .. code-block:: python

    def logical_disjunction(p, q):
        if p == False:
            if q == False:
                return False
            if q == True:
                return True
        if p == True:
            if q == False:
                return True
            if q == True:
                return False
        return p and q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I change the `return statement`_ and comment out the last line in the :ref:`function<functions>`

  .. code-block:: python

    def logical_disjunction(p, q):
        if p == False:
            if q == False:
                return False
            if q == True:
                return True
        if p == True:
            if q == False:
                return True
            if q == True:
                return True
        # return p and q

  the terminal shows green again so I remove the commented line

* This :ref:`function<functions>` only has two results :ref:`True<test_what_is_true>` in one case and :ref:`False<test_what_is_false>` in the other 3 cases, it was the same with ``logical_conjunction``. I add a new `if statement`_ for the condition that returns :ref:`False<test_what_is_false>`

  .. code-block:: python

    def logical_disjunction(p, q):
        if p == False and q == False:
            return False
        else:
            return True
        if p == False:
            if q == False:
                return False
            if q == True:
                return True
        if p == True:
            if q == False:
                return True
            if q == True:
                return True

  the terminal still shows green. I remove the other `if statements`_, then rewrite the first line in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python

    def logical_disjunction(p, q):
        if p != True and q != True:
        # if p == False and q == False:
            return False
        else:
            return True

  the test is still green. I remove the commented line and rewrite the first line with bool_

  .. code-block:: python

    def logical_disjunction(p, q):
        if bool(p) != True and bool(q) != True:
        # if p != True and q != True:
            return False
        else:
            return True

  still green. I remove the commented line and use ``logical_negation(not)``

  .. code-block:: python

    def logical_disjunction(p, q):
        if not bool(p) == True and not bool(q) == True:
        # if bool(p) != True and bool(q) != True:
            return False
        else:
            return True

  the test is still green. I remove the commented line and rewrite the statement without the repeated test

  .. code-block:: python

    def logical_disjunction(p, q):
        if not bool(p) and not bool(q):
        # if not bool(p) == True and not bool(q) == True:
            return False
        else:
            return True

  still green. I remove the commented line and bool_ to use implicit truth value testing

  .. code-block:: python

    def logical_disjunction(p, q):
        if not p and not q:
        # if not bool(p) and not bool(q):
            return False
        else:
            return True

  the terminal shows green

* not_ appears twice in the `if statement`_ I will try to factor it out like in algebra to remove the repetition

  .. code-block:: python

    def logical_disjunction(p, q):
        if not (p and q):
        # if not p and not q:
            return False
        else:
            return True

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I did not do that correctly. I expand the statement using "multiplication" rules to check my work

  .. code-block:: python

    if not (p and q):
    if not p not and not q
    # if not p and not q:

  ``not and`` is ``or``

  .. code-block:: python

    if not (p and q):
      if not p or not q
    # if not p and not q:

  the result of the "multiplication" is different from what I started with so I need something different. I undo the changes to get green again

  .. code-block:: python

    def logical_disjunction(p, q):
        if not p and not q:
            return False
        else:
            return True

  then I try one more time

  .. code-block:: python

    def logical_disjunction(p, q):
        if not (p or q):
        # if not p and not q:
            return False
        else:
            return True

  the test is green again. The new statement "multiplies" out to

  .. code-block:: python

    if not (p or q):
    if not p not or not q
    # if not p and not q:

  ``not or`` is ``and``

  .. code-block:: python

    if not (p or q):
      if not p and not q
    # if not p and not q:

  the statements are the same. I remove the extra lines then rewrite the else_ clause as the opposite of the `if statement`_

  .. code-block:: python

    def logical_disjunction(p, q):
        if not (p or q):
            return False
        if not (not (p or q)):
        # else:
            return True

  the test is green again. I move the first two statements to the bottom, then add an else_ clause

  .. code-block:: python

    def logical_disjunction(p, q):
        if not (not (p or q)):
            return True
        else:
        # if not (p or q):
            return False

  still green. I "multiply" out the first `if statement`_ because not_ appears twice in it

  .. code-block:: python

    def logical_disjunction(p, q):
        if p or q:
        # if not (not (p or q)):
            return True
        else:
            return False

  since the opposite of the opposite of a thing is the thing, the two nots_ cancel each other. I rewrite the statements as a `conditional expressions`_(`ternary operators`_)

  .. code-block:: python

    def logical_disjunction(p, q):
        return True if p or q else False
        if p or q:
            return True
        else:
            return False

  the test is still green. I use a simpler `return statement`_

  .. code-block:: python

    def logical_disjunction(p, q):
        return p or q
        return True if p or q else False

  still green. I remove the second `return statement`_

  .. code-block:: python

    def logical_disjunction(p, q):
        return p or q

  then rename the test

  .. code-block:: python

    def test_logical_disjunction_aka_or(self):
        self.assertTrue(src.truth_table.logical_disjunction(True, True))
        self.assertTrue(src.truth_table.logical_disjunction(True, False))
        self.assertTrue(src.truth_table.logical_disjunction(False, True))
        self.assertFalse(src.truth_table.logical_disjunction(False, False))

----

*********************************************************************************
review
*********************************************************************************

I ran tests for

* ``logical conjunction`` which is and_
* ``logical_disjunction``` which is or_
* ``logical negation`` which is not_

:ref:`Logical Implication and Logical Equality<truth table: Logical Implication and Logical Equality>` are next

----

:doc:`/code/code_truth_table`