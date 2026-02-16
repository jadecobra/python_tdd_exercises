.. meta::
  :description: Learn to build Binary Operations 1n Python with Test-Driven Development. This tutorial covers logical NAND, disjunction, and more. Watch the full tutorial!
  :keywords: Jacob Itegboje, python truth table binary operations, test driven development python tutorial, python logical operations for beginners, how to implement logical NAND in python, python TDD example with unittest, learn python binary logic step by step, python logical disjunction implementation, what is tautology in python programming

.. include:: ../../links.rst

.. _nots: not_

.. _binary_operations_2:

#################################################################################
truth table: Binary Operations 2
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/q_oGDjNG3_I?si=khc7CXDeEA5V46L0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

*********************************************************************************
requirements
*********************************************************************************

:ref:`Binary Operations 1<truth table: Binary Operations 1>`


----

*********************************************************************************
preview
*********************************************************************************

Here are the tests I have at the end of this chapter

.. literalinclude:: ../../code/truth_table/tests/test_binary_2.py
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
    :emphasize-lines: 5

    rootdir: .../pumping_python/truth_table
    configfile: pyproject.toml
    collected 8 items

    tests/test_binary.py ....                                     [ 50%]
    tests/test_nullary_unary.py ....                              [100%]

    ======================== 8 passed in G.HIs =========================

* I hold :kbd:`ctrl` (Windows_) or :kbd:`option` (MacOS_) on the keyboard, then click on ``tests/test_binary.py`` with the mouse to open it in the :ref:`editor<2 editors>`

----

*********************************************************************************
test_negate_first
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test for ``negate_first`` in ``test_binary.py``

.. code-block:: python
  :lineno-start: 49
  :emphasize-lines: 15-16

      def test_converse_non_implication(self):
          self.assertFalse(
              src.truth_table.converse_non_implication(True, True)
          )
          self.assertFalse(
              src.truth_table.converse_non_implication(True, False)
          )
          self.assertTrue(
              src.truth_table.converse_non_implication(False, True)
          )
          self.assertFalse(
              src.truth_table.converse_non_implication(False, False)
          )

      def test_negate_first(self):
          self.assertFalse(src.truth_table.negate_first(True, True))


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'negate_first'

there is no definition for ``negate_first`` in ``truth_table.py``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I open ``truth_table.py`` from the ``src`` folder_ in the :ref:`editor<2 editors>`

* I add the :ref:`function<what is a function?>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 6-7

    def converse_non_implication(first_input, second_input):
        return logical_conjunction(not first_input, second_input)
        return not first_input and second_input


    def negate_first(first_input, second_input):
        return False

  the test passes.

``negate_first`` returns :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the second case - when the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`, to ``test_binary.py``

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 3

        def test_negate_first(self):
            self.assertFalse(src.truth_table.negate_first(True, True))
            self.assertFalse(src.truth_table.negate_first(True, False))

  the test is still green. ``negate_first`` returns

  - :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>`

* I add the next case - when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 4

        def test_negate_first(self):
            self.assertFalse(src.truth_table.negate_first(True, True))
            self.assertFalse(src.truth_table.negate_first(True, False))
            self.assertTrue(src.truth_table.negate_first(False, True))

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

* I add :ref:`if statements`  for this case to ``negate_first`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 2-4

    def negate_first(first_input, second_input):
        if first_input == False:
            if second_input == True:
                return True
        return False

  the test passes. ``negate_first`` returns

  - :ref:`True<test_what_is_true>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>`

* I add the last case - when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`False<test_what_is_false>` to ``test_binary.py``

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 5

        def test_negate_first(self):
            self.assertFalse(src.truth_table.negate_first(True, True))
            self.assertFalse(src.truth_table.negate_first(True, False))
            self.assertTrue(src.truth_table.negate_first(False, True))
            self.assertTrue(src.truth_table.negate_first(False, False))


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

* I add an :ref:`if statement<if statements>` for it in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 3-4

    def negate_first(first_input, second_input):
        if first_input == False:
            if second_input == False:
                return True
            if second_input == True:
                return True
        return False

  the test passes. ``negate_first`` returns

  - :ref:`True<test_what_is_true>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>`

  oh! It returns the :ref:`logical negation<test_logical_negation>` of the first input

* I add a `return statement`_

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 2

    def negate_first(first_input, second_input):
        return not first_input
        if first_input == False:
            if second_input == False:
                return True
            if second_input == True:
                return True
        return False

  the test is still green

* I remove the other statements

  .. code-block:: python
    :lineno-start: 34

    def negate_first(first_input, second_input):
        return not first_input

  still green, no need for :ref:`if statements` here.

:ref:`Negate First<test_negate_first>` always returns

* ``not first_input``
* :ref:`True<test_what_is_true>`, if the first input is :ref:`False<test_what_is_false>`
* :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>`
* the :ref:`opposite (Logical Negation)<test_logical_negation>` of the first input in all cases, it does not care about the second input

----

*********************************************************************************
test_logical_nand
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test to ``test_binary.py``

.. code-block:: python
  :lineno-start: 63
  :emphasize-lines: 7-8

      def test_negate_first(self):
          self.assertFalse(src.truth_table.negate_first(True, True))
          self.assertFalse(src.truth_table.negate_first(True, False))
          self.assertTrue(src.truth_table.negate_first(False, True))
          self.assertTrue(src.truth_table.negate_first(False, False))

      def test_logical_nand(self):
          self.assertFalse(src.truth_table.logical_nand(True, True))


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'logical_nand'. Did you mean: 'logical_false'?

there is no definition for :ref:`logical_nand<test_logical_nand>` in ``truth_table.py``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add the :ref:`function<what is a function?>` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 34
  :emphasize-lines: 5-6

  def negate_first(first_input, second_input):
      return not first_input


  def logical_nand(first_input, second_input):
      return False

the test passes. :ref:`logical_nand<test_logical_nand>` returns :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the second case - when the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`, in ``test_binary.py``

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 3

        def test_logical_nand(self):
            self.assertFalse(src.truth_table.logical_nand(True, True))
            self.assertTrue(src.truth_table.logical_nand(True, False))

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

* I add :ref:`if statements` to :ref:`logical_nand<test_logical_nand>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 2-4

    def logical_nand(first_input, second_input):
        if first_input == True:
            if second_input == False:
                return True
        return False

  the test passes. :ref:`logical_nand<test_logical_nand>` returns

  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`
  - the :ref:`logical negation<test_logical_negation>` of the second input so far

* I add another case, where the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`, to :ref:`test_logical_nand` in ``test_binary.py``

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 4

        def test_logical_nand(self):
            self.assertFalse(src.truth_table.logical_nand(True, True))
            self.assertTrue(src.truth_table.logical_nand(True, False))
            self.assertTrue(src.truth_table.logical_nand(False, True))

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

* I add :ref:`if statements` to :ref:`logical_nand<test_logical_nand>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 2-4

    def logical_nand(first_input, second_input):
        if first_input == False:
            if second_input == True:
                return True
        if first_input == True:
            if second_input == False:
                return True
        return False

  the test passes. :ref:`logical_nand<test_logical_nand>` returns

  - :ref:`True<test_what_is_true>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`

* I add the last case - when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`False<test_what_is_false>`, to :ref:`test_logical_nand` in ``test_binary.py``

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 5

        def test_logical_nand(self):
            self.assertFalse(src.truth_table.logical_nand(True, True))
            self.assertTrue(src.truth_table.logical_nand(True, False))
            self.assertTrue(src.truth_table.logical_nand(False, True))
            self.assertTrue(src.truth_table.logical_nand(False, False))


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

* I add an :ref:`if statement<if statements>` to :ref:`logical_nand<test_logical_nand>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 3-4

    def logical_nand(first_input, second_input):
        if first_input == False:
            if second_input == False:
                return True
            if second_input == True:
                return True
        if first_input == True:
            if second_input == False:
                return True
        return False

  the test passes. :ref:`logical_nand<test_logical_nand>` returns

  - :ref:`True<test_what_is_true>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>` - this is the only case where it returns :ref:`False<test_what_is_false>`

* I add an :ref:`if statement<if statements>` for the one case where it returns :ref:`False<test_what_is_false>` with an else_ clause for the other 3 cases

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 2-6

    def logical_nand(first_input, second_input):
        if first_input == True:
            if second_input == True:
                return False
        else:
            return True
        if first_input == False:
            if second_input == False:
                return True
            if second_input == True:
                return True
        if first_input == True:
            if second_input == False:
                return True
        return False

  the test is still green

* I remove the other statements and put the two :ref:`if statements` together

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 2-4

    def logical_nand(first_input, second_input):
        # if first_input == True:
        #     if second_input == True:
        if first_input == True and second_input == True:
                return False
        else:
            return True

  still green

* I remove the comments and use bool_

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 2-3

    def logical_nand(first_input, second_input):
        # if first_input == True and second_input == True:
        if bool(first_input) == True and bool(second_input) == True:
                return False
        else:
            return True

  green

* I remove the commented line and ``== True``

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 2-3

    def logical_nand(first_input, second_input):
        # if bool(first_input) == True and bool(second_input) == True:
        if bool(first_input) and bool(second_input):
                return False
        else:
            return True

  still green

* I remove bool_

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 2-3

    def logical_nand(first_input, second_input):
        # if bool(first_input) and bool(second_input):
        if first_input and second_input:
                return False
        else:
            return

  the test is still green

* I want to use one `return statement`_ (:ref:`a conditional expression<conditional expressions>`) for everything, which means I need an :ref:`if statement<if statements>` that returns :ref:`True<test_what_is_true>`. I use :ref:`logical negation (not)<test_logical_negation>` to change the `else clause`_ to the opposite of the :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 4-5

    def logical_nand(first_input, second_input):
        if first_input and second_input:
                return False
        # else:
        if not (first_input and second_input):
            return True

  still green

* I move the new :ref:`if statement<if statements>` to the top

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 2-3

    def logical_nand(first_input, second_input):
        if not (first_input and second_input):
            return True
        if first_input and second_input:
                return False

  green

* I change the second :ref:`if statement<if statements>` to an `else clause`_

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 4-5

    def logical_nand(first_input, second_input):
        if not (first_input and second_input):
            return True
        # if first_input and second_input:
        else:
                return False

  green, green, green again 🎶

* I add a :ref:`conditional expression<conditional expressions>`

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 2

    def logical_nand(first_input, second_input):
        return True if not (first_input and second_input) else False
        if not (first_input and second_input):
            return True
        else:
                return False

  still green

* I remove the :ref:`if statement<if statements>` and use the simpler form of the :ref:`ternary operator<conditional expressions>`

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 2

    def logical_nand(first_input, second_input):
        return not (first_input and second_input)
        return True if not (first_input and second_input) else False

  the test is still green

* I remove the second `return statement`_

  .. code-block:: python
    :lineno-start: 38

    def logical_nand(first_input, second_input):
        return not (first_input and second_input)

  this is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`logical_conjunction<test_logical_conjunction>`

* I add a `return statement`_ to make sure

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 2

    def logical_nand(first_input, second_input):
        return not logical_conjunction(first_input, second_input)
        return not (first_input and second_input)

  green all the way

:ref:`Logical NAND<test_logical_nand>`

* returns :ref:`False<test_what_is_false>`, if the first input is :ref:`True<test_what_is_true>` and the  second input is :ref:`True<test_what_is_true>`
* returns ``not (first_input and second_input)`` which is the :ref:`opposite (Logical Negation)<test_logical_negation>` of the :ref:`Logical Conjunction<test_logical_conjunction>` of the first input and the second input, many words
* is the opposite of :ref:`Logical Conjunction<test_what_is_true>` which only returns :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and second input is :ref:`True<test_what_is_true>` or returns ``first_input and second_input``
* is the :ref:`not<test_logical_negation>` of the :ref:`and<test_logical_conjunction>` of the first input and second input, confusing?
* is :ref:`not<test_logical_negation>` :ref:`and<test_logical_conjunction>`

----

.. NOTE::

  When there is only one :ref:`if statement<if statements>` that returns :ref:`False<test_what_is_false>` with an `else clause`_

  .. code-block:: python

    if something:
        return False
    else:
        return True

  I can change it with its :ref:`logical negation (not)<test_logical_negation>`

  .. code-block:: python

    if not something:
        return True
    else:
        return False

  I can then write it as a :ref:`ternary operator<conditional expressions>` (:ref:`conditional expression<conditional expressions>`)

  .. code-block:: python

    return True if not (something) else False

  which can be made simpler as

  .. code-block:: python

    return not (something)

  this means

  - ``if something: return False`` is the same as ``return not (something)``, just like
  - ``if something: return True`` is the same as ``return something``

----

*********************************************************************************
test_tautology
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for the next Binary Operation in ``test_binary.py``

.. code-block:: python
  :lineno-start: 69
  :emphasize-lines: 7-8

      def test_logical_nand(self):
          self.assertFalse(src.truth_table.logical_nand(True, True))
          self.assertTrue(src.truth_table.logical_nand(True, False))
          self.assertTrue(src.truth_table.logical_nand(False, True))
          self.assertTrue(src.truth_table.logical_nand(False, False))

      def test_tautology(self):
          self.assertTrue(src.truth_table.tautology(True, True))


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'tautology'

``truth_table.py`` does not have :ref:`tautology<test_tautology>` in it

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add the :ref:`function<what is a function?>` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 38
  :emphasize-lines: 6-7

  def logical_nand(first_input, second_input):
      return not logical_conjunction(first_input, second_input)
      return not (first_input and second_input)


  def tautology(first_input, second_input):
      return True

the test passes. :ref:`tautology<test_tautology>` returns :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the next case, where the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`, to :ref:`test_tautology` in ``test_binary.py``

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 3

        def test_tautology(self):
            self.assertTrue(src.truth_table.tautology(True, True))
            self.assertTrue(src.truth_table.tautology(True, False))

  the test is still green. :ref:`tautology<test_tautology>` returns

  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>`

* I add the next case - when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 4

        def test_tautology(self):
            self.assertTrue(src.truth_table.tautology(True, True))
            self.assertTrue(src.truth_table.tautology(True, False))
            self.assertTrue(src.truth_table.tautology(False, True))

  the test is still green. :ref:`tautology<test_tautology>` returns :ref:`True<test_what_is_true>`

  - if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - if the first input is :ref:`True<test_what_is_true>`

* I add the last case - when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 5

        def test_tautology(self):
            self.assertTrue(src.truth_table.tautology(True, True))
            self.assertTrue(src.truth_table.tautology(True, False))
            self.assertTrue(src.truth_table.tautology(False, True))
            self.assertTrue(src.truth_table.tautology(False, False))


    # Exceptions seen

  still green, there is only one result for this operation.

:ref:`Tautology<test_tautology>` always returns :ref:`True<test_what_is_true>`, it does not care about the inputs. It is the opposite of :ref:`contradiction<test_contradiction>`  which always returns :ref:`False<test_what_is_false>`

----

*********************************************************************************
test_logical_disjunction
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add another test to ``test_binary.py``

.. code-block:: python
  :lineno-start: 75
  :emphasize-lines: 7-10

      def test_tautology(self):
          self.assertTrue(src.truth_table.tautology(True, True))
          self.assertTrue(src.truth_table.tautology(True, False))
          self.assertTrue(src.truth_table.tautology(False, True))
          self.assertTrue(src.truth_table.tautology(False, False))

      def test_logical_disjunction(self):
          self.assertTrue(
              src.truth_table.logical_disjunction(True, True)
          )


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'logical_disjunction'. Did you mean: 'logical_conjunction'?

there is no :ref:`logical_disjunction<test_logical_disjunction>` in ``truth_table.py`` in the ``src`` folder_, yet

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add the :ref:`function<what is a function?>` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 41
  :emphasize-lines: 5-6

  def tautology(first_input, second_input):
      return True


  def logical_disjunction(first_input, second_input):
      return True

the test passes. :ref:`logical_disjunction<test_logical_disjunction>` returns :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the next case - when the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`, to :ref:`test_logical_disjunction` in ``test_binary.py``

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 5-7

        def test_logical_disjunction(self):
            self.assertTrue(
                src.truth_table.logical_disjunction(True, True)
            )
            self.assertTrue(
                src.truth_table.logical_disjunction(True, False)
            )

  the test is still green. :ref:`logical_disjunction<test_logical_disjunction>` returns

  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>`

  so far this is the same as :ref:`Tautology<test_tautology>`

* I add the next case - when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 8-10

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

  the test is still green. :ref:`logical_disjunction<test_logical_disjunction>` still looks like :ref:`Tautology<test_tautology>`, it returns

  - :ref:`True<test_what_is_true>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>`

* I add the fourth case, where the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 11-13

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


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

* I add :ref:`if statements` for the new case to :ref:`logical_disjunction<test_logical_disjunction>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 2-4

    def logical_disjunction(first_input, second_input):
        if first_input == False:
            if second_input == False:
                return False
        return True

  the test passes. :ref:`logical_disjunction<test_logical_disjunction>` returns

  - :ref:`False<test_what_is_false>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`False<test_what_is_false>` - this is the only case where it returns :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>`

* I change the two :ref:`if statements` to one :ref:`if statement<if statements>` with :ref:`logical conjunction (and)<test_logical_conjunction>`

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 2-4

    def logical_disjunction(first_input, second_input):
        # if first_input == False:
        #     if second_input == False:
        if first_input == False and second_input == False:
                return False
        return True

  the test is still green

* I use :ref:`not<test_logical_negation>` to write the statements with :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 2-3

    def logical_disjunction(first_input, second_input):
        # if first_input == False and second_input == False:
        if (not first_input == True) and (not second_input == True):
                return False
        return True

  still green

* I use bool_

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 2-7

    def logical_disjunction(first_input, second_input):
        # if (not first_input == True) and (not second_input == True):
        if (
            (not bool(first_input) == True)
            and
            (not bool(second_input) == True)
        ):
                return False
        return True

  green

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 2-7

    def logical_disjunction(first_input, second_input):
        # if (
        #     (not bool(first_input) == True)
        #     and
        #     (not bool(second_input) == True)
        # ):
        if (not bool(first_input)) and (not bool(second_input)):
                return False
        return True

  still green

* I use a simpler :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 2-3

    def logical_disjunction(first_input, second_input):
        # if (not bool(first_input)) and (not bool(second_input)):
        if (not first_input) and (not second_input):
                return False
        return True

  how many green bottles standing on a wall?

* I add a second :ref:`if statement<if statements>` for the :ref:`opposite (logical negation)<test_logical_negation>` of the statement I have, like I did with :ref:`Logical NAND<test_logical_nand>`

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 4-5

    def logical_disjunction(first_input, second_input):
        if (not first_input) and (not second_input):
                return False
        if not ((not first_input) and (not second_input)):
            return True

  the test is still green, that is a lot of :ref:`nots<test_logical_negation>`

* I move the new :ref:`if statement<if statements>` to the top

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 2-3

    def logical_disjunction(first_input, second_input):
        if not ((not first_input) and (not second_input)):
            return True
        if (not first_input) and (not second_input):
                return False

  still green

* I change the second :ref:`if statement<if statements>` to an `else clause`_

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 4-5

    def logical_disjunction(first_input, second_input):
        if not ((not first_input) and (not second_input)):
            return True
        # if (not first_input) and (not second_input):
        else:
                return False

  green

* I add a :ref:`conditional expression<conditional expressions>`

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 2-4

    def logical_disjunction(first_input, second_input):
        return True if not (
            (not first_input) and (not second_input)
        ) else False
        if not ((not first_input) and (not second_input)):
            return True
        else:
                return False

  green again 🎶

* I make the `return statement`_ simpler

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 2

    def logical_disjunction(first_input, second_input):
        return not ((not first_input) and (not second_input))
        return True if not (
            (not first_input) and (not second_input)
        ) else False

  the test is still green. A reminder that I can return the :ref:`Logical Negation (not)<test_logical_negation>` of an :ref:`if statement<if statements>` that returns :ref:`False<test_what_is_false>` like I did with :ref:`Logical NAND<test_logical_nand>`

  .. NOTE::

    ``return not ((not first_input) and (not second_input))`` returns the :ref:`opposite (Logical Negation)<test_logical_negation>` of the :ref:`Logical Conjunction<test_logical_conjunction>` of the :ref:`Logical Negation<test_logical_negation>` of ``first_input``, and the :ref:`Logical Negation<test_logical_negation>` of ``second_input``. This means that in the 4 cases

    - if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`, :ref:`logical_disjunction<test_logical_disjunction>` returns

      .. code-block:: python
        :emphasize-lines: 5

        not ((not first_input) and (not second_input))
        not ((not True)        and (not True))
        not (False             and False)
        not False
        True

    - if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`, :ref:`logical_disjunction<test_logical_disjunction>` returns

      .. code-block:: python
        :emphasize-lines: 5

        not ((not first_input) and (not second_input))
        not ((not True)        and (not False))
        not (False             and True)
        not False
        True

    - if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`, :ref:`logical_disjunction<test_logical_disjunction>` returns

      .. code-block:: python
        :emphasize-lines: 5

        not ((not first_input) and (not second_input))
        not ((not False)       and (not True))
        not (True              and False)
        not False
        True

    - if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`False<test_what_is_false>`, :ref:`logical_disjunction<test_logical_disjunction>` returns

      .. code-block:: python
        :emphasize-lines: 5

        not ((not first_input) and (not second_input))
        not ((not False)       and (not False))
        not (True              and True)
        not True
        False

* ":ref:`not<test_logical_negation>`" appears 3 times in this statement, I want to change that. I "multiply" it by each thing inside the parentheses to try to make the statement simpler

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 2

    def logical_disjunction(first_input, second_input):
        return (not not first_input) (not and) (not not second_input)
        return not ((not first_input) and (not second_input))

  the terminal_ shows SyntaxError_

  .. code-block:: shell

    SyntaxError: invalid syntax

* I add SyntaxError_ to the list of :ref:`Exceptions<errors>` seen in ``test_binary.py``

  .. code-block:: python
    :lineno-start: 97
    :emphasize-lines: 5
    :emphasize-text: SyntaxError

    # Exceptions seen
    # AttributeError
    # TypeError
    # AssertionError
    # SyntaxError

* I fix the failing line by changing ":ref:`not<test_logical_negation>` :ref:`and<test_logical_conjunction>`" to "or_" in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 2
    :emphasize-text: or

    def logical_disjunction(first_input, second_input):
        return (not not first_input) or (not not second_input)
        return not ((not first_input) and (not second_input))

  the test passes

* I remove ``not not`` from the `return statement`_ because it cancels out

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 2

    def logical_disjunction(first_input, second_input):
        return first_input or second_input
        return (not not first_input) or (not not second_input)

  the test is still green. Do two :ref:`nots<test_logical_negation>` make a right?

* I remove the second `return statement`_

  .. code-block:: python
    :lineno-start: 47

    def logical_disjunction(first_input, second_input):
        return first_input or second_input

  green everywhere

:ref:`Logical Disjunction<test_logical_disjunction>` also known as "or_" returns

* ``first_input or second_input``
* :ref:`False<test_what_is_false>`, if the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`False<test_what_is_false>`

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_binary.py`` and ``truth_table.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_, then use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line

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

Binary Operations take 2 inputs, each input can be :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`, if the first input is named ``first_input`` and the second input is named ``second_input``, the tests show that

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

All the logic statements or conditions have been written with some or all of these 3.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed for the Truth Table?<truth table: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

:ref:`Would you like test even more binary operations? <binary_operations_3>`

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