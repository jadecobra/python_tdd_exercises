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

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test to the ``TestBinaryOperations`` :ref:`class<classes>` in ``test_truth_table.py`` for ``negate_first``

.. code-block:: python
  :lineno-start: 49
  :emphasize-lines: 3-4

          self.assertFalse(src.truth_table.converse_non_implication(False, False))

      def test_negate_first(self):
          self.assertFalse(src.truth_table.negate_first(True, True))


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'negate_first'

there is no definition for ``negate_first`` in ``truth_table.py``

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add the :ref:`function<functions>` definition in ``truth_table.py``

.. code-block:: python
  :lineno-start: 29
  :emphasize-lines: 5-6

  def converse_non_implication(first_input, second_input):
      return not first_input and second_input


  def negate_first(first_input, second_input):
      return False

the test passes. ``negate_first`` returns :ref:`False<test_what_is_false>` when the first and second inputs are both :ref:`True<test_what_is_true>`

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add the second case - where the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`, to ``test_negate_first`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 3

        def test_negate_first(self):
            self.assertFalse(src.truth_table.negate_first(True, True))
            self.assertFalse(src.truth_table.negate_first(True, False))

  the test is still green. ``negate_first`` returns

  - :ref:`False<test_what_is_false>` when the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>` when both the first and second inputs are :ref:`True<test_what_is_true>`
  - :ref:`False<test_what_is_false>` when the first input is :ref:`True<test_what_is_true>`

* I add the next case - when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 4

        def test_negate_first(self):
            self.assertFalse(src.truth_table.negate_first(True, True))
            self.assertFalse(src.truth_table.negate_first(True, False))
            self.assertTrue(src.truth_table.negate_first(False, True))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: False is not true

* I add `if statements`_  for this case to ``negate_first`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2-4

    def negate_first(first_input, second_input):
        if first_input == False:
            if second_input == True:
                return True
        return False

  the test passes

* this is the same as the first `if statements`_ in :ref:`converse_non_implication<test_converse_non_implication>`. I change the two `if statements`_ to one `if statement`_ with :ref:`Logical Conjunction<test_logical_conjunction>` (and_)

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2-4

    def negate_first(first_input, second_input):
        if first_input == False and second_input == True:
        # if first_input == False:
        #     if second_input == True:
                return True
        return False

  the test is still green. I remove the commented lines and move the first `return statement`_ to the left

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 3

    def negate_first(first_input, second_input):
        if first_input == False and second_input == True:
            return True
        return False

  ``negate_first`` returns

  - :ref:`True<test_what_is_true>` when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`False<test_what_is_false>` when the first input is :ref:`True<test_what_is_true>`

* I add the last case - when the first and second inputs are both :ref:`False<test_what_is_false>`, to ``test_negate_first`` in ``test_truth_table.py``

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

  .. code-block:: shell

    AssertionError: False is not true

* I add `if statements`_ for this case to the ``negate_first`` :ref:`function<functions>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2-4

    def negate_first(first_input, second_input):
        if first_input == False:
            if second_input == False:
                return True
        if first_input == False and second_input == True:
            return True
        return False

  the test passes

* I change the two `if statements`_ to one `if statement`_ with and_

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2-4

    def negate_first(first_input, second_input):
        if first_input == False and second_input == False:
        # if first_input == False:
        #     if second_input == False:
                return True
        if first_input == False and second_input == True:
            return True
        return False

  the test is still green. I remove the commented lines and move the new `return statement`_ to the left

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 3

    def negate_first(first_input, second_input):
        if first_input == False and second_input == False:
            return True
        if first_input == False and second_input == True:
            return True
        return False

  ``negate_first`` returns

  - :ref:`True<test_what_is_true>` when ``first_input`` and ``second_input`` are both :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>` when ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`
  - :ref:`True<test_what_is_true>`
  - :ref:`False<test_what_is_false>` when ``first_input`` is :ref:`True<test_what_is_true>`

* since the 2 cases where the ``negate_first`` :ref:`function<functions>` returns :ref:`True<test_what_is_true>` are when the first input is :ref:`False<test_what_is_false>`. I can write it as an `if statement`_ with an else_ clause

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2-5

    def negate_first(first_input, second_input):
        if first_input == False:
            return True
        else:
            return False
        if first_input == False and second_input == False:
            return True
        if first_input == False and second_input == True:
            return True
        return False

  the test is still green

* I remove the other `if statements`_ then use :ref:`logical_negation<test_logical_negation>` (not_) to write the first `if statement`_ in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2-3

    def negate_first(first_input, second_input):
        if not first_input == True:
        # if first_input == False:
            return True
        else:
            return False

  the test is still passing

* I remove the commented line and use bool_ with the `if statement`_

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2-3

    def negate_first(first_input, second_input):
        if not bool(first_input):
        # if not first_input == True:
            return True
        else:
            return False

  still green

* I remove the commented line and make the `if statement`_ simpler

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2-3

    def negate_first(first_input, second_input):
        if not first_input:
        # if not bool(first_input):
            return True
        else:
            return False

  the test is still green

* I remove the commented line then add a `ternary operator`_ (`conditional expression`_)

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2

    def negate_first(first_input, second_input):
        return True if not first_input else False
        if not first_input:
            return True
        else:
            return False

  still green

* I remove the `if statement`_ and else_ clause, then use the simpler form of the `return statement`_

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2

    def negate_first(first_input, second_input):
        return not first_input
        return True if not first_input else False

  the test is still green

* I remove the second `return statement`_

  .. code-block:: python
    :lineno-start: 33

    def negate_first(first_input, second_input):
        return not first_input

:ref:`Negate First<test_negate_first>` negates the first input, it always returns

* ``not first_input``
* the :ref:`Logical Negation<test_logical_negation>` of the first input
* the opposite of the first input
* :ref:`True<test_what_is_true>` when the first input is :ref:`False<test_what_is_false>`
* :ref:`False<test_what_is_false>` when the first input is :ref:`True<test_what_is_true>`

----

*********************************************************************************
test_logical_nand
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a new test to ``test_truth_table.py``

.. code-block:: python
  :lineno-start: 55
  :emphasize-lines: 3-4

          self.assertTrue(src.truth_table.negate_first(False, False))

      def test_logical_nand(self):
          self.assertFalse(src.truth_table.logical_nand(True, True))


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'logical_nand'. Did you mean: 'logical_false'?

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add a definition for the :ref:`function<functions>` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 33
  :emphasize-lines: 5-6

  def negate_first(first_input, second_input):
      return not first_input


  def logical_nand(first_input, second_input):
      return False

the test passes.

``logical_nand`` returns :ref:`False<test_what_is_false>` when the first and second inputs are both :ref:`True<test_what_is_true>`

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add the second case - where the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`, to ``test_logical_nand`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 3

        def test_logical_nand(self):
            self.assertFalse(src.truth_table.logical_nand(True, True))
            self.assertTrue(src.truth_table.logical_nand(True, False))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: False is not true

* I add `if statements`_ to the ``logical_nand`` :ref:`function<functions>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2-4

    def logical_nand(first_input, second_input):
        if first_input == True:
            if second_input == False:
                return True
        return False

  the test passes

* I comment out the two `if statements`_, and change them to one `if statement`_

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 3-5

    def logical_nand(first_input, second_input):
        if first_input == True and second_input == False:
        # if first_input == True:
        #     if second_input == False:
                return True
        return False

  the test is still green

* I remove the commented lines, and move the first `return statement`_ to the left

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 3

    def logical_nand(first_input, second_input):
        if first_input == True and second_input == False:
            return True
        return False

  the terminal_ still shows green. the ``logical_nand`` :ref:`function<functions>` returns

  - :ref:`True<test_what_is_true>` when the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>` when the first and second inputs are both :ref:`True<test_what_is_true>`

* I add another case, where the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`, to ``test_logical_nand`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 4

        def test_logical_nand(self):
            self.assertFalse(src.truth_table.logical_nand(True, True))
            self.assertTrue(src.truth_table.logical_nand(True, False))
            self.assertTrue(src.truth_table.logical_nand(False, True))

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: False is not true

* I add two `if statements`_ to ``logical_nand`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2-4

    def logical_nand(first_input, second_input):
        if first_input == False:
            if second_input == True:
                return True
        if first_input == True and second_input == False:
            return True
        return False

  the test passes

* I change the two `if statements`_ to one `if statement`_ with :ref:`logical_conjunction<test_logical_conjunction>` (and_)

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2-4

    def logical_nand(first_input, second_input):
        if first_input == False and second_input == True:
        # if first_input == False:
        #     if second_input == True:
                return True
        if first_input == True and second_input == False:
            return True
        return False

  the test is still green

* I remove the commented lines and move the new `return statement`_ to the left

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 3

    def logical_nand(first_input, second_input):
        if first_input == False and second_input == True:
            return True
        if first_input == True and second_input == False:
            return True
        return False

  still green. ``logical_nand`` returns

  - :ref:`True<test_what_is_true>` when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`True<test_what_is_true>` when the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>` when the first and second inputs are both :ref:`True<test_what_is_true>`

* I add the last case - where the first and second inputs are both :ref:`False<test_what_is_false>`, to ``test_logical_nand`` in ``test_truth_table.py``

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

  .. code-block:: shell

    AssertionError: False is not true

* I add two `if statements`_ to ``logical_nand`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2-4

    def logical_nand(first_input, second_input):
        if first_input == False:
            if second_input == False:
                return True
        if first_input == False and second_input == True:
            return True
        if first_input == True and second_input == False:
            return True
        return False

  the test passes

* I change the two `if statements`_ to one `if statement`_

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2-4

    def logical_nand(first_input, second_input):
        if first_input == False and second_input == False:
        # if first_input == False:
        #     if second_input == False:
                return True
        if first_input == False and second_input == True:
            return True
        if first_input == True and second_input == False:
            return True
        return False

  the test is still green

* I remove the comments and move the `return statement`_ to the left

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 3

    def logical_nand(first_input, second_input):
        if first_input == False and second_input == False:
            return True
        if first_input == False and second_input == True:
            return True
        if first_input == True and second_input == False:
            return True
        return False

  the terminal_ still shows green. ``logical_nand`` returns

  - :ref:`True<test_what_is_true>` when the first and second inputs are both :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>` when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`True<test_what_is_true>` when the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>` when the first and second inputs are both :ref:`True<test_what_is_true>`

* I add one `if statement`_ for the case that returns :ref:`False<test_what_is_false>` with an else_ clause for the other 3 since they all return :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2-5

    def logical_nand(first_input, second_input):
        if first_input == True and second_input == True:
            return False
        else:
            return True
        if first_input == False and second_input == False:
            return True
        if first_input == False and second_input == True:
            return True
        if first_input == True and second_input == False:
            return True
        return False

  the test is still green

* I remove the other `if statements`_ and use bool_ to change the `if statement`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2-3

    def logical_nand(first_input, second_input):
        if bool(first_input) and bool(second_input):
        # if first_input == True and second_input == True:
            return False
        else:
            return True

  the terminal_ still shows green

* I remove the commented line and use the simpler `if statement`_ that checks if the inputs are :ref:`True<test_what_is_true>` behind the scenes

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2-3

    def logical_nand(first_input, second_input):
        if first_input and second_input:
        # if bool(first_input) and bool(second_input):
            return False
        else:
            return True

  still green

* I want to use a single `return statement`_ (a `conditional expression`_), which means I have to use an `if statement`_ that returns :ref:`True<test_what_is_true>`. use :ref:`logical negation<test_logical_negation>` aka not_ to change the else_ clause to the opposite of the `if statement`_

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 4-5

    def logical_nand(first_input, second_input):
        if first_input and second_input:
            return False
        if not (first_input and second_input):
        # else:
            return True

  the test is still green

* I remove the `else`_ clause and move the new `if statement`_ to the top

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2-3

    def logical_nand(first_input, second_input):
        if not (first_input and second_input):
            return True
        if first_input and second_input:
            return False

  the terminal_ still shows green

* I change the second `if statement`_ to an else_ clause

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2-3

    def logical_nand(first_input, second_input):
        if not (first_input and second_input):
            return True
        else:
        # if first_input and second_input:
            return False

  green, green, green again 🎶

* I remove the comment, then add a `conditional expression`_

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2

    def logical_nand(first_input, second_input):
        return True if not (first_input and second_input) else False
        if not (first_input and second_input):
            return True
        else:
            return False

  still green

* I remove the `if statements` and use the simpler form of the `ternary operator`_

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2

    def logical_nand(first_input, second_input):
        return not (first_input and second_input)
        return True if not (first_input and second_input) else False

  the test is still passing

* I remove the second `return statement`_

  .. code-block:: python
    :lineno-start: 37

    def logical_nand(first_input, second_input):
        return not (first_input and second_input)

:ref:`Logical Nand<test_logical_nand>`

* returns :ref:`False<test_what_is_false>` only when the first input and second input are both :ref:`True<test_what_is_true>`
* returns ``not (first_input and second_input)`` which is the :ref:`Logical Negation<test_logical_negation>` of the :ref:`Logical Conjunction<test_logical_conjunction>` of the first input and the second input
* in other words is the not_ of the and_ of the first input and second input
* it is the opposite of :ref:`Logical Conjunction<test_what_is_true>` which only returns :ref:`True<test_what_is_true>` when the first input and second input are both :ref:`True<test_what_is_true>` or returns ``first_input and second_input``

.. TIP::

  When there is only one `if statement`_ that returns :ref:`False<test_what_is_false>` with an else_ clause, for example

  .. code-block:: python

    if condition:
        return False
    else:
        return True

  I can return its :ref:`logical negation<test_logical_negation>` with not_

  .. code-block:: python

    return True if not (condition) else False

  which can be made simpler as

  .. code-block:: python

    return not (condition)

----

*********************************************************************************
test_tautology
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test for the next Binary Operation in ``test_truth_table.py`` with the first case where both inputs are :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 61
  :emphasize-lines: 3-4

          self.assertTrue(src.truth_table.logical_nand(False, False))

      def test_tautology(self):
          self.assertTrue(src.truth_table.tautology(True, True))


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'tautology'

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add a :ref:`function<functions>` definition in ``truth_table.py``

.. code-block:: python
  :lineno-start: 37
  :emphasize-lines: 5-6

  def logical_nand(first_input, second_input):
      return not (first_input and second_input)


  def tautology(first_input, second_input):
      return True

the test passes. ``tatutology`` returns :ref:`True<test_what_is_true>` when both inputs are :ref:`True<test_what_is_true>`

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add the next case to ``test_tautology`` in ``test_truth_table.py`` - when ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 3

        def test_tautology(self):
            self.assertTrue(src.truth_table.tautology(True, True))
            self.assertTrue(src.truth_table.tautology(True, False))

  the terminal_ still shows green. ``tautology`` returns :ref:`True<test_what_is_true>` when the first input is :ref:`True<test_what_is_true>`

* I add the next case - when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 4

        def test_tautology(self):
            self.assertTrue(src.truth_table.tautology(True, True))
            self.assertTrue(src.truth_table.tautology(True, False))
            self.assertTrue(src.truth_table.tautology(False, True))

  the test is still green. ``tautology`` returns :ref:`True<test_what_is_true>`

  - when the first input is :ref:`True<test_what_is_true>`
  - when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`

* I add the last case - when both inputs are :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 5

        def test_tautology(self):
            self.assertTrue(src.truth_table.tautology(True, True))
            self.assertTrue(src.truth_table.tautology(True, False))
            self.assertTrue(src.truth_table.tautology(False, True))
            self.assertTrue(src.truth_table.tautology(False, False))


    # Exceptions Encountered

  still green, there is only one result for this operation. :ref:`Tautology<test_tautology>` always returns :ref:`True<test_what_is_true>`, it is the opposite of :ref:`Contradiction<test_contradiction>` which always returns :ref:`False<test_what_is_false>`

----

*********************************************************************************
test_logical_disjunction
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add another test to ``test_truth_table.py`` with the first case, where the two inputs are :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 67
  :emphasize-lines: 4-5

          self.assertTrue(src.truth_table.tautology(False, False))

      def test_logical_disjunction(self):
          self.assertTrue(src.truth_table.logical_disjunction(True, True))


  # Exceptions Encountered

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'logical_disjunction'. Did you mean: 'logical_conjunction'?

there is no definition for ``logical_disjunction`` in ``truth_table.py`` in the ``src`` folder_ yet

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add the :ref:`function<functions>` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 41
  :emphasize-lines: 5-6

  def tautology(first_input, second_input):
      return True


  def logical_disjunction(first_input, second_input):
      return True

the test passes. ``logical_disjunction`` returns :ref:`True<test_what_is_true>` when both inputs are :ref:`True<test_what_is_true>`

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add the next case - when ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`, to ``test_logical_disjunction`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 3

        def test_logical_disjunction(self):
            self.assertTrue(src.truth_table.logical_disjunction(True, True))
            self.assertTrue(src.truth_table.logical_disjunction(True, False))

  the terminal_ still shows green. ``logical_disjunction`` returns :ref:`True<test_what_is_true>` when the first input is :ref:`True<test_what_is_true>`, so far this is the same as :ref:`Tautology<test_tautology>`

* I add the next case - when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 4

        def test_logical_disjunction(self):
            self.assertTrue(src.truth_table.logical_disjunction(True, True))
            self.assertTrue(src.truth_table.logical_disjunction(True, False))
            self.assertTrue(src.truth_table.logical_disjunction(False, True))

  the test is still green. ``logical_disjunction`` still looks like :ref:`Tautology<test_tautology>`, it returns

  - :ref:`True<test_what_is_true>` when ``first_input`` is :ref:`True<test_what_is_true>`
  - :ref:`True<test_what_is_true>` when ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`

* I add the fourth case, where both inputs are :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 5

        def test_logical_disjunction(self):
            self.assertTrue(src.truth_table.logical_disjunction(True, True))
            self.assertTrue(src.truth_table.logical_disjunction(True, False))
            self.assertTrue(src.truth_table.logical_disjunction(False, True))
            self.assertFalse(src.truth_table.logical_disjunction(False, False))


    # Exceptions Encountered

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: True is not false

* I add `if statements`_ for the new case to ``logical_disjunction`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2-4

    def logical_disjunction(first_input, second_input):
        if first_input == False:
            if second_input == False:
                return False
        return True

  the test passes. ``logical_disjunction`` only returns :ref:`False<test_what_is_false>` when both inputs are :ref:`False<test_what_is_false>`

* I change the two `if statements`_ to one `if statement`_ with and_

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2-4

    def logical_disjunction(first_input, second_input):
        if first_input == False and second_input == False:
        # if first_input == False:
        #     if second_input == False:
                return False
        return True

  the test is still green

* I remove the commented line and move the first `return statement`_ to the left

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 3

    def logical_disjunction(first_input, second_input):
        if first_input == False and second_input == False:
            return False
        return True

  still green

* I use not_ to write the statements in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2-3

    def logical_disjunction(first_input, second_input):
        if not first_input == True and not second_input == True:
        # if first_input == False and second_input == False:
            return False
        return True

  the terminal_ still shows green

* I use bool_ to make the `if statement`_ simpler

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2-3

    def logical_disjunction(first_input, second_input):
        if not bool(first_input) and not bool(second_input):
        # if not first_input == True and not second_input == True:
            return False
        return True

  the terminal_ shows green

* I use a simpler `if statement`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2-3

    def logical_disjunction(first_input, second_input):
        if not first_input and not second_input:
        # if not bool(first_input) and not bool(second_input):
            return False
        return True

  green

* I add a second `if statement`_ for the cases where the ``logical_disjunction`` returns :ref:`True<test_what_is_true>` like I did with :ref:`Logical NAND<test_logical_nand>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 4-5

    def logical_disjunction(first_input, second_input):
        if not first_input and not second_input:
            return False
        if not (not first_input and not second_input):
            return True

  the test is still green

* I move the new `if statement`_ to the top

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2-3

    def logical_disjunction(first_input, second_input):
        if not (not first_input and not second_input):
            return True
        if not first_input and not second_input:
            return False

* I change the second `if statement`_ to an else_ clause

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 3-4

    def logical_disjunction(first_input, second_input):
        if not (not first_input and not second_input):
            return True
        else:
        # if not first_input and not second_input:
            return False

* I add a `conditional expression`_

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2

    def logical_disjunction(first_input, second_input):
        return True if not (not first_input and not second_input) else False
        if not (not first_input and not second_input):
            return True
        else:
            return False

* I make the `return statement`_ simpler

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2

    def logical_disjunction(first_input, second_input):
        return not (not first_input and not second_input)
        return True if not (not first_input and not second_input) else False

  the terminal_ still shows green. A reminder that I can return the negation of an `if statement`_ that returns :ref:`False<test_what_is_false>` like I did in :ref:`Logical NAND<test_logical_nand>`

* "not_" appears 3 times in this statement, I want to change that. I "multiply" it by each thing in the parentheses to try to make the statement simpler

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2

    def logical_disjunction(first_input, second_input):
        return (not not first_input) (not and) (not not second_input)
        return not (not first_input and not second_input)

  the terminal_ shows SyntaxError_

  .. code-block:: shell

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

    def logical_disjunction(first_input, second_input):
        return (not not first_input) or (not not second_input)
        return not (not first_input and not second_input)

  the test passes

* I remove "not_ not_" from the `return statement`_ because it cancels out

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2

    def logical_disjunction(first_input, second_input):
        return first_input or second_input
        return (not not first_input) or (not not second_input)

  the test is still green. Two nots_ don't make a right

* I remove the the second `return statement`_

  .. code-block:: python
    :lineno-start: 45

    def logical_disjunction(first_input, second_input):
        return first_input or second_input

:ref:`Logical Disjunction<test_logical_disjunction>` aka or_ returns

* :ref:`False<test_what_is_false>` only when both inputs are :ref:`False<test_what_is_false>`
* ``first_input or second_input``

----

*********************************************************************************
review
*********************************************************************************

Binary Operations take 2 inputs, each input can be :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`, if the first input is named``first_input`` and the second input is named ``second_input``, the tests show that

* :ref:`Logical Disjunction <test_logical_disjunction>` returns ``first_input or second_input``
* :ref:`Tautology <test_tautology>` always returns :ref:`True<test_what_is_true>`
* :ref:`Logical NAND <test_logical_nand>` returns ``not (first_input and second_input)``
* :ref:`Negate First<test_negate_first>` always returns ``not first_input``
* :ref:`Converse NonImplication <test_converse_non_implication>` returns ``not first_input and second_input``
* :ref:`Project Second <test_project_second>` always returns ``second_input``
* :ref:`Logical Conjunction <test_logical_conjunction>` returns ``first_input and second_input``
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