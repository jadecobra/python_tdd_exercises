.. meta::
  :description: Master Python truth tables for binary operations. This guide simplifies 'if' statements with clear, step-by-step Python code examples. Watch the tutorial!
  :keywords: Jacob Itegboje, python truth table for if statements, python truth table generator from expression, python logical operators truth table, python truth table for two variables, how to make a truth table in python, python contradiction function, python logical conjunction truth table

.. include:: ../../../links.rst
.. _if statement: https://docs.python.org/3/tutorial/controlflow.html#if-statements
.. _if statements: `if statement`_

.. _binary_operations_i:

#################################################################################
truth table: Binary Operations 1
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/Q_jhE204MoE?si=m9_EvOX-4lrmSzo7" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

The last chapter covered 2 types of operations. :ref:`Nullary Operations` which do not take input, and :ref:`Unary Operations` which take 1 input.

There are also Binary Operations, these take 2 inputs. Each of the inputs in this exercise will be :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>` which means there are 4 possible ways the inputs can be sent to an :ref:`operation<what is a function?>`

* :ref:`True <test_what_is_true>`, :ref:`True <test_what_is_true>`
* :ref:`True <test_what_is_true>`, :ref:`False <test_what_is_false>`
* :ref:`False <test_what_is_false>`, :ref:`True <test_what_is_true>`
* :ref:`False <test_what_is_false>`, :ref:`False <test_what_is_false>`

*********************************************************************************
preview
*********************************************************************************

These combinations give 16 binary operations each of which returns :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>` based on the inputs it receives. Here are the 16 operations that are covered in these chapters and what they return

* :ref:`Material Implication  <test_material_implication>` returns

  - ``not first_input or second_input``
  - :ref:`False<test_what_is_false>` when ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`

* :ref:`Logical Equality <test_logical_equality>` returns

  - ``first_input == second_input``
  - :ref:`True<test_what_is_true>` when ``first_input`` and ``second_input`` are equal

* :ref:`Logical NOR <test_logical_nor>` returns

  - ``not (first_input or second_input)``
  - :ref:`True<test_what_is_true>` when ``first_input`` and ``second_input`` are both :ref:`False<test_what_is_false>`

* :ref:`Negate Second <test_negate_second>` returns

  - ``not second_input``
  - :ref:`True<test_what_is_true>` when ``second_input`` is :ref:`True<test_what_is_true>`

* :ref:`Converse Implication <test_converse_implication>` returns

  - ``first_input or not second_input``
  - :ref:`False<test_what_is_false>` when ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`

* :ref:`Project First <test_project_first>` returns

  - ``first_input``
  - :ref:`True<test_what_is_true>` when ``first_input`` is :ref:`True<test_what_is_true>`

* :ref:`Material NonImplication <test_material_non_implication>` returns

  - ``first_input and not second_input``
  - :ref:`True<test_what_is_true>` when ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`

* :ref:`Exclusive Disjunction <test_exclusive_disjunction>` returns

  - ``first_input != second_input``
  - :ref:`True<test_what_is_true>` when ``first_input`` and ``second_input`` are NOT equal

* :ref:`Logical Disjunction <test_logical_disjunction>` returns

  - ``first_input or second_input``
  - :ref:`True<test_what_is_true>` when ``first_input`` and ``second_input`` are both :ref:`False<test_what_is_false>`

* :ref:`Tautology <test_tautology>` always returns :ref:`True<test_what_is_true>`

* :ref:`Logical NAND <test_logical_nand>` returns

  - ``not (first_input and second_input)``
  - :ref:`False<test_what_is_false>` when ``first_input`` and ``second_input`` are both :ref:`True<test_what_is_true>`

* :ref:`Negate First<test_negate_first>` returns

  - ``not first_input``
  - :ref:`True<test_what_is_true>` when ``first_input`` is :ref:`False<test_what_is_false>`

* :ref:`Converse NonImplication <test_converse_non_implication>` returns

  - ``not first_input and second_input``
  - :ref:`True<test_what_is_true>` when ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`

* :ref:`Project Second <test_project_second>` returns

  - ``second_input``
  - :ref:`True<test_what_is_true>` when ``second_input`` is :ref:`True<test_what_is_true>`

* :ref:`Logical Conjunction <test_logical_conjunction>` returns

  - ``first_input and second_input``
  - :ref:`True<test_what_is_true>` when ``first_input`` and ``second_input`` are :ref:`True<test_what_is_true>`

* :ref:`Contradiction <test_contradiction>` always returns :ref:`False<test_what_is_false>`

----

*********************************************************************************
requirements
*********************************************************************************

:ref:`truth table: Nullary and Unary Operations`

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

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``.venv/scripts/activate.ps1`` instead of ``source .venv/bin/activate``

    .. code-block:: shell
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
test_contradiction
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a new TestCase_ to ``test_truth_table.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 25, 27-28

  import unittest
  import src.truth_table


  class TestNullaryOperations(unittest.TestCase):

      def test_logical_true(self):
          self.assertTrue(src.truth_table.logical_true())

      def test_logical_false(self):
          self.assertFalse(src.truth_table.logical_false())


  class TestUnaryOperations(unittest.TestCase):

      def test_logical_identity(self):
          self.assertTrue(src.truth_table.logical_identity(True))
          self.assertFalse(src.truth_table.logical_identity(False))

      def test_logical_negation_aka_not(self):
          self.assertFalse(src.truth_table.logical_negation(True))
          self.assertTrue(src.truth_table.logical_negation(False))


  class TestBinaryOperations(unittest.TestCase):

      def test_contradiction(self):
          self.assertFalse(src.truth_table.contradiction(True, True))


  # Exceptions seen

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'contradiction'

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add a :ref:`function<what is a function?>` definition to ``truth_table.py``

.. code-block:: python
  :lineno-start: 13
  :emphasize-lines: 5-6

  def logical_negation(the_input):
      return not the_input


  def contradiction(the_input):
      return not the_input

the terminal_ shows :ref:`TypeError`

.. code-block:: shell

  TypeError: contradiction() takes 1 positional argument but 2 were given

The definition only takes one input, but the test sent two. I add ``second_input`` as the second name in parentheses then change ``argument`` to ``first_input`` for the first input given when the :ref:`function<what is a function?>` is called by the test

.. TIP:: In `Visual Studio Code`_ I can change all the places that a name is in the file_, by using

  * Find and Replace - ``ctrl+H`` on Windows_ or ``option+command+F`` on MacOS_ or with
  * Rename Symbol

    - Right click on the name you want to change, for example ``the_input`` then select ``Rename Symbol`` or
    - Select the name you want to change then used :kbd:`F2` on your keyboard to rename it

.. code-block:: python
  :lineno-start: 17
  :emphasize-lines: 1-2

  def contradiction(first_input, second_input):
      return not first_input

the test passes. When ``contradiction`` gets :ref:`True<test_what_is_true>` as its first input and :ref:`True<test_what_is_true>` as its second input, it returns the :ref:`opposite<test_logical_negation>` of the first input, that means it returns not_ :ref:`True<test_what_is_true>` which is :ref:`False<test_what_is_false>`

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add the second case to ``test_contradiction`` in ``test_truth_table.py``, this is when the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 3

        def test_contradiction(self):
            self.assertFalse(src.truth_table.contradiction(True, True))
            self.assertFalse(src.truth_table.contradiction(True, False))

  the test is still green. ``contradiction`` returns :ref:`False<test_what_is_false>` in the two cases where the first input is :ref:`True<test_what_is_true>`

* I add the third case, which is when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 4


        def test_contradiction(self):
            self.assertFalse(src.truth_table.contradiction(True, True))
            self.assertFalse(src.truth_table.contradiction(True, False))
            self.assertFalse(src.truth_table.contradiction(False, True))

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

  so far all three cases of the test expect :ref:`False<test_what_is_false>`, which means ``contradiction`` should return :ref:`False<test_what_is_false>` when

  - the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`
  - the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`
  - the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`

* I change the `return statement`_ in the ``contradiction`` :ref:`function<what is a function?>` in ``truth_table.py`` to return the expectation

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 2

    def contradiction(first_input, second_input):
        return False

  the test passes

* I add the fourth case to ``test_contradiction`` in ``test_truth_table.py``, this is when the two inputs are :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 5

        def test_contradiction(self):
            self.assertFalse(src.truth_table.contradiction(True, True))
            self.assertFalse(src.truth_table.contradiction(True, False))
            self.assertFalse(src.truth_table.contradiction(False, True))
            self.assertFalse(src.truth_table.contradiction(False, False))


    # Exceptions seen

  the test is still green!

:ref:`Contradiction<test_contradiction>` always returns :ref:`False<test_what_is_false>` it does not matter what inputs it gets

----

*********************************************************************************
test_logical_conjunction
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test for ``logical_conjunction`` in ``test_truth_table.py`` with the first case where the two inputs are :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 31
  :emphasize-lines: 3-4

            self.assertFalse(src.truth_table.contradiction(False, False))

        def test_logical_conjunction(self):
            self.assertTrue(src.truth_table.logical_conjunction(True, True))


  # Exceptions seen

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'logical_conjunction'. Did you mean: 'logical_negation'?

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add the :ref:`function<what is a function?>` in ``truth_table.py``

.. code-block:: python
  :lineno-start: 17
  :emphasize-lines: 5-6

  def contradiction(first_input, second_input):
      return False


  def logical_conjunction(first_input, second_input):
      return True

the test . ``logical_conjunction`` returns :ref:`True<test_what_is_true>` when the first and second input are both :ref:`True<test_what_is_true>`

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add the next case - when the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`, to ``test_logical_conjunction`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 3

        def test_logical_conjunction(self):
            self.assertTrue(src.truth_table.logical_conjunction(True, True))
            self.assertFalse(src.truth_table.logical_conjunction(True, False))

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

* I make the ``logical_conjunction`` :ref:`function<what is a function?>` in ``truth_table.py`` return :ref:`False <test_what_is_false>`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2

    def logical_conjunction(first_input, second_input):
        return False
        return True

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

  The line that was passing before is now failing

``logical_conjunction`` has to make a choice. It should return

- :ref:`False<test_what_is_false>` when the first input and second input are both :ref:`True<test_what_is_true>`
- :ref:`True<test_what_is_true>` when the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`

I can make it do that with `if statements`_

---------------------------------------------------------------------------------
if statements
---------------------------------------------------------------------------------

An `if statement`_ is a way for a program_ to do something based on something else. I can use them to make a :ref:`function<what is a function?>` choose between 2 things, there are written as

.. code-block:: python

  if something:
      do this

* I add `if statements`_ to the ``logical_conjunction`` :ref:`function<what is a function?>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2-4

    def logical_conjunction(first_input, second_input):
        if first_input == True:
            if second_input == False:
                return False
        return True

  the test passes. ``logical_conjunction`` returns

  - :ref:`False<test_what_is_false>` when ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>` when the two inputs are :ref:`True<test_what_is_true>`

* I add the case where the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>` to ``test_logical_conjunction`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 4

        def test_logical_conjunction(self):
            self.assertTrue(src.truth_table.logical_conjunction(True, True))
            self.assertFalse(src.truth_table.logical_conjunction(True, False))
            self.assertFalse(src.truth_table.logical_conjunction(False, True))

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

* I add another `if statement`_ for this case to ``logical_conjunction`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2-4

    def logical_conjunction(first_input, second_input):
        if first_input == False:
            if second_input == True:
                return False
        if first_input == True:
            if second_input == False:
                return False
        return True

  the test passes. ``logical_conjunction`` returns

  - :ref:`False<test_what_is_false>` when ``first_input`` is :ref:`False<test_what_is_False>` and ``second_input`` is :ref:`True<test_what_is_true>`
  - :ref:`False<test_what_is_false>` when ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>` when the two inputs are :ref:`True<test_what_is_true>`

* I add the last case, which is when the two inputs are :ref:`False<test_what_is_false>`, to ``test_logical_conjunction`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 5

        def test_logical_conjunction(self):
            self.assertTrue(src.truth_table.logical_conjunction(True, True))
            self.assertFalse(src.truth_table.logical_conjunction(True, False))
            self.assertFalse(src.truth_table.logical_conjunction(False, True))
            self.assertFalse(src.truth_table.logical_conjunction(False, False))


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

* I add `if statements`_ for the new case to ``logical_conjunction`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2-4

    def logical_conjunction(first_input, second_input):
        if first_input == False:
            if second_input == False:
                return False
        if first_input == False:
            if second_input == True:
                return False
        if first_input == True:
            if second_input == False:
                return False
        return True

  the test passes. ``logical_conjunction`` returns

  - :ref:`False<test_what_is_false>` when the two inputs are :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>` when ``first_input`` is :ref:`False<test_what_is_False>` and ``second_input`` is :ref:`True<test_what_is_true>`
  - :ref:`False<test_what_is_false>` when ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>` when the two inputs are :ref:`True<test_what_is_true>`

* I have the same `if statement`_ twice - ``if first_input == False`` for the 3rd and 4th cases where the first input is :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2, 5

    def logical_conjunction(first_input, second_input):
        if first_input == False:
            if second_input == False:
                return False
        if first_input == False:
            if second_input == True:
                return False
        if first_input == True:
            if second_input == False:
                return False
        return True

  I remove the second one

  .. code-block:: python
    :lineno-start: 21

    def logical_conjunction(first_input, second_input):
        if first_input == False:
            if second_input == False:
                return False
            if second_input == True:
                return False
        if first_input == True:
            if second_input == False:
                return False
        return True

  the test is still green

* I add an `if statement`_ for the first case, where the first and second inputs are both :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 10-11

    def logical_conjunction(first_input, second_input):
        if first_input == False:
            if second_input == False:
                return False
            if second_input == True:
                return False
        if first_input == True:
            if second_input == False:
                return False
            if second_input == True:
                return True

  the terminal_ still shows green

* there are only 2 results for this operation, in the first case the :ref:`function<what is a function?>` returns :ref:`True <test_what_is_true>`. In the other 3 cases it returns :ref:`False <test_what_is_false>`.

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 4, 6, 9, 11

    def logical_conjunction(first_input, second_input):
        if first_input == False:
            if second_input == False:
                return False
            if second_input == True:
                return False
        if first_input == True:
            if second_input == False:
                return False
            if second_input == True:
                return True

  .. TIP:: I can put two `if statements`_ together when one is under the other. For example

    .. code-block:: python

      if something:
          if something_else:

    can also be written as

    .. code-block:: python

      if something and something_else:

* I put the two `if statements`_ for the one case where the result is :ref:`True <test_what_is_true>` together and use an `else clause`_ for the other cases where the first and second inputs are not both :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2-5

    def logical_conjunction(first_input, second_input):
        if first_input == True and second_input == True:
            return True
        else:
            return False
        if first_input == False:
            if second_input == False:
                return False
            if second_input == True:
                return False
        if first_input == True:
            if second_input == False:
                return False
            if second_input == True:
                return True

  the test is still green

* I remove the other `if statements`_ then use bool_ in the first `if statement`_

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2-3

    def logical_conjunction(first_input, second_input):
        if bool(first_input) and bool(second_input):
        # if first_input == True and second_input == True:
            return True
        else:
            return False

  still green. bool_ checks if the thing in parentheses is :ref:`True <test_what_is_true>` in the background

* I remove the commented line then change the first line to make it simpler

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2-3

    def logical_conjunction(first_input, second_input):
        if first_input and second_input:
        # if bool(first_input) and bool(second_input):
            return True
        else:
            return False

  the test is still green

  .. TIP:: these `if statements`_ are the same

    - ``if something == True:``
    - ``if bool(something): == True``
    - ``if bool(something):``
    - ``if something:``

    Python_ checks if ``something`` is :ref:`True<test_what_is_true>` in the background when I type ``if something:``

  I remove the commented line

---------------------------------------------------------------------------------
conditional expressions
---------------------------------------------------------------------------------

* Python_ has `ternary operators`_ or `conditional expressions`_ which allow me to write the `if statement`_ and the `else clause`_ as one line

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2

    def logical_conjunction(first_input, second_input):
        return True if first_input and second_input else False
        if first_input and second_input:
            return True
        else:
            return False

  the terminal_ shows green

* I remove the other `if statements`_ then change the `return statement`_ to a simpler form

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2

    def logical_conjunction(first_input, second_input):
        return first_input and second_input
        return True if first_input and second_input else False

  still green!

* I remove the second `return statement`_

  .. code-block:: python
    :lineno-start: 21

    def logical_conjunction(first_input, second_input):
        return first_input and second_input

:ref:`Logical Conjunction<test_logical_conjunction>` also known as and_, returns

* ``first_input and second_input``
* :ref:`True<test_what_is_true>` when the two inputs are both :ref:`True<test_what_is_true>`

.. TIP:: All of the statements below give the same result

  * this checks if ``something`` is :ref:`True<test_what_is_true>`

    .. code-block:: python

      if something == True:
          return True
      else:
          return False

  * this uses bool_ to get the :ref:`boolean<what are booleans?>` of ``something`` then checks if the result is :ref:`True<test_what_is_true>`

    .. code-block:: python

      if bool(something) == True:
          return True
      else:
          return False

  * this checks if ``bool(something)`` is :ref:`True<test_what_is_true>` in the background

    .. code-block:: python

      if bool(something):
          return True
      else:
          return False

  * this checks if ``something`` is :ref:`True<test_what_is_true>` in the background

    .. code-block:: python

      if something:
          return True
      else:
          return False

  * this returns :ref:`True<test_what_is_true>` if ``something`` is :ref:`True<test_what_is_true>`

    .. code-block:: python

      return True if something else False

  * this also returns :ref:`True<test_what_is_true>` after checking if ``something`` is :ref:`True<test_what_is_true>` in the background

    .. code-block:: python

      return something

  the last one works because Python_ tests if ``something`` is :ref:`True<test_what_is_true>` in the background same as it does when I type ``if something:``

----

*********************************************************************************
test_project_second
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test for another Binary Operation in ``test_truth_table.py``

.. code-block:: python
  :lineno-start: 37
  :emphasize-lines: 3-4

          self.assertFalse(src.truth_table.logical_conjunction(False, False))

      def test_project_second(self):
          self.assertTrue(src.truth_table.project_second(True, True))


  # Exceptions seen

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'project_second'

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add a definition for the :ref:`function<what is a function?>` in ``truth_table.py``

.. code-block:: python
  :lineno-start: 21
  :emphasize-lines: 5-6

  def logical_conjunction(first_input, second_input):
      return first_input and second_input


  def project_second(first_input, second_input):
      return True

the test passes. When the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`, this :ref:`function<what is a function?>` returns :ref:`True<test_what_is_true>`

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add the second case - where the first input is :ref:`True<test_what_is_true>` and the second input :ref:`False<test_what_is_false>`, to ``test_project_second`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 3

        def test_project_second(self):
            self.assertTrue(src.truth_table.project_second(True, True))
            self.assertFalse(src.truth_table.project_second(True, False))

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

* I add an `if statement`_ for the case to ``project_second`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 2-4

    def project_second(first_input, second_input):
        if first_input == True:
            if second_input == False:
                return False
        return True

  the test

  - ``project_second`` returns :ref:`False<test_what_is_false>` when the first input is :ref:`True<test_what_is_true>` and the second input :ref:`False<test_what_is_false>`
  - it returns :ref:`True<test_what_is_true>` in every other case

* I add the next case, which is when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>` to ``test_project_second`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 4

        def test_project_second(self):
            self.assertTrue(src.truth_table.project_second(True, True))
            self.assertFalse(src.truth_table.project_second(True, False))
            self.assertTrue(src.truth_table.project_second(False, True))

  the test is still green

* I add the last case - when the two inputs are :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 5

        def test_project_second(self):
            self.assertTrue(src.truth_table.project_second(True, True))
            self.assertFalse(src.truth_table.project_second(True, False))
            self.assertTrue(src.truth_table.project_second(False, True))
            self.assertFalse(src.truth_table.project_second(False, False))


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

* I add an `if statement`_ for this case to ``project_second`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 2-4

    def project_second(first_input, second_input):
        if first_input == False:
            if second_input == False:
                return False
        if first_input == True:
            if second_input == False:
                return False
        return True

  the test passes

* ``project_second`` returns

  - :ref:`False<test_what_is_false>` when ``second_input`` is :ref:`False<test_what_is_false>`
  - :ref:`True<test_what_is_true>` when ``second_input`` is :ref:`True<test_what_is_true>`

  It returns the same value as the second input. I add a new `return statement`_ to show this

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 2

    def project_second(first_input, second_input):
        return second_input
        if first_input == False:
            if second_input == False:
                return False
        if first_input == True:
            if second_input == False:
                return False
        return True

  the test is still green

* I remove the other statements

  .. code-block:: python
    :lineno-start: 25

    def project_second(first_input, second_input):
        return second_input

:ref:`Project Second<test_project_second>` returns the second input, it always returns

* :ref:`True<test_what_is_true>` when the second input is :ref:`True<test_what_is_true>`
* :ref:`False<test_what_is_false>` when the second input is :ref:`False<test_what_is_false>`

----

*********************************************************************************
test_converse_non_implication
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test for ``converse_non_implication`` in ``test_truth_table.py``

.. code-block:: python
  :lineno-start: 43
  :emphasize-lines: 3-4

          self.assertFalse(src.truth_table.project_second(False, False))

      def test_converse_non_implication(self):
          self.assertFalse(src.truth_table.converse_non_implication(True, True))


  # Exceptions seen

the terminal_ shows :ref:`AttributeError`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'converse_non_implication'

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I add the :ref:`function<what is a function?>` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 25
  :emphasize-lines: 5-6

  def project_second(first_input, second_input):
      return second_input


  def converse_non_implication(first_input, second_input):
      return False

the test passes. ``converse_non_implication`` returns :ref:`False<test_what_is_false>` when the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add the next case to ``test_converse_non_implication`` in ``test_truth_table.py``, when the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 3

        def test_converse_non_implication(self):
            self.assertFalse(src.truth_table.converse_non_implication(True, True))
            self.assertFalse(src.truth_table.converse_non_implication(True, False))

  the test is still green, because it expects :ref:`False<test_what_is_false>` in both cases

* I add the third case - where the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 4

        def test_converse_non_implication(self):
            self.assertFalse(src.truth_table.converse_non_implication(True, True))
            self.assertFalse(src.truth_table.converse_non_implication(True, False))
            self.assertTrue(src.truth_table.converse_non_implication(False, True))

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

* I add an `if statement`_ to ``converse_non_implication`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2-4

    def converse_non_implication(first_input, second_input):
        if first_input == False:
            if second_input == True:
                return True
        return False

  the test passes. The ``converse_non_implication`` :ref:`function<what is a function?>` returns

  - :ref:`True<test_what_is_true>` when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`
  - :ref:`False<test_what_is_false>` in all other cases

* I add the next case - when the first and second inputs are both :ref:`False<test_what_is_false>`, to ``test_converse_non_implication`` in ``test_truth_table.py``

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 5

        def test_converse_non_implication(self):
            self.assertFalse(src.truth_table.converse_non_implication(True, True))
            self.assertFalse(src.truth_table.converse_non_implication(True, False))
            self.assertTrue(src.truth_table.converse_non_implication(False, True))
            self.assertFalse(src.truth_table.converse_non_implication(False, False))


    # Exceptions seen

  the test is still passing

* I use ``and`` also known as ``logical_conjunction`` to put the two `if statements`_ together in ``converse_non_implication`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2-4

    def converse_non_implication(first_input, second_input):
        if first_input == False and second_input == True:
        # if first_input == False:
        #    if second_input == True:
                return True
        return False

  the terminal_ still shows green

* I remove the commented lines then change the first line with :ref:`logical negation<test_logical_negation>` and bool_

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2-4

    def converse_non_implication(first_input, second_input):
        if not first_input == True and bool(second_input):
        # if first_input == False and second_input == True:
            return True
        return False

  still green

* I add an `else clause`_

  .. code-block:: python

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 5-6

    def converse_non_implication(first_input, second_input):
        if not first_input == True and bool(second_input):
        # if first_input == False and second_input == True:
            return True
        else:
            return False

  the test is still green

* I remove the comment and use bool_ with the first part of the `if statement`_ to make it simpler

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2-3

    def converse_non_implication(first_input, second_input):
        if not bool(first_input) and second_input:
        # if not first_input == True and bool(second_input):
            return True
        else:
            return False

  the test is still green

* I remove the commented line and make the `if statement`_ simpler

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2-3

    def converse_non_implication(first_input, second_input):
        if not first_input and second_input:
        # if not bool(first_input) and second_input:
            return True
        else:
            return False

  the terminal_ still shows green

* I use a `conditional expression`_

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2

    def converse_non_implication(first_input, second_input):
        return True if not first_input and second_input else False
        if not first_input and second_input:
            return True
        else:
            return False

  still green

* I remove the `if statements`_ then use the simpler `return statement`_

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2

    def converse_non_implication(first_input, second_input):
        return not first_input and second_input
        return True if not first_input and second_input else False

  all tests are still passing

* I remove the second `return statement`_

  .. code-block:: python
    :lineno-start: 29

    def converse_non_implication(first_input, second_input):
        return not first_input and second_input

:ref:`Converse NonImplication<test_converse_non_implication>` always returns

* ``not first_input and second_input``
* the :ref:`Logical Conjunction<test_logical_conjunction>` of the :ref:`Negation<test_logical_negation>` of the first input and the second input
* :ref:`True<test_what_is_true>` only when the first input is :ref:`False<test_what_is_false>` and the second input is :ref:`True<test_what_is_true>`

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_truth_table.py`` and ``truth_table.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_ and exit the tests with :kbd:`ctrl+c` on the keyboard
* I deactivate the `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    deactivate

  the terminal_ goes back to the command line, ``(.venv)`` is no longer on the left side

  .. code-block:: shell

    .../pumping_python/truth_table

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

* :ref:`Logical Conjunction <test_logical_conjunction>` is "and_"
* :ref:`Logical Negation <test_logical_negation>` is "not_"

All the logic statements or conditions have been written with some or all of the above 2.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed for the Truth Table?<truth table: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

:ref:`Would you like to test more binary operations? <binary_operations_ii>`

----


.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->