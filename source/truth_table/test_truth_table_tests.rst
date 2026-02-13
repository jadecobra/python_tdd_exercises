.. meta::
  :description: Master test-driven development in Python by learning to build and refactor logical functions from scratch. Watch the full tutorial to go from 20 failures to success.
  :keywords: Jacob Itegboje, python test driven development tutorial, how to write logical functions in python, python tdd practical example, python truth table tests, refactoring python code, python unittest tutorial, learn tdd with python, python binary operations tutorial

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
* :ref:`Binary Operations 1<truth table: Binary Operations 1>`
* :ref:`Binary Operations 2<truth table: Binary Operations 2>`
* :ref:`Binary Operations 3<truth table: Binary Operations 3>`
* :ref:`Binary Operations 4<truth table: Binary Operations 4>`

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

* I run the tests with `pytest-watcher`_

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows

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
* I delete everything in ``truth_table.py``, the terminal_ shows 20 failures, I start with the last one

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'logical_negation'

----

*********************************************************************************
:green:`GREEN`: make it pass
*********************************************************************************

* I add the name to ``truth_table.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    logical_negation

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'logical_negation' is not defined

* I point it to :ref:`None<what is None?>` to define it

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    logical_negation = None

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  :ref:`I cannot call None the way I can call a function<test_type_error_w_the_uncallables>`

* I make it a :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def logical_negation():
        return None

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: logical_negation() takes 0 positional arguments but 1 was given

* I add a name in parentheses

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def logical_negation(something):
        return None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None is not true

  the test expects :ref:`True<test_what_is_true>`

* I change :ref:`None<what is None?>` in the `return statement`_ to give the test what it wants

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def logical_negation(something):
        return True

  the terminal shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  the test expects :ref:`False<test_what_is_false>` if the :ref:`function<what is a function?>` returns :ref:`True<test_what_is_true>`

* I change the `return statement`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def logical_negation(something):
        return False

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  the test expects

  - :ref:`True<test_what_is_true>` if the :ref:`function<what is a function?>` returns :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>` if the :ref:`function<what is a function?>` returns :ref:`True<test_what_is_true>`

* I change the `return statement`_ to see the difference between the input and what the test expects

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def logical_negation(something):
        return something

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  the test expects

  - the :ref:`opposite<test_logical_negation>` of the input
  - :ref:`True<test_what_is_true>` if the :ref:`function<what is a function?>` returns :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>` if the :ref:`function<what is a function?>` returns :ref:`True<test_what_is_true>`

* I use :ref:`not<test_logical_negation>` in the `return statement`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def logical_negation(something):
        return not something

  1 test passes with 19 failures to go, progress! The terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.truth_table' has no attribute 'logical_identity'

* I add a :ref:`function<what is a function?>` for it

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def logical_negation(something):
        return not something


    def logical_identity():
        return None

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: logical_identity() takes 0 positional arguments but 1 was given

* I add a name in parentheses

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 1

    def logical_identity(something):
        return None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None is not true

* I change the `return statement`_ to give the test what it wants

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2

    def logical_identity(something):
        return True

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  the test expects :ref:`False<test_what_is_false>` if the :ref:`function<what is a function?>` returns :ref:`True<test_what_is_true>`

* I change the `return statement`_

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2

    def logical_identity(something):
        return False

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  the test expects

  - :ref:`True<test_what_is_true>` if the :ref:`function<what is a function?>` returns :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>` if the :ref:`function<what is a function?>` returns :ref:`True<test_what_is_true>`

* I change the `return statement`_ to see the difference between the input and what the test expects

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2

    def logical_identity(something):
        return something

  18 failed, 2 passed, more progress! The terminal_ shows :ref:`AttributeError<what causes ATtributeError?>`

  .. code-block:: python

    AttributeError: module 'src.truth_table' has no attribute 'logical_true'

* I add the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 5-6

    def logical_identity(something):
        return something


    def logical_true():
        return None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None is not true

* I change the `return statement`_ to give the test what it wants

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2

    def logical_true():
        return True

  17 failed, 3 passed. That was simple. The terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'logical_false'. Did you mean: 'logical_true'?

* I add the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 5-6

    def logical_true():
        return True


    def logical_false():
        return None

  16 failed, 4 passed, simple again. I am getting it. The terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.truth_table' has no attribute 'tautology'

* I add the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 5-6

    def logical_false():
        return None


    def tautology():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: tautology() takes 0 positional arguments but 2 were given

* I add two names in parentheses for the :ref:`function<what is a function?>` to take input arguments

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 1

    def tautology(first, second):
        return None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None is not true

* I change :ref:`None<what is None?>` to :ref:`True<test_what_is_true>` in the `return statement`_

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 2

    def tautology(first, second):
        return True

  15 failed, 5 passed, Ayy! the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'project_second'

* I add the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 5-6

    def tautology(first, second):
        return True


    def project_second():
        return None

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: project_second() takes 0 positional arguments but 2 were given

* I add two names in parentheses for the :ref:`function<what is a function?>` to take input arguments

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 1

    def project_second(first, second):
        return None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None is not true

* I change the `return statement`_ to give the test what it wants

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2

    def project_second(first, second):
        return False

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  the test expects :ref:`True<test_what_is_true>` if the :ref:`function<what is a function?>` returns :ref:`False<test_what_is_false>`

* I change the `return statement`_

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2

    def project_second(first, second):
        return True

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  the test expects

  - :ref:`False<test_what_is_false>` if the :ref:`function<what is a function?>` returns :ref:`True<test_what_is_true>`
  - :ref:`True<test_what_is_true>` if the :ref:`function<what is a function?>` returns :ref:`False<test_what_is_false>`

* I change the `return statement`_ to see the difference between the input and what the test expects

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2

    def project_second(first, second):
        return first, second

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, False) is not false

* I remove ``first`` from the `return statement`_  since ``second`` is :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2

    def project_second(first, second):
        return second

  14 failed, 6 passed. The terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'project_first'

* I add a :ref:`function<what is a function?>` for it

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 5-6

    def project_second(first, second):
        return second


    def project_first():
        return None

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: project_second() takes 0 positional arguments but 2 were given

  okay, I have seen this before

* I add 2 names in parentheses

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 1

    def project_first(first, second):
        return None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None is not true

* I change the `return statement`_ to give the test what it wants

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 2

    def project_first(first, second):
        return True

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  the test expects :ref:`False<test_what_is_false>` if the :ref:`function<what is a function?>` returns :ref:`True<test_what_is_true>`

* I change the `return statement`_

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 2

    def project_first(first, second):
        return False

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  the test expects

  - :ref:`True<test_what_is_true>` if the :ref:`function<what is a function?>` returns :ref:`False<test_what_is_false>`
  - :ref:`False<test_what_is_false>` if the :ref:`function<what is a function?>` returns :ref:`True<test_what_is_true>`

* I change the `return statement`_ to see the difference between the input and what the test expects

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 2

    def project_first(first, second):
        return first, second

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (False, True) is not false

* I remove ``second`` from the `return statement`_ since ``first`` is :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 2

    def project_first(first, second):
        return first

  13 failed, 7 passed. The terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'negate_second'

* I add a :ref:`function<what is a function?>` for :ref:`negate_second<test_negate_second>` with a `return statement`_ to see the difference between the input and what the test expects

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 5-6

    def project_first(first, second):
        return first


    def negate_second(first, second):
        return first, second

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, True) is not false

* I add an :ref:`if statement<if statements>` to :ref:`negate_second<test_negate_second>` since ``first`` and ``second`` are both not :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2

    def negate_second(first, second):
        if (first, second) == (True, True): return False
        return first, second

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (False, True) is not false

* I add another :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 3

    def negate_second(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (False, True): return False
        return first, second

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'negate_first'

* I add a :ref:`function<what is a function?>` for it with a `return statement`_ to see the difference between the input and what the test expects

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 7-8

    def negate_second(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (False, True): return False
        return first, second


    def negate_first(first, second):
        return first, second

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, True)

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 2

    def negate_first(first, second):
        if (first, second) == (True, True): return False
        return first, second

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, False) is not false

* I add another :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 3

    def negate_first(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        return first, second

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'material_non_implication'

* I add a :ref:`function<what is a function?>` for :ref:`material_non_implication<test_material_non_implication>` with a `return statement`_ to see the difference between the input and what the test expects

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 7-8

    def negate_first(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        return first, second


    def material_non_implication(first, second):
        return first, second

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, True) is not false

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 2

    def material_non_implication(first, second):
        if (first, second) == (True, True): return False
        return first, second

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (False, True) is not false

* I add another :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 3

    def material_non_implication(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (False, True): return False
        return first, second

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (False, False) is not false

* I add an :ref:`if statement<if statements>` for it

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 4

    def material_non_implication(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (False, True): return False
        if (first, second) == (False, False): return False
        return first, second

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'material_implication'

* I add a :ref:`function<what is a function?>` for :ref:`material_implication<test_material_implication>` with a `return statement`_ to see the difference between the input and what the test expects

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 8-9

    def material_non_implication(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (False, True): return False
        if (first, second) == (False, False): return False
        return first, second


    def material_implication(first, second):
        return first, second

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, False) is not false

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 2

    def material_implication(first, second):
        if (first, second) == (True, False): return False
        return first, second

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'logical_nor'

* I add a :ref:`function<what is a function?>` for :ref:`logical_nor<test_logical_nor>`

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 6-7

    def material_implication(first, second):
        if (first, second) == (True, False): return False
        return first, second


    def logical_nor(first, second):
        return first, second

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, True) is not false

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines:  2

    def logical_nor(first, second):
        if (first, second) == (True, True): return False
        return first, second

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, False) is not false

* I add another :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 3

    def logical_nor(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        return first, second

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (False, True) is not false

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 4

    def logical_nor(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        if (first, second) == (False, True): return False
        return first, second

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'logical_nand'. Did you mean: 'logical_nor'?

* I add a :ref:`function<what is a function?>` for :ref:`logical_nand<test_logical_nand>`

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 8-9

    def logical_nor(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        if (first, second) == (False, True): return False
        return first, second


    def logical_nand(first, second):
        return first, second

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, True) is not false

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 2

    def logical_nand(first, second):
        if (first, second) == (True, True): return False
        return first, second

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'logical_equality'

* I add the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 6-7

    def logical_nand(first, second):
        if (first, second) == (True, True): return False
        return first, second


    def logical_equality(first, second):
        return first, second

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, False) is not false

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 2

    def logical_equality(first, second):
        if (first, second) == (True, False): return False
        return first, second

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (False, True) is not false

* I add another :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 3

    def logical_equality(first, second):
        if (first, second) == (True, False): return False
        if (first, second) == (False, True): return False
        return first, second

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'logical_disjunction'

* I add a :ref:`function<what is a function?>` for :ref:`logical_disjunction<test_logical_disjunction>`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 7-8

    def logical_equality(first, second):
        if (first, second) == (True, False): return False
        if (first, second) == (False, True): return False
        return first, second


    def logical_disjunction(first, second):
        return first, second

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (False, False) is not false

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 2

    def logical_disjunction(first, second):
        if (first, second) == (False, False): return False
        return first, second

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'logical_conjunction'. Did you mean: 'logical_disjunction'?

* I add a :ref:`function<what is a function?>` for :ref:`logical_conjunction<test_logical_conjunction>`

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 6-7

    def logical_disjunction(first, second):
        if (first, second) == (False, False): return False
        return first, second


    def logical_conjunction(first, second):
        return first, second

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, False) is not false

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 2

    def logical_conjunction(first, second):
        if (first, second) == (True, False): return False
        return first, second

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (False, True) is not false

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 3

    def logical_conjunction(first, second):
        if (first, second) == (True, False): return False
        if (first, second) == (False, True): return False
        return first, second

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (False, False) is not false

* I add another :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 4

    def logical_conjunction(first, second):
        if (first, second) == (True, False): return False
        if (first, second) == (False, True): return False
        if (first, second) == (False, False): return False
        return first, second

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'exclusive_disjunction'

* I add a :ref:`function<what is a function?>` for :ref:`exclusive_disjunction<test_exclusive_disjunction>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 8-9

    def logical_conjunction(first, second):
        if (first, second) == (True, False): return False
        if (first, second) == (False, True): return False
        if (first, second) == (False, False): return False
        return first, second


    def exclusive_disjunction(first, second):
        return first, second

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, True) is not false

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 2

    def exclusive_disjunction(first, second):
        if (first, second) == (True, True): return False
        return first, second

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (False, False) is not false

* I add another :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 3

    def exclusive_disjunction(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (False, False): return False
        return first, second

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'converse_non_implication'. Did you mean: 'material_non_implication'?

* I add :ref:`converse_non_implication<test_converse_non_implication>`

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 7-8

    def exclusive_disjunction(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (False, False): return False
        return first, second


    def converse_non_implication(first, second):
        return first, second

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, True) is not false

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 2

    def converse_non_implication(first, second):
        if (first, second) == (True, True): return False
        return first, second

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, False) is not false

* I add another :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 3

    def converse_non_implication(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        return first, second

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (False, False) is not false

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 4

    def converse_non_implication(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        if (first, second) == (False, False): return False
        return first, second

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'converse_implication'. Did you mean: 'converse_non_implication'?

* I :ref:`converse_implication<test_converse_implication>`

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 8-9

    def converse_non_implication(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        if (first, second) == (False, False): return False
        return first, second


    def converse_implication(first, second):
        return first, second

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (False, True) is not false

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 2

    def converse_implication(first, second):
        if (first, second) == (False, True): return False
        return first, second

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'contradiction'

* I add :ref:`contradiction<test_contradiction>`

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 6-7

    def converse_implication(first, second):
        if (first, second) == (False, True): return False
        return first, second


    def contradiction(first, second):
        return first, second

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, True) is not false

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 2

    def contradiction(first, second):
        if (first, second) == (True, True): return False
        return first, second

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (True, False) is not false

* I add another :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 3

    def contradiction(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        return first, second

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (False, True) is not false

* I add another :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 4

    def contradiction(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        if (first, second) == (False, True): return False
        return first, second

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: (False, False) is not false

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 5

    def contradiction(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        if (first, second) == (False, True): return False
        if (first, second) == (False, False): return False
        return first, second

  the terminal_ shows

  .. code-block:: shell

    ======================== 20 passed in G.HIs ========================

All the tests are passing and the world is a better place than when I started! I am going home. Wait, there is more...

----

*********************************************************************************
:yellow:`REFACTOR`: make it better
*********************************************************************************

I can play with the :ref:`functions<what is a function?>` I have to make them simpler and understand why my solutions work, since all the tests are passing.

* :ref:`contradiction<test_contradiction>`  returns :ref:`False<test_what_is_false>` in 4 cases, with 2 inputs there are only 4 cases. I add a `return statement`_

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 2

    def contradiction(first, second):
        return False
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        if (first, second) == (False, True): return False
        if (first, second) == (False, False): return False
        return first, second

  the test is still green.

* I remove the other lines in :ref:`contradiction<test_contradiction>`

  .. code-block:: python
    :lineno-start: 101

    def contradiction(first, second):
        return False

----

* :ref:`converse_implication<test_converse_implication>` returns :ref:`False<test_what_is_false>` in only one case. I write out the :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 2-3

    def converse_implication(first, second):
        # if (first, second) == (False, True): return False
        if first == False and second == True:
            return False
        return first, second

  still green

* I change the statement with :ref:`not<test_logical_negation>` and :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 2-3

    def converse_implication(first, second):
        # if first == False and second == True:
        if not first == True and second == True:
            return False
        return first, second

  green

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 2-3

    def converse_implication(first, second):
        # if not first == True and second == True:
        if not first and second:
            return False
        return first, second

  still green

* I use a `return statement`_ because ``if something: return False`` is the same as ``return not (something)``

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 2

    def converse_implication(first, second):
        return not (not first and second)
        if not first and second:
            return False
        return first, second

  the test is still green

* I remove the other statements then "multiply :ref:`not<test_logical_negation>`" by the things in the parentheses

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 2

    def converse_implication(first, second):
        return (not not first) (not and) (not second)
        return not (not first and second)

  the terminal_ shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

* I change ``not and`` to :ref:`or<test_logical_disjunction>`

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 2

    def converse_implication(first, second):
        return (not not first) or (not second)
        return not (not first and second)

  the test is green again

* I remove the other `return statement`_ and ``not not`` because two :ref:`nots<test_logical_negation>` make a right?

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 2

    def converse_implication(first, second):
        return first or not second
        return (not not first) or (not second)

  the test is still green

* I remove the other statement in :ref:`converse_implication<test_converse_implication>`

  .. code-block:: python
    :lineno-start: 96

    def converse_implication(first, second):
        return first or not second


    def contradiction(first, second):
        return False

-----

* I add an :ref:`if statement<if statements>` for the only case that returns :ref:`True<test_what_is_true>` in :ref:`converse_non_implication<test_converse_non_implication>`

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 2

    def converse_non_implication(first, second):
        if (first, second) == (False, True): return True
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        if (first, second) == (False, False): return False
        return first, second

  the test is still green

* I break the statement up then add an `else clause`_ for the other 3 statements

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 2-6

    def converse_non_implication(first, second):
        # if (first, second) == (False, True): return True
        if first == False and second == True:
            return True
        else:
            return False
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        if (first, second) == (False, False): return False
        return first, second

  still green

* I remove the commented line and other statements, then change the :ref:`if statement<if statements>` with :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 2-3

    def converse_non_implication(first, second):
        # if first == False and second == True:
        if not first == True and second == True:
            return True
        else:
            return False

  green

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 2-3

    def converse_non_implication(first, second):
        # if not first == True and second == True:
        if not first and second:
            return True
        else:
            return False

  still green

* I add a `return statement`_ because ``if something: return True`` is the same as ``return something``

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 2

    def converse_non_implication(first, second):
        return not first and second
        if not first and second:
            return True
        else:
            return False

  the test is still green

* I remove the other statements in :ref:`converse_non_implication<test_converse_non_implication>`

  .. code-block:: python
    :lineno-start: 89

    def converse_non_implication(first, second):
        return not first and second


    def converse_implication(first, second):
        return first or not second

----

* I make the :ref:`if statements` in :ref:`exclusive_disjunction<test_exclusive_disjunction>` simpler

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 2-7

    def exclusive_disjunction(first, second):
        if (first, second) == (True, True): return False
        if (first, second) == (False, False): return False
        if first == True and second == True:
            return False
        if first == False and second == False:
            return False
        return first, second

  the test is still green

* I remove the first two :ref:`if statements` then change the new second :ref:`if statement<if statements>` with :ref:`not<test_logical_negation>` and :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 4-5

    def exclusive_disjunction(first, second):
        if first == True and second == True:
            return False
        # if first == False and second == False:
        if not first == True and not second == True:
            return False
        return first, second

  still green

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 2-3, 5-6

    def exclusive_disjunction(first, second):
        # if first == True and second == True:
        if first and second:
            return False
        # if not first == True and not second == True:
        if not first and not second:
            return False
        return first, second

  green

* I write everything in the second :ref:`if statement<if statements>` with :ref:`not<test_logical_negation>` because it happens two times in the line

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 4-5

    def exclusive_disjunction(first, second):
        if first and second:
            return False
        # if not first and not second:
        if (not first) (not or) (not second):
            return False
        return first, second

  the terminal_ shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

* I factor out the :ref:`nots<test_logical_negation>`

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 5-6

    def exclusive_disjunction(first, second):
        if first and second:
            return False
        # if not first and not second:
        # if (not first) (not or) (not second):
        if not (first or second):
            return False
        return first, second

  the test is green again

* I put the two :ref:`if statements` together to make one

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 2-5

    def exclusive_disjunction(first, second):
        # if first and second:
        #     return False
        # if not (first or second):
        if (first and second) or (not (first or second)):
            return False
        return first, second

  the test is still green

* I remove the commented lines, then add a `return statement`_ because ``if something: return False`` is the same as ``return not (something)``

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 2-6

    def exclusive_disjunction(first, second):
        return not (
            (first and second)
            or
            (not (first or second))
        )
        if (first and second) or (not (first or second)):
            return False
        return first, second

  still green

* I remove the other statements then multiply :ref:`not<test_logical_negation>` by everything in the parentheses because it happens two times in the line

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 2-5

    def exclusive_disjunction(first, second):
        return (
            (not (first and second))
            (not or)
            (not (not (first or second)))
        )
        return not (
            (first and second)
            or
            (not (first or second))
        )

  the terminal shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

* I change ``not or`` to :ref:`and<test_logical_conjunction>`

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 4

    def exclusive_disjunction(first, second):
        return (
            (not (first and second))
            and
            (not (not (first or second)))
        )
        return not (
            (first and second)
            or
            (not (first or second))
        )

  the test is green again

* I remove ``not not`` because "the negation of a negation is ..."

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 2

    def exclusive_disjunction(first, second):
        return ((not (first and second)) and (first or second))
        return not (
            (first and second)
            or
            (not (first or second))
        )

  green

* I remove the other statements in :ref:`exclusive_disjunction<test_exclusive_disjunction>`

  .. code-block:: python
    :lineno-start: 83

    def exclusive_disjunction(first, second):
        return (not (first and second)) and (first or second)


    def converse_non_implication(first, second):
        return not first and second

----

* :ref:`logical_conjunction<test_logical_conjunction>` has only one case that returns :ref:`True<test_what_is_true>`, it is the  case. I add an :ref:`if statement<if statements>` for it

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 2

    def logical_conjunction(first, second):
        if (first, second) == (True, True): return True
        if (first, second) == (True, False): return False
        if (first, second) == (False, True): return False
        if (first, second) == (False, False): return False
        return first, second

  the test is still green

* I remove the other statements and break up the :ref:`if statement<if statements>` to make it simpler

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 2-3

    def logical_conjunction(first, second):
        # if (first, second) == (True, True): return True
        if first == True and second == True:
            return True

  the test is still green because :ref:`all functions return None by default, as if they have an invisible line that says return None<test_making_a_function_w_return_none>`

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 2-3

    def logical_conjunction(first, second):
        # if first == True and second == True:
        if first and second:
            return True

  still green

* I use a `return statement`_ because ``if something: return True`` is the same as ``return something``

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 2

    def logical_conjunction(first, second):
        return first and second
        if first and second:
            return True

  green

* I remove the other statements in :ref:`logical_conjunction<test_logical_conjunction>`

  .. code-block:: python
    :lineno-start: 76

    def logical_conjunction(first, second):
        return first and second


    def exclusive_disjunction(first, second):
        return (not (first and second)) and (first or second)

----

* :ref:`logical_disjunction<test_logical_disjunction>` has only one case that returns :ref:`False<test_what_is_false>`, I break up the :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 2-4

    def logical_disjunction(first, second):
        # if (first, second) == (False, False): return False
        if first == False and second == False:
            return False
        return first, second

  the test is still green

* I remove the comment then change the :ref:`if statement<if statements>` with :ref:`not<test_logical_negation>` and :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 2-3

    def logical_disjunction(first, second):
        # if first == False and second == False:
        if not first == True and not second == True:
            return False
        return first, second

  still green

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 2-3

    def logical_disjunction(first, second):
        # if not first == True and not second == True:
        if not first and not second:
            return False
        return first, second

  green

* I change the statement with :ref:`not<test_logical_negation>` because it happens two times

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 2-3

    def logical_disjunction(first, second):
        # if not first and not second:
        if (not first) (not and) (not second):
            return False
        return first, second

  the terminal_ shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

* I factor out :ref:`not<test_logical_negation>`

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 3-4

    def logical_disjunction(first, second):
        # if not first and not second:
        # if (not first) (not or) (not second):
        if not (first or second):
            return False
        return first, second

  the test is green again

* I add a `return statement`_ for the :ref:`opposite<test_logical_negation>` of the :ref:`if statement<if statements>` because ``if something: return False`` is the same as ``return not (something)``

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 2

    def logical_disjunction(first, second):
        return not (not (first or second))
        if not (first or second):
            return False
        return first, second

  still green

* I remove ``not not``

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 2

    def logical_disjunction(first, second):
        return first or second
        return not (not (first or second))

  the test is still green

* I remove the other statement in :ref:`logical_disjunction<test_logical_disjunction>`

  .. code-block:: python
    :lineno-start: 71

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

  the test is still green

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

  still green

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

  green

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

  still green

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

  the test is still green

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

  the terminal_ shows SyntaxError_

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

  the terminal_ shows SyntaxError_

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

  still green

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

  the terminal_ shows SyntaxError_

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

  the test is still green

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

  still green

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

  the test is still green

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 2-3

    def logical_nand(first, second):
        # if first == True and second == True:
        if first and second:
            return False
        return first, second

  still green

* I use I use a `return statement`_ because ...

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 2

    def logical_nand(first, second):
        return not (first and second)
        if first and second:
            return False
        return first, second

  green

* I remove the other lines in :ref:`logical_nand<test_logical_nand>`

  .. code-block:: python
    :lineno-start: 60

    def logical_nand(first, second):
        return not (first and second)


    def logical_equality(first, second):
        return (not first or second) and (first or not second)

----

* :ref:`logical_nor<test_logical_nor>` has only one case that returns :ref:`True<test_what_is_true>`. I add an :ref:`if statement<if statements>` for it

  .. code-block:: python
    :lineno-start: 53
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

  the test is still green

* I remove the other lines, then use :ref:`not<test_logical_negation>` and remove ``== False``

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 2-3

    def logical_nor(first, second):
        # if first == False and second == False:
        if not first and not second:
            return True
        else:
            return False

  still green

* I use a `return statement`_

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 2

    def logical_nor(first, second):
        return not first and not second
        if not first and not second:
            return True
        else:
            return False

  green

* I write the statement with :ref:`not<test_logical_negation>` because it happens 2 times

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 2

    def logical_nor(first, second):
        return (not first) (not or) (not second)
        return not first and not second

  the terminal_ shows `SyntaxError`_

  .. code-block:: python

    SyntaxError: invalid syntax

* I factor out the :ref:`not<test_logical_negation>`

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 2

    def logical_nor(first, second):
        return not (first or second)
        # return (not first) (not or) (not second)
        return not first and not second

  the test is green again

* I remove the other statements in :ref:`logical_nor<test_logical_nor>`

  .. code-block:: python
    :lineno-start: 53

    def logical_nor(first, second):
        return not (first or second)


    def logical_nand(first, second):
        return not (first and second)

----

* :ref:`material_implication<test_material_implication>` has only one case that returns :ref:`False<test_what_is_false>`, I add a `return statement`_ for it because ``if something: return False`` is the same as ``return not (something)``

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 2

    def material_implication(first, second):
        return not ((first, second) == (True, False))
        if (first, second) == (True, False): return False
        return first, second

  the test is still green

* I break up the `return statement`_ to make it simpler

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 2

    def material_implication(first, second):
        return not (first == True and second == False)
        return not ((first, second) == (True, False))

  still green

* I use :ref:`not<test_logical_negation>` and remove ``== True`` and ``== False``

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 2

    def material_implication(first, second):
        return not (first and not second)
        return not (first == True and second == False)

  green

* I multiply :ref:`not<test_logical_negation>` by everything in the parentheses

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 2

    def material_implication(first, second):
        return (not first) (not and) (not not second)
        return not (first and not second)

  the terminal_ shows `SyntaxError`_

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

  still green

* I remove the other statements in :ref:`material_implication<test_material_implication>`

  .. code-block:: python
    :lineno-start: 48

    def material_implication(first, second):
        return not first or second


    def logical_nor(first, second):
        return not (first or second)

----

* :ref:`material_non_implication<test_material_non_implication>` has 3 cases that return :ref:`False<test_what_is_false>`. I add a `return statement`_ for the  case that returns :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 2

    def material_non_implication(first, second):
        return (first, second) == (True, False)
        if (first, second) == (True, True): return False
        if (first, second) == (False, True): return False
        if (first, second) == (False, False): return False
        return first, second

  the test is still green

* I make the `return statement`_ simpler

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 2

    def material_non_implication(first, second):
        return first == True and second == False
        return (first, second) == (True, False)

  still green

* I use :ref:`not<test_logical_negation>` and remove ``== True`` and ``== False``

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 2

    def material_non_implication(first, second):
        return first and not second
        return first == True and second == False

  green

* I remove the other statement in :ref:`material_non_implication<test_material_non_implication>`

  .. code-block:: python
    :lineno-start: 41

    def material_non_implication(first, second):
        return first and not second


    def material_implication(first, second):
        return not first or second

----

* ``first`` is :ref:`True<test_what_is_true>` in the 2 cases where :ref:`negate_first<test_negate_first>` returns :ref:`False<test_what_is_false>`, I add an :ref:`if statement<if statements>` for them

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 2

    def negate_first(first, second):
        if first == True: return False
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        return first, second

  the test is still green

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 2

    def negate_first(first, second):
        # if first == True: return False
        if first: return False
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        return first, second

  still green

* I add a `return statement`_ because ...

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 2

    def negate_first(first, second):
        return not first
        if first: return False
        if (first, second) == (True, True): return False
        if (first, second) == (True, False): return False
        return first, second

  green

* I remove the other statements from :ref:`negate_first<test_negate_first>`

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 2

    def negate_first(first, second):
        return not first


    def material_non_implication(first, second):
        return first and not second

----

* ``second`` is :ref:`True<test_what_is_true>` in the 2 cases where :ref:`negate_second<test_negate_second>` returns :ref:`False<test_what_is_false>`. I add a `return statement`_ ``if something: return False`` is the same as ...

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2

    def negate_second(first, second):
        return not second == True
        if (first, second) == (True, True): return False
        if (first, second) == (False, True): return False
        return first, second

  the test is still green

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2

    def negate_second(first, second):
        return not second
        return not second == True

  green

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

* I close ``truth_table.py`` in the :ref:`editor<2 editors>`
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

I ran tests using :ref:`booleans<what are booleans?>` which can be :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>` for the operations of the `Truth Table`_ from Mathematics

* there are :ref:`2 nullary operations<Nullary Operations>`, they do not take input and always return the same thing, they are :ref:`constant<test_constant_function>`

  - :ref:`Logical False<test_logical_false>` always returns :ref:`False<test_what_is_false>`
  - :ref:`Logical True<test_logical_true>` always returns :ref:`True<test_what_is_true>`

* there are :ref:`2 unary operations<Unary Operations>`, they take one input

  - :ref:`Logical Identity<test_logical_identity>` returns its input as output
  - :ref:`Logical Negation<test_logical_negation>` returns the negation of its input as output

* there are 16 binary operations, they each take 2 inputs, in this case I named the second input ``second`` and the first one ``first``

  * :ref:`Contradiction<test_contradiction>`

    - always returns :ref:`False<test_what_is_false>`
    - never returns :ref:`True<test_what_is_true>`
    - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Tautology<test_tautology>` which always returns :ref:`True<test_what_is_true>`

  * :ref:`Converse Implication<test_converse_implication>`

    - returns ``first or not second``
    - returns :ref:`False<test_what_is_false>` if ``first`` is :ref:`False<test_what_is_false>` and ``second`` is :ref:`True<test_what_is_true>`
    - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Converse NonImplication<test_converse_non_implication>` which returns :ref:`True<test_what_is_true>` only if ``first`` is :ref:`False<test_what_is_false>` and ``second`` is :ref:`True<test_what_is_true>`

  * :ref:`Converse NonImplication<test_converse_non_implication>`

    - returns ``not first and second``
    - returns :ref:`True<test_what_is_true>` only if ``first`` is :ref:`False<test_what_is_false>` and ``second`` is :ref:`True<test_what_is_true>`
    - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Converse Implication<test_converse_implication>` which returns :ref:`False<test_what_is_false>` if ``first`` is :ref:`False<test_what_is_false>` and ``second`` is :ref:`True<test_what_is_true>`

  * :ref:`Exclusive Disjunction<test_exclusive_disjunction>`

    - returns ``first != second``
    - returns :ref:`True<test_what_is_true>` only if ``first`` and ``second`` are NOT equal
    - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Logical Equality<test_logical_equality>` which returns :ref:`True<test_what_is_true>` only if ``first`` and ``second`` are equal

  * :ref:`Logical Conjunction<test_logical_conjunction>` returns

    - returns ``first and second``
    - returns :ref:`True<test_what_is_true>` only if ``first`` is :ref:`True<test_what_is_true>` and ``second`` is :ref:`True<test_what_is_true>`
    - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Logical NAND<test_logical_nand>` which returns :ref:`False<test_what_is_false>` only if ``first`` is :ref:`True<test_what_is_true>` and ``second`` is :ref:`True<test_what_is_true>`

  * :ref:`Logical Disjunction<test_logical_disjunction>`

    - returns ``first or second``
    - returns :ref:`False<test_what_is_false>` only if ``first`` is :ref:`False<test_what_is_false>` and ``second`` is :ref:`False<test_what_is_false>`
    - is the  :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Logical NOR<test_logical_nor>` which returns :ref:`True<test_what_is_true>` only if ``first`` is :ref:`False<test_what_is_False>` and ``second`` is :ref:`False<test_what_is_false>`

  * :ref:`Logical Equality<test_logical_equality>`

    - returns ``first == second``
    - returns :ref:`True<test_what_is_true>` only if ``first`` and ``second`` are equal
    - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Exclusive Disjunction (Exclusive OR)<test_exclusive_disjunction>` which returns :ref:`True<test_what_is_true>` only if ``first`` and ``second`` are NOT equal

  * :ref:`Logical NAND<test_logical_nand>`

    - returns ``not (first and second)``
    - returns :ref:`False<test_what_is_false>` only if ``first`` is :ref:`True<test_what_is_true>` and ``second`` is :ref:`True<test_what_is_true>`
    - is the :ref:`opposite (Logical Negation) (not)<test_logical_negation>` of :ref:`Logical Conjunction (and)<test_logical_conjunction>` which returns :ref:`True<test_what_is_true>` only if ``first`` is :ref:`True<test_what_is_true>` and ``second`` is :ref:`True<test_what_is_true>`

  * :ref:`Logical NOR<test_logical_nor>`

    - returns ``not (first or second)``
    - returns :ref:`True<test_what_is_true>` only if ``first`` is :ref:`False<test_what_is_False>` and ``second`` is :ref:`False<test_what_is_false>`
    - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Logical Disjunction<test_logical_disjunction>` which returns :ref:`False<test_what_is_false>` only if ``first`` is :ref:`False<test_what_is_false>` and ``second`` is :ref:`False<test_what_is_false>`

  * :ref:`Material/Logical Implication<test_material_implication>`

    - returns ``not first or second``
    - returns :ref:`False<test_what_is_false>` only if ``first`` is :ref:`True<test_what_is_true>` and ``second`` is :ref:`False<test_what_is_false>`
    - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Material NonImplication<test_material_non_implication>` which returns :ref:`True<test_what_is_true>` only if ``first`` is :ref:`True<test_what_is_true>` and ``second`` is :ref:`False<test_what_is_false>`

  * :ref:`Material NonImplication<test_material_non_implication>`

    - returns ``first and not second``
    - returns :ref:`True<test_what_is_true>` only if ``first`` is :ref:`True<test_what_is_true>` and ``second`` is :ref:`False<test_what_is_false>`
    - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Material/Logical Implication<test_material_implication>` which returns :ref:`False<test_what_is_false>` only if ``first`` is :ref:`True<test_what_is_true>` and ``second`` is :ref:`False<test_what_is_false>`

  * :ref:`Negate First<test_negate_first>`

    - always returns ``not first``
    - returns :ref:`True<test_what_is_true>` only if ``first`` is :ref:`False<test_what_is_false>`
    - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Project First<test_project_first>` which returns :ref:`True<test_what_is_true>` only if ``first`` is :ref:`True<test_what_is_true>`

  * :ref:`Negate Second<test_negate_second>`

    - always returns ``not second``
    - returns :ref:`True<test_what_is_true>` only if ``second`` is :ref:`False<test_what_is_false>`
    - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Project Second<test_project_second>` which returns :ref:`True<test_what_is_true>` only if ``second`` is :ref:`True<test_what_is_true>`

  * :ref:`Project First<test_project_first>`

    - always returns ``first``
    - returns :ref:`True<test_what_is_true>` only if ``first`` is :ref:`True<test_what_is_true>`
    - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Negate First<test_negate_first>` which returns :ref:`True<test_what_is_true>` only if ``first`` is :ref:`False<test_what_is_false>`
  * :ref:`Project Second<test_project_second>`

    - always returns ``second``
    - returns :ref:`True<test_what_is_true>` only if ``second`` is :ref:`True<test_what_is_true>`
    - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Negate Second<test_negate_second>` which returns :ref:`True<test_what_is_true>` only if ``second`` is :ref:`False<test_what_is_false>`

  * :ref:`Tautology<test_tautology>`

    - always returns :ref:`True<test_what_is_true>`
    - never returns :ref:`False<test_what_is_false>`
    - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`contradiction<test_contradiction>`  which always returns :ref:`False<test_what_is_false>`

and

* :ref:`Logical Disjunction is "or"<test_logical_disjunction>`
* :ref:`Logical Conjunction is "and"<test_logical_conjunction>`
* :ref:`Logical Negation is "not" <test_logical_negation>`

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

you now know

* :ref:`how to make a test driven development environment manually<how to make a test driven development environment>`
* :ref:`how to raise AssertionError with assert methods<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`what causes AttributeError<what causes AttributeError?>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what is None and NOT None<what is None?>`
* :ref:`what is True and False in Python<what are booleans?>`
* :ref:`how to write programs that make decisions<truth table>`

:ref:`Would you like to test making a calculator?<how to make a calculator>`

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