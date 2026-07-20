.. meta::
  :description: Truth table Binary Operations 1 in Python for beginners using TDD in the truth_table project. Create tests/test_binary.py (touch/New-Item) and implement the first four of sixteen binary operations—contradiction (always False), logical_conjunction (AND: first and second), project_second (returns second input), converse_non_implication (not first and second)—each tested with four assertTrue/assertFalse pairs for TT/TF/FT/FF inputs. Red-Green-Refactor through AttributeError module has no attribute, TypeError takes 0 positional arguments but 2 were given, AssertionError True is not false and False is not true. Learn if statements, nested if vs the and operator, conditional expressions (ternary operator), and bool() truthy/falsy refactoring. Real-world examples: broken light switch, voting eligibility, MFA password+code login, discount for new customer with coupon. Preview test_binary_1.py. Requires Nullary and Unary Operations. Jacob Itegboje Pumping Python.
  :keywords: Jacob Itegboje, Pumping Python, truth table Binary Operations 1, python binary operations tutorial, test_binary_1.py, contradiction always False, logical_conjunction AND first and second, project_second returns second input, converse_non_implication not first and second, TDD red green refactor truth table, AttributeError module has no attribute contradiction, TypeError takes 0 positional arguments but 2 were given, AssertionError True is not false, AssertionError False is not true, python if statement nested if, python and operator vs nested if, conditional expression ternary operator, bool truthy falsy refactor, assertTrue assertFalse four input combinations, broken light switch logic, voting eligibility truth table, MFA multi-factor authentication logic, new customer coupon discount rule, programming truth tables beginners, boolean logic gates python unittest

.. include:: ../../links.rst
.. _if statement: https://docs.python.org/3/tutorial/controlflow.html#if-statements
.. _if statements: `if statement`_
.. _conditional expression: https://docs.python.org/3/reference/expressions.html#conditional-expressions
.. _conditional expressions: `conditional expression`_
.. _ternary operator: `conditional expression`_
.. _ternary operators: `conditional expression`_

.. _binary_operations_1:

#################################################################################
truth table: Binary Operations 1
#################################################################################

----

*********************************************************************************
preview
*********************************************************************************

These are the tests I have at the end of the chapter

.. literalinclude:: ../../code/truth_table/tests/test_binary_1.py
  :language: python
  :linenos:
  :caption: truth_table/tests/test_binary.py
  :lines: 1-21

.. literalinclude:: ../../code/truth_table/tests/test_binary_1.py
  :language: python
  :lineno-start: 23
  :caption: truth_table/tests/test_binary.py
  :lines: 23-

----

*********************************************************************************
questions about Binary Operations 1
*********************************************************************************

Questions to think about as I go through the chapter

* :ref:`how many inputs do binary operations take?<truth table: Binary Operations>`
* :ref:`what is contradiction?<test_contradiction>`
* :ref:`what is and?<test_logical_conjunction>`
* :ref:`what is an if statement?<if statements>`
* :ref:`what is a conditional expression?<conditional expressions>`
* :ref:`what is a ternary operator?<conditional expressions>`

----

*********************************************************************************
requirements
*********************************************************************************

:ref:`truth table: Nullary and Unary Operations`

*********************************************************************************
open the project
*********************************************************************************

* Make sure you are in the ``pumping_python`` folder_ with pwd_ in the terminal_

  .. code-block:: shell
    :emphasize-lines: 1

    pwd

  if the terminal_ does not show

  .. code-block:: shell

    .../pumping_python

  `change directory`_ to the ``pumping_python`` folder

* Once in ``pumping_python``, `change directory`_ to the project

  .. code-block:: shell
    :emphasize-lines: 1

    cd truth_table

* I use touch_ to make a new :ref:`Python file<what is a module?>` named ``test_binary.py`` in the ``tests`` directory_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 1

        touch tests/test_binary.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        New-Item tests/test_binary.py

* I add ``test_binary.py`` to git_ for tracking

  .. code-block:: python
    :emphasize-lines: 1

    git add tests/test_binary.py

* I open ``test_binary.py`` from the ``tests`` folder_

* I run the tests with `pytest-watcher`_

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

* the terminal_ is my friend, and shows

  .. code-block:: shell

    rootdir: .../pumping_python/truth_table
    configfile: pyproject.toml
    collected 4 items

    tests/test_nullary_unary.py ....                  [100%]

    ================== 4 passed in G.HIs ===================

----

*********************************************************************************
test_contradiction
*********************************************************************************

The :ref:`truth table` for :ref:`contradiction<test_contradiction>` is

==============  ============== ==============
first input     second input   return
==============  ============== ==============
:green:`True`   :green:`True`  :red:`False`
:green:`True`   :red:`False`   :red:`False`
:red:`False`    :green:`True`  :red:`False`
:red:`False`    :red:`False`   :red:`False`
==============  ============== ==============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a test for :ref:`contradiction<test_contradiction>` with an :ref:`assertion<what is an assertion?>` for when the first input is :green:`True` and the second input is :green:`True`, in ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :red:`False`
  ==============  ============== ==============

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

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table'
                    has no attribute 'contradiction'

  because I have not :ref:`defined<how to make a function>` :ref:`contradiction<test_contradiction>` in ``truth_table.py``

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

* I open ``truth_table.py`` from the ``src`` folder_

* I add ``contradiction`` to ``truth_table.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 5-6

    def logical_negation(the_input):
        return not the_input


    def contradiction():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: contradiction() takes
               0 positional arguments but 2 were given

  because the test called the :ref:`contradiction function<test_contradiction>` with two arguments (:green:`True` and :green:`True`) and the :ref:`definition<how to make a function>` does not allow any arguments (the parentheses are empty).

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` , in ``test_binary.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 3
    :emphasize-text: TypeError

    # Exceptions seen
    # AttributeError
    # TypeError

* I add ``first_input`` as the name of the first argument in the :ref:`function signature<how to make a function>` for :ref:`contradiction<test_contradiction>`, in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 1-2

    # def contradiction():
    def contradiction(first_input):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: contradiction() takes
               1 positional argument but 2 were given

  because the test called the :ref:`contradiction function<test_contradiction>` with two arguments (:green:`True` and :green:`True`) and I just changed the :ref:`definition<how to make a function>` to only allow calls with one argument.

* I add ``second_input`` as the name of the second input in parentheses

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 3-4

    # def contradiction():
    # def contradiction(first_input):
    def contradiction(first_input, second_input):
        return None

  the test passes because :ref:`None is grouped as False  (the result of bool(None) is False)<test_is_none_falsy_or_truthy>` and the :ref:`assertion<what is an assertion?>` expects :red:`False`.

  .. code-block:: python

    contradiction(True, True) -> None

  Using substitution since :ref:`I can treat a call to a function as the object it returns<test_what_happens_after_functions_return>`

  .. code-block:: python


    assertFalse(src.truth_table.contradiction(True, True))
    assertFalse(None                                     )
    assertFalse(bool(None)                               )
    assertFalse(False                                    )

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the :ref:`return statement<the return statement>` to make it clearer

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 4-5

    # def contradiction():
    # def contradiction(first_input):
    def contradiction(first_input, second_input):
        # return None
        return False

  the test is still green. :ref:`contradiction<test_contradiction>` returns :red:`False`, if the first input is :green:`True` and the second input is :green:`True`.

* I remove the commented lines from ``contradiction``

  .. code-block:: python
    :lineno-start: 13

    def logical_negation(the_input):
        return not the_input


    def contradiction(first_input, second_input):
        return False

* I add an :ref:`assertion<what is an assertion?>` for the second case, which is if the first input is :green:`True` and the second input is :red:`False`, to ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :red:`False`   :red:`False`
  ==============  ============== ==============

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


    # Exceptions seen

  the test is still green. :ref:`contradiction<test_contradiction>` returns :red:`False`

  - if the first input is :green:`True` and the second input is :red:`False`
  - if the first input is :green:`True` and the second input is :green:`True`
  - if the first input is :green:`True`

  .. code-block:: python

    contradiction(True, False) -> False
    contradiction(True, True ) -> False

* I add an :ref:`assertion<what is an assertion?>` for the third case, which is if the first input is :red:`False` and the second input is :green:`True`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :green:`True`  :red:`False`
  ==============  ============== ==============

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

  the test is still green. :ref:`contradiction<test_contradiction>` returns :red:`False`

  - if the first input is :red:`False` and the second input is :green:`True`
  - if the first input is :green:`True`

  .. code-block:: python

    contradiction(False, True ) -> False
    contradiction(True , False) -> False
    contradiction(True , True ) -> False

* I add an :ref:`assertion<what is an assertion?>` for the fourth case, which is if the first input is :red:`False` and the second input is :red:`False`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :red:`False`   :red:`False`
  ==============  ============== ==============

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

  the test is still green. :ref:`contradiction<test_contradiction>` returns :red:`False`

  - if the first input is :red:`False`
  - if the first input is :green:`True`

  .. code-block:: python

    contradiction(False, False) -> False
    contradiction(False, True ) -> False
    contradiction(True , False) -> False
    contradiction(True , True ) -> False

* I add a :ref:`variable<what is a variable?>` for ``src.truth_table.contradiction``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2

        def test_contradiction(self):
            contradiction = src.truth_table.contradiction
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

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``src.truth_table.contradiction``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4-5, 8-9, 12-13, 16-17

        def test_contradiction(self):
            contradiction = src.truth_table.contradiction
            self.assertFalse(
                # src.truth_table.contradiction(True, True)
                contradiction(True, True)
            )
            self.assertFalse(
                # src.truth_table.contradiction(True, False)
                contradiction(True, False)
            )
            self.assertFalse(
                # src.truth_table.contradiction(False, True)
                contradiction(False, True)
            )
            self.assertFalse(
                # src.truth_table.contradiction(False, False)
                contradiction(False, False)
            )


    # Exceptions seen

  the test is still green.

* I remove the commented lines from :ref:`test_contradiction`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 3-6

        def test_contradiction(self):
            contradiction = src.truth_table.contradiction
            self.assertFalse(contradiction(True, True))
            self.assertFalse(contradiction(True, False))
            self.assertFalse(contradiction(False, True))
            self.assertFalse(contradiction(False, False))


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add contradiction'

:ref:`contradiction always returns False, it does not care about the inputs<test_contradiction>`

----

=================================================================================
examples of Contradiction
=================================================================================

----

* A broken light switch, if the inputs are

  - is the switch on?
  - is there electricity?

  If the switch is broken, the inputs do not matter

  ==============  ============== ==============
  switch          electricity    bulb
  ==============  ============== ==============
  :green:`on`     :green:`on`    :red:`off`
  :green:`on`     :red:`off`     :red:`off`
  :red:`off`      :green:`on`    :red:`off`
  :red:`off`      :red:`off`     :red:`off`
  ==============  ============== ==============

* A rule that does not allow watching TV, if the inputs are

  - is homework done?
  - is the room clean?

  the rule does not take the inputs into consideration

  ==============  ============== ==============
  homework done   clean room     can watch TV
  ==============  ============== ==============
  :green:`yes`    :green:`yes`   :red:`no`
  :green:`yes`    :red:`no`      :red:`no`
  :red:`no`       :green:`yes`   :red:`no`
  :red:`no`       :red:`no`      :red:`no`
  ==============  ============== ==============

* A rule about loaning money to friends, if the inputs are

  - person can be trusted?
  - is a small amount?

  ==============  ============== ====================
  trusted person  small amount   loan money to friend
  ==============  ============== ====================
  :green:`yes`    :green:`yes`   :red:`no`
  :green:`yes`    :red:`no`      :red:`no`
  :red:`no`       :green:`yes`   :red:`no`
  :red:`no`       :red:`no`      :red:`no`
  ==============  ============== ====================

* Do not disturb, if the inputs are

  - is the person in favorites list?
  - is it during allowed hours?

  ==============  ============== ====================
  favorites       allowed hours  allow to ring
  ==============  ============== ====================
  :green:`yes`    :green:`yes`   :red:`no`
  :green:`yes`    :red:`no`      :red:`no`
  :red:`no`       :green:`yes`   :red:`no`
  :red:`no`       :red:`no`      :red:`no`
  ==============  ============== ====================

* Broken Multi Factor Authentication to log in, if the inputs are

  - did the user provide the right password?
  - did the user provide the right MFA code?

  ==============  ============== ==============
  right password  right MFA code log in
  ==============  ============== ==============
  :green:`yes`    :green:`yes`   :red:`no`
  :green:`yes`    :red:`no`      :red:`no`
  :red:`no`       :green:`yes`   :red:`no`
  :red:`no`       :red:`no`      :red:`no`
  ==============  ============== ==============

----

*********************************************************************************
test_logical_conjunction
*********************************************************************************

The :ref:`truth table` for :ref:`logical_conjunction<test_logical_conjunction>` is

==============  ============== ==============
first input     second input   return
==============  ============== ==============
:green:`True`   :green:`True`  :green:`True`
:green:`True`   :red:`False`   :red:`False`
:red:`False`    :green:`True`  :red:`False`
:red:`False`    :red:`False`   :red:`False`
==============  ============== ==============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test for :ref:`logical_conjunction<test_logical_conjunction>` with an :ref:`assertion<what is an assertion?>` for the first case, which is if the first input is :green:`True` and the second input is :green:`True`, in ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 3-6

            self.assertFalse(contradiction(False, False))

        def test_logical_conjunction(self):
            self.assertTrue(
                src.truth_table.logical_conjunction(True, True)
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table'
                    has no attribute 'logical_conjunction'.
                    Did you mean: 'logical_negation'?

  because there is nothing named :ref:`logical_conjunction<test_logical_conjunction>` in ``truth_table.py``, yet.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``logical_conjunction`` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 17
  :emphasize-lines: 5-6

  def contradiction(first_input, second_input):
      return False


  def logical_conjunction(first_input, second_input):
      return True

the test passes. :ref:`logical_conjunction<test_logical_conjunction>` returns :green:`True`, if the first input is :green:`True` and the second input is :green:`True`.

.. code-block:: python

  logical_conjunction(True , True ) -> True

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for the next case, which is if the first input is :green:`True` and the second input is :red:`False`, to :ref:`test_logical_conjunction` in ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :red:`False`   :red:`False`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 7-11

        def test_logical_conjunction(self):
            self.assertTrue(
                src.truth_table.logical_conjunction(
                    True, True
                )
            )
            self.assertFalse(
                src.truth_table.logical_conjunction(
                    True, False
                )
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  because the :ref:`function<what is a function?>` returns :green:`True` and the :ref:`assertion<what is an assertion?>` expects :red:`False`. Using substitution since :ref:`I can treat a call to a function as the object it returns<test_what_happens_after_functions_return>`

  .. code-block:: python


    assertFalse(src.truth_table.logical_conjunction(True, False))
    assertFalse(True                                            )

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen, in ``test_binary.py``

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 4
    :emphasize-text: AssertionError

    # Exceptions seen
    # AttributeError
    # TypeError
    # AssertionError

* I make the :ref:`logical_conjunction function<test_logical_conjunction>` in ``truth_table.py`` return :ref:`False <test_what_is_false>`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2-3

    def logical_conjunction(first_input, second_input):
        # return True
        return False

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  because the :ref:`function<what is a function?>` now returns :red:`False` and the :ref:`assertion<what is an assertion?>` before this one, expects :green:`True`.

  :ref:`logical_conjunction<test_logical_conjunction>` has to make a choice. It should return

  - :red:`False`, if the first input is :green:`True` and the second input is :red:`False`
  - :green:`True`, if the first input is :green:`True` and the second input is :green:`True`
  - the second input in these 2 cases

* I change the :ref:`return statement<the return statement>` of the :ref:`logical_conjunction function<test_logical_conjunction>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 3-4

    def logical_conjunction(first_input, second_input):
        # return False
        # return True
        return second_input

  the test passes.

  .. code-block:: python

    logical_conjunction(True, False) -> False
    logical_conjunction(True, True ) -> True

* I add an :ref:`assertion<what is an assertion?>` for the third case, which is if the first input is :red:`False` and the second input is :green:`True`, to :ref:`test_logical_conjunction` in ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :green:`True`  :red:`False`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 12-16

        def test_logical_conjunction(self):
            self.assertTrue(
                src.truth_table.logical_conjunction(
                    True, True
                )
            )
            self.assertFalse(
                src.truth_table.logical_conjunction(
                    True, False
                )
            )
            self.assertFalse(
                src.truth_table.logical_conjunction(
                    False, True
                )
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  because my solution does not work for this case. The :ref:`function<what is a function?>` returns :green:`True` and the :ref:`assertion<what is an assertion?>` expects :red:`False`. The :ref:`logical_conjunction function<test_logical_conjunction>` has to make a choice, it should return

  - :red:`False`, if the first input is :red:`False` and the second input is :green:`True`
  - :red:`False`, if the first input is :green:`True` and the second input is :red:`False`
  - :green:`True`, if the first input is :green:`True` and the second input is :green:`True`

  I can use `if statements`_ to make it choose what to do based on the inputs.

----

*********************************************************************************
if statements
*********************************************************************************

An `if statement`_ is a way for a program_ to choose what to do based on something else. I can use `if statements`_ to make a :ref:`function<what is a function?>` choose between two things. They are written this way in Python_

.. code-block:: python

  if something:
      then do this

* I add an `if statement`_ for when the first input is :red:`False` to the :ref:`logical_conjunction function<test_logical_conjunction>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 4-5

    def logical_conjunction(first_input, second_input):
        # return False
        # return True
        if first_input == False:
            return False
        return second_input

  the test passes. :ref:`logical_conjunction<test_logical_conjunction>` returns

  - :red:`False`, if the first input is :red:`False`
  - the second input if the above :ref:`condition<if statements>` is NOT met

  because Python_ checks if ``first_input`` is equal to :red:`False` when ``if first_input == False:`` runs,

  - if ``first_input`` is NOT equal to :red:`False`, it leaves the `if statement`_ and continues to run the rest of the :ref:`function<what is a function?>` - ``return second_input``, which returns the value of ``second_input`` as the output, then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`

    .. code-block:: shell

      logical_conjunction(True , True ) -> True
      └── def logical_conjunction(first_input, second_input):
          ├── first_input  == True
          ├── second_input == True
          ├── if first_input == False:
          │      return False
          └── return second_input

    .. code-block:: shell

      logical_conjunction(True , False) -> False
      └── def logical_conjunction(first_input, second_input):
          ├── first_input  == True
          ├── second_input == False
          ├── if first_input == False:
          │      return False
          └── return second_input

  - if ``first_input`` is equal to :red:`False`, it goes to the next line - ``return False`` then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`

    .. code-block:: shell

      logical_conjunction(False, True ) -> False
      └── def logical_conjunction(first_input, second_input):
          ├── first_input  == False
          ├── second_input == False
          └── if first_input == False:
              └── return False
              return second_input

* I add an :ref:`assertion<what is an assertion?>` for the last case, which is if the first input is :red:`False` and the second input is :red:`False`, to :ref:`test_logical_conjunction` in ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :red:`False`   :red:`False`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 17-21

        def test_logical_conjunction(self):
            self.assertTrue(
                src.truth_table.logical_conjunction(
                    True, True
                )
            )
            self.assertFalse(
                src.truth_table.logical_conjunction(
                    True, False
                )
            )
            self.assertFalse(
                src.truth_table.logical_conjunction(
                    False, True
                )
            )
            self.assertFalse(
                src.truth_table.logical_conjunction(
                    False, False
                )
            )


    # Exceptions seen

  the test is still green.

* There is only one case where :ref:`logical_conjunction<test_logical_conjunction>` returns :green:`True`, I add an `if statement`_ for it in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 4-9

    def logical_conjunction(first_input, second_input):
        # return False
        # return True
        # if first_input == False:
        #     return False
        # return second_input
        if first_input == True:
            if second_input == True:
                return True

  the test is still green, because the :ref:`function<what is a function?>` returns

  - :green:`True` when the :ref:`conditions<if statements>` are met.
  - :ref:`None<what is None?>` when the :ref:`conditions<if statements>` are NOT met, because :ref:`all functions return None by default, as if they have an invisible line that says return None<test_making_a_function_w_return_none>`.

* I add a :ref:`return statement<the return statement>` to make it clearer

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 10

    def logical_conjunction(first_input, second_input):
        # return False
        # return True
        # if first_input == False:
        #     return False
        # return second_input
        if first_input == True:
            if second_input == True:
                return True
        return None

  still green, because :ref:`None is grouped as False<test_is_none_falsy_or_truthy>`.

* I change :ref:`None<what is None?>` to :red:`False` in the :ref:`return statement<the return statement>`, to make it clearer

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 10-11

    def logical_conjunction(first_input, second_input):
        # return False
        # return True
        # if first_input == False:
        #     return False
        # return second_input
        if first_input == True:
            if second_input == True:
                return True
        # return None
        return False

  green. It now only checks ``second_input`` if ``first_input`` is :green:`True`.

* I add :ref:`bool<how to test if something is grouped as True>` to the `if statements`_

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 7-10

    def logical_conjunction(first_input, second_input):
        # return False
        # return True
        # if first_input == False:
        #     return False
        # return second_input
        # if first_input == True:
        if bool(first_input) == True:
            # if second_input == True:
            if bool(second_input) == True:
                return True
        # return None
        return False

  still green because ``bool(something)`` returns :green:`True` if the :ref:`object<everything is an object>` in parentheses is :ref:`grouped as True<test_what_is_true>`.

* Since ``bool(True)`` is the same as :green:`True`, ``bool(first_input) == True`` is the same thing as ``True == True`` when ``first_input`` is :green:`True`, which is a repetition.

  .. code-block:: python

    first_input = True

    if bool(first_input) == True:
    if bool(True       ) == True:
    if True              == True:

  I remove ``== True`` from the `if statements`_

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 8-9, 11-12

    def logical_conjunction(first_input, second_input):
        # return False
        # return True
        # if first_input == False:
        #     return False
        # return second_input
        # if first_input == True:
        # if bool(first_input) == True:
        if bool(first_input):
            # if second_input == True:
            # if bool(second_input) == True:
            if bool(second_input):
                return True
        # return None
        return False

  the test is still green because

  - ``if bool(something)`` checks if ``bool(something)`` returns :ref:`True <test_what_is_true>`
  - if the result of ``bool(something)`` is :green:`True` then ``if bool(something)`` is the same thing as ``if True``
  - ``if bool(something)`` is the same as ``if bool(something) == True``

  .. code-block:: python

    if bool(something)
    if bool(something) == True
    if True            == True
    if True

* Which means I can remove :ref:`bool<how to test if something is grouped as True>`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 9-10, 13-14

    def logical_conjunction(first_input, second_input):
        # return False
        # return True
        # if first_input == False:
        #     return False
        # return second_input
        # if first_input == True:
        # if bool(first_input) == True:
        # if bool(first_input):
        if first_input:
            # if second_input == True:
            # if bool(second_input) == True:
            # if bool(second_input):
            if second_input:
                return True
        # return None
        return False

  still green because I can assume the following substitutions for ``if something == True:``

  - if the value of ``something`` is :red:`False`

    .. literalinclude:: ../../code/truth_table/solutions/if_something_false.py
      :language: python

  - if the value of ``something`` is :green:`True`

    .. literalinclude:: ../../code/truth_table/solutions/if_something_true.py
      :language: python

  this means that ``if bool(something) == True`` is the same as ``if bool(something)`` is the same as ``if something``.

* I can use :ref:`AND<test_logical_conjunction>` to put two `if statements`_ together when one is indented under the other

  .. code-block:: python

    if something:
        if something_else:

  can also be written as

  .. code-block:: python

    if something and something_else:

  I use :ref:`AND<test_logical_conjunction>` to put the two `if statements`_ together

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 10, 14-15

    def logical_conjunction(first_input, second_input):
        # return False
        # return True
        # if first_input == False:
        #     return False
        # return second_input
        # if first_input == True:
        # if bool(first_input) == True:
        # if bool(first_input):
        # if first_input:
            # if second_input == True:
            # if bool(second_input) == True:
            # if bool(second_input):
            # if second_input:
        if first_input and second_input:
                return True
        # return None
        return False

  green.

* I add an else_ clause to make it clearer

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 15, 18-19

    def logical_conjunction(first_input, second_input):
        # return False
        # return True
        # if first_input == False:
        #     return False
        # return second_input
        # if first_input == True:
        # if bool(first_input) == True:
        # if bool(first_input):
        # if first_input:
            # if second_input == True:
            # if bool(second_input) == True:
            # if bool(second_input):
            # if second_input:
        if first_input and second_input:
            return True
        # return None
        else:
            return False

  still green because Python_ checks if ``first_input`` is grouped as :green:`True` when the :ref:`logical_conjunction function<test_logical_conjunction>` is :ref:`called<how to call a function with input>`. When ``if first_input and second_input:`` runs,

  - if ``first_input`` is grouped as :red:`False`, it leaves the `if statement`_ to run the rest of the :ref:`function<what is a function?>` - ``else: return False``, which returns :red:`False` as the output then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`

    .. code-block:: shell

      logical_conjunction(False, False) -> False
      └── def logical_conjunction(first_input, second_input):
          ├── first_input  == False
          ├── second_input == False
          ├── if first_input and second_input:
          │       return True
          └── else:
              └── return False

    .. code-block:: shell

      logical_conjunction(False, True ) -> False
      └── def logical_conjunction(first_input, second_input):
          ├── first_input  == False
          ├── second_input == True
          ├── if first_input and second_input:
          │       return True
          └── else:
              └── return False

  - if ``first_input`` is grouped as :green:`True`, it checks if ``second_input`` is grouped as :green:`True`

    * if ``second_input`` is grouped as :red:`False`, it leaves the `if statement`_ to run the rest of the :ref:`function<what is a function?>` - ``else: return False``, which returns :red:`False` as the output then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`

      .. code-block:: shell

        logical_conjunction(True , False) -> False
        └── def logical_conjunction(first_input, second_input):
            ├── first_input  == True
            ├── second_input == False
            ├── if first_input and second_input:
            │       return True
            └── else:
                └── return False

    * if ``second_input`` is grouped as :green:`True`, it runs ``return True``, which returns :green:`True` as the output then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`

      .. code-block:: shell

        logical_conjunction(True , True ) -> True
        └── def logical_conjunction(first_input, second_input):
            ├── first_input  == True
            ├── second_input == True
            └── if first_input and second_input:
                └── return True
                else:
                    return False

  - it only checks ``second_input`` if ``first_input`` is :green:`True`.

----

*********************************************************************************
conditional expressions
*********************************************************************************

* There is a way to write the `if statement`_ and `else clause`_ on one line instead of four lines. It is called a `ternary operator`_ or `conditional expression`_. I add one to the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 15-16, 18-24

    def logical_conjunction(first_input, second_input):
        # return False
        # return True
        # if first_input == False:
        #     return False
        # return second_input
        # if first_input == True:
        # if bool(first_input) == True:
        # if bool(first_input):
        # if first_input:
            # if second_input == True:
            # if bool(second_input) == True:
            # if bool(second_input):
            # if second_input:
        # if first_input and second_input:
        #     return True
        # return None
        # else:
        #     return False
        return (
            True if
            first_input and second_input
            else False
        )

  the test is still green, because this is the same statement in a different order

  - ``return True`` comes first instead of after ``if first_input and second_input``
  - ``first_input and second_input`` come next, without the ``if``
  - ``else`` comes after ``first_input and second_input``
  - then :red:`False` without the return comes after ``else``

  .. code-block:: python

    if first_input and second_input: vs return True
        return True                  vs if first_input and second_input
    else:                            vs else
        return False                 vs False

  .. code-block:: python

    return True if something else False

  is a simpler way to write

  .. code-block:: python

    if something:
        return True
    else:
        return False

* I can make the `conditional expression`_ even simpler, if I remove ``True if`` and ``else False``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 21, 23

    def logical_conjunction(first_input, second_input):
        # return False
        # return True
        # if first_input == False:
        #     return False
        # return second_input
        # if first_input == True:
        # if bool(first_input) == True:
        # if bool(first_input):
        # if first_input:
            # if second_input == True:
            # if bool(second_input) == True:
            # if bool(second_input):
            # if second_input:
        # if first_input and second_input:
        #     return True
        # return None
        # else:
        #     return False
        return (
            # True if
            first_input and second_input
            # else False
        )

  still green!

  .. code-block:: python

    return something

  is a simpler way to write

  .. code-block:: python

    return True if something else False

  which is a simpler way to write

  .. code-block:: python

    if something:
        return True
    else:
        return False

* I remove the commented lines from ``logical_conjunction``

  .. code-block:: python
    :lineno-start: 17

    def contradiction(first_input, second_input):
        return False


    def logical_conjunction(first_input, second_input):
        return first_input and second_input

* I add a :ref:`variable<what is a variable?>` for ``src.truth_table.logical_conjunction`` in :ref:`test_logical_conjunction` of ``test_binary.py``

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 2-4

        def test_logical_conjunction(self):
            logical_conjunction = (
                src.truth_table.logical_conjunction
            )
            self.assertTrue(
                src.truth_table.logical_conjunction(
                    True, True
                )
            )
            self.assertFalse(
                src.truth_table.logical_conjunction(
                    True, False
                )
            )
            self.assertFalse(
                src.truth_table.logical_conjunction(
                    False, True
                )
            )
            self.assertFalse(
                src.truth_table.logical_conjunction(
                    False, False
                )
            )


    # Exceptions seen

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``src.truth_table.logical_conjunction``  from the test

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 6-7, 12-13, 18-19, 24-25

        def test_logical_conjunction(self):
            logical_conjunction = (
                src.truth_table.logical_conjunction
            )
            self.assertTrue(
                # src.truth_table.logical_conjunction(
                logical_conjunction(
                    True, True
                )
            )
            self.assertFalse(
                # src.truth_table.logical_conjunction(
                logical_conjunction(
                    True, False
                )
            )
            self.assertFalse(
                # src.truth_table.logical_conjunction(
                logical_conjunction(
                    False, True
                )
            )
            self.assertFalse(
                # src.truth_table.logical_conjunction(
                logical_conjunction(
                    False, False
                )
            )


    # Exceptions seen

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 5-8

        def test_logical_conjunction(self):
            logical_conjunction = (
                src.truth_table.logical_conjunction
            )
            self.assertTrue(logical_conjunction(True, True))
            self.assertFalse(logical_conjunction(True, False))
            self.assertFalse(logical_conjunction(False, True))
            self.assertFalse(logical_conjunction(False, False))


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add logical_conjunction'

:ref:`logical_conjunction<test_logical_conjunction>` also known as and_, always returns

* ``first_input and second_input``
* :green:`True`, if the first input is :green:`True` and the second input is :green:`True`

----

=================================================================================
examples of Logical Conjunction
=================================================================================

----

* A person can vote, if the inputs are

  - is the person a citizen?
  - is the person old enough?

  ==============  ============== ==============
  is a citizen    is old enough  can vote
  ==============  ============== ==============
  :green:`yes`    :green:`yes`   :green:`yes`
  :green:`yes`    :red:`no`      :red:`no`
  :red:`no`       :green:`yes`   :red:`no`
  :red:`no`       :red:`no`      :red:`no`
  ==============  ============== ==============

* A person can get a license, if the inputs are

  - did the person pass the test?
  - is the person old enough?

  ==============  ============== ================
  passed test     is old enough  can get license
  ==============  ============== ================
  :green:`yes`    :green:`yes`   :green:`yes`
  :green:`yes`    :red:`no`      :red:`no`
  :red:`no`       :green:`yes`   :red:`no`
  :red:`no`       :red:`no`      :red:`no`
  ==============  ============== ================

* I can bake a cake, if the inputs are

  - flour?
  - eggs?

  =============  ============= ==============
  flour          eggs          can bake
  =============  ============= ==============
  :green:`yes`   :green:`yes`  :green:`yes`
  :green:`yes`   :red:`no`     :red:`no`
  :red:`no`      :green:`yes`  :red:`no`
  :red:`no`      :red:`no`     :red:`no`
  =============  ============= ==============

* I am a programmer, if the inputs are

  - can read code?
  - can write code?

  =============  ============= ================
  read           write         is a programmer
  =============  ============= ================
  :green:`yes`   :green:`yes`  :green:`yes`
  :green:`yes`   :red:`no`     :red:`no`
  :red:`no`      :green:`yes`  :red:`no`
  :red:`no`      :red:`no`     :red:`no`
  =============  ============= ================

  how did I learn to write without reading?

* Multi Factor Authentication to log in, if the inputs are

  - did the user provide the right password?
  - did the user provide the MFA code?

  ==============  ============== ==============
  right password  right MFA code log in
  ==============  ============== ==============
  :green:`yes`    :green:`yes`   :green:`yes`
  :green:`yes`    :red:`no`      :red:`no`
  :red:`no`       :green:`yes`   :red:`no`
  :red:`no`       :red:`no`      :red:`no`
  ==============  ============== ==============

  how did I get the right MFA code without the right password?

* I can sell a product, if the inputs are

  - is there supply?
  - is there demand?

  ==============  ============== ==============
  supply          demand         can sell
  ==============  ============== ==============
  :green:`yes`    :green:`yes`   :green:`yes`
  :green:`yes`    :red:`no`      :red:`no`
  :red:`no`       :green:`yes`   :red:`no`
  :red:`no`       :red:`no`      :red:`no`
  ==============  ============== ==============

-----

.. admonition:: All of the statements below have the same result as ``return something`` because Python_ groups :ref:`objects<everything is an object>` as :red:`False` or :green:`True`

  * return :green:`True`  if ``something`` is equal to :green:`True`

    .. code-block:: python

      if something == True:
          return True
      else:
          return False

  * return :green:`True` if the result of  ``bool(something)`` is equal to :green:`True`

    .. code-block:: python

      if bool(something) == True:
          return True
      else:
          return False

  * return :green:`True` if the result of  ``bool(something)`` is :green:`True`

    .. code-block:: python

      if bool(something):
          return True
      else:
          return False

  * return :green:`True` if the result of  ``bool(something)`` is :green:`True`

    .. code-block:: python

      if something:
          return True
      else:
          return False

  * return :green:`True` if the result of  ``bool(something)`` is :green:`True`

    .. code-block:: python

      return True if something else False

----

*********************************************************************************
test_project_second
*********************************************************************************

The :ref:`truth table` for :ref:`project_second<test_project_second>` is

==============  ============== ==============
first input     second input   return
==============  ============== ==============
:green:`True`   :green:`True`  :green:`True`
:green:`True`   :red:`False`   :red:`False`
:red:`False`    :green:`True`  :green:`True`
:red:`False`    :red:`False`   :red:`False`
==============  ============== ==============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test for :ref:`project_second<test_project_second>` with an :ref:`assertion<what is an assertion?>` for the case when the first input is :green:`True` and the second input is :green:`True`, to ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 3-6

            self.assertFalse(logical_conjunction(False, False))

        def test_project_second(self):
            self.assertTrue(
                src.truth_table.project_second(True, True)
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table'
                    has no attribute 'project_second'

  because I do not have a :ref:`definition<how to make a function>` for the :ref:`project_second function<test_project_second>` in ``truth_table.py``.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``project_second`` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 31
  :emphasize-lines: 5-6

  def logical_conjunction(first_input, second_input):
      return first_input and second_input


  def project_second(first_input, second_input):
      return True

the test passes. :ref:`project_second<test_project_second>` returns :green:`True`, if the first input is :green:`True` and the second input is :green:`True`, just like :ref:`logical_conjunction<test_logical_conjunction>`

.. code-block:: python

       project_second(True , True ) -> True
  logical_conjunction(True , True ) -> True

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for the second case, which is if the first input is :green:`True` and the second input is :red:`False`, to :ref:`test_project_second` in ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :red:`False`   :red:`False`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 5-7

        def test_project_second(self):
            self.assertTrue(
                src.truth_table.project_second(True, True)
            )
            self.assertFalse(
                src.truth_table.project_second(True, False)
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  because the :ref:`function<what is a function?>` returns :green:`True` and the :ref:`assertion<what is an assertion?>` expects

  - :red:`False`, if the first input is :green:`True` and the second input is :red:`False`
  - :green:`True`, if the first input is :green:`True` and the second input is :green:`True`
  - the second input in both cases

* I make :ref:`project_second<test_project_second>` return ``second_input`` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 2-3

    def project_second(first_input, second_input):
        # return True
        return second_input

  the test passes. The :ref:`project_second function<test_project_second>` returns the second input.

  .. code-block:: python

    project_second(True , False) -> False
    project_second(True , True ) -> True

* I remove the commented line

  .. code-block:: python
    :lineno-start: 25

    def project_second(first_input, second_input):
        return second_input

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_project_second` for the next case, which is if the first input is :red:`False` and the second input is :green:`True`, in ``test_binary.py``

  .. code-block:: python
    :lineno-start: 23
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


    # Exceptions seen

  the test is still green.

  .. code-block:: python

    project_second(False, True ) -> True
    project_second(True , False) -> False
    project_second(True , True ) -> True

* I add an :ref:`assertion<what is an assertion?>` for the last case, which is if the first input is :red:`False` and the second input is :red:`False`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :red:`False`   :red:`False`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 23
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

  still green.

  .. code-block:: python

    project_second(False, False) -> False
    project_second(False, True ) -> True
    project_second(True , False) -> False
    project_second(True , True ) -> True

* I add a :ref:`variable<what is a variable?>` for ``src.truth_table.project_second``

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 2

        def test_project_second(self):
            project_second = src.truth_table.project_second
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

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``src.truth_table.project_second`` from the test

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 4-5, 8-9, 12-13, 16-17

        def test_project_second(self):
            project_second = src.truth_table.project_second
            self.assertTrue(
                # src.truth_table.project_second(True, True)
                project_second(True, True)
            )
            self.assertFalse(
                # src.truth_table.project_second(True, False)
                project_second(True, False)
            )
            self.assertTrue(
                # src.truth_table.project_second(False, True)
                project_second(False, True)
            )
            self.assertFalse(
                # src.truth_table.project_second(False, False)
                project_second(False, False)
            )


    # Exceptions seen

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 3-6

        def test_project_second(self):
            project_second = src.truth_table.project_second
            self.assertTrue(project_second(True, True))
            self.assertFalse(project_second(True, False))
            self.assertTrue(project_second(False, True))
            self.assertFalse(project_second(False, False))


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add project_second'

:ref:`project_second<test_project_second>` always returns the second input. It does not care about the first input, it projects the second input.

----

=================================================================================
examples of Project Second
=================================================================================

----

* Binge watching TV, if the inputs are

  - should I sleep?
  - do I want to watch one more episode?

  ==============  =============== ==============
  sleep?          do I want it?   watch TV
  ==============  =============== ==============
  :green:`yes`    :green:`yes`    :green:`yes`
  :green:`yes`    :red:`no`       :red:`no`
  :red:`no`       :green:`yes`    :green:`yes`
  :red:`no`       :red:`no`       :red:`no`
  ==============  =============== ==============

* dictatorship, if the inputs are

  - is voters' choice?
  - is dictator's choice?

  ==============  =============== ==============
  voters          dictator        outcome
  ==============  =============== ==============
  :green:`yes`    :green:`yes`    :green:`yes`
  :green:`yes`    :red:`no`       :red:`no`
  :red:`no`       :green:`yes`    :green:`yes`
  :red:`no`       :red:`no`       :red:`no`
  ==============  =============== ==============

* being sick, if the inputs are

  - sick before?
  - sick now?

  ================  ================  ================
  before            now               sick
  ================  ================  ================
  :green:`healthy`  :green:`healthy`  :green:`healthy`
  :green:`healthy`  :red:`sick`       :red:`sick`
  :red:`sick`       :green:`healthy`  :green:`healthy`
  :red:`sick`       :red:`sick`       :red:`sick`
  ================  ================  ================

* my expectation versus reality, if the inputs are

  - my expectation
  - reality

  ================  ================  ================
  expectation       reality           result
  ================  ================  ================
  :green:`True`     :green:`True`     :green:`True`
  :green:`True`     :red:`False`      :red:`False`
  :red:`False`      :green:`True`     :green:`True`
  :red:`False`      :red:`False`      :red:`False`
  ================  ================  ================

----

*********************************************************************************
test_converse_non_implication
*********************************************************************************

The :ref:`truth table` for :ref:`converse_non_implication<test_converse_non_implication>` is

==============  ============== ==============
first input     second input   return
==============  ============== ==============
:green:`True`   :green:`True`  :red:`False`
:green:`True`   :red:`False`   :red:`False`
:red:`False`    :green:`True`  :green:`True`
:red:`False`    :red:`False`   :red:`False`
==============  ============== ==============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test for :ref:`converse_non_implication<test_converse_non_implication>` with an :ref:`assertion<what is an assertion?>` for when the first input is :green:`True` and the second input is :green:`True`, to ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :red:`False`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 3-8

            self.assertFalse(project_second(False, False))

        def test_converse_non_implication(self):
            self.assertFalse(
                src.truth_table.converse_non_implication(
                    True, True
                )
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table'
                    has no attribute 'converse_non_implication'

  because there is no definition for :ref:`converse_non_implication<test_converse_non_implication>` in ``truth_table.py`` in the ``src`` folder_.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``converse_non_implication`` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 25
  :emphasize-lines: 5-6

    def project_second(first_input, second_input):
        return second_input


    def converse_non_implication(first_input, second_input):
        return False

the test passes. :ref:`converse_non_implication<test_converse_non_implication>` returns :red:`False`, if the first input is :green:`True` and the second input is :green:`True`.

.. code-block:: python

  converse_non_implication(True , True ) -> False

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for the next case, which is if the first input is :green:`True` and the second input is :red:`False`, to :ref:`test_converse_non_implication` of ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :red:`False`   :red:`False`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 7-11

        def test_converse_non_implication(self):
            self.assertFalse(
                src.truth_table.converse_non_implication(
                    True, True
                )
            )
            self.assertFalse(
                src.truth_table.converse_non_implication(
                    True, False
                )
            )


    # Exceptions seen

  the test is still green. :ref:`converse_non_implication<test_converse_non_implication>` returns :red:`False`

  - if the first input is :green:`True` and the second input is :red:`False`
  - if the first input is :green:`True` and the second input is :green:`True`

  .. code-block:: python

    converse_non_implication(True , False) -> False
    converse_non_implication(True , True ) -> False

* I add an :ref:`assertion<what is an assertion?>` for the third case, which is if the first input is :red:`False` and the second input is :green:`True`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :green:`True`  :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 12-16

        def test_converse_non_implication(self):
            self.assertFalse(
                src.truth_table.converse_non_implication(
                    True, True
                )
            )
            self.assertFalse(
                src.truth_table.converse_non_implication(
                    True, False
                )
            )
            self.assertTrue(
                src.truth_table.converse_non_implication(
                    False, True
                )
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  because the :ref:`converse_non_implication function<test_converse_non_implication>` returns :red:`False` and the :ref:`assertion<what is an assertion?>` expects :green:`True`.

* I add an `if statement`_ for this case to the :ref:`converse_non_implication function<test_converse_non_implication>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2-3

    def converse_non_implication(first_input, second_input):
        if first_input == False:
            return True
        return False

  the test passes. :ref:`converse_non_implication<test_converse_non_implication>` returns

  - :green:`True` if the first input is :red:`False`
  - :red:`False` if the above condition is NOT met

  because Python_ checks if ``first_input`` is equal to :red:`False`, when the :ref:`converse_non_implication function<test_converse_non_implication>` is :ref:`called<how to call a function with input>`. When ``if first_input == False:`` runs

  - if ``first_input`` is NOT equal to :red:`False`, it leaves the `if statement`_ to run the rest of the :ref:`function<what is a function?>` - ``return False``, which returns :red:`False` as the output then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`

    .. code-block:: shell

      converse_non_implication(True , True ) -> False
      └── def converse_non_implication(first_input, second_input):
          ├── first_input  == True
          ├── second_input == True
          ├── if first_input == False:
          │       return True
          └── return False

    .. code-block:: shell

      converse_non_implication(True , False) -> False
      └── def converse_non_implication(first_input, second_input):
          ├── first_input  == True
          ├── second_input == False
          ├── if first_input == False:
          │       return True
          └── return False

  - if ``first_input`` is equal to :red:`False`, it runs ``return True``, which returns :green:`True` as the output then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`

    .. code-block:: shell

      converse_non_implication(False, True ) -> True
      └── def converse_non_implication(first_input, second_input):
          ├── first_input  == False
          ├── second_input == True
          └── if first_input == False:
              └── return True
              return False

* I add an :ref:`assertion<what is an assertion?>` for the next case, which is if the first input is :red:`False` and the second input is :red:`False`, to :ref:`test_converse_non_implication` in ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :red:`False`   :red:`False`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 17-21

        def test_converse_non_implication(self):
            self.assertFalse(
                src.truth_table.converse_non_implication(
                    True, True
                )
            )
            self.assertFalse(
                src.truth_table.converse_non_implication(
                    True, False
                )
            )
            self.assertTrue(
                src.truth_table.converse_non_implication(
                    False, True
                )
            )
            self.assertFalse(
                src.truth_table.converse_non_implication(
                    False, False
                )
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  because the :ref:`function<what is a function?>` returned :green:`True` and the :ref:`assertion<what is an assertion?>` expects :red:`False`.

* I add an `if statement`_ for the one case that returns :green:`True`, to the one in :ref:`the converse_non_implication function<test_converse_non_implication>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 3-4

    def converse_non_implication(first_input, second_input):
        if first_input == False:
            if second_input == True:
                return True
        return False

  the test passes. The :ref:`converse_non_implication function<test_converse_non_implication>` only checks the second input if the first input is :red:`False`.

* I add :ref:`bool<how to test if something is grouped as True>`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2-5

    def converse_non_implication(first_input, second_input):
        # if first_input == False:
        if bool(first_input) == False:
            # if second_input == True:
            if bool(second_input) == True:
                return True
        return False

  the test is still green.

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write the first `if statement`_ in terms of :green:`True`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 3-4

    def converse_non_implication(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        if bool(not first_input) == True:
            # if second_input == True:
            if bool(second_input) == True:
                return True
        return False

  still green.

* I remove ``== True`` to remove repetition

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 4-5, 7-8

    def converse_non_implication(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if bool(not first_input) == True:
        if bool(not first_input):
            # if second_input == True:
            # if bool(second_input) == True:
            if bool(second_input):
                return True
        return False

  green.

* I remove :ref:`bool<how to test if something is grouped as True>`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 5-6, 9-10

    def converse_non_implication(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if bool(not first_input) == True:
        # if bool(not first_input):
        if not first_input:
            # if second_input == True:
            # if bool(second_input) == True:
            # if bool(second_input):
            if second_input:
                return True
        return False

  still green, because

  * Python_ checks if ``first_input`` is equal to :red:`False` when ``if first_input == False:`` runs. I can assume the following substitutions

    - if the value of ``something`` is :red:`False`

      .. literalinclude:: ../../code/truth_table/solutions/if_not_something_false.py
        :language: python

    - if the value of ``something`` is :green:`True`

      .. literalinclude:: ../../code/truth_table/solutions/if_not_something_true.py
        :language: python

  * Python_ checks if ``(second_input)`` is equal to :green:`True` when ``if second_input == True:`` runs. I can assume the following substitutions

    - if the value of ``something`` is :red:`False`

      .. literalinclude:: ../../code/truth_table/solutions/if_something_false.py
        :language: python

    - if the value of ``something`` is :green:`True`

      .. literalinclude:: ../../code/truth_table/solutions/if_something_true.py
        :language: python

  this means that

  - ``if bool(something) == False`` is the same as ``if bool(not something) == True`` is the same as ``if bool(not something)`` is the same as ``if not something``.
  - ``if bool(something) == True`` is the same as ``if bool(something)`` is the same as ``if something``.

* I use :ref:`Logical Conjunction (AND)<test_logical_conjunction>` to put the two `if statements`_ together

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 6, 10-11

    def converse_non_implication(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if bool(not first_input) == True:
        # if bool(not first_input):
        # if not first_input:
            # if second_input == True:
            # if bool(second_input) == True:
            # if bool(second_input):
            # if second_input:
        if not first_input and second_input:
                return True
        return False

  the test is still green, because I can put two `if statements`_ together when one is indented under the other

  .. code-block:: python

    if something:
        if something_else:

  can also be written as

  .. code-block:: python

    if something and something_else:

* I add an `else clause`_ to be clearer

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 12-14

    def converse_non_implication(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if bool(not first_input) == True:
        # if bool(not first_input):
        # if not first_input:
            # if second_input == True:
            # if bool(second_input) == True:
            # if bool(second_input):
            # if second_input:
        if not first_input and second_input:
            return True
        else:
            return False

  still green because Python_ checks if ``first_input`` is grouped as :green:`False` when the :ref:`converse_non_implication function<test_converse_non_implication>` is :ref:`called<how to call a function with input>`. When ``if not first_input and second_input:`` runs,

  - if ``first_input`` is grouped as :green:`True`, it leaves the `if statement`_ to run the rest of the :ref:`function<what is a function?>` - ``else: return False``, which returns :red:`False` as the output then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`

    .. code-block:: shell

      converse_non_implication(True , True ) -> False
      └── def converse_non_implication(first_input, second_input):
          ├── first_input  == True
          ├── second_input == True
          ├── if not first_input and second_input:
          │       return True
          └── else:
              └── return False

    .. code-block:: shell

      converse_non_implication(True , False) -> False
      └── def converse_non_implication(first_input, second_input):
          ├── first_input  == True
          ├── second_input == False
          ├── if not first_input and second_input:
          │       return True
          └── else:
              └── return False

  - if ``first_input`` is grouped as :green:`False`, it checks if ``second_input`` is grouped as :green:`True`

    * if ``second_input`` is grouped as :red:`False`, it leaves the `if statement`_ to run the rest of the :ref:`function<what is a function?>` - ``else: return False``, which returns :red:`False` as the output then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`

      .. code-block:: shell

        converse_non_implication(False, False) -> False
        └── def converse_non_implication(first_input, second_input):
            ├── first_input  == False
            ├── second_input == False
            ├── if not first_input and second_input:
            │       return True
            └── else:
                └── return False

    * if ``second_input`` is grouped as :green:`True`, it runs ``return True``, which returns :green:`True` as the output then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`

      .. code-block:: shell

        converse_non_implication(False, True ) -> True
        └── def converse_non_implication(first_input, second_input):
            ├── first_input  == False
            ├── second_input == True
            └── if not first_input and second_input:
                └── return True
                else:
                    return False

  - it only checks ``second_input`` if ``first_input`` is :red:`False`.

* I use a `conditional expression`_

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 11-19

    def converse_non_implication(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if bool(not first_input) == True:
        # if bool(not first_input):
        # if not first_input:
            # if second_input == True:
            # if bool(second_input) == True:
            # if bool(second_input):
            # if second_input:
        # if not first_input and second_input:
        #     return True
        # else:
        #     return False
        return (
            True if
            not first_input and second_input
            else False
        )

  green.

  .. code-block:: python

    if (                  vs return True
        not first_input
        and second_input
    ):
        return True       vs if not first_input and second_input
    else:                 vs else
        return False      vs False

* I remove ``True if`` and ``else False`` to make the simpler :ref:`return statement<the return statement>`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 16, 18

    def converse_non_implication(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if bool(not first_input) == True:
        # if bool(not first_input):
        # if not first_input:
            # if second_input == True:
            # if bool(second_input) == True:
            # if bool(second_input):
            # if second_input:
        # if not first_input and second_input:
        #     return True
        # else:
        #     return False
        return (
            # True if
            not first_input and second_input
            # else False
        )

  still green.

* :ref:`converse_non_implication<test_converse_non_implication>` returns ``not first_input and second_input``

  * Python_ replaces ``not first_input`` with :ref:`the logical negation (NOT)<test_logical_negation>` of ``first_input`` when it runs

  - if ``first_input`` is :red:`False`

    .. code-block:: python

      not first_input
      not False
      True

  - if ``first_input`` is :green:`True`

    .. code-block:: python

      not first_input
      not True
      False

  this means that in the four cases

  - if the first input is :green:`True` and the second input is :green:`True`, :ref:`converse_non_implication<test_converse_non_implication>` returns

    .. code-block:: python
      :emphasize-lines: 4

      (not first) and second
      (not True ) and True
       False      and True  # logical_conjunction(False, True)
       False

  - if the first input is :green:`True` and the second input is :red:`False`, :ref:`converse_non_implication<test_converse_non_implication>` returns

    .. code-block:: python
      :emphasize-lines: 4

      (not first) and second
      (not True ) and False
       False      and False # logical_conjunction(False, False)
       False

  - if the first input is :red:`False` and the second input is :green:`True`, :ref:`converse_non_implication<test_converse_non_implication>` returns

    .. code-block:: python
      :emphasize-lines: 4

      (not first) and second
      (not False) and True
       True       and True  # logical_conjunction(True, True)
       True

  - if the first input is :red:`False` and the second input is :red:`False`, :ref:`converse_non_implication<test_converse_non_implication>` returns

    .. code-block:: python
      :emphasize-lines: 4

      (not first) and second
      (not False) and False
       True       and False # logical_conjunction(True, False) -> False
       False

  ==============  =============== =============== ================
  first           not first       second          (not first)
                                                  and
                                                  second
  ==============  =============== =============== ================
  :green:`True`   :red:`False`    :green:`True`   :red:`False`
  :green:`True`   :red:`False`    :red:`False`    :red:`False`
  :red:`False`    :green:`True`   :green:`True`   :green:`True`
  :red:`False`    :green:`True`   :red:`False`    :red:`False`
  ==============  =============== =============== ================

  I add a :ref:`return statement<the return statement>` to show this

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 15-18

    def converse_non_implication(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if bool(not first_input) == True:
        # if bool(not first_input):
        # if not first_input:
            # if second_input == True:
            # if bool(second_input) == True:
            # if bool(second_input):
            # if second_input:
        # if not first_input and second_input:
        #     return True
        # else:
        #     return False
        return logical_conjunction(
            logical_negation(first_input),
            second_input
        )
        return (
            # True if
            not first_input and second_input
            # else False
        )

  the test is still green.

  .. code-block:: shell

    converse_non_implication(False, False) -> False
     └── logical_conjunction(True , False) -> False

    converse_non_implication(False, True ) -> True
     └── logical_conjunction(True , True ) -> True

    converse_non_implication(True , False) -> False
     └── logical_conjunction(False, False) -> False

    converse_non_implication(True , True ) -> False
     └── logical_conjunction(False, True ) -> False

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 6

    def converse_non_implication(first_input, second_input):
        return logical_conjunction(
            logical_negation(first_input),
            second_input
        )
        return not first_input and second_input

  I can use either of these two :ref:`return statements<the return statement>`. Only the first one will run in this case, because :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`.

* I add a :ref:`variable<what is a variable?>` for ``src.truth_table.converse_non_implication`` in ``test_binary.py``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 2-4

        def test_converse_non_implication(self):
            converse_non_implication = (
                src.truth_table.converse_non_implication
            )
            self.assertFalse(
                src.truth_table.converse_non_implication(
                    True, True
                )
            )
            self.assertFalse(
                src.truth_table.converse_non_implication(
                    True, False
                )
            )
            self.assertTrue(
                src.truth_table.converse_non_implication(
                    False, True
                )
            )
            self.assertFalse(
                src.truth_table.converse_non_implication(
                    False, False
                )
            )


    # Exceptions seen

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``src.truth_table.converse_non_implication``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 6-7, 12-13, 18-19, 24-25

        def test_converse_non_implication(self):
            converse_non_implication = (
                src.truth_table.converse_non_implication
            )
            self.assertFalse(
                # src.truth_table.converse_non_implication(
                converse_non_implication(
                    True, True
                )
            )
            self.assertFalse(
                # src.truth_table.converse_non_implication(
                converse_non_implication(
                    True, False
                )
            )
            self.assertTrue(
                # src.truth_table.converse_non_implication(
                converse_non_implication(
                    False, True
                )
            )
            self.assertFalse(
                # src.truth_table.converse_non_implication(
                converse_non_implication(
                    False, False
                )
            )


    # Exceptions seen

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 5-8

        def test_converse_non_implication(self):
            converse_non_implication = (
                src.truth_table.converse_non_implication
            )
            self.assertFalse(converse_non_implication(True, True))
            self.assertFalse(converse_non_implication(True, False))
            self.assertTrue(converse_non_implication(False, True))
            self.assertFalse(converse_non_implication(False, False))


    # Exceptions seen
    # AttributeError
    # TypeError
    # AssertionError

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add converse_non_implication'

:ref:`Converse Non-Implication<test_converse_non_implication>` always returns

* ``not first_input and second_input``
* the :ref:`Logical Conjunction<test_logical_conjunction>` of, the :ref:`Logical Negation<test_logical_negation>` of the first input, and the second input.
* :green:`True`, if the first input is :red:`False` and the second input is :green:`True`.

----

=================================================================================
examples of Converse Non-Implication
=================================================================================

----

* crossing the street, if the inputs are

  - light is green for cars?
  - light is green for walking?

  ===============  ===================  =======================
  green for cars?  green for walking?   can I cross the street?
  ===============  ===================  =======================
  :green:`yes`     :green:`yes`         :red:`no`
  :green:`yes`     :red:`no`            :red:`no`
  :red:`no`        :green:`yes`         :green:`yes`
  :red:`no`        :red:`no`            :red:`no`
  ===============  ===================  =======================

* do a computer update, if the inputs are

  - is the computer in use?
  - is there an update available?

  ===============  ================  ============
  computer in use  update available  do update
  ===============  ================  ============
  :green:`yes`     :green:`yes`      :red:`no`
  :green:`yes`     :red:`no`         :red:`no`
  :red:`no`        :green:`yes`      :green:`yes`
  :red:`no`        :red:`no`         :red:`no`
  ===============  ================  ============

* should I reply to a message?, if the inputs are

  - is it a group message?
  - is it one on one from a close friend?

  ===============  ================  ============
  group chat       close friend      reply
  ===============  ================  ============
  :green:`yes`     :green:`yes`      :red:`no`
  :green:`yes`     :red:`no`         :red:`no`
  :red:`no`        :green:`yes`      :green:`yes`
  :red:`no`        :red:`no`         :red:`no`
  ===============  ================  ============

* only give a discount to a new customer with a coupon code, if the inputs are

  - is already a customer?
  - does customer have the coupon code?

  ================  ================  =============
  already customer  has coupon        give discount
  ================  ================  =============
  :green:`yes`      :green:`yes`      :red:`no`
  :green:`yes`      :red:`no`         :red:`no`
  :red:`no`         :green:`yes`      :green:`yes`
  :red:`no`         :red:`no`         :red:`no`
  ================  ================  =============

* run the gas generator, if the inputs are

  - is the house receiving electricity from the grid?
  - is there fuel in the generator?

  ==============  ============== ==============
  grid            fuel           run generator
  ==============  ============== ==============
  :green:`yes`    :green:`yes`   :red:`no`
  :green:`yes`    :red:`no`      :red:`no`
  :red:`no`       :green:`yes`   :green:`yes`
  :red:`no`       :red:`no`      :red:`no`
  ==============  ============== ==============

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_binary.py`` and ``truth_table.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``truth_table``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

----

*********************************************************************************
review
*********************************************************************************

:ref:`Binary Operations<truth table: Binary Operations>` take two inputs, each input can be :green:`True` or :red:`False`. If I name the first input ``first_input`` and the second input ``second_input``, the tests show that

* :ref:`Converse Non-Implication<test_converse_non_implication>`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :red:`False`
  :green:`True`   :red:`False`   :red:`False`
  :red:`False`    :green:`True`  :green:`True`
  :red:`False`    :red:`False`   :red:`False`
  ==============  ============== ==============

  - returns ``not first_input and second_input``
  - returns :green:`True` only if ``first_input`` is :red:`False` and ``second_input`` is :green:`True`
  - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Converse Implication<test_converse_implication>` which returns :red:`False` if ``first_input`` is :red:`False` and ``second_input`` is :green:`True`

* :ref:`Project Second<test_project_second>`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :green:`True`
  :green:`True`   :red:`False`   :red:`False`
  :red:`False`    :green:`True`  :green:`True`
  :red:`False`    :red:`False`   :red:`False`
  ==============  ============== ==============

  - always returns ``second_input``
  - returns :green:`True` only if ``second_input`` is :green:`True`
  - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Negate Second<test_negate_second>` which returns :green:`True` only if ``second_input`` is :red:`False`

* :ref:`Logical Conjunction<test_logical_conjunction>` returns

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :green:`True`
  :green:`True`   :red:`False`   :red:`False`
  :red:`False`    :green:`True`  :red:`False`
  :red:`False`    :red:`False`   :red:`False`
  ==============  ============== ==============

  - returns ``first_input and second_input``
  - returns :green:`True` only if ``first_input`` is :green:`True` and ``second_input`` is :green:`True`
  - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Logical NAND<test_logical_nand>` which returns :red:`False` only if ``first_input`` is :green:`True` and ``second_input`` is :green:`True`

* :ref:`Contradiction<test_contradiction>`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :red:`False`
  :green:`True`   :red:`False`   :red:`False`
  :red:`False`    :green:`True`  :red:`False`
  :red:`False`    :red:`False`   :red:`False`
  ==============  ============== ==============

  - always returns :red:`False`
  - never returns :green:`True`
  - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Tautology<test_tautology>` which always returns :green:`True`

and

* :ref:`Logical Conjunction is "AND"<test_logical_conjunction>`
* :ref:`Logical Negation is "NOT" <test_logical_negation>`

One logic statement has been written with and_, another was written both and_ and :ref:`not<test_logical_negation>`.

=============================================== =============  ============= ============= ============= ==============================================================
return                                          True,          True,         False,        False,        name of operation
                                                True           False         True          False
=============================================== =============  ============= ============= ============= ==============================================================
False                                           :red:`False`   :red:`False`  :red:`False`  :red:`False`  :ref:`contradiction<test_contradiction>`
first and second                                :green:`True`  :red:`False`  :red:`False`  :red:`False`  :ref:`logical_conjunction<test_logical_conjunction>`
second                                          :green:`True`  :red:`False`  :green:`True` :red:`False`  :ref:`project_second<test_project_second>`
(not first) and second                          :red:`False`   :red:`False`  :green:`True` :red:`False`  :ref:`converse_non_implication<test_converse_non_implication>`
=============================================== =============  ============= ============= ============= ==============================================================

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<truth table: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

:ref:`Would you like to write more tests with bool?<how to test if something is grouped as True>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too.

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->