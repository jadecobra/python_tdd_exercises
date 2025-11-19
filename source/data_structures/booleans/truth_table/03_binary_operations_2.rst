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
  :lineno-start: 49
  :emphasize-lines: 3-4

          self.assertFalse(src.truth_table.converse_non_implication(False, False))

      def test_negate_first(self):
          self.assertFalse(src.truth_table.negate_first(True, True))


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'negate_first'

green: make it pass
#################################################################################

I add the :ref:`function<functions>` definition in ``truth_table.py``

.. code-block:: python
  :lineno-start: 29
  :emphasize-lines: 5-6

  def converse_non_implication(p, q):
      return not p and q


  def negate_first(p, q):
      return False

the test passes

refactor: make it better
#################################################################################

* I add the second case to ``test_negate_first`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 3

        def test_negate_first(self):
            self.assertFalse(src.truth_table.negate_first(True, True))
            self.assertFalse(src.truth_table.negate_first(True, False))

  the test is still green

* I add the next case

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 4

        def test_negate_first(self):
            self.assertFalse(src.truth_table.negate_first(True, True))
            self.assertFalse(src.truth_table.negate_first(True, False))
            self.assertTrue(src.truth_table.negate_first(False, True))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I add an `if statement`_ to ``negate_first`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2-3

    def negate_first(p, q):
        if p == False and q == True:
            return True
        return False

  the test passes

* I add the last case to ``test_negate_first`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 5

        def test_negate_first(self):
            self.assertFalse(src.truth_table.negate_first(True, True))
            self.assertFalse(src.truth_table.negate_first(True, False))
            self.assertTrue(src.truth_table.negate_first(False, True))
            self.assertTrue(src.truth_table.negate_first(False, False))


    # Exceptions Encountered

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

* I add an `if statement`_ for the case to the ``negate_first`` :ref:`function<functions>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2-3

    def negate_first(p, q):
        if p == False and q == False:
            return True
        if p == False and q == True:
            return True
        return False

  the test is green again

* The 2 cases where the :ref:`function<functions>` returns :ref:`True<test_what_is_true>` are when ``p`` is :ref:`False<test_what_is_false>`, I add a new `if statement`_ with an else_ clause

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2-5

    def negate_first(p, q):
        if p == False:
            return True
        else:
            return False
        if p == False and q == False:
            return True
        if p == False and q == True:
            return True
        return False

  the test is still green

* I remove the other `if statements`_ then use bool_ with not_

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2-3

    def negate_first(p, q):
        if not bool(p):
        # if p == False:
            return True
        return False

  the test is still passing

* I remove the commented line and simplify the `if statement`_

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2-3

    def negate_first(p, q):
        if not p:
        # if not bool(p):
            return True
        return False

  the test is still green

* I add a `ternary operator`_

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2

    def negate_first(p, q):
        return True if not p else False
        if not p:
            return True
        return False

  the test is still passing

* I change the `return statement`_ to the simpler form

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2

    def negate_first(p, q):
        return not p
        return True if not p else False

  the test is still green

* I remove the second `return statement`_

  .. code-block:: python
    :lineno-start: 33

    def negate_first(p, q):
        return not p

----

*********************************************************************************
test_logical_nand
*********************************************************************************

red: make it fail
#################################################################################

I add a new test to ``test_truth_table.py``

.. code-block:: python
  :lineno-start: 55
  :emphasize-lines: 3-4

          self.assertTrue(src.truth_table.negate_first(False, False))

      def test_logical_nand(self):
          self.assertFalse(src.truth_table.logical_nand(True, True))


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: python
  :force:

  AttributeError: module 'src.truth_table' has no attribute 'logical_nand'. Did you mean: 'logical_false'?

green: make it pass
#################################################################################

I add a definition for the :ref:`function<functions>` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 33
  :emphasize-lines: 5-6

  def negate_first(p, q):
      return not p


  def logical_nand(p, q):
      return False

the terminal_ shows green again

refactor: make it better
#################################################################################

* I add the next case to ``test_logical_nand`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 3

        def test_logical_nand(self):
            self.assertFalse(src.truth_table.logical_nand(True, True))
            self.assertTrue(src.truth_table.logical_nand(True, False))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

* I add an `if statement`_ to ``logical_nand`` in ``truth_table.py`` using what I know so far

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2-3

    def logical_nand(p, q):
        if p and not q
            return True
        return False

  the test passes

* I add another case to ``test_logical_nand`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 4

        def test_logical_nand(self):
            self.assertFalse(src.truth_table.logical_nand(True, True))
            self.assertTrue(src.truth_table.logical_nand(True, False))
            self.assertTrue(src.truth_table.logical_nand(False, True))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

* I add an `if statement`_ to ``logical_nand`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2-3

    def logical_nand(p, q):
        if not p and q:
            return True
        if p and not q:
            return True
        return False

  the test passes

* I add the last case to ``test_logical_nand`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 5

        def test_logical_nand(self):
            self.assertFalse(src.truth_table.logical_nand(True, True))
            self.assertTrue(src.truth_table.logical_nand(True, False))
            self.assertTrue(src.truth_table.logical_nand(False, True))
            self.assertTrue(src.truth_table.logical_nand(False, False))

    # Exceptions Encountered

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

* I add another `if statement`_ to ``logical_nand`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2-3

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
    :lineno-start: 37
    :emphasize-lines: 2-5

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

  the test is still green

* I want to use a single `return statement`_, which means I have to use an `if statement`_ that returns :ref:`True<test_what_is_true>`. I remove the other `return statements`_ then use :ref:`logical negation<test_logical_negation>` to change the else_ clause with not_

  .. code-block:: python
    :emphasize-lines: 4-5

    def logical_nand(p, q):
        if p and q:
            return False
        if not (p and q):
        # else:
            return True

  the test is still green

* I remove the comment, then add a simple `return statement`_

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2

    def logical_nand(p, q):
        return not (p and q)
        if p and q:
            return False
        if not (p and q):
            return True

  the test is still passing

* I remove the other statements

  .. code-block:: python
    :lineno-start: 37

    def logical_nand(p, q):
        return not (p and q)

  When there is only one `if statement`_ that returns :ref:`False<test_what_is_false>` with an else_ clause, I can return its :ref:`logical negation<test_logical_negation>` with not_

----

*********************************************************************************
test_tautology
*********************************************************************************

red: make it fail
#################################################################################

I add a test for the next Binary Operation to ``test_truth_table.py``

.. code-block:: python
  :lineno-start: 61
  :emphasize-lines: 3-4

          self.assertTrue(src.truth_table.logical_nand(False, False))

      def test_tautology(self):
          self.assertTrue(src.truth_table.tautology(True, True))


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'tautology'

green: make it pass
#################################################################################

I add a :ref:`function<functions>` definition to ``truth_table.py``

.. code-block:: python
  :lineno-start: 37
  :emphasize-lines: 5-6

  def logical_nand(p, q):
      return not (p and q)


  def tautology(p, q):
      return True

the test passes

refactor: make it better
#################################################################################

* I add the next case to ``test_tautology`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 3

        def test_tautology(self):
            self.assertTrue(src.truth_table.tautology(True, True))
            self.assertTrue(src.truth_table.tautology(True, False))

  the terminal_ still shows green

* I add another case

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 4

        def test_tautology(self):
            self.assertTrue(src.truth_table.tautology(True, True))
            self.assertTrue(src.truth_table.tautology(True, False))
            self.assertTrue(src.truth_table.tautology(False, True))

  the test is still green

* I add the last case

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 5

        def test_tautology(self):
            self.assertTrue(src.truth_table.tautology(True, True))
            self.assertTrue(src.truth_table.tautology(True, False))
            self.assertTrue(src.truth_table.tautology(False, True))
            self.assertTrue(src.truth_table.tautology(False, False))


    # Exceptions Encountered

  still green, there is only one result for this operation.

----

*********************************************************************************
test_logical_disjunction
*********************************************************************************

red: make it fail
#################################################################################

I add another test

.. code-block:: python
  :lineno-start: 67
  :emphasize-lines: 4-5

          self.assertTrue(src.truth_table.tautology(False, False))

      def test_logical_disjunction(self):
          self.assertTrue(src.truth_table.logical_disjunction(True, True))


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: python
  :force:

  AttributeError: module 'src.truth_table' has no attribute 'logical_disjunction'. Did you mean: 'logical_conjunction'?

green: make it pass
#################################################################################

I add the :ref:`function<functions>` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 41
  :emphasize-lines: 5-6

  def tautology(p, q):
      return True


  def logical_disjunction(p, q):
      return True

the test passes

refactor: make it better
#################################################################################

* I add the next case to ``test_logical_disjunction`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 3

        def test_logical_disjunction(self):
            self.assertTrue(src.truth_table.logical_disjunction(True, True))
            self.assertTrue(src.truth_table.logical_disjunction(True, False))

  the terminal_ still shows green

* I add the next case

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 4

        def test_logical_disjunction(self):
            self.assertTrue(src.truth_table.logical_disjunction(True, True))
            self.assertTrue(src.truth_table.logical_disjunction(True, False))
            self.assertTrue(src.truth_table.logical_disjunction(False, True))

  the test is still green

* I add the fourth case

  .. code-block:: python
    :lineno-start: 69
    :emphasize-liens: 5

        def test_logical_disjunction(self):
            self.assertTrue(src.truth_table.logical_disjunction(True, True))
            self.assertTrue(src.truth_table.logical_disjunction(True, False))
            self.assertTrue(src.truth_table.logical_disjunction(False, True))
            self.assertFalse(src.truth_table.logical_disjunction(False, False))


    # Exceptions Encountered

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

* I add an `if statement`_ for the new case to ``logical_disjunction`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2-3

    def logical_disjunction(p, q):
        if not p and not q:
            return False
        return True

  the test passes

* I know from :ref:`Logical NAND<test_logical_nand>` that I can return the negation of an `if statement`_ that returns :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2

    def logical_disjunction(p, q):
        return not (not p and not q)
        if not p and not q:
            return False
        return True

  the test is still green, ``not`` appears 3 times in this statement

* I remove the other statements then "multiply" ``not`` by each symbol in the parentheses to try to make the statement simpler

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2

    def logical_disjunction(p, q):
        return not not p not and not not q
        return not (not p and not q)

  the terminal_ shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

* I add it to the list of :ref:`Exceptions<errors>` encountered in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 5

    # Exceptions Encountered
    # AssertionError
    # AttributeError
    # TypeError
    # SyntaxError

* I fix the failing line by changing "not_ and_" to "or_" in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2

    def logical_disjunction(p, q):
        return not not p or not not q
        return not (not p and not q)

  the test passes

* I remove the second `return statement`_ and "not_ not_" from the statement because it cancels out

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2

    def logical_disjunction(p, q):
        return p or q

  the test is still green

----

*********************************************************************************
review
*********************************************************************************

Binary Operations take 2 inputs, each input can be :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`, if we name the first input ``p`` and the second ``q``, the tests show that

* :ref:`Logical Disjunction <test_logical_disjunction>` returns ``p or q``
* :ref:`Tautology <test_tautology>` always returns :ref:`True<test_what_is_true>`
* :ref:`Logical NAND <test_logical_nand>` returns ``not (p and q)``
* :ref:`Negate First<test_negate_first>` always returns ``not p``
* :ref:`Converse NonImplication <test_converse_non_implication>` returns ``not p and q``
* :ref:`Project Second <test_project_second>` always returns ``q``
* :ref:`Logical Conjunction <test_logical_conjunction>` returns ``p and q``
* :ref:`Contradiction <test_contradiction>` always returns :ref:`False<test_what_is_false>`

and

* :ref:`Logical Disjunction <test_logical_disjunction>` is "or_"
* :ref:`Logical Conjunction <test_logical_conjunction>` is "and_"
* :ref:`Logical Negation <test_logical_negation>` is "not_"

do you want to :ref:`test more binary operations? <binary_operations_iii>`

----

:ref:`truth table: tests and solutions`

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">Click Here to leave a 5 star review on TrustPilot, if you found this helpful</a>
  </div>
  <!-- End TrustBox widget -->