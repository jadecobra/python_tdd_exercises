.. meta::
  :description: Master Python's boolean logic. This clear, step-by-step guide explains AND, OR, and NOT operators with easy-to-follow truth tables. Build your first one now.
  :keywords: Jacob Itegboje, python truth table for beginners, boolean logic and or not python tutorial, how to make a truth table in python code, practical use of truth tables in programming, python logical operators explained for new programmers, understanding boolean expressions in python, python 'and' vs 'or' truth table differences, troubleshooting boolean logic in python script

.. include:: ../../../links.rst

.. _binary_operations_iii:

#################################################################################
truth table: Binary Operations part 3
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/EaLR4MMiW4c?si=yok1ej79nisTRUBq" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

*********************************************************************************
requirements
*********************************************************************************

:ref:`Binary Operations part 2<truth table: Binary Operations part 2>`

----

*********************************************************************************
test_exclusive_disjunction
*********************************************************************************

red: make it fail
#################################################################################

I add a new test

.. code-block:: python

  def test_logical_disjunction(self):
      ...

  def test_exclusive_disjunction(self):
      self.assertFalse(src.truth_table.exclusive_disjunction(True, True))

the terminal_ shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'exclusive_disjunction'

green: make it pass
#################################################################################

I add the :ref:`function<functions>`

.. code-block:: python

  def logical_disjunction(p, q):
      return p or q


  def exclusive_disjunction(p, q):
      return False

the test passes

refactor: make it better
#################################################################################

* I add the next case

  .. code-block:: python

    def test_exclusive_disjunction(self):
        self.assertFalse(src.truth_table.exclusive_disjunction(True, True))
        self.assertTrue(src.truth_table.exclusive_disjunction(True, False))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I add an `if statement`_

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p and not q:
            return True
        return False

  the test is green again

* I add the third case

  .. code-block:: python

    def test_exclusive_disjunction(self):
        self.assertFalse(src.truth_table.exclusive_disjunction(True, True))
        self.assertTrue(src.truth_table.exclusive_disjunction(True, False))
        self.assertTrue(src.truth_table.exclusive_disjunction(False, True))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I add another `if statement`_

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if not p and q:
            return True
        if p and not q:
            return True
        return False

  the test is green

* I add the last case

  .. code-block:: python

    def test_exclusive_disjunction(self):
        self.assertFalse(src.truth_table.exclusive_disjunction(True, True))
        self.assertTrue(src.truth_table.exclusive_disjunction(True, False))
        self.assertTrue(src.truth_table.exclusive_disjunction(False, True))
        self.assertFalse(src.truth_table.exclusive_disjunction(False, False))

  the test is still green

* I can use :ref:`Logical Disjunction<test_logical_disjunction>` to put the two `if statements`_ that return :ref:`True<test_what_is_true>` together

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if (not p and q) or (p and not q):
            return True
        if not p and q:
            return True
        if p and not q:
            return True
        return False

  the test is still green. I remove the other `if statements`_ then use a simple `return statement`_

  .. code-block:: python

    def exclusive_disjunction(p, q):
        return (not p and q) or (p and not q)
        if (not p and q) or (p and not q):
            return True
        return False

  the terminal_ still shows green. I remove the other statements

  .. code-block:: python

    def exclusive_disjunction(p, q):
        return (not p and q) or (p and not q)

* This :ref:`function<functions>` returns :ref:`False<test_what_is_false>` in the 2 cases where ``p`` and ``q`` are the same, I can use this `if statement`_

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p == q:
            return False
        else:
            return True
        return (not p and q) or (p and not q)

  I can change it to a simple `return statement`_

  .. code-block:: python

    def exclusive_disjunction(p, q):
        return not (p == q)
        if p == q:
            return False
        else:
            return True
        return (not p and q) or (p and not q)

  there is an even simpler statement

  .. code-block:: python

    def exclusive_disjunction(p, q):
        return p != q
        return not (p == q)
        return (not p and q) or (p and not q)

  ``!=`` is the symbol for NOT equal

----

*********************************************************************************
test_material_non_implication
*********************************************************************************

red: make it fail
#################################################################################

I add another test

.. code-block:: python

    def test_exclusive_disjunction(self):
        ...

    def test_material_non_implication(self):
        self.assertFalse(src.truth_table.material_non_implication(True, True))

the terminal_ shows :ref:`AttributeError`

.. code-block:: python
  :force:

  AttributeError: module 'src.truth_table' has no attribute 'material_non_implication'. Did you mean: 'converse_non_implication'?

green: make it pass
#################################################################################

I add a :ref:`function<functions>`

.. code-block:: python

  def exclusive_disjunction(p, q):
      return p != q
      return not (p == q)
      return (not p and q) or (p and not q)


  def material_non_implication(p, q):
      return False

the test passes

refactor: make it better
#################################################################################

* I add another case

  .. code-block:: python

    def test_material_non_implication(self):
        self.assertFalse(src.truth_table.material_non_implication(True, True))
        self.assertTrue(src.truth_table.material_non_implication(True, False))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I add an `if statement`_

  .. code-block:: python

    def material_non_implication(p, q):
        if p and not q:
            return True
        return False

  the test passes

* I add the next case

  .. code-block:: python

    def test_material_non_implication(self):
        self.assertFalse(src.truth_table.material_non_implication(True, True))
        self.assertTrue(src.truth_table.material_non_implication(True, False))
        self.assertFalse(src.truth_table.material_non_implication(False, True))

  the test is still green

* I add the fourth case

  .. code-block:: python

    def test_material_non_implication(self):
        self.assertFalse(src.truth_table.material_non_implication(True, True))
        self.assertTrue(src.truth_table.material_non_implication(True, False))
        self.assertFalse(src.truth_table.material_non_implication(False, True))
        self.assertFalse(src.truth_table.material_non_implication(False, False))

  the terminal_ still shows green

* there is only one case where the result is :ref:`True<test_what_is_true>`, I add a `return statement`_ for it

  .. code-block:: python

    def material_non_implication(p, q):
        return p and not q
        if p and not q:
            return True
        return False

  the test is still green. I remove the other statements

  .. code-block:: python

    def material_non_implication(p, q):
        return p and not q

----

*********************************************************************************
test_project_first
*********************************************************************************

red: make it fail
#################################################################################

I add a test

.. code-block:: python

  def test_material_non_implication(self):
      ...

  def test_project_first(self):
      self.assertTrue(src.truth_table.project_first(True, True))

the terminal_ shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'project_first'

green: make it pass
#################################################################################

I add a :ref:`function<functions>` definition for it

.. code-block:: python

  def material_non_implication(p, q):
      return p and not q


  def project_first(p, q):
      return True

the test passes

refactor: make it better
#################################################################################

* I add the second case

  .. code-block:: python

    def test_project_first(self):
        self.assertTrue(src.truth_table.project_first(True, True))
        self.assertTrue(src.truth_table.project_first(True, False))

  the test is still green

* on to the next case

  .. code-block:: python

    def test_project_first(self):
        self.assertTrue(src.truth_table.project_first(True, True))
        self.assertTrue(src.truth_table.project_first(True, False))
        self.assertFalse(src.truth_table.project_first(False, True))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I add an `if statement`_

  .. code-block:: python

    def project_first(p, q):
        if not p and q:
            return False
        return True

  the test passes

* I add the last case

  .. code-block:: python

    def test_project_first(self):
        self.assertTrue(src.truth_table.project_first(True, True))
        self.assertTrue(src.truth_table.project_first(True, False))
        self.assertFalse(src.truth_table.project_first(False, True))
        self.assertFalse(src.truth_table.project_first(False, False))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I add another `if statement`_

  .. code-block:: python

    def project_first(p, q):
        if not p and not q:
            return False
        if not p and q:
            return False
        return True

* I add a `return statement`_ to show that this :ref:`function<functions>` returns the same value as ``p``

  .. code-block:: python

    def project_first(p, q):
        return p
        if not p and not q:
            return False
        if not p and q:
            return False
        return True

  still green. I remove the other statements

  .. code-block:: python

    def project_first(p, q):
        return p

----

*********************************************************************************
test_converse_implication
*********************************************************************************

red: make it fail
#################################################################################

I add a new test

.. code-block:: python

  def test_project_first(self):
      ...

  def test_converse_implication(self):
      self.assertTrue(src.truth_table.converse_implication(True, True))

the terminal_ shows :ref:`AttributeError`

.. code-block:: python
  :force:

  AttributeError: module 'src.truth_table' has no attribute 'converse_implication'. Did you mean: 'converse_non_implication'?

green: make it pass
#################################################################################

I add a :ref:`function<functions>` definition

.. code-block:: python

  def project_first(p, q):
      return p


  def converse_implication(p, q):
      return True

the test passes

refactor: make it better
#################################################################################

* I add the second case

  .. code-block:: python

    def test_converse_implication(self):
        self.assertTrue(src.truth_table.converse_implication(True, True))
        self.assertTrue(src.truth_table.converse_implication(True, False))

  the test is still green

* time for the next case

  .. code-block:: python

    def test_converse_implication(self):
        self.assertTrue(src.truth_table.converse_implication(True, True))
        self.assertTrue(src.truth_table.converse_implication(True, False))
        self.assertFalse(src.truth_table.converse_implication(False, True))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I add an `if statement`_

  .. code-block:: python

    def converse_implication(p, q):
        if not p and q:
            return False
        return True

  the test passes

* I add another case

  .. code-block:: python

    def test_converse_implication(self):
        self.assertTrue(src.truth_table.converse_implication(True, True))
        self.assertTrue(src.truth_table.converse_implication(True, False))
        self.assertFalse(src.truth_table.converse_implication(False, True))
        self.assertTrue(src.truth_table.converse_implication(False, False))

  the terminal_ still shows green

* I add a `return statement`_

  .. code-block:: python

    def converse_implication(p, q):
        return not (not p and q)
        if not p and q:
            return False
        return True

  I "multiply not_" by the symbols in the parentheses

  .. code-block:: python

    def converse_implication(p, q):
        return not not p not and not q
        return not (not p and q)

  the terminal_ shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  I change "not_ and_" to "or_" to be correct

  .. code-block:: python

    def converse_implication(p, q):
        return not not p or not q
        return not (not p and q)

  back to green. I remove "not_ not_" since it cancels out, the negation of a negation is the original thing

  .. code-block:: python

    def converse_implication(p, q):
        return p or not q
        return not (not p and q)

  all the tests are still green. I remove the other statements

  .. code-block:: python

    def converse_implication(p, q):
        return p or not q

----

*********************************************************************************
review
*********************************************************************************

Binary Operations take 2 inputs, each of which could be :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`, if we name the first input ``p`` and the second one ``q``, the tests show that

* :ref:`Converse Implication <test_converse_implication>` returns ``p or not q``
* :ref:`Project First <test_project_first>` always returns ``p``
* :ref:`Material NonImplication <test_material_non_implication>` returns ``p and not q``
* :ref:`Exclusive Disjunction <test_exclusive_disjunction>` returns ``p != q``
* :ref:`Logical Disjunction <test_logical_disjunction>` returns ``p or q``
* :ref:`Tautology <test_tautology>` always returns :ref:`True<test_what_is_true>`
* :ref:`Logical NAND <test_logical_nand>` returns ``not (p and q)``
* :ref:`Negate First<test_negate_first>` always returns ``not p``
* :ref:`Converse NonImplication <test_converse_non_implication>` returns ``not p and q``
* :ref:`Project Second <test_project_second>` always returns ``q``
* :ref:`Logical Conjunction <test_logical_conjunction>` returns ``p and q``
* :ref:`Contradiction <test_contradiction>` always returns :ref:`False<test_what_is_false>`

do you want to :ref:`test more binary operations? <binary_operations_iv>`

----

:ref:`truth table: tests and solutions`

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">Click Here to leave a 5 star review on TrustPilot, if you found this helpful</a>
  </div>
  <!-- End TrustBox widget -->