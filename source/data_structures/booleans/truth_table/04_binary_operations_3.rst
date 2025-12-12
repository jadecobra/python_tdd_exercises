.. meta::
  :description: Master Python's boolean logic. This clear, step-by-step guide explains AND, OR, and NOT operators with easy-to-follow truth tables. Build your first one now.
  :keywords: Jacob Itegboje, python truth table for beginners, boolean logic and or not first_inputython tutorial, how to make a truth table in python code, practical use of truth tables in programming, python logical operators explained for new programmers, understanding boolean expressions in python, python 'and' vs 'or' truth table differences, troubleshooting boolean logic in python script

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

*********************************************************************************
how to get back to the automated tests
*********************************************************************************

If your tests stopped after the :ref:`previous chapter<truth table: Binary Operations part 2>`, heres's how to get back to the tests

* Make sure you are in the ``pumping_python`` folder_ with pwd_

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

* run the automated tests

  .. code-block:: shell
    :emphasize-lines: 1

    pytest-watch

----

*********************************************************************************
test_exclusive_disjunction
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

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

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add the :ref:`function<functions>` for ``exclusive_disjunction`` in ``truth_table.py``

.. code-block:: python
  :lineno-start: 45
  :emphasize-lines: 5-6

  def logical_disjunction(first_input, second_input):
      return first_input or second_input


  def exclusive_disjunction(first_input, second_input):
      return False

the test passes. ``exclusive_disjunction`` returns :ref:`False<test_what_is_false>` when both inputs are :ref:`True<test_what_is_true>`

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

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

* I add `if statements`_ to ``exclusive_disjunction`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2-4

    def exclusive_disjunction(first_input, second_input):
        if first_input == True:
            if second_input == False:
                return True
        return False

  the test passes

* I change the two `if statements`_ to one `if statement`_

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2-3

    def exclusive_disjunction(first_input, second_input):
        if first_input == True and second_input == False:
        # if first_input == True:
        #     if second_input == False:
                return True
        return False

  still green

* I remove the commented line and move the `return statement`_ to the left

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 3

    def exclusive_disjunction(first_input, second_input):
        if first_input == True and second_input == False:
            return True
        return False

  the terminal_ still shows green. ``exclusive_disjunction`` returns

  - :ref:`True<test_what_is_true>` when ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>` when both inputs are :ref:`True<test_what_is_true>`

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

* I add `if statements`_ to ``exclusive_disjunction`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2-3

    def exclusive_disjunction(first_input, second_input):
        if first_input == False:
            if second_input == True:
                return True
        if first_input == True and second_input == False:
            return True
        return False

  the test passes

* I change the new statements to one `if statement`_

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2-4

    def exclusive_disjunction(first_input, second_input):
        if first_input == False and second_input == True:
        # if first_input == False:
        #     if second_input == True:
                return True
        if first_input == True and second_input == False:
            return True
        return False

  still green

* I remove the comments and move the `return statement`_ to the left

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 3

    def exclusive_disjunction(first_input, second_input):
        if first_input == False and second_input == True:
            return True
        if first_input == True and second_input == False:
            return True
        return False

  the terminal_ still shows green. ``exclusive_disjunction`` returns

  - :ref:`True<test_what_is_true>` when ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`
  - :ref:`True<test_what_is_true>` when ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>` when both inputs are :ref:`True<test_what_is_true>`

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

  the test is still green. ``exclusive_disjunction`` returns

  - :ref:`False<test_what_is_false>` when both inputs are :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>` when ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`
  - :ref:`True<test_what_is_true>` when ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>` when both inputs are :ref:`True<test_what_is_true>`

* I write the `if statements`_ in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2-3, 5-6

    def exclusive_disjunction(first_input, second_input):
        if not first_input == True and second_input == True:
        # if first_input == False and second_input == True:
            return True
        if first_input == True and not second_input == True:
        # if first_input == True and second_input == False:
            return True
        return False

  is green the color of money?

* I remove the commented lines and make the statements simpler with bool_

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2-3, 5-6

    def exclusive_disjunction(first_input, second_input):
        if not bool(first_input) and bool(second_input):
        # if not first_input == True and second_input == True:
            return True
        if bool(first_input) and not bool(second_input):
        # if first_input == True and not second_input == True:
            return True
        return False

  still green

* I remove the commented lines and make the `if statements`_ simpler

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2-3, 5-6

    def exclusive_disjunction(first_input, second_input):
        if not first_input and second_input:
        # if not bool(first_input) and bool(second_input):
            return True
        if first_input and not second_input:
        # if bool(first_input) and not bool(second_input):
            return True
        return False

  the test is still passing

  .. TIP:: I can put two `if statements`_ together with :ref:`Logical Disjunction<test_logical_disjunction>` (or_) when they are at the same indentation level and return the same thing. For example

    .. code-block:: python

      if something:
          return this
      if something_else:
          return this

    can also be written as

    .. code-block:: python

      if something or something_else:
          return this

* I use :ref:`Logical Disjunction<test_logical_disjunction>` to put the two `if statements`_ that return :ref:`True<test_what_is_true>` together

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2-3

    def exclusive_disjunction(first_input, second_input):
        if (not first_input and second_input) or (first_input and not second_input):
            return True
        # if not first_input and second_input:
        #     return True
        # if first_input and not second_input:
        #     return True
        return False

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 49

    def exclusive_disjunction(first_input, second_input):
        if (not first_input and second_input) or (first_input and not second_input):
            return True
        return False

  the test is still passing

* I use a `conditional expression`_

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2

    def exclusive_disjunction(first_input, second_input):
        return True if (not first_input and second_input) or (first_input and not second_input) else False
        if (not first_input and second_input) or (first_input and not second_input):
            return True
        return False

  why is the grass greener on the other side?

* I remove the other statements and make the `ternary operator`_ simpler

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2

    def exclusive_disjunction(first_input, second_input):
        return (not first_input and second_input) or (first_input and not second_input)
        return True if (not first_input and second_input) or (first_input and not second_input) else False

  the terminal_ still shows green

* I remove the second `return statement`_

  .. code-block:: python
    :lineno-start: 49

    def exclusive_disjunction(first_input, second_input):
        return (not first_input and second_input) or (first_input and not second_input)

  still green

* ``exclusive_disjunction`` returns :ref:`False<test_what_is_false>` when ``first_input`` and ``second_input`` are the same and returns :ref:`True<test_what_is_true>` when they are NOT. I add an `if statement`_ to show this with the equality symbol (``==``)

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2-5

    def exclusive_disjunction(first_input, second_input):
        if first_input == second_input:
            return False
        else:
            return True
        return (not first_input and second_input) or (first_input and not second_input)

  the terminal_ still shows green

* I change the new `if statement`_ to a simple `return statement`_

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2

    def exclusive_disjunction(first_input, second_input):
        return not (first_input == second_input)
        # if first_input == second_input:
        #     return False
        # else:
        #     return True
        return (not first_input and second_input) or (first_input and not second_input)

  the test is still green

* I remove the commented lines, then use an even simpler `return statement`_ with the NOT equal symbol (``!=``)

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2

    def exclusive_disjunction(first_input, second_input):
        return first_input != second_input
        return not (first_input == second_input)
        return (not first_input and second_input) or (first_input and not second_input)

:ref:`Exclusive Disjunction<test_exclusive_disjunction>` returns

* :ref:`True<test_what_is_true>` when the two inputs are NOT equal
* :ref:`False<test_what_is_false>` when the two inputs are equal
* ``first_input != second_input`` - which reads as first input is NOT equal to second input
* ``not (first_input == second_input)`` - which reads as the :ref:`Logical Negation<test_logical_negation>` of the :ref:`Logical Equality<test_logical_equality>` of the first input and the second input
* ``(not first_input and second_input) or (first_input and not second_input)`` which is the :ref:`Logical Disjunction<test_logical_disjunction>` of the :ref:`Logical Conjunction<test_logical_conjunction>` of the :ref:`Logical Negation<test_logical_negation>` of the first input and the second input, and the :ref:`Logical Conjunction<test_logical_conjunction>` of first input and the :ref:`Logical Negation<test_logical_negation>` of the second input. Wow! That's a lot

all of the above statements mean the same thing. Would "Logical Inequality" be a better name for :ref:`Exclusive Disjunction<test_exclusive_disjunction>`?

:ref:`Exclusive Disjunction<test_exclusive_disjunction>` is also known as `Exclusive OR <https://grokipedia.com/page/Exclusive_or>`_


----

*********************************************************************************
test_material_non_implication
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

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

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add a :ref:`function<functions>` for ``material_non_implication`` in ``truth_table.py``

.. code-block:: python
  :lineno-start: 49
  :emphasize-lines: 7-8

  def exclusive_disjunction(first_input, second_input):
      return first_input != second_input
      return not first_input == second_input
      return (not first_input and second_input) or (first_input and not second_input)


  def material_non_implication(first_input, second_input):
      return False

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

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

    def material_non_implication(first_input, second_input):
        if first_input and not second_input:
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

    def material_non_implication(first_input, second_input):
        return first_input and not second_input
        if first_input and not second_input:
            return True
        return False

  the test is still green

* I remove the other statements

  .. code-block:: python
    :lineno-start: 55

    def material_non_implication(first_input, second_input):
        return first_input and not second_input

----

*********************************************************************************
test_project_first
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

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

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add a :ref:`function<functions>` definition for ``project_first`` in ``truth_table.py``

.. code-block:: python
  :lineno-start: 55
  :emphasize-lines: 5-6

  def material_non_implication(first_input, second_input):
      return first_input and not second_input


  def project_first(first_input, second_input):
      return True

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

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

    def project_first(first_input, second_input):
        if not first_input and second_input:
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

    def project_first(first_input, second_input):
        if not first_input and not second_input:
            return False
        if not first_input and second_input:
            return False
        return True

  the test passes

* I add a `return statement`_ to show that this :ref:`function<functions>` returns the same value as ``first_input`` in every case

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 2

    def project_first(first_input, second_input):
        return first_input
        if not first_input and not second_input:
            return False
        if not first_input and second_input:
            return False
        return True

  the terminal_ still shows green

* I remove the other statements

  .. code-block:: python
    :lineno-start: 59

    def project_first(first_input, second_input):
        return first_input

----

*********************************************************************************
test_converse_implication
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

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

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add a :ref:`function<functions>` definition for ``converse_implication`` in ``truth_table.py``

.. code-block:: python
  :lineno-start: 59
  :emphasize-lines: 5-6

  def project_first(first_input, second_input):
      return first_input


  def converse_implication(first_input, second_input):
      return True

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

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

    def converse_implication(first_input, second_input):
        if not first_input and second_input:
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

    def converse_implication(first_input, second_input):
        return not (not first_input and second_input)
        if not first_input and second_input:
            return False
        return True

  the test is still green

* I "multiply not_" by the symbols in the parentheses

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 2

    def converse_implication(first_input, second_input):
        return not not first_input not and not second_input
        return not (not first_input and second_input)

  the terminal_ shows SyntaxError_

  .. code-block:: shell

    SyntaxError: invalid syntax

  I change "not_ and_" to "or_" to be correct

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 2

    def converse_implication(first_input, second_input):
        return not not first_input or not second_input
        return not (not first_input and second_input)

  back to green

* I remove "not_ not_" since it cancels out, the negation of a negation is the original thing

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 2

    def converse_implication(first_input, second_input):
        return first_input or not second_input
        return not (not first_input and second_input)

  the tests is still green

* I remove the other statements

  .. code-block:: python
    :lineno-start: 63

    def converse_implication(first_input, second_input):
        return first_input or not second_input

----

*********************************************************************************
review
*********************************************************************************

Binary Operations take 2 inputs, each input can be :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`, if we name the first input ``first_input`` and the second one ``second_input``, the tests show that

* :ref:`Converse Implication <test_converse_implication>` returns ``first_input or not second_input``
* :ref:`Project First <test_project_first>` always returns ``first_input``
* :ref:`Material NonImplication <test_material_non_implication>` returns ``first_input and not second_input``
* :ref:`Exclusive Disjunction <test_exclusive_disjunction>` returns ``first_input != second_input``
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