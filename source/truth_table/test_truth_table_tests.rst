.. meta::
  :description: Rebuild a complete boolean logic library from scratch in this ultimate Python TDD challenge. Follow a step-by-step guide to resolving 20 failing tests while learning to debug NameError, TypeError, and AttributeError. Master the full lifecycle of software engineering—from a blank file to passing tests—and refactor complex logic gates like XOR, NAND, and Implication into clean, idiomatic Python.
  :keywords: Jacob Itegboje, Python TDD challenge, test driven development from scratch, rebuilding truth tables, debugging Python errors tutorial, how to fix TypeError in Python, AttributeError module attribute, logical negation implementation, NAND NOR XOR Python code, TDD Red Green Refactor cycle, Python boolean logic library, programming logic final exam, refactoring nested if-statements, De Morgan's Law in practice, Python unittest examples, binary operations tutorial, software engineering best practices, logic gate implementation guide, truth table test suite, coding from failing tests

.. include:: ../links.rst

.. _test_truth_table_tests:

#################################################################################
truth table: test_truth_table_tests
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/DtGE6WqRZgo?si=08uXK8QMZaG06XWp" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-if-cross-origin" allowfullscreen></iframe>

----

I want to write a program_ that makes the tests in ``test_truth_table.py`` pass without looking at them

*********************************************************************************
requirements
*********************************************************************************

* :ref:`Nullary & Unary Operations<truth table: Nullary and Unary Operations>`
* :ref:`Binary Operations<truth table: Binary Operations>`

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

    rootdir: .../pumping_python/truth_table
    configfile: pyproject.toml
    collected 20 items

    tests/test_binary.py ....................                     [ 80%]
    tests/test_nullary_unary.py ....                              [100%]

    ======================== 20 passed in G.HIs ========================

----

*********************************************************************************
:red:`RED`: make it fail
*********************************************************************************

* I open ``truth_table.py`` from the ``src`` folder_
* I delete everything in ``truth_table.py``, the terminal_ is my friend, and shows 20 failures, I start with the last one

  .. code-block:: shell

    AttributeError: module 'src.truth_table'
                    has no attribute 'logical_negation'

  because ...

  Can you make the tests pass without looking at how I solve it below? You can come back to compare solutions when you are done.

----

*********************************************************************************
:green:`GREEN`: make it pass
*********************************************************************************

* I add the name to ``truth_table.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    logical_negation

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'logical_negation' is not defined

* I point it to :ref:`None<what is None?>` to define it

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    logical_negation = None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  because :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`.

* I make it a :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-3

    # logical_negation
    def logical_negation():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: logical_negation() takes
               0 positional arguments but 1 was given

* I add a name in parentheses

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    # logical_negation
    # def logical_negation():
    def logical_negation(something):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None is not true

  the :ref:`assertion<what is an assertion?>` expects :green:`True`.

* I change :ref:`None<what is None?>` in the `return statement`_ to give the test what it wants

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    # logical_negation
    # def logical_negation():
    def logical_negation(something):
        # return None
        return True

  the terminal shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  the :ref:`assertion<what is an assertion?>` expects :red:`False` and the :ref:`function<what is a function?>` returns :green:`True`.

* I change the `return statement`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    # logical_negation
    # def logical_negation():
    def logical_negation(something):
        # return None
        # return True
        return False

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

* I change the `return statement`_ to see the difference between the input and what the :ref:`assertion<what is an assertion?>` expects, remember :ref:`the identity_function?<test_identity_function>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    # logical_negation
    # def logical_negation():
    def logical_negation(something):
        # return None
        # return True
        # return False
        return something

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  - the :ref:`assertion<what is an assertion?>` expects the :ref:`opposite<test_logical_negation>` of the input
  - the :ref:`function<what is a function?>` returned

    * :red:`False` when the :ref:`assertion<what is an assertion?>` expected :green:`True`
    * :green:`True` when the :ref:`assertion<what is an assertion?>` expected :red:`False`
    * :ref:`None<what is None?>` when the :ref:`assertion<what is an assertion?>` expected :green:`True`

* I use :ref:`not<test_logical_negation>` in the `return statement`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-8

    # logical_negation
    # def logical_negation():
    def logical_negation(something):
        # return None
        # return True
        # return False
        # return something
        return not something

  the terminal_ shows ``19 failed, 1 passed``, progress! It also shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.truth_table'
                    has no attribute 'logical_identity'

* I add a :ref:`function<what is a function?>` for it

  .. code-block:: python
    :linenos:
    :emphasize-lines: 11-12

    # logical_negation
    # def logical_negation():
    def logical_negation(something):
        # return None
        # return True
        # return False
        # return something
        return not something


    def logical_identity():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: logical_identity() takes
               0 positional arguments but 1 was given

* I add a name in parentheses

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 2-3

    # def logical_identity():
    def logical_identity(something):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None is not true

* I change the `return statement`_ for :ref:`logical_identity<test_logical_identity>` to give the test what it wants

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3-4

    # def logical_identity():
    def logical_identity(something):
        # return None
        return True

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  the :ref:`assertion<what is an assertion?>` expects :red:`False` and the :ref:`function<what is a function?>` returns :green:`True`.

* I change the `return statement`_

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 4-5

    # def logical_identity():
    def logical_identity(something):
        # return None
        # return True
        return False

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  the :ref:`function<what is a function?>` returned

  - :red:`False` when the :ref:`assertion<what is an assertion?>` expected :green:`True`
  - :green:`True` when the :ref:`assertion<what is an assertion?>` expected :red:`False`
  - :ref:`None<what is None?>` when the :ref:`assertion<what is an assertion?>` expected :green:`True`

* I change the `return statement`_ to see the difference between the input and what the :ref:`assertion<what is an assertion?>` expects

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 5-6

    # def logical_identity():
    def logical_identity(something):
        # return None
        # return True
        # return False
        return something

  the terminal_ shows ``18 failed, 2 passed``, more progress! It also shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.truth_table'
                    has no attribute 'logical_true'

* I add the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 9-10

    # def logical_identity():
    def logical_identity(something):
        # return None
        # return True
        # return False
        return something


    def logical_true():
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None is not true

* I change the `return statement`_ for :ref:`logical_true<test_logical_true>` to give the test what it wants

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 2-3

    def logical_true():
        # return None
        return True

  17 failed, 3 passed. That was simple. the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table'
                    has no attribute 'logical_false'.
                    Did you mean: 'logical_true'?

* I add the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 6-7

    def logical_true():
        # return None
        return True


    def logical_false():
        return None

  the terminal_ shows ``16 failed, 4 passed``, simple again. I am getting it. The terminal_ also shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.truth_table'
                    has no attribute 'tautology'

* I add the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 5-6

    def logical_false():
        return None


    def tautology():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: tautology() takes
               0 positional arguments but 2 were given

* I add two names in parentheses for the :ref:`function<what is a function?>` to take input arguments

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 1-2

    # def tautology():
    def tautology(first, second):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None is not true

* I change :ref:`None<what is None?>` to :ref:`True<test_what_is_true>` in the `return statement`_

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 3-4

    # def tautology():
    def tautology(first, second):
        # return None
        return True

  the terminal shows ``15 failed, 5 passed``, Yes! It also shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table'
                    has no attribute 'project_second'

* I add the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 7-8

    # def tautology():
    def tautology(first, second):
        # return None
        return True


    def project_second():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: project_second() takes
               0 positional arguments but 2 were given

* I add two names in parentheses for the :ref:`function<what is a function?>` to take input arguments

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 1-2

    # def project_second():
    def project_second(first, second):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None is not true

* I change the `return statement`_ to give the test what it wants

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 3-4

    # def project_second():
    def project_second(first, second):
        # return None
        return True

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  the :ref:`assertion<what is an assertion?>` expects :red:`False` and the :ref:`function<what is a function?>` returns :green:`True`.

* I change the `return statement`_

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 4-5

    # def project_second():
    def project_second(first, second):
        # return None
        # return True
        return False

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  the :ref:`function<what is a function?>` returned

  - :red:`False` when the :ref:`assertion<what is an assertion?>` expected :green:`True`
  - :green:`True` when the :ref:`assertion<what is an assertion?>` expected :red:`False`
  - :ref:`None<what is None?>` when the :ref:`assertion<what is an assertion?>` expected :green:`True`

* I change the `return statement`_ to see the difference between the input and what the :ref:`assertion<what is an assertion?>` expects

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 5-6

    # def project_second():
    def project_second(first, second):
        # return None
        # return True
        # return False
        return first, second

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, False) is not false

  ``second`` is :red:`False` and is equal to the expectation of the :ref:`assertion<what is an assertion?>`.

* I remove ``first`` from the `return statement`_  since ``second`` is :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 6-7

    # def project_second():
    def project_second(first, second):
        # return None
        # return True
        # return False
        # return first, second
        return second

  the terminal_ shows ``14 failed, 6 passed``, and :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table'
                    has no attribute 'project_first'

* I add a :ref:`function<what is a function?>` for it

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 10-11

    # def project_second():
    def project_second(first, second):
        # return None
        # return True
        # return False
        # return first, second
        return second


    def project_first():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: project_first() takes
               0 positional arguments but 2 were given

  okay, I have seen this before.

* I add 2 names in the parentheses

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 1-2

    # def project_first():
    def project_first(first, second):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None is not true

* I change the `return statement`_ to give the test what it wants

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 3-4

    # def project_first():
    def project_first(first, second):
        # return None
        return True

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  the :ref:`assertion<what is an assertion?>` expects :red:`False` and the :ref:`function<what is a function?>` returns :green:`True`.

* I change the `return statement`_

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 4-5

    # def project_first():
    def project_first(first, second):
        # return None
        # return True
        return False

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  the :ref:`function<what is a function?>` returned

  - :red:`False` when the :ref:`assertion<what is an assertion?>` expected :green:`True`
  - :green:`True` when the :ref:`assertion<what is an assertion?>` expected :red:`False`
  - :ref:`None<what is None?>` when the :ref:`assertion<what is an assertion?>` expected :green:`True`

* I change the `return statement`_ to see the difference between the input and what the :ref:`assertion<what is an assertion?>` expects

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 5-6

    # def project_first():
    def project_first(first, second):
        # return None
        # return True
        # return False
        return first, second

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (False, True) is not false

  ``second`` is :red:`True` and is equal to the expectation of the :ref:`assertion<what is an assertion?>`.

* I remove ``second`` from the `return statement`_ since ``first`` is :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 6-7

    # def project_first():
    def project_first(first, second):
        # return None
        # return True
        # return False
        # return first, second
        return first

  the terminal_ shows ``13 failed, 7 passed``, and :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table'
                    has no attribute 'negate_second'

* I add a :ref:`function<what is a function?>` for :ref:`negate_second<test_negate_second>` with a `return statement`_ to see the difference between the input and what the :ref:`assertion<what is an assertion?>` expects

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 10-11

    # def project_first():
    def project_first(first, second):
        # return None
        # return True
        # return False
        # return first, second
        return first


    def negate_second(first, second):
        return first, second

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, True) is not false

* I add an :ref:`if statement<if statements>` to :ref:`negate_second<test_negate_second>` since ``first`` and ``second`` are both not :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 2

    def negate_second(first, second):
        if (first, second) == (True, True): return False
        return first, second

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (False, True) is not false

* I add another :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 3

    def negate_second(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (False, True): return False
        return first, second

  the terminal_ is my friend, and shows ``12 failed, 8 passed`` with :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.truth_table'
                    has no attribute 'negate_first'

* I add a :ref:`function<what is a function?>` for it with a `return statement`_ to see the difference between the input and what the :ref:`assertion<what is an assertion?>` expects

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 7-8

    def negate_second(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (False, True): return False
        return first, second


    def negate_first(first, second):
        return first, second

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, True)

* I add an :ref:`if statement<if statements>` since ``first`` and ``second`` are both not :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 2

    def negate_first(first, second):
        if (first, second) == (True, True): return False
        return first, second

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, False) is not false

* I add another :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 3

    def negate_first(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        return first, second

  the terminal_ is my friend, and shows ``11 failed, 9 passed`` with :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.truth_table'
                    has no attribute 'material_non_implication'

* I add a :ref:`function<what is a function?>` for :ref:`material_non_implication<test_material_non_implication>` with a `return statement`_ to see the difference between the input and what the :ref:`assertion<what is an assertion?>` expects

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 7-8

    def negate_first(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        return first, second


    def material_non_implication(first, second):
        return first, second

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, True) is not false

* I add an :ref:`if statement<if statements>` since ``first`` and ``second`` are both not :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 2

    def material_non_implication(first, second):
        if (first, second) == (True, True): return False
        return first, second

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (False, True) is not false

* I add another :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 3

    def material_non_implication(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (False, True): return False
        return first, second

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (False, False) is not false

* I add an :ref:`if statement<if statements>` for it

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 4

    def material_non_implication(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (False, True): return False
        if (first, second) == (False, False): return False
        return first, second

  the terminal_ is my friend, and shows ``10 failed, 10 passed`` with :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.truth_table'
                    has no attribute 'material_implication'

* I add a :ref:`function<what is a function?>` for :ref:`material_implication<test_material_implication>` with a `return statement`_ to see the difference between the input and what the :ref:`assertion<what is an assertion?>` expects

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 8-9

    def material_non_implication(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (False, True): return False
        if (first, second) == (False, False): return False
        return first, second


    def material_implication(first, second):
        return first, second

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, False) is not false

* I add an :ref:`if statement<if statements>` for it

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 2

    def material_implication(first, second):
        if (first, second) == (True, False): return False
        return first, second

  the terminal_ is my friend, and shows ``9 failed, 11 passed`` with :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.truth_table'
                    has no attribute 'logical_nor'

* I add a :ref:`function<what is a function?>` for :ref:`logical_nor<test_logical_nor>`

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 6-7

    def material_implication(first, second):
        if (first, second) == (True, False): return False
        return first, second


    def logical_nor(first, second):
        return first, second

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, True) is not false

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines:  2

    def logical_nor(first, second):
        if (first, second) == (True, True): return False
        return first, second

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, False) is not false

* I add another :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 3

    def logical_nor(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        return first, second

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (False, True) is not false

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 4

    def logical_nor(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        if (first, second) == (False, True): return False
        return first, second

  the terminal_ is my friend, and shows ``8 failed, 12 passed`` with :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table'
                    has no attribute 'logical_nand'.
                    Did you mean: 'logical_nor'?

* I add a :ref:`function<what is a function?>` for :ref:`logical_nand<test_logical_nand>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 8-9

    def logical_nor(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        if (first, second) == (False, True): return False
        return first, second


    def logical_nand(first, second):
        return first, second

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, True) is not false

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 2

    def logical_nand(first, second):
        if (first, second) == (True, True): return False
        return first, second

  the terminal_ is my friend, and shows ``7 failed, 13 passed`` with :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table'
                    has no attribute 'logical_equality'.
                    Did you mean: 'logical_identity'?

* I add the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 6-7

    def logical_nand(first, second):
        if (first, second) == (True, True): return False
        return first, second


    def logical_equality(first, second):
        return first, second

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, False) is not false

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 2

    def logical_equality(first, second):
        if (first, second) == (True, False): return False
        return first, second

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (False, True) is not false

* I add another :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 3

    def logical_equality(first, second):
        if (first, second) == (True, False): return False
        if (first, second) == (False, True): return False
        return first, second

  the terminal_ is my friend, and shows ``6 failed, 14 passed`` with :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.truth_table'
                    has no attribute 'logical_disjunction'

* I add a :ref:`function<what is a function?>` for :ref:`logical_disjunction<test_logical_disjunction>`

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 7-8

    def logical_equality(first, second):
        if (first, second) == (True, False): return False
        if (first, second) == (False, True): return False
        return first, second


    def logical_disjunction(first, second):
        return first, second

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (False, False) is not false

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 2

    def logical_disjunction(first, second):
        if (first, second) == (False, False): return False
        return first, second

  the terminal_ is my friend, and shows ``5 failed, 15 passed`` with :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table'
                    has no attribute 'logical_conjunction'.
                    Did you mean: 'logical_disjunction'?

* I add a :ref:`function<what is a function?>` for :ref:`logical_conjunction<test_logical_conjunction>`

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 6-7

    def logical_disjunction(first, second):
        if (first, second) == (False, False): return False
        return first, second


    def logical_conjunction(first, second):
        return first, second

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, False) is not false

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 99
    :emphasize-lines: 2

    def logical_conjunction(first, second):
        if (first, second) == (True, False): return False
        return first, second

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (False, True) is not false

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 99
    :emphasize-lines: 3

    def logical_conjunction(first, second):
        if (first, second) == (True, False): return False
        if (first, second) == (False, True): return False
        return first, second

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (False, False) is not false

* I add another :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 99
    :emphasize-lines: 4

    def logical_conjunction(first, second):
        if (first, second) == (True, False): return False
        if (first, second) == (False, True): return False
        if (first, second) == (False, False): return False
        return first, second

  the terminal_ is my friend, and shows ``4 failed, 16 passed`` with :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.truth_table'
                    has no attribute 'exclusive_disjunction'

* I add a :ref:`function<what is a function?>` for :ref:`exclusive_disjunction<test_exclusive_disjunction>`

  .. code-block:: python
    :lineno-start: 99
    :emphasize-lines: 8-9

    def logical_conjunction(first, second):
        if (first, second) == (True, False): return False
        if (first, second) == (False, True): return False
        if (first, second) == (False, False): return False
        return first, second


    def exclusive_disjunction(first, second):
        return first, second

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, True) is not false

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 2

    def exclusive_disjunction(first, second):
        if (first, second) == (True, True): return False
        return first, second

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (False, False) is not false

* I add another :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 3

    def exclusive_disjunction(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (False, False): return False
        return first, second

  the terminal_ is my friend, and shows ``3 failed, 17 passed`` with :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table'
                    has no attribute 'converse_non_implication'.
                    Did you mean: 'material_non_implication'?

* I add :ref:`converse_non_implication<test_converse_non_implication>`

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 7-8

    def exclusive_disjunction(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (False, False): return False
        return first, second


    def converse_non_implication(first, second):
        return first, second

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, True) is not false

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 112
    :emphasize-lines: 2

    def converse_non_implication(first, second):
        if (first, second) == (True, True): return False
        return first, second

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, False) is not false

* I add another :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 112
    :emphasize-lines: 3

    def converse_non_implication(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        return first, second

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (False, False) is not false

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 112
    :emphasize-lines: 4

    def converse_non_implication(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        if (first, second) == (False, False): return False
        return first, second

  the terminal_ is my friend, and shows ``2 passed, 18 failed`` for :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table'
                    has no attribute 'converse_implication'.
                    Did you mean: 'converse_non_implication'?

* I add :ref:`converse_implication<test_converse_implication>`

  .. code-block:: python
    :lineno-start: 112
    :emphasize-lines: 8-9

    def converse_non_implication(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        if (first, second) == (False, False): return False
        return first, second


    def converse_implication(first, second):
        return first, second

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (False, True) is not false

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 119
    :emphasize-lines: 2

    def converse_implication(first, second):
        if (first, second) == (False, True): return False
        return first, second

  the terminal_ is my friend, and shows ``1 failed, 19 passed`` with :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.truth_table'
                    has no attribute 'contradiction'

* I add :ref:`contradiction<test_contradiction>`

  .. code-block:: python
    :lineno-start: 119
    :emphasize-lines: 6-7

    def converse_implication(first, second):
        if (first, second) == (False, True): return False
        return first, second


    def contradiction(first, second):
        return first, second

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, True) is not false

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 124
    :emphasize-lines: 2

    def contradiction(first, second):
        if (first, second) == (True, True): return False
        return first, second

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, False) is not false

* I add another :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 124
    :emphasize-lines: 3

    def contradiction(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        return first, second

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (False, True) is not false

* I add another :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 124
    :emphasize-lines: 4

    def contradiction(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        if (first, second) == (False, True): return False
        return first, second

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (False, False) is not false

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 124
    :emphasize-lines: 5

    def contradiction(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        if (first, second) == (False, True): return False
        if (first, second) == (False, False): return False
        return first, second

  the terminal_ is my friend, and shows

  .. code-block:: shell

    ======================== 20 passed in G.HIs ========================

All the tests are passing and the world is a better place than when I started! I am going home.

----

*********************************************************************************
:yellow:`REFACTOR`: make it better
*********************************************************************************

Wait, there is more... Since all the tests are passing, I can play with the :ref:`functions<what is a function?>` I have to make them simpler and understand why my solutions work.

* :ref:`contradiction<test_contradiction>`  returns :red:`False` in 4 cases, with 2 inputs there are only 4 cases. I add a `return statement`_

  .. code-block:: python
    :lineno-start: 124
    :emphasize-lines: 2-7

    def contradiction(first, second):
        # if (first, second) == (True, True): return False
        # if (first, second) == (True, False): return False
        # if (first, second) == (False, True): return False
        # if (first, second) == (False, False): return False
        # return first, second
        return False

  the test is still green.

* I remove the commented lines from :ref:`contradiction<test_contradiction>`

  .. code-block:: python
    :lineno-start: 124

    def contradiction(first, second):
        return False

----

* :ref:`converse_implication<test_converse_implication>` returns :red:`False` in only one case. I write out the :ref:`if statement<if statements>` for that case, to make it clearer

  .. code-block:: python
    :lineno-start: 119
    :emphasize-lines: 2-3

    def converse_implication(first, second):
        # if (first, second) == (False, True): return False
        if first == False and second == True:
            return False
        return first, second

  still green.

* I change the statement with :ref:`not<test_logical_negation>` and :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 119
    :emphasize-lines: 3-4

    def converse_implication(first, second):
        # if (first, second) == (False, True): return False
        # if first == False and second == True:
        if not first == True and second == True:
            return False
        return first, second

  green.

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 119
    :emphasize-lines: 4-5

    def converse_implication(first, second):
        # if (first, second) == (False, True): return False
        # if first == False and second == True:
        # if not first == True and second == True:
        if not first and second:
            return False
        return first, second

  still green.

* I use a `return statement`_ because ``if something: return False`` can be written as ``return not (something)``

  .. code-block:: python
    :lineno-start: 119
    :emphasize-lines: 5-8

    def converse_implication(first, second):
        # if (first, second) == (False, True): return False
        # if first == False and second == True:
        # if not first == True and second == True:
        # if not first and second:
        #     return False
        # return first, second
        return not (not first and second)

  the test is still green.

* I "multiply :ref:`not<test_logical_negation>`" by the things in the parentheses

  .. code-block:: python
    :lineno-start: 119
    :emphasize-lines: 8-9

    def converse_implication(first, second):
        # if (first, second) == (False, True): return False
        # if first == False and second == True:
        # if not first == True and second == True:
        # if not first and second:
        #     return False
        # return first, second
        # return not (not first and second)
        return (not not first) (not and) (not second)

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

* I change ``not and`` to :ref:`or<test_logical_disjunction>`

  .. code-block:: python
    :lineno-start: 119
    :emphasize-lines: 9-10

    def converse_implication(first, second):
        # if (first, second) == (False, True): return False
        # if first == False and second == True:
        # if not first == True and second == True:
        # if not first and second:
        #     return False
        # return first, second
        # return not (not first and second)
        # return (not not first) (not and) (not second)
        return (not not first) or (not second)

  the test is green again.

* I remove ``not not`` because two :ref:`nots<test_logical_negation>` make a right?

  .. code-block:: python
    :lineno-start: 119
    :emphasize-lines: 10-11

    def converse_implication(first, second):
        # if (first, second) == (False, True): return False
        # if first == False and second == True:
        # if not first == True and second == True:
        # if not first and second:
        #     return False
        # return first, second
        # return not (not first and second)
        # return (not not first) (not and) (not second)
        # return (not not first) or (not second)
        return first or not second

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 119

    def converse_implication(first, second):
        return first or not second


    def contradiction(first, second):
        return False

-----

* I add an :ref:`if statement<if statements>` for the only case that returns :green:`True` in :ref:`converse_non_implication<test_converse_non_implication>`

  .. code-block:: python
    :lineno-start: 112
    :emphasize-lines: 2-9

    def converse_non_implication(first, second):
        # if (first, second) == (True, True): return False
        # if (first, second) == (True, False): return False
        # if (first, second) == (False, False): return False
        # return first, second
        if first == False and second == True:
            return True
        else:
            return False

  the test is still green.

* I change ``if first == False`` to terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 112
    :emphasize-lines: 6-7

    def converse_non_implication(first, second):
        # if (first, second) == (True, True): return False
        # if (first, second) == (True, False): return False
        # if (first, second) == (False, False): return False
        # return first, second
        # if first == False and second == True:
        if not first == True and second == True:
            return True
        else:
            return False

  green.

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 112
    :emphasize-lines: 7-8

    def converse_non_implication(first, second):
        # if (first, second) == (True, True): return False
        # if (first, second) == (True, False): return False
        # if (first, second) == (False, False): return False
        # return first, second
        # if first == False and second == True:
        # if not first == True and second == True:
        if not first and second:
            return True
        else:
            return False

  still green.

* I add a `return statement`_ because ``if something: return True`` can be written as ``return something`` since ``something`` is grouped as :green:`True`

  .. code-block:: python
    :lineno-start: 112
    :emphasize-lines: 8-12

    def converse_non_implication(first, second):
        # if (first, second) == (True, True): return False
        # if (first, second) == (True, False): return False
        # if (first, second) == (False, False): return False
        # return first, second
        # if first == False and second == True:
        # if not first == True and second == True:
        # if not first and second:
        #     return True
        # else:
        #     return False
        return not first and second

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 112

    def converse_non_implication(first, second):
        return not first and second


    def converse_implication(first, second):
        return first or not second


    def contradiction(first, second):
        return False

----

* I make the :ref:`if statements` in :ref:`exclusive_disjunction<test_exclusive_disjunction>` simpler

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 2-9

    def exclusive_disjunction(first, second):
        # if (first, second) == (True, True): return False
        # if (first, second) == (False, False): return False
        # return first, second
        if first == True and second == True:
            return False
        if first == False and second == False:
            return False
        return True

  the test is still green.

* I change the new second :ref:`if statement<if statements>` with :ref:`not<test_logical_negation>` and :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 7-8

    def exclusive_disjunction(first, second):
        # if (first, second) == (True, True): return False
        # if (first, second) == (False, False): return False
        # return first, second
        if first == True and second == True:
            return False
        # if first == False and second == False:
        if not first == True and not second == True:
            return False
        return True

  still green.

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 5-6, 9-10

    def exclusive_disjunction(first, second):
        # if (first, second) == (True, True): return False
        # if (first, second) == (False, False): return False
        # return first, second
        # if first == True and second == True:
        if first and second:
            return False
        # if first == False and second == False:
        # if not first == True and not second == True:
        if not first and not second:
            return False
        return True

  green.

* I write everything in the second :ref:`if statement<if statements>` with :ref:`not<test_logical_negation>` because it happens two times in the line, I might as well make it three

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 10-11

    def exclusive_disjunction(first, second):
        # if (first, second) == (True, True): return False
        # if (first, second) == (False, False): return False
        # return first, second
        # if first == True and second == True:
        if first and second:
            return False
        # if first == False and second == False:
        # if not first == True and not second == True:
        # if not first and not second:
        if (not first) (not or) (not second):
            return False
        return True

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

* I factor out the :ref:`nots<test_logical_negation>`

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 11-12

    def exclusive_disjunction(first, second):
        # if (first, second) == (True, True): return False
        # if (first, second) == (False, False): return False
        # return first, second
        # if first == True and second == True:
        if first and second:
            return False
        # if first == False and second == False:
        # if not first == True and not second == True:
        # if not first and not second:
        # if (not first) (not or) (not second):
        if not (first or second):
            return False
        return True

  the test is green .

* I put the two :ref:`if statements` together as one

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 6-7, 12-17

    def exclusive_disjunction(first, second):
        # if (first, second) == (True, True): return False
        # if (first, second) == (False, False): return False
        # return first, second
        # if first == True and second == True:
        # if first and second:
        #     return False
        # if first == False and second == False:
        # if not first == True and not second == True:
        # if not first and not second:
        # if (not first) (not or) (not second):
        # if not (first or second):
        if (
            (first and second)
            or
            (not (first or second))
        ):
            return False
        return True

  the test is still green.

* I add a `return statement`_ because ``if something: return False`` can be written as ``return not (something)``

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 13-24

    def exclusive_disjunction(first, second):
        # if (first, second) == (True, True): return False
        # if (first, second) == (False, False): return False
        # return first, second
        # if first == True and second == True:
        # if first and second:
        #     return False
        # if first == False and second == False:
        # if not first == True and not second == True:
        # if not first and not second:
        # if (not first) (not or) (not second):
        # if not (first or second):
        # if (
        #     (first and second)
        #     or
        #     (not (first or second))
        # ):
        #     return False
        # return True
        return not (
            (first and second)
            or
            (not (first or second))
        )

  still green.

* I "multiply" :ref:`not<test_logical_negation>` by everything in the parentheses since it happens two times in the line

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 20-29

    def exclusive_disjunction(first, second):
        # if (first, second) == (True, True): return False
        # if (first, second) == (False, False): return False
        # return first, second
        # if first == True and second == True:
        # if first and second:
        #     return False
        # if first == False and second == False:
        # if not first == True and not second == True:
        # if not first and not second:
        # if (not first) (not or) (not second):
        # if not (first or second):
        # if (
        #     (first and second)
        #     or
        #     (not (first or second))
        # ):
        #     return False
        # return True
        # return not (
        #     (first and second)
        #     or
        #     (not (first or second))
        # )
        return (
            (not (first and second))
            (not or)
            (not (not (first or second)))
        )

  the terminal shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

* I change ``not or`` to :ref:`and<test_logical_conjunction>`

  .. code-block:: python
    :lineno-start: 130
    :emphasize-lines: 3-4

        return (
            (not (first and second))
            # (not or)
            and
            (not (not (first or second)))
        )

  the test is green again.

* I remove ``not not`` because "the negation of a negation is ..."

  .. code-block:: python
    :lineno-start: 130
    :emphasize-lines: 5-6

        return (
            (not (first and second))
            # (not or)
            and
            # (not (not (first or second)))
            (first or second)
        )

  green.

* I remove the commented lines from :ref:`exclusive_disjunction<test_exclusive_disjunction>`

  .. code-block:: python
    :lineno-start: 106

    def exclusive_disjunction(first, second):
        return (not (first and second)) and (first or second)


    def converse_non_implication(first, second):
        return not first and second


    def converse_implication(first, second):
        return first or not second


    def contradiction(first, second):
        return False

----

* :ref:`logical_conjunction<test_logical_conjunction>` has only one case that returns :green:`True`. I add an :ref:`if statement<if statements>` for it

  .. code-block:: python
    :lineno-start: 99
    :emphasize-lines: 2-9

    def logical_conjunction(first, second):
        # if (first, second) == (True, False): return False
        # if (first, second) == (False, True): return False
        # if (first, second) == (False, False): return False
        # return first, second
        if first == True and second == True:
            return True
        else:
            return False

  the test is still green.

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 99
    :emphasize-lines: 6-7

    def logical_conjunction(first, second):
        # if (first, second) == (True, False): return False
        # if (first, second) == (False, True): return False
        # if (first, second) == (False, False): return False
        # return first, second
        # if first == True and second == True:
        if first and second:
            return True
        else:
            return False

  still green.

* I use a `return statement`_ because ``if something: return True`` can be written as ``return something`` since ``something`` is grouped as :green:`True`

  .. code-block:: python
    :lineno-start: 99
    :emphasize-lines: 7-11

    def logical_conjunction(first, second):
        # if (first, second) == (True, False): return False
        # if (first, second) == (False, True): return False
        # if (first, second) == (False, False): return False
        # return first, second
        # if first == True and second == True:
        # if first and second:
        #     return True
        # else:
        #     return False
        return first and second

  green.

* I remove the commented lines from :ref:`logical_conjunction<test_logical_conjunction>`

  .. code-block:: python
    :lineno-start: 99

    def logical_conjunction(first, second):
        return first and second


    def exclusive_disjunction(first, second):
        return (not (first and second)) and (first or second)

----

* :ref:`logical_disjunction<test_logical_disjunction>` has only one case that returns :red:`False`, I break up the :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 2-7

    def logical_disjunction(first, second):
        # if (first, second) == (False, False): return False
        # return first, second
        if first == False and second == False:
            return False
        else:
            return True

  the test is still green.

* I then change the :ref:`if statement<if statements>` with :ref:`not<test_logical_negation>` and :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 4-5

    def logical_disjunction(first, second):
        # if (first, second) == (False, False): return False
        # return first, second
        # if first == False and second == False:
        if not first == True and not second == True:
            return False
        else:
            return True

  still green.

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 5-6

    def logical_disjunction(first, second):
        # if (first, second) == (False, False): return False
        # return first, second
        # if first == False and second == False:
        # if not first == True and not second == True:
        if not first and not second:
            return False
        else:
            return True

  green.

* I change the statement with :ref:`not<test_logical_negation>` since it happens two times

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 6-7

    def logical_disjunction(first, second):
        # if (first, second) == (False, False): return False
        # return first, second
        # if first == False and second == False:
        # if not first == True and not second == True:
        # if not first and not second:
        if (not first) (not or) (not second):
            return False
        else:
            return True

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

* I factor out :ref:`not<test_logical_negation>`

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 7-8

    def logical_disjunction(first, second):
        # if (first, second) == (False, False): return False
        # return first, second
        # if first == False and second == False:
        # if not first == True and not second == True:
        # if not first and not second:
        # if (not first) (not or) (not second):
        if not (first or second):
            return False
        else:
            return True

  the test is green again.

* I add a `return statement`_ for the :ref:`opposite<test_logical_negation>` of the :ref:`if statement<if statements>` because ``if something: return False`` can be written as ``return not (something)``

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 8-12

    def logical_disjunction(first, second):
        # if (first, second) == (False, False): return False
        # return first, second
        # if first == False and second == False:
        # if not first == True and not second == True:
        # if not first and not second:
        # if (not first) (not or) (not second):
        # if not (first or second):
        #     return False
        # else:
        #     return True
        return not (not (first or second))

  still green.

* I remove ``not not``

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 12-13

    def logical_disjunction(first, second):
        # if (first, second) == (False, False): return False
        # return first, second
        # if first == False and second == False:
        # if not first == True and not second == True:
        # if not first and not second:
        # if (not first) (not or) (not second):
        # if not (first or second):
        #     return False
        # else:
        #     return True
        # return not (not (first or second))
        return first or second

  the test is still green.

* I remove the commented lines from :ref:`logical_disjunction<test_logical_disjunction>`

  .. code-block:: python
    :lineno-start: 94

    def logical_disjunction(first, second):
        return first or second


    def logical_conjunction(first, second):
        return first and second

----

* I break up the :ref:`if statements` in :ref:`logical_equality<test_logical_equality>`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 2-7

    def logical_equality(first, second):
        # if (first, second) == (True, False): return False
        if first == True and second == False:
            return False
        # if (first, second) == (False, True): return False
        if first == False and second == True:
            return False
        return first, second

  the test is still green.

* I remove the comments then change the :ref:`if statements` with :ref:`not<test_logical_negation>` and :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 2-3, 5-6

    def logical_equality(first, second):
        # if first == True and second == False:
        if first == True and not second == True:
            return False
        # if first == False and second == True:
        if not first == True and second == True:
            return False
        return first, second

  still green.

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 2-3, 5-6

    def logical_equality(first, second):
        # if first == True and not second == True:
        if first and not second:
            return False
        # if not first == True and second == True:
        if not first and second:
            return False
        return first, second

  green.

* I put the two :ref:`if statements` together to make one

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 2-5

    def logical_equality(first, second):
        # if first and not second:
        #     return False
        # if not first and second:
        if (first and not second) or (not first and second):
            return False
        return first, second

  still green.

* I use a `return statement`_ because ...

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 2-6

    def logical_equality(first, second):
        return not (
            (first and not second)
            or
            (not first and second)
        )
        if (first and not second) or (not first and second):
            return False
        return first, second

  the test is still green.

* I multiply :ref:`not<test_logical_negation>` by all the symbols in parentheses

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 2-6

    def logical_equality(first, second):
        return (
            (not (first and not second))
            (not or)
            (not (not first and second))
        )
        return not (
            (first and not second)
            or
            (not first and second)
        )

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

* I change ``not or`` to :ref:`and<test_logical_conjunction>`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 3

    def logical_equality(first, second):
        return (
            (not (first and not second))
            and
            (not (not first and second))
        )
        return not (
            (first and not second)
            or
            (not first and second)
        )

  the test is green again

* I multiply :ref:`not<test_logical_negation>` by the symbols in the first part of the statement

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 3-4

    def logical_equality(first, second):
        return (
            # (not (first and not second))
            ((not first) (not and) (not not second))
            and
            (not (not first and second))
        )

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

* I change ``not and`` to :ref:`or<test_logical_disjunction>`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 3-4

    def logical_equality(first, second):
        return (
            # (not (first and not second))
            ((not first) or (not not second))
            and
            (not (not first and second))
        )

  the test is green again

* I remove ``not not``

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 3-4

    def logical_equality(first, second):
        return (
            # ((not first) or (not not second))
            (not first or second)
            and
            (not (not first and second))
        )

  still green.

* I multiply :ref:`not<test_logical_negation>` by the symbols in the second part of the statement

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 5-6

    def logical_equality(first, second):
        return (
            (not first or second)
            and
            # (not (not first and second))
            ((not not first) (not and) (not second))
        )

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python
    :lineno-start: 65

    SyntaxError: invalid syntax

* I change ``not and`` to :ref:`or<test_logical_disjunction>`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 5-6

    def logical_equality(first, second):
        return (
            (not first or second)
            and
            # (not (not first and second))
            ((not not first) or (not second))
        )

  the test is still green.

* I remove ``not not``

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 5-6

    def logical_equality(first, second):
        return (
            (not first or second)
            and
            # ((not not first) or (not second))
            (first or not second)
        )

  still green.

* I remove the comment

  .. code-block:: python
    :lineno-start: 65

    def logical_equality(first, second):
        return (not first or second) and (first or not second)


    def logical_disjunction(first, second):
        return first or second

----

* I make the :ref:`if statement<if statements>` in :ref:`logical_nand<test_logical_nand>` simpler

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 2

    def logical_nand(first, second):
        # if (first, second) == (True, True): return False
        if first == True and second == True:
            return False
        return first, second

  the test is still green.

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 2-3

    def logical_nand(first, second):
        # if first == True and second == True:
        if first and second:
            return False
        return first, second

  still green.

* I use I use a `return statement`_ because ...

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 2

    def logical_nand(first, second):
        return not (first and second)
        if first and second:
            return False
        return first, second

  green.

* I remove the other lines in :ref:`logical_nand<test_logical_nand>`

  .. code-block:: python
    :lineno-start: 60

    def logical_nand(first, second):
        return not (first and second)


    def logical_equality(first, second):
        return (not first or second) and (first or not second)

----

* :ref:`logical_nor<test_logical_nor>` has only one case that returns :green:`True`. I add an :ref:`if statement<if statements>` for it

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 2-5

    def logical_nor(first, second):
        if first == False and second == False:
            return True
        else:
            return False
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        if (first, second) == (False, True): return False
        return first, second

  the test is still green.

* I remove the other lines, then use :ref:`not<test_logical_negation>` and remove ``== False``

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 2-3

    def logical_nor(first, second):
        # if first == False and second == False:
        if not first and not second:
            return True
        else:
            return False

  still green.

* I use a `return statement`_

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 2

    def logical_nor(first, second):
        return not first and not second
        if not first and not second:
            return True
        else:
            return False

  green.

* I write the statement with :ref:`not<test_logical_negation>` because it happens 2 times

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 2

    def logical_nor(first, second):
        return (not first) (not or) (not second)
        return not first and not second

  the terminal_ is my friend, and shows `SyntaxError`_

  .. code-block:: python

    SyntaxError: invalid syntax

* I factor out the :ref:`not<test_logical_negation>`

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 2

    def logical_nor(first, second):
        return not (first or second)
        # return (not first) (not or) (not second)
        return not first and not second

  the test is green again

* I remove the other statements in :ref:`logical_nor<test_logical_nor>`

  .. code-block:: python
    :lineno-start: 113

    def logical_nor(first, second):
        return not (first or second)


    def logical_nand(first, second):
        return not (first and second)

----

* :ref:`material_implication<test_material_implication>` has only one case that returns :red:`False`, I add a `return statement`_ for it because ``if something: return False`` can be written as ``return not (something)``

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 2

    def material_implication(first, second):
        return not ((first, second) == (True, False))
        if (first, second) == (True, False): return False
        return first, second

  the test is still green.

* I break up the `return statement`_ to make it simpler

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 2

    def material_implication(first, second):
        return not (first == True and second == False)
        return not ((first, second) == (True, False))

  still green.

* I use :ref:`not<test_logical_negation>` and remove ``== True`` and ``== False``

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 2

    def material_implication(first, second):
        return not (first and not second)
        return not (first == True and second == False)

  green.

* I multiply :ref:`not<test_logical_negation>` by everything in the parentheses

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 2

    def material_implication(first, second):
        return (not first) (not and) (not not second)
        return not (first and not second)

  the terminal_ is my friend, and shows `SyntaxError`_

  .. code-block:: python

    SyntaxError: invalid syntax

* I change ``not and`` to :ref:`or<test_logical_disjunction>`

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 2

    def material_implication(first, second):
        return (not first) or (not not second)
        return not (first and not second)

  the test is green again

* I remove ``not not``

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 2

    def material_implication(first, second):
        return not first or second
        return (not first) or (not not second)
        return not (first and not second)

  still green.

* I remove the other statements in :ref:`material_implication<test_material_implication>`

  .. code-block:: python
    :lineno-start: 48

    def material_implication(first, second):
        return not first or second


    def logical_nor(first, second):
        return not (first or second)

----

* :ref:`material_non_implication<test_material_non_implication>` has 3 cases that return :ref:`False<test_what_is_false>`. I add a `return statement`_ for the  case that returns :green:`True`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 2

    def material_non_implication(first, second):
        return (first, second) == (True, False)
        if (first, second) == (True, True): return False
        if (first, second) == (False, True): return False
        if (first, second) == (False, False): return False
        return first, second

  the test is still green.

* I make the `return statement`_ simpler

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 2

    def material_non_implication(first, second):
        return first == True and second == False
        return (first, second) == (True, False)

  still green.

* I use :ref:`not<test_logical_negation>` and remove ``== True`` and ``== False``

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 2

    def material_non_implication(first, second):
        return first and not second
        return first == True and second == False

  green.

* I remove the other statement in :ref:`material_non_implication<test_material_non_implication>`

  .. code-block:: python
    :lineno-start: 43

    def material_non_implication(first, second):
        return first and not second


    def material_implication(first, second):
        return not first or second

----

* ``first`` is :ref:`True<test_what_is_true>` in the 2 cases where :ref:`negate_first<test_negate_first>` returns :red:`False`, I add an :ref:`if statement<if statements>` for them

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 2

    def negate_first(first, second):
        if first == True: return False
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        return first, second

  the test is still green.

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 2

    def negate_first(first, second):
        # if first == True: return False
        if first: return False
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        return first, second

  still green.

* I add a `return statement`_ because ...

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 2

    def negate_first(first, second):
        return not first
        if first: return False
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        return first, second

  green.

* I remove the other statements from :ref:`negate_first<test_negate_first>`

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 2

    def negate_first(first, second):
        return not first


    def material_non_implication(first, second):
        return first and not second

----

* ``second`` is :ref:`True<test_what_is_true>` in the 2 cases where :ref:`negate_second<test_negate_second>` returns :red:`False`. I add a `return statement`_ ``if something: return False`` can be written as ...

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 2

    def negate_second(first, second):
        return not second == True
        if (first, second) == (True, True): return False
        if (first, second) == (False, True): return False
        return first, second

  the test is still green.

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 2

    def negate_second(first, second):
        return not second
        return not second == True

  green.

* I remove the other statement in :ref:`negate_second<test_negate_second>`

  .. code-block:: python
    :linenos:

    def logical_negation(something):
        return not something


    def logical_identity(something):
        return something


    def logical_true():
        return True


    def logical_false():
        return None


    def tautology(first, second):
        return True


    def project_second(first, second):
        return second


    def project_first(first, second):
        return first


    def negate_second(first, second):
        return not second


    def negate_first(first, second):
        return not first


    def material_non_implication(first, second):
        return first and not second


    def material_implication(first, second):
        return not first or second


    def logical_nor(first, second):
        return not (first or second)


    def logical_nand(first, second):
        return not (first and second)


    def logical_equality(first, second):
        return (not first or second) and (first or not second)


    def logical_disjunction(first, second):
        return first or second


    def logical_conjunction(first, second):
        return first and second


    def exclusive_disjunction(first, second):
        return (not (first and second)) and (first or second)


    def converse_non_implication(first, second):
        return not first and second


    def converse_implication(first, second):
        return first or not second


    def contradiction(first, second):
        return False

* all the other :ref:`functions<what is a function?>` are already simple

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``truth_table.py``
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

I ran tests using :ref:`booleans<what are booleans?>` which can be :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>` for the operations of the `Truth Table`_ from Mathematics

* there are :ref:`2 nullary operations<Nullary Operations>`, they do not take input and always return the same thing, they are :ref:`constant<test_constant_function>`

  - :ref:`Logical False<test_logical_false>` always returns :red:`False`
  - :ref:`Logical True<test_logical_true>` always returns :green:`True`

* there are :ref:`2 unary operations<Unary Operations>`, they take one input

  - :ref:`Logical Identity<test_logical_identity>` returns its input as output
  - :ref:`Logical Negation<test_logical_negation>` returns the negation of its input as output

* there are 16 binary operations, they each take 2 inputs, in this case I named the second input ``second`` and the first one ``first``

  * :ref:`Contradiction<test_contradiction>`

    - always returns :red:`False`
    - never returns :green:`True`
    - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Tautology<test_tautology>` which always returns :green:`True`

  * :ref:`Converse Implication<test_converse_implication>`

    - returns ``first or not second``
    - returns :red:`False` if ``first`` is :ref:`False<test_what_is_false>` and ``second`` is :ref:`True<test_what_is_true>`
    - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Converse Non-Implication<test_converse_non_implication>` which returns :green:`True` only if ``first`` is :ref:`False<test_what_is_false>` and ``second`` is :ref:`True<test_what_is_true>`

  * :ref:`Converse Non-Implication<test_converse_non_implication>`

    - returns ``not first and second``
    - returns :green:`True` only if ``first`` is :ref:`False<test_what_is_false>` and ``second`` is :ref:`True<test_what_is_true>`
    - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Converse Implication<test_converse_implication>` which returns :red:`False` if ``first`` is :ref:`False<test_what_is_false>` and ``second`` is :ref:`True<test_what_is_true>`

  * :ref:`Exclusive Disjunction<test_exclusive_disjunction>`

    - returns ``first != second``
    - returns :green:`True` only if ``first`` and ``second`` are NOT equal
    - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Logical Equality<test_logical_equality>` which returns :green:`True` only if ``first`` and ``second`` are equal

  * :ref:`Logical Conjunction<test_logical_conjunction>` returns

    - returns ``first and second``
    - returns :green:`True` only if ``first`` is :ref:`True<test_what_is_true>` and ``second`` is :ref:`True<test_what_is_true>`
    - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Logical NAND<test_logical_nand>` which returns :red:`False` only if ``first`` is :ref:`True<test_what_is_true>` and ``second`` is :ref:`True<test_what_is_true>`

  * :ref:`Logical Disjunction<test_logical_disjunction>`

    - returns ``first or second``
    - returns :red:`False` only if ``first`` is :ref:`False<test_what_is_false>` and ``second`` is :ref:`False<test_what_is_false>`
    - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Logical NOR<test_logical_nor>` which returns :green:`True` only if ``first`` is :ref:`False<test_what_is_False>` and ``second`` is :ref:`False<test_what_is_false>`

  * :ref:`Logical Equality<test_logical_equality>`

    - returns ``first == second``
    - returns :green:`True` only if ``first`` and ``second`` are equal
    - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Exclusive Disjunction (Exclusive OR)<test_exclusive_disjunction>` which returns :green:`True` only if ``first`` and ``second`` are NOT equal

  * :ref:`Logical NAND<test_logical_nand>`

    - returns ``not (first and second)``
    - returns :red:`False` only if ``first`` is :ref:`True<test_what_is_true>` and ``second`` is :ref:`True<test_what_is_true>`
    - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Logical Conjunction (AND)<test_logical_conjunction>` which returns :green:`True` only if ``first`` is :ref:`True<test_what_is_true>` and ``second`` is :ref:`True<test_what_is_true>`

  * :ref:`Logical NOR<test_logical_nor>`

    - returns ``not (first or second)``
    - returns :green:`True` only if ``first`` is :ref:`False<test_what_is_False>` and ``second`` is :ref:`False<test_what_is_false>`
    - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Logical Disjunction<test_logical_disjunction>` which returns :red:`False` only if ``first`` is :ref:`False<test_what_is_false>` and ``second`` is :ref:`False<test_what_is_false>`

  * :ref:`Material/Logical Implication<test_material_implication>`

    - returns ``not first or second``
    - returns :red:`False` only if ``first`` is :ref:`True<test_what_is_true>` and ``second`` is :ref:`False<test_what_is_false>`
    - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Material Non-Implication<test_material_non_implication>` which returns :green:`True` only if ``first`` is :ref:`True<test_what_is_true>` and ``second`` is :ref:`False<test_what_is_false>`

  * :ref:`Material Non-Implication<test_material_non_implication>`

    - returns ``first and not second``
    - returns :green:`True` only if ``first`` is :ref:`True<test_what_is_true>` and ``second`` is :ref:`False<test_what_is_false>`
    - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Material/Logical Implication<test_material_implication>` which returns :red:`False` only if ``first`` is :ref:`True<test_what_is_true>` and ``second`` is :ref:`False<test_what_is_false>`

  * :ref:`Negate First<test_negate_first>`

    - always returns ``not first``
    - returns :green:`True` only if ``first`` is :ref:`False<test_what_is_false>`
    - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Project First<test_project_first>` which returns :green:`True` only if ``first`` is :ref:`True<test_what_is_true>`

  * :ref:`Negate Second<test_negate_second>`

    - always returns ``not second``
    - returns :green:`True` only if ``second`` is :ref:`False<test_what_is_false>`
    - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Project Second<test_project_second>` which returns :green:`True` only if ``second`` is :ref:`True<test_what_is_true>`

  * :ref:`Project First<test_project_first>`

    - always returns ``first``
    - returns :green:`True` only if ``first`` is :ref:`True<test_what_is_true>`
    - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Negate First<test_negate_first>` which returns :green:`True` only if ``first`` is :ref:`False<test_what_is_false>`
  * :ref:`Project Second<test_project_second>`

    - always returns ``second``
    - returns :green:`True` only if ``second`` is :ref:`True<test_what_is_true>`
    - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`Negate Second<test_negate_second>` which returns :green:`True` only if ``second`` is :ref:`False<test_what_is_false>`

  * :ref:`Tautology<test_tautology>`

    - always returns :green:`True`
    - never returns :red:`False`
    - is the :ref:`Logical Negation (NOT)<test_logical_negation>` of :ref:`contradiction<test_contradiction>`  which always returns :red:`False`

and

* :ref:`Logical Disjunction is "OR"<test_logical_disjunction>`
* :ref:`Logical Conjunction is "AND"<test_logical_conjunction>`
* :ref:`Logical Negation is "NOT" <test_logical_negation>`

All the :ref:`binary operations<truth table: binary operations>` or conditions have been written with some or all of the above 3.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed for the Truth Table?<truth table: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

you now know

* :ref:`how to make a Python test driven development environment manually<how to make a Python test driven development environment>`
* :ref:`what causes AssertionError?`
* :ref:`how to make functions<what is a function?>`
* :ref:`what causes AttributeError<what causes AttributeError?>`
* :ref:`how to pass values from tests to functions<telephone>`
* :ref:`what is None and NOT None<what is None?>`
* :ref:`what is True and False in Python<what are booleans?>`
* :ref:`how to write programs that make decisions<truth table>`

:ref:`Would you like to test projects that use the Truth Table?<truth table: projects>`

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