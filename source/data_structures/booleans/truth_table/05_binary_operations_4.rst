.. meta::
  :description: Master Python truth tables by implementing binary operations like negation, NOR, and material implication. Learn to code these logical functions step-by-step. Watch the full tutorial.
  :keywords: Jacob Itegboje, python truth table for binary operations, how to implement logical NOR in python, python material implication explained, python truth table for loop, python logical operations tutorial, truth table for negation in python, python binary operations tutorial, how to create a truth table in python with multiple inputs

.. include:: ../../../links.rst

.. _binary_operations_iv:

#################################################################################
truth table: Binary Operations part 4
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/5nyHcOL4BMc?si=_O84cSTjCaqLcWry" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

*********************************************************************************
requirements
*********************************************************************************

:ref:`Binary Operations part 3<truth table: Binary Operations part 3>`

----

*********************************************************************************
test_negate_second
*********************************************************************************

red: make it fail
#################################################################################

I add a new test for another Binary Operation to ``test_truth_table.py

.. code-block:: python
  :lineno-start: 97
  :emphasize-lines: 3-4

          self.assertTrue(src.truth_table.converse_implication(False, False))

      def test_negate_second(self):
          self.assertFalse(src.truth_table.negate_second(True, True))

  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'negate_second'

green: make it pass
#################################################################################

I add a :ref:`function<functions>` definition for it to ``truth_table.py``

.. code-block:: python
  :lineno-start: 65
  :emphasize-lines: 5-6

  def converse_implication(p, q):
      return p or not q


  def negate_second(p, q):
      return False

the test passes

refactor: make it better
#################################################################################

* I add the next case to ``test_negate_second`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 99
    :emphasize-lines: 3

        def test_negate_second(self):
            self.assertFalse(src.truth_table.negate_second(True, True))
            self.assertTrue(src.truth_table.negate_second(True, False))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

* I add an `if statement`_ to ``negate_second`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 2-3

    def negate_second(p, q):
        if p and not q:
            return True
        return False

  the test passes

* I add the third case to ``test_negate_second`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 99
    :emphasize-lines: 4

        def test_negate_second(self):
            self.assertFalse(src.truth_table.negate_second(True, True))
            self.assertTrue(src.truth_table.negate_second(True, False))
            self.assertFalse(src.truth_table.negate_second(False, True))

  the test is still passing

* I add another case

  .. code-block:: python
    :lineno-start: 99
    :emphasize-lines: 5

        def test_negate_second(self):
            self.assertFalse(src.truth_table.negate_second(True, True))
            self.assertTrue(src.truth_table.negate_second(True, False))
            self.assertFalse(src.truth_table.negate_second(False, True))
            self.assertTrue(src.truth_table.negate_second(False, False))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

* I add an `if statement`_ for the case to ``negate_second`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 2-3

    def negate_second(p, q):
        if not p and not q:
            return True
        if p and not q:
            return True
        return False

  the test is green again

* the ``negate_second`` :ref:`function<functions>` returns :ref:`True<test_what_is_true>` in the two cases where ``q`` is :ref:`False<test_what_is_false>`, I add a `return statement`_ to show this

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 2

    def negate_second(p, q):
        return not q
        if not p and not q:
            return True
        if p and not q:
            return True
        return False

  the test is still green

* I remove the other statements

  .. code-block:: python
    :lineno-start: 69

    def negate_second(p, q):
        return not q

----

*********************************************************************************
test_logical_nor
*********************************************************************************

red: make it fail
#################################################################################

I add a test for another Binary Operation in ``test_truth_table.py``

.. code-block:: python
  :lineno-start: 103
  :emphasize-lines: 3-4

          self.assertTrue(src.truth_table.negate_second(False, False))

      def test_logical_nor(self):
          self.assertFalse(src.truth_table.logical_nor(True, True))


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: python
  :force:

  AttributeError: module 'src.truth_table' has no attribute 'logical_nor'. Did you mean: 'logical_nand'?

green: make it pass
#################################################################################

I add a :ref:`function<functions>` for ``logical_nor`` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 69
  :emphasize-lines: 5-6

  def negate_second(p, q):
      return not q


  def logical_nor(p, q):
      return False

the test passes

refactor: make it better
#################################################################################

* I add the next case to ``test_logical_nor`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 105
    :emphasize-lines: 3

        def test_logical_nor(self):
            self.assertFalse(src.truth_table.logical_nor(True, True))
            self.assertFalse(src.truth_table.logical_nor(True, False))

  the terminal_ still shows green

* on to the next case

  .. code-block:: python
    :lineno-start: 105
    :emphasize-lines: 4

        def test_logical_nor(self):
            self.assertFalse(src.truth_table.logical_nor(True, True))
            self.assertFalse(src.truth_table.logical_nor(True, False))
            self.assertFalse(src.truth_table.logical_nor(False, True))

  the test is still green

* I add the last case

  .. code-block:: python
    :lineno-start: 105
    :emphasize-lines: 5

        def test_logical_nor(self):
            self.assertFalse(src.truth_table.logical_nor(True, True))
            self.assertFalse(src.truth_table.logical_nor(True, False))
            self.assertFalse(src.truth_table.logical_nor(False, True))
            self.assertTrue(src.truth_table.logical_nor(False, False))


    # Exceptions Encountered

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  this is the only case that returns :ref:`True<test_what_is_true>`. I add a `return statement`_ for it

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 2

        def logical_nor(p, q):
            return not p and not q
            return False

  the test passes

* I factor out "not_" since it happens 2 times

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 2

    def logical_nor(p, q):
        return not p not or not q
        return not p and not q

  the terminal_ shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

* I comment out the line then add the correct statement

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 2-3

    def logical_nor(p, q):
        return not (p or q)
        # return not p not or not q
        return not p and not q

  still green

* I remove the other statements

  .. code-block:: python
    :lineno-start: 73

    def logical_nor(p, q):
        return not (p or q)

----

*********************************************************************************
test_logical_equality
*********************************************************************************

red: make it fail
#################################################################################

I add a new test for the next Binary Operation to ``test_truth_table.py``

.. code-block:: python
  :lineno-start: 109
  :emphasize-lines: 3-4

          self.assertTrue(src.truth_table.logical_nor(False, False))

      def test_logical_equality(self):
          self.assertTrue(src.truth_table.logical_equality(True, True))


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: python
  :force:

  AttributeError: module 'src.truth_table' has no attribute 'logical_equality'. Did you mean: 'logical_identity'?

green: make it pass
#################################################################################

I add a :ref:`function<functions>` definition for it in ``truth_table.py``

.. code-block:: python
  :lineno-start: 73
  :emphasize-lines: 5-6

  def logical_nor(p, q):
      return not (p or q)


  def logical_equality(p, q):
      return True

the test passes

refactor: make it better
#################################################################################

* I add the next case to ``test_logical_equality`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 111
    :emphasize-lines: 3

        def test_logical_equality(self):
            self.assertTrue(src.truth_table.logical_equality(True, True))
            self.assertFalse(src.truth_table.logical_equality(True, False))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

* I add an `if statement`_ to ``logical_equality`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 2-3

    def logical_equality(p, q):
        if p and not q:
            return False
        return True

  the test passes

* I add another case to ``test_logical_equality`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 111
    :emphasize-lines: 4

        def test_logical_equality(self):
            self.assertTrue(src.truth_table.logical_equality(True, True))
            self.assertFalse(src.truth_table.logical_equality(True, False))
            self.assertFalse(src.truth_table.logical_equality(False, True))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

* I add another `if statement`_ to ``logical_equality`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 2-3

    def logical_equality(p, q):
        if not p and q:
            return False
        if p and not q:
            return False
        return True

  the test passes

* I add the last case ``test_logical_equality`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 111
    :emphasize-lines: 5

        def test_logical_equality(self):
            self.assertTrue(src.truth_table.logical_equality(True, True))
            self.assertFalse(src.truth_table.logical_equality(True, False))
            self.assertFalse(src.truth_table.logical_equality(False, True))
            self.assertTrue(src.truth_table.logical_equality(False, False))


    # Exceptions Encountered

  the test is still green

* I use "or_" to put the 2 statements that return :ref:`False<test_what_is_false>` together, since they are at the same level

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 2-3

    def logical_equality(p, q):
        if (not p and q) or (p and not q):
            return False
        if not p and q:
            return False
        if p and not q:
            return False
        return True

  still green

* I remove the other `if statements`_

  .. code-block:: python
    :lineno-start: 77

    def logical_equality(p, q):
        if (not p and q) or (p and not q):
            return False
        return True

  the test is still passing

* I write a new `return statement`_ with not_ to replace the `if statement`_

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 2

    def logical_equality(p, q):
        return not ((not p and q) or (p and not q))
        if (not p and q) or (p and not q):
            return False
        return True

  the test is still green

* I "multiply not_" by every symbol in the parentheses

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 2

    def logical_equality(p, q):
        return (not not p not and not q) not or (not p not and not not q)
        return not ((not p and q) or (p and not q):)

  the terminal_ shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  I change "not_ and_" to "or_" in both parentheses and "not_ or_" to "and_" in between them

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 2

    def logical_equality(p, q):
        return (not not p or not q) and (not p or not not q)
        return not ((not p and q) or (p and not q))

  the test is green again

* I remove "not_ not_" from both parentheses

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 2

    def logical_equality(p, q):
        return (p or not q) and (not p or q)
        return not ((not p and q) or (p and not q))

  still green

* I remove the second `return statement`_

  .. code-block:: python
    :lineno-start: 77

    def logical_equality(p, q):
        return (p or not q) and (not p or q)

  the test is still passing

* The 2 cases that return :ref:`True<test_what_is_true>` are when ``p`` and ``q`` are the same, which means I can write an even simpler `return statement`_

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 2

    def logical_equality(p, q):
        return p == q
        return (p or not q) and (not p or q)

  the test is still green

----

*********************************************************************************
test_material_implication
*********************************************************************************

red: make it fail
#################################################################################

I add a new test for another Binary Operation to ``test_truth_table.py``

.. code-block:: python
  :lineno-start: 115
  :emphasize-lines: 3-4

          self.assertTrue(src.truth_table.logical_equality(False, False))

      def test_material_implication(self):
          self.assertTrue(src.truth_table.material_implication(True, True))


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: python
  :force:

  AttributeError: module 'src.truth_table' has no attribute 'material_implication'

green: make it pass
#################################################################################

I add a :ref:`method<functions>` for ``material_implication`` in ``truth_table.py``

.. code-block:: python
  :lineno-start: 77
  :emphasize-lines: 6-7

  def logical_equality(p, q):
      return p == q
      return (p or not q) and (not p or q)


  def material_implication(p, q):
      return True

the test passes

refactor: make it better
#################################################################################

* I add the next case to ``test_material_implication`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 117
    :emphasize-lines: 3

        def test_material_implication(self):
            self.assertTrue(src.truth_table.material_implication(True, True))
            self.assertFalse(src.truth_table.material_implication(True, False))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

* I add an `if statement`_ for the case in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 2-3

    def material_implication(p, q):
        if p and not q:
            return False
        return True

  the terminal_ shows green

* I add the next case to ``test_material_implication`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 117
    :emphasize-lines: 4

        def test_material_implication(self):
            self.assertTrue(src.truth_table.material_implication(True, True))
            self.assertFalse(src.truth_table.material_implication(True, False))
            self.assertTrue(src.truth_table.material_implication(False, True))

  the test is still green

* I add the fourth case

  .. code-block:: python
    :lineno-start: 117
    :emphasize-lines: 5

        def test_material_implication(self):
            self.assertTrue(src.truth_table.material_implication(True, True))
            self.assertFalse(src.truth_table.material_implication(True, False))
            self.assertTrue(src.truth_table.material_implication(False, True))
            self.assertTrue(src.truth_table.material_implication(False, False))

    # Exceptions Encountered

  the test is still passing

* there is only one case where ``material_implication`` returns :ref:`False<test_what_is_false>`, I add a `return statement`_ for it in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 2

    def material_implication(p, q):
        return not (p and not q)
        if p and not q:
            return False
        return True

  the test is still green

* I "multiply not_" by the symbols in the parentheses

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 2

    def material_implication(p, q):
        return not p not and not not q
        return not (p and not q)

  the terminal_ shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

* I change "not_ and_" to "or_"

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 2

    def material_implication(p, q):
        return not p or not not q
        return not (p and not q)

  the test is green again

* I remove "not_ not_"

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 2

    def material_implication(p, q):
        return not p or q
        return not (p and not q)

  the test is still passing

* I remove the other statement

  .. code-block:: python
    :lineno-start: 82

    def material_implication(p, q):
        return not p or q

----

*********************************************************************************
review
*********************************************************************************

Binary Operations take 2 inputs, each input can be :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`, if we name the first input ``p`` and the second one ``q``, the tests show that

* :ref:`Material Implication  <test_material_implication>` returns ``not p or q``
* :ref:`Logical Equality <test_logical_equality>` returns ``p == q``
* :ref:`Logical NOR <test_logical_nor>` returns ``not (p or q)``
* :ref:`Negate Second <test_negate_second>` always returns ``not q``
*  :ref:`Converse Implication <test_converse_implication>` returns ``p or not q``
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

and

* :ref:`Logical Disjunction <test_logical_disjunction>` is "or_"
* :ref:`Logical Conjunction <test_logical_conjunction>` is "and_"
* :ref:`Logical Negation <test_logical_negation>` is "not_"

Would you like to :ref:`test the truth table tests?<test_truth_table_tests>`

----

:ref:`truth table: tests and solutions`

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">Click Here to leave a 5 star review on TrustPilot, if you found this helpful</a>
  </div>
  <!-- End TrustBox widget -->