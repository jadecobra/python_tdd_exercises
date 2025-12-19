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

*********************************************************************************
how to get back to the automated tests
*********************************************************************************

If your tests stopped after the :ref:`previous chapter<truth table: Binary Operations part 3>`, heres's how to get back to the tests

* Make sure you are in the ``pumping_python`` folder_ with pwd_ in the terminal_

  .. code-block:: shell
    :emphasize-lines: 1

    pwd

  if the terminal_ shows anything other than

  .. code-block:: shell

    .../pumping_python

  you need to `change directory`_ to the ``pumping_python`` folder

* Once in the ``pumping_python`` directory_, `change directory`_ to the project

  .. code-block:: shell
    :emphasize-lines: 1

    cd truth_table

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/truth_table

* activate the `Virtual Environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    source .venv/bin/activate

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use ``.venv/scripts/activate.ps1`` instead of ``source .venv/bin/activate``

    .. code-block:: python
      :emphasize-lines: 1

      .venv/scripts/activate.ps1

  when the `Virtual Environment`_ is activated, the terminal_ shows

  .. code-block:: shell

    (.venv) .../pumping_python/truth_table

* run the tests

  .. code-block:: shell
    :emphasize-lines: 1

    pytest-watch

----

*********************************************************************************
test_negate_second
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a new test for another Binary Operation to ``test_truth_table.py`` with the first case where both ``first_input`` and ``second_input`` are :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 97
  :emphasize-lines: 3-4

          self.assertTrue(src.truth_table.converse_implication(False, False))

      def test_negate_second(self):
          self.assertFalse(src.truth_table.negate_second(True, True))

  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'negate_second'

there is no definition for it yet

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add a :ref:`function<functions>` definition for ``negate_second`` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 63
  :emphasize-lines: 5-6

  def converse_implication(first_input, second_input):
      return first_input or not second_input


  def negate_second(first_input, second_input):
      return False

the test passes. ``negate_second`` returns :ref:`False<test_what_is_false>` when the two inputs are :ref:`True<test_what_is_true>`

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add the next case - when ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`, to ``test_negate_second`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 99
    :emphasize-lines: 3

        def test_negate_second(self):
            self.assertFalse(src.truth_table.negate_second(True, True))
            self.assertTrue(src.truth_table.negate_second(True, False))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: False is not true

* I add an :ref:`if statement<if statements (conditionals)>` to ``negate_second`` in ``truth_table.py``

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

  the test is still passing. ``negate_second`` returns

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

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: False is not true

* I add an :ref:`if statement<if statements (conditionals)>` for the case to ``negate_second`` in ``truth_table.py``

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

* I remove the other statements

  .. code-block:: python
    :lineno-start: 67

    def negate_second(first_input, second_input):
        return not second_input

:ref:`Negate Second<test_negate_second>` always returns

* ``not second_input``
* the :ref:`Logical Negation<test_logical_negation>` of the second input

it is the opposite or :ref:`Logical Negation<test_logical_negation>` of :ref:`Project Second<test_project_second>` which always returns the second input

----

*********************************************************************************
test_logical_nor
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test for ``logical_nor`` in ``test_truth_table.py``

.. code-block:: python
  :lineno-start: 103
  :emphasize-lines: 3-4

          self.assertTrue(src.truth_table.negate_second(False, False))

      def test_logical_nor(self):
          self.assertFalse(src.truth_table.logical_nor(True, True))


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'logical_nor'. Did you mean: 'logical_nand'?

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add the :ref:`function<functions>` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 67
  :emphasize-lines: 5-6

  def negate_second(first_input, second_input):
      return not second_input


  def logical_nor(first_input, second_input):
      return False

the test passes. ``logical_nor`` returns :ref:`False<test_what_is_false>` when the first and second inputs are both :ref:`True<test_what_is_true>`

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add the next case to ``test_logical_nor`` in ``test_truth_table.py`` - when ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 105
    :emphasize-lines: 3

        def test_logical_nor(self):
            self.assertFalse(src.truth_table.logical_nor(True, True))
            self.assertFalse(src.truth_table.logical_nor(True, False))

  the terminal_ still shows green. ``logical_nor`` returns

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


    # Exceptions Encountered

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: False is not true

  this is the only case where ``logical_nor`` returns :ref:`True<test_what_is_true>`

* I add a `conditional expression`_ for it in ``truth_table.py``

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

* I remove the second `return statement`_ then use the simpler form of the `conditional expression`_

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

  the terminal_ still shows green

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

* I remove the other statements

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

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a new test for the next Binary Operation in ``test_truth_table.py``

.. code-block:: python
  :lineno-start: 109
  :emphasize-lines: 3-4

          self.assertTrue(src.truth_table.logical_nor(False, False))

      def test_logical_equality(self):
          self.assertTrue(src.truth_table.logical_equality(True, True))


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'logical_equality'. Did you mean: 'logical_identity'?

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add a :ref:`function<functions>` definition for it in ``truth_table.py``

.. code-block:: python
  :lineno-start: 71
  :emphasize-lines: 5-6

  def logical_nor(first_input, second_input):
      return not (first_input or second_input)


  def logical_equality(first_input, second_input):
      return True

the test passes. ``logical_equality`` returns :ref:`True<test_what_is_true>` when the two inputs are :ref:`True<test_what_is_true>`

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add the next case to ``test_logical_equality`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 111
    :emphasize-lines: 3

        def test_logical_equality(self):
            self.assertTrue(src.truth_table.logical_equality(True, True))
            self.assertFalse(src.truth_table.logical_equality(True, False))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: True is not false

* I add an :ref:`if statement<if statements (conditionals)>` to ``logical_equality`` in ``truth_table.py``

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

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: True is not false

* I add another :ref:`if statement<if statements (conditionals)>` to ``logical_equality`` in ``truth_table.py``

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


    # Exceptions Encountered

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

  the test is still passing

* I write a new `return statement`_ with not_ to replace the :ref:`if statement<if statements (conditionals)>`

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 2

    def logical_equality(first_input, second_input):
        return not ((not first_input and second_input) or (first_input and not second_input))
        if (not first_input and second_input) or (first_input and not second_input):
            return False
        return True

  the test is still green

* I remove the other statements then "multiply not_" by every symbol in the parentheses

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

  I change "not_ or_" to "and_"

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

  the terminal shows SyntaxError_

  .. code-block:: shell

    SyntaxError: invalid syntax

  I change "not_ and_" to "or_"

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

* The 2 cases where ``logical_equality`` returns :ref:`True<test_what_is_true>` are when ``first_input`` and ``second_input`` are the same, which means I can write a much simpler `return statement`_ thanks to the equality symbol

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
* the :ref:`Logical Conjunction<test_logical_conjunction>` of the result of :ref:`Logical Disjunction<test_logical_disjunction>` of the first input and the :ref:`Logical Negation<test_logical_negation>` of the second input, and the result of the :ref:`Logical Disjunction<test_logical_disjunction>` of the the :ref:`Logical Negation<test_logical_negation>` of the first input and the second input
* is the opposite of :ref:`Exclusive Disjunction<test_logical_disjunction>` which returns :ref:`False<test_what_is_false>` when the two inputs are the same

----

*********************************************************************************
test_material_implication
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a new test for one more Binary Operation in ``test_truth_table.py``

.. code-block:: python
  :lineno-start: 115
  :emphasize-lines: 3-4

          self.assertTrue(src.truth_table.logical_equality(False, False))

      def test_material_implication(self):
          self.assertTrue(src.truth_table.material_implication(True, True))


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'material_implication'

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add a :ref:`method<functions>` for ``material_implication`` in ``truth_table.py``

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

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add the next case to ``test_material_implication`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 117
    :emphasize-lines: 3

        def test_material_implication(self):
            self.assertTrue(src.truth_table.material_implication(True, True))
            self.assertFalse(src.truth_table.material_implication(True, False))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: True is not false

* I add an :ref:`if statement<if statements (conditionals)>` to ``material_implication`` in ``truth_table.py``

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

    # Exceptions Encountered

  the test is still passing. ``material_implication`` returns

  - :ref:`True<test_what_is_true>` when the two inputs are :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>` when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`False<test_what_is_false>` when the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>` when the two inputs are :ref:`True<test_what_is_true>`

* there is only one case where ``material_implication`` returns :ref:`False<test_what_is_false>`, I add a `return statement`_ for it with :ref:`Logical Negation<test_logical_negation>` since the :ref:`if statement<if statements (conditionals)>` returns :ref:`False<test_what_is_false>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 2

    def material_implication(first_input, second_input):
        return not (first_input and not second_input)
        if first_input and not second_input:
            return False
        return True

  the test is still green

* I remove the other statements then "multiply not_" by the symbols in the parentheses

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
    :lineno-start: 80
    :emphasize-lines: 2

    def material_implication(first_input, second_input):
        return not first_input or second_input
        return (not first_input) or (not not second_input)

  the test is still passing

* I remove the other statement

  .. code-block:: python
    :lineno-start: 80

    def material_implication(first_input, second_input):
        return not first_input or second_input

:ref:`Material Implication aka Logical Implication<test_material_implication>` returns

* ``not first_input or second_input``
* the :ref:`Logical Disjunction<test_logical_disjunction>` of the :ref:`Logical Negation<test_logical_negation>` of the first input, and the second input
* :ref:`False<test_what_is_false>` only when the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`

it is the :ref:`opposite or Logical Negation<test_logical_negation>` of :ref:`Material NonImplication<test_material_non_implication>` which only returns :ref:`True<test_what_is_true>` when the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`

----

*********************************************************************************
review
*********************************************************************************

Binary Operations take 2 inputs, each input can be :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`, if we name the first input ``first_input`` and the second one ``second_input``, the tests show that

* :ref:`Material Implication  <test_material_implication>`

  - returns ``not first_input or second_input``
  - returns :ref:`False<test_what_is_false>` when ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`
  - is the :ref:`opposite or Logical Negation<test_logical_negation>` of :ref:`Material NonImplication<test_material_non_implication>` which returns :ref:`True<test_what_is_true>` only when ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`

* :ref:`Logical Equality <test_logical_equality>`

  - returns ``first_input == second_input``
  - returns :ref:`True<test_what_is_true>` when ``first_input`` and ``second_input`` are equal
  - is the :ref:`opposite or Logical Negation<test_logical_negation>` of :ref:`Exclusive Disjunction (Exclusive OR)<test_exclusive_disjunction>` which only returns :ref:`True<test_what_is_true>` when the two inputs are NOT equal

* :ref:`Logical NOR <test_logical_nor>`

  - returns ``not (first_input or second_input)``
  - returns :ref:`True<test_what_is_true>` when ``first_input`` and ``second_input`` are both :ref:`False<test_what_is_false>`
  - is the :ref:`opposite or Logical Negation<test_logical_negation>` of :ref:`Logical Disjunction<test_logical_disjunction>` which only returns :ref:`False<test_what_is_false>` when the two inputs are :ref:`False<test_what_is_false>`

* :ref:`Negate Second <test_negate_second>`

  - returns ``not second_input``
  - returns :ref:`True<test_what_is_true>` when ``second_input`` is :ref:`True<test_what_is_true>`
  - is the :ref:`opposite or Logical Negation<test_logical_negation>` of :ref:`Project Second<test_project_second>` which only returns :ref:`True<test_what_is_true>` when ``second_input`` is :ref:`True<test_what_is_true>`

*  :ref:`Converse Implication <test_converse_implication>`

  - returns ``first_input or not second_input``
  - returns :ref:`False<test_what_is_false>` when ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`
  - is the :ref:`opposite or Logical Negation<test_logical_negation>` of :ref:`Converse NonImplication<test_converse_non_implication>` which only returns :ref:`True<test_what_is_true>` when ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`

* :ref:`Project First <test_project_first>`

  - returns ``first_input``
  - returns :ref:`True<test_what_is_true>` when ``first_input`` is :ref:`True<test_what_is_true>`
  - is the :ref:`opposite or Logical Negation<test_logical_negation>` of :ref:`Negate First<test_negate_first>` which only returns :ref:`True<test_what_is_true>` when ``first_input`` is :ref:`False<test_what_is_false>`

* :ref:`Material NonImplication <test_material_non_implication>`

  - returns ``first_input and not second_input``
  - returns :ref:`True<test_what_is_true>` when ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`
  - is the :ref:`opposite or Logical Negation<test_logical_negation>` of :ref:`Material or Logical Implication<test_material_implication>` which only returns :ref:`False<test_what_is_false>` when ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`

* :ref:`Exclusive Disjunction <test_exclusive_disjunction>`

  - returns ``first_input != second_input``
  - returns :ref:`True<test_what_is_true>` when ``first_input`` and ``second_input`` are NOT equal
  - is the :ref:`opposite or Logical Negation<test_logical_negation>` of :ref:`Logical Equality<test_logical_equality>` which only returns :ref:`True<test_what_is_true>` when the two inputs are equal

* :ref:`Logical Disjunction <test_logical_disjunction>`

  - returns ``first_input or second_input``
  - returns :ref:`True<test_what_is_true>` when ``first_input`` and ``second_input`` are both :ref:`False<test_what_is_false>`
  - is the  :ref:`opposite or Logical Negation<test_logical_negation>` of :ref:`Logical NOR<test_logical_nor>` which only returns :ref:`True<test_what_is_true>` when the two inputs are :ref:`False<test_what_is_false>`

* :ref:`Tautology <test_tautology>`

  - always returns :ref:`True<test_what_is_true>`
  - is the :ref:`opposite or Logical Negation<test_logical_negation>` of :ref:`Contradiction<test_contradiction>` which always returns :ref:`False<test_what_is_false>`

* :ref:`Logical NAND <test_logical_nand>`

  - returns ``not (first_input and second_input)``
  - returns :ref:`False<test_what_is_false>` when ``first_input`` and ``second_input`` are both :ref:`True<test_what_is_true>`
  - is the :ref:`opposite or Logical Negation (not)<test_logical_negation>` of :ref:`Logical Conjunction (and)<test_logical_conjunction>` which only returns :ref:`True<test_what_is_true>` when the two inputs are :ref:`True<test_what_is_true>`

* :ref:`Negate First<test_negate_first>`

  - returns ``not first_input``
  - returns :ref:`True<test_what_is_true>` when ``first_input`` is :ref:`False<test_what_is_false>`
  - is the :ref:`opposite or Logical Negation<test_logical_negation>` of :ref:`Project First<test_project_first>` which only returns :ref:`True<test_what_is_true>` when ``first_input`` is :ref:`True<test_what_is_true>`

* :ref:`Converse NonImplication <test_converse_non_implication>`

  - returns ``not first_input and second_input``
  - returns :ref:`True<test_what_is_true>` when ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<tets_What_is_true>`
  - is the :ref:`opposite or Logical Negation<test_logical_negation>` of :ref:`Converse Implication<test_converse_implication>` which only returns :ref:`False<test_what_is_false>` when ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`

* :ref:`Project Second <test_project_second>`

  - returns ``second_input``
  - returns :ref:`True<test_what_is_true>` when ``second_input`` is :ref:`True<test_what_is_true>`
  - is the :ref:`opposite or Logical Negation<test_logical_negation>` of :ref:`Negate Second<test_negate_second>` which only returns :ref:`True<test_what_is_true>` when ``second_input`` is :ref:`False<test_what_is_false>`

* :ref:`Logical Conjunction <test_logical_conjunction>` returns

  - returns ``first_input and second_input``
  - returns :ref:`True<test_what_is_true>` when ``first_input`` and ``second_input`` are :ref:`True<test_what_is_true>`
  - is the :ref:`opposite or Logical Negation<test_logical_negation>` of :ref:`Logical NAND<test_logical_nand>` which only returns :ref:`False<test_what_is_false>` when the two inputs are :ref:`True<test_what_is_true>`

* :ref:`Contradiction <test_contradiction>`

  - always returns :ref:`False<test_what_is_false>`
  - is the opposite or :ref:`Tautology<test_tautology>` which always returns :ref:`True<test_what_is_true>`

and

* :ref:`Logical Disjunction <test_logical_disjunction>` is "or_"
* :ref:`Logical Conjunction <test_logical_conjunction>` is "and_"
* :ref:`Logical Negation <test_logical_negation>` is "not_"

All the logic statements or conditions have been written with some or all of the above 3.

----

:ref:`Click Here for the code<truth table: tests and solutions>`

----

*********************************************************************************
what is next?
*********************************************************************************

Would you like to :ref:`test the truth table tests?<test_truth_table_tests>`

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">Click Here to leave a 5 star review on TrustPilot, if you found this helpful</a>
  </div>
  <!-- End TrustBox widget -->