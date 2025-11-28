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

RED: make it fail
#################################################################################

I add a new test to ``test_truth_table.py``

.. code-block:: python
  :lineno-start: 73
  :emphasize-lines: 3-4

          self.assertFalse(src.truth_table.logical_disjunction(False, False))

      def test_exclusive_disjunction(self):
          self.assertFalse(src.truth_table.exclusive_disjunction(True, True))


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'exclusive_disjunction'

GREEN: make it pass
#################################################################################

I add the :ref:`function<functions>` for ``exclusive_disjunction`` in ``truth_table.py``

.. code-block:: python
  :lineno-start: 45
  :emphasize-lines: 5-6

  def logical_disjunction(input_1, input_2):
      return input_1 or input_2


  def exclusive_disjunction(input_1, input_2):
      return False

the test passes

REFACTOR: make it better
#################################################################################

* I add the next case to ``test_exclusive_disjunction`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 3

        def test_exclusive_disjunction(self):
            self.assertFalse(src.truth_table.exclusive_disjunction(True, True))
            self.assertTrue(src.truth_table.exclusive_disjunction(True, False))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: False is not true

* I add an `if statement`_ to ``exclusive_disjunction`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2-3

    def exclusive_disjunction(input_1, input_2):
        if input_1 and not q:
            return True
        return False

  the test is green again

* I add the third case to ``test_exclusive_disjunction`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 4

        def test_exclusive_disjunction(self):
            self.assertFalse(src.truth_table.exclusive_disjunction(True, True))
            self.assertTrue(src.truth_table.exclusive_disjunction(True, False))
            self.assertTrue(src.truth_table.exclusive_disjunction(False, True))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: False is not true

* I add another `if statement`_ to ``exclusive_disjunction`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2-3

    def exclusive_disjunction(input_1, input_2):
        if not input_1 and input_2:
            return True
        if input_1 and not q:
            return True
        return False

  the test passes

* I add the last case to ``test_exclusive_disjunction`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 5

        def test_exclusive_disjunction(self):
            self.assertFalse(src.truth_table.exclusive_disjunction(True, True))
            self.assertTrue(src.truth_table.exclusive_disjunction(True, False))
            self.assertTrue(src.truth_table.exclusive_disjunction(False, True))
            self.assertFalse(src.truth_table.exclusive_disjunction(False, False))


    # Exceptions Encountered

  the test is still green

* I can use :ref:`Logical Disjunction<test_logical_disjunction>` to put the two `if statements`_ that return :ref:`True<test_what_is_true>` together

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2-3

    def exclusive_disjunction(input_1, input_2):
        if (not input_1 and input_2) or (input_1 and not input_2):
            return True
        if not input_1 and input_2:
            return True
        if input_1 and not q:
            return True
        return False

  the test is still green

* I remove the other `if statements`_

  .. code-block:: python
    :lineno-start: 49

    def exclusive_disjunction(input_1, input_2):
        if (not input_1 and input_2) or (input_1 and not input_2):
            return True
        return False

  still green

* I use a simple `return statement`_

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2

    def exclusive_disjunction(input_1, input_2):
        return (not input_1 and input_2) or (input_1 and not input_2)
        if (not input_1 and input_2) or (input_1 and not input_2):
            return True
        return False

  the terminal_ still shows green

* I remove the other statements

  .. code-block:: python
    :lineno-start: 49

    def exclusive_disjunction(input_1, input_2):
        return (not input_1 and input_2) or (input_1 and not input_2)

  still green

* This :ref:`function<functions>` returns :ref:`False<test_what_is_false>` in the 2 cases where ``p`` and ``q`` are the same. I add an `if statement`_ to show this

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2-5

    def exclusive_disjunction(input_1, input_2):
        if input_1 == q:
            return False
        else:
            return True
        return (not input_1 and input_2) or (input_1 and not input_2)

* I change it to a simple `return statement`_

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2

    def exclusive_disjunction(input_1, input_2):
        return not input_1 == input_2
        if input_1 == q:
            return False
        else:
            return True
        return (not input_1 and input_2) or (input_1 and not input_2)

  the test is still green

* I use an even simpler `return statement`_

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2

    def exclusive_disjunction(input_1, input_2):
        return input_1 != input_2
        return not input_1 == input_2
        return (not input_1 and input_2) or (input_1 and not input_2)

  the terminal_ still shows green. ``!=`` is the symbol for NOT equal

----

*********************************************************************************
test_material_non_implication
*********************************************************************************

RED: make it fail
#################################################################################

I add another test to ``test_truth_table.py``

.. code-block:: python
  :lineno-start: 79
  :emphasize-lines: 3-4

          self.assertFalse(src.truth_table.exclusive_disjunction(False, False))

      def test_material_non_implication(self):
          self.assertFalse(src.truth_table.material_non_implication(True, True))


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'material_non_implication'. Did you mean: 'converse_non_implication'?

GREEN: make it pass
#################################################################################

I add a :ref:`function<functions>` for ``material_non_implication`` in ``truth_table.py``

.. code-block:: python
  :lineno-start: 49
  :emphasize-lines: 7-8

  def exclusive_disjunction(input_1, input_2):
      return input_1 != input_2
      return not input_1 == input_2
      return (not input_1 and input_2) or (input_1 and not input_2)


  def material_non_implication(input_1, input_2):
      return False

the test passes

REFACTOR: make it better
#################################################################################

* I add another case to ``test_material_non_implication`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 3

        def test_material_non_implication(self):
            self.assertFalse(src.truth_table.material_non_implication(True, True))
            self.assertTrue(src.truth_table.material_non_implication(True, False))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: False is not true

* I add an `if statement`_ to ``material_non_implication`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 2-3

    def material_non_implication(input_1, input_2):
        if input_1 and not q:
            return True
        return False

  the test passes

* I add the next case in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 4

        def test_material_non_implication(self):
            self.assertFalse(src.truth_table.material_non_implication(True, True))
            self.assertTrue(src.truth_table.material_non_implication(True, False))
            self.assertFalse(src.truth_table.material_non_implication(False, True))

  the test is still green

* I add the fourth case

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 5

        def test_material_non_implication(self):
            self.assertFalse(src.truth_table.material_non_implication(True, True))
            self.assertTrue(src.truth_table.material_non_implication(True, False))
            self.assertFalse(src.truth_table.material_non_implication(False, True))
            self.assertFalse(src.truth_table.material_non_implication(False, False))


    # Exceptions Encountered

  the terminal_ still shows green

* there is only one case where ``material_non_implication`` returns :ref:`True<test_what_is_true>`, I add a `return statement`_ for it in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 2

    def material_non_implication(input_1, input_2):
        return input_1 and not input_2
        if input_1 and not q:
            return True
        return False

  the test is still green

* I remove the other statements

  .. code-block:: python
    :lineno-start: 55

    def material_non_implication(input_1, input_2):
        return input_1 and not input_2

----

*********************************************************************************
test_project_first
*********************************************************************************

RED: make it fail
#################################################################################

I add a new test for the next Binary Operation in ``test_truth_table.py``

.. code-block:: python
  :lineno-start: 85
  :emphasize-lines: 3-4

          self.assertFalse(src.truth_table.material_non_implication(False, False))

      def test_project_first(self):
          self.assertTrue(src.truth_table.project_first(True, True))


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'project_first'

GREEN: make it pass
#################################################################################

I add a :ref:`function<functions>` definition for ``project_first`` in ``truth_table.py``

.. code-block:: python
  :lineno-start: 55
  :emphasize-lines: 5-6

  def material_non_implication(input_1, input_2):
      return input_1 and not input_2


  def project_first(input_1, input_2):
      return True

the test passes

REFACTOR: make it better
#################################################################################

* I add the second case to ``test_project_first`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 87
    :emphasize-lines: 3

        def test_project_first(self):
            self.assertTrue(src.truth_table.project_first(True, True))
            self.assertTrue(src.truth_table.project_first(True, False))

  the test is still green

* on to the next case

  .. code-block:: python
    :lineno-start: 87
    :emphasize-lines: 4

        def test_project_first(self):
            self.assertTrue(src.truth_table.project_first(True, True))
            self.assertTrue(src.truth_table.project_first(True, False))
            self.assertFalse(src.truth_table.project_first(False, True))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: True is not false

* I add an `if statement`_ for this case to ``project_first`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 2-3

    def project_first(input_1, input_2):
        if not input_1 and input_2:
            return False
        return True

  the test passes

* I add the last case to ``test_project_first`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 87
    :emphasize-lines: 5

        def test_project_first(self):
            self.assertTrue(src.truth_table.project_first(True, True))
            self.assertTrue(src.truth_table.project_first(True, False))
            self.assertFalse(src.truth_table.project_first(False, True))
            self.assertFalse(src.truth_table.project_first(False, False))


    # Exceptions Encountered

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: True is not false

* I add another `if statement`_ to ``project_first`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 2-3

    def project_first(input_1, input_2):
        if not input_1 and not input_2:
            return False
        if not input_1 and input_2:
            return False
        return True

  the test passes

* I add a `return statement`_ to show that this :ref:`function<functions>` returns the same value as ``p`` in every case

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 2

    def project_first(input_1, input_2):
        return input_1
        if not input_1 and not input_2:
            return False
        if not input_1 and input_2:
            return False
        return True

  the terminal_ still shows green

* I remove the other statements

  .. code-block:: python
    :lineno-start: 59

    def project_first(input_1, input_2):
        return input_1

----

*********************************************************************************
test_converse_implication
*********************************************************************************

RED: make it fail
#################################################################################

I add a new test to ``test_truth_table.py``

.. code-block:: python
  :lineno-start: 91
  :emphasize-lines: 3-4

          self.assertFalse(src.truth_table.project_first(False, False))

      def test_converse_implication(self):
          self.assertTrue(src.truth_table.converse_implication(True, True))


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'converse_implication'. Did you mean: 'converse_non_implication'?

GREEN: make it pass
#################################################################################

I add a :ref:`function<functions>` definition for ``converse_implication`` in ``truth_table.py``

.. code-block:: python
  :lineno-start: 59
  :emphasize-lines: 5-6

  def project_first(input_1, input_2):
      return input_1


  def converse_implication(input_1, input_2):
      return True

the test passes

REFACTOR: make it better
#################################################################################

* I add the second case to ``test_converse_implication`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 3

        def test_converse_implication(self):
            self.assertTrue(src.truth_table.converse_implication(True, True))
            self.assertTrue(src.truth_table.converse_implication(True, False))

  the test is still green

* time for the next case

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 4

        def test_converse_implication(self):
            self.assertTrue(src.truth_table.converse_implication(True, True))
            self.assertTrue(src.truth_table.converse_implication(True, False))
            self.assertFalse(src.truth_table.converse_implication(False, True))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: True is not false

* I add an `if statement`_ to ``converse_implication`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 2-3

    def converse_implication(input_1, input_2):
        if not input_1 and input_2:
            return False
        return True

  the test passes

* I add another case to ``test_converse_implication`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 5

        def test_converse_implication(self):
            self.assertTrue(src.truth_table.converse_implication(True, True))
            self.assertTrue(src.truth_table.converse_implication(True, False))
            self.assertFalse(src.truth_table.converse_implication(False, True))
            self.assertTrue(src.truth_table.converse_implication(False, False))


    # Exceptions Encountered

  the terminal_ still shows green

* I add a `return statement`_ to replace the `if statement_` in ``converse_implication`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 2

    def converse_implication(input_1, input_2):
        return not (not input_1 and input_2)
        if not input_1 and input_2:
            return False
        return True

  the test is still green

* I "multiply not_" by the symbols in the parentheses

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 2

    def converse_implication(input_1, input_2):
        return not not input_1 not and not q
        return not (not input_1 and input_2)

  the terminal_ shows SyntaxError_

  .. code-block:: shell

    SyntaxError: invalid syntax

  I change "not_ and_" to "or_" to be correct

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 2

    def converse_implication(input_1, input_2):
        return not not input_1 or not input_2
        return not (not input_1 and input_2)

  back to green

* I remove "not_ not_" since it cancels out, the negation of a negation is the original thing

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 2

    def converse_implication(input_1, input_2):
        return input_1 or not input_2
        return not (not input_1 and input_2)

  the tests is still green

* I remove the other statements

  .. code-block:: python
    :lineno-start: 63

    def converse_implication(input_1, input_2):
        return input_1 or not input_2

----

*********************************************************************************
review
*********************************************************************************

Binary Operations take 2 inputs, each input can be :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`, if we name the first input ``p`` and the second one ``q``, the tests show that

* :ref:`Converse Implication <test_converse_implication>` returns ``input_1 or not input_2``
* :ref:`Project First <test_project_first>` always returns ``p``
* :ref:`Material NonImplication <test_material_non_implication>` returns ``input_1 and not input_2``
* :ref:`Exclusive Disjunction <test_exclusive_disjunction>` returns ``p != q``
* :ref:`Logical Disjunction <test_logical_disjunction>` returns ``input_1 or input_2``
* :ref:`Tautology <test_tautology>` always returns :ref:`True<test_what_is_true>`
* :ref:`Logical NAND <test_logical_nand>` returns ``not (input_1 and input_2)``
* :ref:`Negate First<test_negate_first>` always returns ``not p``
* :ref:`Converse NonImplication <test_converse_non_implication>` returns ``not input_1 and input_2``
* :ref:`Project Second <test_project_second>` always returns ``q``
* :ref:`Logical Conjunction <test_logical_conjunction>` returns ``input_1 and input_2``
* :ref:`Contradiction <test_contradiction>` always returns :ref:`False<test_what_is_false>`

and

* :ref:`Logical Disjunction <test_logical_disjunction>` is "or_"
* :ref:`Logical Conjunction <test_logical_conjunction>` is "and_"
* :ref:`Logical Negation <test_logical_negation>` is "not_"

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