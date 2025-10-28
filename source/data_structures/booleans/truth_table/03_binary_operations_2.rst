.. meta::
  :description: Learn to build binary operations in Python with Test-Driven Development. This tutorial covers logical NAND, disjunction, and more. Watch the full tutorial!
  :keywords: Jacob Itegboje, python truth table binary operations, test driven development python tutorial, python logical operations for beginners, how to implement logical NAND in python, python TDD example with unittest, learn python binary logic step by step, python logical disjunction implementation, what is tautology in python programming

.. include:: ../../../links.rst

.. _binary_operations_ii:

#################################################################################
truth table: Binary Operations part 2
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/q_oGDjNG3_I?si=khc7CXDeEA5V46L0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

*********************************************************************************
requirements
*********************************************************************************

:ref:`Binary Operations part 1<truth table: Binary Operations part 1>`

----

*********************************************************************************
test_negate_first
*********************************************************************************

red: make it fail
#################################################################################

I add a test to the ``TestBinaryOperations`` :ref:`class<classes>` in ``test_truth_table.py``

.. code-block:: python

  def test_converse_non_implication(self):
      ...

  def test_negate_first(self):
      self.assertFalse(src.truth_table.negate_first(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'negate_first'

green: make it pass
#################################################################################

I add the :ref:`function<functions>` definition

.. code-block:: python

  def converse_non_implication(p, q):
      return not p and q


  def negate_first(p, q):
      return False

the test passes

refactor: make it better
#################################################################################

* I add the second case

  .. code-block:: python

    def test_negate_first(self):
        self.assertFalse(src.truth_table.negate_first(True, True))
        self.assertFalse(src.truth_table.negate_first(True, False))

  the test is still green

* I add the next case

  .. code-block:: python

    def test_negate_first(self):
        self.assertFalse(src.truth_table.negate_first(True, True))
        self.assertFalse(src.truth_table.negate_first(True, False))
        self.assertTrue(src.truth_table.negate_first(False, True))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I add an `if statement`_

  .. code-block:: python

    def negate_first(p, q):
        if p == False and q == True:
            return True
        return False

  the test passes

* I add the last case

  .. code-block:: python

    def test_negate_first(self):
        self.assertFalse(src.truth_table.negate_first(True, True))
        self.assertFalse(src.truth_table.negate_first(True, False))
        self.assertTrue(src.truth_table.negate_first(False, True))
        self.assertTrue(src.truth_table.negate_first(False, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I add an `if statement`_ for the case

  .. code-block:: python

    def negate_first(p, q):
        if p == False and q == False:
            return True
        if p == False and q == True:
            return True
        return False

  the test is green again

* The 2 cases where the :ref:`function<functions>` returns :ref:`True<test_what_is_true>` are when ``p`` is :ref:`False<test_what_is_false>`, I add a new `if statement`_ with an else_ clause

  .. code-block:: python

    def negate_first(p, q):
        if p == False:
            return True
        if p == False and q == False:
            return True
        if p == False and q == True:
            return True
        return False

  the test is still green. I remove the other `if statements`_ then use bool_ with not_

  .. code-block:: python

    def negate_first(p, q):
        if not bool(p):
        # if p == False:
            return True
        return False

  the test is still passing, I remove the commented line and simplify the `if statement`_

  .. code-block:: python

    def negate_first(p, q):
        if not p:
        # if not bool(p):
            return True
        return False

  the test is still green. I add a `ternary operator`_

  .. code-block:: python

    def negate_first(p, q):
        return True if not p else False
        if not p:
            return True
        return False

  the test is still passing. I change the `return statement`_ to the simpler form

  .. code-block:: python

    def negate_first(p, q):
        return not p
        return True if not p else False

  all tests are still passing. I remove the second `return statement`_

  .. code-block:: python

    def negate_first(p, q):
        return not p

----

*********************************************************************************
test_logical_nand
*********************************************************************************

red: make it fail
#################################################################################

I add a new test

.. code-block:: python

  def test_negate_first(self):
      ...

  def test_logical_nand(self):
      self.assertFalse(src.truth_table.logical_nand(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python
  :force:

  AttributeError: module 'src.truth_table' has no attribute 'logical_nand'. Did you mean: 'logical_false'?

green: make it pass
#################################################################################

I add a definition for the :ref:`function<functions>`

.. code-block:: python

  def negate_first(p, q):
      return not p


  def logical_nand(p, q):
      return False

the terminal shows green again

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

  using what I know so far, I add an `if statement`_

  .. code-block:: python

    def logical_nand(p, q):
        if p and not q
            return True
        return False

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

  I add an `if statement`_

  .. code-block:: python

    def logical_nand(p, q):
        if not p and q:
            return True
        if p and not q:
            return True
        return False

  green again

* I add the last case

  .. code-block:: python

    def test_logical_nand(self):
        self.assertFalse(src.truth_table.logical_nand(True, True))
        self.assertTrue(src.truth_table.logical_nand(True, False))
        self.assertTrue(src.truth_table.logical_nand(False, True))
        self.assertTrue(src.truth_table.logical_nand(False, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I add another `if statement`_

  .. code-block:: python

    def logical_nand(p, q):
        if not p and not q:
            return True
        if not p and q:
            return True
        if p and not q:
            return True
        return False

  the test is green again

* I add an `if statement`_ for the case that returns :ref:`False<test_what_is_false>` with an else_ clause for the other 3 that return :ref:`True<test_what_is_true>`

  .. code-block:: python

    def logical_nand(p, q):
        if p and q:
            return False
        else:
            return True
        if not p and not q:
            return True
        if not p and q:
            return True
        if p and not q:
            return True
        return False

  the test is still green. I want to use a single `return statement`_, which means I have to use an `if statement`_ that returns :ref:`True<test_what_is_true>`. I use :ref:`logical negation<test_logical_negation>` to change the else_ clause with not_

  .. code-block:: python

    def logical_nand(p, q):
        if p and q:
            return False
        if not (p and q):
        # else:
            return True

  the test is still green, I use the simple `return statement`_

  .. code-block:: python

    def logical_nand(p, q):
        return not (p and q)
        if p and q:
            return False
        if not (p and q):
            return True

  the test is still passing, I remove the other statements.

  .. code-block:: python

    def logical_nand(p, q):
        return not (p and q)

  When there is only one `if statement`_ that returns :ref:`False<test_what_is_false>` with an else_ clause, I can return its :ref:`logical negation<test_logical_negation>` with not_

----

*********************************************************************************
test_tautology
*********************************************************************************

red: make it fail
#################################################################################

I add a test

.. code-block:: python

  def test_logical_nand(self):
      ...

  def test_tautology(self):
      self.assertTrue(src.truth_table.tautology(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'tautology'

green: make it pass
#################################################################################

I add a :ref:`function<functions>` definition

.. code-block:: python

  def logical_nand(p, q):
      return not (p and q)


  def tautology(p, q):
      return True

the test passes

refactor: make it better
#################################################################################

* I add the next case

  .. code-block:: python

    def test_tautology(self):
        self.assertTrue(src.truth_table.tautology(True, True))
        self.assertTrue(src.truth_table.tautology(True, False))

  the terminal still shows green

* I add another case

  .. code-block:: python

    def test_tautology(self):
        self.assertTrue(src.truth_table.tautology(True, True))
        self.assertTrue(src.truth_table.tautology(True, False))
        self.assertTrue(src.truth_table.tautology(False, True))

  the test is still green

* I add the last case

  .. code-block:: python

    def test_tautology(self):
        self.assertTrue(src.truth_table.tautology(True, True))
        self.assertTrue(src.truth_table.tautology(True, False))
        self.assertTrue(src.truth_table.tautology(False, True))
        self.assertTrue(src.truth_table.tautology(False, False))

  still green, there is only one result for this operation.

----

*********************************************************************************
test_logical_disjunction
*********************************************************************************

red: make it fail
#################################################################################

I add another test

.. code-block:: python

  def test_tautology(self):
      ...

  def test_logical_disjunction(self):
      self.assertTrue(src.truth_table.logical_disjunction(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python
  :force:

  AttributeError: module 'src.truth_table' has no attribute 'logical_disjunction'. Did you mean: 'logical_conjunction'?

green: make it pass
#################################################################################

I add the :ref:`function<functions>`

.. code-block:: python

  def tautology(p, q):
      return True


  def logical_disjunction(p, q):
      return True

the test passes

refactor: make it better
#################################################################################

* I add the next case

  .. code-block:: python

    def test_logical_disjunction(self):
        self.assertTrue(src.truth_table.logical_disjunction(True, True))
        self.assertTrue(src.truth_table.logical_disjunction(True, False))

  the terminal still shows green

* I add the next case

  .. code-block:: python

    def test_logical_disjunction(self):
        self.assertTrue(src.truth_table.logical_disjunction(True, True))
        self.assertTrue(src.truth_table.logical_disjunction(True, False))
        self.assertTrue(src.truth_table.logical_disjunction(False, True))

  the test is still green

* I add the fourth case

  .. code-block:: python

    def test_logical_disjunction(self):
        self.assertTrue(src.truth_table.logical_disjunction(True, True))
        self.assertTrue(src.truth_table.logical_disjunction(True, False))
        self.assertTrue(src.truth_table.logical_disjunction(False, True))
        self.assertFalse(src.truth_table.logical_disjunction(False, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I add an `if statement`_

  .. code-block:: python

    def logical_disjunction(p, q):
        if not p and not q:
            return False
        return True

  the test passes

* I know from :ref:`Logical NAND<test_logical_nand>` that I can return the negation of the `if statement`_ that returns :ref:`False<test_what_is_false>`

  .. code-block:: python

    def logical_disjunction(p, q):
        return not (not p and not q):
        if not p and not q:
            return False
        return True

  the test is still green, ``not`` appears 3 times in this statement, I "multiply" it by each symbol in the parentheses to try to make the statement simpler

  .. code-block:: python

    def logical_disjunction(p, q):
        return not not p not and not not q:
        return not (not p and not q):

  the terminal shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  I add it to the list of :ref:`Exceptions<errors>` encountered in ``test_truth_table.py``

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # AttributeError
    # TypeError
    # SyntaxError

  then I fix the line by changing "not_ and_" to "or_"

  .. code-block:: python

    def logical_disjunction(p, q):
        return not not p or not not q:
        return not (not p and not q):

  the test passes. "not_ not_" cancels out, so I remove it from the statement

  .. code-block:: python

    def logical_disjunction(p, q):
        return p or q

----

*********************************************************************************
review
*********************************************************************************

Binary Operations take 2 inputs, each of them could be :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`, if we name the first input ``p`` and the second ``q``, the tests show that

* :ref:`Logical Disjunction <test_logical_disjunction>` returns ``p or q``
* :ref:`Tautology <test_tautology>` always returns :ref:`True<test_what_is_true>`
* :ref:`Logical NAND <test_logical_nand>` returns ``not (p and q)``
* :ref:`Negate First<test_negate_first>` always returns ``not p``
* :ref:`Converse NonImplication <test_converse_non_implication>` returns ``not p and q``
* :ref:`Project Second <test_project_second>` always returns ``q``
* :ref:`Logical Conjunction <test_logical_conjunction>` returns ``p and q``
* :ref:`Contradiction <test_contradiction>` always returns :ref:`False<test_what_is_false>`

do you want to :ref:`test more binary operations? <binary_operations_iii>`

----

:ref:`truth table: tests and solutions`