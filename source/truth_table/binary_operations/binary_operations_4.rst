.. meta::
  :description: Truth table Binary Operations 4 in Python using TDD—complete all sixteen binary operations in test_binary.py by adding negate_second (not second), logical_nor (not (first or second), True only when both False), logical_equality (first == second), and material_implication (not first or second). Full cumulative unittest suite: 16 test methods, 64 assertions across TT/TF/FT/FF. Refactor nested if-statements to return not (first or second), first == second, and not first or second; debug SyntaxError invalid syntax; factor not from if/else and return not (something). Real-world examples: defective product return rule, fire alarm works when power and sensor, logical equality matching pairs, material implication promise logic. Review includes complete sixteen-row truth table (logical_nor returns True only when both inputs False). Requires Binary Operations 3. Jacob Itegboje Pumping Python.
  :keywords: Jacob Itegboje, Pumping Python, truth table Binary Operations 4, test_binary.py all sixteen operations, negate_second not second, logical_nor not first or second, logical_equality first == second, material_implication not first or second, complete binary truth table 16 gates, TDD red green refactor final binary chapter, SyntaxError invalid syntax boolean refactor, return not something if else pattern, defective product return logic, fire alarm power and sensor rule, logical equality vs exclusive disjunction XOR, material implication promise logic, assertTrue assertFalse 64 assertions, not A or B NOR gate python, programming truth tables beginners, boolean algebra software engineering, unittest truth_table project

.. include:: ../../links.rst

.. _binary_operations_4:

#################################################################################
truth table: Binary Operations 4
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/5nyHcOL4BMc?si=_O84cSTjCaqLcWry" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

*********************************************************************************
requirements
*********************************************************************************

:ref:`Binary Operations 3<truth table: Binary Operations 3>`

----

*********************************************************************************
preview
*********************************************************************************

These are the tests I have at the end of the chapter

.. literalinclude:: ../../code/truth_table/tests/test_binary.py
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
    collected 16 items

    tests/test_binary.py ............                  [ 75%]
    tests/test_nullary_unary.py ....                   [100%]

    ================== 16 passed in G.HIs ===================

* Over the past 3 chapters I tested

  - :ref:`contradiction<test_contradiction>` which always returns :red:`False`
  - :ref:`logical_conjunction aka and<test_logical_conjunction>` which returns ``first_input and second_input``
  - :ref:`project_second<test_project_second>` which always returns ``second_input``
  - :ref:`converse_non_implication<test_converse_non_implication>` which returns ``not first_input and second_input``
  - :ref:`negate_first<test_negate_first>` which always returns ``not first_input``
  - :ref:`logical_nand<test_logical_nand>` which returns ``not (first_input and second_input)``
  - :ref:`tautology<test_tautology>` which always returns :green:`True`
  - :ref:`logical_disjunction<test_logical_disjunction>` which returns ``first_input or second_input``
  - :ref:`exclusive_disjunction<test_exclusive_disjunction>` which returns ``((not first_input and second_input) or (first_input and not second_input))``
  - :ref:`material_non_implication<test_material_non_implication>` which returns ``first_input and not second_input``
  - :ref:`project_first<test_project_first>` which always returns ``first_input``
  - :ref:`converse_implication<test_converse_implication>` which returns ``first_input or not second_input``

----

*********************************************************************************
test_negate_second
*********************************************************************************

The :ref:`truth table` for :ref:`negate_second<test_negate_second>` is

==============  ============== ==============
first input     second input   return
==============  ============== ==============
:green:`True`   :green:`True`  :red:`False`
:green:`True`   :red:`False`   :green:`True`
:red:`False`    :green:`True`  :red:`False`
:red:`False`    :red:`False`   :green:`True`
==============  ============== ==============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test for :ref:`negate_second<test_negate_second>` with an :ref:`assertion<what is an assertion?>` for when the first input is :green:`True` and the second input is :green:`True`, to ``test_truth_table.py``

==============  ============== ==============
first input     second input   return
==============  ============== ==============
:green:`True`   :green:`True`  :red:`False`
==============  ============== ==============

.. code-block:: python
  :lineno-start: 118
  :emphasize-lines: 18-20

      def test_converse_implication(self):
          converse_implication = (
              src.truth_table.converse_implication
          )
          self.assertTrue(
              converse_implication(True, True)
          )
          self.assertTrue(
              converse_implication(True, False)
          )
          self.assertFalse(
              converse_implication(False, True)
          )
          self.assertTrue(
              converse_implication(False, False)
          )

      def test_negate_second(self):
          negate_second = src.truth_table.negate_second
          self.assertFalse(negate_second(True, True))


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: python

  AttributeError: module 'src.truth_table'
                  has no attribute 'negate_second'

I do not have a definition for :ref:`negate_second<test_negate_second>` in ``truth_table.py``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a :ref:`function<what is a function?>` for :ref:`negate_second<test_negate_second>` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 94
  :emphasize-lines: 9-10

  def converse_implication(first_input, second_input):
      return logical_disjunction(
          first_input,
          logical_negation(second_input)
      )
      return first_input or not second_input


  def negate_second(first_input, second_input):
      return False

the test passes. :ref:`negate_second<test_negate_second>` returns :red:`False`, if the first input is :green:`True` and the second input is :green:`True`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for the next case, which is when the first input is :green:`True` and the second input is :red:`False`, to :ref:`test_negate_second` in ``test_truth_table.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :red:`False`   :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 135
    :emphasize-lines: 4

        def test_negate_second(self):
            negate_second = src.truth_table.negate_second
            self.assertFalse(negate_second(True, True))
            self.assertTrue(negate_second(True, False))


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  because the :ref:`negate_second function<test_negate_second>` returns :red:`False` and the :ref:`assertion<what is an assertion?>` expects :green:`True`.

* I add an :ref:`if statement<if statements>` to :ref:`negate_second<test_negate_second>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 102
    :emphasize-lines: 2-3

    def negate_second(first_input, second_input):
        if second_input == False:
            return True
        return False

  the test passes because when :ref:`negate_second<test_negate_second>` is called, it runs ``if second_input == False:``

  - if ``second_input`` is NOT equal to :red:`False`, it runs ``return False``
  - if ``second_input`` is equal to :red:`False`, it runs ``return True``

* I add an :ref:`assertion<what is an assertion?>` for the third case, which is when the first input is :red:`False` and the second input is :green:`True`, to :ref:`test_negate_second` in ``test_truth_table.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :green:`True`  :red:`False`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 135
    :emphasize-lines: 5

        def test_negate_second(self):
            negate_second = src.truth_table.negate_second
            self.assertFalse(negate_second(True, True))
            self.assertTrue(negate_second(True, False))
            self.assertFalse(negate_second(False, True))


    # Exceptions seen

  the test is still green. :ref:`negate_second<test_negate_second>` returns the :ref:`logical negation<test_logical_negation>` of the second input in all 3 cases.

* I add an :ref:`assertion<what is an assertion?>` for the last case, which is when the first input is :red:`False` and the second input is :red:`False`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :red:`False`   :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 135
    :emphasize-lines: 6

        def test_negate_second(self):
            negate_second = src.truth_table.negate_second
            self.assertFalse(negate_second(True, True))
            self.assertTrue(negate_second(True, False))
            self.assertFalse(negate_second(False, True))
            self.assertTrue(negate_second(False, False))


    # Exceptions seen

  the test is still green.

* I add :ref:`the bool built-in function<how to test if something is grouped as True>` to the :ref:`negate_second function<test_negate_second>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 102
    :emphasize-lines: 2-3

    def negate_second(first_input, second_input):
        # if second_input == False:
        if bool(second_input) == False:
            return True
        return False

  still green.

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write the statement in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 102
    :emphasize-lines: 3-4

    def negate_second(first_input, second_input):
        # if second_input == False:
        # if bool(second_input) == False:
        if bool(not second_input) == True:
            return True
        return False

  green.

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 102
    :emphasize-lines: 4-5

    def negate_second(first_input, second_input):
        # if second_input == False:
        # if bool(second_input) == False:
        # if bool(not second_input) == True:
        if bool(not second_input):
            return True
        return False

  still green.

* I remove :ref:`bool<how to test if something is grouped as True>`

  .. code-block:: python
    :lineno-start: 102
    :emphasize-lines: 5-6

    def negate_second(first_input, second_input):
        # if second_input == False:
        # if bool(second_input) == False:
        # if bool(not second_input) == True:
        # if bool(not second_input):
        if not second_input:
            return True
        return False

  the test is still green, because when ``if second_input == False:`` runs, Python_ checks if ``second_input`` is equal to :red:`False`. I can assume the following substitutions

  - if the value of ``something`` is :red:`False`

    .. literalinclude:: ../../code/truth_table/solutions/if_not_something_false.py
      :language: python

  - if the value of ``something`` is :green:`True`

    .. literalinclude:: ../../code/truth_table/solutions/if_not_something_true.py
      :language: python

  ``if bool(something) == False`` is the same as ``if bool(not something) == True`` is the same as ``if bool(not something)`` is the same as ``if not something``.

* I add a :ref:`conditional expression<conditional expressions>`

  .. code-block:: python
    :lineno-start: 102
    :emphasize-lines: 6-9

    def negate_second(first_input, second_input):
        # if second_input == False:
        # if bool(second_input) == False:
        # if bool(not second_input) == True:
        # if bool(not second_input):
        # if not second_input:
        #     return True
        # return False
        return True if not second_input else False

  still green.

* I remove ``True if`` and ``else False`` to make the statement simpler

  .. code-block:: python
    :lineno-start: 102
    :emphasize-lines: 9-10

    def negate_second(first_input, second_input):
        # if second_input == False:
        # if bool(second_input) == False:
        # if bool(not second_input) == True:
        # if bool(not second_input):
        # if not second_input:
        #     return True
        # return False
        # return True if not second_input else False
        return not second_input

* I remove the comments

  .. code-block:: python
    :lineno-start: 102

    def negate_second(first_input, second_input):
        return not second_input

* I add a git_ commit message in another terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add negate_second'

:ref:`Negate Second<test_negate_second>` always returns

* ``not second_input``
* the :ref:`Logical Negation<test_logical_negation>` of the second input

It is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Project Second<test_project_second>` which always returns the second input

----

=================================================================================
examples of Negate Second
=================================================================================

----

* returning a defective product, if the inputs are

  - do I have the original receipt?
  - does the product work?

  ==============  ============== ==============
  receipt?        product works? return?
  ==============  ============== ==============
  :green:`yes`    :green:`yes`   :red:`no`
  :green:`yes`    :red:`no`      :green:`yes`
  :red:`no`       :green:`yes`   :red:`no`
  :red:`no`       :red:`no`      :green:`yes`
  ==============  ============== ==============

* I do not pick up calls from numbers that are not in my contact list, if the inputs are

  - am I busy?
  - is the number saved in my phone?

  ==============  ============== ==================
  busy?           number saved?  send to voicemail?
  ==============  ============== ==================
  :green:`yes`    :green:`yes`   :red:`no`
  :green:`yes`    :red:`no`      :green:`yes`
  :red:`no`       :green:`yes`   :red:`no`
  :red:`no`       :red:`no`      :green:`yes`
  ==============  ============== ==================

----

*********************************************************************************
test_logical_nor
*********************************************************************************

The :ref:`truth table` for :ref:`logical_nor<test_logical_nor>` is

==============  ============== ==============
first input     second input   return
==============  ============== ==============
:green:`True`   :green:`True`  :red:`False`
:green:`True`   :red:`False`   :red:`False`
:red:`False`    :green:`True`  :red:`False`
:red:`False`    :red:`False`   :green:`True`
==============  ============== ==============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test for :ref:`logical_nor<test_logical_nor>` with an :ref:`assertion<what is an assertion?>` for when the first input is :green:`True` and the second input is :green:`True`, to ``test_truth_table.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :red:`False`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 135
    :emphasize-lines: 8-10

        def test_negate_second(self):
            negate_second = src.truth_table.negate_second
            self.assertFalse(negate_second(True, True))
            self.assertTrue(negate_second(True, False))
            self.assertFalse(negate_second(False, True))
            self.assertTrue(negate_second(False, False))

        def test_logical_nor(self):
            logical_nor = src.truth_table.logical_nor
            self.assertFalse(logical_nor(True, True))


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table'
                    has no attribute 'logical_nor'.
                    Did you mean: 'logical_nand'?

  ``truth_table.py`` does not have any definition for :ref:`logical_nor<test_logical_nor>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add the :ref:`function<what is a function?>` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 102
  :emphasize-lines: 5-6

  def negate_second(first_input, second_input):
      return not second_input


  def logical_nor(first_input, second_input):
      return False

the test passes. :ref:`logical_nor<test_logical_nor>` returns :red:`False`, if the first input is :green:`True` and the second input is :green:`True`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for the second case, which is when the first input is :green:`True` and the second input is :red:`False`, to :ref:`test_logical_nor` in ``test_truth_table.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :red:`False`   :red:`False`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 147
    :emphasize-lines: 4

        def test_logical_nor(self):
            logical_nor = src.truth_table.logical_nor
            self.assertFalse(logical_nor(True, True))
            self.assertFalse(logical_nor(True, False))


    # Exceptions seen

  the test is still green. :ref:`logical_nor<test_logical_nor>` returns

  - :red:`False`, if the first input is :green:`True` and the second input is :red:`False`
  - :red:`False`, if the first input is :green:`True` and the second input is :green:`True`
  - :red:`False`, if the first input is :green:`True`

* I add an :ref:`assertion<what is an assertion?>` for the next case, which is when the first input is :red:`False` and the second input is :green:`True`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :green:`True`  :red:`False`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 147
    :emphasize-lines: 5

        def test_logical_nor(self):
            logical_nor = src.truth_table.logical_nor
            self.assertFalse(logical_nor(True, True))
            self.assertFalse(logical_nor(True, False))
            self.assertFalse(logical_nor(False, True))


    # Exceptions seen

  the test is still green. :ref:`logical_nor<test_logical_nor>` returns

  - :red:`False`, if the first input is :red:`False` and the second input is :green:`True`
  - :red:`False`, if the first input is :green:`True`

* I add an :ref:`assertion<what is an assertion?>` for the last case, which is when the first input is :red:`False` and the second input is :red:`False`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :red:`False`   :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 147
    :emphasize-lines: 6

        def test_logical_nor(self):
            logical_nor = src.truth_table.logical_nor
            self.assertFalse(logical_nor(True, True))
            self.assertFalse(logical_nor(True, False))
            self.assertFalse(logical_nor(False, True))
            self.assertTrue(logical_nor(False, False))


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

  because the :ref:`logical_nor function<test_logical_nor>` returns :red:`False` and the :ref:`assertion<what is an assertion?>` expects :green:`True`.

* I add :ref:`if statements` for this case to :ref:`logical_nor<test_logical_nor>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 2-4

    def logical_nor(first_input, second_input):
        if first_input == False:
            if second_input == False:
                return True
        return False

  the test passes.

* I add :ref:`the bool built-in function<how to test if something is grouped as True>`

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 2-5

    def logical_nor(first_input, second_input):
        # if first_input == False:
        if bool(first_input) == False:
            # if second_input == False:
            if bool(second_input) == False:
                return True
        return False

  the test still green.

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write the :ref:`if statements` in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 3-4, 6-7

    def logical_nor(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        if bool(not first_input) == True:
            # if second_input == False:
            # if bool(second_input) == False:
            if bool(not second_input) == True:
                return True
        return False

  still green.

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 4-5, 8-9

    def logical_nor(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if bool(not first_input) == True:
        if bool(not first_input):
            # if second_input == False:
            # if bool(second_input) == False:
            # if bool(not second_input) == True:
            if bool(not second_input):
                return True
        return False

  green.

* I remove :ref:`bool<how to test if something is grouped as True>`

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 5-6, 10-11

    def logical_nor(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if bool(not first_input) == True:
        # if bool(not first_input):
        if not first_input:
            # if second_input == False:
            # if bool(second_input) == False:
            # if bool(not second_input) == True:
            # if bool(not second_input):
            if not second_input:
                return True
        return False

  still green, because I can assume the following substitutions for when ``if something == False:`` runs

  - if the value of ``something`` is :red:`False`

    .. literalinclude:: ../../code/truth_table/solutions/if_not_something_false.py
      :language: python

  - if the value of ``something`` is :green:`True`

    .. literalinclude:: ../../code/truth_table/solutions/if_not_something_true.py
      :language: python

  ``if bool(something) == False`` is the same as ``if bool(not something) == True`` is the same as ``if bool(not something)`` is the same as ``if not something``.

* I use :ref:`Logical Conjunction (AND)<test_logical_conjunction>` to put the two :ref:`if statements` together

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 6, 11-12

    def logical_nor(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if bool(not first_input) == True:
        # if bool(not first_input):
        # if not first_input:
            # if second_input == False:
            # if bool(second_input) == False:
            # if bool(not second_input) == True:
            # if bool(not second_input):
            # if not second_input:
        if not first_input and not second_input:
                return True
        return False

  still green, because I can put two :ref:`if statements` together when one is indented under the other

  .. code-block:: python

    if something:
        if something_else:

  can also be written as

  .. code-block:: python

    if something and something_else:

* I add a :ref:`conditional expression<conditional expressions>`

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 12-19

    def logical_nor(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if bool(not first_input) == True:
        # if bool(not first_input):
        # if not first_input:
            # if second_input == False:
            # if bool(second_input) == False:
            # if bool(not second_input) == True:
            # if bool(not second_input):
            # if not second_input:
        # if not first_input and not second_input:
        #         return True
        # return False
        return (
            True if
            not first_input and not second_input
            else False
        )

  the test is still green.

* I remove ``True if`` and ``else False``

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 16, 18

    def logical_nor(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if bool(not first_input) == True:
        # if bool(not first_input):
        # if not first_input:
            # if second_input == False:
            # if bool(second_input) == False:
            # if bool(not second_input) == True:
            # if bool(not second_input):
            # if not second_input:
        # if not first_input and not second_input:
        #         return True
        # return False
        return (
            # True if
            not first_input and not second_input
            # else False
        )

  still green.

* I write the statement in terms of :ref:`not<test_logical_negation>` because it happens 2 times

  .. code-block:: python
    :lineno-start: 120
    :emphasize-lines: 3-6

        return (
            # True if
            # not first_input and not second_input
            (not first_input)
            (not or)
            (not second_input)
            # else False
        )

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  because I cannot :ref:`negate<test_logical_negation>` :ref:`or<test_logical_disjunction>` this way

* I "factor" out the :ref:`nots<test_logical_negation>`

  .. code-block:: python
    :lineno-start: 120
    :emphasize-lines: 4-7

        return (
            # True if
            # not first_input and not second_input
            # (not first_input)
            # (not or)
            # (not second_input)
            not (first_input or second_input)
            # else False
        )

  the test is green again.

* :ref:`logical_nor<test_logical_nor>` returns ``not (first_input or second_input)`` which is the :ref:`Logical Negation (NOT)<test_logical_negation>` of the :ref:`Logical Disjunction (OR)<test_logical_disjunction>` of the first input and the second input

  .. code-block:: python

    logical_negation(
        logical_disjunction(
            first_input, second_input
        )
    )

  this means that in the four cases

  - if the first input is :green:`True` and the second input is :green:`True`, :ref:`logical_nor<test_logical_nor>` returns

    .. code-block:: python
      :emphasize-lines: 4

      not (first_input or second_input)
      not (True        or True        )
      not (True                       )
      False # not logical_disjunction(True, False)

  - if the first input is :green:`True` and the second input is :red:`False`, :ref:`logical_nor<test_logical_nor>` returns

    .. code-block:: python
      :emphasize-lines: 4

      not (first_input or second_input)
      not (True        or False       )
      not (True                       )
      False # not logical_disjunction(True, True)

  - if the first input is :red:`False` and the second input is :green:`True`, :ref:`logical_nor<test_logical_nor>` returns

    .. code-block:: python
      :emphasize-lines: 4

      not (first_input or second_input)
      not (False       or True        )
      not (True                       )
      False # not logical_disjunction(False, False)

  - if the first input is :red:`False` and the second input is :red:`False`, :ref:`logical_nor<test_logical_nor>` returns

    .. code-block:: python
      :emphasize-lines: 4

      not (first_input or second_input)
      not (False       or False       )
      not (False                      )
      True  # not logical_disjunction(False, True)

  ==============  =============== =============== =====================
  first           second          first or second not (first or second)
  ==============  =============== =============== =====================
  :green:`True`   :green:`True`   :green:`True`   :red:`False`
  :green:`True`   :red:`False`    :green:`True`   :red:`False`
  :red:`False`    :green:`True`   :green:`True`   :red:`False`
  :red:`False`    :red:`False`    :red:`False`    :green:`True`
  ==============  =============== =============== =====================

  I add a :ref:`return statement<the return statement>` to show this

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 15-19

    def logical_nor(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if bool(not first_input) == True:
        # if bool(not first_input):
        # if not first_input:
            # if second_input == False:
            # if bool(second_input) == False:
            # if bool(not second_input) == True:
            # if bool(not second_input):
            # if not second_input:
        # if not first_input and not second_input:
        #         return True
        # return False
        return logical_negation(
            logical_disjunction(
                first_input, second_input
            )
        )
        return (
            # True if
            # not first_input and not second_input
            # (not first_input)
            # (not or)
            # (not second_input)
            not (first_input or second_input)
            # else False
        )

  still green.

* I remove the comments

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 7

    def logical_nor(first_input, second_input):
        return logical_negation(
            logical_disjunction(
                first_input, second_input
            )
        )
        return not (first_input or second_input)

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add logical_nor'

  I can use either of these `return statements`_. The first :ref:`return statement<the return statement>` is the only one that runs in this case, because :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`.

:ref:`Logical NOR<test_logical_nor>` returns

* ``not (first_input or second_input)``
* :green:`True` if the first input is :red:`False` and the second input is :red:`False`
* the :ref:`Logical Negation<test_logical_negation>` of the :ref:`Logical Disjunction (OR)<test_logical_disjunction>` of the first input and second input
* :ref:`not<test_logical_negation>` :ref:`or<test_logical_disjunction>` of the first input and second input

----

=================================================================================
examples of Logical Nor
=================================================================================

----

* fitness discipline, if the inputs are

  - did I eat cake?
  - did I skip the workout?

  ==============  ============== ==============
  eat cake        skip workout   disciplined
  ==============  ============== ==============
  :green:`yes`    :green:`yes`   :red:`no`
  :green:`yes`    :red:`no`      :red:`no`
  :red:`no`       :green:`yes`   :red:`no`
  :red:`no`       :red:`no`      :green:`yes`
  ==============  ============== ==============

* a late fee, if the inputs are

  - did I make the payment?
  - am I within the grace period?

  ==============  ============== ================
  made payment    grace period   late fee charged
  ==============  ============== ================
  :green:`yes`    :green:`yes`   :red:`no`
  :green:`yes`    :red:`no`      :red:`no`
  :red:`no`       :green:`yes`   :red:`no`
  :red:`no`       :red:`no`      :green:`yes`
  ==============  ============== ================

----

*********************************************************************************
test_logical_equality
*********************************************************************************

The :ref:`truth table` for :ref:`logical_equality<test_logical_equality>` is

==============  ============== ==============
first input     second input   return
==============  ============== ==============
:green:`True`   :green:`True`  :green:`True`
:green:`True`   :red:`False`   :red:`False`
:red:`False`    :green:`True`  :red:`False`
:red:`False`    :red:`False`   :green:`True`
==============  ============== ==============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test for :ref:`Logical Equality<test_logical_equality>` with an :ref:`assertion<what is an assertion?>` for when the first input is :green:`True` and the second input is :green:`True` to ``test_truth_table.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 135
    :emphasize-lines: 23-26

        def test_logical_nor(self):
            logical_nor = src.truth_table.logical_nor
            self.assertFalse(logical_nor(True, True))
            self.assertFalse(logical_nor(True, False))
            self.assertFalse(logical_nor(False, True))
            self.assertTrue(logical_nor(False, False))

        def test_logical_equality(self):
            logical_equality = (
                src.truth_table.logical_equality
            )
            self.assertTrue(logical_equality(True, True))


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table'
                    has no attribute 'logical_equality'.
                    Did you mean: 'logical_identity'?

  because there is no definition for :ref:`logical_equality<test_logical_equality>` in ``truth_table.py``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a :ref:`function<what is a function?>` for it in ``truth_table.py``

.. code-block:: python
  :lineno-start: 106
  :emphasize-lines: 10-11

  def logical_nor(first_input, second_input):
      return logical_negation(
          logical_disjunction(
              first_input, second_input
          )
      )
      return not (first_input or second_input)


  def logical_equality(first_input, second_input):
      return True

the test passes. :ref:`logical_equality<test_logical_equality>` returns :green:`True`, if the first input is :green:`True` and the second input is :green:`True`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for the next case, which is when the first input is :green:`True` and the second input is :red:`False`, to :ref:`test_logical_equality` in ``test_truth_table.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :red:`False`   :red:`False`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 149
    :emphasize-lines: 6

        def test_logical_equality(self):
            logical_equality = (
                src.truth_table.logical_equality
            )
            self.assertTrue(logical_equality(True, True))
            self.assertFalse(logical_equality(True, False))


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  because the :ref:`logical_equality function<test_logical_equality>` returns :green:`True` and the :ref:`assertion<what is an assertion?>` expects :red:`False`.

* I add an :ref:`if statement<if statements>` to :ref:`logical_equality<test_logical_equality>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 115
    :emphasize-lines: 2-3

    def logical_equality(first_input, second_input):
        if second_input == False:
            return False
        return True

  the test passes because when :ref:`logical_equality<test_logical_equality>` is called, it runs ``if second_input == False:``

  - if ``second_input`` is NOT equal to :red:`False`, it leaves the :ref:`if statement<if statements>` then runs ``return True``
  - if ``second_input`` is equal to :red:`False`, it runs ``return False``

* I add an :ref:`assertion<what is an assertion?>` for the next case, which is when the first input is :red:`False` and the second input is :green:`True`, to :ref:`test_logical_equality` in ``test_truth_table.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :green:`True`  :red:`False`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 149
    :emphasize-lines: 7

        def test_logical_equality(self):
            logical_equality = (
                src.truth_table.logical_equality
            )
            self.assertTrue(logical_equality(True, True))
            self.assertFalse(logical_equality(True, False))
            self.assertFalse(logical_equality(False, True))


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  because when :ref:`logical_equality<test_logical_equality>` is called, it runs ``if second_input == False:``

  - if ``second_input`` is equal to :red:`False`, it runs ``return False``
  - if ``second_input`` is NOT equal to :red:`False`, it leaves the :ref:`if statement<if statements>` then runs ``return True``
  - ``second_input`` is :green:`True` in this case, which raises :ref:`AssertionError<what causes AssertionError?>` since the :ref:`assertion<what is an assertion?>` expects :red:`False` and the :ref:`function<what is a function?>` returns :green:`True`

* I add another :ref:`if statement<if statements>` to the :ref:`logical_equality function<test_logical_equality>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 115
    :emphasize-lines: 2-3

    def logical_equality(first_input, second_input):
        if first_input == False:
            return False
        if second_input == False:
            return False
        return True

  the test passes because when :ref:`logical_equality<test_logical_equality>` is called, it runs ``if first_input == False:``

  - if ``first_input`` is NOT equal to :red:`False`, it runs the next :ref:`if statement<if statements>` - ``if second_input == False:``

    * if ``second_input`` is NOT equal to :red:`False`, it leaves the :ref:`if statement<if statements>` then runs ``return True `` and leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`
    * if ``second_input`` is equal to :red:`False`, it runs ``return False`` and leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`

  - if ``first_input`` is equal to :red:`False`, it runs ``return False`` and leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`

* I add an :ref:`assertion<what is an assertion?>` for the last case, which is when the first input is :red:`False` and the second input is :red:`False`, to :ref:`test_logical_equality` in ``test_truth_table.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :red:`False`   :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 149
    :emphasize-lines: 8

        def test_logical_equality(self):
            logical_equality = (
                src.truth_table.logical_equality
            )
            self.assertTrue(logical_equality(True, True))
            self.assertFalse(logical_equality(True, False))
            self.assertFalse(logical_equality(False, True))
            self.assertTrue(logical_equality(False, False))


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  because when :ref:`logical_equality<test_logical_equality>` is called, it runs ``if first_input == False:``

  - if ``first_input`` is equal to :red:`False`, it runs ``return False``
  - if ``first_input`` is NOT equal to :red:`False`, it runs the next :ref:`if statement<if statements>` - ``if second_input == False:``

    * if ``second_input`` is NOT equal to :red:`False`, it leaves the :ref:`if statement<if statements>` then runs ``return True``
    * if ``second_input`` is equal to :red:`False`, it runs ``return False``
    * ``second_input`` is :red:`False` in this case, which raises :ref:`AssertionError<what causes AssertionError?>` since the :ref:`assertion<what is an assertion?>` expects :green:`True` and the :ref:`function<what is a function?>` returns :red:`False`


* I add an :ref:`if statement<if statements>` to the :ref:`logical_equality function<test_logical_equality>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 115
    :emphasize-lines: 3-4

    def logical_equality(first_input, second_input):
        if first_input == False:
            if second_input == False:
                return True
            return False
        if second_input == False:
            return False
        return True

  the test passes because when :ref:`logical_equality<test_logical_equality>` is called, it runs ``if first_input == False:``

  - if ``first_input`` is NOT equal to :red:`False`, it runs the next :ref:`if statement<if statements>` - ``if second_input == False:``

    * if ``second_input`` is NOT equal to :red:`False`, it leaves the :ref:`if statement<if statements>` then runs ``return True``
    * if ``second_input`` is equal to :red:`False`, it runs ``return False``

  - if ``first_input`` is equal to :red:`False`, it runs ``if second_input == False:``

    * if ``second_input`` is NOT equal to :red:`False`, it leaves the :ref:`if statement<if statements>` then runs the next line - ``return False``
    * if ``second_input`` is equal to :red:`False`, it runs ``return True``

* I add :ref:`the bool built-in function<how to test if something is grouped as True>`

  .. code-block:: python
    :lineno-start: 115
    :emphasize-lines: 2-5, 8-9

    def logical_equality(first_input, second_input):
        # if first_input == False:
        if bool(first_input) == False:
            # if second_input == False:
            if bool(second_input) == False:
                return True
            return False
        # if second_input == False:
        if bool(second_input) == False:
            return False
        return True

  the test is still green.

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write the statements in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 115
    :emphasize-lines: 3-4, 6-7, 11-12

    def logical_equality(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        if bool(not first_input) == True:
            # if second_input == False:
            # if bool(second_input) == False:
            if bool(not second_input) == True:
                return True
            return False
        # if second_input == False:
        # if bool(second_input) == False:
        if bool(not second_input) == True:
            return False
        return

  still green.

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 115
    :emphasize-lines: 4-5, 8-9, 14-15

    def logical_equality(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if bool(not first_input) == True:
        if bool(not first_input):
            # if second_input == False:
            # if bool(second_input) == False:
            # if bool(not second_input) == True:
            if bool(not second_input):
                return True
            return False
        # if second_input == False:
        # if bool(second_input) == False:
        # if bool(not second_input) == True:
        if bool(not second_input):
            return False
        return True

  green.

* I remove :ref:`bool<how to test if something is grouped as True>`

  .. code-block:: python
    :lineno-start: 115
    :emphasize-lines: 5-6, 10-11, 17-18

    def logical_equality(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if bool(not first_input) == True:
        # if bool(not first_input):
        if not first_input:
            # if second_input == False:
            # if bool(second_input) == False:
            # if bool(not second_input) == True:
            # if bool(not second_input):
            if not second_input:
                return True
            return False
        # if second_input == False:
        # if bool(second_input) == False:
        # if bool(not second_input) == True:
        # if bool(not second_input):
        if not second_input:
            return False
        return True

  still green because I can assume the following substitutions for when ``if something == False:`` runs

  - if the value of ``something`` is :red:`False`

    .. literalinclude:: ../../code/truth_table/solutions/if_not_something_false.py
      :language: python

  - if the value of ``something`` is :green:`True`

    .. literalinclude:: ../../code/truth_table/solutions/if_not_something_true.py
      :language: python

  ``if bool(something) == False`` is the same as ``if bool(not something) == True`` is the same as ``if bool(not something)`` is the same as ``if not something``.

* I use :ref:`Logical Conjunction (AND)<test_logical_conjunction>` to make two of the cases clearer

  .. code-block:: python
    :lineno-start: 115
    :emphasize-lines: 6, 11-15

    def logical_equality(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if bool(not first_input) == True:
        # if bool(not first_input):
        # if not first_input:
            # if second_input == False:
            # if bool(second_input) == False:
            # if bool(not second_input) == True:
            # if bool(not second_input):
            # if not second_input:
        if not first_input and not second_input:
            return True
        if not first_input and second_input:
            return False
        # if second_input == False:
        # if bool(second_input) == False:
        # if bool(not second_input) == True:
        # if bool(not second_input):
        if not second_input:
            return False
        return True

  the test is still green, because I can put two :ref:`if statements` together when one is indented under the other

  .. code-block:: python

    if something:
        if something_else:

  can also be written as

  .. code-block:: python

    if something and something_else:

* I do the same thing for the other two cases

  .. code-block:: python
    :lineno-start: 126
    :emphasize-lines: 10-13

        if not first_input and not second_input:
            return True
        if not first_input and second_input:
            return False
        # if second_input == False:
        # if bool(second_input) == False:
        # if bool(not second_input) == True:
        # if bool(not second_input):
        # if not second_input:
        if first_input and not second_input:
            return False
        if first_input and second_input:
            return True

  still green.

* I put the :ref:`if statements` that return the same thing together

  .. code-block:: python
    :lineno-start: 115
    :emphasize-lines: 17-18, 23-24

    def logical_equality(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if bool(not first_input) == True:
        # if bool(not first_input):
        # if not first_input:
            # if second_input == False:
            # if bool(second_input) == False:
            # if bool(not second_input) == True:
            # if bool(not second_input):
            # if not second_input:
        # if second_input == False:
        # if bool(second_input) == False:
        # if bool(not second_input) == True:
        # if bool(not second_input):
        # if not second_input:
        if not first_input and second_input:
            return False
        if first_input and not second_input:
            return False
        if first_input and second_input:
            return True
        if not first_input and not second_input:
            return True

* I use :ref:`Logical Disjunction (OR)<test_logical_disjunction>` to put the two :ref:`if statements` that return :green:`True` together

  .. code-block:: python
    :lineno-start: 131
    :emphasize-lines: 1-16

        # if not first_input and second_input:
        #     return False
        # if first_input and not second_input:
        #     return False
        # if first_input and second_input:
        #     return True
        # if not first_input and not second_input:
        #     return True
        if (
            (first_input and second_input)
            or
            (not first_input and not second_input)
        ):
            return True
        else:
            return False

  green, because I can put two :ref:`if statements` together when they both return the same thing and are at the same indentation level

  .. code-block:: python

    if something:
        return this
    if something_else:
        return this

  can also be written as

  .. code-block:: python

    if something or something_else:
        return this

* I add a :ref:`conditional expression<conditional expressions>`

  .. code-block:: python
    :lineno-start: 131
    :emphasize-lines: 9-21

        # if not first_input and second_input:
        #     return False
        # if first_input and not second_input:
        #     return False
        # if first_input and second_input:
        #     return True
        # if not first_input and not second_input:
        #     return True
        # if (
        #     (first_input and second_input)
        #     or
        #     (not first_input and not second_input)
        # ):
        #     return True
        # else:
        #     return False
        return True if (
            (first_input and second_input)
            or
            (not first_input and not second_input)
        ) else False

  still green.

* I remove ``True if`` and ``else False``

  .. code-block:: python
    :lineno-start: 147
    :emphasize-lines: 1-2, 6-7

        # return True if (
        return (
            (first_input and second_input)
            or
            (not first_input and not second_input)
        # ) else False
        )

  the test is still green.

* I write the second part of the statement in terms of :ref:`not<test_logical_negation>` because it happens twice

  .. code-block:: python
    :lineno-start: 147
    :emphasize-lines: 5-10

        # return True if (
        return (
            (first_input and second_input)
            or
            # (not first_input and not second_input)
            (
                (not first_input)
                (not or)
                (not second_input)
            )
        # ) else False
        )

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  because I cannot :ref:`negate<test_logical_negation>` :ref:`or<test_logical_disjunction>` this way

* I "factor" out the :ref:`nots<test_logical_negation>`

  .. code-block:: python
    :lineno-start: 147
    :emphasize-lines: 6-11

        # return True if (
        return (
            (first_input and second_input)
            or
            # (not first_input and not second_input)
            # (
            #     (not first_input)
            #     (not or)
            #     (not second_input)
            # )
            not (first_input or second_input)
        # ) else False
        )

  the test is green again.

* :ref:`Logical Equality<test_logical_equality>` returns ``((first_input and second_input) or not (first_input or second_input))``, which can be thought of as the :ref:`Logical Disjunction (OR)<test_logical_disjunction>` of the :ref:`Logical Conjunction (AND)<test_logical_conjunction>` of the first input and second input, and the :ref:`Logical Negation(NOT)<test_logical_negation>` of the :ref:`Logical Disjunction (OR)<test_logical_disjunction>` of the first input and second input also known as the :ref:`Logical NOR<test_logical_nor>` of the first input and second input

  .. code-block:: python

    return logical_disjunction(
        logical_conjunction(first_input, second_input),
        logical_nor(first_input, second_input)
    )

  because

  .. code-block:: python

    logical_disjunction(first_input, second_input)

    first_input              == (first_input and second_input)
    logical_conjunction      == (first_input and second_input)

    second_input             == not (first_input or second_input)
    logical_nor              == not (first_input or second_input)

  * :ref:`logical_disjunction<test_logical_disjunction>` returns ``first_input or second_input``
  * :ref:`logical_conjunction<test_logical_conjunction>` returns ``first_input and second_input``
  * :ref:`logical_nor<test_logical_nor>` returns ``not (first_input or second_input)``

  or

  .. code-block:: python

    return logical_disjunction(
        logical_conjunction(first_input, second_input),
        logical_negation(
            logical_disjunction(first_input, second_input)
        )
    )

  This means that in the four cases

  * if the first input is :green:`True` and the second input is :green:`True`, :ref:`logical_equality<test_logical_equality>` returns

    .. code-block:: python
      :emphasize-lines: 5

      (first and second) or (not (first or second))
      (True  and True  ) or (not (True  or True  ))
       True              or (not  True            )
       True              or  False
       True              # logical_disjunction(True, False)

  * if the first input is :green:`True` and the second input is :red:`False`, :ref:`logical_equality<test_logical_equality>` returns

    .. code-block:: python
      :emphasize-lines: 5
      :force:

      (first and second) or (not (first or second))
      (True  and False ) or (not (True  or False ))
       False             or (not  True            )
       False             or  False
       False             # logical_disjunction(False, False)

  * if the first input is :red:`False` and the second input is :green:`True`, :ref:`logical_equality<test_logical_equality>` returns

    .. code-block:: python
      :emphasize-lines: 5

      (first and second) or (not (first or second))
      (False and True  ) or (not (False or True  ))
       False             or (not  True            )
       False             or  False
       False             # logical_disjunction(False, False)

  * if the first input is :red:`False` and the second input is :red:`False`, :ref:`logical_equality<test_logical_equality>` returns

    .. code-block:: python
      :emphasize-lines: 5

      (first and second) or (not (first or second))
      (False and False ) or (not (False or False ))
       False             or (not  False           )
       False             or  True
       True              # logical_disjunction(False, True)

  ============= ============= ================  ================  ================  ======================
  first         second        first and second  first or second   not (first        ((first and second)
                                                                  or                or
                                                                  second)           not (first or second))
  ============= ============= ================  ================  ================  ======================
  :green:`True` :green:`True` :green:`True`     :red:`False`      :green:`True`     :green:`True`
  :green:`True` :red:`False`  :red:`False`      :green:`True`     :green:`True`     :red:`False`
  :red:`False`  :green:`True` :red:`False`      :red:`False`      :red:`False`      :red:`False`
  :red:`False`  :red:`False`  :red:`False`      :green:`True`     :green:`True`     :green:`True`
  ============= ============= ================  ================  ================  ======================

  I add a :ref:`return statement<the return statement>` to show this

  .. code-block:: python
    :lineno-start: 147
    :emphasize-lines: 2-5

        # return True if (
        return logical_disjunction(
            logical_conjunction(first_input, second_input),
            logical_nor(first_input, second_input)
        )
        return (
            (first_input and second_input)
            or
            # (not first_input and not second_input)
            # (
            #     (not first_input)
            #     (not or)
            #     (not second_input)
            # )
            not (first_input or second_input)
        # ) else False
        )

  still green.

* :ref:`logical_equality<test_logical_equality>` returns :green:`True`, if the first input and second input are the equal, which means I can write a much simpler :ref:`return statement<the return statement>` thanks to the equality (``==``) symbol (2 equal signs together :kbd:`=+=` on the keyboard)

  .. code-block:: python
    :lineno-start: 115
    :emphasize-lines: 34

    def logical_equality(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if bool(not first_input) == True:
        # if bool(not first_input):
        # if not first_input:
            # if second_input == False:
            # if bool(second_input) == False:
            # if bool(not second_input) == True:
            # if bool(not second_input):
            # if not second_input:
        # if second_input == False:
        # if bool(second_input) == False:
        # if bool(not second_input) == True:
        # if bool(not second_input):
        # if not second_input:
        # if not first_input and second_input:
        #     return False
        # if first_input and not second_input:
        #     return False
        # if first_input and second_input:
        #     return True
        # if not first_input and not second_input:
        #     return True
        # if (
        #     (first_input and second_input)
        #     or
        #     (not first_input and not second_input)
        # ):
        #     return True
        # else:
        #     return False
        # return True if (
        return first_input == second_input
        return logical_disjunction(
            logical_conjunction(first_input, second_input),
            logical_nor(first_input, second_input)
        )
        return (
            (first_input and second_input)
            or
            # (not first_input and not second_input)
            # (
            #     (not first_input)
            #     (not or)
            #     (not second_input)
            # )
            not (first_input or second_input)
        # ) else False
        )

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 115

    def logical_equality(first_input, second_input):
        return first_input == second_input
        return logical_disjunction(
            logical_conjunction(first_input, second_input),
            logical_nor(first_input, second_input)
        )
        return (
            (first_input and second_input)
            or
            not (first_input or second_input)
        )

  I can use any of these `return statements`_. The first :ref:`return statement<the return statement>` is the only one that runs in this case, because :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add logical_equality'

:ref:`Logical Equality<test_logical_equality>`

* returns ``first_input == second_input``
* returns :ref:`True<test_what_is_true>` when the first input is equal to the second input
* returns the :ref:`Logical Disjunction (OR)<test_logical_disjunction>` of the :ref:`Logical Conjunction (AND)<test_logical_conjunction>` of the first input and second input, and the :ref:`Logical Negation(NOT)<test_logical_negation>` of the :ref:`Logical Disjunction (OR)<test_logical_disjunction>` of the first input and second input. Oh brother!
* is the :ref:`opposite<test_logical_negation>` of :ref:`Exclusive Disjunction<test_logical_disjunction>` which returns :green:`True`, only if the first input and second input are NOT equal.

----

=================================================================================
examples of Logical Equality
=================================================================================

----

* my expectation matches reality, if the inputs are

  - reality
  - expectation

  ================  ==================  ===========================
  reality           my expectation      expectation matches reality
  ================  ==================  ===========================
  :green:`yes`      :green:`yes`        :green:`yes`
  :green:`yes`      :red:`no`           :red:`no`
  :red:`no`         :green:`yes`        :red:`no`
  :red:`no`         :red:`no`           :green:`yes`
  ================  ==================  ===========================

* a market is balanced, if the inputs are

  - supply
  - demand

  ==============  ==============  ==============
  supply          demand          balance
  ==============  ==============  ==============
  :green:`high`   :green:`high`   :green:`yes`
  :green:`high`   :red:`low`      :red:`no`
  :red:`low`      :green:`high`   :red:`no`
  :red:`low`      :red:`low`      :green:`yes`
  ==============  ==============  ==============

* we are in agreement, if the inputs are

  - what did I say?
  - what did you say?

  ==============  ==============  ==============
  I said          You said        agreement
  ==============  ==============  ==============
  :green:`yes`    :green:`yes`    :green:`yes`
  :green:`yes`    :red:`no`       :red:`no`
  :red:`no`       :green:`yes`    :red:`no`
  :red:`no`       :red:`no`       :green:`yes`
  ==============  ==============  ==============

----

*********************************************************************************
test_material_implication
*********************************************************************************


The :ref:`truth table` for :ref:`material_implication<test_material_implication>` is

==============  ============== ==============
first input     second input   return
==============  ============== ==============
:green:`True`   :green:`True`  :green:`True`
:green:`True`   :red:`False`   :red:`False`
:red:`False`    :green:`True`  :green:`True`
:red:`False`    :red:`False`   :green:`True`
==============  ============== ==============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test for :ref:`material_implication<test_material_implication>` with an :ref:`assertion<what is an assertion?>` for when the first input is :green:`True` and the second input is :green:`True`, to ``test_truth_table.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 149
    :emphasize-lines: 10-16

        def test_logical_equality(self):
            logical_equality = (
                src.truth_table.logical_equality
            )
            self.assertTrue(logical_equality(True, True))
            self.assertFalse(logical_equality(True, False))
            self.assertFalse(logical_equality(False, True))
            self.assertTrue(logical_equality(False, False))

        def test_material_implication(self):
            material_implication = (
                src.truth_table.material_implication
            )
            self.assertTrue(
                material_implication(True, True)
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.truth_table'
                    has no attribute 'material_implication'

  because there is no definition for :ref:`material_implication<test_material_implication>` in ``truth_table.py``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a :ref:`function<what is a function?>` for :ref:`material_implication<test_material_implication>` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 115
  :emphasize-lines: 14-15

  def logical_equality(first_input, second_input):
      return first_input == second_input
      return logical_disjunction(
          logical_conjunction(first_input, second_input),
          logical_nor(first_input, second_input)
      )
      return (
          (first_input and second_input)
          or
          not (first_input or second_input)
      )


  def material_implication(first_input, second_input):
      return True

the test passes. :ref:`material_implication<test_material_implication>` returns :green:`True`, if the first input is :green:`True` and the second input is :green:`True`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_material_implication` for the next case, which is when the first input is :green:`True` and the second input is :red:`False`,  in ``test_truth_table.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :red:`False`   :red:`False`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 158
    :emphasize-lines: 8-10

        def test_material_implication(self):
            material_implication = (
                src.truth_table.material_implication
            )
            self.assertTrue(
                material_implication(True, True)
            )
            self.assertFalse(
                material_implication(True, False)
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  because the :ref:`function<what is a function?>` returns :green:`True` and the :ref:`assertion<what is an assertion?>` expects :red:`False`.

* I add an :ref:`if statement<if statements>` to :ref:`material_implication<test_material_implication>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 128
    :emphasize-lines: 2-3

    def material_implication(first_input, second_input):
        if second_input == False:
            return False
        return True

  the test passes because when :ref:`material_implication<test_material_implication>` is called, it runs ``if second_input == False:``

  - if ``second_input`` is NOT equal to :red:`False`, it runs ``return True``
  - if ``second_input`` is equal to :red:`False`, it runs ``return False``

* I add an :ref:`assertion<what is an assertion?>`  to :ref:`test_material_implication` for the next case, which is when the first input is :red:`False` and the second input is :green:`True` in ``test_truth_table.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :green:`True`  :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 158
    :emphasize-lines: 11-13

        def test_material_implication(self):
            material_implication = (
                src.truth_table.material_implication
            )
            self.assertTrue(
                material_implication(True, True)
            )
            self.assertFalse(
                material_implication(True, False)
            )
            self.assertTrue(
                material_implication(False, True)
            )


    # Exceptions seen

  the test is still green. :ref:`material_implication<test_material_implication>` returns

  - :green:`True`, if the first input is :red:`False` and the second input is :green:`True`
  - :red:`False`, if the first input is :green:`True` and the second input is :red:`False`
  - :green:`True`, if the first input is :green:`True` and the second input is :green:`True`
  - the second input in these three cases

* I add an :ref:`assertion<what is an assertion?>` for the fourth case, which is when the first input is :red:`False` and the second input is :red:`False`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :red:`False`   :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 158
    :emphasize-lines: 14-16

        def test_material_implication(self):
            material_implication = (
                src.truth_table.material_implication
            )
            self.assertTrue(
                material_implication(True, True)
            )
            self.assertFalse(
                material_implication(True, False)
            )
            self.assertTrue(
                material_implication(False, True)
            )
            self.assertTrue(
                material_implication(False, False)
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  because when :ref:`material_implication<test_material_implication>` gets called, it runs ``if second_input == False:``

  - if ``second_input`` is NOT equal to :red:`False`, it runs ``return True``
  - if ``second_input`` is equal to :red:`False`, it runs ``return False``
  - ``second_input`` is :red:`False` in this case, which causes :ref:`AssertionError<what causes AssertionError?>` since the :ref:`assertion<what is an assertion?>` expects :green:`True` and the :ref:`function<what is a function?>` returns :red:`False`

* I add an :ref:`if statement<if statements>` to the :ref:`material_implication function<test_material_implication>` for the one case where it returns :red:`False`, in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 128
    :emphasize-lines: 2-4

    def material_implication(first_input, second_input):
        if first_input == True:
            if second_input == False:
                return False
        return True

  the test passes.

* I use :ref:`the bool built-in function<how to test if something is grouped as True>`

  .. code-block:: python
    :lineno-start: 128
    :emphasize-lines: 2-5

    def material_implication(first_input, second_input):
        # if first_input == True:
        if bool(first_input) == True:
            # if second_input == False:
            if bool(second_input) == False:
                return False
        return True

  the test is still green.

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write the second :ref:`if statement<if statements>` in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 128
    :emphasize-lines: 5-6

    def material_implication(first_input, second_input):
        # if first_input == True:
        if bool(first_input) == True:
            # if second_input == False:
            # if bool(second_input) == False:
            if bool(not second_input) == True:
                return False
        return True

  still green.

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 128
    :emphasize-lines: 3-4, 7-8

    def material_implication(first_input, second_input):
        # if first_input == True:
        # if bool(first_input) == True:
        if bool(first_input):
            # if second_input == False:
            # if bool(second_input) == False:
            # if bool(not second_input) == True:
            if bool(not second_input):
                return False
        return True

  green.

* I remove :ref:`bool<how to test if something is grouped as True>`

  .. code-block:: python
    :lineno-start: 128
    :emphasize-lines: 4-5, 9-10

    def material_implication(first_input, second_input):
        # if first_input == True:
        # if bool(first_input) == True:
        # if bool(first_input):
        if first_input:
            # if second_input == False:
            # if bool(second_input) == False:
            # if bool(not second_input) == True:
            # if bool(not second_input):
            if not second_input:
                return False
        return True

  still green, because

  * when ``if something == False:`` runs, Python_ checks if ``something`` is equal to :red:`False`. I can assume the following substitutions

    - if the value of ``something`` is :red:`False`

      .. literalinclude:: ../../code/truth_table/solutions/if_not_something_false.py
        :language: python

    - if the value of ``something`` is :green:`True`

      .. literalinclude:: ../../code/truth_table/solutions/if_not_something_true.py
        :language: python

  * when ``if something == True:`` runs, Python_ checks if ``(something)`` is equal to :green:`True`. I can assume the following substitutions

    - if the value of ``something`` is :red:`False`

      .. literalinclude:: ../../code/truth_table/solutions/if_something_false.py
        :language: python

    - if the value of ``something`` is :green:`True`

      .. literalinclude:: ../../code/truth_table/solutions/if_something_true.py
        :language: python

  - ``if bool(something) == False`` is the same as ``if bool(not something) == True`` is the same as ``if bool(not something)`` is the same as ``if not something``.
  - ``if bool(something) == True`` is the same as ``if bool(something)`` is the same as ``if something``.

* I use :ref:`Logical Conjunction (AND)<test_logical_conjunction>` to put the two :ref:`if statements` together

  .. code-block:: python
    :lineno-start: 128
    :emphasize-lines: 5, 10-11

    def material_implication(first_input, second_input):
        # if first_input == True:
        # if bool(first_input) == True:
        # if bool(first_input):
        # if first_input:
            # if second_input == False:
            # if bool(second_input) == False:
            # if bool(not second_input) == True:
            # if bool(not second_input):
            # if not second_input:
        if first_input and not second_input:
                return False
        return True

  the test is still green, because I can put two :ref:`if statements` together when one is indented under the other

  .. code-block:: python

    if something:
        if something_else:

  can also be written as

  .. code-block:: python

    if something and something_else:

* I add an :ref:`else clause<if statements>` to make it clearer

  .. code-block:: python
    :lineno-start: 128
    :emphasize-lines: 12-14

    def material_implication(first_input, second_input):
        # if first_input == True:
        # if bool(first_input) == True:
        # if bool(first_input):
        # if first_input:
            # if second_input == False:
            # if bool(second_input) == False:
            # if bool(not second_input) == True:
            # if bool(not second_input):
            # if not second_input:
        if first_input and not second_input:
            return False
        else:
            return True

  still green.

* I change the :ref:`else clause<if statements>` to the :ref:`Logical Negation (NOT)<if statements>` of the :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 138
    :emphasize-lines: 3-4

        if first_input and not second_input:
            return False
        # else:
        if not (first_input and not second_input):
            return True

  green.

* I add a :ref:`conditional expression<conditional expressions>`

  .. code-block:: python
    :lineno-start: 138
    :emphasize-lines: 1-2, 4-10

        # if first_input and not second_input:
        #     return False
        # else:
        # if not (first_input and not second_input):
        #     return
        return (
            True if
            not (first_input and not second_input)
            else False
        )

  still green.

* I remove ``True if`` and ``else False`` to make it simpler

  .. code-block:: python
    :lineno-start: 138
    :emphasize-lines: 7, 9

        # if first_input and not second_input:
        #     return False
        # else:
        # if not (first_input and not second_input):
        #     return
        return (
            # True if
            not (first_input and not second_input)
            # else False
        )

  the test is still green.

* I "multiply" :ref:`not<test_logical_negation>` by the symbols in parentheses

  .. code-block:: python
    :lineno-start: 138
    :emphasize-lines: 8-11

        # if first_input and not second_input:
        #     return False
        # else:
        # if not (first_input and not second_input):
        #     return
        return (
            # True if
            # not (first_input and not second_input)
            (not first_input)
            (not and)
            (not not second_input)
            # else False
        )

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  because I cannot :ref:`negate<test_logical_negation>` :ref:`and<test_logical_conjunction>` this way.

* I change ``not and`` to :ref:`or<test_logical_disjunction>`

  .. code-block:: python
    :lineno-start: 138
    :emphasize-lines: 10-11

        # if first_input and not second_input:
        #     return False
        # else:
        # if not (first_input and not second_input):
        #     return
        return (
            # True if
            # not (first_input and not second_input)
            (not first_input)
            # (not and)
            or
            (not not second_input)
            # else False
        )

  the test is green again.

* I remove ``not not`` because they cancel out

  .. code-block:: python
    :lineno-start: 138
    :emphasize-lines: 12-13

        # if first_input and not second_input:
        #     return False
        # else:
        # if not (first_input and not second_input):
        #     return
        return (
            # True if
            # not (first_input and not second_input)
            (not first_input)
            # (not and)
            or
            # (not not second_input)
            second_input
            # else False
        )

  the test is still green, because two :ref:`nots<test_logical_negation>` make a "right"?

* :ref:`material_implication<test_material_implication>` returns ``not first_input or second_input``

  - ``not first_input`` is the :ref:`Logical Negation (NOT)<test_logical_negation>` of ``first_input``

    * if the first input is :green:`True`, this part of the statement is :red:`False`
    * if the first input is :red:`False`, this part of the statement is :green:`True`

  - ``not first_input or second_input`` is the :ref:`Logical Disjunction (OR)<test_logical_disjunction>` of the :ref:`Logical Negation (NOT)<test_logical_negation>` of the first input, and the second input

    .. code-block:: python

      logical_disjunction(
          logical_negation(first_input),
          second_input
      )

  this means that in the four cases

  - if the first input is :green:`True` and the second input is :green:`True`, :ref:`material_implication<test_material_implication>` returns

    .. code-block:: python
      :emphasize-lines: 4

      not first_input or second_input
      not True        or True
      False           or True
      True            # logical_disjunction(False, True)

  - if the first input is :green:`True` and the second input is :red:`False`, :ref:`material_implication<test_material_implication>` returns

    .. code-block:: python
      :emphasize-lines: 4

      not first_input or second_input
      not True        or False
      False           or False
      False           # logical_disjunction(False, False)

  - if the first input is :red:`False` and the second input is :green:`True`, :ref:`material_implication<test_material_implication>` returns

    .. code-block:: python
      :emphasize-lines: 4

      not first_input or second_input
      not False       or True
      True            or True
      True            # logical_disjunction(True, True)

  - if the first input is :red:`False` and the second input is :red:`False`, :ref:`material_implication<test_material_implication>` returns

    .. code-block:: python
      :emphasize-lines: 4

      not first_input or second_input
      not False       or False
      True            or False
      True            # logical_disjunction(True, False)

  ==============  =============== =============== =====================
  first           not first       second          (not first or second)
  ==============  =============== =============== =====================
  :green:`True`   :red:`False`    :green:`True`   :green:`True`
  :green:`True`   :red:`False`    :red:`False`    :red:`False`
  :red:`False`    :green:`True`   :green:`True`   :green:`True`
  :red:`False`    :green:`True`   :red:`False`    :green:`True`
  ==============  =============== =============== =====================

  I add a :ref:`return statement<the return statement>` to show this

  .. code-block:: python
    :lineno-start: 128
    :emphasize-lines: 16-19

    def material_implication(first_input, second_input):
        # if first_input == True:
        # if bool(first_input) == True:
        # if bool(first_input):
        # if first_input:
            # if second_input == False:
            # if bool(second_input) == False:
            # if bool(not second_input) == True:
            # if bool(not second_input):
            # if not second_input:
        # if first_input and not second_input:
        #     return False
        # else:
        # if not (first_input and not second_input):
        #     return
        return logical_disjunction(
            logical_negation(first_input),
            second_input
        )
        return (
            # True if
            # not (first_input and not second_input)
            (not first_input)
            # (not and)
            or
            # (not not second_input)
            second_input
            # else False
        )

  still green.

* I remove the comments

  .. code-block:: python
    :lineno-start: 128
    :emphasize-lines: 6

    def material_implication(first_input, second_input):
        return logical_disjunction(
            logical_negation(first_input),
            second_input
        )
        return not first_input or second_input

  I can use either of these `return statements`_. The first :ref:`return statement<the return statement>` is the only one that runs in this case, because :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`.

* I add a git_ commit message in another terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add material_implication'

:ref:`Material Implication also known as Logical Implication<test_material_implication>` returns

* ``not first_input or second_input``
* the :ref:`Logical Disjunction<test_logical_disjunction>` of the :ref:`Logical Negation<test_logical_negation>` of the first input, and the second input
* :ref:`False<test_what_is_false>` only if the first input is :green:`True` and the second input is :red:`False`

it is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Material Non-Implication<test_material_non_implication>` which returns :green:`True` only if the first input is :green:`True` and the second input is :red:`False`.

----

=================================================================================
examples of Material Implication
=================================================================================

----

* does the fire alarm work, if the inputs are

  - is there a fire?
  - is the alarm ringing?

  ==============  ==============  ==============
  fire?           alarm?          alarm works
  ==============  ==============  ==============
  :green:`yes`    :green:`yes`    :green:`yes`
  :green:`yes`    :red:`no`       :red:`no`
  :red:`no`       :green:`yes`    :green:`yes` (false positive)
  :red:`no`       :red:`no`       :green:`yes`
  ==============  ==============  ==============

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_truth_table.py`` and ``truth_table.py``
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

:ref:`Binary Operations<truth table: Binary Operations>` take two inputs, each input can be :green:`True` or :red:`False`. If I name the first input ``first_input`` and the second input ``second_input``, the tests show that

* :ref:`Material/Logical Implication<test_material_implication>`

  - returns ``not first_input or second_input``
  - returns :red:`False` only if ``first_input`` is :green:`True` and ``second_input`` is :red:`False`
  - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Material Non-Implication<test_material_non_implication>` which returns :green:`True` only if ``first_input`` is :green:`True` and ``second_input`` is :red:`False`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :green:`True`
  :green:`True`   :red:`False`   :red:`False`
  :red:`False`    :green:`True`  :green:`True`
  :red:`False`    :red:`False`   :green:`True`
  ==============  ============== ==============

* :ref:`Logical Equality<test_logical_equality>`

  - returns ``first_input == second_input``
  - returns :green:`True` only if ``first_input`` and ``second_input`` are equal
  - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Exclusive Disjunction (Exclusive OR)<test_exclusive_disjunction>` which returns :green:`True` only if ``first_input`` and ``second_input`` are NOT equal

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :green:`True`
  :green:`True`   :red:`False`   :red:`False`
  :red:`False`    :green:`True`  :red:`False`
  :red:`False`    :red:`False`   :green:`True`
  ==============  ============== ==============

* :ref:`Logical NOR<test_logical_nor>`

  - returns ``not (first_input or second_input)``
  - returns :green:`True` only if ``first_input`` is :red:`False` and ``second_input`` is :red:`False`
  - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Logical Disjunction<test_logical_disjunction>` which returns :red:`False` only if ``first_input`` is :red:`False` and ``second_input`` is :red:`False`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :red:`False`
  :green:`True`   :red:`False`   :red:`False`
  :red:`False`    :green:`True`  :red:`False`
  :red:`False`    :red:`False`   :green:`True`
  ==============  ============== ==============

* :ref:`Negate Second<test_negate_second>`

  - always returns ``not second_input``
  - returns :green:`True` only if ``second_input`` is :red:`False`
  - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Project Second<test_project_second>` which returns :green:`True` only if ``second_input`` is :green:`True`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :red:`False`
  :green:`True`   :red:`False`   :green:`True`
  :red:`False`    :green:`True`  :red:`False`
  :red:`False`    :red:`False`   :green:`True`
  ==============  ============== ==============

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
  - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Logical Conjunction (AND)<test_logical_conjunction>` which returns :green:`True` only if ``first_input`` is :green:`True` and ``second_input`` is :green:`True`

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

The :ref:`binary operations<truth table: binary operations>` can be written with some combination of :ref:`AND<test_logical_conjunction>`, :ref:`NOT<test_logical_negation>` and :ref:`OR<test_logical_disjunction>`.

=============================================== ============= ============= ============= ============= ==============================================================
return                                          True,         True,         False,        False,        operation
                                                True          False         True          False
=============================================== ============= ============= ============= ============= ==============================================================
:red:`False`                                    :red:`False`  :red:`False`  :red:`False`  :red:`False`  :ref:`contradiction<test_contradiction>`
first and second                                :green:`True` :red:`False`  :red:`False`  :red:`False`  :ref:`logical_conjunction<test_logical_conjunction>`
second                                          :green:`True` :red:`False`  :green:`True` :red:`False`  :ref:`project_second<test_project_second>`
(not first) and second                          :red:`False`  :red:`False`  :green:`True` :red:`False`  :ref:`converse_non_implication<test_converse_non_implication>`
not first                                       :red:`False`  :red:`False`  :green:`True` :green:`True` :ref:`negate_first<test_negate_first>`
not (first and second)                          :red:`False`  :green:`True` :green:`True` :green:`True` :ref:`logical_nand<test_logical_nand>`
:green:`True`                                   :green:`True` :green:`True` :green:`True` :green:`True` :ref:`tautology<test_tautology>`
first or second                                 :green:`True` :green:`True` :green:`True` :red:`False`  :ref:`logical_disjunction<test_logical_disjunction>`
(not (first and second)) and (first or second)  :red:`False`  :green:`True` :green:`True` :red:`False`  :ref:`exclusive_disjunction<test_exclusive_disjunction>`
first and (not second)                          :red:`False`  :green:`True` :red:`False`  :red:`False`  :ref:`material_non_implication<test_material_non_implication>`
first                                           :green:`True` :green:`True` :red:`False`  :red:`False`  :ref:`project_first<test_project_first>`
first or (not second)                           :green:`True` :green:`True` :red:`False`  :green:`True` :ref:`converse_implication<test_converse_implication>`
not second                                      :red:`False`  :green:`True` :red:`False`  :green:`True` :ref:`negate_second<test_negate_second>`
not (first or second)                           :red:`False`  :red:`False`  :red:`False`  :green:`True` :ref:`logical_nor<test_logical_nor>`
(not first or second) and (first or not second) :green:`True` :red:`False`  :red:`False`  :green:`True` :ref:`logical_equality<test_logical_equality>`
(not first) or second                           :green:`True` :red:`False`  :green:`True` :green:`True` :ref:`material_implication<test_material_implication>`
=============================================== ============= ============= ============= ============= ==============================================================

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed for the Truth Table?<truth table: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

:ref:`Would you like to see more examples of the truth table?<truth table: Binary Operations Examples>`

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