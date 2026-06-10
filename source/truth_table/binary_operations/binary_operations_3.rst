.. meta::
  :description: Explore advanced Python logic gates with a focus on Exclusive Disjunction (XOR), Material Non-Implication, and Converse Implication. This TDD-driven guide explains why XOR is the same as logical inequality (!=) and how to model complex rules like light switch circuits, magnet attraction, and broken promises. Learn to refactor verbose nested if-statements into elegant boolean expressions and conditional operators.
  :keywords: Jacob Itegboje, Python exclusive disjunction XOR, Python material non-implication, project first logic, converse implication python, XOR vs logical inequality, Python != operator truth table, real-world examples of XOR, light switch logic circuit, magnets attract repel logic, TDD Red Green Refactor tutorial, Python conditional expressions, boolean logic for software engineers, programming truth tables for beginners, python boolean simplification, logical negation examples, vending machine logic, coin toss probability code, refactoring python logic, boolean algebra for programmers

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

These are the tests I have at the end of the chapter

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

  if the terminal_ does not show

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

  the terminal_ is my friend, and shows

  .. code-block:: shell
    :emphasize-lines: 5

    rootdir: .../pumping_python/truth_table
    configfile: pyproject.toml
    collected 12 items

    tests/test_binary.py ........                      [ 66%]
    tests/test_nullary_unary.py ....                   [100%]

    ================== 12 passed in G.HIs ===================

* I hold :kbd:`ctrl` (Windows_) or :kbd:`option` (MacOS_) on the keyboard, then click on ``tests/test_binary.py`` with the mouse to open it

----

*********************************************************************************
test_exclusive_disjunction
*********************************************************************************

The :ref:`truth table` for :ref:`exclusive_disjunction<test_exclusive_disjunction>` is

==============  ============== ==============
first input     second input   return
==============  ============== ==============
:green:`True`   :green:`True`  :red:`False`
:green:`True`   :red:`False`   :green:`True`
:red:`False`    :green:`True`  :green:`True`
:red:`False`    :red:`False`   :red:`False`
==============  ============== ==============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for :ref:`exclusive_disjunction<test_exclusive_disjunction>` with an :ref:`assertion<what is an assertion?>` for the case when the first input is :green:`True` and the second input is :green:`True`, to ``test_binary.py``

==============  ============== ==============
first input     second input   return
==============  ============== ==============
:green:`True`   :green:`True`  :red:`False`
==============  ============== ==============

.. code-block:: python
  :lineno-start: 121
  :emphasize-lines: 23-28

      def test_logical_disjunction(self):
          self.assertTrue(
              src.truth_table.logical_disjunction(
                  True, True
              )
          )
          self.assertTrue(
              src.truth_table.logical_disjunction(
                  True, False
              )
          )
          self.assertTrue(
              src.truth_table.logical_disjunction(
                  False, True
              )
          )
          self.assertFalse(
              src.truth_table.logical_disjunction(
                  False, False
              )
          )

      def test_exclusive_disjunction(self):
          self.assertFalse(
              src.truth_table.exclusive_disjunction(
                  True, True
              )
          )


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'exclusive_disjunction'

because ``truth_table.py`` does not have anything in it with that name

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add :ref:`exclusive_disjunction<test_exclusive_disjunction>` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 52
  :emphasize-lines: 5-6

  def logical_disjunction(first_input, second_input):
      return first_input or second_input


  def exclusive_disjunction(first_input, second_input):
      return False

the test passes. :ref:`exclusive_disjunction<test_exclusive_disjunction>` returns :red:`False`, if the first input is :green:`True` and the second input is :green:`True`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for the next case, which is when the first input is :green:`True` and the second input is :red:`False`, to :ref:`test_exclusive_disjunction` in ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :red:`False`   :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 143
    :emphasize-lines: 7-11

        def test_exclusive_disjunction(self):
            self.assertFalse(
                src.truth_table.exclusive_disjunction(
                    True, True
                )
            )
            self.assertTrue(
                src.truth_table.exclusive_disjunction(
                    True, False
                )
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

  because the :ref:`function<what is a function?>` returns :red:`False` and the :ref:`assertion<what is an assertion?>` expects :green:`True`

* I add an :ref:`if statement<if statements>` to the :ref:`exclusive_disjunction function<test_exclusive_disjunction>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 2-3

    def exclusive_disjunction(first_input, second_input):
        if second_input == False:
            return True
        return False

  the test passes. :ref:`exclusive_disjunction<test_exclusive_disjunction>` returns

  - :green:`True`, if the second input is :red:`False`
  - :red:`False`, if the above condition is NOT met

* I add an :ref:`assertion<what is an assertion?>` for the third case, which is when the first input is :red:`False` and the second input is :green:`True`, to ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :green:`True`  :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 143
    :emphasize-lines: 12-16

        def test_exclusive_disjunction(self):
            self.assertFalse(
                src.truth_table.exclusive_disjunction(
                    True, True
                )
            )
            self.assertTrue(
                src.truth_table.exclusive_disjunction(
                    True, False
                )
            )
            self.assertTrue(
                src.truth_table.exclusive_disjunction(
                    False, True
                )
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

  because the :ref:`function<what is a function?>` returned :red:`False` and the :ref:`assertion<what is an assertion?>` expects :green:`True`

* I add an :ref:`if statement<if statements>` to :ref:`exclusive_disjunction<test_exclusive_disjunction>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 2-3

    def exclusive_disjunction(first_input, second_input):
        if first_input == False:
            return True
        if second_input == False:
            return True
        return False

  the test passes. :ref:`exclusive_disjunction<test_exclusive_disjunction>` returns

  - :green:`True`, if the first input is :red:`False`
  - :green:`True`, if the second input is :red:`False`
  - :red:`False`, if the above conditions are not met

* I add an :ref:`assertion<what is an assertion?>` for the last case, which is when the first input is :red:`False` and the second input is :red:`False` to :ref:`test_exclusive_disjunction`, in ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :red:`False`   :red:`False`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 143
    :emphasize-lines: 17-21

        def test_exclusive_disjunction(self):
            self.assertFalse(
                src.truth_table.exclusive_disjunction(
                    True, True
                )
            )
            self.assertTrue(
                src.truth_table.exclusive_disjunction(
                    True, False
                )
            )
            self.assertTrue(
                src.truth_table.exclusive_disjunction(
                    False, True
                )
            )
            self.assertFalse(
                src.truth_table.exclusive_disjunction(
                    False, False
                )
            )


    # Exceptions

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  because the :ref:`function<what is a function?>` returned :green:`True` and the :ref:`assertion<what is an assertion?>` expects :red:`False`

* I add an :ref:`if statement<if statements>` for this case, to the one for when the first input is :red:`False` in the :ref:`exclusive_disjunction function<test_exclusive_disjunction>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 3-4

    def exclusive_disjunction(first_input, second_input):
        if first_input == False:
            if second_input == False:
                return False
            return True
        if second_input == False:
            return True
        return False

  the test passes.

* there are two cases where :ref:`exclusive_disjunction<test_exclusive_disjunction>` returns :red:`False` and two cases where it returns :green:`True`. I add an :ref:`if statement<if statements>` for the other case where it returns :red:`False`, to make it clearer

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 6-8

    def exclusive_disjunction(first_input, second_input):
        if first_input == False:
            if second_input == False:
                return False
            return True
        if first_input == True:
            if second_input == False:
                return True
            return False

  the test is still green.

* I add the :ref:`bool built-in function<booleans 2: test with bool>`

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 2-5, 8-11

    def exclusive_disjunction(first_input, second_input):
        # if first_input == False:
        if bool(first_input) == False:
            # if second_input == False:
            if bool(second_input) == False:
                return False
            return True
        # if first_input == True:
        if bool(first_input) == True:
            # if second_input == False:
            if bool(second_input) == False:
                return True
            return False

  still green.

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write three of the :ref:`if statements` in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 3-4, 6-7, 13-14

    def exclusive_disjunction(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        if not bool(first_input) == True:
            # if second_input == False:
            # if bool(second_input) == False:
            if not bool(second_input) == True:
                return False
            return True
        # if first_input == True:
        if bool(first_input) == True:
            # if second_input == False:
            # if bool(second_input) == False:
            if not bool(second_input) == True:
                return True
            return False

  green.

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 4-5, 8-9, 13-14, 17-18

    def exclusive_disjunction(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool(first_input) == True:
        if not bool(first_input):
            # if second_input == False:
            # if bool(second_input) == False:
            # if not bool(second_input) == True:
            if not bool(second_input):
                return False
            return True
        # if first_input == True:
        # if bool(first_input) == True:
        if bool(first_input):
            # if second_input == False:
            # if bool(second_input) == False:
            # if not bool(second_input) == True:
            if not bool(second_input):
                return True
            return False


  still green.

* I remove :ref:`bool<booleans 2: test with bool>`

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 5-6, 10-11, 16-17, 21-22

    def exclusive_disjunction(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool(first_input) == True:
        # if not bool(first_input):
        if not first_input:
            # if second_input == False:
            # if bool(second_input) == False:
            # if not bool(second_input) == True:
            # if not bool(second_input):
            if not second_input:
                return False
            return True
        # if first_input == True:
        # if bool(first_input) == True:
        # if bool(first_input):
        if first_input:
            # if second_input == False:
            # if bool(second_input) == False:
            # if not bool(second_input) == True:
            # if not bool(second_input):
            if not second_input:
                return True
            return False

  the test is still green, because

  - ``if bool(something) == False`` is the same as ``if not bool(something) == True`` is the same as ``if not bool(something)`` is the same as ``if not something``
  - ``if bool(something) == True`` is the same as ``if bool(something)`` is the same as ``if something``

* I move the :ref:`if statements` to put them together

  .. tip:: In `Visual Studio Code`_ I can move lines I select or where the cursor is, with :kbd:`alt/option+Up` on the keyboard to move lines up or :kbd:`alt/option+Down` to move lines down

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 17-21

    def exclusive_disjunction(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool(first_input) == True:
        # if not bool(first_input):
            # if second_input == False:
            # if bool(second_input) == False:
            # if not bool(second_input) == True:
            # if not bool(second_input):
        # if first_input == True:
        # if bool(first_input) == True:
        # if bool(first_input):
            # if second_input == False:
            # if bool(second_input) == False:
            # if not bool(second_input) == True:
            # if not bool(second_input):
        if not first_input:
            if not second_input:
                return False
            return True
        if first_input:
            if not second_input:
                return True
            return False

  still green.

* I add :ref:`if statements` for the other two cases to make it clearer

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 20-21, 25-26

    def exclusive_disjunction(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool(first_input) == True:
        # if not bool(first_input):
            # if second_input == False:
            # if bool(second_input) == False:
            # if not bool(second_input) == True:
            # if not bool(second_input):
        # if first_input == True:
        # if bool(first_input) == True:
        # if bool(first_input):
            # if second_input == False:
            # if bool(second_input) == False:
            # if not bool(second_input) == True:
            # if not bool(second_input):
        if not first_input:
            if not second_input:
                return False
            if second_input:
                return True
        if first_input:
            if not second_input:
                return True
            if second_input:
                return False

  green.

* I use :ref:`Logical Conjunction (AND)<test_logical_conjunction>` to write the :ref:`if statements` for all the cases

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 17-30

    def exclusive_disjunction(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool(first_input) == True:
        # if not bool(first_input):
            # if second_input == False:
            # if bool(second_input) == False:
            # if not bool(second_input) == True:
            # if not bool(second_input):
        # if first_input == True:
        # if bool(first_input) == True:
        # if bool(first_input):
            # if second_input == False:
            # if bool(second_input) == False:
            # if not bool(second_input) == True:
            # if not bool(second_input):
        # if not first_input:
        #     if not second_input:
        if not first_input and not second_input:
            return False
            # if second_input:
        if not first_input and second_input:
            return True
        # if first_input:
        #     if not second_input:
        if first_input and not second_input:
            return True
            # if second_input:
        if first_input and second_input:
            return False

  still green, because I can put two :ref:`if statements` together when one is indented under the other. For example

  .. code-block:: python

    if something:
        if something_else:

  can also be written as

  .. code-block:: python

    if something and something_else:

* I move the first :ref:`if statement<if statements>` to the bottom to be with the other statement that returns the same thing (:red:`False`)

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 27-28

    def exclusive_disjunction(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool(first_input) == True:
        # if not bool(first_input):
            # if second_input == False:
            # if bool(second_input) == False:
            # if not bool(second_input) == True:
            # if not bool(second_input):
        # if first_input == True:
        # if bool(first_input) == True:
        # if bool(first_input):
            # if second_input == False:
            # if bool(second_input) == False:
            # if not bool(second_input) == True:
            # if not bool(second_input):
        # if not first_input:
        #     if not second_input:
            # if second_input:
        if not first_input and second_input:
            return True
        # if first_input:
        #     if not second_input:
        if first_input and not second_input:
            return True
            # if second_input:
        if not first_input and not second_input:
            return False
        if first_input and second_input:
            return False

  the test is still green.

* I use :ref:`Logical Disjunction (OR)<test_logical_conjunction>` to put the :ref:`if statements` that return the same thing together

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 4-5, 8-13, 16-23

        # if not first_input:
        #     if not second_input:
            # if second_input:
        # if not first_input and second_input:
        #     return True
        # if first_input:
        #     if not second_input:
        # if first_input and not second_input:
        if (
            (not first_input and second_input)
            or
            (first_input and not second_input)
        ):
            return True
            # if second_input:
        # if not first_input and not second_input:
        #     return False
        # if first_input and second_input:
        if (
            (not first_input and not second_input)
            or
            (first_input and second_input)
        ):
            return False

  still green, because I can put two :ref:`if statements` together when they both return the same thing and are at the same indentation level. For example

  .. code-block:: python

    if something:
        return this
    if something_else:
        return this

  can also be written as

  .. code-block:: python

    if something or something_else:
        return this

* I change the second :ref:`if statement<if statements>` to an :ref:`else clause<if statements>`

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 11-16

        if (
            (not first_input and second_input)
            or
            (first_input and not second_input)
        ):
            return True
            # if second_input:
        # if not first_input and not second_input:
        #     return False
        # if first_input and second_input:
        if (
            (not first_input and not second_input)
            or
            (first_input and second_input)
        ):
        else:
            return False

  green.

* I add a :ref:`conditional expression<conditional expressions>`

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 1-6, 16-22

        # if (
        #     (not first_input and second_input)
        #     or
        #     (first_input and not second_input)
        # ):
        #     return True
            # if second_input:
        # if not first_input and not second_input:
        #     return False
        # if first_input and second_input:
        # if (
        #     (not first_input and not second_input)
        #     or
        #     (first_input and second_input)
        # ):
        # else:
        #     return False
        return True if (
            (not first_input and second_input)
            or
            (first_input and not second_input)
        ) else False

  still green.

* I remove ``True if`` and ``else False`` to make it simpler

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 42-51

        # if (
        #     (not first_input and second_input)
        #     or
        #     (first_input and not second_input)
        # ):
        #     return True
            # if second_input:
        # if not first_input and not second_input:
        #     return False
        # if first_input and second_input:
        # if (
        #     (not first_input and not second_input)
        #     or
        #     (first_input and second_input)
        # ):
        # else:
        #     return False
        # return True if (
        #     (not first_input and second_input)
        #     or
        #     (first_input and not second_input)
        # ) else False
        return (
            (not first_input and second_input)
            or
            (first_input and not second_input)
        )

  the test is still green.

* :ref:`exclusive_disjunction<test_exclusive_disjunction>` returns ``((not first_input and second_input) or (first_input and not second_input))``

  - ``not first_input and second_input`` is the :ref:`Logical Conjunction (AND)<test_logical_conjunction>` of the :ref:`Logical Negation (NOT)<test_logical_negation>` of the first input, and the second input

    .. code-block:: python

      logical_conjunction(
          logical_negation(first_input),
          second_input
      )

  - ``not first_input`` is the :ref:`Logical Negation (NOT)<test_logical_negation>` of ``first_input``

    * if the first input is :green:`True`, this part of the statement is :red:`False`
    * if the first input is :red:`False`, this part of the statement is :green:`True`

  - ``first_input and not second_input`` is the :ref:`Logical Conjunction (AND)<test_logical_conjunction>` of the first input, and the :ref:`Logical Negation (NOT)<test_logical_negation>` of the second input

    .. code-block:: python

      logical_conjunction(
          first_input,
          logical_negation(second_input)
      )

  - ``not second_input`` is the :ref:`Logical Negation (NOT)<test_logical_negation>` of ``second_input``

    * if the second input is :green:`True`, this part of the statement is :red:`False`
    * if the second input is :red:`False`, this part of the statement is :green:`True`

  - ``((not first_input and second_input) or (first_input and not second_input))`` can be thought of as the :ref:`Logical Disjunction (OR)<test_logical_disjunction>` of the :ref:`Logical Conjunction (AND)<test_logical_conjunction>` of the :ref:`Logical Negation (NOT)<test_logical_negation>` of the first input, and the second input, and the :ref:`Logical Conjunction (AND)<test_logical_conjunction>` of the first input, and the :ref:`Logical Negation (NOT)<test_logical_negation>` of the second input. Very confusing when written in English

    .. code-block:: python

      logical_disjunction(
          logical_conjunction(
              logical_negation(first_input),
              second_input
          ),
          logical_conjunction(
              first_input,
              logical_negation(second_input)
          )
      )

    it can be thought of as the :ref:`Logical Disjunction (OR)<test_logical_disjunction>` of the :ref:`Converse Non-Implication<test_converse_non_implication>` of the first input, and the second input, and the :ref:`Logical Conjunction (AND)<test_logical_conjunction>` of the first input, and the :ref:`Logical Negation (NOT)<test_logical_negation>` of the second input

    .. code-block:: python

      logical_disjunction(
          converse_non_implication(
              first_input,
              second_input
          ),
          logical_conjunction(
              first_input,
              logical_negation(second_input)
          )
      )

    because :ref:`converse_non_implication<test_converse_non_implication>` returns ``not first_input and second_input``

  This means that in the four cases

  * if the first input is :green:`True` and the second input is :green:`True`, :ref:`exclusive_disjunction<test_exclusive_disjunction>` returns

    .. code-block:: python
      :emphasize-lines: 5

      (not first and second) or (first and not second)
      (not True  and True  ) or (True  and not True  )
      (False     and True  ) or (True  and False     )
       False                 or  False
       False                 # logical_disjunction(False, False)

  * if the first input is :green:`True` and the second input is :red:`False`, :ref:`exclusive_disjunction<test_exclusive_disjunction>` returns

    .. code-block:: python
      :emphasize-lines: 5
      :force:

      (not first and second) or (first and not second)
      (not True  and False ) or (True  and not False )
      (False     and False ) or (True  and True      )
       False                 or  True
       True                  # logical_disjunction(False, True)

  * if the first input is :red:`False` and the second input is :green:`True`, :ref:`exclusive_disjunction<test_exclusive_disjunction>` returns

    .. code-block:: python
      :emphasize-lines: 5

      (not first and second) or (first and not second)
      (not False and True  ) or (False and not True  )
      (True      and True  ) or (False and False     )
       True                  or  False
       True                  # logical_disjunction(True, False)

  * if the first input is :red:`False` and the second input is :red:`False`, :ref:`exclusive_disjunction<test_exclusive_disjunction>` returns

    .. code-block:: python
      :emphasize-lines: 5

      (not first and second) or (first and not second)
      (not False and False ) or (False and not False )
      (True      and False ) or (False and True      )
       False                 or  False
       False                 # logical_disjunction(False, False)

  ==============  =============== =============== ================  ================  ================= ========================
  first           second          not first       not second        ((not first)      (first            ((not first) and second)
                                                                    and               and               or
                                                                    second)           (not second))     (first and (not second))
  ==============  =============== =============== ================  ================  ================= ========================
  :green:`True`   :green:`True`   :red:`False`    :red:`False`      :red:`False`      :red:`False`      :red:`False`
  :green:`True`   :red:`False`    :red:`False`    :green:`True`     :red:`False`      :green:`True`     :green:`True`
  :red:`False`    :green:`True`   :green:`True`   :red:`False`      :green:`True`     :red:`False`      :green:`True`
  :red:`False`    :red:`False`    :green:`True`   :green:`True`     :red:`False`      :red:`False`      :red:`False`
  ==============  =============== =============== ================  ================  ================= ========================

  I add a `return statement`_ to show this

  .. code-block:: python
    :lineno-start: 103
    :emphasize-lines: 52-56

    # return True if (
    #     (not first_input and second_input)
    #     or
    #     (first_input and not second_input)
    # ) else False
    return logical_disjunction(
        converse_non_implication(
            first_input,
            second_input
        ),
        logical_conjunction(
            first_input,
            logical_negation(second_input)
        )
    )
    return (
        (not first_input and second_input)
        or
        (first_input and not second_input)
    )

  the test is still green.

* :ref:`exclusive_disjunction<test_exclusive_disjunction>` returns :red:`False` when ``first_input`` and ``second_input`` are the same and returns :green:`True`, if they are NOT. I add an :ref:`if statement<if statements>` to show this with the equality symbol (2 equal signs together :kbd:`=+=` on the keyboard)

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 6-15

        # return True if (
        #     (not first_input and second_input)
        #     or
        #     (first_input and not second_input)
        # ) else False
        return logical_disjunction(
            converse_non_implication(
                first_input,
                second_input
            ),
            logical_conjunction(
                first_input,
                logical_negation(second_input)
            )
        )
        return (
            (not first_input and second_input)
            or
            (first_input and not second_input)
        )

  still green.

* :ref:`exclusive_disjunction<test_exclusive_disjunction>` returns :red:`False` when the two inputs are equal, it returns :green:`True` when the two inputs are NOT equal. I add an :ref:`if statement<if statements>` to show this

  .. code-block:: python
    :lineno-start: 103
    :emphasize-lines: 6-9

        # return True if (
        #     (not first_input and second_input)
        #     or
        #     (first_input and not second_input)
        # ) else False
        if first_input == second_input:
            return False
        else:
            return True
        return logical_disjunction(
            converse_non_implication(
                first_input,
                second_input
            ),
            logical_conjunction(
                first_input,
                logical_negation(second_input)
            )
        )
        return (
            (not first_input and second_input)
            or
            (first_input and not second_input)
        )

  green.

* I change the :ref:`else clause<if statements>` to the :ref:`Logical Negation (NOT)<test_logical_negation>` of the new :ref:`if statement<if statements>` so I can write a :ref:`conditional expression<conditional expressions>`

  .. code-block:: python
    :lineno-start: 108
    :emphasize-lines: 3-4

        if first_input == second_input:
            return False
        # else:
        if not (first_input == second_input):
            return True
        return logical_disjunction(
            converse_non_implication(
                first_input,
                second_input
            ),
            logical_conjunction(
                first_input,
                logical_negation(second_input)
            )
        )
        return (
            (not first_input and second_input)
            or
            (first_input and not second_input)
        )

  still green.

* I add a :ref:`conditional expression<conditional expressions>`

  .. code-block:: python
    :lineno-start: 108
    :emphasize-lines: 1-2, 4-10

        # if first_input == second_input:
        #     return False
        # else:
        # if not (first_input == second_input):
        #     return True
        return (
            True if
            not (first_input == second_input)
            else False
        )
        return logical_disjunction(
            converse_non_implication(
                first_input,
                second_input
            ),
            logical_conjunction(
                first_input,
                logical_negation(second_input)
            )
        )
        return (
            (not first_input and second_input)
            or
            (first_input and not second_input)
        )

  the test is still green.

* I remove ``True if`` and ``else False`` to make the statement simpler

  .. code-block:: python
    :lineno-start: 108
    :emphasize-lines: 6-11

        # if first_input == second_input:
        #     return False
        # else:
        # if not (first_input == second_input):
        #     return True
        # return (
        #     True if
        #     not (first_input == second_input)
        #     else False
        # )
        return not (first_input == second_input)
        return logical_disjunction(
            converse_non_implication(
                first_input,
                second_input
            ),
            logical_conjunction(
                first_input,
                logical_negation(second_input)
            )
        )
        return (
            (not first_input and second_input)
            or
            (first_input and not second_input)
        )

  still green.

* I can also write the :ref:`conditional expression<conditional expressions>` with the NOT equal symbol (``!=``) (exclamation mark and equal symbol :kbd:`!+=` on the keyboard)

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 57

    def exclusive_disjunction(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool(first_input) == True:
        # if not bool(first_input):
            # if second_input == False:
            # if bool(second_input) == False:
            # if not bool(second_input) == True:
            # if not bool(second_input):
        # if first_input == True:
        # if bool(first_input) == True:
        # if bool(first_input):
            # if second_input == False:
            # if bool(second_input) == False:
            # if not bool(second_input) == True:
            # if not bool(second_input):
        # if not first_input:
        #     if not second_input:
            # if second_input:
        # if not first_input and second_input:
        #     return True
        # if first_input:
        #     if not second_input:
        # if first_input and not second_input:
        # if (
        #     (not first_input and second_input)
        #     or
        #     (first_input and not second_input)
        # ):
        #     return True
            # if second_input:
        # if not first_input and not second_input:
        #     return False
        # if first_input and second_input:
        # if (
        #     (not first_input and not second_input)
        #     or
        #     (first_input and second_input)
        # ):
        # else:
        #     return False
        # return True if (
        #     (not first_input and second_input)
        #     or
        #     (first_input and not second_input)
        # ) else False
        # if first_input == second_input:
        #     return False
        # else:
        # if not (first_input == second_input):
        #     return True
        # return (
        #     True if
        #     not (first_input == second_input)
        #     else False
        # )
        return first_input != second_input
        return not (first_input == second_input)
        return logical_disjunction(
            converse_non_implication(
                first_input,
                second_input
            ),
            logical_conjunction(
                first_input,
                logical_negation(second_input)
            )
        )
        return (
            (not first_input and second_input)
            or
            (first_input and not second_input)
        )

  green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 62

    def exclusive_disjunction(first_input, second_input):
        return first_input != second_input
        return not (first_input == second_input)
        return logical_disjunction(
            converse_non_implication(
                first_input,
                second_input
            ),
            logical_conjunction(
                first_input,
                logical_negation(second_input)
            )
        )
        return (
            (not first_input and second_input)
            or
            (first_input and not second_input)
        )

  I can use any of these `return statements`_. The first `return statement`_ is the only one that runs in this case, because :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`.

:ref:`Exclusive Disjunction<test_exclusive_disjunction>` returns

* :green:`True`, if the first input is NOT EQUAL to the second input
* :red:`False`, if the first input is EQUAL to the second input
* ``first_input != second_input`` - which reads as first input is NOT equal to second input
* ``not (first_input == second_input)`` - which reads as the :ref:`Logical Negation<test_logical_negation>` of the :ref:`Logical Equality<test_logical_equality>` of the first input and the second input. Ha ha ha.
* ``(not first_input and second_input) or (first_input and not second_input)`` which is the :ref:`Logical Disjunction<test_logical_disjunction>` of the :ref:`Logical Conjunction<test_logical_conjunction>` of the :ref:`Logical Negation<test_logical_negation>` of the first input, and the second input, and the :ref:`Logical Conjunction<test_logical_conjunction>` of the first input and the :ref:`Logical Negation<test_logical_negation>` of the second input. Wow! That's a lot.
* All of the above statements mean the same thing.

:ref:`Exclusive Disjunction<test_exclusive_disjunction>` is also known as `Exclusive OR`_ or XOR_. Would "Logical Inequality" be a better name?

----

=================================================================================
examples of Exclusive Disjunction
=================================================================================

----

* two light switches for one bulb, if the inputs are

  - is switch A on?
  - is switch B on?

  ================  ==================  ==================
  switch A?         switch B?           bulb
  ================  ==================  ==================
  :green:`on`       :green:`on`         :red:`off`
  :green:`on`       :red:`off`          :green:`on`
  :red:`off`        :green:`on`         :green:`on`
  :red:`off`        :red:`off`          :red:`off`
  ================  ==================  ==================

* magnets attract or repel, if the inputs are

  - what is the direction of magnet A?
  - what is the direction of magnet B?

  ================  ==================  ==================
  magnet A?         magnet B?           attract/repel
  ================  ==================  ==================
  :green:`north`    :green:`north`      :red:`repel`
  :green:`north`    :red:`south`        :green:`attract`
  :red:`south`      :green:`north`      :green:`attract`
  :red:`south`      :red:`south`        :red:`repel`
  ================  ==================  ==================

* a coin toss, if the inputs are

  - my choice
  - your choice

  ================  ==================  ==================
  my choice         your choice         there is a winner
  ================  ==================  ==================
  :green:`heads`    :green:`heads`      :red:`no`
  :green:`heads`    :red:`tails`        :green:`yes`
  :red:`tails`      :green:`heads`      :green:`yes`
  :red:`tails`      :red:`tails`        :red:`no`
  ================  ==================  ==================

* two people meet at a door that can only take one person at a time, if the inputs are

  - I go
  - You go

  ================  ==================  ==================
  I go              you go              we both go
  ================  ==================  ==================
  :green:`go`       :green:`go`         :red:`no`
  :green:`go`       :red:`stop`         :green:`yes`
  :red:`stop`       :green:`go`         :green:`yes`
  :red:`stop`       :red:`stop`         :red:`no`
  ================  ==================  ==================

* A broken vending machine, if the inputs are

  - did I put money in the machine?
  - did I get what I picked?

  ================  ==================  ==================
  I paid            I got what I want   machine is broken
  ================  ==================  ==================
  :green:`yes`      :green:`yes`        :red:`no`
  :green:`yes`      :red:`no`           :green:`yes`
  :red:`no`         :green:`yes`        :green:`yes`
  :red:`no`         :red:`no`           :red:`no`
  ================  ==================  ==================

----

*********************************************************************************
test_material_non_implication
*********************************************************************************

The :ref:`truth table` for :ref:`material_non_implication<test_material_non_implication>` is

==============  ============== ==============
first input     second input   return
==============  ============== ==============
:green:`True`   :green:`True`  :red:`False`
:green:`True`   :red:`False`   :green:`True`
:red:`False`    :green:`True`  :red:`False`
:red:`False`    :red:`False`   :red:`False`
==============  ============== ==============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for :ref:`material_non_implication<test_material_non_implication>` with an :ref:`assertion<what is an assertion?>` for when the first input is :green:`True` and the second input is :green:`True`, to ``test_binary.py``

==============  ============== ==============
first input     second input   return
==============  ============== ==============
:green:`True`   :green:`True`  :red:`False`
==============  ============== ==============

.. code-block:: python
  :lineno-start: 143
  :emphasize-lines: 23-28

      def test_exclusive_disjunction(self):
          self.assertFalse(
              src.truth_table.exclusive_disjunction(
                  True, True
              )
          )
          self.assertTrue(
              src.truth_table.exclusive_disjunction(
                  True, False
              )
          )
          self.assertTrue(
              src.truth_table.exclusive_disjunction(
                  False, True
              )
          )
          self.assertFalse(
              src.truth_table.exclusive_disjunction(
                  False, False
              )
          )

      def test_material_non_implication(self):
          self.assertFalse(
              src.truth_table.material_non_implication(
                  True, True
              )
          )


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'material_non_implication'. Did you mean: 'converse_non_implication'?

:ref:`material_non_implication<test_material_non_implication>` is not in ``truth_table.py``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add :ref:`material_non_implication<test_material_non_implication>` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 62
  :emphasize-lines: 21-22

  def exclusive_disjunction(first_input, second_input):
      return first_input != second_input
      return not (first_input == second_input)
      return logical_disjunction(
          converse_non_implication(
              first_input,
              second_input
          ),
          logical_conjunction(
              first_input,
              logical_negation(second_input)
          )
      )
      return (
          (not first_input and second_input)
          or
          (first_input and not second_input)
      )


  def material_non_implication(first_input, second_input):
      return False

the test passes. :ref:`material_non_implication<test_material_non_implication>` returns :red:`False`, if the first input is :green:`True` and the second input is :green:`True`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for the second case, which is when the first input is :green:`True` and the second input is :red:`False` to :ref:`test_material_non_implication` in ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :red:`False`   :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 165
    :emphasize-lines: 7-11

        def test_material_non_implication(self):
            self.assertFalse(
                src.truth_table.material_non_implication(
                    True, True
                )
            )
            self.assertTrue(
                src.truth_table.material_non_implication(
                    True, False
                )
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

  because the :ref:`function<what is a function?>` returns :red:`False` and the :ref:`assertion<what is an assertion?>` expects :green:`True`

* I add an :ref:`if statement<if statements>` to :ref:`material_non_implication<test_material_non_implication>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 2-3

    def material_non_implication(first_input, second_input):
        if second_input == False:
            return True
        return False

  the test passes. :ref:`material_non_implication<test_material_non_implication>` returns

  - :green:`True`, if the second input is :red:`False`
  - :red:`False`, if the above condition is NOT met

* I add an :ref:`assertion<what is an assertion?>` for the third case to :ref:`test_material_non_implication`, for when the first input is :red:`False` and the second input is :green:`True`, in ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :green:`True`  :red:`False`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 165
    :emphasize-lines: 12-16

        def test_material_non_implication(self):
            self.assertFalse(
                src.truth_table.material_non_implication(
                    True, True
                )
            )
            self.assertTrue(
                src.truth_table.material_non_implication(
                    True, False
                )
            )
            self.assertFalse(
                src.truth_table.material_non_implication(
                    False, True
                )
            )


    # Exceptions seen

  the test is still green. :ref:`material_non_implication<test_material_non_implication>` returns

  - :green:`True`, if the second input is :red:`False`
  - :red:`False`, if the above condition is NOT met

* I add an :ref:`assertion<what is an assertion?>` for the fourth case, which is when the first input is :red:`False` and the second input is :red:`False`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :red:`False`   :red:`False`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 165
    :emphasize-lines: 17-21

        def test_material_non_implication(self):
            self.assertFalse(
                src.truth_table.material_non_implication(
                    True, True
                )
            )
            self.assertTrue(
                src.truth_table.material_non_implication(
                    True, False
                )
            )
            self.assertFalse(
                src.truth_table.material_non_implication(
                    False, True
                )
            )
            self.assertFalse(
                src.truth_table.material_non_implication(
                    False, False
                )
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  because the :ref:`function<what is a function?>` returned :green:`True` and the :ref:`assertion<what is an assertion?>` expects :red:`False`

* I add an :ref:`if statement<if statements>` for the one case that returns :green:`True` to the :ref:`material_non_implication function<test_material_non_implication>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 2-4

    def material_non_implication(first_input, second_input):
        if first_input == True:
            if second_input == False:
                return True
        return False

  the test passes.

* I use the :ref:`bool built-in function<booleans 2: test with bool>`

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 2-5

    def material_non_implication(first_input, second_input):
        # if first_input == True:
        if bool(first_input) == True:
            # if second_input == False:
            if bool(second_input) == False:
                return True
        return False

  the test is still green.

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write the second :ref:`if statement<if statements>` in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 5-6

    def material_non_implication(first_input, second_input):
        # if first_input == True:
        if bool(first_input) == True:
            # if second_input == False:
            # if bool(second_input) == False:
            if not bool(second_input) == True:
                return True
        return False

  still green.

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 3-4, 7-8

    def material_non_implication(first_input, second_input):
        # if first_input == True:
        # if bool(first_input) == True:
        if bool(first_input):
            # if second_input == False:
            # if bool(second_input) == False:
            # if not bool(second_input) == True:
            if not bool(second_input):
                return True
        return False

  green.

* I remove :ref:`bool<booleans 2: test with bool>`

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 4-5, 9-10

    def material_non_implication(first_input, second_input):
        # if first_input == True:
        # if bool(first_input) == True:
        # if bool(first_input):
        if first_input:
            # if second_input == False:
            # if bool(second_input) == False:
            # if not bool(second_input) == True:
            # if not bool(second_input):
            if not second_input:
                return True
        return False

  still green, because

  - ``if bool(something) == True`` is the same as ``if bool(something)`` is the same as ``if something``
  - ``if bool(something) == False`` is the same as ``if not bool(something) == True`` is the same as ``if not bool(something)`` is the same as ``if not something``

* I use :ref:`Logical Conjunction (AND)<test_logical_conjunction>` to put the two :ref:`if statements` together

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 5, 10-11

    def material_non_implication(first_input, second_input):
        # if first_input == True:
        # if bool(first_input) == True:
        # if bool(first_input):
        # if first_input:
            # if second_input == False:
            # if bool(second_input) == False:
            # if not bool(second_input) == True:
            # if not bool(second_input):
            # if not second_input:
        if first_input and not second_input:
                return True
        return False

  the test is still green, because I can put two :ref:`if statements` together when one is indented under the other. For example

  .. code-block:: python

    if something:
        if something_else:

  can also be written as

  .. code-block:: python

    if something and something_else:

* I add a :ref:`conditional expression<conditional expressions>`

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 11-18

    def material_non_implication(first_input, second_input):
        # if first_input == True:
        # if bool(first_input) == True:
        # if bool(first_input):
        # if first_input:
            # if second_input == False:
            # if bool(second_input) == False:
            # if not bool(second_input) == True:
            # if not bool(second_input):
            # if not second_input:
        # if first_input and not second_input:
        #         return True
        # return False
        return (
            True if
            first_input and not second_input
            else False
        )

  still green.

* I remove ``True if`` and ``else False`` to make the statement simpler

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 4-9

        # if first_input and not second_input:
        #         return True
        # return False
        # return (
        #     True if
        #     first_input and not second_input
        #     else False
        # )
        return first_input and not second_input

  green.

* :ref:`material_non_implication<test_material_non_implication>` returns ``first_input and not second_input``

  - ``not second_input`` is the :ref:`Logical Negation (NOT)<test_logical_negation>` of ``second_input``

    * if the second input is :green:`True`, this part of the statement is :red:`False`
    * if the second input is :red:`False`, this part of the statement is :green:`True`
  - ``first_input and not second_input`` is the :ref:`Logical Conjunction (AND)<test_logical_conjunction>` of the first input and the :ref:`Logical Negation (NOT)<test_logical_negation>` of the second input

    .. code-block:: python

      logical_conjunction(
          first_input,
          logical_negation(second_input)
      )

  this means that in the four cases

  - if the first input is :green:`True` and the second input is :green:`True`, :ref:`material_non_implication<test_material_non_implication>` returns

    .. code-block:: python
      :emphasize-lines: 4

      first_input and not second_input
      True        and not True
      True        and False
      False       # logical_conjunction(True, False)

  - if the first input is :green:`True` and the second input is :red:`False`, :ref:`material_non_implication<test_material_non_implication>` returns

    .. code-block:: python
      :emphasize-lines: 4

      first_input and not second_input
      True        and not False
      True        and True
      True        # logical_conjunction(True, True)

  - if the first input is :red:`False` and the second input is :green:`True`, :ref:`material_non_implication<test_material_non_implication>` returns

    .. code-block:: python
      :emphasize-lines: 4

      first_input and not second_input
      False       and not True
      False       and False
      False       # logical_conjunction(False, False)

  - if the first input is :red:`False` and the second input is :red:`False`, :ref:`material_non_implication<test_material_non_implication>` returns

    .. code-block:: python
      :emphasize-lines: 4

      first_input and not second_input
      False       and not False
      False       and True
      False       # logical_conjunction(False, True)

  ==============  =============== =============== =======================
  first           second          not second      (first and not second)
  ==============  =============== =============== =======================
  :green:`True`   :green:`True`   :red:`False`    :red:`False`
  :green:`True`   :red:`False`    :green:`True`   :green:`True`
  :red:`False`    :green:`True`   :red:`False`    :red:`False`
  :red:`False`    :red:`False`    :green:`True`   :red:`False`
  ==============  =============== =============== =======================

  I add a `return statement`_ to show this

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 19-22

    def material_non_implication(first_input, second_input):
        # if first_input == True:
        # if bool(first_input) == True:
        # if bool(first_input):
        # if first_input:
            # if second_input == False:
            # if bool(second_input) == False:
            # if not bool(second_input) == True:
            # if not bool(second_input):
            # if not second_input:
        # if first_input and not second_input:
        #         return True
        # return False
        # return (
        #     True if
        #     first_input and not second_input
        #     else False
        # )
        return logical_conjunction(
            first_input,
            logical_negation(second_input)
        )
        return first_input and not second_input

  still green.

* I remove the comments

  .. code-block:: python
    :lineno-start: 71

    def material_non_implication(first_input, second_input):
        return logical_conjunction(
            first_input,
            logical_negation(second_input)
        )
        return first_input and not second_input

  I can use either of these `return statements`_. The first `return statement`_ is the only one that runs in this case, because :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`.

:ref:`Material Non-Implication<test_material_non_implication>`

* returns ``first_input and not second_input`` which is the :ref:`Logical Conjunction<test_logical_conjunction>` of the first input and the :ref:`Logical Negation<test_logical_negation>` of the second input
* returns :green:`True`, only if the first input is :green:`True` and the second input is :red:`False`
* is the :ref:`Logical Negation<test_logical_negation>` of :ref:`Material/Logical Implication<test_material_implication>` which returns :red:`False` only if the first input is :green:`True` and the second input is :red:`False`
* can be thought of as a claim that does not deliver

----

=================================================================================
examples of Material Non-Implication
=================================================================================

----

* A broken promise, if the inputs are

  - did I make a promise?
  - did I do something?

  ================  ==================  ==================
  I promised        I did something     broken promise
  ================  ==================  ==================
  :green:`yes`      :green:`yes`        :red:`no`
  :green:`yes`      :red:`no`           :green:`yes`
  :red:`no`         :green:`yes`        :red:`no`
  :red:`no`         :red:`no`           :red:`no`
  ================  ==================  ==================

* A false alarm, if the inputs are

  - did alarm ring?
  - was there a bad event?

  ================  ==================  ==================
  alarm rang        bad event           false alarm
  ================  ==================  ==================
  :green:`yes`      :green:`yes`        :red:`no`
  :green:`yes`      :red:`no`           :green:`yes`
  :red:`no`         :green:`yes`        :red:`no` (alarm is broken)
  :red:`no`         :red:`no`           :red:`no`
  ================  ==================  ==================

* the boy who cried wolf, if the inputs are

  - did the boy cry?
  - was there a wolf?

  ================  ==================  ==================
  boy cried         wolf                false claim
  ================  ==================  ==================
  :green:`yes`      :green:`yes`        :red:`no`
  :green:`yes`      :red:`no`           :green:`yes`
  :red:`no`         :green:`yes`        :red:`no`
  :red:`no`         :red:`no`           :red:`no`
  ================  ==================  ==================

----

*********************************************************************************
more about Exclusive Disjunction
*********************************************************************************

----

Since I now know :ref:`material_non_implication<test_material_non_implication>` I can think of :ref:`Exclusive Disjunction<test_exclusive_disjunction>` which returns ``(not first_input and second_input) or (first_input and not second_input)`` as

.. code-block:: python

  return logical_disjunction(
      converse_non_implication(
          first_input, second_input
      ),
      material_non_implication(
          first_input, second_input
      )
  )

because

* :ref:`logical_disjunction<test_logical_disjunction>` returns ``first_input or second_input``

  - ``first_input`` in this case is ``(not first_input and second_input)``
  - ``second_input`` in this case is ``(first_input and not second_input)``

* :ref:`converse_non_implication<test_converse_non_implication>` returns ``not first_input and second_input``
* :ref:`material_non_implication<test_material_non_implication>` returns ``first_input and not second_input``

I change the `return statement`_ in the :ref:`exclusive_disjunction function<test_exclusive_disjunction>` in ``truth_table.py``

.. code-block:: python
  :lineno-start: 62
  :emphasize-lines: 9, 11

  def exclusive_disjunction(first_input, second_input):
      return first_input != second_input
      return not (first_input == second_input)
      return logical_disjunction(
          converse_non_implication(
              first_input,
              second_input
          ),
          material_non_implication(
              first_input,
              second_input
          )
      )
      return (
          (not first_input and second_input)
          or
          (first_input and not second_input)
      )

----

*********************************************************************************
test_project_first
*********************************************************************************

The :ref:`truth table` for :ref:`project_first<test_project_first>` is

==============  ============== ==============
first input     second input   return
==============  ============== ==============
:green:`True`   :green:`True`  :green:`True`
:green:`True`   :red:`False`   :green:`True`
:red:`False`    :green:`True`  :red:`False`
:red:`False`    :red:`False`   :red:`False`
==============  ============== ==============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for :ref:`project_first<test_project_first>` with an :ref:`assertion<what is an assertion?>` for when the first input is :green:`True` and the second input is :green:`True`, in ``test_binary.py``

==============  ============== ==============
first input     second input   return
==============  ============== ==============
:green:`True`   :green:`True`  :green:`True`
==============  ============== ==============

.. code-block:: python
  :lineno-start: 165
  :emphasize-lines: 23-26

      def test_material_non_implication(self):
          self.assertFalse(
              src.truth_table.material_non_implication(
                  True, True
              )
          )
          self.assertTrue(
              src.truth_table.material_non_implication(
                  True, False
              )
          )
          self.assertFalse(
              src.truth_table.material_non_implication(
                  False, True
              )
          )
          self.assertFalse(
              src.truth_table.material_non_implication(
                  False, False
              )
          )

      def test_project_first(self):
          self.assertTrue(
              src.truth_table.project_first(True, True)
          )


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'project_first'

there is nothing named :ref:`project_first<test_project_first>` in ``truth_table.py``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a :ref:`function<what is a function?>` for :ref:`project_first<test_project_first>` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 82
  :emphasize-lines: 9-10

  def material_non_implication(first_input, second_input):
      return logical_conjunction(
          first_input,
          logical_negation(second_input)
      )
      return first_input and not second_input


  def project_first(first_input, second_input):
      return True

the test passes. :ref:`project_first<test_project_first>` returns :green:`True`, if the first input is :green:`True` and the second input is :green:`True`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for the second case, which is when the first input is :green:`True` and the second input is :red:`False`, to :ref:`test_project_first` in ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :red:`False`   :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 187
    :emphasize-lines: 5-7

        def test_project_first(self):
            self.assertTrue(
                src.truth_table.project_first(True, True)
            )
            self.assertTrue(
                src.truth_table.project_first(True, False)
            )


    # Exceptions seen

  the test is still green. :ref:`project_first<test_project_first>` returns

  - :green:`True`, if the first input is :green:`True` and the second input is :red:`False`
  - :green:`True`, if the first input is :green:`True` and the second input is :green:`True`
  - :green:`True`, if the first input is :green:`True`

* on to the next case, which is when the first input is :red:`False` and the second input is :green:`True`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :green:`True`  :red:`False`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 187
    :emphasize-lines: 8-10

        def test_project_first(self):
            self.assertTrue(
                src.truth_table.project_first(True, True)
            )
            self.assertTrue(
                src.truth_table.project_first(True, False)
            )
            self.assertFalse(
                src.truth_table.project_first(False, True)
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

  because the :ref:`function<what is a function?>` returns :green:`True` and the :ref:`assertion<what is an assertion?>` expects :red:`False`

* I add an :ref:`if statement<if statements>` for this case to the :ref:`project_first function<test_project_first>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 2-3

    def project_first(first_input, second_input):
        if first_input == False:
            return False
        return True

  the test passes. :ref:`project_first<test_project_first>` returns

  - :red:`False`, if the first input is :red:`False`
  - :green:`True`, if the above condition is NOT met

* I add an :ref:`assertion<what is an assertion?>` for the last case, which is when the first input is :red:`False` and the second input is :red:`False`, to :ref:`test_project_first` in ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :red:`False`   :red:`False`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 187
    :emphasize-lines: 11-13

        def test_project_first(self):
            self.assertTrue(
                src.truth_table.project_first(True, True)
            )
            self.assertTrue(
                src.truth_table.project_first(True, False)
            )
            self.assertFalse(
                src.truth_table.project_first(False, True)
            )
            self.assertFalse(
                src.truth_table.project_first(False, False)
            )


    # Exceptions seen

  the test is still green.

* I add the :ref:`bool built-in function<booleans 2: test with bool>` to the :ref:`if statement<if statements>` in the :ref:`project_first function<test_project_first>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 2-3

    def project_first(first_input, second_input):
        # if first_input == False:
        if bool(first_input) == False:
            return False
        return True

  still green.

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write it in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 3-4

    def project_first(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        if not bool(first_input) == True:
            return False
        return True

  green.

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 4-5

    def project_first(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool(first_input) == True:
        if not bool(first_input):
            return False
        return True

  still green.

* I remove :ref:`bool<booleans 2: test with bool>`

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 5-6

    def project_first(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool(first_input) == True:
        # if not bool(first_input):
        if not first_input:
            return False
        return True

  the test is still green, because ``if bool(something) == False`` is the same as ``if not bool(something) == True`` is the same as ``if not bool(something)`` is the same as ``if not something``

* I add an :ref:`else clause<if statements>` to make it clearer

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 8-9

    def project_first(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool(first_input) == True:
        # if not bool(first_input):
        if not first_input:
            return False
        else:
            return True

  still green.

* I use :ref:`Logical Negation (NOT)<if statements>` for the :ref:`else clause<if statements>`

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 8-9

    def project_first(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool(first_input) == True:
        # if not bool(first_input):
        if not first_input:
            return False
        # else:
        if not (not first_input):
            return True

  green.

* I remove the :ref:`nots<test_logical_negation>` because they cancel out

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 9-10

    def project_first(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool(first_input) == True:
        # if not bool(first_input):
        if not first_input:
            return False
        # else:
        # if not (not first_input):
        if first_input:
            return True

  still green.

* I add a :ref:`conditional expression<conditional expressions>`

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 6-7, 10-12

    def project_first(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool(first_input) == True:
        # if not bool(first_input):
        # if not first_input:
        #     return False
        # else:
        # if not (not first_input):
        # if first_input:
        #     return True
        return True if first_input else False

  the test is still green.

* I remove ``True if`` and ``else False``

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 13

    def project_first(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool(first_input) == True:
        # if not bool(first_input):
        # if not first_input:
        #     return False
        # else:
        # if not (not first_input):
        # if first_input:
        #     return True
        # return True if first_input else False
        return first_input

  still green.

* I remove the other statements

  .. code-block:: python
    :lineno-start: 90

    def project_first(first_input, second_input):
        return first_input

:ref:`Project First always returns the first input<test_project_first>` it does not care about the second input, like :ref:`Project Second which always returns the second input<test_project_second>` and does not care about the first input

----

=================================================================================
examples of Project First
=================================================================================

----

* did the event happen, if the inputs are

  - did the event happen?
  - did we get a notification about it?

  ================  ==================  ==================
  event             notification        event happened
  ================  ==================  ==================
  :green:`yes`      :green:`yes`        :green:`yes`
  :green:`yes`      :red:`no`           :green:`yes`
  :red:`no`         :green:`yes`        :red:`no` (notification is broken)
  :red:`no`         :red:`no`           :red:`no`
  ================  ==================  ==================

* able to login with or without Multi Factor Authentication, if the inputs are

  - did user provide the right password?
  - does user have MFA?

  ==============  ============== ==============
  right password  right MFA code log in
  ==============  ============== ==============
  :green:`yes`    :green:`yes`   :green:`yes`
  :green:`yes`    :red:`no`      :green:`yes` (why ask for MFA code?)
  :red:`no`       :green:`yes`   :red:`no` (how did user get the MFA code?)
  :red:`no`       :red:`no`      :red:`no`
  ==============  ============== ==============

* my actions, if the inputs are

  - what I want to do?
  - what you think I should do?

  ==============  ============== ==============
  what I want     your thoughts  what happens
  ==============  ============== ==============
  :green:`yes`    :green:`yes`   :green:`yes`
  :green:`yes`    :red:`no`      :green:`yes`
  :red:`no`       :green:`yes`   :red:`no`
  :red:`no`       :red:`no`      :red:`no`
  ==============  ============== ==============

* autocorrect, if the inputs are

  - autocorrect suggests a word
  - I write what I want

  ==============  ============== ==============
  autocorrect     what I want    what I get
  ==============  ============== ==============
  :green:`yes`    :green:`yes`   :green:`yes`
  :green:`yes`    :red:`no`      :green:`yes`
  :red:`no`       :green:`yes`   :red:`no`
  :red:`no`       :red:`no`      :red:`no`
  ==============  ============== ==============

----

*********************************************************************************
test_converse_implication
*********************************************************************************

The :ref:`truth table` for :ref:`converse_implication<test_converse_implication>` is

==============  ============== ==============
first input     second input   return
==============  ============== ==============
:green:`True`   :green:`True`  :green:`True`
:green:`True`   :red:`False`   :green:`True`
:red:`False`    :green:`True`  :red:`False`
:red:`False`    :red:`False`   :green:`True`
==============  ============== ==============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for :ref:`converse_implication<test_converse_implication>` with an :ref:`assertion<what is an assertion?>` for when the first input is :green:`True` and the second input is :green:`True`, to ``test_binary.py``

==============  ============== ==============
first input     second input   return
==============  ============== ==============
:green:`True`   :green:`True`  :green:`True`
==============  ============== ==============

.. code-block:: python
  :lineno-start: 187
  :emphasize-lines: 15-20

      def test_project_first(self):
          self.assertTrue(
              src.truth_table.project_first(True, True)
          )
          self.assertTrue(
              src.truth_table.project_first(True, False)
          )
          self.assertFalse(
              src.truth_table.project_first(False, True)
          )
          self.assertFalse(
              src.truth_table.project_first(False, False)
          )

      def test_converse_implication(self):
          self.assertTrue(
              src.truth_table.converse_implication(
                  True, True
              )
          )


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'converse_implication'. Did you mean: 'converse_non_implication'?

because ``truth_table.py`` does not have anything named :ref:`converse_implication<test_converse_implication>` in it

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a :ref:`function<what is a function?>` for :ref:`converse_implication<test_converse_implication>` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 90
  :emphasize-lines: 5-6

  def project_first(first_input, second_input):
      return first_input


  def converse_implication(first_input, second_input):
      return True

the test passes. :ref:`converse_implication<test_converse_implication>` returns :green:`True`, if the first input is :green:`True` and the second input is :green:`True`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for the second case, which is when the first input is :green:`True` and the second input is :red:`False` to :ref:`test_converse_implication` in ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :red:`False`   :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 201
    :emphasize-lines: 7-11

        def test_converse_implication(self):
            self.assertTrue(
                src.truth_table.converse_implication(
                    True, True
                )
            )
            self.assertTrue(
                src.truth_table.converse_implication(
                    True, False
                )
            )


    # Exceptions seen

  the test is still green.

* time for the next case, which is when the first input is :red:`False` and the second input is :green:`True`

  .. code-block:: python
    :lineno-start: 201
    :emphasize-lines: 12-16

        def test_converse_implication(self):
            self.assertTrue(
                src.truth_table.converse_implication(
                    True, True
                )
            )
            self.assertTrue(
                src.truth_table.converse_implication(
                    True, False
                )
            )
            self.assertFalse(
                src.truth_table.converse_implication(
                    False, True
                )
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

  because the :ref:`converse_implication function<test_converse_implication>` returns :green:`True` and the :ref:`assertion<what is an assertion?>` expects :red:`False`

* I add an :ref:`if statement<if statements>` to :ref:`converse_implication<test_converse_implication>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 2-3

    def converse_implication(first_input, second_input):
        if first_input == False:
            return False
        return True

  the test passes. :ref:`converse_implication<test_converse_implication>` returns

  - :red:`False`, if the first input is :red:`False`
  - :green:`True`, if the above condition is NOT met

* I add an :ref:`assertion<what is an assertion?>` for the last case, which is when the first input is :red:`False` and the second input is :red:`False`, to :ref:`test_converse_implication` in ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :red:`False`   :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 201
    :emphasize-lines: 17-21

        def test_converse_implication(self):
            self.assertTrue(
                src.truth_table.converse_implication(
                    True, True
                )
            )
            self.assertTrue(
                src.truth_table.converse_implication(
                    True, False
                )
            )
            self.assertFalse(
                src.truth_table.converse_implication(
                    False, True
                )
            )
            self.assertTrue(
                src.truth_table.converse_implication(
                    False, False
                )
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  because the :ref:`converse_implication function<test_converse_implication>` returned :red:`False` and the :ref:`assertion<what is an assertion?>` expects :green:`True`

* I add an :ref:`if statement<if statements>` for the only case that returns :green:`True`

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 3-4

    def converse_implication(first_input, second_input):
        if first_input == False:
            if second_input == True:
                return False
        return True

  the test passes.

* I add the :ref:`bool built-in function<booleans 2: test with bool>`

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 2-5

    def converse_implication(first_input, second_input):
        # if first_input == False:
        if bool(first_input) == False:
            # if second_input == True:
            if bool(second_input) == True:
                return False
        return True

  the test is still green.

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write the first :ref:`if statement<if statements>` in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 3-4

    def converse_implication(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        if not bool(first_input) == True:
            # if second_input == True:
            if bool(second_input) == True:
                return False
        return True

  still green.

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 4-5, 7-8

    def converse_implication(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool(first_input) == True:
        if not bool(first_input):
            # if second_input == True:
            # if bool(second_input) == True:
            if bool(second_input):
                return False
        return True

  green.

* I remove :ref:`bool<booleans 2: test with bool>`

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 5-6, 9-10

    def converse_implication(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool(first_input) == True:
        # if not bool(first_input):
        if not first_input:
            # if second_input == True:
            # if bool(second_input) == True:
            # if bool(second_input):
            if second_input:
                return False
        return True

  still green, because

  - ``if bool(something) == False`` is the same as ``if not bool(something) == True`` is the same as ``if not bool(something)`` is the same as ``if not something``
  - ``if bool(something) == True`` is the same as ``if bool(something)`` is the same as ``if something``

* I use :ref:`Logical Conjunction (AND)<test_logical_conjunction>` to put the two :ref:`if statements` together

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 6, 10-11

    def converse_implication(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool(first_input) == True:
        # if not bool(first_input):
        # if not first_input:
            # if second_input == True:
            # if bool(second_input) == True:
            # if bool(second_input):
            # if second_input:
        if not first_input and second_input:
                return False
        return True

  the test is still green, because I can put two :ref:`if statements` together when one is indented under the other. For example

  .. code-block:: python

    if something:
        if something_else:

  can also be written as

  .. code-block:: python

    if something and something_else:

* I add an :ref:`else clause<if statements>` to make it clearer

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 12-14

    def converse_implication(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool(first_input) == True:
        # if not bool(first_input):
        # if not first_input:
            # if second_input == True:
            # if bool(second_input) == True:
            # if bool(second_input):
            # if second_input:
        if not first_input and second_input:
            return False
        else:
            return True

  still green.

* I use the :ref:`Logical Negation (NOT)<test_logical_negation>` of the :ref:`if statement<if statements>` for the :ref:`else clause<if statements>`

  .. code-block:: python
    :lineno-start: 104
    :emphasize-lines: 3-4

        if not first_input and second_input:
            return False
        # else:
        if not (not first_input and second_input):
            return True

  green.

* I "multiply" the :ref:`not<test_logical_negation>` by every symbol in the parentheses

  .. code-block:: python
    :lineno-start: 104
    :emphasize-lines: 4-5

        if not first_input and second_input:
            return False
        # else:
        # if not (not first_input and second_input):
        if (not not first_input) (not and) (not second_input):
            return True

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  I cannot :ref:`negate<test_logical_negation>` :ref:`and<test_logical_conjunction>` this way

* I change ``not and`` to :ref:`or<test_logical_disjunction>`

  .. code-block:: python
    :lineno-start: 104
    :emphasize-lines: 5-6

        if not first_input and second_input:
            return False
        # else:
        # if not (not first_input and second_input):
        # if (not not first_input) (not and) (not second_input):
        if (not not first_input) or (not second_input):
            return True

  the test is green again

* I remove ``not not``

  .. code-block:: python
    :lineno-start: 104
    :emphasize-lines: 6-7

        if not first_input and second_input:
            return False
        # else:
        # if not (not first_input and second_input):
        # if (not not first_input) (not and) (not second_input):
        # if (not not first_input) or (not second_input):
        if first_input or not second_input:
            return True

  the test is still green because two :ref:`nots<test_logical_negation>` cancel out

* I add a :ref:`conditional expression<conditional expressions>`

  .. code-block:: python
    :lineno-start: 104
    :emphasize-lines: 1-2, 7-12

        # if not first_input and second_input:
        #     return False
        # else:
        # if not (not first_input and second_input):
        # if (not not first_input) (not and) (not second_input):
        # if (not not first_input) or (not second_input):
        # if first_input or not second_input:
        #     return True
        return (
            True if first_input or not second_input
            else False
        )

  still green.

* I remove ``True if`` and ``else False``

  .. code-block:: python
    :lineno-start: 104
    :emphasize-lines: 9-13

        # if not first_input and second_input:
        #     return False
        # else:
        # if not (not first_input and second_input):
        # if (not not first_input) (not and) (not second_input):
        # if (not not first_input) or (not second_input):
        # if first_input or not second_input:
        #     return True
        # return (
        #     True if first_input or not second_input
        #     else False
        # )
        return first_input or not second_input

  green.

* :ref:`converse_implication<test_converse_implication>` returns ``first_input or not second_input``

  - ``not second_input`` is the :ref:`Logical Negation (NOT)<test_logical_negation>` of ``second_input``

    * if the second input is :green:`True`, this part of the statement is :red:`False`
    * if the second input is :red:`False`, this part of the statement is :green:`True`
  - ``first_input or not second_input`` is the :ref:`Logical Disjunction (OR)<test_logical_disjunction>` of the first input and the :ref:`Logical Negation (NOT)<test_logical_negation>` of the second input

    .. code-block:: python

      logical_disjunction(
          first_input,
          logical_negation(second_input)
      )

  this means that in the four cases

  - if the first input is :green:`True` and the second input is :green:`True`, :ref:`converse_implication<test_converse_implication>` returns

    .. code-block:: python
      :emphasize-lines: 4

      first_input or not second_input
      True        or not True
      True        or False
      True        # logical_disjunction(True, False)

  - if the first input is :green:`True` and the second input is :red:`False`, :ref:`converse_implication<test_converse_implication>` returns

    .. code-block:: python
      :emphasize-lines: 4

      first_input or not second_input
      True        or not False
      True        or True
      True        # logical_disjunction(True, True)

  - if the first input is :red:`False` and the second input is :green:`True`, :ref:`converse_implication<test_converse_implication>` returns

    .. code-block:: python
      :emphasize-lines: 4

      first_input or not second_input
      False       or not True
      False       or False
      False       # logical_disjunction(False, False)

  - if the first input is :red:`False` and the second input is :red:`False`, :ref:`converse_implication<test_converse_implication>` returns

    .. code-block:: python
      :emphasize-lines: 4

      first_input or not second_input
      False       or not False
      False       or True
      True        # logical_disjunction(False, True)

  ==============  =============== =============== =====================
  first           second          not second      (first or not second)
  ==============  =============== =============== =====================
  :green:`True`   :green:`True`   :red:`False`    :green:`True`
  :green:`True`   :red:`False`    :green:`True`   :green:`True`
  :red:`False`    :green:`True`   :red:`False`    :red:`False`
  :red:`False`    :red:`False`    :green:`True`   :green:`True`
  ==============  =============== =============== ================

  I add a `return statement`_ to show this

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 23-26

    def converse_implication(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool(first_input) == True:
        # if not bool(first_input):
        # if not first_input:
            # if second_input == True:
            # if bool(second_input) == True:
            # if bool(second_input):
            # if second_input:
        # if not first_input and second_input:
        #     return False
        # else:
        # if not (not first_input and second_input)
        # if (not not first_input) (not and) (not second_input):
        # if (not not first_input) or (not second_input):
        # if first_input or not second_input:
        #     return True
        # return (
        #     True if first_input or not second_input
        #     else False
        # )
        return logical_disjunction(
            first_input,
            logical_negation(second_input)
        )
        return first_input or not second_input

  still green.

* I remove the comments

  .. code-block:: python
    :lineno-start: 94

    def converse_implication(first_input, second_input):
        return logical_disjunction(
            first_input,
            logical_negation(second_input)
        )
        return first_input or not second_input

  I can use either of these `return statements`_. The first `return statement`_ is the only one that runs in this case, because :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`.

:ref:`Converse Implication<test_converse_implication>` returns

- ``first_input or not second_input``
- :red:`False`, only if the first input is :red:`False` and the second input is :green:`True`
- the :ref:`Logical Disjunction<test_logical_disjunction>` of the first input and the :ref:`Logical Negation<test_logical_negation>` of the second input
- It is the opposite of :ref:`Converse Non-Implication<test_converse_non_implication>` which always returns ``not first_input and second_input`` or :ref:`True<test_what_is_true>`, only if the first input is :red:`False` and the second input is :green:`True`

----

=================================================================================
examples of Converse Implication
=================================================================================

----

* I cannot get a table at a restaurant, if the inputs are

  - do I have a reservation?
  - is the place full?

  ============  =============  =============
  reservation   place is full  I get a table
  ============  =============  =============
  :green:`yes`  :green:`yes`   :green:`yes`
  :green:`yes`  :red:`no`      :green:`yes`
  :red:`no`     :green:`yes`   :red:`no`
  :red:`no`     :red:`no`      :green:`yes`
  ============  =============  =============

* sleep through alarm, if the inputs are

  - am I too deep in sleep to hear the alarm?
  - is the alarm ringing?

  ============  =============  =============
  too tired     alarm rings    I sleep
  ============  =============  =============
  :green:`yes`  :green:`yes`   :green:`yes`
  :green:`yes`  :red:`no`      :green:`yes`
  :red:`no`     :green:`yes`   :red:`no`
  :red:`no`     :red:`no`      :green:`yes`
  ============  =============  =============

* staying dry outside, if the inputs are

  - do I have an umbrella?
  - is it raining?

  ================  ==================  ==================
  umbrella?         raining?            dry/wet
  ================  ==================  ==================
  :green:`yes`      :green:`yes`        :green:`dry`
  :green:`yes`      :red:`no`           :green:`dry`
  :red:`no`         :green:`yes`        :red:`wet`
  :red:`no`         :red:`no`           :green:`dry`
  ================  ==================  ==================

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

  I am back in the ``pumping_python`` directory_

----

*********************************************************************************
review
*********************************************************************************

Binary Operations take 2 inputs, each input can be :ref:`True<test_what_is_true>` or :red:`False`, if I name the first input ``first_input`` and the second one ``second_input``, the tests show that

* :ref:`Converse Implication<test_converse_implication>`

  - returns ``first_input or not second_input``
  - returns :red:`False` if ``first_input`` is :red:`False` and ``second_input`` is :green:`True`
  - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Converse Non-Implication<test_converse_non_implication>` which returns :green:`True` only if ``first_input`` is :red:`False` and ``second_input`` is :green:`True`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :green:`True`
  :green:`True`   :red:`False`   :green:`True`
  :red:`False`    :green:`True`  :red:`False`
  :red:`False`    :red:`False`   :green:`True`
  ==============  ============== ==============

* :ref:`Project First<test_project_first>`

  - always returns ``first_input``
  - returns :green:`True` only if ``first_input`` is :green:`True`
  - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Negate First<test_negate_first>` which returns :green:`True` only if ``first_input`` is :red:`False`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :green:`True`
  :green:`True`   :red:`False`   :green:`True`
  :red:`False`    :green:`True`  :red:`False`
  :red:`False`    :red:`False`   :red:`False`
  ==============  ============== ==============

* :ref:`Material Non-Implication<test_material_non_implication>`

  - returns ``first_input and not second_input``
  - returns :green:`True` only if ``first_input`` is :green:`True` and ``second_input`` is :red:`False`
  - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Material/Logical Implication<test_material_implication>` which returns :red:`False` only if ``first_input`` is :green:`True` and ``second_input`` is :red:`False`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :red:`False`
  :green:`True`   :red:`False`   :green:`True`
  :red:`False`    :green:`True`  :red:`False`
  :red:`False`    :red:`False`   :red:`False`
  ==============  ============== ==============

* :ref:`Exclusive Disjunction<test_exclusive_disjunction>`

  - returns ``first_input != second_input``
  - returns :green:`True` only if ``first_input`` and ``second_input`` are NOT equal
  - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Logical Equality<test_logical_equality>` which returns :green:`True` only if ``first_input`` and ``second_input`` are equal

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :red:`False`
  :green:`True`   :red:`False`   :green:`True`
  :red:`False`    :green:`True`  :green:`True`
  :red:`False`    :red:`False`   :red:`False`
  ==============  ============== ==============

* :ref:`Logical Disjunction<test_logical_disjunction>`

  - returns ``first_input or second_input``
  - returns :red:`False` only if ``first_input`` is :red:`False` and ``second_input`` is :red:`False`
  - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Logical NOR<test_logical_nor>` which returns :green:`True` only if ``first_input`` is :red:`False` and ``second_input`` is :red:`False`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :green:`True`
  :green:`True`   :red:`False`   :green:`True`
  :red:`False`    :green:`True`  :green:`True`
  :red:`False`    :red:`False`   :red:`False`
  ==============  ============== ==============

* :ref:`Tautology<test_tautology>`

  - always returns :green:`True`
  - never returns :red:`False`
  - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`contradiction<test_contradiction>`  which always returns :red:`False`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :green:`True`
  :green:`True`   :red:`False`   :green:`True`
  :red:`False`    :green:`True`  :green:`True`
  :red:`False`    :red:`False`   :green:`True`
  ==============  ============== ==============

* :ref:`Logical NAND<test_logical_nand>`

  - returns ``not (first_input and second_input)``
  - returns :red:`False` only if ``first_input`` is :green:`True` and ``second_input`` is :green:`True`
  - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Logical Conjunction (and)<test_logical_conjunction>` which returns :green:`True` only if ``first_input`` is :green:`True` and ``second_input`` is :green:`True`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :red:`False`
  :green:`True`   :red:`False`   :green:`True`
  :red:`False`    :green:`True`  :green:`True`
  :red:`False`    :red:`False`   :green:`True`
  ==============  ============== ==============

* :ref:`Negate First<test_negate_first>`

  - always returns ``not first_input``
  - returns :green:`True` only if ``first_input`` is :red:`False`
  - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Project First<test_project_first>` which returns :green:`True` only if ``first_input`` is :green:`True`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :red:`False`
  :green:`True`   :red:`False`   :red:`False`
  :red:`False`    :green:`True`  :green:`True`
  :red:`False`    :red:`False`   :green:`True`
  ==============  ============== ==============

* :ref:`Converse Non-Implication<test_converse_non_implication>`

  - returns ``not first_input and second_input``
  - returns :green:`True` only if ``first_input`` is :red:`False` and ``second_input`` is :green:`True`
  - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Converse Implication<test_converse_implication>` which returns :red:`False` if ``first_input`` is :red:`False` and ``second_input`` is :green:`True`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :red:`False`
  :green:`True`   :red:`False`   :red:`False`
  :red:`False`    :green:`True`  :green:`True`
  :red:`False`    :red:`False`   :red:`False`
  ==============  ============== ==============

* :ref:`Project Second<test_project_second>`

  - always returns ``second_input``
  - returns :green:`True` only if ``second_input`` is :green:`True`
  - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Negate Second<test_negate_second>` which returns :green:`True` only if ``second_input`` is :red:`False`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :green:`True`
  :green:`True`   :red:`False`   :red:`False`
  :red:`False`    :green:`True`  :green:`True`
  :red:`False`    :red:`False`   :red:`False`
  ==============  ============== ==============

* :ref:`Logical Conjunction<test_logical_conjunction>` returns

  - returns ``first_input and second_input``
  - returns :green:`True` only if ``first_input`` is :green:`True` and ``second_input`` is :green:`True`
  - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Logical NAND<test_logical_nand>` which returns :red:`False` only if ``first_input`` is :green:`True` and ``second_input`` is :green:`True`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :green:`True`
  :green:`True`   :red:`False`   :red:`False`
  :red:`False`    :green:`True`  :red:`False`
  :red:`False`    :red:`False`   :red:`False`
  ==============  ============== ==============

* :ref:`Contradiction<test_contradiction>`

  - always returns :red:`False`
  - never returns :green:`True`
  - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Tautology<test_tautology>` which always returns :green:`True`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :red:`False`
  :green:`True`   :red:`False`   :red:`False`
  :red:`False`    :green:`True`  :red:`False`
  :red:`False`    :red:`False`   :red:`False`
  ==============  ============== ==============

and

* :ref:`Logical Disjunction is "OR"<test_logical_disjunction>`
* :ref:`Logical Conjunction is "AND"<test_logical_conjunction>`
* :ref:`Logical Negation is "NOT" <test_logical_negation>`

All the :ref:`binary operations<truth table: binary operations>` or conditions have been written with some or all of the above 3.

The :ref:`binary operations<truth table: binary operations>` can be written with some combination of :ref:`AND<test_logical_conjunction>`, :ref:`NOT<test_logical_negation>` and :ref:`OR<test_logical_disjunction>`.

=============================================== =============  ============= ============= ============= ==============================================================
return                                          True,          True,         False,        False,        name of operation
                                                True           False         True          False
=============================================== =============  ============= ============= ============= ==============================================================
False                                           :red:`False`   :red:`False`  :red:`False`  :red:`False`  :ref:`contradiction<test_contradiction>`
first and second                                :green:`True`  :red:`False`  :red:`False`  :red:`False`  :ref:`logical_conjunction<test_logical_conjunction>`
second                                          :green:`True`  :red:`False`  :green:`True` :red:`False`  :ref:`project_second<test_project_second>`
(not first) and second                          :red:`False`   :red:`False`  :green:`True` :red:`False`  :ref:`converse_non_implication<test_converse_non_implication>`
not first                                       :red:`False`   :red:`False`  :green:`True` :green:`True` :ref:`negate_first<test_negate_first>`
not (first and second)                          :red:`False`   :green:`True` :green:`True` :green:`True` :ref:`logical_nand<test_logical_nand>`
True                                            :green:`True`  :green:`True` :green:`True` :green:`True` :ref:`tautology<test_tautology>`
first or second                                 :green:`True`  :green:`True` :green:`True` :red:`False`  :ref:`logical_disjunction<test_logical_disjunction>`
(not (first and second)) and (first or second)  :red:`False`   :green:`True` :green:`True` :red:`False`  :ref:`exclusive_disjunction<test_exclusive_disjunction>`
first and (not second)                          :red:`False`   :green:`True` :red:`False`  :red:`False`  :ref:`material_non_implication<test_material_non_implication>`
first                                           :green:`True`  :green:`True` :red:`False`  :red:`False`  :ref:`project_first<test_project_first>`
first or (not second)                           :green:`True`  :green:`True` :red:`False`  :green:`True` :ref:`converse_implication<test_converse_implication>`
=============================================== =============  ============= ============= ============= ==============================================================

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

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too.

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->