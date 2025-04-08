.. include:: ../../../links.rst

#################################################################################
truth table: Binary Operations I
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

----

*********************************************************************************
test_contradiction
*********************************************************************************

red: make it fail
#################################################################################

I add a new TestCase_ to ``test_truth_table.py``

.. code-block:: python

      def test_logical_negation_aka_not(self):
          ...


  class TestBinaryOperations(unittest.TestCase):

      def test_contradiction(self):
          self.assertFalse(src.truth_table.contradiction(True, True))

the terminal shows :ref:`AttributeError`

  AttributeError: module 'src.truth_table' has no attribute 'contradiction'

green: make it pass
#################################################################################

I add a :ref:`function<functions>` definition to ``truth_table.py``

.. code-block:: python

  def logical_negation(argument):
      return not argument


  def contradiction(argument):
      return not argument

the terminal shows :ref:`TypeError`

.. code-block:: python

  TypeError: contradiction() takes 1 positional argument but 2 were given

I change the signature to make it take 2 inputs

.. code-block:: python

  def contradiction(p, q):
      return not p

the test passes

refactor: make it better
#################################################################################

* I add the second case

  .. code-block:: python

    def test_contradiction(self):
        self.assertFalse(src.truth_table.contradiction(True, True))
        self.assertFalse(src.truth_table.contradiction(True, False))

  the test is still green. I change the `return statement` to make sure the test works

  .. code-block:: python

    def contradiction(p, q):
        return True
        return not p

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I remove the new statement and the test is green again

* I add the next case

  .. code-block:: python

    def test_contradiction(self):
        self.assertFalse(src.truth_table.contradiction(True, True))
        self.assertFalse(src.truth_table.contradiction(True, False))
        self.assertFalse(src.truth_table.contradiction(False, True))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  the test expects :ref:`False<test_what_is_false>` in the 3 cases so far, I change the `return statement` to match

  .. code-block:: python

    def contradiction(p, q):
        return False

  green again

* I add the fourth case

  .. code-block:: python

    def test_contradiction(self):
        self.assertFalse(src.truth_table.contradiction(True, True))
        self.assertFalse(src.truth_table.contradiction(True, False))
        self.assertFalse(src.truth_table.contradiction(False, True))
        self.assertFalse(src.truth_table.contradiction(False, False))

  another case that expects :ref:`False<test_what_is_false>`, the test is still green! :ref:`contradiction<test_contradiction>` is a :ref:`singleton function<test_singleton_functions>` it always returns :ref:`False<test_what_is_false>`

----

*********************************************************************************
test_logical_conjunction
*********************************************************************************

red: make it fail
#################################################################################

I add the next test

.. code-block:: python

  def test_contradiction(self):
      ...

  def test_logical_conjunction(self):
      self.assertTrue(src.truth_table.logical_conjunction(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python
  :force:

  AttributeError: module 'src.truth_table' has no attribute 'logical_conjunction'. Did you mean: 'logical_negation'?

green: make it pass
#################################################################################

I add the :ref:`function<functions>`

.. code-block:: python

  def contradiction(p, q):
      return False


  def logical_conjunction(p, q):
      return False

and the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: False is not true

I change :ref:`False <test_what_is_false>` to :ref:`True <test_what_is_true>` in the `return statement`_

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

  for the line that was passing before. ``logical_conjunction`` has to choose if it will return :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>` based on the inputs. I can make it do that with `if statements`_

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

  I add another `if statement`_

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

  I change :ref:`False <test_what_is_false>` to :ref:`True<test_what_is_true>` on the new line and comment out the last `return statement`_

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

  still green. ``bool(x)`` checks if ``x`` is :ref:`True <test_what_is_true>`. I remove the commented line and rewrite the first line to make it simpler

  .. code-block:: python

    def logical_conjunction(p, q):
        if p and q:
        # if bool(p) and bool(q):
            return True
        else:
            return False

  the test is still green, Python tests if ``p`` and ``q`` are :ref:`True<test_what_is_true>` in the background, I remove the commented line

* Python has `ternary operators`_ or `conditional expressions`_ which allow me to write the `if statements`_ as a one line `return statement`_

  .. code-block:: python

    def logical_conjunction(p, q):
        return True if p and q else False
        if p and q:
            return True
        else:
            return False

  the terminal shows green, I remove the other `if statements`_ and rewrite the `return statement`_ in an even simpler way thanks to Python's truth value testing

  .. code-block:: python

    def logical_conjunction(p, q):
        return p and q
        return True if p and q else False

  still green! I remove the second `return statement`_

  .. code-block:: python

    def logical_conjunction(p, q):
        return p and q

----

*********************************************************************************
test_project_second
*********************************************************************************

red: make it fail
#################################################################################

I add another test

.. code-block:: python

  def test_logical_conjunction(self):
      ...

  def test_project_second(self):
      self.assertTrue(src.truth_table.project_second(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'project_second'

green: make it pass
#################################################################################

When I add a :ref:`function<functions>` definition for it

.. code-block:: python

  def logical_conjunction(p, q):
      return p and q


  def project_second(p, q):
      return p and q

the test passes

refactor: make it better
#################################################################################

* I add the second case

  .. code-block:: python

    def test_project_second(self):
        self.assertTrue(src.truth_table.project_second(True, True))
        self.assertFalse(src.truth_table.project_second(True, False))

  the terminal shows green. I add an `if statement`_ to make sure it works

  .. code-block:: python

    def project_second(p, q):
        if p == True:
            if q == False:
                return True
        return p and q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I change the `return statement`_ I added

  .. code-block:: python

    def project_second(p, q):
        if p == True:
            if q == False:
                return False
        return p and q

  the test passes

* I add the next case

  .. code-block:: python

    def test_project_second(self):
        self.assertTrue(src.truth_table.project_second(True, True))
        self.assertFalse(src.truth_table.project_second(True, False))
        self.assertTrue(src.truth_table.project_second(False, True))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I add another `if statement`

  .. code-block:: python

    def project_second(p, q):
        if p == False:
            if q == True:
                return True
        if p == True:
            if q == False:
                return False
        return p and q

  the test is green again

* I add the last case

  .. code-block:: python

    def test_project_second(self):
        self.assertTrue(src.truth_table.project_second(True, True))
        self.assertFalse(src.truth_table.project_second(True, False))
        self.assertTrue(src.truth_table.project_second(False, True))
        self.assertFalse(src.truth_table.project_second(False, False))

  and the test is still green, I add an `if statement`_ for it anyways

  .. code-block:: python

    def project_second(p, q):
        if p == False:
            if q == False:
                return True
            if q == True:
                return True
        if p == True:
            if q == False:
                return False
        return p and q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I change the `return statement`_

  .. code-block:: python

    def project_second(p, q):
        if p == False:
            if q == False:
                return False
            if q == True:
                return True
        if p == True:
            if q == False:
                return False
        return p and q

  the test passes and I add an `if statement`_ for the first case

  .. code-block:: python

    def project_second(p, q):
        if p == False:
            if q == False:
                return False
            if q == True:
                return True
        if p == True:
            if q == False:
                return False
            if q == True:
                return False
        return p and q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I change :ref:`False<test_what_is_false>` to :ref:`True<test_what_is_true>` in the line I added

  .. code-block:: python

    def project_second(p, q):
        if p == False:
            if q == False:
                return False
            if q == True:
                return True
        if p == True:
            if q == False:
                return False
            if q == True:
                return True
        return p and q

  the test is green again. and remove ``return p and q``

* This :ref:`function<functions>` returns :ref:`True<test_what_is_true>` when ``q`` is :ref:`True<test_what_is_true>` and returns :ref:`False<test_what_is_false>` when it is not. I rewrite the statements in terms of ``q`` with an else_ clause

  .. code-block:: python

    def project_second(p, q):
        if q == True:
            return True
        else:
            return False
        if p == False:
            if q == False:
                return False
            if q == True:
                return True
        if p == True:
            if q == False:
                return False
            if q == True:
                return True

  the test is still green, I remove the other `if statements`_

  .. code-block:: python

    def project_second(p, q):
        if q == True:
            return True
        else:
            return False

  I rewrite the first statement with bool_ since it is the same as ``x == True``

  .. code-block:: python

    def project_second(p, q):
        if bool(q):
        # if q == True:
            return True
        else:
            return False

  the terminal still shows green. I remove the commented line and use a simpler `if statement`_ like I did with :ref:`Logical Conjunction<test_logical_conjunction>`

  .. code-block:: python

    def project_second(p, q):
        if q:
        # if bool(q):
            return True
        else:
            return False

  the test is still green. I use a `conditional expression`

  .. code-block:: python

    def project_second(p, q):
        return q
        if q:
            return True
        else:
            return False

  the terminal shows all tests are still passing. I remove the other statements

  .. code-block:: python

    def project_second(p, q):
        return q

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

  the test is still green. I add an `if statement`_

  .. code-block:: python

    def converse_non_implication(p, q):
        if not p and q:
            return False
        if p and not q:
            return False
        return p != q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I make it return :ref:`True<test_what_is_true>`

  .. code-block:: python

    def converse_non_implication(p, q):
        if not p and q:
            return True
        if p and not q:
            return False
        return p != q

  the test is green again

* I add the fourth case

  .. code-block:: python

    def test_converse_non_implication(self):
        self.assertFalse(src.truth_table.converse_non_implication(True, True))
        self.assertFalse(src.truth_table.converse_non_implication(True, False))
        self.assertTrue(src.truth_table.converse_non_implication(False, True))
        self.assertFalse(src.truth_table.converse_non_implication(False, False))

  the terminal still shows green. I add another `if statement`_

  .. code-block:: python

    def converse_non_implication(p, q):
        if not p and not q:
            return True
        if not p and q:
            return True
        if p and not q:
            return False
        return p != q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I change the `return statement`_

  .. code-block:: python

    def converse_non_implication(p, q):
        if not p and not q:
            return False
        if not p and q:
            return True
        if p and not q:
            return False
        return p != q

  the test is green again

* I move the statement where :ref:`True<test_what_is_true>` is the result to the top then add an else_ clause

  .. code-block:: python

    def converse_non_implication(p, q):
        if not p and q:
            return True
        else:
            return False
        if not p and not q:
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
test_logical_disjunction
*********************************************************************************

red: make it fail
#################################################################################

I add another test to the ``TestBinaryOperations`` TestCase_

.. code-block:: python

  def test_logical_conjunction(self):
      ...
      self.assertFalse(src.truth_table.logical_conjunction(False, False))

  def test_logical_disjunction(self):
      self.assertTrue(src.truth_table.logical_disjunction(True, True))

and the terminal shows :ref:`AttributeError`

.. code-block:: python
  :force:

  AttributeError: module 'src.truth_table' has no attribute 'logical_disjunction'. Did you mean: 'logical_conjunction'?

green: make it pass
#################################################################################

I add the :ref:`function<functions>`

.. code-block:: python

  def logical_conjunction(p, q):
    return p and q


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

  the terminal shows green. I add an `if statement`_ to double check the last case

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

  the test passes, I also add an `if statement`_ for the first case

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
        return p and q

  the terminal shows green again and I remove ``return p and q``

* There are only two results for ``logical_disjunction`` as well - :ref:`True<test_what_is_true>` in the first 3 cases and :ref:`False<test_what_is_false>` in the last case. I add a new `if statement`_ with an else_ clause

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

  the terminal still shows green. I remove the other statements then write the opposite of the `if statement`_

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

  still green. I remove the commented line and move the first two lines to the bottom

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

  the terminal shows green. I remove the commented line and "multiply" not_ by each symbol in the parentheses to make it simpler

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

  and the test passes. I remove the commented line and rewrite the `if statement`_

  .. code-block:: python

    def logical_disjunction(p, q):
        if not p == False or not q == False:
        # if not p != True or not q != True:
            return True
        else:
            return False

  ``not x == False`` is the same as ``x == True``, I rewrite the `if statement`_ to show this

  .. code-block:: python

    def logical_disjunction(p, q):
        if p == True or q == True:
        # if not p != True or not q != True:
            return True
        else:
            return False

  still green, I remove the commented line and rewrite it with bool_

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

    def test_logical_disjunction(self):
        self.assertTrue(src.truth_table.logical_disjunction(True, True))
        self.assertTrue(src.truth_table.logical_disjunction(True, False))
        self.assertTrue(src.truth_table.logical_disjunction(False, True))
        self.assertFalse(src.truth_table.logical_disjunction(False, False))

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

*********************************************************************************
review
*********************************************************************************

From the tests I know that

*  :ref:`Converse Implication <test_converse_implication>` returns ``p or not q``
* :ref:`Logical or Material Implication  <test_logical_implication>` returns ``not p or q``
* :ref:`Logical Disjunction <test_logical_disjunction>` is or_
* :ref:`Logical Conjunction <test_logical_conjunction>` is and_
* :ref:`Logical Negation<test_logical_negation>` is not_

do you want more :ref:`more binary operations? <truth table: Binary Operations II>`

----

:doc:`/code/code_truth_table`