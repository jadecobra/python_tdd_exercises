.. meta::
  :description: Truth table Binary Operations 2 in Python using TDD—add four more binary logic gates to test_binary.py: negate_first (not first), logical_nand (not (first and second)), tautology (always True), logical_disjunction (OR: first or second). Continue pytest-watcher Red-Green-Refactor with assertTrue/assertFalse on all four TT/TF/FT/FF combinations per operation. Refactor nested if-statements into conditional expressions and ternary operators; apply De Morgan's Law (not (A and B) → not A or not B) to reach not ((not first) and (not second)) for OR. Debug SyntaxError invalid syntax from edit artifacts. Real-world examples: smoke detector battery+smoke beep rule, main+backup server downtime, emergency room triage. Preview test_binary_2.py (8 operations cumulative). Logical Disjunction is OR; NAND is NOT of AND. Requires Binary Operations 1. Jacob Itegboje Pumping Python.
  :keywords: Jacob Itegboje, Pumping Python, truth table Binary Operations 2, test_binary_2.py, negate_first not first, logical_nand not first and second, tautology always True, logical_disjunction OR first or second, De Morgan's Law python boolean, not A and B refactor to not A or not B, nested if to ternary conditional expression, SyntaxError invalid syntax truth table, AssertionError True is not false, smoke detector battery dead logic, server redundancy backup down, emergency room triage OR rule, TDD red green refactor binary operations, assertTrue assertFalse unittest, eight binary operations truth table, programming logic gates beginners, boolean algebra software engineering

.. include:: ../../links.rst

.. _binary_operations_2:

#################################################################################
truth table: Binary Operations 2
#################################################################################

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
  :caption: truth_table/tests/test_binary.py
  :lines: 1-21

.. literalinclude:: ../../code/truth_table/tests/test_binary_2.py
  :language: python
  :lineno-start: 23
  :caption: truth_table/tests/test_binary.py
  :lines: 23-37

.. literalinclude:: ../../code/truth_table/tests/test_binary_2.py
  :language: python
  :lineno-start: 39
  :caption: truth_table/tests/test_binary.py
  :lines: 39-51

.. literalinclude:: ../../code/truth_table/tests/test_binary_2.py
  :language: python
  :lineno-start: 53
  :caption: truth_table/tests/test_binary.py
  :lines: 53-

----

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

* I hold :kbd:`ctrl` (Windows_) or :kbd:`option` (MacOS_) on the keyboard, then click on ``tests/test_binary.py`` with the mouse to open it

* So far I have tested

  - :ref:`contradiction<test_contradiction>` which always returns :red:`False`
  - :ref:`logical_conjunction aka and<test_logical_conjunction>` which returns ``first_input and second_input``
  - :ref:`project_second<test_project_second>` which always returns ``second_input``
  - :ref:`converse_non_implication<test_converse_non_implication>` which returns ``not first_input and second_input``

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

I add a test for :ref:`negate_first<test_negate_first>` with an :ref:`assertion<what is an assertion?>` for if the first input is :green:`True` and the second input is :green:`True`, to ``test_binary.py``

==============  ============== ==============
first input     second input   return
==============  ============== ==============
:green:`True`   :green:`True`  :red:`False`
==============  ============== ==============

.. code-block:: python
  :lineno-start: 37
  :emphasize-lines: 3-5

          self.assertFalse(converse_non_implication(False, False))

      def test_negate_first(self):
          negate_first = src.truth_table.negate_first
          self.assertFalse(negate_first(True, True))


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: python

  AttributeError: module 'src.truth_table'
                  has no attribute 'negate_first'

there is no definition for :ref:`negate_first<test_negate_first>` in ``truth_table.py``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I open ``truth_table.py`` from the ``src`` folder_

* I add ``negate_first`` to ``truth_table.py``

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 9-10

    def converse_non_implication(first_input, second_input):
        return logical_conjunction(
            logical_negation(first_input),
            second_input
        )
        return not first_input and second_input


    def negate_first(first_input, second_input):
        return False

  the test passes. :ref:`negate_first<test_negate_first>` returns :red:`False`, if the first input is :green:`True` and the second input is :green:`True`.

  .. code-block:: python

    negate_first(True , True ) -> False

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for the second case, which is if the first input is :green:`True` and the second input is :red:`False`, to :ref:`test_negate_first` in ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :red:`False`   :red:`False`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 4

        def test_negate_first(self):
            negate_first = src.truth_table.negate_first
            self.assertFalse(negate_first(True, True))
            self.assertFalse(negate_first(True, False))


    # Exceptions seen

  the test is still green. :ref:`negate_first<test_negate_first>` returns

  - :red:`False`, if the first input is :green:`True` and the second input is :red:`False`.
  - :red:`False`, if the first input is :green:`True` and the second input is :green:`True`.
  - :red:`False`, if the first input is :green:`True`.

  .. code-block:: python

    negate_first(True , False) -> False
    negate_first(True , True ) -> False

* I add an :ref:`assertion<what is an assertion?>` for the next case, which is if the first input is :red:`False` and the second input is :green:`True`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :green:`True`  :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 5

        def test_negate_first(self):
            negate_first = src.truth_table.negate_first
            self.assertFalse(negate_first(True, True))
            self.assertFalse(negate_first(True, False))
            self.assertTrue(negate_first(False, True))


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  because :ref:`the negate_first function<test_negate_first>` returns :red:`False` and the :ref:`assertion<what is an assertion?>` expects :green:`True`.

* I add an :ref:`if statement<if statements>` for this case to :ref:`negate_first<test_negate_first>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2-3

    def negate_first(first_input, second_input):
        if first_input == False:
            return True
        return False

  the test passes. :ref:`negate_first<test_negate_first>` returns

  - :green:`True`, if the first input is :red:`False`
  - :red:`False`, if the above :ref:`condition<if statements>` is not met

  .. code-block:: python

    negate_first(False, True ) -> True
    negate_first(True , False) -> False
    negate_first(True , True ) -> False

* I add an :ref:`assertion<what is an assertion?>` for the last case, which is if the first input is :red:`False` and the second input is :red:`False` to :ref:`test_negate_first` in ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :red:`False`   :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 6

        def test_negate_first(self):
            negate_first = src.truth_table.negate_first
            self.assertFalse(negate_first(True, True))
            self.assertFalse(negate_first(True, False))
            self.assertTrue(negate_first(False, True))
            self.assertTrue(negate_first(False, False))


    # Exceptions seen

  the test is still green because Python_ checks if ``first_input`` is equal to :red:`False` when ``if first_input == False:`` runs,

  - if ``first_input`` is NOT equal to :red:`False`, it leaves the :ref:`if statement<if statements>` and continues to run the rest of the :ref:`function<what is a function?>` - ``return False`` then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`

    .. code-block:: shell

      negate_first(True , True ) -> False
      └── def negate_first(first_input, second_input):
          ├── first_input  == True
          ├── second_input == True
          ├── if first_input == False:
          │       return True
          └── return False

    .. code-block:: shell

      negate_first(True , False) -> False
      └── def negate_first(first_input, second_input):
          ├── first_input  == True
          ├── second_input == False
          ├── if first_input == False:
          │       return True
          └── return False

  - if ``first_input`` is equal to :red:`False`, it goes to the next line - ``return True`` then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`

    .. code-block:: shell

      negate_first(False, True ) -> True
      └── def negate_first(first_input, second_input):
          ├── first_input  == False
          ├── second_input == True
          └── if first_input == False:
              └── return True
              else:
                  return False

    .. code-block:: shell

      negate_first(False, False) -> True
      └── def negate_first(first_input, second_input):
          ├── first_input  == False
          ├── second_input == False
          └── if first_input == False:
              └── return True
              else:
                  return False

* I add :ref:`the bool built-in function<how to test if something is grouped as True>` to the :ref:`if statement<if statements>` in :ref:`the negate_first function<test_negate_first>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2-3

    def negate_first(first_input, second_input):
        # if first_input == False:
        if bool(first_input) == False:
            return True
        return False

  still green.

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write it in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 3-4

    def negate_first(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        if not bool( first_input) == True:
            return True
        return False

  green.

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 4-5

    def negate_first(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool( first_input) == True:
        if not bool( first_input):
            return True
        return False

  still green.

* I remove :ref:`bool<how to test if something is grouped as True>`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 5-6

    def negate_first(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool( first_input) == True:
        # if not bool( first_input):
        if not first_input:
            return True
        return False

  the test is still green because Python_ checks the value of ``not first_input`` when ``if not first_input:`` runs

  - if the value of ``something`` is :red:`False`

    .. literalinclude:: ../../code/truth_table/solutions/if_not_something_false.py
      :language: python

  - if the value of ``something`` is :green:`True`

    .. literalinclude:: ../../code/truth_table/solutions/if_not_something_true.py
      :language: python

  ``if bool(something) == False`` is the same as ``if not bool( something) == True`` is the same as ``if not bool( something)`` is the same as ``if not something``.

* I add an :ref:`else clause<if statements>` to be clearer

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 8-9

    def negate_first(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool( first_input) == True:
        # if not bool( first_input):
        if not first_input:
            return True
        else:
            return False

  still green.

* I use a :ref:`conditional expression (ternary operator)<conditional expressions>` for the :ref:`if statements`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 6-10

    def negate_first(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool( first_input) == True:
        # if not bool( first_input):
        # if not first_input:
        #     return True
        # else:
        #     return False
        return True if not first_input else False

  still green.

  .. code-block:: python

    if not first_input: vs return True
        return True     vs if not first_input
    else:               vs else
        return False    vs False

* I remove ``True if`` and ``else False``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 10-11

    def negate_first(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool( first_input) == True:
        # if not bool( first_input):
        # if not first_input:
        #     return True
        # else:
        #     return False
        # return True if not first_input else False
        return not first_input

  green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 37

    def negate_first(first_input, second_input):
        return not first_input

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add negate_first'

:ref:`Negate First<test_negate_first>` always returns

* ``not first_input``
* :green:`True`, if the first input is :red:`False`.
* :red:`False`, if the first input is :green:`True`.
* the :ref:`Logical Negation (NOT)<test_logical_negation>` of the first input in all cases. It does not care about the second input, it negates the first input.

----

=================================================================================
examples of Negate First
=================================================================================

----

* approval to do something based only on risk, if the inputs are

  - is it risky?
  - has a good reason?

  ===============  =================  ================
  is risky?        good reason?       approved
  ===============  =================  ================
  :green:`yes`     :green:`yes`       :red:`no`
  :green:`yes`     :red:`no`          :red:`no`
  :red:`no`        :green:`yes`       :green:`yes`
  :red:`no`        :red:`no`          :green:`yes`
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
  :green:`yes`     :green:`yes`       :red:`no`
  :green:`yes`     :red:`no`          :red:`no`
  :red:`no`        :green:`yes`       :green:`yes`
  :red:`no`        :red:`no`          :green:`yes`
  ===============  =================  ================

* can the system be used while it is being updated, if the inputs are

  - is update running?
  - is user admin?

  ===============  ==================  ==================
  update running?  admin?              system can be used
  ===============  ==================  ==================
  :green:`yes`     :green:`yes`        :red:`no`
  :green:`yes`     :red:`no`           :red:`no`
  :red:`no`        :green:`yes`        :green:`yes`
  :red:`no`        :red:`no`           :green:`yes`
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

* I go back to the terminal_ where the tests are running
* I add a test for :ref:`logical_nand<test_logical_nand>` with an :ref:`assertion<what is an assertion?>` for if the first input is :green:`True` and the second input is :green:`True`, to ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :red:`False`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 3-5

            self.assertTrue(negate_first(False, False))

        def test_logical_nand(self):
            nand = src.truth_table.logical_nand
            self.assertFalse(nand(True, True))


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table'
                    has no attribute 'logical_nand'.
                    Did you mean: 'logical_false'?

  because there is no definition for :ref:`logical_nand<test_logical_nand>` in ``truth_table.py``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``logical_nand`` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 37
  :emphasize-lines: 5-6

  def negate_first(first_input, second_input):
      return not first_input


  def logical_nand(first_input, second_input):
      return False


the test passes. :ref:`logical_nand<test_logical_nand>` returns :red:`False`, if the first input is :green:`True` and the second input is :green:`True`.

.. code-block:: python

  logical_nand(True , True ) -> False

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for the second case, which is if the first input is :green:`True` and the second input is :red:`False`, to :ref:`test_logical_nand` in ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :red:`False`   :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 4

        def test_logical_nand(self):
            nand = src.truth_table.logical_nand
            self.assertFalse(nand(True, True))
            self.assertTrue(nand(True, False))


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  because the :ref:`function<what is a function?>` returns :red:`False` and the :ref:`assertion<what is an assertion?>` expects :green:`True`.

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
  - :red:`False`, if the above condition is NOT met
  - the :ref:`logical negation<test_logical_negation>` of the second input so far

  .. code-block:: python

    logical_nand(True , False) -> True
    logical_nand(True , True ) -> False

* I add another :ref:`assertion<what is an assertion?>`, for the case when the first input is :red:`False` and the second input is :green:`True`, to :ref:`test_logical_nand` in ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :green:`True`  :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 5

        def test_logical_nand(self):
            nand = src.truth_table.logical_nand
            self.assertFalse(nand(True, True))
            self.assertTrue(nand(True, False))
            self.assertTrue(nand(False, True))


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  because Python_ checks if ``second_input`` is equal to :red:`False` when ``if second_input == False:`` runs,

  - if ``second_input`` is NOT equal to :red:`False`, it leaves the :ref:`if statement<if statements>` and continues to run the rest of the :ref:`function<what is a function?>` - ``return False`` then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`

  - if ``second_input`` is equal to :red:`False`, it goes to the next line - ``return True`` then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`


  - ``second_input`` is :green:`True` in this case, which raises :ref:`AssertionError<what causes AssertionError?>` since the :ref:`function<what is a function?>` returns :red:`False` and the :ref:`assertion<what is an assertion?>` expects :green:`True`

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

  .. code-block:: python

    logical_nand(False, True ) -> True
    logical_nand(True , False) -> True
    logical_nand(True , True ) -> False

* I add an :ref:`assertion<what is an assertion?>` for the last case, which is if the first input is :red:`False` and the second input is :red:`False`, to :ref:`test_logical_nand` in ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :red:`False`   :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 6

        def test_logical_nand(self):
            nand = src.truth_table.logical_nand
            self.assertFalse(nand(True, True))
            self.assertTrue(nand(True, False))
            self.assertTrue(nand(False, True))
            self.assertTrue(nand(False, False))


    # Exceptions seen

  the test is still green because when :ref:`logical_nand<test_logical_nand>` is :ref:`called<how to call a function with input>` it runs ``if first_input == False:``, where Python_ checks if ``first_input`` is equal to :red:`False`


  * if ``first_input`` is equal to :red:`False`, it goes to the next line - ``return True`` then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`

    .. code-block:: shell

      logical_nand(False, False) -> True
      └── def logical_nand(first_input, second_input):
          ├── first_input  == False
          ├── second_input == False
          └── if first_input  == False:
              └── return True
              if second_input == False:
                  return True
              return False

    .. code-block:: shell

      logical_nand(False, True ) -> True
      └── def logical_nand(first_input, second_input):
          ├── first_input  == False
          ├── second_input == True
          └── if first_input  == False:
              └── return True
              if second_input == False:
                  return True
              return False

  * if ``first_input`` is NOT equal to :red:`False`, it leaves the :ref:`if statement<if statements>` and continues to the next :ref:`if statement<if statements>` in the :ref:`function<what is a function?>` - ``if second_input == False:`` which checks if ``second_input`` is equal to :red:`False`

    - if ``second_input`` is equal to :red:`False`, it goes to the next line - ``return True`` then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`

      .. code-block:: shell

        logical_nand(True , False) -> True
        └── def logical_nand(first_input, second_input):
            ├── first_input  == True
            ├── second_input == False
            ├── if first_input  == False:
            │       return True
            └── if second_input == False:
                └── return True
                return False

    - if ``second_input`` is NOT equal to :red:`False`, it leaves the :ref:`if statement<if statements>` and continues to run the rest of the :ref:`function<what is a function?>` - ``return False`` then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`

      .. code-block:: shell

        logical_nand(True , True ) -> False
        └── def logical_nand(first_input, second_input):
            ├── first_input  == True
            ├── second_input == True
            ├── if first_input  == False:
            │       return True
            ├── if second_input == False:
            │       return True
            └── return False

* There is only one case where :ref:`logical_nand<test_logical_nand>` returns :red:`False` (the first case, when the first input is :green:`True` and the second input is :green:`True`). I add :ref:`if statements` for it, in ``truth_table.py``

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

  still green because :ref:`logical_nand<test_logical_nand>` returns

  - :red:`False` if the first input is :green:`True` and the second input is :green:`True`
  - :green:`True` if the above condition is NOT met

  .. code-block:: python

    logical_nand(False, False) -> True
    logical_nand(False, True ) -> True
    logical_nand(True , False) -> True
    logical_nand(True , True ) -> False

  Python_ checks if ``first_input`` is equal to :green:`True` when ``if first_input == True:`` runs

  - if ``first_input`` is NOT equal to :green:`True`, it leaves the :ref:`if statement<if statements>` and continues to run the rest of the :ref:`function<what is a function?>` - ``return True`` then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`

    .. code-block:: shell

      logical_nand(False, False) -> True
      └── def logical_nand(first_input, second_input):
          ├── first_input  == False
          ├── second_input == False
          ├── if first_input == True:
          │       if second_input == True:
          │           return False
          └── return True

    .. code-block:: shell

      logical_nand(False, True ) -> True
      └── def logical_nand(first_input, second_input):
          ├── first_input  == False
          ├── second_input == True
          ├── if first_input == True:
          │       if second_input == True:
          │           return False
          └── return True

  - if ``first_input`` is equal to :green:`True`, it goes to the next :ref:`if statement<if statements>` - ``if second_input == True``, which checks if ``second_input`` is equal to :green:`True`

    * if ``second_input`` is NOT equal to :green:`True`, it leaves the :ref:`if statement<if statements>` and continues to run the rest of the :ref:`function<what is a function?>` - ``return True`` then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`

      .. code-block:: shell

        logical_nand(True , False) -> True
        └── def logical_nand(first_input, second_input):
            ├── first_input  == True
            ├── second_input == False
            └── if first_input == True:
            ┌───┴── if second_input == True:
            │           return False
            └── return True

    * if ``second_input`` is equal to :green:`True`, it goes to the next line - ``return False`` then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`

      .. code-block:: shell

        logical_nand(True , True ) -> False
        └── def logical_nand(first_input, second_input):
            ├── first_input  == True
            ├── second_input == True
            └── if first_input == True:
                └── if second_input == True:
                    └── return False
                return True

  - it only checks the second input if the first input is :green:`True`.

* I use :ref:`the bool built-in function<how to test if something is grouped as True>`

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

  green.

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

  still green.

* I remove :ref:`bool<how to test if something is grouped as True>`

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

  the test is still green, because I can assume the following substitutions for ``if something == True:``

  - if the value of ``something`` is :red:`False`

    .. literalinclude:: ../../code/truth_table/solutions/if_something_false.py
      :language: python

  - if the value of ``something`` is :green:`True`

    .. literalinclude:: ../../code/truth_table/solutions/if_something_true.py
      :language: python

  ``if bool(something) == True`` is the same as ``if bool(something)`` is the same as ``if something``.

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

  still green, because I can put two :ref:`if statements` together when one is indented under the other

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

  green.

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

  still green.

* I move the first :ref:`if statement<if statements>` below this new one

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

  the test is still green.

* I change ``if first_input and second_input`` to an :ref:`else clause<if statements>`

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

  still green.

* I add a :ref:`conditional expression<conditional expressions>`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 2-3, 5-11

        # else:
        # if not (first_input and second_input):
        #     return True
        # if first_input and second_input:
        # else:
        #     return False
        return (
            True if
            not (first_input and second_input)
            else False
        )

  green.

  .. code-block:: python

    if not (              vs return True
        first_input
        and second_input
    ):
        return True       vs if not (first_input and second_input)
    else:                 vs else
        return False      vs False

* I remove ``True if`` and ``else False`` to make the statement simpler

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 8, 10

        # else:
        # if not (first_input and second_input):
        #     return True
        # if first_input and second_input:
        # else:
        #     return False
        return (
            # True if
            not (first_input and second_input)
            # else False
        )

  still green because when there is only one :ref:`if statement<if statements>` that returns :red:`False` with an `else clause`_

  .. code-block:: python

    if something:
        return False
    else:
        return True

  since ``else`` is the :ref:`logical_negation (not)<test_logical_negation>` of the :ref:`if statement<if statements>`

  .. code-block:: python

    if something:
        return False
    if not something:
        return True

  I can use its :ref:`logical negation (not)<test_logical_negation>` to return :ref:`True<test_what_is_true>`

  .. code-block:: python

    if not something:
        return True
    else:
        return False

  I can then write it with a :ref:`ternary operator<conditional expressions>` (:ref:`conditional expression<conditional expressions>`)

  .. code-block:: python

    return True if not (something) else False

  which can be made simpler as

  .. code-block:: python

    return not (something)

  this means ``if something: return False`` is the same as ``return not (something)`` since :ref:`Python groups objects as False or True<what are booleans?>`.

* :ref:`logical_nand<test_logical_nand>` returns ``not (first_input and second_input)`` which is the :ref:`Logical Negation (NOT)<test_logical_negation>` of the :ref:`Logical Conjunction (AND)<test_logical_conjunction>` of the first input and second input, which means that in the four cases

  - if the first input is :green:`True` and the second input is :green:`True`, :ref:`logical_nand<test_logical_nand>` returns

    .. code-block:: python
      :emphasize-lines: 4

      not (first and second)
      not (True  and True  )  # not logical_conjunction(True, True)
      not (True            )
      False

  - if the first input is :green:`True` and the second input is :red:`False`, :ref:`logical_nand<test_logical_nand>` returns

    .. code-block:: python
      :emphasize-lines: 4

      not (first and second)
      not (True  and False ) # not logical_conjunction(True, False)
      not (False           )
      True

  - if the first input is :red:`False` and the second input is :green:`True`, :ref:`logical_nand<test_logical_nand>` returns

    .. code-block:: python
      :emphasize-lines: 4

      not (first and second)
      not (False and True  )  # not logical_conjunction(False, True)
      not (False           )
      True

  - if the first input is :red:`False` and the second input is :red:`False`, :ref:`logical_nand<test_logical_nand>` returns

    .. code-block:: python
      :emphasize-lines: 4

      not (first and second)
      not (False and False ) # not logical_conjunction(False, False)
      not (False           )
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

  I add a :ref:`return statement<the return statement>` to show this

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 7-9

        # else:
        # if not (first_input and second_input):
        #     return True
        # if first_input and second_input:
        # else:
        #     return
        return logical_negation(
            logical_conjunction(first_input, second_input)
        )
        return (
            # True if
            not (first_input and second_input)
            # else False
        )

  the test is still green.

  .. code-block:: shell

    logical_nand(False, False) -> True
     └── not logical_conjunction(False , False) -> True

    logical_nand(False, True ) -> True
     └── not logical_conjunction(False , True ) -> True

    logical_nand(True , False) -> True
     └── not logical_conjunction(True  , False) -> True

    logical_nand(True , True ) -> False
     └── not logical_conjunction(True  , True ) -> False

* I remove the comments

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 5

    def logical_nand(first_input, second_input):
        return logical_negation(
            logical_conjunction(first_input, second_input)
        )
        return not (first_input and second_input)

  I can use any of these two :ref:`return statements<the return statement>`, only the first one will run in this case, because :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add logical_nand'

:ref:`Logical NAND<test_logical_nand>`

* returns :red:`False`, if the first input is :green:`True` and the second input is :green:`True`.
* returns ``not (first_input and second_input)`` which is the :ref:`Logical Negation (NOT)<test_logical_negation>` of the :ref:`Logical Conjunction (AND)<test_logical_conjunction>` of the first input and the second input, many words.
* is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Logical Conjunction (AND)<test_logical_conjunction>` which only returns :green:`True`, if the first input is :green:`True` and the second input is :green:`True`.
* is the :ref:`not<test_logical_negation>` of the :ref:`and<test_logical_conjunction>` of the first input and second input, confusing?
* is the :ref:`negation of and<test_logical_nand>`.

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
  :green:`yes`      :green:`yes`        :red:`no`
  :green:`yes`      :red:`no`           :green:`yes`
  :red:`no`         :green:`yes`        :green:`yes`
  :red:`no`         :red:`no`           :green:`yes`
  ================  ==================  ==================

* approve a transaction, if the inputs are

  - amount is larger than normal?
  - the recipient is new?

  ================  ==================  ==================
  large amount?     new recipient?      approve?
  ================  ==================  ==================
  :green:`yes`      :green:`yes`        :red:`no`
  :green:`yes`      :red:`no`           :green:`yes`
  :red:`no`         :green:`yes`        :green:`yes`
  :red:`no`         :red:`no`           :green:`yes`
  ================  ==================  ==================

* show content, if the inputs are

  - is user younger than 18?
  - is the content flagged as adult?

  ================  ==================  ==================
  less than 18?     adult content?      show content
  ================  ==================  ==================
  :green:`yes`      :green:`yes`        :red:`no`
  :green:`yes`      :red:`no`           :green:`yes`
  :red:`no`         :green:`yes`        :green:`yes`
  :red:`no`         :red:`no`           :green:`yes`
  ================  ==================  ==================

* allow 2 processes writing to the same place, if the inputs are

  - is process A writing?
  - is process B writing?

  ================  ==================  ==================
  process A write?  process B write?    allow?
  ================  ==================  ==================
  :green:`yes`      :green:`yes`        :red:`no`
  :green:`yes`      :red:`no`           :green:`yes`
  :red:`no`         :green:`yes`        :green:`yes`
  :red:`no`         :red:`no`           :green:`yes`
  ================  ==================  ==================

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

* I go back to the terminal_ where the tests are running
* I add a test for :ref:`tautology<test_tautology>` with an :ref:`assertion<what is an assertion?>` for if the first input is :green:`True` and the second input is :green:`True`, to ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 3-5

            self.assertTrue(nand(False, False))

        def test_tautology(self):
            tautology = src.truth_table.tautology
            self.assertTrue(tautology(True, True))


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.truth_table'
                    has no attribute 'tautology'

  ``truth_table.py`` does not have :ref:`tautology<test_tautology>` in it.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``tautology`` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 41
  :emphasize-lines: 8-9

  def logical_nand(first_input, second_input):
      return logical_negation(
          logical_conjunction(first_input, second_input)
      )
      return not (first_input and second_input)


  def tautology(first_input, second_input):
      return True

the test passes. :ref:`tautology<test_tautology>` returns :green:`True`, if the first input is :green:`True` and the second input is :green:`True`.

.. code-block:: python

  tautology(True , True ) -> True

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for the next case, which is if the first input is :green:`True` and the second input is :red:`False`, to :ref:`test_tautology` in ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :red:`False`   :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 4

        def test_tautology(self):
            tautology = src.truth_table.tautology
            self.assertTrue(tautology(True, True))
            self.assertTrue(tautology(True, False))


    # Exceptions seen

  the test is still green. :ref:`tautology<test_tautology>` returns

  - :green:`True`, if the first input is :green:`True` and the second input is :red:`False`
  - :green:`True`, if the first input is :green:`True` and the second input is :green:`True`
  - :green:`True`, if the first input is :green:`True`

  .. code-block:: python

    tautology(True , False) -> True
    tautology(True , True ) -> True

* I add an :ref:`assertion<what is an assertion?>` for the next case, which is if the first input is :red:`False` and the second input is :green:`True`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :green:`True`  :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 5

        def test_tautology(self):
            tautology = src.truth_table.tautology
            self.assertTrue(tautology(True, True))
            self.assertTrue(tautology(True, False))
            self.assertTrue(tautology(False, True))


    # Exceptions seen

  the test is still green. :ref:`tautology<test_tautology>` returns :green:`True`

  - if the first input is :red:`False` and the second input is :green:`True`
  - if the first input is :green:`True`

  .. code-block:: python

    tautology(False, True ) -> True
    tautology(True , False) -> True
    tautology(True , True ) -> True

* I add an :ref:`assertion<what is an assertion?>` for the last case, which is if the first input is :red:`False` and the second input is :red:`False`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :red:`False`   :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 6

        def test_tautology(self):
            tautology = src.truth_table.tautology
            self.assertTrue(tautology(True, True))
            self.assertTrue(tautology(True, False))
            self.assertTrue(tautology(False, True))
            self.assertTrue(tautology(False, False))


    # Exceptions seen

  still green, there is only one result for this operation.

  .. code-block:: python

    tautology(False, False) -> True
    tautology(False, True ) -> True
    tautology(True , False) -> True
    tautology(True , True ) -> True

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add tautology'

:ref:`Tautology<test_tautology>` always returns :green:`True`, it does not care about the inputs. It is the opposite of :ref:`contradiction<test_contradiction>` which always returns :red:`False`.

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
  :green:`yes`     :green:`yes`       :green:`yes`
  :green:`yes`     :red:`no`          :green:`yes`
  :red:`no`        :green:`yes`       :green:`yes`
  :red:`no`        :red:`no`          :green:`yes`
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

  ===============  =================  ==================
  good?            done before?       can I get better?
  ===============  =================  ==================
  :green:`yes`     :green:`yes`       :green:`yes`
  :green:`yes`     :red:`no`          :green:`yes`
  :red:`no`        :green:`yes`       :green:`yes`
  :red:`no`        :red:`no`          :green:`yes`
  ===============  =================  ==================

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
  :green:`yes`     :green:`yes`       :green:`yes`
  :green:`yes`     :red:`no`          :green:`yes`
  :red:`no`        :green:`yes`       :green:`yes`
  :red:`no`        :red:`no`          :green:`yes`
  ===============  =================  ================

----

*********************************************************************************
test_logical_disjunction
*********************************************************************************

The :ref:`truth table` for :ref:`logical_disjunction<test_logical_disjunction>` is

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
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test for :ref:`logical_disjunction<test_logical_disjunction>` with an :ref:`assertion<what is an assertion?>` for if the first input is :green:`True` and the second input is :green:`True`, to ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :green:`True`  :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 3-7

            self.assertTrue(tautology(False, False))

        def test_logical_disjunction(self):
            logical_disjunction = (
                src.truth_table.logical_disjunction
            )
            self.assertTrue(logical_disjunction(True, True))


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table'
                    has no attribute 'logical_disjunction'.
                    Did you mean: 'logical_conjunction'?

  there is no :ref:`logical_disjunction<test_logical_disjunction>` in ``truth_table.py`` in the ``src`` folder_, yet.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``logical_disjunction`` to ``truth_table.py``

.. code-block:: python
  :lineno-start: 48
  :emphasize-lines: 5-6

  def tautology(first_input, second_input):
      return True


  def logical_disjunction(first_input, second_input):
      return True

the test passes. :ref:`logical_disjunction<test_logical_disjunction>` returns :green:`True`, if the first input is :green:`True` and the second input is :green:`True`.

.. code-block:: python

  logical_disjunction(True , True ) -> True

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for the next case, which is if the first input is :green:`True` and the second input is :red:`False`, to :ref:`test_logical_disjunction` in ``test_binary.py``

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :green:`True`   :red:`False`   :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 6

        def test_logical_disjunction(self):
            logical_disjunction = (
                src.truth_table.logical_disjunction
            )
            self.assertTrue(logical_disjunction(True, True))
            self.assertTrue(logical_disjunction(True, False))


    # Exceptions seen

  the test is still green. :ref:`logical_disjunction<test_logical_disjunction>` returns

  - :green:`True`, if the first input is :green:`True` and the second input is :red:`False`
  - :green:`True`, if the first input is :green:`True` and the second input is :green:`True`
  - :green:`True`, if the first input is :green:`True`

  so far this is the same as :ref:`tautology<test_tautology>`.

  .. code-block:: python

    logical_disjunction(True , False) -> True
              tautology(True , False) -> True

    logical_disjunction(True , True ) -> True
              tautology(True , True ) -> True

* I add an :ref:`assertion<what is an assertion?>` for the next case, which is if the first input is :red:`False` and the second input is :green:`True`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :green:`True`  :green:`True`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 7

        def test_logical_disjunction(self):
            logical_disjunction = (
                src.truth_table.logical_disjunction
            )
            self.assertTrue(logical_disjunction(True, True))
            self.assertTrue(logical_disjunction(True, False))
            self.assertTrue(logical_disjunction(False, True))


    # Exceptions seen

  the test is still green. :ref:`logical_disjunction<test_logical_disjunction>` still looks like :ref:`Tautology<test_tautology>`, it returns

  - :green:`True`, if the first input is :red:`False` and the second input is :green:`True`
  - :green:`True`, if the first input is :green:`True`

  .. code-block:: python

    logical_disjunction(False, True ) -> True
              tautology(False, True ) -> True

    logical_disjunction(True , False) -> True
              tautology(True , False) -> True

    logical_disjunction(True , True ) -> True
              tautology(True , True ) -> True

* I add an :ref:`assertion<what is an assertion?>` for the fourth case, which is if the first input is :red:`False` and the second input is :red:`False`

  ==============  ============== ==============
  first input     second input   return
  ==============  ============== ==============
  :red:`False`    :red:`False`   :red:`False`
  ==============  ============== ==============

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 8

        def test_logical_disjunction(self):
            logical_disjunction = (
                src.truth_table.logical_disjunction
            )
            self.assertTrue(logical_disjunction(True, True))
            self.assertTrue(logical_disjunction(True, False))
            self.assertTrue(logical_disjunction(False, True))
            self.assertFalse(logical_disjunction(False, False))


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  because the :ref:`logical_disjunction function<test_logical_disjunction>` returns :green:`True` and this :ref:`assertion<what is an assertion?>` expects :red:`False`.

* I add :ref:`if statements` for the new case to :ref:`logical_disjunction<test_logical_disjunction>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 2-4

    def logical_disjunction(first_input, second_input):
        if first_input == False:
            if second_input == False:
                return False
        return True

  the test passes because Python_ checks if ``first_input`` is equal to :red:`False` when ``if first_input == False:`` runs

  - if ``first_input`` is NOT equal to :red:`False`, it leaves the :ref:`if statement<if statements>` and continues to run the rest of the :ref:`function<what is a function?>` - ``return True`` then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`

    .. code-block:: shell

      logical_disjunction(True , True ) -> True
      └── def logical_disjunction(first_input, second_input):
          ├── first_input  == True
          ├── second_input == True
          ├── if first_input == False:
          │       if second_input == False:
          │           return False
          └── return True

    .. code-block:: shell

      logical_disjunction(True , False) -> True
      └── def logical_disjunction(first_input, second_input):
          ├── first_input  == True
          ├── second_input == False
          ├── if first_input == False:
          │       if second_input == False:
          │           return False
          └── return True

  - if ``first_input`` is equal to :red:`False`, it goes to the next line - ``if second_input == False:``, which checks if ``second_input`` is equal to :red:`False`

    * if ``second_input`` is NOT equal to :red:`False`, it leaves the :ref:`if statement<if statements>` and continues to run the rest of the :ref:`function<what is a function?>` - ``return True`` then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`

      .. code-block:: shell

        logical_disjunction(False, True ) -> True
        └── def logical_disjunction(first_input, second_input):
            ├── first_input  == False
            ├── second_input == True
            └── if first_input == False:
            ┌───┴── if second_input == False:
            │           return False
            └── return True

    * if ``second_input`` is equal to :red:`False`, it goes to the next line - ``return False`` then leaves the :ref:`function<what is a function?>` since :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`

      .. code-block:: shell

        logical_disjunction(False, False) -> False
        └── def logical_disjunction(first_input, second_input):
            ├── first_input  == False
            ├── second_input == False
            └── if first_input == False:
                └── if second_input == False:
                    └── return False
                return True

  - it only checks the second input if the first input is :red:`False`.

* I add :ref:`the bool built-in function<how to test if something is grouped as True>`

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 2-5

    def logical_disjunction(first_input, second_input):
        # if first_input == False:
        if bool(first_input) == False:
            # if second_input == False:
            if bool(second_input) == False:
                return False
        return True

  the test is still green.

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write the :ref:`if statements` in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 3-4, 6-7

    def logical_disjunction(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        if not bool( first_input) == True:
            # if second_input == False:
            # if bool(second_input) == False:
            if not bool( second_input) == True:
                return False
        return True

  still green.

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 4-5, 8-9

    def logical_disjunction(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool( first_input) == True:
        if not bool( first_input):
            # if second_input == False:
            # if bool(second_input) == False:
            # if not bool( second_input) == True:
            if not bool( second_input):
                return False
        return True

  green.

* I remove :ref:`bool<how to test if something is grouped as True>`

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 5-6, 10-11

    def logical_disjunction(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool( first_input) == True:
        # if not bool( first_input):
        if not first_input:
            # if second_input == False:
            # if bool(second_input) == False:
            # if not bool( second_input) == True:
            # if not bool( second_input):
            if not second_input:
                return False
        return True

  still green because I can assume the following substitutions for ``if something == False:``

  - if the value of ``something`` is :red:`False`

    .. literalinclude:: ../../code/truth_table/solutions/if_not_something_false.py
      :language: python

  - if the value of ``something`` is :green:`True`

    .. literalinclude:: ../../code/truth_table/solutions/if_not_something_true.py
      :language: python

  ``if bool(something) == False`` is the same as ``if not bool( something) == True`` is the same as ``if not bool( something)`` is the same as ``if not something``.

* I use :ref:`Logical Conjunction (AND)<test_logical_conjunction>` to put the two :ref:`if statements` together

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 6, 11-12

    def logical_disjunction(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool( first_input) == True:
        # if not bool( first_input):
        # if not first_input:
            # if second_input == False:
            # if bool(second_input) == False:
            # if not bool( second_input) == True:
            # if not bool( second_input):
            # if not second_input:
        if not first_input and not second_input:
                return False
        return True

  still green, because I can put two :ref:`if statements` together when one is indented under the other

  .. code-block:: python

    if something:
        if something_else:

  can also be written as

  .. code-block:: python

    if something and something_else:

* I add an :ref:`else clause<if statements>` to make it clearer

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 13-15

    def logical_disjunction(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool( first_input) == True:
        # if not bool( first_input):
        # if not first_input:
            # if second_input == False:
            # if bool(second_input) == False:
            # if not bool( second_input) == True:
            # if not bool( second_input):
            # if not second_input:
        if not first_input and not second_input:
            return False
        else:
            return True

  green.

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to change the :ref:`else clause<if statements>` to the opposite of the :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 3-4

        if not first_input and not second_input:
            return False
        # else:
        if not (not first_input and not second_input):
            return True

  still green.

* I move the first :ref:`if statement<if statements>` below the new one

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 15-16

    def logical_disjunction(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool( first_input) == True:
        # if not bool( first_input):
        # if not first_input:
            # if second_input == False:
            # if bool(second_input) == False:
            # if not bool( second_input) == True:
            # if not bool( second_input):
            # if not second_input:
        # else:
        if not (not first_input and not second_input):
            return True
        if not first_input and not second_input:
            return False

  the test is still green.

* I change it to an :ref:`else clause<if statements>`

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 15-16

    def logical_disjunction(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool( first_input) == True:
        # if not bool( first_input):
        # if not first_input:
            # if second_input == False:
            # if bool(second_input) == False:
            # if not bool( second_input) == True:
            # if not bool( second_input):
            # if not second_input:
        # else:
        if not (not first_input and not second_input):
            return True
        # if not first_input and not second_input:
        else:
            return False

  still green.

* I add a :ref:`conditional expression (ternary operator)<conditional expressions>`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 2-3, 5-11

        # else:
        # if not (not first_input and not second_input):
        #     return True
        # if not first_input and not second_input:
        # else:
        #     return False
        return (
            True if
            not (not first_input and not second_input)
            else False
        )

  green.

  .. code-block:: python

    if not (              vs return True
        not first_input
        and
        not second_input
    ):
        return True       vs if not (
                                not first_input
                                and
                                not second_input
                             )
    else:                 vs else
        return False      vs False

* I remove ``True if`` and ``else False`` to make it simpler

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 8, 10

        # else:
        # if not (not first_input and not second_input):
        #     return True
        # if not first_input and not second_input:
        # else:
        #     return False
        return (
            # True if
            not (not first_input and not second_input)
            # else False
        )

  still green.

* :ref:`not<test_logical_negation>` happens 3 times in this statement. I "multiply" it by every symbol in the statement to try to make it simpler

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 7-8, 10-16

        # else:
        # if not (not first_input and not second_input):
        #     return True
        # if not first_input and not second_input:
        # else:
        #     return False
        # return (
            # True if
            # not (not first_input and not second_input)
            # else False
        # )
        return (
            (not not first_input)
            (not and)
            (not not second_input)
        )

  the terminal_ is my friend and shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  I cannot :ref:`negate<test_logical_negation>` :ref:`and<test_logical_conjunction>` this way.

* I add SyntaxError_ to the list of :ref:`Exceptions<errors>` seen, in ``test_binary.py``

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 8
    :emphasize-text: SyntaxError

            self.assertFalse(logical_disjunction(False, False))


    # Exceptions seen
    # AttributeError
    # TypeError
    # AssertionError
    # SyntaxError

* I change ``not and`` to ``or`` in the :ref:`logical_disjunction function<test_logical_disjunction>` in ``truth_table.py``

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 3-4

        return (
            (not not first_input)
            # (not and)
            or
            (not not second_input)
        )

  the test is green again

* I remove ``not not`` because they cancel out

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 2-3, 6-7

        return (
            # (not not first_input)
            first_input
            # (not and)
            or
            # (not not second_input)
            second_input
        )

  the test is still green. Do two :ref:`nots<test_logical_negation>` make a right?

* :ref:`logical_disjunction<test_logical_disjunction>` returns ``not ((not first_input) and (not second_input))`` which is the :ref:`Logical Negation (NOT)<test_logical_negation>`, of the :ref:`Logical Conjunction<test_logical_conjunction>` of the :ref:`Logical Negation<test_logical_negation>` of ``first_input``, and the :ref:`Logical Negation<test_logical_negation>` of ``second_input``.

  .. code-block:: python

    logical_negation(
        logical_conjunction(
            logical_negation(first_input),
            logical_negation(second_input)
        )
    )

  - ``not first_input`` is the :ref:`Logical Negation (NOT)<test_logical_negation>` of ``first_input``

    * if the first input is :green:`True`, this part of the statement is :red:`False`
    * if the first input is :red:`False`, this part of the statement is :green:`True`

  - ``not second_input`` is the :ref:`Logical Negation (NOT)<test_logical_negation>` of ``second_input``

    * if the second input is :green:`True`, this part of the statement is :red:`False`
    * if the second input is :red:`False`, this part of the statement is :green:`True`

  This means that in the four cases

  - if the first input is :green:`True` and the second input is :green:`True`, :ref:`logical_disjunction<test_logical_disjunction>` returns

    .. code-block:: python
      :emphasize-lines: 5

      not ((not first) and (not second))
      not ((not True ) and (not True  ))
      not (False       and False       )
      not  False       # not logical_conjunction(False, False)
      True

  - if the first input is :green:`True` and the second input is :red:`False`, :ref:`logical_disjunction<test_logical_disjunction>` returns

    .. code-block:: python
      :emphasize-lines: 5

      not ((not first) and (not second))
      not ((not True ) and (not False ))
      not (False       and True        )
      not  False       # not logical_conjunction(False, True)
      True

  - if the first input is :red:`False` and the second input is :green:`True`, :ref:`logical_disjunction<test_logical_disjunction>` returns

    .. code-block:: python
      :emphasize-lines: 5

      not ((not first) and (not second))
      not ((not False) and (not True  ))
      not (True        and False       )
      not  False       # not logical_conjunction(True, False)
      True

  - if the first input is :red:`False` and the second input is :red:`False`, :ref:`logical_disjunction<test_logical_disjunction>` returns

    .. code-block:: python
      :emphasize-lines: 5

      not ((not first) and (not second))
      not ((not False) and (not False ))
      not (True        and True        )
      not  True        # not logical_conjunction(True, True)
      False

  ==============  =============== ===============  ================ ==============================  ===================================
  first           second          not first        not second       ((not first) and (not second))  not ((not first) and (not second))
  ==============  =============== ===============  ================ ==============================  ===================================
  :green:`True`   :green:`True`   :red:`False`     :red:`False`     :red:`False`                    :green:`True`
  :green:`True`   :red:`False`    :red:`False`     :green:`True`    :red:`False`                    :green:`True`
  :red:`False`    :green:`True`   :green:`True`    :red:`False`     :red:`False`                    :green:`True`
  :red:`False`    :red:`False`    :green:`True`    :green:`True`    :green:`True`                   :red:`False`
  ==============  =============== ===============  ================ ==============================  ===================================

  I add a :ref:`return statement<the return statement>` to show this

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 23-28

    def logical_disjunction(first_input, second_input):
        # if first_input == False:
        # if bool(first_input) == False:
        # if not bool( first_input) == True:
        # if not bool( first_input):
        # if not first_input:
            # if second_input == False:
            # if bool(second_input) == False:
            # if not bool( second_input) == True:
            # if not bool( second_input):
            # if not second_input:
        # else:
        # if not (not first_input and not second_input):
        #     return True
        # if not first_input and not second_input:
        # else:
        #     return False
        # return (
            # True if
            # not (not first_input and not second_input)
            # else False
        # )
        return logical_negation(
            logical_conjunction(
                logical_negation(first_input),
                logical_negation(second_input)
            )
        )
        return (
            # (not not first_input)
            first_input
            # (not and)
            or
            # (not not second_input)
            second_input
        )

  still green.

  .. code-block:: shell

    logical_disjunction(False, False) -> False
    └── not logical_conjunction(True, True)
        not True  -> False

    logical_disjunction(False, True ) -> True
    └── not logical_conjunction(True , False)
        not False -> True

    logical_disjunction(True , False) -> True
    └── not logical_conjunction(False, True )
        not False -> True

    logical_disjunction(True , True ) -> True
    └── not logical_conjunction(False, False)
        not False -> True

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 8

    def logical_disjunction(first_input, second_input):
        return logical_negation(
            logical_conjunction(
                logical_negation(first_input),
                logical_negation(second_input)
            )
        )
        return first_input or second_input

  I can use any of these two :ref:`return statements<the return statement>`, only the first one will run in this case, because :ref:`the return statement is the last thing to run in a function<test_what_happens_after_functions_return>`.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add logical_disjunction'

:ref:`Logical Disjunction<test_logical_disjunction>` also known as "OR_" returns

* ``first_input or second_input``.
* :red:`False`, if the first input is :red:`False` and the second input is :red:`False`.
* is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Logical NOR<test_logical_nor>` which returns :green:`True` only if ``first_input`` is :red:`False` and ``second_input`` is :red:`False`

----

=================================================================================
examples of Logical Disjunction
=================================================================================

----

* the system works, if the inputs are

  - is the main system running?
  - is the backup system running?

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
  - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`contradiction<test_contradiction>` which always returns :red:`False`

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

Three :ref:`binary operations<truth table: binary operations>` were written with :ref:`AND<test_logical_conjunction>`, three with :ref:`NOT<test_logical_negation>` and one was written with :ref:`OR<test_logical_disjunction>`.

=============================================== ============== ============== ============= ============= ==============================================================
return                                          :green:`True`, :green:`True`, :red:`False`, :red:`False`, name of operation
                                                :green:`True`  :red:`False`   :green:`True` :red:`False`
=============================================== ============== ============== ============= ============= ==============================================================
False                                           :red:`False`   :red:`False`   :red:`False`  :red:`False`  :ref:`contradiction<test_contradiction>`
first and second                                :green:`True`  :red:`False`   :red:`False`  :red:`False`  :ref:`logical_conjunction<test_logical_conjunction>`
second                                          :green:`True`  :red:`False`   :green:`True` :red:`False`  :ref:`project_second<test_project_second>`
(not first) and second                          :red:`False`   :red:`False`   :green:`True` :red:`False`  :ref:`converse_non_implication<test_converse_non_implication>`
not first                                       :red:`False`   :red:`False`   :green:`True` :green:`True` :ref:`negate_first<test_negate_first>`
not (first and second)                          :red:`False`   :green:`True`  :green:`True` :green:`True` :ref:`logical_nand<test_logical_nand>`
True                                            :green:`True`  :green:`True`  :green:`True` :green:`True` :ref:`tautology<test_tautology>`
first or second                                 :green:`True`  :green:`True`  :green:`True` :red:`False`  :ref:`logical_disjunction<test_logical_disjunction>`
=============================================== ============== ============== ============= ============= ==============================================================

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

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too.

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->