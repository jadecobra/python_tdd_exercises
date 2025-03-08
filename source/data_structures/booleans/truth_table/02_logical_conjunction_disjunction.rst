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

There are 16 binary operations with outcomes for conditions using booleans_

*********************************************************************************
test_logical_conjunction
*********************************************************************************

red: make it fail
#################################################################################

I add a TestCase_ to ``test_truth_table.py`` with ``test_logical_conjunction`` as the first test

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

I change the `return statement`_

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

  I add a condition to the :ref:`function <functions>`

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

  I add another condition

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

  I add a condition

  .. code-block:: python

    def logical_conjunction(p, q):
        if p == False:
            if q == True:
                return False
            if q == False:
                return False
        if p == True:
            if q == False:
                return False
        return True

  the terminal shows passing tests

* I add the condition for the first case to make it clear



* I can express these conditions on one line with the and_ keyword

  .. code-block:: python

    def logical_conjunction(p, q):
        if p == True and q == True:
            return True
        return False

  still green
* I rewrite the opposite of the `if statement`_ by adding an else_ clause

  .. code-block:: python

    def logical_conjunction(p, q):
        if p == True and q == True:
            return True
        else:
            return False

  tests are still green because this covers all four cases

  - in the case where ``p is True`` and ``q is True`` it returns :ref:`True<test_what_is_true>`
  - in the 3 remaining cases it returns False
  - in a binary operation, even though there are 4 cases, there are only 2 outcomes. I can write a condition for one case then write an else_ clause for the others, I do not have to write a condition for every case

  .. note::

    comparisons_ for :ref:`booleans` can be implicitly stated because Python calls ``bool()`` on the values, which returns :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`. This means ``if p == True`` can be rewritten as ``if p``

  I rewrite the `if statement`_ in a simpler way

  .. code-block:: python

    def logical_conjunction(p, q):
        if p and q:
            return True
        else:
            return False

  the tests are still green, so far so good
* I can use `conditional expressions`_(`ternary operators`_) to make the `return statement`_ simpler

  .. code-block:: python

    def logical_conjunction(p, q):
        return True if p and q else False

* since Python implicitly tests conditionals I can make the statement even simpler

  .. code-block:: python

    def logical_conjunction(p, q):
        return p and q

  tests are still green. I don't think I can get a simpler statement than this

----

*********************************************************************************
test_logical_disjunction
*********************************************************************************

red: make it fail
#################################################################################

I add a test for logical disjunction to ``TestBinaryOperations`` in ``test_truth_table.py``

.. code-block:: python

    def test_logical_disjunction(self):
        self.assertTrue(src.truth_table.logical_disjunction(True, True))
        self.assertTrue(src.truth_table.logical_disjunction(True, False))
        self.assertTrue(src.truth_table.logical_disjunction(False, True))
        self.assertFalse(src.truth_table.logical_disjunction(False, False))

and the terminal shows :ref:`AttributeError`

green: make it pass
#################################################################################

* Then I make ``truth_table.py`` with a:ref:`function<functions>`definition like I did for ``logical_conjunction``

  .. code-block:: python

    def logical_disjunction(p, q):
        return True

  and the terminal shows :ref:`AssertionError`

* 3 of the test cases are passing because ``logical_disjunction`` returns :ref:`True<test_what_is_true>` for each one of them. I need a condition for the fourth case to pass, so I change the definition

  .. code-block:: python

    def logical_disjunction(p, q):
        if p == False:
            if q == False:
                return False
        return True

  the terminal shows passing tests

refactor: make it better
#################################################################################

* I know from :doc:`/data_structures/booleans/truth_table/02_logical_conjunction` that when I have a nested if statement it can be changed with an and_ so I make the condition

  .. code-block:: python

    def logical_disjunction(p, q):
        if p == False and q == False:
            return False
        return True

  the terminal shows the tests are still passing

* I can restate the equality comparison against :ref:`False<test_what_is_false>` in terms of :ref:`True<test_what_is_true>` by using the ``not equal`` comparison operator ``!=``

  .. code-block:: python

    def logical_disjunction(p, q):
        if p != True and q != True:
            return False
        return True

* I can also express the `if statement`_ with the not_ keyword like I did with ``logical_negation`` to express the opposite of a :doc:`boolean </data_structures/booleans/booleans>`

  .. code-block:: python

    def logical_disjunction(p, q):
        if not p and not q:
            return False
        return True

* not_ happens twice in that statement, which I can "factor" out like in algebra

  .. code-block:: python

    def logical_disjunction(p, q):
        if not(p and q):
            return False
        return True

  the terminal shows a failing test. OOPS! I have introduced a regression. If I expand the statement using "multiplication" rules. What I have above is

  .. code-block:: python

    def logical_disjunction(p, q):
        if not p not and not q:
            return False
        return True

  I get a SyntaxError_ which I add to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # TypeError
    # SyntaxError

* The result of the "multiplication" is different from what I started with so I need something different. It should be something that expands out to

  .. code-block:: python

      def logical_disjunction(p, q):
          if not p not not and not q:
              return False
          return True

  this would "factor" out to be

  .. code-block:: python

    def logical_disjunction(p, q):
        if not(p not and q):
            return False
        return True

  okay, this looks more like what will get the original statement when "multiplied" since ``the opposite of the opposite of something is something``. To fix the syntax I use the opposite of and_ which is or_

  .. code-block:: python

    def logical_disjunction(p, q):
        if not(p or q):
            return False
        return True

  Hooray! tests are passing again

* I add an else statement to be explicit

  .. code-block:: python

    def logical_disjunction(p, q):
        if not(p or q):
            return False
        else:
            return True

* the else_ clause that returns :ref:`True<test_what_is_true>` can be restated as the opposite of the `if statement`_

  .. code-block:: python

    def logical_disjunction(p, q):
        if not(p or q):
            return False
        if not(not(p or q)):
            return True

  since the ``the opposite of the opposite of something is something`` I could restate it by canceling out the ``nots``

  .. code-block:: python

    def logical_disjunction(p, q):
        if not(p or q):
            return False
        if p or q:
            return True

* I then reorder the statements

  .. code-block:: python

    def logical_disjunction(p, q):
        if p or q:
            return True
        if not(p or q):
            return False

* I restate using ``else``

  .. code-block:: python

    def logical_disjunction(p, q):
        if p or q:
            return True
        else:
            return False

* then rewrite to one line with a ``return`` statement

  .. code-block:: python

    def logical_disjunction(p, q):
        return True if p or q else return False

* using python's implicit conditional evaluation I simplify to

  .. code-block:: python

    def logical_disjunction(p, q):
        return p or q

  *VOILA!* the tests still pass and I have a simple statement that makes all 4 states pass for ``logical_disjunction``

----

*********************************************************************************
review
*********************************************************************************

From the tests, I know that for any :ref:`boolean<booleans>` operation involving 2 inputs: ``p`` and ``q`` for example, that can take the values :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`


* ``return True if x else y`` can be rewritten as ``return x`` if ``x`` evaluates to :ref:`True<test_what_is_true>`
* even though there are 4 cases, there are only 2 outcomes, I only need to write the condition for the special case and use an else_ clause for the others
* ``logical negation`` is not_
* ``logical conjunction`` is and_

:ref:`Logical Implication <truth_table: Logical Implication>` is next

----

:doc:`/code/code_truth_table`