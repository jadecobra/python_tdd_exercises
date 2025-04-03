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
test_exclusive_disjunction
*********************************************************************************

red: make it fail
#################################################################################

I add a new test

.. code-block:: python

  def test_exclusive_disjunction(self):
      self.assertFalse(src.truth_table.exclusive_disjunction(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'exclusive_disjunction'

green: make it pass
#################################################################################

I add the :ref:`function<functions>`

.. code-block:: python

  def exclusive_disjunction(p, q):
      return (p or not q) and (not p or q)

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: True is not false

I change the `return statement`

.. code-block:: python

  def exclusive_disjunction(p, q):
      return False

and the test passes

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
        if p == True and q == False:
            return True
        return False

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
        if p == False and q == True:
            return True
        if p == True and q == False:
            return True
        return False

* I add the last case

  .. code-block:: python

    def test_exclusive_disjunction(self):
        self.assertFalse(src.truth_table.exclusive_disjunction(True, True))
        self.assertTrue(src.truth_table.exclusive_disjunction(True, False))
        self.assertTrue(src.truth_table.exclusive_disjunction(False, True))
        self.assertFalse(src.truth_table.exclusive_disjunction(False, False))

  and the terminal shows green

* I add an `if statement`_ for the last case

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p == False and q == False:
            return False
        if p == False and q == True:
            return True
        if p == True and q == False:
            return True
        return False

  then add another one for the first case

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p == True and q == True:
            return False
        if p == False and q == False:
            return False
        if p == False and q == True:
            return True
        if p == True and q == False:
            return True
        # return False

  the terminal still shows green

* I rewrite the statements in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p and q:
        # if p == True and q == True:
            return False
        if p != True and q != True:
            return False
        if p == False and q == True:
            return True
        if p == True and q == False:
            return True

  the test is still green, so I change the next statement

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p and q:
            return False
        if not p and not q:
        # if p != True and q != True:
            return False
        if p == False and q == True:
            return True
        if p == True and q == False:
            return True

  still green, on to the next one

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p and q:
            return False
        if not p and not q:
            return False
        if not p and q:
        # if p == False and q == True:
            return True
        if p == True and q == False:
            return True

  the terminal still shows green. I change the next statement

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p and q:
            return False
        if not p and not q:
            return False
        if not p and q:
            return True
        if p and not q:
        # if p == True and q == False:
            return True

  still green.

* not_ shows up twice in the second `if statement`_, I "factor" it out

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p and q:
            return False
        if not (p or q):
        # if not p and not q:
            return False
        if not p and q:
            return True
        if p and not q:
            return True

  the terminal still shows green

* I add the two statements that return :ref:`False<test_what_is_false>`

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if (p and q) or not (p or q):
            return False
        else:
            return True
        if p and q:
            return False
        if not (p or q):
            return False
        if not p and q:
            return True
        if p and not q:
            return True

  the terminal still shows green

* I want the statement that returns :ref:`True<test_what_is_true>`, I use it to replace the else_ clause

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if (p and q) or not (p or q):
            return False
        if not ((p and q) or not (p or q)):
        # else:
            return True

  the terminal still shows green. I reorder the `if statements`_

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if not ((p and q) or not (p or q)):
            return True
        else:
        # if (p and q) or not (p or q):
            return False

  still green. I "multiply" out the statement

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if not (p and q) not or not (not (p or q)):
        # if not ((p and q) or not (p or q)):
            return True
        else:
            return False

  not_ or_ is and_

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if not (p and q) and not (not (p or q)):
        # if not ((p and q) or not (p or q)):
            return True
        else:
            return False

  not_ not_ cancels out

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if not (p and q) and (p or q):
        # if not (p and q) and not (not (p or q)):
            return True
        else:
            return False

* I can now use `conditional expressions`_

  .. code-block:: python

    def exclusive_disjunction(p, q):
        return True if not (p and q) and (p or q) else False
        if not (p and q) and (p or q):
        # if not (p and q) and not (not (p or q)):
            return True
        else:
            return False

  the terminal shows green. I can make it simpler

  .. code-block:: python

    def exclusive_disjunction(p, q):
        return not (p and q) and (p or q)
        return True if not (p and q) and (p or q) else False

  still green, I remove the second `return statement`


* Just like with ``logical_equality`` there is a simpler solution. Since the :ref:`function<functions>` returns :ref:`False<test_what_is_false>` when both ``p`` and ``q`` are the same

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p == q:
            return False
        else:
            return True

  I change the else_ clause to use the opposite of the `if statement`_

  .. code-block:: python



* I add a condition to resolve it

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p == True and q == True:
            return False
        if p == False and q == False:
            return False
        return True

  and all the tests pass. Wonderful!







* In the first case ``p`` and ``q`` have the same value, I can change the statement to reflect this like I did with ``logical_equality``

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p == q:
            return False
        if p == False and q == False:
            return False
        return True

  tests still pass
* the second statement looks similar, I can rewrite it as

  .. code-block:: python

    def exclusive_disjunction(p, q):
      if p == q:
          return False
      if p == q:
          return False
      return True

* I remove the repetition since it is exactly the same statement as the first

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p == q:
            return False
        return True

* I add an else_ clause to be explicit

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p == q:
            return False
        else:
            return True

* then rewrite it as the opposite `if statement`_

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p == q:
            return False
        if p != q:
            return True

* I reorder the statements

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p != q:
            return True
        if p == q:
            return False

* then change the second one with ``else``

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p != q:
            return True
        else:
            return False

* time to use the one line `return statement`_

  .. code-block:: python

    def exclusive_disjunction(p, q):
        return True if p != q else False

* then using implied conditional testing I can simplify it to

  .. code-block:: python

    def exclusive_disjunction(p, q):
        return p != q

----

*********************************************************************************
test_logical_nand
*********************************************************************************

red: make it fail
#################################################################################

I add a test for Logical NAND to ``TestBinaryOperations`` in ``test_truth_table.py``

.. code-block:: python

    def test_logical_nand(self):
        self.assertFalse(src.truth_table.logical_nand(True, True))
        self.assertTrue(src.truth_table.logical_nand(True, False))
        self.assertTrue(src.truth_table.logical_nand(False, True))
        self.assertTrue(src.truth_table.logical_nand(False, False))

the terminal shows :ref:`AttributeError`

green: make it pass
#################################################################################


* I add a definition for the :ref:`function<functions>` to ``truth_table.py`` returning :ref:`True<test_what_is_true>` since 3 out of the 4 cases return it

  .. code-block:: python

    def logical_nand(p, q):
      return True

  the terminal shows :ref:`AssertionError` for the first case
* and I add a condition for the one case that returns :ref:`False<test_what_is_false>`

  .. code-block:: python

    def logical_nand(p, q):
        if p == True and q == True:
            return False
        return True

  Green! All tests pass

refactor: make it better
#################################################################################

* I add an else_ clause to be explicit

  .. code-block:: python

    def logical_nand(p, q):
        if p == True and q == True:
            return False
        else:
            return True

* then change the first condition to an implied conditional test

  .. code-block:: python

    def logical_nand(p, q):
        if p and q:
            return False
        else:
            return True

* I make the else_ clause to the opposite of the `if statement`_

  .. code-block:: python

    def logical_nand(p, q):
        if p and q:
            return False
        if not (p and q):
            return True

* then reorder the statements

  .. code-block:: python

    def logical_nand(p, q):
        if not(p and q):
            return True
        if p and q:
            return False

* I change the second statement with ``else`` to simplify

  .. code-block:: python

    def logical_nand(p, q):
        if not(p and q):
            return True
        else:
            return False

* then change it to a one line `return statement`_

  .. code-block:: python

    def logical_nand(p, q):
        return True if not(p and q) else False

* which I simplify to

  .. code-block:: python

    def logical_nand(p, q):
        return not(p and q)

----

*********************************************************************************
test_logical_nor
*********************************************************************************

red: make it fail
#################################################################################

I add a test for exclusive disjunction to ``TestBinaryOperations`` in ``test_truth_table.py``

.. code-block:: python

    def test_logical_nor(self):
        self.assertFalse(src.truth_table.logical_nor(True, True))
        self.assertFalse(src.truth_table.logical_nor(True, False))
        self.assertFalse(src.truth_table.logical_nor(False, True))
        self.assertTrue(src.truth_table.logical_nor(False, False))

and the terminal shows :ref:`AttributeError`

green: make it pass
#################################################################################

* I add a :ref:`function<functions>` definition to ``truth_table.py``

  .. code-block:: python

    def logical_nor(p, q):
        return False

* and the first 3 pass, there is a failure for the 4th case, so I add a condition for it

  .. code-block:: python

    def logical_nor(p, q):
        if p == False and q == False:
            return True
        return False

refactor: make it better
#################################################################################

* I restate the ``if`` condition using hidden conditional testing

  .. code-block:: python

    def logical_nor(p, q):
        if not p and not q:
            return True
        return False

* I abstract the repetition of not_ by rewriting the entire statement in terms of not_

  .. code-block:: python

    def logical_nor(p, q):
        if (not p) (not or) (not q):
            return True
        return False

  the terminal shows a SyntaxError_ and I rewrite the statement with proper syntax, "factoring" out the not_

  .. code-block:: python

    def logical_nor(p, q):
        if not(p or q):
            return True
        return False

* then rewrite the entire thing on one line

  .. code-block:: python

    def logical_nor(p, q):
      return True if not(p or q) else False

* I simplify using implied conditional testing

  .. code-block:: python

    def logical_nor(p, q):
        return not(p or q)

----

*********************************************************************************
test_converse_non_implication
*********************************************************************************

red: make it fail
#################################################################################

I add a test for converse nonimplication to ``TestBinaryOperations`` in ``test_truth_table.py``

.. code-block:: python

    def test_converse_non_implication(self):
        self.assertFalse(src.truth_table.converse_non_implication(True, True))
        self.assertFalse(src.truth_table.converse_non_implication(True, False))
        self.assertTrue(src.truth_table.converse_non_implication(False, True))
        self.assertFalse(src.truth_table.converse_non_implication(False, False))

the terminal shows :ref:`AttributeError`

green: make it pass
#################################################################################

* I add a :ref:`function<functions>` definition to ``truth_table.py``

  .. code-block:: python

    def converse_non_implication(p, q):
        return False

  since the first two cases pass, the terminal shows :ref:`AssertionError` for the third case
* I add a condition for it

  .. code-block:: python

    def converse_non_implication(p, q):
        if p == False and q == True:
            return True
        return False

  all the tests pass

refactor: make it better
#################################################################################

* I use implied conditional testing with not_ for the first part of the if statement

  .. code-block:: python

    def converse_non_implication(p, q):
        if not p and q  == True:
            return True
        return False

  and the test passes

* I do the same for the second part of the statement

  .. code-block:: python

    def converse_non_implication(p, q):
        if not p and q:
            return True
        return False

* I add an else clause

  .. code-block:: python

    def converse_non_implication(p, q):
        if not p and q:
            return True
        else:
          return False

* then I rewrite as a ``return`` statement

  .. code-block:: python

    def converse_non_implication(p, q):
        return not p and q

  Another success! All tests pass

----

*********************************************************************************
review
*********************************************************************************


----

:doc:`/code/code_truth_table`