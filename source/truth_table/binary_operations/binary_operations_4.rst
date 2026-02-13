.. meta::
  :description: Master Python truth tables by implementing binary operations like negation, NOR, and material implication. Learn to code these logical functions step-by-step. Watch the full tutorial.
  :keywords: Jacob Itegboje, python truth table for binary operations, how to implement logical NOR in python, python material implication explained, python truth table for loop, python logical operations tutorial, truth table for negation in python, python binary operations tutorial, how to create a truth table in python with multiple inputs

.. include:: ../../links.rst

.. _binary_operations_4:

#################################################################################
truth table: Binary Operations 4
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/5nyHcOL4BMc?si=_O84cSTjCaqLcWry" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

*********************************************************************************
requirements
*********************************************************************************

:ref:`Binary Operations 3<truth table: Binary Operations 3>`

----

*********************************************************************************
preview
*********************************************************************************

Here are the tests I have at the end of this chapter

.. literalinclude:: ../../code/truth_table/tests/test_binary.py
  :language: python
  :linenos:

----

*********************************************************************************
continue the project
*********************************************************************************

* Make sure you are in the ``pumping_python`` folder_ with pwd_ in the terminal_

  .. code-block:: shell
    :emphasize-lines: 1

    pwd

  if the terminal_ shows anything other than

  .. code-block:: shell

    .../pumping_python

  `change directory`_ to the ``pumping_python`` folder

* Once in ``pumping_python``, `change directory`_ to the project

  .. code-block:: shell
    :emphasize-lines: 1

    cd truth_table

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/truth_table

* I run the tests with `pytest-watcher`_

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 7

    ======================= test session starts ========================
    platform ____ -- Python 3.X.Y, pytest-A.B.C, pluggy-D.E.F
    rootdir: .../pumping_python/truth_table
    configfile: pyproject.toml
    collected 16 items

    tests/test_binary.py ................                         [ 66%]
    tests/test_nullary_unary.py ....                              [100%]

    ======================== 16 passed in G.HIs ========================

----

*********************************************************************************
test_negate_second
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test with the first case for another Binary Operation - when the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`, to ``test_truth_table.py``

.. code-block:: python
  :lineno-start: 127
  :emphasize-lines: 7-8

      def test_converse_implication(self):
          self.assertTrue(src.truth_table.converse_implication(True, True))
          self.assertTrue(src.truth_table.converse_implication(True, False))
          self.assertFalse(src.truth_table.converse_implication(False, True))
          self.assertTrue(src.truth_table.converse_implication(False, False))

      def test_negate_second(self):
          self.assertFalse(src.truth_table.negate_second(True, True))


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'negate_second'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a :ref:`function<what is a function?>` for :ref:`negate_second<test_negate_second>` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 69
  :emphasize-lines: 5-6

  def converse_implication(first_input, second_input):
      return first_input or not second_input


  def negate_second(first_input, second_input):
      return False

the test passes. :ref:`negate_second<test_negate_second>` returns :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the next case - when the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`, to :ref:`test_negate_second` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 127
    :emphasize-lines: 3

        def test_negate_second(self):
            self.assertFalse(src.truth_table.negate_second(True, True))
            self.assertTrue(src.truth_table.negate_second(True, False))

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

* I add an :ref:`if statement<if statements>` to :ref:`negate_second<test_negate_second>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 2-3

    def negate_second(first_input, second_input):
        if first_input == True and second_input == False:
            return True
        return False

  the test passes. :ref:`negate_second<test_negate_second>` returns

  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`
  - the :ref:`logical negation<test_logical_negation>` of the second input

* I add the third case - when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`, to :ref:`test_negate_second` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 127
    :emphasize-lines: 4

        def test_negate_second(self):
            self.assertFalse(src.truth_table.negate_second(True, True))
            self.assertTrue(src.truth_table.negate_second(True, False))
            self.assertFalse(src.truth_table.negate_second(False, True))

  the test is still green. :ref:`negate_second<test_negate_second>` returns

  - :ref:`False<test_what_is_false>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - the :ref:`logical negation<test_logical_negation>` of the second input in all 3 cases

* I add the last case - when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 127
    :emphasize-lines: 5

        def test_negate_second(self):
            self.assertFalse(src.truth_table.negate_second(True, True))
            self.assertTrue(src.truth_table.negate_second(True, False))
            self.assertFalse(src.truth_table.negate_second(False, True))
            self.assertTrue(src.truth_table.negate_second(False, False))

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

* I add an :ref:`if statement<if statements>` for the case to :ref:`negate_second<test_negate_second>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 2-3

    def negate_second(first_input, second_input):
        if first_input == False and second_input == False:
            return True
        if first_input == True and second_input == False:
            return True
        return False

  the test passes. :ref:`negate_second<test_negate_second>` returns

  - :ref:`True<test_what_is_true>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`False<test_what_is_false>`
  - the :ref:`logical negation<test_logical_negation>` of the second input in all 4 cases

* I add a `return statement`_ to show that :ref:`negate_second<test_negate_second>` always returns the :ref:`opposite<test_logical_negation>` of the second input

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 2

    def negate_second(first_input, second_input):
        return not second_input
        if first_input == False and second_input == False:
            return True
        if first_input == True and second_input == False:
            return True
        return False

  the test is still green

* I remove the other statements in the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 73

    def negate_second(first_input, second_input):
        return not second_input

:ref:`Negate Second<test_negate_second>` always returns

* ``not second_input``
* the :ref:`Logical Negation<test_logical_negation>` of the second input

It is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Project Second<test_project_second>` which always returns the second input

----

*********************************************************************************
test_logical_nor
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for :ref:`logical_nor<test_logical_nor>` in ``test_truth_table.py``

.. code-block:: python
  :lineno-start: 127
  :emphasize-lines: 7-8

      def test_negate_second(self):
          self.assertFalse(src.truth_table.negate_second(True, True))
          self.assertTrue(src.truth_table.negate_second(True, False))
          self.assertFalse(src.truth_table.negate_second(False, True))
          self.assertTrue(src.truth_table.negate_second(False, False))

      def test_logical_nor(self):
          self.assertFalse(src.truth_table.logical_nor(True, True))


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'logical_nor'. Did you mean: 'logical_nand'?

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add the :ref:`function<what is a function?>` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 73
  :emphasize-lines: 5-6

  def negate_second(first_input, second_input):
      return not second_input


  def logical_nor(first_input, second_input):
      return False

the test passes. :ref:`logical_nor<test_logical_nor>` returns :ref:`False<test_what_is_false>`, if the first and second inputs are both :ref:`True<test_what_is_true>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the second case - when the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`, to :ref:`test_logical_nor` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 3

        def test_logical_nor(self):
            self.assertFalse(src.truth_table.logical_nor(True, True))
            self.assertFalse(src.truth_table.logical_nor(True, False))

  the test is still green. :ref:`logical_nor<test_logical_nor>` returns

  - :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>`

* on to the next case - when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 4

        def test_logical_nor(self):
            self.assertFalse(src.truth_table.logical_nor(True, True))
            self.assertFalse(src.truth_table.logical_nor(True, False))
            self.assertFalse(src.truth_table.logical_nor(False, True))

  the test is still green. :ref:`logical_nor<test_logical_nor>` returns

  - :ref:`False<test_what_is_false>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>`

* I add the last case - when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 5

        def test_logical_nor(self):
            self.assertFalse(src.truth_table.logical_nor(True, True))
            self.assertFalse(src.truth_table.logical_nor(True, False))
            self.assertFalse(src.truth_table.logical_nor(False, True))
            self.assertTrue(src.truth_table.logical_nor(False, False))


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

* I add an :ref:`if statement<if statements>` for this case in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 2-3

    def logical_nor(first_input, second_input):
        if first_input == False and second_input == False:
            return True
        return False

  the test passes. :ref:`logical_nor<test_logical_nor>` returns

  - :ref:`True<test_what_is_true>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>`

* I make the :ref:`if statement<if statements>` simpler

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 2-3

    def logical_nor(first_input, second_input):
        # if first_input == False and second_input == False:
        if not first_input and not second_input:
            return True
        return False

  the test is still green

* since ``if something: return True`` is the same as ``return something``, I use a :ref:`conditional expression<conditional expressions>` for the :ref:`if statement<if statements>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 2

    def logical_nor(first_input, second_input):
        return not first_input and not second_input
        if not first_input and not second_input:
            return True
        return False

  still green

* I remove the other statements then factor out ":ref:`not<test_logical_negation>`" because it happens 2 times

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 2

    def logical_nor(first_input, second_input):
        return (not first_input) (not or) (not second_input)
        return not first_input and not second_input

  the terminal_ shows SyntaxError_

  .. code-block:: shell

    SyntaxError: invalid syntax

* I add the correct statement

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 2-3

    def logical_nor(first_input, second_input):
        # return (not first_input) (not or) (not second_input)
        return not (first_input or second_input)
        return not first_input and not second_input

  green, green, green again 🎶

* I remove the other statements in the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 77

    def logical_nor(first_input, second_input):
        return not (first_input or second_input)

:ref:`Logical NOR<test_logical_nor>` returns

* ``not (first_input or second_input)``
* :ref:`True<test_what_is_true>` if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`False<test_what_is_false>`
* the :ref:`Logical Negation<test_logical_negation>` of the :ref:`Logical Disjunction (or)<test_logical_disjunction>` of the first input and second input
* :ref:`not<test_logical_negation>` :ref:`or<test_logical_disjunction>` of the first input and second input

----

*********************************************************************************
test_logical_equality
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test for the next Binary Operation in ``test_truth_table.py``

.. code-block:: python
  :lineno-start: 133
  :emphasize-lines: 7-8

      def test_logical_nor(self):
          self.assertFalse(src.truth_table.logical_nor(True, True))
          self.assertFalse(src.truth_table.logical_nor(True, False))
          self.assertFalse(src.truth_table.logical_nor(False, True))
          self.assertTrue(src.truth_table.logical_nor(False, False))

      def test_logical_equality(self):
          self.assertTrue(src.truth_table.logical_equality(True, True))


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'logical_equality'. Did you mean: 'logical_identity'?

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a :ref:`function<what is a function?>` for it in ``truth_table.py``

.. code-block:: python
  :lineno-start: 77
  :emphasize-lines: 5-6

  def logical_nor(first_input, second_input):
      return not (first_input or second_input)


  def logical_equality(first_input, second_input):
      return True

the test passes. :ref:`logical_equality<test_logical_equality>` returns :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the next case to :ref:`test_logical_equality` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 139
    :emphasize-lines: 3

        def test_logical_equality(self):
            self.assertTrue(src.truth_table.logical_equality(True, True))
            self.assertFalse(src.truth_table.logical_equality(True, False))

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

* I add an :ref:`if statement<if statements>` to :ref:`logical_equality<test_logical_equality>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 2-3

    def logical_equality(first_input, second_input):
        if first_input and not second_input:
            return False
        return True

  the test passes. :ref:`logical_equality<test_logical_equality>` returns

  - :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`
  - the second input, if the first input is :ref:`True<test_what_is_true>

* I add the next case to :ref:`test_logical_equality` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 139
    :emphasize-lines: 4

        def test_logical_equality(self):
            self.assertTrue(src.truth_table.logical_equality(True, True))
            self.assertFalse(src.truth_table.logical_equality(True, False))
            self.assertFalse(src.truth_table.logical_equality(False, True))

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

* I add another :ref:`if statement<if statements>` to :ref:`logical_equality<test_logical_equality>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 2-3

    def logical_equality(first_input, second_input):
        if not first_input and second_input:
            return False
        if first_input and not second_input:
            return False
        return True

  the test passes. :ref:`logical_equality<test_logical_equality>` returns

  - :ref:`False<test_what_is_false>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`
  - the second input, if the first input is :ref:`True<test_what_is_true>`

* I add the last case to :ref:`test_logical_equality` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 139
    :emphasize-lines: 5

        def test_logical_equality(self):
            self.assertTrue(src.truth_table.logical_equality(True, True))
            self.assertFalse(src.truth_table.logical_equality(True, False))
            self.assertFalse(src.truth_table.logical_equality(False, True))
            self.assertTrue(src.truth_table.logical_equality(False, False))


    # Exceptions seen

  the test is still green. :ref:`logical_equality<test_logical_equality>` returns

  - :ref:`True<test_what_is_true>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - the :ref:`logical_negation<test_logical_negation>` of the second input if the first input is :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`
  - the second input, if the first input is :ref:`True<test_what_is_true>`
  - :ref:`True<test_what_is_true>`, if the two inputs are the same
  - :ref:`False<test_what_is_false>`, if the two inputs are NOT the same

* I use ":ref:`or<test_logical_disjunction>`" to put the 2 statements that return :ref:`False<test_what_is_false>` together, since they are at the same level in :ref:`logical_equality<test_logical_equality>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 2-11

    def logical_equality(first_input, second_input):
        # if not first_input and second_input:
        #     return False
        # if first_input and not second_input:
        #     return False
        if (
            (not first_input and second_input)
            or
            (first_input and not second_input)
        ):
            return False
        return True

  still green

* since ``if something: return False`` is the same as ``return not (something)``, I remove the commented lines and use a :ref:`conditional expression<conditional expressions>` with :ref:`not<test_logical_negation>`

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 2-6

    def logical_equality(first_input, second_input):
        return not (
            (not first_input and second_input)
            or
            (first_input and not second_input)
        )
        if (
            (not first_input and second_input)
            or
            (first_input and not second_input)
        ):
            return False
        return True

  greennn, yellow?

* I remove the other statements in the :ref:`function<what is a function?>` then "multiply :ref:`not<test_logical_negation>`" by everything in the parentheses

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 2-6

    def logical_equality(first_input, second_input):
        return (
            (not (not first_input and second_input))
            (not or)
            (not (first_input and not second_input))
        )
        return not (
            (not first_input and second_input)
            or
            (first_input and not second_input)
        )

  the terminal_ shows SyntaxError_

  .. code-block:: shell

    SyntaxError: invalid syntax

* I change ":ref:`not<test_logical_negation>` :ref:`or<test_logical_disjunction>`" to ":ref:`and<test_logical_conjunction>`"

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 4

    def logical_equality(first_input, second_input):
        return (
            (not (not first_input and second_input))
            and
            (not (first_input and not second_input))
        )
        return not (
            (not first_input and second_input)
            or
            (first_input and not second_input)
        )

  green again

* I remove the other `return statement`_ then "multiply" " :ref:`not<test_logical_negation>` in the first parentheses

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 3-4

    def logical_equality(first_input, second_input):
        return (
            # (not (not first_input and second_input))
            ((not not first_input) (not and) (not second_input))
            and
            (not (first_input and not second_input))
        )

  the terminal_ shows SyntaxError_

  .. code-block:: shell

    SyntaxError: invalid syntax

* I change ":ref:`not<test_logical_negation>` :ref:`and<test_logical_conjunction>`" to ":ref:`or<test_logical_disjunction>`"

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 4

    def logical_equality(first_input, second_input):
        return (
            # (not (not first_input and second_input))
            ((not not first_input) or (not second_input))
            and
            (not (first_input and not second_input))
        )

  the test is green again

* I remove the commented line and "multiply" :ref:`not<test_logical_negation>` in the next statement

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 5-6

    def logical_equality(first_input, second_input):
        return (
            ((not not first_input) or (not second_input))
            and
            # (not (first_input and not second_input))
            ((not first_input) (not and) (not not second_input))
        )

  the terminal_ shows SyntaxError_

  .. code-block:: shell

    SyntaxError: invalid syntax

* I change ":ref:`not<test_logical_negation>` :ref:`and<test_logical_conjunction>`" to ":ref:`or<test_logical_disjunction>`"

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 5

    def logical_equality(first_input, second_input):
        return (
            ((not not first_input) or (not second_input))
            and
            # (not (first_input and not second_input))
            ((not first_input) or (not not second_input))
        )

  green again

* I remove the commented line and ``not not`` from both parentheses because they cancel out

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 3, 5

    def logical_equality(first_input, second_input):
        return (
            (first_input or not second_input)
            and
            (not first_input or second_input)
        )

  the test is still green

* :ref:`logical_equality<test_logical_equality>` returns :ref:`True<test_what_is_true>`, if the first input and second input are the same, which means I can write a much simpler `return statement`_ thanks to the equality (``==``) symbol (2 equal signs together :kbd:`=+=`)

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 2

    def logical_equality(first_input, second_input):
        return first_input == second_input
        return (
            (first_input or not second_input)
            and
            (not first_input or second_input)
        )

  the test is still green

:ref:`Logical Equality<test_logical_equality>` returns

* ``first_input == second_input``
* :ref:`True<test_what_is_true>` when the first input is equal to the second input
* the :ref:`Logical Conjunction<test_logical_conjunction>` of the result of the :ref:`Logical Disjunction<test_logical_disjunction>` of the first input and the :ref:`Logical Negation<test_logical_negation>` of the second input, and the result of the :ref:`Logical Disjunction<test_logical_disjunction>` of the :ref:`Logical Negation<test_logical_negation>` of the first input, and the second input. Oh brother!
* is the :ref:`opposite<test_logical_negation>` of :ref:`Exclusive Disjunction<test_logical_disjunction>` which returns :ref:`True<test_what_is_false>`, only if the first input and second input are NOT equal

----

*********************************************************************************
test_material_implication
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test for one more Binary Operation in ``test_truth_table.py``

.. code-block:: python
  :lineno-start: 139
  :emphasize-lines: 7-8

      def test_logical_equality(self):
          self.assertTrue(src.truth_table.logical_equality(True, True))
          self.assertFalse(src.truth_table.logical_equality(True, False))
          self.assertFalse(src.truth_table.logical_equality(False, True))
          self.assertTrue(src.truth_table.logical_equality(False, False))

      def test_material_implication(self):
          self.assertTrue(src.truth_table.material_implication(True, True))


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'material_implication'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a :ref:`function<what is a function?>` for :ref:`material_implication<test_material_implication>` in ``truth_table.py``

.. code-block:: python
  :lineno-start: 81
  :emphasize-lines: 10-11

  def logical_equality(first_input, second_input):
      return first_input == second_input
      return (
          (first_input or not second_input)
          and
          (not first_input or second_input)
      )


  def material_implication(first_input, second_input):
      return True

the test passes. :ref:`material_implication<test_material_implication>` returns :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the next case to :ref:`test_material_implication` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 145
    :emphasize-lines: 3

        def test_material_implication(self):
            self.assertTrue(src.truth_table.material_implication(True, True))
            self.assertFalse(src.truth_table.material_implication(True, False))

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

* I add an :ref:`if statement<if statements>` to :ref:`material_implication<test_material_implication>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 2-3

    def material_implication(first_input, second_input):
        if first_input and not second_input:
            return False
        return True

  the test passes. :ref:`material_implication<test_material_implication>` returns

  - :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`
  - the second input in these 2 cases

* I add the next case to :ref:`test_material_implication` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 145
    :emphasize-lines: 4

        def test_material_implication(self):
            self.assertTrue(src.truth_table.material_implication(True, True))
            self.assertFalse(src.truth_table.material_implication(True, False))
            self.assertTrue(src.truth_table.material_implication(False, True))

  the test is still green. :ref:`material_implication<test_material_implication>` returns

  - :ref:`True<test_what_is_true>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`
  - returns the second input in all 3 cases

* I add the fourth case

  .. code-block:: python
    :lineno-start: 145
    :emphasize-lines: 5

        def test_material_implication(self):
            self.assertTrue(src.truth_table.material_implication(True, True))
            self.assertFalse(src.truth_table.material_implication(True, False))
            self.assertTrue(src.truth_table.material_implication(False, True))
            self.assertTrue(src.truth_table.material_implication(False, False))


    # Exceptions seen

  the test is still green. :ref:`material_implication<test_material_implication>` returns

  - :ref:`True<test_what_is_true>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>` - this is the only case where it returns :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`

* since ``if something: return False`` is the same as ``return not (something)``, I add a `return statement`_ for the :ref:`if statement<if statements>` in :ref:`material_implication<test_material_implication>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 2

    def material_implication(first_input, second_input):
        return not (first_input and not second_input)
        if first_input and not second_input:
            return False
        return True

  the test is still green

* I remove the other statements in the :ref:`function<what is a function?>` then "multiply :ref:`not<test_logical_negation>`" by the symbols in the parentheses

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 2

    def material_implication(first_input, second_input):
        return (not first_input) (not and) (not not second_input)
        return not (first_input and not second_input)

  the terminal_ shows SyntaxError_

  .. code-block:: shell

    SyntaxError: invalid syntax

* I change ":ref:`not<test_logical_negation>` :ref:`and<test_logical_conjunction>`" to ":ref:`or<test_logical_disjunction>`"

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 2

    def material_implication(first_input, second_input):
        return (not first_input) or (not not second_input)
        return not (first_input and not second_input)

  the test is green again

* I remove ``not not``

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 2

    def material_implication(first_input, second_input):
        return not first_input or second_input
        return (not first_input) or (not not second_input)

  still green

* I remove the other statement

  .. code-block:: python
    :lineno-start: 90

    def material_implication(first_input, second_input):
        return not first_input or second_input

:ref:`Material Implication also known as Logical Implication<test_material_implication>` returns

* ``not first_input or second_input``
* the :ref:`Logical Disjunction<test_logical_disjunction>` of the :ref:`Logical Negation<test_logical_negation>` of the first input, and the second input
* :ref:`False<test_what_is_false>` only if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`

it is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Material NonImplication<test_material_non_implication>` which returns :ref:`True<test_what_is_true>` only if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`

----

*********************************************************************************
more about Logical Equality
*********************************************************************************

----

``return ((first_input or not second_input) and (not first_input or second_input))`` can be thought of as

.. code-block:: python

  return x or y

* if ``x`` is ``first_input or not second_input``
* if ``y`` is ``not first_input or second_input``

:ref:`Exclusive Disjunction<test_exclusive_disjunction>` can also be thought of as

.. code-block:: python

  return (
      converse_implication(first_input, second_input)
      and
      material_implication(first_input, second_input)
  )

because

* :ref:`converse_implication<test_converse_implication>` returns ``first_input or not second_input``
* :ref:`material_implication<test_material_implication>` return ``not first_input or second_input``

This means that in the 4 cases

* if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`, :ref:`logical_equality<test_logical_equality>` returns

  .. code-block:: python
    :emphasize-lines: 5

    (first_input or not second_input) and (not first_input or second_input)
    (True        or not True        ) and (not True        or True        )
    (True        or False           ) and (False           or True        )
     True                             and  True
     True                             # logical_conjunction(True, True)

* if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`, :ref:`logical_equality<test_logical_equality>` returns

  .. code-block:: python
    :emphasize-lines: 5
    :force:

    (first_input or not second_input) and (not first_input or second_input)
    (True        or not False       ) and (not True        or False       )
    (True        or True            ) and (False           or False       )
     True                             and  False
     False                            # logical_conjunction(True, False)

* if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`, :ref:`logical_equality<test_logical_equality>` returns

  .. code-block:: python
    :emphasize-lines: 5

    (first_input or not second_input) and (not first_input or second_input)
    (False       or not True        ) and (not False       or True        )
    (False       or False           ) and (True            or True        )
     False                            and  True
     False                            # logical_conjunction(False, True)

* if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`False<test_what_is_false>`, :ref:`logical_equality<test_logical_equality>` returns

  .. code-block:: python
    :emphasize-lines: 5

    (first_input or not second_input) and (not first_input or second_input)
    (False       or not False       ) and (not False       or False       )
    (False       or True            ) and (True            or False       )
     True                             and  True
     True                             # logical_conjunction(True, True)

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_truth_table.py`` and ``truth_table.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_ and use :kbd:`q` on the keyboard to leave the tests and the terminal_ goes back to the command line

* I `change directory`_ to the parent of ``truth_table``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_

----

*********************************************************************************
review
*********************************************************************************

Binary Operations take 2 inputs, each input can be :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`, if I name the first input ``first_input`` and the second one ``second_input``, the tests show that

* :ref:`Material/Logical Implication<test_material_implication>`

  - returns ``not first_input or second_input``
  - returns :ref:`False<test_what_is_false>` only if ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Material NonImplication<test_material_non_implication>` which returns :ref:`True<test_what_is_true>` only if ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`

* :ref:`Logical Equality<test_logical_equality>`

  - returns ``first_input == second_input``
  - returns :ref:`True<test_what_is_true>` only if ``first_input`` and ``second_input`` are equal
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Exclusive Disjunction (Exclusive OR)<test_exclusive_disjunction>` which returns :ref:`True<test_what_is_true>` only if ``first_input`` and ``second_input`` are NOT equal

* :ref:`Logical NOR<test_logical_nor>`

  - returns ``not (first_input or second_input)``
  - returns :ref:`True<test_what_is_true>` only if ``first_input`` is :ref:`False<test_what_is_False>` and ``second_input`` is :ref:`False<test_what_is_false>`
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Logical Disjunction<test_logical_disjunction>` which returns :ref:`False<test_what_is_false>` only if ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`False<test_what_is_false>`

* :ref:`Negate Second<test_negate_second>`

  - always returns ``not second_input``
  - returns :ref:`True<test_what_is_true>` only if ``second_input`` is :ref:`False<test_what_is_false>`
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Project Second<test_project_second>` which returns :ref:`True<test_what_is_true>` only if ``second_input`` is :ref:`True<test_what_is_true>`

* :ref:`Converse Implication<test_converse_implication>`

  - returns ``first_input or not second_input``
  - returns :ref:`False<test_what_is_false>` if ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Converse NonImplication<test_converse_non_implication>` which returns :ref:`True<test_what_is_true>` only if ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`

* :ref:`Project First<test_project_first>`

  - always returns ``first_input``
  - returns :ref:`True<test_what_is_true>` only if ``first_input`` is :ref:`True<test_what_is_true>`
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Negate First<test_negate_first>` which returns :ref:`True<test_what_is_true>` only if ``first_input`` is :ref:`False<test_what_is_false>`

* :ref:`Material NonImplication<test_material_non_implication>`

  - returns ``first_input and not second_input``
  - returns :ref:`True<test_what_is_true>` only if ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Material/Logical Implication<test_material_implication>` which returns :ref:`False<test_what_is_false>` only if ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`

* :ref:`Exclusive Disjunction<test_exclusive_disjunction>`

  - returns ``first_input != second_input``
  - returns :ref:`True<test_what_is_true>` only if ``first_input`` and ``second_input`` are NOT equal
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Logical Equality<test_logical_equality>` which returns :ref:`True<test_what_is_true>` only if ``first_input`` and ``second_input`` are equal

* :ref:`Logical Disjunction<test_logical_disjunction>`

  - returns ``first_input or second_input``
  - returns :ref:`False<test_what_is_false>` only if ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`False<test_what_is_false>`
  - is the  :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Logical NOR<test_logical_nor>` which returns :ref:`True<test_what_is_true>` only if ``first_input`` is :ref:`False<test_what_is_False>` and ``second_input`` is :ref:`False<test_what_is_false>`

* :ref:`Tautology<test_tautology>`

  - always returns :ref:`True<test_what_is_true>`
  - never returns :ref:`False<test_what_is_false>`
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`contradiction<test_contradiction>`  which always returns :ref:`False<test_what_is_false>`

* :ref:`Logical NAND<test_logical_nand>`

  - returns ``not (first_input and second_input)``
  - returns :ref:`False<test_what_is_false>` only if ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`True<test_what_is_true>`
  - is the :ref:`opposite (Logical Negation) (not)<test_logical_negation>` of :ref:`Logical Conjunction (and)<test_logical_conjunction>` which returns :ref:`True<test_what_is_true>` only if ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`True<test_what_is_true>`

* :ref:`Negate First<test_negate_first>`

  - always returns ``not first_input``
  - returns :ref:`True<test_what_is_true>` only if ``first_input`` is :ref:`False<test_what_is_false>`
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Project First<test_project_first>` which returns :ref:`True<test_what_is_true>` only if ``first_input`` is :ref:`True<test_what_is_true>`

* :ref:`Converse NonImplication<test_converse_non_implication>`

  - returns ``not first_input and second_input``
  - returns :ref:`True<test_what_is_true>` only if ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Converse Implication<test_converse_implication>` which returns :ref:`False<test_what_is_false>` if ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`

* :ref:`Project Second<test_project_second>`

  - always returns ``second_input``
  - returns :ref:`True<test_what_is_true>` only if ``second_input`` is :ref:`True<test_what_is_true>`
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Negate Second<test_negate_second>` which returns :ref:`True<test_what_is_true>` only if ``second_input`` is :ref:`False<test_what_is_false>`

* :ref:`Logical Conjunction<test_logical_conjunction>` returns

  - returns ``first_input and second_input``
  - returns :ref:`True<test_what_is_true>` only if ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`True<test_what_is_true>`
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Logical NAND<test_logical_nand>` which returns :ref:`False<test_what_is_false>` only if ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`True<test_what_is_true>`

* :ref:`Contradiction<test_contradiction>`

  - always returns :ref:`False<test_what_is_false>`
  - never returns :ref:`True<test_what_is_true>`
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Tautology<test_tautology>` which always returns :ref:`True<test_what_is_true>`

and

* :ref:`Logical Disjunction is "or"<test_logical_disjunction>`
* :ref:`Logical Conjunction is "and"<test_logical_conjunction>`
* :ref:`Logical Negation is "not" <test_logical_negation>`

All the logic statements or conditions have been written with some or all of the above 3.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed for the Truth Table?<truth table: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

:ref:`Would you like to test the truth table tests?<test_truth_table_tests>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->