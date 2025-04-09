.. include:: ../../../links.rst

.. _binary_operations_i:

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

There are 16 binary operations, they take 2 inputs that can be :ref:`True <test_what_is_true>` or :ref:`False <test_what_is_false>`, which gives them all four cases

* :ref:`True <test_what_is_true>`, :ref:`True <test_what_is_true>`
* :ref:`True <test_what_is_true>`, :ref:`False <test_what_is_false>`
* :ref:`False <test_what_is_false>`, :ref:`True <test_what_is_true>`
* :ref:`False <test_what_is_false>`, :ref:`False <test_what_is_false>`

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

.. code-block:: python

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

* There are only 2 results for this operation, in the first case the :ref:`function<functions>` returns `True <test_what_is_true>` and in the other 3 cases it returns `False <test_what_is_false>`. I remove the commented line and rewrite the `if statement`_ for the case where the result is `True <test_what_is_true>` then use an else_ clause for the other cases

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

I add another test

.. code-block:: python

  def test_project_second(self):
      ...

  def test_converse_non_implication(self):
      self.assertFalse(src.truth_table.converse_non_implication(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'converse_non_implication'

green: make it pass
#################################################################################

I add the :ref:`function<functions>`

.. code-block:: python

  def project_second(p, q):
      return q



  def converse_non_implication(p, q):
      return q

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: True is not false

I add an `if statement`_

.. code-block:: python

  def converse_non_implication(p, q):
      if p == True:
          if q == True:
              return False
      return q

the test passes

refactor: make it better
#################################################################################

* I add another case

  .. code-block:: python

    def test_converse_non_implication(self):
        self.assertFalse(src.truth_table.converse_non_implication(True, True))
        self.assertFalse(src.truth_table.converse_non_implication(True, False))

  the terminal still shows green. I add another `if statement`_ to make sure

  .. code-block:: python

    def converse_non_implication(p, q):
        if p == True:
            if q == False:
                return True
            if q == True:
                return False
        return q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I fix the statement

  .. code-block:: python

    def converse_non_implication(p, q):
        if p == True:
            if q == False:
                return False
            if q == True:
                return False
        return q

  the test is green again

* I add the third case

  .. code-block:: python

    def test_converse_non_implication(self):
        self.assertFalse(src.truth_table.converse_non_implication(True, True))
        self.assertFalse(src.truth_table.converse_non_implication(True, False))
        self.assertTrue(src.truth_table.converse_non_implication(False, True))

  the test is still green. I add another `if statement`_ to check

  .. code-block:: python

    def converse_non_implication(p, q):
        if p == False:
            if q == True:
                return False
        if p == True:
            if q == False:
                return False
            if q == True:
                return False
        return q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I make it return :ref:`True<test_what_is_true>`

  .. code-block:: python

    def converse_non_implication(p, q):
        if p == False:
            if q == True:
                return True
        if p == True:
            if q == False:
                return False
            if q == True:
                return False
        return q

  the test is green again

* I add the next case

  .. code-block:: python

    def test_converse_non_implication(self):
        self.assertFalse(src.truth_table.converse_non_implication(True, True))
        self.assertFalse(src.truth_table.converse_non_implication(True, False))
        self.assertTrue(src.truth_table.converse_non_implication(False, True))
        self.assertFalse(src.truth_table.converse_non_implication(False, False))

  the terminal still shows green. I add one more `if statement`_

  .. code-block:: python

    def converse_non_implication(p, q):
        if p == False:
            if q == False:
                return True
            if q == True:
                return True
        if p == True:
            if q == False:
                return False
            if q == True:
                return False
        return q

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I change the `return statement`_

  .. code-block:: python

    def converse_non_implication(p, q):
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
        return q

  the test is green again. I remove ``return q``

* there are only 2 results like with :ref:`Logical Conjunction<test_logical_conjunction>`, in one case the :ref:`function<functions>` return :ref:`True<test_what_is_true>` and in the other 3 it returns :ref:`False<test_what_is_false>`. I use an `if statement`_ for the case that returns :ref:`True<test_what_is_true>`

  .. code-block:: python

    def converse_non_implication(p, q):
        if p == False and q == True:
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
                return False

  the terminal still shows green. I remove the other `if statements`_ and change the first statement with bool_

  .. code-block:: python

    def converse_non_implication(p, q):
        if p != True and bool(q):
        # if p == False and q == True:
            return True
        else:
            return False

  still green. I remove the comment and rewrite the line again, using bool_ and not_ for the first part

  .. code-block:: python

    def converse_non_implication(p, q):
        if not bool(p) and q:
        # if p != True and bool(q):
            return True
        else:
            return False

  still green, ``x != True`` is the same as ``not bool(x)``. I remove the commented line and make the line simpler

  .. code-block:: python

    def converse_non_implication(p, q):
        if not p and q:
        # if not bool(p) and q:
            return True
        else:
            return False

  the test is still green. I use a `conditional expression`_

  .. code-block:: python

    def converse_non_implication(p, q):
        return True if not p and q else False
        if not p and q:
            return True
        else:
            return False

  still green. I use the simpler `return statement`_

  .. code-block:: python

    def converse_non_implication(p, q):
        return not p and q
        return True if not p and q else False

  all tests are still passing. I remove the second `return statement`

  .. code-block:: python

    def converse_non_implication(p, q):
        return not p and q

----

*********************************************************************************
review
*********************************************************************************

From the tests I know that

* :ref:`Converse NonImplication <test_converse_non_implication>` returns ``not p and q``
* :ref:`Project Second <test_project_second>` always returns ``q``
* :ref:`Logical Conjunction <test_logical_conjunction>` returns ``p and q``
* :ref:`Contradiction <test_contradiction>` always returns :ref:`False<test_what_is_false>`

do you want to :ref:`test more binary operations? <binary_operations_ii>`

----

:doc:`/code/code_truth_table`