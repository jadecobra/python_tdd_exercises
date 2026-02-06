.. meta::
  :description: Learn to build Binary Operations 1n Python with Test-Driven Development. This tutorial covers logical NAND, disjunction, and more. Watch the full tutorial!
  :keywords: Jacob Itegboje, python truth table binary operations, test driven development python tutorial, python logical operations for beginners, how to implement logical NAND in python, python TDD example with unittest, learn python binary logic step by step, python logical disjunction implementation, what is tautology in python programming

.. include:: ../links.rst

.. _binary_operations_ii:

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

Here are the tests I have at the end of the chapters

.. literalinclude:: ../code/truth_table/tests/test_truth_table_binary_ii.py
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

  .. NOTE::

    on Windows_ without `Windows Subsystem for Linux`_ use ``.venv/scripts/activate.ps1`` instead of ``source .venv/bin/activate``

    .. code-block:: shell
      :emphasize-lines: 1

      .venv/scripts/activate.ps1

  when the `Virtual Environment`_ is activated, the terminal_ shows

  .. code-block:: shell

    (.venv) .../pumping_python/truth_table

* run the tests

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

----

*********************************************************************************
test_negate_first
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test to the ``TestBinaryOperations`` :ref:`class<what is a class?>` in ``test_truth_table.py`` for ``negate_first``

.. code-block:: python
  :lineno-start: 49
  :emphasize-lines: 3-4

          self.assertFalse(src.truth_table.converse_non_implication(False, False))

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

I add the :ref:`function<what is a function?>` definition in ``truth_table.py``

.. code-block:: python
  :lineno-start: 29
  :emphasize-lines: 5-6

  def converse_non_implication(first_input, second_input):
      return not first_input and second_input


  def negate_first(first_input, second_input):
      return False

the test passes. ``negate_first`` returns :ref:`False<test_what_is_false>` when the first and second inputs are both :ref:`True<test_what_is_true>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

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

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

* I add :ref:`if statements`  for this case to ``negate_first`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2-4

    def negate_first(first_input, second_input):
        if first_input == False:
            if second_input == True:
                return True
        return False

  the test passes

* this is the same as the first :ref:`if statement<if statements>` in :ref:`converse_non_implication<test_converse_non_implication>`. I change the two :ref:`if statements` to one :ref:`if statement<if statements>` with :ref:`Logical Conjunction<test_logical_conjunction>` (and_)

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2-4

    def negate_first(first_input, second_input):
        if first_input == False and second_input == True:
        # if first_input == False:
        #     if second_input == True:
                return True
        return False

  the test is still green

* I remove the commented lines and move the first `return statement`_ to the left

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


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

* I add :ref:`if statements` for this case to the ``negate_first`` :ref:`function<what is a function?>` in ``truth_table.py``

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

* I change the two :ref:`if statements` to one :ref:`if statement<if statements>` with and_

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

  the test is still green

* I remove the commented lines and move the new `return statement`_ to the left

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

* since the 2 cases where the ``negate_first`` :ref:`function<what is a function?>` returns :ref:`True<test_what_is_true>` are when the first input is :ref:`False<test_what_is_false>`. I can write it as an :ref:`if statement<if statements>` with an `else clause`_

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

* I remove the other :ref:`if statement<if statements>` then use :ref:`logical_negation<test_logical_negation>` (not_) to write the first :ref:`if statement<if statements>` in terms of :ref:`True<test_what_is_true>`

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

* I remove the commented line and use bool_ with the :ref:`if statement<if statements>`

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

* I remove the commented line and make the :ref:`if statement<if statements>` simpler

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

* I remove the :ref:`if statement<if statements>` and `else clause`_, then use the simpler form of the `return statement`_

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

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test to ``test_truth_table.py``

.. code-block:: python
  :lineno-start: 55
  :emphasize-lines: 3-4

          self.assertTrue(src.truth_table.negate_first(False, False))

      def test_logical_nand(self):
          self.assertFalse(src.truth_table.logical_nand(True, True))


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'logical_nand'. Did you mean: 'logical_false'?

there is no definition for ``logical_nand`` in ``truth_table.py``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a definition for the :ref:`function<what is a function?>` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 33
  :emphasize-lines: 5-6

  def negate_first(first_input, second_input):
      return not first_input


  def logical_nand(first_input, second_input):
      return False

the test passes.

``logical_nand`` returns :ref:`False<test_what_is_false>` when the first and second inputs are both :ref:`True<test_what_is_true>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the second case - where the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`, to ``test_logical_nand`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 3

        def test_logical_nand(self):
            self.assertFalse(src.truth_table.logical_nand(True, True))
            self.assertTrue(src.truth_table.logical_nand(True, False))

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

* I add :ref:`if statements` to the ``logical_nand`` :ref:`function<what is a function?>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2-4

    def logical_nand(first_input, second_input):
        if first_input == True:
            if second_input == False:
                return True
        return False

  the test passes

* I comment out the two :ref:`if statements`, and change them to one :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2-4

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

  the terminal_ still shows green. the ``logical_nand`` :ref:`function<what is a function?>` returns

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

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

* I add two :ref:`if statements` to ``logical_nand`` in ``truth_table.py``

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

* I change the two :ref:`if statements` to one :ref:`if statement<if statements>` with :ref:`logical_conjunction<test_logical_conjunction>` (and_)

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


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

* I add two :ref:`if statements` to ``logical_nand`` in ``truth_table.py``

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

* I change the two :ref:`if statements` to one :ref:`if statement<if statements>`

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

* I remove the comments and move the new `return statement`_ to the left

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

* I add one :ref:`if statement<if statements>` for the one case that returns :ref:`False<test_what_is_false>` with an `else clause`_ for the other three cases since they all return :ref:`True<test_what_is_true>`

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

* I remove the other :ref:`if statement<if statements>` and use bool_ to change the new :ref:`if statement<if statements>`

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

* I remove the commented line and use the simpler :ref:`if statement<if statements>` that checks if the inputs are :ref:`True<test_what_is_true>` behind the scenes

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

* I want to use one `return statement`_ (a `conditional expression`_) for everything, which means I need an :ref:`if statement<if statements>` that returns :ref:`True<test_what_is_true>`. I use :ref:`logical negation<test_logical_negation>` (not_) to change the `else clause`_ to the opposite of the :ref:`if statement<if statements>`

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

* I remove the commented line and move the new :ref:`if statement<if statements>` to the top

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2-3

    def logical_nand(first_input, second_input):
        if not (first_input and second_input):
            return True
        if first_input and second_input:
            return False

  the terminal_ still shows green

* I change the second :ref:`if statement<if statements>` to an `else clause`_

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

* I remove the :ref:`if statement<if statements>` and use the simpler form of the `ternary operator`_

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

:ref:`Logical NAND<test_logical_nand>`

* returns :ref:`False<test_what_is_false>` only when the first input and second input are both :ref:`True<test_what_is_true>`
* returns ``not (first_input and second_input)`` which is the :ref:`Logical Negation<test_logical_negation>` of the :ref:`Logical Conjunction<test_logical_conjunction>` of the first input and the second input, many words
* is the not_ of the and_ of the first input and second input, confusing?
* it is the opposite of :ref:`Logical Conjunction<test_what_is_true>` which only returns :ref:`True<test_what_is_true>` when the first input and second input are both :ref:`True<test_what_is_true>` or returns ``first_input and second_input``

.. TIP::

  When there is only one :ref:`if statement<if statements>` that returns :ref:`False<test_what_is_false>` with an `else clause`_, for example

  .. code-block:: python

    if condition:
        return False
    else:
        return True

  I can rewrite it in terms of :ref:`True<test_what_is_true>` with its :ref:`logical negation<test_logical_negation>` with not_

  .. code-block:: python

    if not condition:
        return True
    else:
        return False

  I can then write it as a `ternary operator`_ (`conditional expression`_)

  .. code-block:: python

    return True if not (condition) else False

  which can be made simpler as

  .. code-block:: python

    return not (condition)

----

*********************************************************************************
test_tautology
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for the next Binary Operation in ``test_truth_table.py`` with the first case where the two inputs are :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 61
  :emphasize-lines: 3-4

          self.assertTrue(src.truth_table.logical_nand(False, False))

      def test_tautology(self):
          self.assertTrue(src.truth_table.tautology(True, True))


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'tautology'

``truth_table.py`` does not have ``tautology`` defined inside it

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a :ref:`function<what is a function?>` definition in ``truth_table.py``

.. code-block:: python
  :lineno-start: 37
  :emphasize-lines: 5-6

  def logical_nand(first_input, second_input):
      return not (first_input and second_input)


  def tautology(first_input, second_input):
      return True

the test passes. ``tatutology`` returns :ref:`True<test_what_is_true>` when the two inputs are :ref:`True<test_what_is_true>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the next case to ``test_tautology`` in ``test_truth_table.py`` - when ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 3

        def test_tautology(self):
            self.assertTrue(src.truth_table.tautology(True, True))
            self.assertTrue(src.truth_table.tautology(True, False))

  the terminal_ still shows green. ``tautology`` returns

  - :ref:`True<test_what_is_true>` when the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>` when the two inputs are :ref:`True<test_what_is_true>`
  - :ref:`True<test_what_is_true>` when the first input is :ref:`True<test_what_is_true>`

* I add the next case - when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 4

        def test_tautology(self):
            self.assertTrue(src.truth_table.tautology(True, True))
            self.assertTrue(src.truth_table.tautology(True, False))
            self.assertTrue(src.truth_table.tautology(False, True))

  the test is still green. ``tautology`` returns :ref:`True<test_what_is_true>`

  - when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - when the first input is :ref:`True<test_what_is_true>`

* I add the last case - when the two inputs are :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 5

        def test_tautology(self):
            self.assertTrue(src.truth_table.tautology(True, True))
            self.assertTrue(src.truth_table.tautology(True, False))
            self.assertTrue(src.truth_table.tautology(False, True))
            self.assertTrue(src.truth_table.tautology(False, False))


    # Exceptions seen

  still green, there is only one result for this operation.

:ref:`Tautology<test_tautology>` returns :ref:`True<test_what_is_true>`

* when the two inputs are :ref:`False<test_what_is_false>`
* when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
* when the first input is :ref:`False<test_what_is_false>`
* when the first input is :ref:`True<test_what_is_true>`

It always returns :ref:`True<test_what_is_true>`, it is the opposite of :ref:`Contradiction<test_contradiction>` which always returns :ref:`False<test_what_is_false>`

----

*********************************************************************************
test_logical_disjunction
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add another test to ``test_truth_table.py`` with the first case, where the two inputs are :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 67
  :emphasize-lines: 3-4

          self.assertTrue(src.truth_table.tautology(False, False))

      def test_logical_disjunction(self):
          self.assertTrue(src.truth_table.logical_disjunction(True, True))


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'logical_disjunction'. Did you mean: 'logical_conjunction'?

there is no definition for ``logical_disjunction`` in ``truth_table.py`` in the ``src`` folder_ yet

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

the test passes. ``logical_disjunction`` returns :ref:`True<test_what_is_true>` when the two inputs are :ref:`True<test_what_is_true>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the next case - when ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`, to ``test_logical_disjunction`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 3

        def test_logical_disjunction(self):
            self.assertTrue(src.truth_table.logical_disjunction(True, True))
            self.assertTrue(src.truth_table.logical_disjunction(True, False))

  the terminal_ still shows green. ``logical_disjunction`` returns

  - :ref:`True<test_what_is_true>` when the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>` when the two inputs are :ref:`True<test_what_is_true>`
  - :ref:`True<test_what_is_true>` when the first input is :ref:`True<test_what_is_true>`

  so far this is the same as :ref:`Tautology<test_tautology>`

* I add the next case - where the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 4

        def test_logical_disjunction(self):
            self.assertTrue(src.truth_table.logical_disjunction(True, True))
            self.assertTrue(src.truth_table.logical_disjunction(True, False))
            self.assertTrue(src.truth_table.logical_disjunction(False, True))

  the test is still green. ``logical_disjunction`` still looks like :ref:`Tautology<test_tautology>`, it returns

  - :ref:`True<test_what_is_true>` when ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`
  - :ref:`True<test_what_is_true>` when ``first_input`` is :ref:`True<test_what_is_true>`

* I add the fourth case, where the two inputs are :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 5

        def test_logical_disjunction(self):
            self.assertTrue(src.truth_table.logical_disjunction(True, True))
            self.assertTrue(src.truth_table.logical_disjunction(True, False))
            self.assertTrue(src.truth_table.logical_disjunction(False, True))
            self.assertFalse(src.truth_table.logical_disjunction(False, False))


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

* I add :ref:`if statements` for the new case to ``logical_disjunction`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2-4

    def logical_disjunction(first_input, second_input):
        if first_input == False:
            if second_input == False:
                return False
        return True

  the test passes. ``logical_disjunction`` returns

  - :ref:`False<test_what_is_false>` when the two inputs are :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>` when ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`
  - :ref:`True<test_what_is_true>` when ``first_input`` is :ref:`True<test_what_is_true>`
  - :ref:`True<test_what_is_true>` when the two inputs are NOT :ref:`False<test_what_is_false>`

* I change the two :ref:`if statements` to one :ref:`if statement<if statements>` with and_

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
        if (not first_input == True) and (not second_input == True):
        # if first_input == False and second_input == False:
            return False
        return True

  the terminal_ still shows green

* I use bool_ to make the :ref:`if statement<if statements>` simpler

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2-3

    def logical_disjunction(first_input, second_input):
        if (not bool(first_input)) and (not bool(second_input)):
        # if (not first_input == True) and (not second_input == True):
            return False
        return True

  the terminal_ shows green

* I use a simpler `if statement`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2-3

    def logical_disjunction(first_input, second_input):
        if (not first_input) and (not second_input):
        # if (not bool(first_input)) and (not bool(second_input)):
            return False
        return True

  how many green bottles standing on a wall?

* I add a second :ref:`if statement<if statements>` for the cases where ``logical_disjunction`` returns :ref:`True<test_what_is_true>` like I did with :ref:`Logical NAND<test_logical_nand>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 4-5

    def logical_disjunction(first_input, second_input):
        if (not first_input) and (not second_input):
            return False
        if not ((not first_input) and (not second_input)):
            return True

  the test is still green

* I move the new :ref:`if statement<if statements>` to the top

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2-3

    def logical_disjunction(first_input, second_input):
        if not ((not first_input) and (not second_input)):
            return True
        if (not first_input) and (not second_input):
            return False

  green

* I change the second :ref:`if statement<if statements>` to an `else clause`_

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 4-5

    def logical_disjunction(first_input, second_input):
        if not ((not first_input) and (not second_input)):
            return True
        else:
        # if (not first_input) and (not second_input):
            return False

* I add a `conditional expression`_

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2

    def logical_disjunction(first_input, second_input):
        return True if not ((not first_input) and (not second_input)) else False
        if not ((not first_input) and (not second_input)):
            return True
        else:
            return False

* I make the `return statement`_ simpler

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2

    def logical_disjunction(first_input, second_input):
        return not ((not first_input) and (not second_input))
        return True if not ((not first_input) and (not second_input)) else False

  the terminal_ still shows green. A reminder that I can return the :ref:`Logical Negation<test_logical_negation>` (not_) of an :ref:`if statement<if statements>` that returns :ref:`False<test_what_is_false>` like I did with :ref:`Logical NAND<test_logical_nand>`

* "not_" appears 3 times in this statement, I want to change that. I "multiply" it by each thing inside the parentheses to try to make the statement simpler

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2

    def logical_disjunction(first_input, second_input):
        return (not not first_input) (not and) (not not second_input)
        return not ((not first_input) and (not second_input))

  the terminal_ shows SyntaxError_

  .. code-block:: shell

    SyntaxError: invalid syntax

* I add it to the list of :ref:`Exceptions<errors>` seen in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 5

    # Exceptions seen
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
        return not ((not first_input) and (not second_input))

  the test passes

* I remove "not_ not_" from the `return statement`_ because it cancels out

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2

    def logical_disjunction(first_input, second_input):
        return first_input or second_input
        return (not not first_input) or (not not second_input)

  the test is still green. Do two nots_ make a right?

* I remove the second `return statement`_

  .. code-block:: python
    :lineno-start: 45

    def logical_disjunction(first_input, second_input):
        return first_input or second_input

  green everywhere

:ref:`Logical Disjunction<test_logical_disjunction>` also known as "or_" returns

* ``first_input or second_input``
* :ref:`False<test_what_is_false>` only when the two inputs are :ref:`False<test_what_is_false>`

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

Binary Operations take 2 inputs, each input can be :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`, if the first input is named ``first_input`` and the second input is named ``second_input``, the tests show that

* :ref:`Logical Disjunction <test_logical_disjunction>`

  - returns ``first_input or second_input``
  - returns :ref:`False<test_what_is_false>` when ``first_input`` and ``second_input`` are both :ref:`False<test_what_is_false>`
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
  - returns :ref:`True<test_what_is_true>` when ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`
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

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed for the Truth Table?<truth table: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

:ref:`Would you like test even more binary operations? <binary_operations_iii>`

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