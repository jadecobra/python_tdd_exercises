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

* run the tests with `pytest-watcher`_

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

----

*********************************************************************************
test_negate_second
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test for another Binary Operation to ``test_truth_table.py`` with the first case where both ``first_input`` and ``second_input`` are :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 97
  :emphasize-lines: 3-4

          self.assertTrue(src.truth_table.converse_implication(False, False))

      def test_negate_second(self):
          self.assertFalse(src.truth_table.negate_second(True, True))

  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'negate_second'

there is no definition for it yet

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a :ref:`function<what is a function?>` for ``negate_second`` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 63
  :emphasize-lines: 5-6

  def converse_implication(first_input, second_input):
      return first_input or not second_input


  def negate_second(first_input, second_input):
      return False

the test passes. ``negate_second`` returns :ref:`False<test_what_is_false>` when the two inputs are :ref:`True<test_what_is_true>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the next case - when ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`, to ``test_negate_second`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 99
    :emphasize-lines: 3

        def test_negate_second(self):
            self.assertFalse(src.truth_table.negate_second(True, True))
            self.assertTrue(src.truth_table.negate_second(True, False))

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

* I add an :ref:`if statement<if statements>` to ``negate_second`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 2-3

    def negate_second(first_input, second_input):
        if first_input == True and second_input == False:
            return True
        return False

  the test passes. ``negate_second`` returns

  - :ref:`True<test_what_is_true>` when the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>` when the two inputs are :ref:`True<test_what_is_true>`

* I add the third case - when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`, to ``test_negate_second`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 99
    :emphasize-lines: 4

        def test_negate_second(self):
            self.assertFalse(src.truth_table.negate_second(True, True))
            self.assertTrue(src.truth_table.negate_second(True, False))
            self.assertFalse(src.truth_table.negate_second(False, True))

  the test is still green. ``negate_second`` returns

  - :ref:`False<test_what_is_false>` when ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`
  - :ref:`True<test_what_is_true>` when ``first_input`` is :ref:`True<test_what_is_true>` and ``second _input`` is :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>` when both ``first_input`` and ``second_input`` are :ref:`True<test_what_is_true>`
  - :ref:`False<test_what_is_false>` when ``second_input`` is :ref:`True<test_what_is_true>`

* I add the last case - when the two inputs are :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 99
    :emphasize-lines: 5

        def test_negate_second(self):
            self.assertFalse(src.truth_table.negate_second(True, True))
            self.assertTrue(src.truth_table.negate_second(True, False))
            self.assertFalse(src.truth_table.negate_second(False, True))
            self.assertTrue(src.truth_table.negate_second(False, False))

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

* I add an :ref:`if statement<if statements>` for the case to ``negate_second`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 2-3

    def negate_second(first_input, second_input):
        if first_input == False and second_input == False:
            return True
        if first_input == True and second_input == False:
            return True
        return False

  the test passes. ``negate_second`` returns

  - :ref:`True<test_what_is_true>` when both the first input and second input are :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>` when the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>` when the second input is :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>` when the second input is :ref:`True<test_what_is_true>`

* I add a `return statement`_ to show that ``negate_second`` always returns the opposite of the second input

  .. code-block:: python
    :lineno-start: 67
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
    :lineno-start: 67

    def negate_second(first_input, second_input):
        return not second_input

:ref:`Negate Second<test_negate_second>` always returns

* ``not second_input``
* the :ref:`Logical Negation<test_logical_negation>` of the second input

it is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Project Second<test_project_second>` which always returns the second input

----

*********************************************************************************
test_logical_nor
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for ``logical_nor`` in ``test_truth_table.py``

.. code-block:: python
  :lineno-start: 103
  :emphasize-lines: 3-4

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
  :lineno-start: 67
  :emphasize-lines: 5-6

  def negate_second(first_input, second_input):
      return not second_input


  def logical_nor(first_input, second_input):
      return False

the test passes. ``logical_nor`` returns :ref:`False<test_what_is_false>` when the first and second inputs are both :ref:`True<test_what_is_true>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the next case to ``test_logical_nor`` in ``test_truth_table.py`` - when ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 105
    :emphasize-lines: 3

        def test_logical_nor(self):
            self.assertFalse(src.truth_table.logical_nor(True, True))
            self.assertFalse(src.truth_table.logical_nor(True, False))

  the test is still green. ``logical_nor`` returns

  - :ref:`False<test_what_is_false>` when the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>` when the first and second inputs are both :ref:`True<test_what_is_true>`
  - :ref:`False<test_what_is_false>` when the first input is :ref:`True<test_what_is_true>`

* on to the next case - when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 105
    :emphasize-lines: 4

        def test_logical_nor(self):
            self.assertFalse(src.truth_table.logical_nor(True, True))
            self.assertFalse(src.truth_table.logical_nor(True, False))
            self.assertFalse(src.truth_table.logical_nor(False, True))

  the test is still green. ``logical_nor`` returns

  - :ref:`False<test_what_is_false>` when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`False<test_what_is_false>` when the first input is :ref:`True<test_what_is_true>`

* I add the last case - when the two inputs are :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 105
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

  this is the only case where ``logical_nor`` returns :ref:`True<test_what_is_true>`

* I add a :ref:`conditional expression<conditional expressions>` for it in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 2

    def logical_nor(first_input, second_input):
        return True if (first_input == False and second_input == False) else False
        return False

  the test passes. ``logical_nor`` returns

  - :ref:`True<test_what_is_true>` when the two inputs are :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>` when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`False<test_what_is_false>` when the first input is :ref:`True<test_what_is_true>`

* I remove the second `return statement`_ then use the simpler form of the :ref:`conditional expression<conditional expressions>`

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 2

    def logical_nor(first_input, second_input):
        return first_input == False and second_input == False
        return True if (first_input == False and second_input == False) else False

  the test is still green

* I remove the second `return statement`_ and write the first one in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 2

    def logical_nor(first_input, second_input):
        return not first_input == True and not second_input == True
        return first_input == False and second_input == False

  still green

* I remove the second `return statement`_ and make the first one simpler with bool_

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 2

    def logical_nor(first_input, second_input):
        return not bool(first_input) and not bool(second_input)
        return not first_input == True and not second_input == True

  the test is still green

* I make the statement simpler again

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 2

    def logical_nor(first_input, second_input):
        return not first_input and not second_input
        return not bool(first_input) and not bool(second_input)

  green

* I remove the second `return statement`_ then factor out "not_" since it happens 2 times in the first statement

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 2

    def logical_nor(first_input, second_input):
        return (not first_input) (not or) (not second_input)
        return not first_input and not second_input

  the terminal_ shows SyntaxError_

  .. code-block:: shell

    SyntaxError: invalid syntax

* I comment out the line then add the correct statement

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 2-3

    def logical_nor(first_input, second_input):
        return not (first_input or second_input)
        # return (not first_input) (not or) (not second_input)
        return not first_input and not second_input

  green, green, green again

* I remove the other statements in the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 71

    def logical_nor(first_input, second_input):
        return not (first_input or second_input)

:ref:`Logical NOR<test_logical_nor>` returns

* ``not (first_input or second_input)``
* the :ref:`Logical Negation<test_logical_negation>` of the :ref:`Logical Disjunction (or)<test_logical_disjunction>` of the first input and second input
* not_ or_ of the first and second inputs
* :ref:`True<test_what_is_true>` when the two inputs are :ref:`False<test_what_is_false>`

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
  :lineno-start: 109
  :emphasize-lines: 3-4

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
  :lineno-start: 71
  :emphasize-lines: 5-6

  def logical_nor(first_input, second_input):
      return not (first_input or second_input)


  def logical_equality(first_input, second_input):
      return True

the test passes. ``logical_equality`` returns :ref:`True<test_what_is_true>` when the two inputs are :ref:`True<test_what_is_true>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the next case to ``test_logical_equality`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 111
    :emphasize-lines: 3

        def test_logical_equality(self):
            self.assertTrue(src.truth_table.logical_equality(True, True))
            self.assertFalse(src.truth_table.logical_equality(True, False))

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

* I add an :ref:`if statement<if statements>` to ``logical_equality`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 2-3

    def logical_equality(first_input, second_input):
        if first_input and not second_input:
            return False
        return True

  the test passes. ``logical_equality`` returns

  - :ref:`False<test_what_is_false>` when ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>` when the two inputs are :ref:`True<test_what_is_true>`

* I add the next case to ``test_logical_equality`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 111
    :emphasize-lines: 4

        def test_logical_equality(self):
            self.assertTrue(src.truth_table.logical_equality(True, True))
            self.assertFalse(src.truth_table.logical_equality(True, False))
            self.assertFalse(src.truth_table.logical_equality(False, True))

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

* I add another :ref:`if statement<if statements>` to ``logical_equality`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 2-3

    def logical_equality(first_input, second_input):
        if not first_input and second_input:
            return False
        if first_input and not second_input:
            return False
        return True

  the test passes. ``logical_equality`` returns

  - :ref:`False<test_what_is_false>` when ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`
  - :ref:`False<test_what_is_false>` when ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>` when the two inputs are :ref:`True<test_what_is_true>`

* I add the last case to ``test_logical_equality`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 111
    :emphasize-lines: 5

        def test_logical_equality(self):
            self.assertTrue(src.truth_table.logical_equality(True, True))
            self.assertFalse(src.truth_table.logical_equality(True, False))
            self.assertFalse(src.truth_table.logical_equality(False, True))
            self.assertTrue(src.truth_table.logical_equality(False, False))


    # Exceptions seen

  the test is still green. ``logical_equality`` returns

  - :ref:`True<test_what_is_true>` when the two inputs are :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>` when ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`
  - :ref:`False<test_what_is_false>` when ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>` when the two inputs are :ref:`True<test_what_is_true>`
  - :ref:`True<test_what_is_true>` when the two inputs are the same
  - :ref:`False<test_what_is_false>` when the two inputs are NOT the same

* I use "or_" to put the 2 statements that return :ref:`False<test_what_is_false>` together, since they are at the same level in ``logical_equality`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 2-3

    def logical_equality(first_input, second_input):
        if (not first_input and second_input) or (first_input and not second_input):
            return False
        # if not first_input and second_input:
        #     return False
        # if first_input and not second_input:
        #     return False
        return True

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 75

    def logical_equality(first_input, second_input):
        if (not first_input and second_input) or (first_input and not second_input):
            return False
        return True

  the test is still green

* I write a new `return statement`_ with not_ to replace the :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 2

    def logical_equality(first_input, second_input):
        return not ((not first_input and second_input) or (first_input and not second_input))
        if (not first_input and second_input) or (first_input and not second_input):
            return False
        return True

  the test is still green

* I remove the other statements in the :ref:`function<what is a function?>` then "multiply not_" by every symbol in the parentheses

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 2-6

    def logical_equality(first_input, second_input):
        return (
            (not (not first_input and second_input))
            (not or)
            (not (first_input and not second_input))
        )
        return not ((not first_input and second_input) or (first_input and not second_input))

  the terminal_ shows SyntaxError_

  .. code-block:: shell

    SyntaxError: invalid syntax

* I change "not_ or_" to "and_"

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 4

    def logical_equality(first_input, second_input):
        return (
            (not (not first_input and second_input))
            and
            (not (first_input and not second_input))
        )
        return not ((not first_input and second_input) or (first_input and not second_input))

  the test is green again

* I remove the other `return statement`_ then "multiply" " not_ in the first parentheses

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 3

    def logical_equality(first_input, second_input):
        return (
            (not not first_input not and not second_input)
            # (not (not first_input and second_input))
            and
            (not (first_input and not second_input))
        )

  the terminal_ shows SyntaxError_

  .. code-block:: shell

    SyntaxError: invalid syntax

* I change "not_ and_" to "or_"

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 3

    def logical_equality(first_input, second_input):
        return (
            (not not first_input or not second_input)
            # (not (not first_input and second_input))
            and
            (not (first_input and not second_input))
        )

  green again

* I remove the commented line and "multiply" not_ in the next statement

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 5

    def logical_equality(first_input, second_input):
        return (
            (not not first_input or not second_input)
            and
            (not first_input not and not not second_input)
            # (not (first_input and not second_input))
        )

  the terminal_ shows SyntaxError_

  .. code-block:: shell

    SyntaxError: invalid syntax

* I change "not_ and_" to "or_"

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 5

    def logical_equality(first_input, second_input):
        return (
            (not not first_input or not second_input)
            and
            (not first_input or not not second_input)
            # (not (first_input and not second_input))
        )

  the test is green again

* I remove the commented line and the "not_ not_" from both parentheses since they cancel out

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 3, 5

    def logical_equality(first_input, second_input):
        return (
            (first_input or not second_input)
            and
            (not first_input or second_input)
        )

  still green

* The 2 cases where ``logical_equality`` returns :ref:`True<test_what_is_true>` are when ``first_input`` and ``second_input`` are the same, which means I can write a much simpler `return statement`_ thanks to the equality symbol (2 equal signs together :kbd:`=+=`)

  .. code-block:: python
    :lineno-start: 75
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
* :ref:`True<test_what_is_true>` when the two inputs are the same
* :ref:`False<test_what_is_false>` when the two inputs are NOT the same
* the :ref:`Logical Conjunction<test_logical_conjunction>` of the result of the :ref:`Logical Disjunction<test_logical_disjunction>` of the first input and the :ref:`Logical Negation<test_logical_negation>` of the second input, and the result of the :ref:`Logical Disjunction<test_logical_disjunction>` of the :ref:`Logical Negation<test_logical_negation>` of the first input and the second input
* is the opposite of :ref:`Exclusive Disjunction<test_logical_disjunction>` which returns :ref:`False<test_what_is_false>` when the two inputs are the same

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
  :lineno-start: 115
  :emphasize-lines: 3-4

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

I add a :ref:`method<what is a function?>` for ``material_implication`` in ``truth_table.py``

.. code-block:: python
  :lineno-start: 75
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

the test passes. ``material_implication`` returns :ref:`True<test_what_is_true>` when the two inputs are :ref:`True<test_what_is_true>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the next case to ``test_material_implication`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 117
    :emphasize-lines: 3

        def test_material_implication(self):
            self.assertTrue(src.truth_table.material_implication(True, True))
            self.assertFalse(src.truth_table.material_implication(True, False))

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

* I add an :ref:`if statement<if statements>` to ``material_implication`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 2-3

    def material_implication(first_input, second_input):
        if first_input and not second_input:
            return False
        return True

  the test passes. ``material_implication`` returns

  - :ref:`False<test_what_is_false>` when the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>` when the two inputs are :ref:`True<test_what_is_true>`

* I add the next case to ``test_material_implication`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 117
    :emphasize-lines: 4

        def test_material_implication(self):
            self.assertTrue(src.truth_table.material_implication(True, True))
            self.assertFalse(src.truth_table.material_implication(True, False))
            self.assertTrue(src.truth_table.material_implication(False, True))

  the test is still green. ``material_implication`` returns

  - :ref:`True<test_what_is_true>` when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`False<test_what_is_false>` when the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>` when the two inputs are :ref:`True<test_what_is_true>`

* I add the fourth case

  .. code-block:: python
    :lineno-start: 117
    :emphasize-lines: 5

        def test_material_implication(self):
            self.assertTrue(src.truth_table.material_implication(True, True))
            self.assertFalse(src.truth_table.material_implication(True, False))
            self.assertTrue(src.truth_table.material_implication(False, True))
            self.assertTrue(src.truth_table.material_implication(False, False))

    # Exceptions seen

  the test is still green. ``material_implication`` returns

  - :ref:`True<test_what_is_true>` when the two inputs are :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>` when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`False<test_what_is_false>` when the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>` when the two inputs are :ref:`True<test_what_is_true>`

* there is only one case where ``material_implication`` returns :ref:`False<test_what_is_false>`, I add a `return statement`_ for it with :ref:`Logical Negation<test_logical_negation>` since the :ref:`if statement<if statements>` returns :ref:`False<test_what_is_false>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 2

    def material_implication(first_input, second_input):
        return not (first_input and not second_input)
        if first_input and not second_input:
            return False
        return True

  the test is still green

* I remove the other statements in the :ref:`function<what is a function?>` then "multiply not_" by the symbols in the parentheses

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 2

    def material_implication(first_input, second_input):
        return (not first_input) (not and) (not not second_input)
        return not (first_input and not second_input)

  the terminal_ shows SyntaxError_

  .. code-block:: shell

    SyntaxError: invalid syntax

* I change "not_ and_" to "or_"

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 2

    def material_implication(first_input, second_input):
        return (not first_input) or (not not second_input)
        return not (first_input and not second_input)

  the test is green again

* I remove "not_ not_"

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 2

    def material_implication(first_input, second_input):
        return not first_input or second_input
        return (not first_input) or (not not second_input)

  the test is still green

* I remove the other statement

  .. code-block:: python
    :lineno-start: 84

    def material_implication(first_input, second_input):
        return not first_input or second_input

:ref:`Material Implication also known as Logical Implication<test_material_implication>` returns

* ``not first_input or second_input``
* the :ref:`Logical Disjunction<test_logical_disjunction>` of the :ref:`Logical Negation<test_logical_negation>` of the first input, and the second input
* :ref:`False<test_what_is_false>` only when the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`

it is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Material NonImplication<test_material_non_implication>` which only returns :ref:`True<test_what_is_true>` when the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`

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

Binary Operations take 2 inputs, each input can be :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`, if we name the first input ``first_input`` and the second one ``second_input``, the tests show that

* :ref:`Material Implication  <test_material_implication>`

  - returns ``not first_input or second_input``
  - returns :ref:`False<test_what_is_false>` only if ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Material NonImplication<test_material_non_implication>` which returns :ref:`True<test_what_is_true>` only if ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`

* :ref:`Logical Equality <test_logical_equality>`

  - returns ``first_input == second_input``
  - returns :ref:`True<test_what_is_true>` only if ``first_input`` and ``second_input`` are equal
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Exclusive Disjunction (Exclusive OR)<test_exclusive_disjunction>` which returns :ref:`True<test_what_is_true>` only if ``first_input`` and ``second_input`` are NOT equal

* :ref:`Logical NOR <test_logical_nor>`

  - returns ``not (first_input or second_input)``
  - returns :ref:`True<test_what_is_true>` only if ``first_input`` is :ref:`False<test_what_is_False>` and ``second_input`` is :ref:`False<test_what_is_false>`
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Logical Disjunction<test_logical_disjunction>` which returns :ref:`False<test_what_is_false>` only if ``first_input`` is :ref:`False<test_what_is_False>` and ``second_input`` is :ref:`False<test_what_is_false>`

* :ref:`Negate Second <test_negate_second>`

  - always returns ``not second_input``
  - returns :ref:`True<test_what_is_true>` if ``second_input`` is :ref:`False<test_what_is_false>`
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Project Second<test_project_second>` which returns :ref:`True<test_what_is_true>` only if ``first_input`` is :ref:`True<test_what_is_true>`

* :ref:`Converse Implication <test_converse_implication>`

  - returns ``first_input or not second_input``
  - returns :ref:`False<test_what_is_false>` if ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Converse NonImplication<test_converse_non_implication>` which returns :ref:`True<test_what_is_true>` only if ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`

* :ref:`Project First <test_project_first>`

  - always returns ``first_input``
  - returns :ref:`True<test_what_is_true>` only if ``first_input`` is :ref:`True<test_what_is_true>`
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Negate First<test_negate_first>` which returns :ref:`True<test_what_is_true>` only if ``first_input`` is :ref:`False<test_what_is_false>`

* :ref:`Material NonImplication <test_material_non_implication>`

  - returns ``first_input and not second_input``
  - returns :ref:`True<test_what_is_true>` only if ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Material/Logical Implication<test_material_implication>` which returns :ref:`False<test_what_is_false>` only if ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`

* :ref:`Exclusive Disjunction <test_exclusive_disjunction>`

  - returns ``first_input != second_input``
  - returns :ref:`True<test_what_is_true>` only if ``first_input`` and ``second_input`` are NOT equal
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Logical Equality<test_logical_equality>` returns :ref:`True<test_what_is_true>` only if ``first_input`` and ``second_input`` are equal

* :ref:`Logical Disjunction <test_logical_disjunction>`

  - returns ``first_input or second_input``
  - returns :ref:`False<test_what_is_false>` only if ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`False<test_what_is_false>`
  - is the  :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Logical NOR<test_logical_nor>` which returns :ref:`True<test_what_is_true>` only if ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`False<test_what_is_false>`

* :ref:`Tautology <test_tautology>`

  - always returns :ref:`True<test_what_is_true>`
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`contradiction<test_contradiction>`  which always returns :ref:`False<test_what_is_false>`

* :ref:`Logical NAND <test_logical_nand>`

  - returns ``not (first_input and second_input)``
  - returns :ref:`False<test_what_is_false>` only if ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`True<test_what_is_true>`
  - is the :ref:`opposite (Logical Negation) (not)<test_logical_negation>` of :ref:`Logical Conjunction (and)<test_logical_conjunction>` which returns :ref:`True<test_what_is_true>` only if ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`True<test_what_is_true>`

* :ref:`Negate First<test_negate_first>`

  - always returns ``not first_input``
  - returns :ref:`True<test_what_is_true>` only if ``first_input`` is :ref:`False<test_what_is_false>`
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Project First<test_project_first>` which returns :ref:`True<test_what_is_true>` only if ``first_input`` is :ref:`True<test_what_is_true>`

* :ref:`Converse NonImplication <test_converse_non_implication>`

  - returns ``not first_input and second_input``
  - returns :ref:`True<test_what_is_true>` only if ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Converse Implication<test_converse_implication>` which returns :ref:`False<test_what_is_false>` if ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`

* :ref:`Project Second <test_project_second>`

  - always returns ``second_input``
  - returns :ref:`True<test_what_is_true>` only if ``second_input`` is :ref:`True<test_what_is_true>`
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Negate Second<test_negate_second>` which returns :ref:`True<test_what_is_true>` if ``second_input`` is :ref:`False<test_what_is_false>`

* :ref:`Logical Conjunction <test_logical_conjunction>` returns

  - returns ``first_input and second_input``
  - returns :ref:`True<test_what_is_true>` only if ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`True<test_what_is_true>`
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Logical NAND<test_logical_nand>` which returns :ref:`False<test_what_is_false>` only if ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`True<test_what_is_true>`

* :ref:`Contradiction <test_contradiction>`

  - always returns :ref:`False<test_what_is_false>`
  - it never returns :ref:`True<test_what_is_true>`
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