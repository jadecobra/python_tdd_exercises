.. meta::
  :description: Master Python truth tables for binary operations. This guide simplifies 'if' statements with clear, step-by-step Python code examples. Watch the tutorial!
  :keywords: Jacob Itegboje, python truth table for if statements, python truth table generator from expression, python logical operators truth table, python truth table for two variables, how to make a truth table in python, python contradiction function, python logical conjunction truth table

.. include:: ../../links.rst
.. _the Visual Studio Code Python Extension: `Python Extension`_

.. _binary_operations_1:

#################################################################################
truth table: Binary Operations 1
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/Q_jhE204MoE?si=m9_EvOX-4lrmSzo7" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

*********************************************************************************
preview
*********************************************************************************

Here are the tests I have at the end of this chapter

.. literalinclude:: ../../code/truth_table/tests/test_binary_i.py
  :language: python
  :linenos:

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
test_contradiction
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I make a new file_ in the tests_ folder_ named ``test_binary.py``

* I add a new TestCase_ to ``test_binary.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2, 5, 7-10, 13

    import src.truth_table
    import unittest


    class TestBinaryOperations(unittest.TestCase):

        def test_contradiction(self):
            self.assertFalse(
                src.truth_table.contradiction(True, True)
            )


    # Exceptions seen

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'contradiction'

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2
    :emphasize-text: AttributeError

    # Exceptions seen
    # AttributeError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I open ``truth_table.py`` in the :ref:`editor<2 editors>`

* I add a :ref:`function<what is a function?>` with the `return statement`_ of :ref:`logical_negation<test_logical_negation>` to ``truth_table.py``

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

  the :ref:`function<what is a function?>` only takes one input, but the test sent two

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 3
    :emphasize-text: TypeError

    # Exceptions seen
    # AttributeError
    # TypeError

* I add ``second_input`` as the second name in parentheses

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 1-2

    def contradiction(the_input, second_input):
        return not the_input

  the test passes

:ref:`contradiction<test_contradiction>` returns

* :ref:`False<test_what_is_false>`, if :ref:`True<test_what_is_true>` is the first input and if :ref:`True<test_what_is_true>` is the second input
* :ref:`False<test_what_is_false>`, which is the :ref:`opposite<test_logical_negation>` of the first input (:ref:`True<test_what_is_true>`) in this case

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change ``the_input`` to ``first_input`` as the name for the first input given when the :ref:`function<what is a function?>` is called by the test

  .. TIP:: In `Visual Studio Code`_ I can change all the places that a name is in the file_, with

    * Find and Replace - :kbd:`ctrl+H` (Windows_) or :kbd:`option+command+F` (MacOS_) on the keyboard
    * Rename Symbol - this needs `the Visual Studio Code Python Extension`_ to work

      - Right click on the name you want to change, for example ``the_input`` then select ``Rename Symbol`` or
      - Select the name you want to change then use :kbd:`F2` or :kbd:`Fn+F2` on your keyboard to rename it

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 1-
    :emphasize-text: first_input

    def contradiction(first_input, second_input):
        return not first_input

  the test is still green

* I add the second case in :ref:`test_contradiction` to ``test_binary.py``, this is when :ref:`True<test_what_is_true>` is the first input and :ref:`False<test_what_is_false>` is the second input

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 5-7

        def test_contradiction(self):
            self.assertFalse(
                src.truth_table.contradiction(True, True)
            )
            self.assertFalse(
                src.truth_table.contradiction(True, False)
            )

  the test is still green. :ref:`contradiction<test_contradiction>` returns

  - :ref:`False<test_what_is_false>`, if :ref:`True<test_what_is_true>` is the first input and :ref:`False<test_what_is_false>` is the second input
  - :ref:`False<test_what_is_false>`, if :ref:`True<test_what_is_true>` is the first input and :ref:`True<test_what_is_true>` is the second input
  - :ref:`False<test_what_is_false>`, which is the :ref:`opposite<test_logical_negation>` of the first input (:ref:`True<test_what_is_true>`) in these 2 cases

* I add the third case, which is when :ref:`False<test_what_is_false>` is the first input and :ref:`True<test_what_is_true>` is the second input

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 8-10


        def test_contradiction(self):
            self.assertFalse(
                src.truth_table.contradiction(True, True)
            )
            self.assertFalse(
                src.truth_table.contradiction(True, False)
            )
            self.assertFalse(
                src.truth_table.contradiction(False, True)
            )


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

  the 3 cases so far all expect :ref:`False<test_what_is_false>`

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 4
    :emphasize-text: AssertionError

    # Exceptions seen
    # AttributeError
    # TypeError
    # AssertionError

* I make :ref:`the contradiction function<test_contradiction>` return :ref:`False<test_what_is_false>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 2

    def contradiction(first_input, second_input):
        return False

  the test passes. :ref:`contradiction<test_contradiction>` returns

  - :ref:`False<test_what_is_False>`, if :ref:`False<test_what_is_false>` is the first input and :ref:`True<test_what_is_true>` is the second input
  - :ref:`False<test_what_is_false>`, if :ref:`True<test_what_is_true>` is the first input and :ref:`False<test_what_is_false>` is the second input
  - :ref:`False<test_what_is_false>`, if :ref:`True<test_what_is_true>` is the first input and :ref:`True<test_what_is_true>` is the second input

* I add the fourth case for when the two inputs are :ref:`False<test_what_is_false>` in :ref:`test_contradiction` to ``test_binary.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 11-13

        def test_contradiction(self):
            self.assertFalse(
                src.truth_table.contradiction(True, True)
            )
            self.assertFalse(
                src.truth_table.contradiction(True, False)
            )
            self.assertFalse(
                src.truth_table.contradiction(False, True)
            )
            self.assertFalse(
                src.truth_table.contradiction(False, False)
            )


    # Exceptions seen

  the test is still green!

:ref:`contradiction always returns False, it does not care about what it gets<test_contradiction>`

----

*********************************************************************************
test_logical_conjunction
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for the first case where the two inputs are :ref:`True<test_what_is_true>` for :ref:`logical_conjunction<test_logical_conjunction>` to ``test_binary.py``

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 15-18

      def test_contradiction(self):
          self.assertFalse(
              src.truth_table.contradiction(True, True)
          )
          self.assertFalse(
              src.truth_table.contradiction(True, False)
          )
          self.assertFalse(
              src.truth_table.contradiction(False, True)
          )
          self.assertFalse(
              src.truth_table.contradiction(False, False)
          )

      def test_logical_conjunction(self):
          self.assertTrue(
              src.truth_table.logical_conjunction(True, True)
          )


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'logical_conjunction'. Did you mean: 'logical_negation'?

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add the :ref:`function<what is a function?>` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 17
  :emphasize-lines: 5-6

  def contradiction(first_input, second_input):
      return False


  def logical_conjunction(first_input, second_input):
      return True

the test passes. :ref:`logical_conjunction<test_logical_conjunction>` returns :ref:`True<test_what_is_true>`, if :ref:`True<test_what_is_true>` is the first input and :ref:`True<test_what_is_true>` is the second input

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the next case - when :ref:`True<test_what_is_true>` is the first input and :ref:`False<test_what_is_false>` is the second input, to :ref:`test_logical_conjunction` in ``test_binary.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 5-7

        def test_logical_conjunction(self):
            self.assertTrue(
                src.truth_table.logical_conjunction(True, True)
            )
            self.assertFalse(
                src.truth_table.logical_conjunction(True, False)
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

* I make :ref:`the logical_conjunction function<test_logical_conjunction>` in ``truth_table.py`` return :ref:`False <test_what_is_false>`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2

    def logical_conjunction(first_input, second_input):
        return False

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

  the line that was passing before is now failing. :ref:`logical_conjunction<test_logical_conjunction>` has to make a choice. It should return

  - :ref:`False<test_what_is_false>`, if :ref:`True<test_what_is_true>` is the first input and :ref:`False<test_what_is_false>` is the second input
  - :ref:`True<test_what_is_true>`, if :ref:`True<test_what_is_true>` is the first input and :ref:`True<test_what_is_true>` is the second input
  - the second input in these 2 cases

* I change the `return statement`_ of :ref:`the logical_conjunction function<test_logical_conjunction>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2

    def logical_conjunction(first_input, second_input):
        return second_input

  the test passes

* I add the 3rd case where :ref:`False<test_what_is_false>` is the first input and :ref:`True<test_what_is_true>` is the second input to :ref:`test_logical_conjunction` in ``test_binary.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 8-10

        def test_logical_conjunction(self):
            self.assertTrue(
                src.truth_table.logical_conjunction(True, True)
            )
            self.assertFalse(
                src.truth_table.logical_conjunction(True, False)
            )
            self.assertFalse(
                src.truth_table.logical_conjunction(False, True)
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

  my solution does not work for this case. :ref:`logical_conjunction<test_logical_conjunction>` has to make a choice, it should return

  - :ref:`False<test_what_is_false>`, if :ref:`False<test_what_is_false>` is the first input and :ref:`True<test_what_is_true>` is the second input
  - :ref:`False<test_what_is_false>`, if :ref:`True<test_what_is_true>` is the first input and :ref:`False<test_what_is_false>` is the second input
  - :ref:`True<test_what_is_true>`, if :ref:`True<test_what_is_true>` is the first input and :ref:`True<test_what_is_true>` is the second input

  I can make it do that with `if statements`_

----

*********************************************************************************
if statements
*********************************************************************************

An `if statement`_ is a way for a program_ to choose what to do based on something else. I can use `if statements`_ to make a :ref:`function<what is a function?>` choose between 2 things, they are written this way

.. code-block:: python

  if something:
      then do this

* I add `if statements`_ for when :ref:`False<test_what_is_false>` is the first_input and :ref:`True<test_what_is_true>` is the second input to :ref:`the logical_conjunction function<test_logical_conjunction>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2-4

    def logical_conjunction(first_input, second_input):
        if first_input == False:
            if second_input == True:
                return False
        return second_input

  the test passes.

  - ``if first_input == False:`` checks if ``first_input`` is equal to :ref:`False<test_what_is_false>`

    * if ``first_input`` is equal to :ref:`False<test_what_is_false>`, it goes to the next line ``if second_input == True:``
    * if ``first_input`` is NOT equal to :ref:`False<test_what_is_false>`, it leaves the `if statement`_ and continues to run the rest of the :ref:`function<what is a function?>` - ``return second_input``

  - ``if second_input == True:`` checks if ``second_input`` is equal to :ref:`True<test_what_is_true>`

    * if ``second_input`` is equal to :ref:`True<test_what_is_true>`, it goes to the next line ``return False``, it returns :ref:`False<test_what_is_false>` and leaves the :ref:`function<what is a function?>` because :ref:`the return statement is the last thing to run in a function<test_what_happens_after_a_function_returns>`
    * if ``second_input`` is NOT equal to :ref:`True<test_what_is_true>`, it leaves the `if statement`_ and continues to run the rest of the :ref:`function<what is a function?>` - ``return second_input``

  :ref:`logical_conjunction<test_logical_conjunction>` returns

  - :ref:`False<test_what_is_false>`, if :ref:`False<test_what_is_false>` is the first input and :ref:`True<test_what_is_true>` is the second input
  - :ref:`False<test_what_is_false>`, if :ref:`True<test_what_is_true>` is the first input and :ref:`False<test_what_is_false>` is the second input
  - :ref:`True<test_what_is_true>`, if :ref:`True<test_what_is_true>` is the first input and :ref:`True<test_what_is_true>` is the second input

* I add the last case, which is when the two inputs are :ref:`False<test_what_is_false>`, to :ref:`test_logical_conjunction` in ``test_binary.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 11-13

    def test_logical_conjunction(self):
            self.assertTrue(
                src.truth_table.logical_conjunction(True, True)
            )
            self.assertFalse(
                src.truth_table.logical_conjunction(True, False)
            )
            self.assertFalse(
                src.truth_table.logical_conjunction(False, True)
            )
            self.assertFalse(
                src.truth_table.logical_conjunction(False, False)
            )


    # Exceptions seen

  the test is still green.   :ref:`logical_conjunction<test_logical_conjunction>` returns

  - :ref:`False<test_what_is_false>`, if :ref:`False<test_what_is_false>` is the first input and :ref:`False<test_what_is_false>` is the second input
  - :ref:`False<test_what_is_false>`, if :ref:`False<test_what_is_false>` is the first input and :ref:`True<test_what_is_true>` is the second input
  - :ref:`False<test_what_is_false>`, if :ref:`True<test_what_is_true>` is the first input and :ref:`False<test_what_is_false>` is the second input
  - :ref:`True<test_what_is_true>`, if :ref:`True<test_what_is_true>` is the first input and :ref:`True<test_what_is_true>` is the second input
  - it only returns :ref:`True<test_what_is_true>` for the case where the two inputs are :ref:`True<test_what_is_true>`

* I add an `if statement`_ for the case where :ref:`logical_conjunction<test_logical_conjunction>` returns :ref:`True<test_what_is_true>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2-4

    def logical_conjunction(first_input, second_input):
        if first_input == True:
            if second_input == True:
                return True
        if first_input == False:
            if second_input == True:
                return False
        return second_input

  still green

  - ``if first_input == True:`` checks if ``first_input`` is equal to :ref:`True<test_what_is_true>`

    * if ``first_input`` is equal to :ref:`True<test_what_is_true>`, it goes to the next line ``if second_input == True:``
    * if ``first_input`` is NOT equal to :ref:`True<test_what_is_true>`, it leaves this `if statement`_ and continues to ``if first_input == False:``, it will never go to ``if second_input == True:``

  - ``if second_input == True:`` checks if ``second_input`` is equal to :ref:`True<test_what_is_true>`

    * if ``second_input`` is equal to :ref:`True<test_what_is_true>`, it goes to the next line ``return True``, it returns :ref:`False<test_what_is_false>` and leaves the :ref:`function<what is a function?>` because :ref:`the return statement is the last thing to run in a function<test_what_happens_after_a_function_returns>`
    * if ``second_input`` is NOT equal to :ref:`True<test_what_is_true>`, it leaves this `if statement`_ and continues to ``if first_input == False:``

  Since there is only one case where the :ref:`function<what is a function?>` returns :ref:`True<test_what_is_true>`, I do not need any other statements

* I remove the other `if statements`_

  .. code-block:: python
    :lineno-start: 21

    def logical_conjunction(first_input, second_input):
        if first_input == True:
            if second_input == True:
                return True

  the test is still green because :ref:`all functions return None by default, as if they have an invisible line that says return None<test_making_a_function_w_return_none>`

* I add a `return statement`_ to make it clearer

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 5

    def logical_conjunction(first_input, second_input):
        if first_input == True:
            if second_input == True:
                return True
        return None

  still green because :ref:`None is False<is None False or True?>`

* I change the `return statement`_ to use :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 5

    def logical_conjunction(first_input, second_input):
        if first_input == True:
            if second_input == True:
                return True
        return False

  green

* I can put two `if statements`_ together when one is indented under the other. For example

  .. code-block:: python

    if something:
        if something_else:

  can also be written as

  .. code-block:: python

    if something and something_else:

  I put the two `if statements`_ for the one case where the result is :ref:`True <test_what_is_true>` together and use an `else clause`_ for the other cases where the first and second inputs are NOT both :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2-5

    def logical_conjunction(first_input, second_input):
        if first_input == True and second_input == True:
            return True
        else:
            return False
        if first_input == True:
            if second_input == True:
                return True
        return False

  the test is still green

* I remove the other statements after the first ``return False``

* I can use bool_ in the `if statement`_

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2-3

    def logical_conjunction(first_input, second_input):
        # if first_input == True and second_input == True:
        if bool(first_input) == True and bool(second_input) == True:
            return True
        else:
            return False

  still green

  .. NOTE::

    ``bool(anything)`` returns :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>` for the thing in parentheses like the tests in :ref:`the booleans chapter<what are booleans?>` with the assertFalse_ and assertTrue_ :ref:`methods<what is a function?>`

* I remove the commented line

* Since ``bool(True)`` is the same as :ref:`True<test_what_is_true>`, ``bool(first_input) == True`` is the same thing as ``True == True``, which is a repetition. I remove ``== True`` from the `if statement`_

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2-3

    def logical_conjunction(first_input, second_input):
        # if bool(first_input) == True and bool(second_input) == True:
        if bool(first_input) and bool(second_input):
            return True
        else:
            return False

  green

  .. NOTE::

    ``if bool(anything)`` checks if ``bool(anything)`` returns :ref:`True <test_what_is_true>`

* I remove the commented line then change the first line to make it simpler

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2-3

    def logical_conjunction(first_input, second_input):
        # if bool(first_input) and bool(second_input):
        if first_input and second_input:
            return True
        else:
            return False

  still green

.. NOTE::

  these `if statements`_ have the same result

  - ``if something == True:`` - checks if ``something`` is equal to :ref:`True<test_what_is_true>`

  these check if ``bool(something) == True:`` the same way the `assertTrue method`_ does

  - ``if bool(something) == True:``
  - ``if bool(something):``
  - ``if something:``

----

*********************************************************************************
conditional expressions
*********************************************************************************

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

  the test is still green

* I remove the other statements then change the `return statement`_ to a simpler form

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2

    def logical_conjunction(first_input, second_input):
        return first_input and second_input
        return True if first_input and second_input else False

  still green!

* I remove the second `return statement`_ because :ref:`the return statement is the last thing to run in a function<test_what_happens_after_a_function_returns>`

  .. code-block:: python
    :lineno-start: 21

    def logical_conjunction(first_input, second_input):
        return first_input and second_input

:ref:`Logical Conjunction<test_logical_conjunction>` also known as and_, always returns

* ``first_input and second_input``
* :ref:`True<test_what_is_true>`, if the first input is :ref:`True<test_what_is_true>` and the second input is :ref:`True<test_what_is_true>`

.. NOTE::

  All of the statements below have the same result

  * this checks if ``something`` is equal :ref:`True<test_what_is_true>`

    .. code-block:: python

      if something == True:
          return True
      else:
          return False

  * this uses bool_ to get the :ref:`boolean<what are booleans?>` of ``something`` then checks if the result is equal to :ref:`True<test_what_is_true>`

    .. code-block:: python

      if bool(something) == True:
          return True
      else:
          return False

  * this checks if the result of ``bool(something)`` is :ref:`True<test_what_is_true>` in the background

    .. code-block:: python

      if bool(something):
          return True
      else:
          return False

  * this also checks if the result of ``bool(something)`` is :ref:`True<test_what_is_true>` in the background

    .. code-block:: python

      if something:
          return True
      else:
          return False

  * this returns :ref:`True<test_what_is_true>` if the result of  ``bool(something)`` is :ref:`True<test_what_is_true>`

    .. code-block:: python

      return True if something else False

  * this also returns :ref:`True<test_what_is_true>` if the result of ``bool(something)`` is :ref:`True<test_what_is_true>` in the background

    .. code-block:: python

      return something

    it works because Python_ checks if the result of ``bool(something)`` is :ref:`True<test_what_is_true>` in the background same as it does when I use ``if something:``

----

*********************************************************************************
test_project_second
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for another Binary Operation to ``test_binary.py``

.. code-block:: python
  :lineno-start: 21
  :emphasize-lines: 15-18

      def test_logical_conjunction(self):
          self.assertTrue(
              src.truth_table.logical_conjunction(True, True)
          )
          self.assertFalse(
              src.truth_table.logical_conjunction(True, False)
          )
          self.assertFalse(
              src.truth_table.logical_conjunction(False, True)
          )
          self.assertFalse(
              src.truth_table.logical_conjunction(False, False)
          )

      def test_project_second(self):
          self.assertTrue(
              src.truth_table.project_second(True, True)
          )


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'project_second'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add the :ref:`function<what is a function?>` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 21
  :emphasize-lines: 5-6

  def logical_conjunction(first_input, second_input):
      return first_input and second_input


  def project_second(first_input, second_input):
      return True

the test passes.

:ref:`project_second<test_project_second>` returns :ref:`True<test_what_is_true>`, if :ref:`True<test_what_is_true>` is the first input and :ref:`True<test_what_is_true>` is the second input. So far this is the same as :ref:`logical_conjunction<test_logical_conjunction>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the second case - when :ref:`True<test_what_is_true>` is the first input and :ref:`False<test_what_is_false>` is the second input, to :ref:`test_project_second` in ``test_binary.py``

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 5-7

        def test_project_second(self):
            self.assertTrue(
                src.truth_table.project_second(True, True)
            )
            self.assertFalse(
                src.truth_table.project_second(True, False)
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

  the test expects

  - :ref:`False<test_what_is_false>`, if :ref:`True<test_what_is_true>` is the first input and :ref:`False<test_what_is_false>` is the second input
  - :ref:`True<test_what_is_true>`, if :ref:`True<test_what_is_true>` is the first input and :ref:`True<test_what_is_true>` is the second input
  - the second input in both cases
  - still the same as :ref:`logical_conjunction<test_logical_conjunction>`

* I make :ref:`project_second<test_project_second>` return ``second_input`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 2

    def project_second(first_input, second_input):
        return second_input

  the test passes

* I add the next case, which is when :ref:`False<test_what_is_false>` is the first input and :ref:`True<test_what_is_true>` is the second input for :ref:`test_project_second` in ``test_binary.py``

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 8-10

        def test_project_second(self):
            self.assertTrue(
                src.truth_table.project_second(True, True)
            )
            self.assertFalse(
                src.truth_table.project_second(True, False)
            )
            self.assertTrue(
                src.truth_table.project_second(False, True)
            )

  the test is still green. :ref:`project_second<test_project_second>` returns

  - :ref:`True<test_what_is_true>`, if :ref:`False<test_what_is_false>` is the first input and :ref:`True<test_what_is_true>` is the second input
  - :ref:`False<test_what_is_false>`, if :ref:`True<test_what_is_true>` is the first input and :ref:`False<test_what_is_false>` is the second input
  - :ref:`True<test_what_is_true>`, if :ref:`True<test_what_is_true>` is the first input and :ref:`True<test_what_is_true>` is the second input
  - the second input in all 3 cases

* I add the last case - when the two inputs are :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 11-13

        def test_project_second(self):
            self.assertTrue(
                src.truth_table.project_second(True, True)
            )
            self.assertFalse(
                src.truth_table.project_second(True, False)
            )
            self.assertTrue(
                src.truth_table.project_second(False, True)
            )
            self.assertFalse(
                src.truth_table.project_second(False, False)
            )


    # Exceptions seen

  still green

:ref:`project_second<test_project_second>` returns

* :ref:`False<test_what_is_false>`, if :ref:`False<test_what_is_false>` is the first input and :ref:`False<test_what_is_false>` is the second_input
* :ref:`True<test_what_is_true>`, if :ref:`False<test_what_is_false>` is the first input and :ref:`True<test_what_is_true>` is the second input
* :ref:`False<test_what_is_false>`, if :ref:`True<test_what_is_true>` is the first input and :ref:`False<test_what_is_false>` is the second input
* :ref:`True<test_what_is_true>`, if :ref:`True<test_what_is_true>` is the first input and :ref:`True<test_what_is_true>` is the second input
* the second input in all cases, it does not care about the first input
----

*********************************************************************************
test_converse_non_implication
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for :ref:`converse_non_implication<test_converse_non_implication>` to ``test_binary.py``

.. code-block:: python
  :lineno-start: 35
  :emphasize-lines: 15-18

      def test_project_second(self):
          self.assertTrue(
              src.truth_table.project_second(True, True)
          )
          self.assertFalse(
              src.truth_table.project_second(True, False)
          )
          self.assertTrue(
              src.truth_table.project_second(False, True)
          )
          self.assertFalse(
              src.truth_table.project_second(False, False)
          )

      def test_converse_non_implication(self):
          self.assertFalse(
              src.truth_table.converse_non_implication(True, True)
          )


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'converse_non_implication'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add the :ref:`function<what is a function?>` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 25
  :emphasize-lines: 5-6

  def project_second(first_input, second_input):
      return second_input


  def converse_non_implication(first_input, second_input):
      return False

the test passes. :ref:`converse_non_implication<test_converse_non_implication>` returns :ref:`False<test_what_is_false>`, if :ref:`True<test_what_is_true>` is the first input and :ref:`True<test_what_is_true>` is the second input

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the next case - when :ref:`True<test_what_is_true>` is the first input and :ref:`False<test_what_is_false>` is the second input to :ref:`test_converse_non_implication` in ``test_binary.py``

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 5-7

        def test_converse_non_implication(self):
            self.assertFalse(
                src.truth_table.converse_non_implication(True, True)
            )
            self.assertFalse(
                src.truth_table.converse_non_implication(True, False)
            )

  the test is still green because it expects :ref:`False<test_what_is_false>` in both cases

* I add the third case - when :ref:`False<test_what_is_false>` is the first input and :ref:`True<test_what_is_true>` is the second input

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 8-10

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

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

  the test expects

  - :ref:`True<test_what_is_true>`, if :ref:`False<test_what_is_false>` is the first input and :ref:`True<test_what_is_true>` is the second input
  - :ref:`False<test_what_is_false>`, if :ref:`True<test_what_is_true>` is the first input and :ref:`False<test_what_is_false>` is the second input
  - :ref:`False<test_what_is_false>`, if :ref:`True<test_what_is_true>` is the first input and :ref:`True<test_what_is_true>` is the second input

* I add an `if statement`_ for this case to :ref:`converse_non_implication<test_converse_non_implication>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2-4

    def converse_non_implication(first_input, second_input):
        if first_input == False:
            if second_input == True:
                return True
        return False

  the test passes

* I add the next case - when the first and second inputs are both :ref:`False<test_what_is_false>`, to :ref:`test_converse_non_implication` in ``test_binary.py``

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 11-13

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


    # Exceptions seen

  the test is still green. :ref:`converse_non_implication<test_converse_non_implication>` returns

  - :ref:`False<test_what_is_false>`, if :ref:`False<test_what_is_false>` is the first input and :ref:`False<test_what_is_false>` is the second input
  - :ref:`True<test_what_is_true>`, if :ref:`False<test_what_is_false>` is the first input and :ref:`True<test_what_is_true>` is the second input
  - :ref:`False<test_what_is_false>`, if :ref:`True<test_what_is_true>` is the first input and :ref:`False<test_what_is_false>` is the second input
  - :ref:`False<test_what_is_false>`, if :ref:`True<test_what_is_true>` is the first input and :ref:`True<test_what_is_true>` is the second input

  there is only one case where :ref:`converse_non_implication<test_converse_non_implication>` returns :ref:`True<test_what_is_true>`

* I use and_ to put the two `if statements`_ together in :ref:`converse_non_implication<test_converse_non_implication>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2-6

    def converse_non_implication(first_input, second_input):
        # if first_input == False:
        #     if second_input == True:
        #         return True
        if first_input == False and second_input == True:
            return True
        return False

  still green

* I remove the comments and use not_ to write the `if statement`_ in relation to :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2-3

    def converse_non_implication(first_input, second_input):
        # if first_input == False and second_input == True:
        if not first_input == True and second_input == True:
            return True
        return False

  green

* I remove the commented line and use bool_

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2-3

    def converse_non_implication(first_input, second_input):
        # if not first_input == True and second_input == True:
        if not bool(first_input) == True and bool(second_input) == True:
            return True
        return False

  still green

* I remove the comment and the repeated ``== True``

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2-3

    def converse_non_implication(first_input, second_input):
        # if not bool(first_input) == True and bool(second_input) == True:
        if not bool(first_input) and bool(second_input):
            return True
        return False

  the test is still green

* I remove the comment and bool_

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2-3

    def converse_non_implication(first_input, second_input):
        # if not bool(first_input) and bool(second_input):
        if not first_input and second_input:
            return True
        return False

  still green

* I remove the comment then add an `else clause`_

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 4-5

    def converse_non_implication(first_input, second_input):
        if not first_input and second_input:
            return True
        else:
            return False

  green

  .. NOTE::

    - ``if not first_input`` returns the :ref:`opposite or Logical Negation<test_logical_negation>` of ``first_input``

      * if :ref:`True<test_what_is_true>` is the first input, this part of the statement is :ref:`False<test_what_is_false>`
      * if :ref:`False<test_what_is_false>` is the first input, this part of the statement is :ref:`True<test_what_is_true>`

    this means that in the 4 cases with the statement ``if not first_input and second_input``

    - if :ref:`True<test_what_is_true>` is the first input and :ref:`True<test_what_is_true>` is the second input, the statement is

      * ``if not True and True:`` which is
      * ``if False and True:`` which is
      * :ref:`False<test_what_is_false>` because of the result of the third case for :ref:`Logical Conjunction<test_logical_conjunction>` this means that
      * ``converse_non_implication(True, True)`` is the same as ``logical_conjunction(False, True)``

    - if :ref:`True<test_what_is_true>` is the first input and :ref:`False<test_what_is_false>` is the second input, the statement is

      * ``if not True and False:`` which is
      * ``if False and False:`` which is
      * :ref:`False<test_what_is_false>` because of the result of the fourth case for :ref:`Logical Conjunction<test_logical_conjunction>` this means that
      * ``converse_non_implication(True, False)`` is the same as ``logical_conjunction(False, False)``

    - if :ref:`False<test_what_is_false>` is the first input and :ref:`True<test_what_is_true>` is the second input, the statement is

      * ``if not False and True:`` which is
      * ``if True and True:`` which is
      * :ref:`True<test_what_is_true>` because of the result of the first case for :ref:`Logical Conjunction<test_logical_conjunction>` this means that
      * ``converse_non_implication(False, True)`` is the same as ``logical_conjunction(True, True)``

    - if :ref:`False<test_what_is_false>` is the first input and :ref:`False<test_what_is_false>` is the second input, the statement is

      * ``if not False and False:`` which is
      * ``if True and False:`` which is
      * :ref:`False<test_what_is_false>` because of the result of the second case for :ref:`Logical Conjunction<test_logical_conjunction>` this means that
      * ``converse_non_implication(False, False)`` is the same as ``logical_conjunction(True, False)``

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

* I remove the other statements then use the simpler `return statement`_

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

* I add a `return statement`_

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2

    def converse_non_implication(first_input, second_input):
        return logical_conjunction(not first_input, second_input)
        return not first_input and second_input

  the test is still green

:ref:`Converse NonImplication<test_converse_non_implication>` always returns

* ``not first_input and second_input``
* the :ref:`Logical Conjunction<test_logical_conjunction>` of the :ref:`Negation<test_logical_negation>` of the first input, and the second input
* :ref:`True<test_what_is_true>`, only if :ref:`False<test_what_is_false>` is the first input and :ref:`True<test_what_is_true>` is the second input

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

Binary Operations take 2 inputs, each input can be :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`, if the first input is named ``first_input`` and the second input is named ``second_input``, the tests show that

* :ref:`Converse NonImplication <test_converse_non_implication>`

  - returns ``not first_input and second_input``
  - returns :ref:`True<test_what_is_true>` when ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`
  - is the :ref:`Logical Conjunction<test_logical_conjunction>` of the :ref:`Logical Negation<test_logical_negation>` of ``first_input``, and ``second_input``
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
  - is the :ref:`opposite or Logical Negation<test_logical_negation>` of :ref:`Tautology<test_tautology>` which always returns :ref:`True<test_what_is_true>`

and

* :ref:`Logical Conjunction <test_logical_conjunction>` is "and_"
* :ref:`Logical Negation <test_logical_negation>` is "not_"

All the logic statements or conditions have been written with some or all of these 2.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed for the Truth Table?<truth table: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

:ref:`Would you like to test more binary operations? <binary_operations_1i>`

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->