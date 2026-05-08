.. meta::
  :description: Advance your Python logic skills by mastering Negate First, Logical NAND, Tautology, and Logical Disjunction (OR). This TDD-focused tutorial demonstrates how to simplify complex nested if-statements into clean one-line conditional expressions and ternary operators. Explore practical logic gate examples including smoke detector battery tests, server redundancy, and medical triage rules to see how boolean algebra applies to real-world code.
  :keywords: Jacob Itegboje, Python logical NAND implementation, Tautology vs Contradiction, Python negate first logic, logical disjunction OR operator, Python ternary operator tutorial, refactoring nested if statements Python, conditional expressions examples, TDD Red Green Refactor Python, boolean logic gates in programming, smoke detector logic example, server downtime logic, De Morgan's Law for beginners, Python SyntaxError troubleshooting, truthy and falsy evaluation, Python boolean simplification, unittest tutorial Python, logic for software engineers, programming truth tables, conditional return statements

.. include:: ../../links.rst

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

These are the tests I have at the end of the chapter

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
    collected 8 items

    tests/test_binary.py ....                         [ 50%]
    tests/test_nullary_unary.py ....                  [100%]

    ================== 8 passed in G.HIs ===================

* I hold :kbd:`ctrl` (Windows_) or :kbd:`option` (MacOS_) on the keyboard, then click on ``tests/test_binary.py`` with the mouse to open it in the :ref:`editor<2 editors>`

----

*********************************************************************************
test_negate_first
*********************************************************************************

The :ref:`truth table` for :ref:`negate_first<test_negate_first>` is

==============  ============== ==============
first input     second input   return
==============  ============== ==============
:green:`True`   :green:`True`  :red:`False`
:green:`True`   :red:`False`   :red:`False`
:red:`False`    :green:`True`  :green:`True`
:red:`False`    :red:`False`   :green:`True`
==============  ============== ==============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for :ref:`negate_first<test_negate_first>` with an :ref:`assertion<what is an assertion?>` for when the first input is :green:`True` and the second input is :green:`True`, to ``test_binary.py``

==============  ============== ==============
first input     second input   return
==============  ============== ==============
:green:`True`   :red:`False`   :red:`False`
==============  ============== ==============

.. code-block:: python
  :lineno-start: 49
  :emphasize-lines: 23-26

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

      def test_negate_first(self):
          self.assertFalse(
              src.truth_table.negate_first(True, True)
          )


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'negate_first'

there is no definition for :ref:`negate_first<test_negate_first>` in ``truth_table.py``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

*  I use the :ref:`Explorer<explorer on left>` to open ``truth_table.py`` from the ``src`` folder_ in the :ref:`editor<2 editors>`

* I add the :ref:`function<what is a function?>` to ``truth_table.py``

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 9-10

    def converse_non_implication(first_input, second_input):
        return logical_conjunction(
            not first_input,
            second_input
        )
        return not first_input and second_input


    def negate_first(first_input, second_input):
        return False

  the test passes. :ref:`negate_first<test_negate_first>` returns :red:`False`, if the first input is :green:`True` and the second input is :green:`True`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for the second case, which is when the first input is :green:`True` and the second input is :red:`False`, to :ref:`test_negate_first` in ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :red:`False`   :red:`False`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 5-7

        def test_negate_first(self):
            self.assertFalse(
                src.truth_table.negate_first(True, True)
            )
            self.assertFalse(
                src.truth_table.negate_first(True, False)
            )


    # Exceptions seen

  the test is still green. :ref:`negate_first<test_negate_first>` returns

  - :red:`False`, if the first input is :green:`True` and the second input is :red:`False`
  - :red:`False`, if the first input is :green:`True` and the second input is :green:`True`
  - :red:`False`, if the first input is :green:`True`

* I add an :ref:`assertion<what is an assertion?>` for the next case, which is when the first input is :red:`False` and the second input is :green:`True`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :green:`True`  :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 8-10

        def test_negate_first(self):
            self.assertFalse(
                src.truth_table.negate_first(True, True)
            )
            self.assertFalse(
                src.truth_table.negate_first(True, False)
            )
            self.assertTrue(
                src.truth_table.negate_first(False, True)
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

* I add an :ref:`if statement<if statements>` for this case to :ref:`negate_first<test_negate_first>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 2-3

    def negate_first(first_input, second_input):
        if first_input == False:
            return True
        return False

  the test passes. :ref:`negate_first<test_negate_first>` returns

  - :green:`True`, if the first input is :red:`False` and the second input is :green:`True`
  - :red:`False`, if the above :ref:`condition<if statements>` is not met

* I add an :ref:`assertion<what is an assertion?>` for the last case, which is when the first input is :red:`False` and the second input is :red:`False` to :ref:`test_negate_first` in ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :red:`False`   :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 11-13

        def test_negate_first(self):
            self.assertFalse(
                src.truth_table.negate_first(True, True)
            )
            self.assertFalse(
                src.truth_table.negate_first(True, False)
            )
            self.assertTrue(
                src.truth_table.negate_first(False, True)
            )
            self.assertTrue(
                src.truth_table.negate_first(False, False)
            )


    # Exceptions seen

  the test is still green

* I add the :ref:`bool built-in function<booleans 2: test with bool>` to the :ref:`if statement<if statements>` in the :ref:`negate_first function<test_negate_first>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2-3

    def negate_first(first_input, second_input):
        # if first_input == False:
        if bool(first_input) == False:
            return True
        return False

  still green

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write it in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 3-4

    def negate_first(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        if not bool(first_input) == True:
            return True
        return False

  green

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 4-5

    def negate_first(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool(first_input) == True:
        if not bool(first_input):
            return True
        return False

  still green

* I remove :ref:`bool<booleans 2: test with bool>`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 5-6

    def negate_first(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool(first_input) == True:
        # if not bool(first_input):
        if not first_input:
            return True
        return False

  the test is still green, because ``if bool(something) == False`` is the same as ``if not bool(something) == True`` is the same as ``if not bool(something)`` is the same as ``if not something``

* I use a :ref:`conditional expression (ternary operator)<conditional expressions>`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2

    def negate_first(first_input, second_input):
        return True if not first_input else False
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool(first_input) == True:
        # if not bool(first_input):
        if not first_input:
            return True
        return False

  still green

* I remove ``True if`` and ``else False``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2

    def negate_first(first_input, second_input):
        return not first_input
        return True if not first_input else False
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool(first_input) == True:
        # if not bool(first_input):
        if not first_input:
            return True
        return False

  green

* I remove the other statements

  .. code-block:: python
    :lineno-start: 37

    def negate_first(first_input, second_input):
        return not first_input

:ref:`Negate First<test_negate_first>` always returns

* ``not first_input``
* :green:`True`, if the first input is :red:`False`
* :red:`False`, if the first input is :green:`True`
* the :ref:`opposite (Logical Negation)<test_logical_negation>` of the first input in all cases, it does not care about the second input

----

=================================================================================
examples of Negate First
=================================================================================

----

* approval to do something based on risk and reason, if the inputs are

  - is it risky?
  - has a good reason?

  ===============  =================  ================
  is risky?        has reason?        approved
  ===============  =================  ================
  :green:`yes`     :green:`good`      :red:`no`
  :green:`yes`     :red:`bad`         :red:`no`
  :red:`no`        :green:`good`      :green:`yes`
  :red:`no`        :red:`bad`         :green:`yes`
  ===============  =================  ================

* going for a walk, if the inputs are

  - is it raining?
  - do I feel like walking?

  ===============  ===================  ================
  is raining?      feel like walking?   should walk
  ===============  ===================  ================
  :green:`yes`     :green:`yes`         :red:`no`
  :green:`yes`     :red:`no`            :red:`no`
  :red:`no`        :green:`yes`         :green:`yes`
  :red:`no`        :red:`no`            :green:`yes`
  ===============  ===================  ================

* smoke detector battery test, if the inputs are

  - is the battery dead?
  - is there smoke?

  ===============  =================  ================
  battery dead?    is there smoke?    beep
  ===============  =================  ================
  :green:`yes`     :green:`yes`       :red:`NOT silent`
  :green:`yes`     :red:`no`          :red:`NOT silent`
  :red:`no`        :green:`yes`       :green:`silent`
  :red:`no`        :red:`no`          :green:`silent`
  ===============  =================  ================

* can the system be used while it is being updated, if the inputs are

  - is update running?
  - what kind of user?

  ===============  ==================  ==================
  update running?  what kind of user?  system can be used
  ===============  ==================  ==================
  :green:`yes`     :green:`admin`      :red:`no`
  :green:`yes`     :red:`guest`        :red:`no`
  :red:`no`        :green:`admin`      :green:`yes`
  :red:`no`        :red:`guest`        :green:`yes`
  ===============  ==================  ==================

* bad referee call, if the inputs are

  - is the home team playing?
  - is it a bad play?

  ===============  ==================  ==================
  is home team?    is bad play?        good call
  ===============  ==================  ==================
  :green:`yes`     :green:`no`         :red:`no`
  :green:`yes`     :red:`yes`          :red:`no`
  :red:`no`        :green:`no`         :green:`yes`
  :red:`no`        :red:`yes`          :green:`yes`
  ===============  ==================  ==================

----

*********************************************************************************
test_logical_nand
*********************************************************************************

The :ref:`truth table` for :ref:`logical_nand<test_logical_nand>` is

==============  ============== ==============
first input     second input   return
==============  ============== ==============
:green:`True`   :green:`True`  :red:`False`
:green:`True`   :red:`False`   :green:`True`
:red:`False`    :green:`True`  :green:`True`
:red:`False`    :red:`False`   :green:`True`
==============  ============== ==============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for :ref:`logical_nand<test_logical_nand>` with an :ref:`assertion<what is an assertion?>` for when the first input is :green:`True` and the second input is :green:`True`, to ``test_binary.py``

==============  ============== ==============
first input     second input   return
==============  ============== ==============
:green:`True`   :green:`True`  :red:`False`
==============  ============== ==============

.. code-block:: python
  :lineno-start: 71
  :emphasize-lines: 15-18

      def test_negate_first(self):
          self.assertFalse(
              src.truth_table.negate_first(True, True)
          )
          self.assertFalse(
              src.truth_table.negate_first(True, False)
          )
          self.assertTrue(
              src.truth_table.negate_first(False, True)
          )
          self.assertTrue(
              src.truth_table.negate_first(False, False)
          )

      def test_logical_nand(self):
          self.assertFalse(
              src.truth_table.logical_nand(True, True)
          )


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.truth_table' has no attribute 'logical_nand'. Did you mean: 'logical_false'?

because there is no definition for :ref:`logical_nand<test_logical_nand>` in ``truth_table.py``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add the :ref:`function<what is a function?>` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 37
  :emphasize-lines: 5-6

  def negate_first(first_input, second_input):
      return not first_input


  def logical_nand(first_input, second_input):
      return False


the test passes. :ref:`logical_nand<test_logical_nand>` returns :red:`False`, if the first input is :green:`True` and the second input is :green:`True`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for the second case, which is when the first input is :green:`True` and the second input is :red:`False`, to :ref:`test_logical_nand` in ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :red:`False`   :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 85
    :emphasize-lines: 5-7

        def test_logical_nand(self):
            self.assertFalse(
                src.truth_table.logical_nand(True, True)
            )
            self.assertTrue(
                src.truth_table.logical_nand(True, False)
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

  because the :ref:`function<what is a function?>` returns :red:`False` and the :ref:`assertion<what is an assertion?>` expects :green:`True`

* I add an :ref:`if statement<if statements>` to the :ref:`logical_nand function<test_logical_nand>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 2-3

    def logical_nand(first_input, second_input):
        if second_input == False:
            return True
        return False


  the test passes. :ref:`logical_nand<test_logical_nand>` returns

  - :green:`True`, if the second input is :red:`False`
  - :red:`False`, if the above condition is not met
  - the :ref:`logical negation<test_logical_negation>` of the second input so far

* I add another :ref:`assertion<what is an assertion?>`, for the case where the first input is :red:`False` and the second input is :green:`True`, to :ref:`test_logical_nand` in ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :green:`True`  :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 85
    :emphasize-lines: 8-10

        def test_logical_nand(self):
            self.assertFalse(
                src.truth_table.logical_nand(True, True)
            )
            self.assertTrue(
                src.truth_table.logical_nand(True, False)
            )
            self.assertTrue(
                src.truth_table.logical_nand(False, True)
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

  because the :ref:`logical_nand function<test_logical_nand>` returned :red:`False` and the :ref:`assertion<what is an assertion?>` expects :green:`True`

* I add an :ref:`if statement<if statements>` to the :ref:`logical_nand function<test_logical_nand>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 2-3

    def logical_nand(first_input, second_input):
        if first_input == False:
            return True
        if second_input == False:
            return True
        return False


  the test passes. :ref:`logical_nand<test_logical_nand>` returns

  - :green:`True`, if the first input is :red:`False`
  - :green:`True`, if the second input is :red:`False`
  - :red:`False`, if none of the above conditions are met

* I add an :ref:`assertion<what is an assertion?>` for the last case, which is when the first input is :red:`False` and the second input is :red:`False`, to :ref:`test_logical_nand` in ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :red:`False`   :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 85
    :emphasize-lines: 11-13

        def test_logical_nand(self):
            self.assertFalse(
                src.truth_table.logical_nand(True, True)
            )
            self.assertTrue(
                src.truth_table.logical_nand(True, False)
            )
            self.assertTrue(
                src.truth_table.logical_nand(False, True)
            )
            self.assertTrue(
                src.truth_table.logical_nand(False, False)
            )


    # Exceptions seen

  the test is still green

* There is only one case where :ref:`logical_nand<test_logical_nand>` returns :red:`False` I add an :ref:`if statement<if statements>` for it, in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 2-10

    def logical_nand(first_input, second_input):
        # if first_input == False:
        #     return True
        # if second_input == False:
        #     return True
        # return False
        if first_input == True:
            if second_input == True:
                return False
        return True

  still green

* I use the :ref:`bool built-in function<booleans 2: test with bool>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 7-10

    def logical_nand(first_input, second_input):
        # if first_input == False:
        #     return True
        # if second_input == False:
        #     return True
        # return False
        # if first_input == True:
        if bool(first_input) == True:
            # if second_input == True:
            if bool(second_input) == True:
                return False
        return True

  green

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 8-9, 11-12

    def logical_nand(first_input, second_input):
        # if first_input == False:
        #     return True
        # if second_input == False:
        #     return True
        # return False
        # if first_input == True:
        # if bool(first_input) == True:
        if bool(first_input):
            # if second_input == True:
            # if bool(second_input) == True:
            if bool(second_input):
                return False
        return True

  still green

* I remove :ref:`bool<booleans 2: test with bool>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 9-10, 13-14

    def logical_nand(first_input, second_input):
        # if first_input == False:
        #     return True
        # if second_input == False:
        #     return True
        # return False
        # if first_input == True:
        # if bool(first_input) == True:
        # if bool(first_input):
        if first_input:
            # if second_input == True:
            # if bool(second_input) == True:
            # if bool(second_input):
            if second_input:
                return False
        return True

  the test is still green, because ``if something == True`` is the same as ``if bool(something) == True`` is the same as ``if bool(something)`` is the same as ``if something``

* I use :ref:`Logical Conjunction (AND)<test_logical_conjunction>` to put the two :ref:`if statements` together

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 10, 14-15

    def logical_nand(first_input, second_input):
        # if first_input == False:
        #     return True
        # if second_input == False:
        #     return True
        # return False
        # if first_input == True:
        # if bool(first_input) == True:
        # if bool(first_input):
        # if first_input:
            # if second_input == True:
            # if bool(second_input) == True:
            # if bool(second_input):
            # if second_input:
        if first_input and second_input:
                return False
        return True


  still green, because I can use :ref:`AND<test_logical_conjunction>` to put two :ref:`if statements` together when one is indented under the other. For example

  .. code-block:: python

    if something:
        if something_else:

  can also be written as

  .. code-block:: python

    if something and something_else:

* I add an :ref:`else clause<if statements>` to make it clearer

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 16-18

    def logical_nand(first_input, second_input):
        # if first_input == False:
        #     return True
        # if second_input == False:
        #     return True
        # return False
        # if first_input == True:
        # if bool(first_input) == True:
        # if bool(first_input):
        # if first_input:
            # if second_input == True:
            # if bool(second_input) == True:
            # if bool(second_input):
            # if second_input:
        if first_input and second_input:
            return False
        else:
            return True

  green

* I rewrite the :ref:`else clause<if statements>` with the :ref:`Logical Negation (NOT)<test_logical_negation>` of ``first_input and second_input`` so I can write the statements with a :ref:`conditional expression (ternary operator)<conditional expressions>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 17-18

    def logical_nand(first_input, second_input):
        # if first_input == False:
        #     return True
        # if second_input == False:
        #     return True
        # return False
        # if first_input == True:
        # if bool(first_input) == True:
        # if bool(first_input):
        # if first_input:
            # if second_input == True:
            # if bool(second_input) == True:
            # if bool(second_input):
            # if second_input:
        if first_input and second_input:
            return False
        # else:
        if not (first_input and second_input):
            return True

  still green

* I move the first new :ref:`if statement<if statements>` below this new one

  .. TIP:: In `Visual Studio Code`_ I can move lines I select or where the cursor is, with :kbd:`alt/option+Up` on the keyboard to move lines up or  :kbd:`alt/option+Down` to move lines down

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 18-19

    def logical_nand(first_input, second_input):
        # if first_input == False:
        #     return True
        # if second_input == False:
        #     return True
        # return False
        # if first_input == True:
        # if bool(first_input) == True:
        # if bool(first_input):
        # if first_input:
            # if second_input == True:
            # if bool(second_input) == True:
            # if bool(second_input):
            # if second_input:
        # else:
        if not (first_input and second_input):
            return True
        if first_input and second_input:
            return False

  the test is still green

* I change it to an :ref:`else clause<if statements>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 18-19

    def logical_nand(first_input, second_input):
        # if first_input == False:
        #     return True
        # if second_input == False:
        #     return True
        # return False
        # if first_input == True:
        # if bool(first_input) == True:
        # if bool(first_input):
        # if first_input:
            # if second_input == True:
            # if bool(second_input) == True:
            # if bool(second_input):
            # if second_input:
        # else:
        if not (first_input and second_input):
            return True
        # if first_input and second_input:
        else:
            return False

  still green

* I add a :ref:`conditional expression<conditional expressions>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 16-20

    def logical_nand(first_input, second_input):
        # if first_input == False:
        #     return True
        # if second_input == False:
        #     return True
        # return False
        # if first_input == True:
        # if bool(first_input) == True:
        # if bool(first_input):
        # if first_input:
            # if second_input == True:
            # if bool(second_input) == True:
            # if bool(second_input):
            # if second_input:
        # else:
        return (
            True
            if not (first_input and second_input)
            else False
        )
        if not (first_input and second_input):
            return True
        # if first_input and second_input:
        else:
            return False

  green

* I remove ``True if`` and ``else False`` to make the statement simpler

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 16

    def logical_nand(first_input, second_input):
        # if first_input == False:
        #     return True
        # if second_input == False:
        #     return True
        # return False
        # if first_input == True:
        # if bool(first_input) == True:
        # if bool(first_input):
        # if first_input:
            # if second_input == True:
            # if bool(second_input) == True:
            # if bool(second_input):
            # if second_input:
        # else:
        return not (first_input and second_input)
        return (
            True
            if not (first_input and second_input)
            else False
        )
        if not (first_input and second_input):
            return True
        # if first_input and second_input:
        else:
            return False

* :ref:`logical_nand<test_logical_nand>` returns ``not (first_input and second_input)``, which means that in the 4 cases

  - if the first input is :green:`True` and the second input is :green:`True`, :ref:`logical_nand<test_logical_nand>` returns

    .. code-block:: python
      :emphasize-lines: 4

      not (first and second)
      not (True  and True)  # not logical_conjunction(True, True)
      not (True)            # not logical_conjunction(True, True)
      False

  - if the first input is :green:`True` and the second input is :red:`False`, :ref:`logical_nand<test_logical_nand>` returns

    .. code-block:: python
      :emphasize-lines: 4

      not (first and second)
      not (True  and False) # not logical_conjunction(True, False)
      not (False)           # not logical_conjunction(True, False)
      True

  - if the first input is :red:`False` and the second input is :green:`True`, :ref:`logical_nand<test_logical_nand>` returns

    .. code-block:: python
      :emphasize-lines: 4

      not (first and second)
      not (False and True)  # not logical_conjunction(False, True)
      not (False)           # not logical_conjunction(False, True)
      True

  - if the first input is :red:`False` and the second input is :red:`False`, :ref:`logical_nand<test_logical_nand>` returns

    .. code-block:: python
      :emphasize-lines: 4

      not (first and second)
      not (False and False) # not logical_conjunction(False, False)
      not (True)            # not logical_conjunction(False, False)
      True

  ==============  =============== =============== ================
  first           second          first           not (first
                                  and             and
                                  second          second)
  ==============  =============== =============== ================
  :green:`True`   :green:`True`   :green:`True`   :red:`False`
  :green:`True`   :red:`False`    :red:`False`    :green:`True`
  :red:`False`    :green:`True`   :red:`False`    :green:`True`
  :red:`False`    :red:`False`    :red:`False`    :green:`True`
  ==============  =============== =============== ================

  I add a `return statement`_ to show this

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 16-18

    def logical_nand(first_input, second_input):
        # if first_input == False:
        #     return True
        # if second_input == False:
        #     return True
        # return False
        # if first_input == True:
        # if bool(first_input) == True:
        # if bool(first_input):
        # if first_input:
            # if second_input == True:
            # if bool(second_input) == True:
            # if bool(second_input):
            # if second_input:
        # else:
        return not (
            logical_conjunction(first_input, second_input)
        )
        return not (first_input and second_input)
        return (
            True
            if not (first_input and second_input)
            else False
        )
        if not (first_input and second_input):
            return True
        # if first_input and second_input:
        else:
            return False


  the test is still green

* I remove the other statements and comments

  .. code-block:: python
    :lineno-start: 41

    def logical_nand(first_input, second_input):
        return not (
            logical_conjunction(first_input, second_input)
        )
        return not (first_input and second_input)

:ref:`Logical NAND<test_logical_nand>`

* returns :red:`False`, if the first input is :green:`True` and the second input is :green:`True`
* returns ``not (first_input and second_input)`` which is the :ref:`opposite (Logical Negation)<test_logical_negation>` of the :ref:`Logical Conjunction<test_logical_conjunction>` of the first input and the second input, many words
* is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Logical Conjunction<test_what_is_true>` which only returns :green:`True`, if the first input is :green:`True` and the second input is :green:`True`
* is the :ref:`not<test_logical_negation>` of the :ref:`and<test_logical_conjunction>` of the first input and second input, confusing?
* is :ref:`not and<test_logical_nand>`

----

=================================================================================
examples of Logical NAND
=================================================================================

----

* can the website be reached, if the inputs are

  - is main server down?
  - is backup server down?

  ================  ==================  ==================
  is main down?     is backup down?     can reach website?
  ================  ==================  ==================
  :green:`yes`      :green:`yes`        :red:`no`
  :green:`yes`      :red:`no`           :green:`yes`
  :red:`no`         :green:`yes`        :green:`yes`
  :red:`no`         :red:`no`           :green:`yes`
  ================  ==================  ==================

* safety when mixing household cleaning products, if the inputs are

  - is bleach?
  - is soap?

  ================  ==================  ==================
  is bleach?        is soap?            is safe when mixed?
  ================  ==================  ==================
  :green:`yes`      :green:`yes`        :red:`no`
  :green:`yes`      :red:`no`           :green:`yes`
  :red:`no`         :green:`yes`        :green:`yes`
  :red:`no`         :red:`no`           :green:`yes`
  ================  ==================  ==================

* fridge alarm, if the inputs are

  - door open?
  - temperature rose?

  ================  ==================  ==================
  door open?        temperature rose?   silent
  ================  ==================  ==================
  :green:`yes`      :green:`yes`        :red:`alarm`
  :green:`yes`      :red:`no`           :green:`silent`
  :red:`no`         :green:`yes`        :green:`silent`
  :red:`no`         :red:`no`           :green:`silent`
  ================  ==================  ==================

* deny a transaction, if the inputs are

  - amount is larger than normal?
  - the recipient is new?

  ================  ==================  ==================
  large amount?     new recipient?      approve/deny
  ================  ==================  ==================
  :green:`yes`      :green:`yes`        :red:`deny`
  :green:`yes`      :red:`no`           :green:`approve`
  :red:`no`         :green:`yes`        :green:`approve`
  :red:`no`         :red:`no`           :green:`approve`
  ================  ==================  ==================

* show content, if the inputs are

  - is user younger than 18?
  - is the content flagged as adult?

  ================  ==================  ==================
  less than 18?     adult content?      block/show
  ================  ==================  ==================
  :green:`yes`      :green:`yes`        :red:`block`
  :green:`yes`      :red:`no`           :green:`show`
  :red:`no`         :green:`yes`        :green:`show`
  :red:`no`         :red:`no`           :green:`show`
  ================  ==================  ==================

* stop 2 processes from writing to the same place, if the inputs are

  - is process A writing?
  - is process B writing?

  ================  ==================  ==================
  process A write?  process B write?    allow/stop
  ================  ==================  ==================
  :green:`yes`      :green:`yes`        :red:`stop`
  :green:`yes`      :red:`no`           :green:`allow`
  :red:`no`         :green:`yes`        :green:`allow`
  :red:`no`         :red:`no`           :green:`allow`
  ================  ==================  ==================

----

.. NOTE::

  When there is only one :ref:`if statement<if statements>` that returns :red:`False` with an `else clause`_

  .. code-block:: python

    if something:
        return False
    else:
        return True

  I can use its :ref:`logical negation (not)<test_logical_negation>` to return :ref:`True<test_what_is_true>`

  .. code-block:: python

    if not something:
        return True
    else:
        return False

  I can write it with a :ref:`ternary operator<conditional expressions>` (:ref:`conditional expression<conditional expressions>`)

  .. code-block:: python

    return True if not (something) else False

  which can be made simpler as

  .. code-block:: python

    return not (something)

  this means ``if something: return False`` is the same as ``return not (something)``

----

*********************************************************************************
test_tautology
*********************************************************************************

The :ref:`truth table` for :ref:`tautology<test_tautology>` is

==============  ============== ==============
first input     second input   return
==============  ============== ==============
:green:`True`   :green:`True`  :green:`True`
:green:`True`   :red:`False`   :green:`True`
:red:`False`    :green:`True`  :green:`True`
:red:`False`    :red:`False`   :green:`True`
==============  ============== ==============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for :ref:`tautology<test_tautology>` with an :ref:`assertion<what is an assertion?>` for when the first input is :green:`True` and the second input is :green:`True`, to ``test_binary.py``

==============  ============== ==============
first input     second input   return
==============  ============== ==============
:green:`True`   :green:`True`  :green:`True`
==============  ============== ==============

.. code-block:: python
  :lineno-start: 85
  :emphasize-lines: 15-18

      def test_logical_nand(self):
          self.assertFalse(
              src.truth_table.logical_nand(True, True)
          )
          self.assertTrue(
              src.truth_table.logical_nand(True, False)
          )
          self.assertTrue(
              src.truth_table.logical_nand(False, True)
          )
          self.assertTrue(
              src.truth_table.logical_nand(False, False)
          )

      def test_tautology(self):
          self.assertTrue(
              src.truth_table.tautology(True, True)
          )


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

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
  :lineno-start: 41
  :emphasize-lines: 8-9

    def logical_nand(first_input, second_input):
        return not (
            logical_conjunction(first_input, second_input)
        )
        return not (first_input and second_input)


    def tautology(first_input, second_input):
        return True

the test passes. :ref:`tautology<test_tautology>` returns :green:`True`, if the first input is :green:`True` and the second input is :green:`True`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for the next case, which is when the first input is :green:`True` and the second input is :red:`False`, to :ref:`test_tautology` in ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :red:`False`   :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 99
    :emphasize-lines: 5-7

        def test_tautology(self):
            self.assertTrue(
                src.truth_table.tautology(True, True)
            )
            self.assertTrue(
                src.truth_table.tautology(True, False)
            )


    # Exceptions seen

  the test is still green. :ref:`tautology<test_tautology>` returns

  - :green:`True`, if the first input is :green:`True` and the second input is :red:`False`
  - :green:`True`, if the first input is :green:`True` and the second input is :green:`True`
  - :green:`True`, if the first input is :green:`True`

* I add an :ref:`assertion<what is an assertion?>` for the next case, which is when the first input is :red:`False` and the second input is :green:`True`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :green:`True`  :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 99
    :emphasize-lines: 8-10

        def test_tautology(self):
            self.assertTrue(
                src.truth_table.tautology(True, True)
            )
            self.assertTrue(
                src.truth_table.tautology(True, False)
            )
            self.assertTrue(
                src.truth_table.tautology(False, True)
            )


    # Exceptions seen

  the test is still green. :ref:`tautology<test_tautology>` returns :green:`True`

  - if the first input is :red:`False` and the second input is :green:`True`
  - if the first input is :green:`True`

* I add an :ref:`assertion<what is an assertion?>` for the last case, which is when the first input is :red:`False` and the second input is :red:`False`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :red:`False`   :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 99
    :emphasize-lines: 11-13

        def test_tautology(self):
            self.assertTrue(
                src.truth_table.tautology(True, True)
            )
            self.assertTrue(
                src.truth_table.tautology(True, False)
            )
            self.assertTrue(
                src.truth_table.tautology(False, True)
            )
            self.assertTrue(
                src.truth_table.tautology(False, False)
            )


    # Exceptions seen

  still green, there is only one result for this operation.

:ref:`Tautology<test_tautology>` always returns :green:`True`, it does not care about the inputs. It is the opposite of :ref:`contradiction<test_contradiction>`  which always returns :red:`False`

----

=================================================================================
examples of Tautology
=================================================================================

----

* work, if the inputs are

  - do I have work?
  - do I feel like working?

  ===============  =================  ================
  have work?       feel like work?    work?
  ===============  =================  ================
  :green:`yes`     :green:`yes`       :green:`work`
  :green:`yes`     :red:`no`          :green:`work`
  :red:`no`        :green:`yes`       :green:`work`
  :red:`no`        :red:`no`          :green:`work`
  ===============  =================  ================

* the customer is always right, if the inputs are

  - did customer complain?
  - is customer new?

  ===============  =================  =================
  complain?        new?               is customer king?
  ===============  =================  =================
  :green:`yes`     :green:`yes`       :green:`yes`
  :green:`yes`     :red:`no`          :green:`yes`
  :red:`no`        :green:`yes`       :green:`yes`
  :red:`no`        :red:`no`          :green:`yes`
  ===============  =================  =================

* the sun is real, if the inputs are

  - am I awake?
  - is it bright or dark outside?

  ===============  =================  ================
  awake?           bright/dark?       is sun real?
  ===============  =================  ================
  :green:`yes`     :green:`bright`    :green:`yes`
  :green:`yes`     :red:`dark`        :green:`yes`
  :red:`no`        :green:`bright`    :green:`yes`
  :red:`no`        :red:`dark`        :green:`yes`
  ===============  =================  ================

* I can get better, if the inputs are

  - am I good?
  - have I done this before?

  ===============  =================  ================
  good?            done before?       can I get better?
  ===============  =================  ================
  :green:`yes`     :green:`yes`       :green:`yes`
  :green:`yes`     :red:`no`          :green:`yes`
  :red:`no`        :green:`yes`       :green:`yes`
  :red:`no`        :red:`no`          :green:`yes`
  ===============  =================  ================

* a noun is the name of a person, place or thing, if the inputs are

  - is a person?
  - is a place or a thing?

  ===============  =================  ================
  person?          place/thing?       noun is a name
  ===============  =================  ================
  :green:`yes`     :green:`place`     :green:`yes`
  :green:`yes`     :red:`thing`       :green:`yes`
  :red:`no`        :green:`place`     :green:`yes`
  :red:`no`        :red:`thing`       :green:`yes`
  ===============  =================  ================

* unconditional love, if the inputs are

  - has the person been good?
  - does the person deserve love?

  ===============  =================  ================
  been good?       deserving?         love?
  ===============  =================  ================
  :green:`yes`     :green:`yes`       :green:`love`
  :green:`yes`     :red:`no`          :green:`love`
  :red:`no`        :green:`yes`       :green:`love`
  :red:`no`        :red:`no`          :green:`love`
  ===============  =================  ================

----

*********************************************************************************
test_logical_disjunction
*********************************************************************************



----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for :ref:`logical_disjunction<test_logical_disjunction>` with an :ref:`assertion<what is an assertion?>` for when the first input is :green:`True` and the second input is :green:`True`, to ``test_binary.py``

.. code-block:: python
  :lineno-start: 99
  :emphasize-lines: 15-19

      def test_tautology(self):
          self.assertTrue(
              src.truth_table.tautology(True, True)
          )
          self.assertTrue(
              src.truth_table.tautology(True, False)
          )
          self.assertTrue(
              src.truth_table.tautology(False, True)
          )
          self.assertTrue(
              src.truth_table.tautology(False, False)
          )

      def test_logical_disjunction(self):
          self.assertTrue(
              src.truth_table.logical_disjunction(
                  True, True
              )
          )


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

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

the test passes. :ref:`logical_disjunction<test_logical_disjunction>` returns :green:`True`, if the first input is :green:`True` and the second input is :green:`True`

==============  ============== ==============
first input     second input   return
==============  ============== ==============
:green:`True`   :green:`True`  :green:`True`
==============  ============== ==============

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for the next case, which is when the first input is :green:`True` and the second input is :red:`False`, to :ref:`test_logical_disjunction` in ``test_binary.py``

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

  - :green:`True`, if the first input is :green:`True` and the second input is :red:`False`
  - :green:`True`, if the first input is :green:`True` and the second input is :green:`True`
  - :green:`True`, if the first input is :green:`True`

  so far this is the same as :ref:`Tautology<test_tautology>`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :green:`True`
  :green:`True`   :red:`False`   :green:`True`
  ==============  ============== ==============

* I add an :ref:`assertion<what is an assertion?>` for the next case, which is when the first input is :red:`False` and the second input is :green:`True`

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

  - :green:`True`, if the first input is :red:`False` and the second input is :green:`True`
  - :green:`True`, if the first input is :green:`True`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :green:`True`
  :green:`True`   :red:`False`   :green:`True`
  :red:`False`    :green:`True`  :green:`True`
  ==============  ============== ==============

* I add an :ref:`assertion<what is an assertion?>` for the fourth case, where the first input is :red:`False` and the second input is :red:`False`

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

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

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

  - :red:`False`, if the first input is :red:`False` and the second input is :red:`False` - this is the only case where it returns :red:`False`
  - :green:`True`, if the first input is :red:`False` and the second input is :green:`True`
  - :green:`True`, if the first input is :green:`True`

* I change the two :ref:`if statements` to one :ref:`if statement<if statements>` with :ref:`Logical Conjunction (AND)<test_logical_conjunction>`

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

* I use the :ref:`bool built-in function<booleans 2: test with bool>`

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

  the test is still green. A reminder that I can return the :ref:`Logical Negation (not)<test_logical_negation>` of an :ref:`if statement<if statements>` that returns :red:`False` like I did with :ref:`Logical NAND<test_logical_nand>`

  .. NOTE::

    ``return not ((not first_input) and (not second_input))`` returns the :ref:`opposite (Logical Negation)<test_logical_negation>` of the :ref:`Logical Conjunction<test_logical_conjunction>` of the :ref:`Logical Negation<test_logical_negation>` of ``first_input``, and the :ref:`Logical Negation<test_logical_negation>` of ``second_input``. This means that in the 4 cases

    - if the first input is :green:`True` and the second input is :green:`True`, :ref:`logical_disjunction<test_logical_disjunction>` returns

      .. code-block:: python
        :emphasize-lines: 5

        not ((not first) and (not second))
        not ((not True)  and (not True)  )
        not (False       and False       )
        not False        # not logical_conjunction(False, False)
        True

    - if the first input is :green:`True` and the second input is :red:`False`, :ref:`logical_disjunction<test_logical_disjunction>` returns

      .. code-block:: python
        :emphasize-lines: 5

        not ((not first) and (not second))
        not ((not True)  and (not False) )
        not (False       and True        )
        not False        # not logical_conjunction(False, True)
        True

    - if the first input is :red:`False` and the second input is :green:`True`, :ref:`logical_disjunction<test_logical_disjunction>` returns

      .. code-block:: python
        :emphasize-lines: 5

        not ((not first) and (not second))
        not ((not False) and (not True)  )
        not (True        and False       )
        not False        # not logical_conjunction(True, False)
        True

    - if the first input is :red:`False` and the second input is :red:`False`, :ref:`logical_disjunction<test_logical_disjunction>` returns

      .. code-block:: python
        :emphasize-lines: 5

        not ((not first) and (not second))
        not ((not False) and (not False) )
        not (True        and True        )
        not True         # not logical_conjunction(True, True)
        False

    ==============  =============== ===============  ================ ==================  ====================
    first           second          not first        not second       ((not first)        not ((not first)
                                                                      and                 and
                                                                      (not second))       (not second))
    ==============  =============== ===============  ================ ==================  ====================
    :green:`True`   :green:`True`   :red:`False`     :red:`False`     :red:`False`        :green:`True`
    :green:`True`   :red:`False`    :red:`False`     :green:`True`    :red:`False`        :green:`True`
    :red:`False`    :green:`True`   :green:`True`    :red:`False`     :red:`False`        :green:`True`
    :red:`False`    :red:`False`    :green:`True`    :green:`True`    :green:`True`       :red:`False`
    ==============  =============== ===============  ================ ==================  ====================


* ":ref:`not<test_logical_negation>`" appears 3 times in this statement, I want to change that. I "multiply" it by each thing inside the parentheses to try to make the statement simpler

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 2

    def logical_disjunction(first_input, second_input):
        return (not not first_input) (not and) (not not second_input)
        return not ((not first_input) and (not second_input))

  the terminal_ is my friend, and shows SyntaxError_

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
* :red:`False`, if the first input is :red:`False` and the second input is :red:`False`

==============  ============== ==============
first input     second input   return
==============  ============== ==============
:green:`True`   :green:`True`  :green:`True`
:green:`True`   :red:`False`   :green:`True`
:red:`False`    :green:`True`  :green:`True`
:red:`False`    :red:`False`   :red:`False`
==============  ============== ==============

----

=================================================================================
examples of Logical Disjunction
=================================================================================

----

* system works, if the inputs are

  - is main system running?
  - is backup system running?

  ================  ==================  ==================
  is main running?  is backup running?  is system working?
  ================  ==================  ==================
  :green:`yes`      :green:`yes`        :green:`yes`
  :green:`yes`      :red:`no`           :green:`yes`
  :red:`no`         :green:`yes`        :green:`yes`
  :red:`no`         :red:`no`           :red:`no`
  ================  ==================  ==================

* emergency room triage, if the inputs are

  - is it life threatening?
  - is patient a child?

  ================  ==================  ==================
  life threat?      child?              treat immediately
  ================  ==================  ==================
  :green:`yes`      :green:`yes`        :green:`yes`
  :green:`yes`      :red:`no`           :green:`yes`
  :red:`no`         :green:`yes`        :green:`yes`
  :red:`no`         :red:`no`           :red:`no`
  ================  ==================  ==================

* automatic door that opens, if the inputs are

  - has keycard?
  - entered code?

  ================  ==================  ==================
  has keycard?      entered code?       open door
  ================  ==================  ==================
  :green:`yes`      :green:`yes`        :green:`yes`
  :green:`yes`      :red:`no`           :green:`yes`
  :red:`no`         :green:`yes`        :green:`yes`
  :red:`no`         :red:`no`           :red:`no`
  ================  ==================  ==================

* give discount if the person is already a customer or has a coupon, if the inputs are

  - is already a customer?
  - has coupon code?

  ================  ================  =============
  already customer  has coupon        give discount
  ================  ================  =============
  :green:`yes`      :green:`yes`      :green:`yes`
  :green:`yes`      :red:`no`         :green:`yes`
  :red:`no`         :green:`yes`      :green:`yes`
  :red:`no`         :red:`no`         :red:`no`
  ================  ================  =============

* elevator moves, if the inputs are

  - did I push the button?
  - did someone else push the button?


  ================  ===================  ==================
  I pushed          someone else pushed  elevator moves
  ================  ===================  ==================
  :green:`yes`      :green:`yes`         :green:`yes`
  :green:`yes`      :red:`no`            :green:`yes`
  :red:`no`         :green:`yes`         :green:`yes`
  :red:`no`         :red:`no`            :red:`no`
  ================  ===================  ==================

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

Binary Operations take 2 inputs, each input can be :ref:`True<test_what_is_true>` or :red:`False`, if the first input is named ``first_input`` and the second input is named ``second_input``, the tests show that

* :ref:`Logical Disjunction<test_logical_disjunction>`

  - returns ``first_input or second_input``
  - returns :red:`False` only if ``first_input`` is :red:`False` and ``second_input`` is :ref:`False<test_what_is_false>`
  - is the  :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Logical NOR<test_logical_nor>` which returns :green:`True` only if ``first_input`` is :ref:`False<test_what_is_False>` and ``second_input`` is :ref:`False<test_what_is_false>`

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
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`contradiction<test_contradiction>`  which always returns :red:`False`

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
  - is the :ref:`opposite (Logical Negation) (not)<test_logical_negation>` of :ref:`Logical Conjunction (and)<test_logical_conjunction>` which returns :green:`True` only if ``first_input`` is :green:`True` and ``second_input`` is :green:`True`

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
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Project First<test_project_first>` which returns :green:`True` only if ``first_input`` is :green:`True`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :red:`False`
  :green:`True`   :red:`False`   :red:`False`
  :red:`False`    :green:`True`  :green:`True`
  :red:`False`    :red:`False`   :green:`True`
  ==============  ============== ==============

* :ref:`Converse NonImplication<test_converse_non_implication>`

  - returns ``not first_input and second_input``
  - returns :green:`True` only if ``first_input`` is :red:`False` and ``second_input`` is :green:`True`
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Converse Implication<test_converse_implication>` which returns :red:`False` if ``first_input`` is :red:`False` and ``second_input`` is :green:`True`

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
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Negate Second<test_negate_second>` which returns :green:`True` only if ``second_input`` is :red:`False`

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
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Logical NAND<test_logical_nand>` which returns :red:`False` only if ``first_input`` is :green:`True` and ``second_input`` is :green:`True`

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
  - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Tautology<test_tautology>` which always returns :green:`True`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :red:`False`
  :green:`True`   :red:`False`   :red:`False`
  :red:`False`    :green:`True`  :red:`False`
  :red:`False`    :red:`False`   :red:`False`
  ==============  ============== ==============

and

* :ref:`Logical Disjunction is "or"<test_logical_disjunction>`
* :ref:`Logical Conjunction is "AND"<test_logical_conjunction>`
* :ref:`Logical Negation is "NOT" <test_logical_negation>`

All the logic statements or conditions have been written with some or all of these 3.

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

:ref:`Would you like test even more binary operations? <binary_operations_3>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->