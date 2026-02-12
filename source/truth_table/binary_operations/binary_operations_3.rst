.. meta::
  :description: Master Python's boolean logic. This clear, step-by-step guide explains AND, OR, and NOT operators with easy-to-follow truth tables. Build your first one now.
  :keywords: Jacob Itegboje, python truth table for beginners, boolean logic and or not first_inputython tutorial, how to make a truth table in python code, practical use of truth tables in programming, python logical operators explained for new programmers, understanding boolean expressions in python, python 'and' vs 'or' truth table differences, troubleshooting boolean logic in python script

.. include:: ../../links.rst

.. _binary_operations_3:

#################################################################################
truth table: Binary Operations 3
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/EaLR4MMiW4c?si=yok1ej79nisTRUBq" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

*********************************************************************************
requirements
*********************************************************************************

:ref:`Binary Operations 2<truth table: Binary Operations 2>`

----

*********************************************************************************
preview
*********************************************************************************

Here are the tests I have at the end of this chapter

.. literalinclude:: ../../code/truth_table/tests/test_binary_3.py
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

* the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 7

    ======================= test session starts ========================
    platform ____ -- Python 3.X.Y, pytest-A.B.C, pluggy-D.E.F
    rootdir: .../pumping_python/truth_table
    configfile: pyproject.toml
    collected 12 items

    tests/test_binary.py ........                                 [ 66%]
    tests/test_nullary_unary.py ....                              [100%]

    ======================== 12 passed in G.HIs ========================

* I hold :kbd:`ctrl` (Windows_) or :kbd:`option` (MacOS_) on the keyboard and click on ``tests/test_binary.py`` with the mouse to open it in the :ref:`editor<2 editors>`

----

*********************************************************************************
test_exclusive_disjunction
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test to ``test_binary.py``

.. code-block:: python
  :lineno-start: 82
  :emphasize-lines: 15-16

      def test_logical_disjunction(self):
          self.assertTrue(
              src.truth_table.logical_disjunction(True, True)
          )
          self.assertTrue(
              src.truth_table.logical_disjunction(True, False)
          )
          self.assertTrue(
              src.truth_table.logical_disjunction(False, True)
          )
          self.assertFalse(
              src.truth_table.logical_disjunction(False, False)
          )

      def test_exclusive_disjunction(self):
          self.assertFalse(src.truth_table.exclusive_disjunction(True, True))


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'exclusive_disjunction'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add :ref:`exclusive_disjunction<test_exclusive_disjunction>` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 47
  :emphasize-lines: 5-6

  def logical_disjunction(first_input, second_input):
      return first_input or second_input


  def exclusive_disjunction(first_input, second_input):
      return False

the test passes. :ref:`exclusive_disjunction<test_exclusive_disjunction>` returns :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the next case - where the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`, to :ref:`test_exclusive_disjunction` in ``test_binary.py``

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 3

        def test_exclusive_disjunction(self):
            self.assertFalse(src.truth_table.exclusive_disjunction(True, True))
            self.assertTrue(src.truth_table.exclusive_disjunction(True, False))

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

* I add :ref:`if statements` to :ref:`exclusive_disjunction<test_exclusive_disjunction>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 2-4

    def exclusive_disjunction(first_input, second_input):
        if first_input == True:
            if second_input == False:
                return True
        return False

  the test passes. :ref:`exclusive_disjunction<test_exclusive_disjunction>` returns

  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`

* I add the third case - where the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`, to ``test_binary.py``

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 4

        def test_exclusive_disjunction(self):
            self.assertFalse(src.truth_table.exclusive_disjunction(True, True))
            self.assertTrue(src.truth_table.exclusive_disjunction(True, False))
            self.assertTrue(src.truth_table.exclusive_disjunction(False, True))

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

* I add :ref:`if statements` to :ref:`exclusive_disjunction<test_exclusive_disjunction>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 2-4

    def exclusive_disjunction(first_input, second_input):
        if first_input == False:
            if second_input == True:
                return True
        if first_input == True:
            if second_input == False:
                return True
        return False

  the test passes. :ref:`exclusive_disjunction<test_exclusive_disjunction>` returns

  - :ref:`True<test_what_is_true>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`

* I add the last case - when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>` to :ref:`test_exclusive_disjunction`, in ``test_binary.py``

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 5

        def test_exclusive_disjunction(self):
            self.assertFalse(src.truth_table.exclusive_disjunction(True, True))
            self.assertTrue(src.truth_table.exclusive_disjunction(True, False))
            self.assertTrue(src.truth_table.exclusive_disjunction(False, True))
            self.assertFalse(src.truth_table.exclusive_disjunction(False, False))


    # Exceptions seen

  the test is still green. :ref:`exclusive_disjunction<test_exclusive_disjunction>` returns

  - :ref:`False<test_what_is_false>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`

* I put the first two :ref:`if statements` together to make them simpler in :ref:`exclusive_disjunction<test_exclusive_disjunction>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 2-4

    def exclusive_disjunction(first_input, second_input):
        # if first_input == False:
        #     if second_input == True:
        if first_input == False and second_input == True:
                return True
        if first_input == True:
            if second_input == False:
                return True
        return False

  the test is still green

* I do the same thing with the next two :ref:`if statements`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 4-6

    def exclusive_disjunction(first_input, second_input):
        if first_input == False and second_input == True:
                return True
        # if first_input == True:
        #     if second_input == False:
        if first_input == True and second_input == False:
                return True
        return False

  still green

* I add :ref:`not<test_logical_negation>` to the first :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 2-3

    def exclusive_disjunction(first_input, second_input):
        # if first_input == False and second_input == True:
        if not first_input == True and second_input == True:
                return True
        if first_input == True and second_input == False:
                return True
        return False

  green

* I do the same thing to the second :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 4-5

    def exclusive_disjunction(first_input, second_input):
        if not first_input == True and second_input == True:
                return True
        # if first_input == True and second_input == False:
        if first_input == True and not second_input == True:
                return True
        return False

  still green

* I add bool_

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 2-3, 5-6
    :emphasize-text: bool

    def exclusive_disjunction(first_input, second_input):
        # if not first_input == True and second_input == True:
        if not bool(first_input) == True and bool(second_input) == True:
                return True
        # if first_input == True and not second_input == True:
        if bool(first_input) == True and not bool(second_input) == True:
                return True
        return False

  green

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 2-3, 5-6

    def exclusive_disjunction(first_input, second_input):
        # if not bool(first_input) == True and bool(second_input) == True:
        if not bool(first_input) and bool(second_input):
                return True
        # if bool(first_input) == True and not bool(second_input) == True:
        if bool(first_input) and not bool(second_input):
                return True
        return False

  still green

* I remove bool_

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 2-3, 5-6

    def exclusive_disjunction(first_input, second_input):
        # if not bool(first_input) and bool(second_input):
        if not first_input and second_input:
                return True
        # if bool(first_input) and not bool(second_input):
        if first_input and not second_input:
                return True
        return False

  the test is still green

* I use :ref:`Logical Disjunction<test_logical_disjunction>` to put the two :ref:`if statements` together because they both return :ref:`True<test_what_is_true>`

  .. TIP::

    I can put two :ref:`if statements` together with :ref:`Logical Disjunction (or)<test_logical_disjunction>` when they are at the same indentation level and return the same thing.

    For example

    .. code-block:: python

      if something:
          return this
      if something_else:
          return this

    can also be written as

    .. code-block:: python

      if something or something_else:
          return this

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 2-10

    def exclusive_disjunction(first_input, second_input):
        # if not first_input and second_input:
        #         return True
        # if first_input and not second_input:
        #         return True
        if (
            (not first_input and second_input)
            or
            (first_input and not second_input)
        ):
            return True
        return False

  still green

* I use a :ref:`conditional expression<conditional expressions>`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 2-6

    def exclusive_disjunction(first_input, second_input):
        return True if (
            (not first_input and second_input)
            or
            (first_input and not second_input)
        ) else False
        if (
            (not first_input and second_input)
            or
            (first_input and not second_input)
        ):
            return True
        return False

  green

* I remove the other statements in the :ref:`function<what is a function?>` and make the :ref:`ternary operator<conditional expressions>` simpler

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 2-6

    def exclusive_disjunction(first_input, second_input):
        return (
            (not first_input and second_input)
            or
            (first_input and not second_input)
        )
        return True if (
            (not first_input and second_input)
            or
            (first_input and not second_input)
        ) else False

  why is the grass greener on the other side?

* I remove the second `return statement`_

  .. code-block:: python
    :lineno-start: 51

    def exclusive_disjunction(first_input, second_input):
        return (
            (not first_input and second_input)
            or
            (first_input and not second_input)
        )

  still green

* :ref:`exclusive_disjunction<test_exclusive_disjunction>` returns :ref:`False<test_what_is_false>` when ``first_input`` and ``second_input`` are the same and returns :ref:`True<test_what_is_true>`, if they are NOT. I add an :ref:`if statement<if statements>` to show this with the equality symbol (2 equal signs together :kbd:`=+=`)

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 2-5

    def exclusive_disjunction(first_input, second_input):
        if first_input == second_input:
            return False
        else:
            return True
        return (
            (not first_input and second_input)
            or
            (first_input and not second_input)
        )

  the test is still green

* I change the new :ref:`if statement<if statements>` to a simple `return statement`_

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 2

    def exclusive_disjunction(first_input, second_input):
        return not (first_input == second_input)
        if first_input == second_input:
            return False
        else:
            return True
        return (
            (not first_input and second_input)
            or
            (first_input and not second_input)
        )

  still green

* I remove the commented lines, then use an even simpler `return statement`_ with the NOT equal symbol (exclamation mark and equal symbol :kbd:`!+=` on the keyboard)

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 2

    def exclusive_disjunction(first_input, second_input):
        return first_input != second_input
        return not (first_input == second_input)
        return (
            (not first_input and second_input)
            or
            (first_input and not second_input)
        )

:ref:`Exclusive Disjunction<test_exclusive_disjunction>` returns

* :ref:`True<test_what_is_true>`, if the first input is NOT EQUAL to the second input
* :ref:`False<test_what_is_false>`, if the first input is EQUAL to the second input
* ``first_input != second_input`` - which reads as first input is NOT equal to second input
* ``not (first_input == second_input)`` - which reads as the :ref:`Logical Negation<test_logical_negation>` of the :ref:`Logical Equality<test_logical_equality>` of the first input and the second input
* ``(not first_input and second_input) or (first_input and not second_input)`` which is the :ref:`Logical Disjunction<test_logical_disjunction>` of the :ref:`Logical Conjunction<test_logical_conjunction>` of the :ref:`Logical Negation<test_logical_negation>` of the first input, and the second input, and the :ref:`Logical Conjunction<test_logical_conjunction>` of the first input and the :ref:`Logical Negation<test_logical_negation>` of the second input. Wow! That's a lot.

All of the above statements mean the same thing. :ref:`Exclusive Disjunction<test_exclusive_disjunction>` is also known as `Exclusive OR`_ or XOR_.
Would "Logical Inequality" be a better name?

----

*********************************************************************************
test_material_non_implication
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add another test to ``test_binary.py``

.. code-block:: python
  :lineno-start: 95
  :emphasize-lines: 7-10

      def test_exclusive_disjunction(self):
          self.assertFalse(src.truth_table.exclusive_disjunction(True, True))
          self.assertTrue(src.truth_table.exclusive_disjunction(True, False))
          self.assertTrue(src.truth_table.exclusive_disjunction(False, True))
          self.assertFalse(src.truth_table.exclusive_disjunction(False, False))

      def test_material_non_implication(self):
          self.assertFalse(
              src.truth_table.material_non_implication(True, True)
          )


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'material_non_implication'. Did you mean: 'converse_non_implication'?

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add :ref:`material_non_implication<test_material_non_implication>` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 51
  :emphasize-lines: 11-12

  def exclusive_disjunction(first_input, second_input):
      return first_input != second_input
      return not (first_input == second_input)
      return (
          (not first_input and second_input)
          or
          (first_input and not second_input)
      )


  def material_non_implication(first_input, second_input):
      return False

the test passes. :ref:`material_non_implication<test_material_non_implication>` returns :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the second case - when the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>` to :ref:`test_material_non_implication` in ``test_binary.py``

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 5-7

        def test_material_non_implication(self):
            self.assertFalse(
                src.truth_table.material_non_implication(True, True)
            )
            self.assertTrue(
                src.truth_table.material_non_implication(True, False)
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

* I add an :ref:`if statement<if statements>` to :ref:`material_non_implication<test_material_non_implication>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 2-4

    def material_non_implication(first_input, second_input):
        if first_input == True:
            if second_input == False:
                return True
        return False

  the test passes. :ref:`material_non_implication<test_material_non_implication>` returns

  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`

* I add the third case, where the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>` in ``test_binary.py``

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 8-10

        def test_material_non_implication(self):
            self.assertFalse(
                src.truth_table.material_non_implication(True, True)
            )
            self.assertTrue(
                src.truth_table.material_non_implication(True, False)
            )
            self.assertFalse(
                src.truth_table.material_non_implication(False, True)
            )

  the test is still green. :ref:`material_non_implication<test_material_non_implication>` returns

  - :ref:`False<test_what_is_false>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`

* I add the fourth case, where the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 11-13

        def test_material_non_implication(self):
            self.assertFalse(
                src.truth_table.material_non_implication(True, True)
            )
            self.assertTrue(
                src.truth_table.material_non_implication(True, False)
            )
            self.assertFalse(
                src.truth_table.material_non_implication(False, True)
            )
            self.assertFalse(
                src.truth_table.material_non_implication(False, False)
            )


    # Exceptions seen

  still green. :ref:`material_non_implication<test_material_non_implication>` returns

  - :ref:`False<test_what_is_false>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>` - this is the only case where it returns :ref:`True<test_what_is_true>`
  - :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`

* I change the two :ref:`if statements` to one in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 2-4

    def material_non_implication(first_input, second_input):
        # if first_input == True:
            # if second_input == False:
        if first_input == True and second_input == False:
                return True
        return False

  green

* I add :ref:`not<test_logical_negation>`

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 2-3

    def material_non_implication(first_input, second_input):
        # if first_input == True and second_input == False:
        if first_input == True and not second_input == True:
                return True
        return False

  still green

* I use bool_

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 2-3

    def material_non_implication(first_input, second_input):
        # if first_input == True and not second_input == True:
        if bool(first_input) == True and not bool(second_input) == True:
                return True
        return False

  the test is still green

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 2-3

    def material_non_implication(first_input, second_input):
        # if bool(first_input) == True and not bool(second_input) == True:
        if bool(first_input) and not bool(second_input):
                return True
        return False

  still green

* I remove bool_

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 2-3

    def material_non_implication(first_input, second_input):
        # if bool(first_input) and not bool(second_input):
        if first_input and not second_input:
                return True
        return False

  green

* I add a :ref:`conditional expression<conditional expressions>`

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 2

    def material_non_implication(first_input, second_input):
        return True if first_input and not second_input else False
        if first_input and not second_input:
                return True
        return False

  still green

* I make the statement simpler

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 2

    def material_non_implication(first_input, second_input):
        return first_input and not second_input
        return True if first_input and not second_input else False

  the test is still green

* I remove the other statement in the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 61

    def material_non_implication(first_input, second_input):
        return first_input and not second_input

:ref:`Material NonImplication<test_material_non_implication>` returns

* ``first_input and not second_input`` which is the :ref:`Logical Conjunction<test_logical_conjunction>` of the first input and the :ref:`Logical Negation<test_logical_negation>` of the second input
* :ref:`True<test_what_is_true>`, only if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
* it is the :ref:`Logical Negation<test_logical_negation>` of :ref:`Material/Logical Implication<test_material_implication>` which returns :ref:`False<test_what_is_false>` only if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`

.. NOTE::

  ``return first_input and not second_input`` returns the :ref:`Logical Conjunction<test_logical_conjunction>` of the first input and the :ref:`Logical Negation<test_logical_negation>` of  the second input. This means that in the 4 cases

  - if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`, :ref:`material_non_implication<test_material_non_implication>` returns

    .. code-block:: python
      :emphasize-lines: 4

      first_input and not second_input
      True        and not True
      True        and False             # logical_conjunction(True, False)
      False                             # logical_conjunction(True, False)

  - if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`, :ref:`material_non_implication<test_material_non_implication>` returns

    .. code-block:: python
      :emphasize-lines: 4

      first_input and not second_input
      True        and not False
      True        and True              # logical_conjunction(True, True)
      True                              # logical_conjunction(True, True)

  - if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`, :ref:`material_non_implication<test_material_non_implication>` returns

    .. code-block:: python
      :emphasize-lines: 4

      first_input and not second_input
      False       and not True
      False       and False             # logical_conjunction(False, False)
      False                             # logical_conjunction(False, False)

  - if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`False<test_what_is_false>`, :ref:`material_non_implication<test_material_non_implication>` returns

    .. code-block:: python
      :emphasize-lines: 4

      first_input and not second_input
      False       and not False
      False       and True              # logical_conjunction(False, True)
      False                             # logical_conjunction(False, True)

----

*********************************************************************************
test_project_first
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test in ``test_binary.py``

.. code-block:: python
  :lineno-start: 101
  :emphasize-lines: 15-16

      def test_material_non_implication(self):
          self.assertFalse(
              src.truth_table.material_non_implication(True, True)
          )
          self.assertTrue(
              src.truth_table.material_non_implication(True, False)
          )
          self.assertFalse(
              src.truth_table.material_non_implication(False, True)
          )
          self.assertFalse(
              src.truth_table.material_non_implication(False, False)
          )

      def test_project_first(self):
          self.assertTrue(src.truth_table.project_first(True, True))


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'project_first'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a :ref:`function<what is a function?>` for :ref:`project_first<test_project_first>` in ``truth_table.py``

.. code-block:: python
  :lineno-start: 61
  :emphasize-lines: 5-6

  def material_non_implication(first_input, second_input):
      return first_input and not second_input


  def project_first(first_input, second_input):
      return True

the test passes. :ref:`project_first<test_project_first>` returns :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the second case to :ref:`test_project_first` in ``test_binary.py``

  .. code-block:: python
    :lineno-start: 115
    :emphasize-lines: 3

        def test_project_first(self):
            self.assertTrue(src.truth_table.project_first(True, True))
            self.assertTrue(src.truth_table.project_first(True, False))

  the test is still green. :ref:`project_first<test_project_first>` returns

  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>`

* on to the next case

  .. code-block:: python
    :lineno-start: 115
    :emphasize-lines: 4

        def test_project_first(self):
            self.assertTrue(src.truth_table.project_first(True, True))
            self.assertTrue(src.truth_table.project_first(True, False))
            self.assertFalse(src.truth_table.project_first(False, True))

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

* I add :ref:`if statements` for this case to :ref:`project_first<test_project_first>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 2-4

    def project_first(first_input, second_input):
        if first_input == False:
            if second_input == True:
                return False
        return True

  the test passes. :ref:`project_first<test_project_first>` returns

  - :ref:`False<test_what_is_false>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>`

* I add the last case to :ref:`test_project_first` in ``test_binary.py``

  .. code-block:: python
    :lineno-start: 115
    :emphasize-lines: 5

        def test_project_first(self):
            self.assertTrue(src.truth_table.project_first(True, True))
            self.assertTrue(src.truth_table.project_first(True, False))
            self.assertFalse(src.truth_table.project_first(False, True))
            self.assertFalse(src.truth_table.project_first(False, False))


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

* I add more :ref:`if statements` to :ref:`project_first<test_project_first>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 3-4

    def project_first(first_input, second_input):
        if first_input == False:
            if second_input == False:
                return False
            if second_input == True:
                return False
        return True

  the test passes. :ref:`project_first<test_project_first>` returns

  - :ref:`False<test_what_is_false>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`False<test_what_is_false>`, if the first input is :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>`
  - the first input in every case

* I add a `return statement`_

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 2

    def project_first(first_input, second_input):
        return first_input
        if first_input == False:
            if second_input == False:
                return False
            if second_input == True:
                return False
        return True

  the test is still green

* I remove the other statements

  .. code-block:: python
    :lineno-start: 65

    def project_first(first_input, second_input):
        return first_input

:ref:`Project First always returns the first input<test_project_first>`, like :ref:`Project Second which always returns the second input<test_project_second>`

----

*********************************************************************************
test_converse_implication
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test to ``test_binary.py``

.. code-block:: python
  :lineno-start: 115
  :emphasize-lines: 7-8

      def test_project_first(self):
          self.assertTrue(src.truth_table.project_first(True, True))
          self.assertTrue(src.truth_table.project_first(True, False))
          self.assertFalse(src.truth_table.project_first(False, True))
          self.assertFalse(src.truth_table.project_first(False, False))

      def test_converse_implication(self):
          self.assertTrue(src.truth_table.converse_implication(True, True))


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'converse_implication'. Did you mean: 'converse_non_implication'?

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a :ref:`function<what is a function?>` for :ref:`converse_implication<test_converse_implication>` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 65
  :emphasize-lines: 5-6

  def project_first(first_input, second_input):
      return first_input


  def converse_implication(first_input, second_input):
      return True

the test passes. :ref:`converse_implication<test_converse_implication>` returns :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the second case to :ref:`test_converse_implication` in ``test_binary.py``

  .. code-block:: python
    :lineno-start: 121
    :emphasize-lines: 3

        def test_converse_implication(self):
            self.assertTrue(src.truth_table.converse_implication(True, True))
            self.assertTrue(src.truth_table.converse_implication(True, False))

  the test is still green. :ref:`converse_implication<test_converse_implication>` returns

  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>`

* time for the next case

  .. code-block:: python
    :lineno-start: 121
    :emphasize-lines: 4

        def test_converse_implication(self):
            self.assertTrue(src.truth_table.converse_implication(True, True))
            self.assertTrue(src.truth_table.converse_implication(True, False))
            self.assertFalse(src.truth_table.converse_implication(False, True))

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

* I add :ref:`if statements` to :ref:`converse_implication<test_converse_implication>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 2-4

    def converse_implication(first_input, second_input):
        if first_input == False:
            if second_input == True:
                return False
        return True

  the test passes. :ref:`converse_implication<test_converse_implication>` returns

  - :ref:`False<test_what_is_false>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>`

* I add the last case to :ref:`test_converse_implication` in ``test_binary.py``

  .. code-block:: python
    :lineno-start: 121
    :emphasize-lines: 5

        def test_converse_implication(self):
            self.assertTrue(src.truth_table.converse_implication(True, True))
            self.assertTrue(src.truth_table.converse_implication(True, False))
            self.assertFalse(src.truth_table.converse_implication(False, True))
            self.assertTrue(src.truth_table.converse_implication(False, False))


    # Exceptions seen

  the test is still green. :ref:`converse_implication<test_converse_implication>` returns

  - :ref:`True<test_what_is_true>`, if the first input is :ref:`False<tesT_what_is_true>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`False<test_what_is_false>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>` - this is the only case where it returns :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>`

* I change the two :ref:`if statements` to one in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 2-4

    def converse_implication(first_input, second_input):
        # if first_input == False:
        #     if second_input == True:
        if first_input == False and second_input == True:
                return False
        return True

  still green

* I use :ref:`not<test_logical_negation>` to write the :ref:`if statement<if statements>` in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 2-3

    def converse_implication(first_input, second_input):
        # if first_input == False and second_input == True:
        if not first_input == True and second_input == True:
                return False
        return True

  green

* I use bool_

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 2-3

    def converse_implication(first_input, second_input):
        # if not first_input == True and second_input == True:
        if not bool(first_input) == True and bool(second_input) == True:
                return False
        return True

  still green

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 2-3

    def converse_implication(first_input, second_input):
        # if not bool(first_input) == True and bool(second_input) == True:
        if not bool(first_input) and bool(second_input):
                return False
        return True

  the test is still green

* I remove bool_

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 2-3

    def converse_implication(first_input, second_input):
        # if not bool(first_input) and bool(second_input):
        if not first_input and second_input:
                return False
        return True

  do you like green eggs and ham?

* I add the opposite of the :ref:`if statement<if statements>` for the second `return statement`_

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 4-5

    def converse_implication(first_input, second_input):
        if not first_input and second_input:
                return False
        if not (not first_input and second_input):
            return True

  still green

* I move the new :ref:`if statement<if statements>` to the top

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 2-3

    def converse_implication(first_input, second_input):
        if not (not first_input and second_input):
            return True
        if not first_input and second_input:
                return False

  green

* I add a :ref:`conditional expression<conditional expressions>`

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 2

    def converse_implication(first_input, second_input):
        return True if not (not first_input and second_input) else False
        if not (not first_input and second_input):
            return True
        if not first_input and second_input:
                return False

  still green

* I remove the other statements and write a simpler :ref:`conditional expression<conditional expressions>`

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 2

    def converse_implication(first_input, second_input):
        return not (not first_input and second_input)
        return True if not (not first_input and second_input) else False

  the test is still green

* I remove the commented lines and "multiply :ref:`not<test_logical_negation>`" by the symbols in the parentheses

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 2

    def converse_implication(first_input, second_input):
        return (not not first_input) (not and) (not second_input)
        return not (not first_input and second_input)

  the terminal_ shows SyntaxError_

  .. code-block:: shell

    SyntaxError: invalid syntax

* I change ":ref:`not<test_logical_negation>` :ref:`and<test_logical_conjunction>`" to ":ref:`or<test_logical_disjunction>`" to be correct

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 2

    def converse_implication(first_input, second_input):
        return (not not first_input) or (not second_input)
        return not (not first_input and second_input)

  back to green

* I remove the other `return statement`_ then remove  ":ref:`not<test_logical_negation>` :ref:`not<test_logical_negation>`" because they cancel out - the negation of the negation of something is something

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 2

    def converse_implication(first_input, second_input):
        return first_input or not second_input
        return (not not first_input) or (not second_input)

  the test is still green

* I remove the other `return statement`_

  .. code-block:: python
    :lineno-start: 69

    def converse_implication(first_input, second_input):
        return first_input or not second_input

:ref:`Converse Implication<test_converse_implication>` returns

- ``first_input or not second_input``
- :ref:`False<test_what_is_false>`, only if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
- the :ref:`Logical Disjunction<test_logical_disjunction>` of the first input and the :ref:`Logical Negation<test_logical_negation>` of the second input
- It is the opposite of :ref:`Converse NonImplication<test_converse_non_implication>` which always returns ``not first_input and second_input`` or :ref:`True<test_what_is_true>`, only if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`

----

*********************************************************************************
more about Exclusive Disjunction
*********************************************************************************

----

``return (not first_input and second_input) or (first_input and not second_input)`` can be thought of as

.. code-block:: python

  return x or y

- if ``x`` is ``not first_input and second_input``
- if ``y`` is ``first_input and not second_input``

:ref:`Exclusive Disjunction<test_exclusive_disjunction>` can also be thought of as

.. code-block:: python

  return (
      converse_non_implication(first_input, second_input)
      or
      material_non_implication(first_input, second_input)
  )

because

- :ref:`converse_non_implication<test_converse_non_implication>` returns ``not first_input and second_input``
- :ref:`material_non_implication<test_material_non_implication>` return ``first_input and not second_input``



This means that in the 4 cases

- if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`, :ref:`exclusive_disjunction<test_exclusive_disjunction>` returns

  .. code-block:: python
    :emphasize-lines: 5

    (not first_input and second_input) or (first_input and not second_input)
    (not True        and True        ) or (True        and not True        )
    (False           and True        ) or (True        and False           )
      False                            or  False
      False                            # logical_disjunction(False, False)

- if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`, :ref:`exclusive_disjunction<test_exclusive_disjunction>` returns

  .. code-block:: python
    :emphasize-lines: 5
    :force:

    (not first_input and second_input) or (first_input and not second_input)
    (not True        and False       ) or (True        and not False       )
    (False           and False       ) or (True        and True            )
     False                             or  True
     True                              # logical_disjunction(False, True)

- if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`, :ref:`exclusive_disjunction<test_exclusive_disjunction>` returns

  .. code-block:: python
    :emphasize-lines: 5

    (not first_input and second_input) or (first_input and not second_input)
    (not False       and True        ) or (False       and not True        )
    (True            and True        ) or (False       and False           )
     True                              or  False
     True                              # logical_disjunction(True, False)

- if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`False<test_what_is_false>`, :ref:`exclusive_disjunction<test_exclusive_disjunction>` returns

  .. code-block:: python
    :emphasize-lines: 5

    (not first_input and second_input) or (first_input and not second_input)
    (not False       and False       ) or (False       and not False       )
    (True            and False       ) or (False       and True            )
     False                             or  False
     False                             # logical_disjunction(False, False)

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_binary.py`` and ``truth_table.py`` in the :ref:`editor<2 editors>`
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

:ref:`Would you like to test the last binary operations?<binary_operations_4>`

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