.. include:: ../../../links.rst

#################################################################################
truth table: Exclusive Disjunction and Logical NAND
#################################################################################

.. contents:: table of contents
  :local:
  :depth: 1

----

*********************************************************************************
requirements
*********************************************************************************

:doc:`how to make a python test driven development environment </how_to/make_tdd_environment>` with ``truth_table`` as the name of the project

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

From the tests I see that for any boolean operation involving 2 inputs: ``p`` and ``q`` which can take the values :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`

* ``exclusive disjunction`` is ``!=`` or the opposite of ``logical_equality``
* ``logical equality`` is ``==``
* ``logical implication`` is ``not p or q``
* ``logical disjunction`` is or_
* ``logical conjunction`` is and_
* and_ is "not or_"
* or_ is "not and_"
* :ref:`False<test_what_is_false>` is not_ :ref:`True<test_what_is_true>`
* :ref:`True<test_what_is_true>` is not_ :ref:`False<test_what_is_false>`
* :ref:`False<test_what_is_false>` is :ref:`False<test_what_is_false>`
* :ref:`True<test_what_is_true>` is :ref:`True<test_what_is_true>`


----

:doc:`/code/code_truth_table`