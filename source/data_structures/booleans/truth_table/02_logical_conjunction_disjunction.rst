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

  for the line that was passing before. ``logical_conjunction`` has to choose which boolean_ it will return based on the inputs. I can make it do that with `if statements`_

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

  I change :ref:`False <test_what_is_false>` to :ref:`True<test_what_is_true>` in the new line and and comment out the last `return statement`_

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

  the terminal shows green again.

* There are only two results for this operation, in the first case the :ref:`function<functions>` returns `True <test_what_is_true>` and in the other 3 cases it returns `False <test_what_is_false>`. I remove the commented line and rewrite the `if statement`_ for the case where the result is `True <test_what_is_true>` then use an else_ clause for the other cases

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

  the test is still green. I remove the other `if statements`_ then rewrite the first statement with bool_

  .. code-block:: python

    def logical_conjunction(p, q):
        if bool(p) and bool(q):
        # if p == True and q == True:
            return True
        else:
            return False

  still green. ``bool(x)`` checks if ``x`` is :ref:`True <test_what_is_true>`. I remove the commented line and rewrite the first line

  .. code-block:: python

    def logical_conjunction(p, q):
        if p and q:
        # if bool(p) and bool(q):
            return True
        else:
            return False

  the test is still green, Python tests ``p`` and ``q`` for truth in the background, I remove the commented line

* Python has `ternary operators`_ (`conditional expressions`_) which allows me to write the `if statements`_ in a simpler way

  .. code-block:: python

    def logical_conjunction(p, q):
        return True if p and q else False
        if p and q:
            return True
        else:
            return False

  the terminal shows green, I remove the other `if statements`_ and rewrite the `return statement`_ to make it simpler, thanks to Python's truth value testing

  .. code-block:: python

    def logical_conjunction(p, q):
        return p and q
        return True if p and q else False

  still green! I remove the second `return statement`_

  .. code-block:: python

    def logical_conjunction(p, q):
        return p and q

  and rename the test

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

I add another test to the ``TestBinaryOperations`` TestCase_

.. code-block:: python

  def test_logical_conjunction_aka_and(self):
      ...
      self.assertFalse(src.truth_table.logical_conjunction(False, False))

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

the test passes

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

  I add an `if statement`_ for this case

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

  I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the `return statement`_

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
        return p and q

  the test passes, and I add an `if statement`_ for the first case

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
        # return p and q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I change the `return statement`_

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

  the terminal shows green again and I remove the commented line

* There are also only two results for ``logical_disjunction`` - :ref:`True<test_what_is_true>` in one case and :ref:`False<test_what_is_false>` in the other 3 cases. I add a new `if statement`_ with an else_ clause

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

  the terminal still shows green. I remove the other `if statements`_, then write the opposite of the `if statement`_

  .. code-block:: python

    def logical_disjunction(p, q):
        if p == False and q == False:
            return False
        else:
            return True

  the test is still green. I remove the commented line and rewrite the else_ clause with the opposite of the `if statement`_ using ``logical_negation(not)``

  .. code-block:: python

    def logical_disjunction(p, q):
        if p == False and q == False:
            return False
        if not (p == False and q == False):
        # else:
            return True

  still green. I remove the commented line and move the first two lines to the bottome

  .. code-block:: python

    def logical_disjunction(p, q):
        if not (p == False and q == False):
            return True
        if p == False and q == False:
            return False

  the test is still green. I change the second `if statement` to an else_ clause

  .. code-block:: python

    def logical_disjunction(p, q):
        if not (p == False and q == False):
            return True
        else:
        # if p == False and q == False:
            return False

  the terminal shows green. I remove the commented line and "multiply" not_ by each symbol in the parentheses

  .. code-block:: python

    def logical_disjunction(p, q):
        if not p not == not False not and not q not == not False:
        # if not (p == False and q == False):
            return True
        else:
            return False

  the terminal shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  - not_ ``==`` is ``!=``
  - not_ :ref:`False<test_what_is_false>` is :ref:`True<test_what_is_true>`
  - not_ and_ is or_

  I fix the line

  .. code-block:: python

    def logical_disjunction(p, q):
        if not p != True or not q != True:
        # if not (p == False and q == False):
            return True
        else:
            return False

  and the test passes. I remove the commented line and rewrite the first line to remove not_

  .. code-block:: python

    def logical_disjunction(p, q):
        if p == True or q == True:
        # if not p != True or not q != True:
            return True
        else:
            return False


  ``not p != True`` is the same as ``p == True``. I remove the commented line then rewrite it with bool_

  .. code-block:: python

    def logical_disjunction(p, q):
        if bool(p) or bool(q):
        # if p == True or q == True:
            return True
        else:
            return False

  I remove the comment and rewrite the `if statement`_ with Python's hidden truth value testing

  .. code-block:: python

    def logical_disjunction(p, q):
        if p or q:
        # if bool(p) or bool(q):
            return True
        else:
            return False

  still green. I rewrite the statements as a `conditional expression`_

  .. code-block:: python

    def logical_disjunction(p, q):
        return True if p or q else False
        if p or q:
            return True
        else:
            return False

  the test is still green. I remove the `if statements`_ then use a simpler `return statement`_

  .. code-block:: python

    def logical_disjunction(p, q):
        return p or q
        return True if p or q else False

  green again. I remove the second `return statement`_

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
* ``logical_disjunction`` which is or_
* ``logical negation`` which is not_

:ref:`Logical Implication and Logical Equality<truth table: Logical Implication and Logical Equality>` are next

----

:doc:`/code/code_truth_table`