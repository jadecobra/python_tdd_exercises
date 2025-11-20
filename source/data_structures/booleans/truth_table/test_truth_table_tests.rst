.. meta::
  :description: Master test-driven development in Python by learning to build and refactor logical functions from scratch. Watch the full tutorial to go from 20 failures to success.
  :keywords: Jacob Itegboje, python test driven development tutorial, how to write logical functions in python, python tdd practical example, python truth table tests, refactoring python code, python unittest tutorial, learn tdd with python, python binary operations tutorial

.. include:: ../../../links.rst

.. _test_truth_table_tests:

#################################################################################
truth table: test_truth_table_tests
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/DtGE6WqRZgo?si=08uXK8QMZaG06XWp" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

*********************************************************************************
requirements
*********************************************************************************

* :ref:`Binary Operations part 4<truth table: Binary Operations part 4>`

----

I want to write a program that makes the tests in ``test_truth_table.py`` pass without looking at them

*********************************************************************************
red: make it fail
*********************************************************************************

* I close ``test_truth_table.py``
* then delete all the tests in ``truth_table.py``, the terminal_ shows 20 failures, I start with the last one

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'tautology'

*********************************************************************************
green: make it pass
*********************************************************************************

* I add the name

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    tautology

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'tautology' is not defined

  I point the name to :ref:`None`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    tautology = None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

  I make ``tautology`` a :ref:`function<functions>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def tautology():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: tautology() takes 0 positional arguments but 2 were given

  I add names in parentheses for the :ref:`function<functions>` to take input arguments

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def tautology(x, y):
        return None

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None is not true

  I change :ref:`None` to :ref:`True<test_what_is_true>` in the `return statement`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def tautology(x, y):
        return True

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'project_second'

* I add the :ref:`function<functions>` using the solution I just used for ``tautology``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def tautology(x, y):
        return True


    def project_second(x, y):
        return True

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: True is not false

  I change the `return statement`_

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2

    def project_second(x, y):
        return False

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: False is not true

  I want to see the difference between the inputs and the expected output

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2

    def project_second(x, y):
        return x, y

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (True, False) is not false

  ``y`` is :ref:`False<test_what_is_false>`, I remove ``x`` from the `return statement`_

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2

    def project_second(x, y):
        return y

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'project_first'

* I add a :ref:`function<functions>` for it

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 5-6

    def project_second(x, y):
        return y


    def project_first(x, y):
        return x, y

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (False, True) is not false

  ``x`` is :ref:`False<test_what_is_false>`, I remove ``y`` from the `return statement`_

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2

    def project_first(x, y):
        return x

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'negate_second'

* I add a :ref:`function<functions>` for ``negate_second``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 5-6

    def project_first(x, y):
        return x


    def negate_second(x, y):
        return x, y

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (True, True) is not false

  I add an `if statement`_ to ``negate_second``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

    def negate_second(x, y):
        if (x, y) == (True, True): return False
        return x, y

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (False, True) is not false

  I add another `if statement`_

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 3

    def negate_second(x, y):
        if (x, y) == (True, True): return False
        if (x, y) == (False, True): return False
        return x, y

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'negate_first'

* I add a :ref:`function<functions>` definition for it

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 6-7

    def negate_second(x, y):
        if (x, y) == (True, True): return False
        if (x, y) == (False, True): return False
        return x, y

    def negate_first(x, y):
        return x, y

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (True, True)

  I add an `if statement`_

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 2

    def negate_first(x, y):
        if (x, y) == (True, True): return False
        return x, y

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (True, False) is not false

  I add an `if statement`_

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 3

    def negate_first(x, y):
        if (x, y) == (True, True): return False
        if (x, y) == (True, False): return False
        return x, y

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'material_non_implication'

* I add a :ref:`function<functions>` for ``material_non_implication``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 5-6

        if (x, y) == (True, False): return False
        return x, y


    def material_non_implication(x, y):
        return x, y

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (True, True) is not false

  I add an `if statement`_

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 2

    def material_non_implication(x, y):
        if (x, y) == (True, True): return False
        return x, y

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (False, True) is not false

  I add another `if statement`_

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 3

    def material_non_implication(x, y):
        if (x, y) == (True, True): return False
        if (x, y) == (False, True): return False
        return x, y

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (False, False) is not false

  I add an `if statement`_ for it

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 4

    def material_non_implication(x, y):
        if (x, y) == (True, True): return False
        if (x, y) == (False, True): return False
        if (x, y) == (False, False): return False
        return x, y

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'material_implication'

* I add a :ref:`function<functions>` for ``material_implication``

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 5-6

        if (x, y) == (False, False): return False
        return x, y


    def material_implication(x, y):
        return x, y

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (True, False) is not false

  I add an `if statement`_

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 2

    def material_implication(x, y):
        if (x, y) == (True, False): return False
        return x, y

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'logical_nor'

* I add a :ref:`function<functions>` for ``logical_nor``

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 5-6

        if (x, y) == (True, False): return False
        return x, y


    def logical_nor(x, y):
        return x, y

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (True, True) is not false

  I add an `if statement`_

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines:  2

    def logical_nor(x, y):
        if (x, y) == (True, True): return False
        return x, y

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (True, False) is not false

  I add another `if statement`_

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 3

    def logical_nor(x, y):
        if (x, y) == (True, True): return False
        if (x, y) == (True, False): return False
        return x, y

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (False, True) is not false

  I add an `if statement`_

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 4

    def logical_nor(x, y):
        if (x, y) == (True, True): return False
        if (x, y) == (True, False): return False
        if (x, y) == (False, True): return False
        return x, y

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'logical_nand'. Did you mean: 'logical_nor'?

* I add a :ref:`function<functions>` for ``logical_nand``

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 5-6

        if (x, y) == (False, True): return False
        return x, y


    def logical_nand(x, y):
        return x, y

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (True, True) is not false

  I add an `if statement`_

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 2

    def logical_nand(x, y):
        if (x, y) == (True, True): return False
        return x, y

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'logical_equality'

* I add the :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 5-6

        if (x, y) == (True, True): return False
        return x, y


    def logical_equality(x, y):
        return x, y

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (True, False) is not false

  I add an `if statement`_

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2

    def logical_equality(x, y):
        if (x, y) == (True, False): return False
        return x, y

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (False, True) is not false

  I add another `if statement`_

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 3

    def logical_equality(x, y):
        if (x, y) == (True, False): return False
        if (x, y) == (False, True): return False
        return x, y

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'logical_disjunction'

* I add a :ref:`function<functions>` for ``logical_disjunction``

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 5-6

        if (x, y) == (False, True): return False
        return x, y


    def logical_disjunction(x, y):
        return x, y

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (False, False) is not false

  I add an `if statement`_

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2

    def logical_disjunction(x, y):
        if (x, y) == (False, False): return False
        return x, y

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'logical_conjunction'. Did you mean: 'logical_disjunction'?

* I add a :ref:`function<functions>` for ``logical_disjunction``

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 5-6

        if (x, y) == (False, False): return False
        return x, y


    def logical_conjunction(x, y):
        return x, y

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (True, False) is not false

  I add an `if statement`_

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 2

    def logical_conjunction(x, y):
        if (x, y) == (True, False): return False
        return x, y

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (False, True) is not false

  I add an `if statement`_

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 3

    def logical_conjunction(x, y):
        if (x, y) == (True, False): return False
        if (x, y) == (False, True): return False
        return x, y

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (False, False) is not false

  I add another `if statement`_

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 4

    def logical_conjunction(x, y):
        if (x, y) == (True, False): return False
        if (x, y) == (False, True): return False
        if (x, y) == (False, False): return False
        return x, y

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'exclusive_disjunction

* I add a :ref:`function<functions>` for ``exclusive_disjunction``

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 5-6

        if (x, y) == (False, False): return False
        return x, y


    def exclusive_disjunction(x, y):
        return x, y

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (True, True) is not false

  I add an `if statement`_

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 2

    def exclusive_disjunction(x, y):
        if (x, y) == (True, True): return False
        return x, y

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (False, False) is not false

  I add another `if statement`_

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 3

    def exclusive_disjunction(x, y):
        if (x, y) == (True, True): return False
        if (x, y) == (False, False): return False
        return x, y

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'converse_non_implication'. Did you mean: 'material_non_implication'?

* I add a definition for the ``material_non_implication`` :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 5-6

        if (x, y) == (False, False): return False
        return x, y


    def converse_non_implication(x, y):
        return x, y

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (True, True) is not false

  I add an `if statement`_

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 2

    def converse_non_implication(x, y):
        if (x, y) == (True, True): return False
        return x, y

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (True, False) is not false

  I add another `if statement`_

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 3

    def converse_non_implication(x, y):
        if (x, y) == (True, True): return False
        if (x, y) == (True, False): return False
        return x, y

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (False, False) is not false

  I add an `if statement`_

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 4

    def converse_non_implication(x, y):
        if (x, y) == (True, True): return False
        if (x, y) == (True, False): return False
        if (x, y) == (False, False): return False
        return x, y

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'converse_implication'. Did you mean: 'converse_non_implication'?

* I add the :ref:`function<functions>` for ``converse_non_implication``

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 5-6

        if (x, y) == (False, False): return False
        return x, y


    def converse_implication(x, y):
        return x, y

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (False, True) is not false

  I add an `if statement`_

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 2

    def converse_implication(x, y):
        if (x, y) == (False, True): return False
        return x, y

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'contradiction'

* I add a :ref:`function<functions>` for ``contradiction``

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 5-6

        if (x, y) == (False, True): return False
        return x, y


    def contradiction(x, y):
        return x, y

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (True, True) is not false

  I add an `if statement`_

  .. code-block:: python
    :lineno-start: 85
    :emphasize-lines: 2

    def contradiction(x, y):
        if (x, y) == (True, True): return False
        return x, y

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (True, False) is not false

  I add another `if statement`_

  .. code-block:: python
    :lineno-start: 85
    :emphasize-lines: 3

    def contradiction(x, y):
        if (x, y) == (True, True): return False
        if (x, y) == (True, False): return False
        return x, y

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (False, True) is not false

  I add another `if statement`_

  .. code-block:: python
    :lineno-start: 85
    :emphasize-lines: 4

    def contradiction(x, y):
        if (x, y) == (True, True): return False
        if (x, y) == (True, False): return False
        if (x, y) == (False, True): return False
        return x, y

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: (False, False) is not false

  I add an `if statement`_

  .. code-block:: python
    :lineno-start: 85
    :emphasize-lines: 5

    def contradiction(x, y):
        if (x, y) == (True, True): return False
        if (x, y) == (True, False): return False
        if (x, y) == (False, True): return False
        if (x, y) == (False, False): return False
        return x, y

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'logical_negation'. Did you mean: 'logical_conjunction'?

* I add a :ref:`function<functions>` for ``logical_negation``

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 5-6

        if (x, y) == (False, False): return False
        return x, y


    def logical_negation(x, y):
        return x, y

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: logical_negation() missing 1 required positional argument: 'y'

  I remove ``y`` from the parentheses, to make the :ref:`function<functions>` take only 1 input

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 1-2

    def logical_negation(x):
        return x

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: True is not false

  I add "not_" to the `return statement`_

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 2

    def logical_negation(x):
        return not x

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'logical_identity'. Did you mean: 'logical_equality'?

* I add a :ref:`function<functions>` for ``logical_identity``

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 5-6

    def logical_negation(x):
        return not x


    def logical_identity(x):
        return not x

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: False is not true

  I remove "not_" from the `return statement`_

  .. code-block:: python
    :lineno-start: 97
    :emphasize-lines: 2

    def logical_identity(x):
        return x

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'logical_true'. Did you mean: 'logical_nand'?

* I add a :ref:`function<functions>` for ``logical_true``

  .. code-block:: python
    :lineno-start: 97
    :emphasize-lines: 5-6

    def logical_identity(x):
        return x


    def logical_true(x):
        return x

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: logical_true() missing 1 required positional argument: 'x'

  I remove ``x`` from the parentheses, this :ref:`function` does not take input, I change the `return statement`_

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 1-2

    def logical_true():
        return None

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None is not true

  I change :ref:`None` to :ref:`True<test_what_is_true>` in the `return statement`_

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 2

    def logical_true():
        return True

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'logical_false'. Did you mean: 'logical_nand'?

* I add a :ref:`function<functions>` for ``logical_false``

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 5-6

    def logical_true():
        return True


    def logical_false():
        return False

  the terminal_ shows green! All tests are passing and the world is a better place than when I started.

refactor: make it better
#################################################################################

I can refactor the :ref:`functions<functions>` I have, to make them simpler since all the tests are passing

* :ref:`logical_false<test_logical_false>`, :ref:`logical_true<test_logical_true>`, :ref:`logical_identity<test_logical_identity>` and :ref:`logical_negation<test_logical_negation>` are already simple

* :ref:`contradiction<test_contradiction>` returns :ref:`False<test_what_is_false>` in 4 cases, with 2 inputs there are only 4 cases. I add a `return statement`_

  .. code-block:: python
    :lineno-start: 85
    :emphasize-lines: 2

    def contradiction(x, y):
        return False
        if (x, y) == (True, True): return False
        if (x, y) == (True, False): return False
        if (x, y) == (False, True): return False
        if (x, y) == (False, False): return False
        return x, y

  the test is still green. I remove the other lines in the :ref:`function<functions>`

  .. code-block:: python
    :lineno-start: 85

    def contradiction(x, y):
        return False


    def logical_negation(x):
        return not x

* :ref:`converse_implication<test_converse_implication>` returns :ref:`False<test_what_is_false>` in only one case, I return the :ref:`logical negation<test_logical_negation>` of the `if statement`_, for the 3 cases that return :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 2

    def converse_implication(x, y):
        return (x, y) != (False, True)
        if (x, y) == (False, True): return False
        return x, y

  still green. I remove the other statements

  .. code-block:: python
    :lineno-start: 80

    def converse_implication(x, y):
        return (x, y) != (False, True)


    def contradiction(x, y):
        return False

* :ref:`converse_non_implication<test_converse_non_implication>` has only one case that returns :ref:`True<test_what_is_true>`, it is the missing case. I add a `return statement`_ for it

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 2

    def converse_non_implication(x, y):
        return (x, y) == (False, True)
        if (x, y) == (True, True): return False
        if (x, y) == (True, False): return False
        if (x, y) == (False, False): return False
        return x, y

  the terminal_ still shows green and I remove the other lines

  .. code-block:: python
    :lineno-start: 73

    def converse_non_implication(x, y):
        return (x, y) == (False, True)


    def converse_implication(x, y):
        return (x, y) != (False, True)

* :ref:`exclusive_disjunction<test_exclusive_disjunction>` has two `if statements`_ I can put them together as one

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 2

    def exclusive_disjunction(x, y):
        if (x, y) == (True, True) or (x, y) == (False, False): return False
        if (x, y) == (True, True): return False
        if (x, y) == (False, False): return False
        return x, y

  the test is still green. I remove the other `if statements`_ then return the :ref:`logical negation<test_logical_negation>`

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 2

    def exclusive_disjunction(x, y):
        return (x, y) != (True, True) and (x, y) != (False, False)
        if (x, y) == (True, True) or (x, y) == (False, False): return False
        return x, y

  the test is still green, I remove the other lines

  .. code-block:: python
    :lineno-start: 67

    def exclusive_disjunction(x, y):
        return (x, y) != (True, True) and (x, y) != (False, False)


    def converse_non_implication(x, y):
        return (x, y) == (False, True)

* :ref:`logical_conjunction<test_logical_conjunction>` only has one case that returns :ref:`True<test_what_is_true>`, I add a `return statement` for it

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 2

    def logical_conjunction(x, y):
        return (x, y) == (True, True)
        if (x, y) == (True, False): return False
        if (x, y) == (False, True): return False
        if (x, y) == (False, False): return False
        return x, y

  still green, I remove the other statements

  .. code-block:: python
    :lineno-start: 60

    def logical_conjunction(x, y):
        return (x, y) == (True, True)


    def exclusive_disjunction(x, y):
        return (x, y) != (True, True) and (x, y) != (False, False)

* :ref:`logical_disjunction<test_logical_disjunction>` only has one case that returns :ref:`False<test_what_is_false>`, I add a `return statement`_ for the opposite of it which covers the other 3 cases

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 2

    def logical_disjunction(x, y):
        return (x, y) != (False, False)
        if (x, y) == (False, False): return False
        return x, y

  the terminal_ still shows green, and I remove the other lines

  .. code-block:: python
    :lineno-start: 55

    def logical_disjunction(x, y):
        return (x, y) != (False, False)


    def logical_conjunction(x, y):
        return (x, y) == (True, True)

* :ref:`logical_equality<test_logical_equality>` has two `if statements`_, I use what I know from :ref:`exclusive_disjunction<test_exclusive_disjunction>` to add a `return statement`

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2

    def logical_equality(x, y):
        return (x, y) != (True, False) and (x, y) != (False, True)
        if (x, y) == (True, False): return False
        if (x, y) == (False, True): return False
        return x, y

  the terminal_ still shows green. I remove the other lines

  .. code-block:: python
    :lineno-start: 49

    def logical_equality(x, y):
        return (x, y) != (True, False) and (x, y) != (False, True)


    def logical_disjunction(x, y):
        return (x, y) != (False, False)

* :ref:`logical_nand<test_logical_nand>` only has one case that returns :ref:`False<test_what_is_false>`, I add a `return statement`_ for its opposite which covers the other 3 cases

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 2

    def logical_nand(x, y):
        return (x, y) != (True, True)
        if (x, y) == (True, True): return False
        return x, y

  still green. I remove the other lines

  .. code-block:: python
    :lineno-start: 44

    def logical_nand(x, y):
        return (x, y) != (True, True)


    def logical_equality(x, y):
        return (x, y) != (True, False) and (x, y) != (False, True)

* :ref:`logical_nor<test_logical_nor>` only has one case that returns :ref:`True<test_what_is_true>`, I add a `return statement`_ for it

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2

    def logical_nor(x, y):
        return (x, y) == (False, False)
        if (x, y) == (True, True): return False
        if (x, y) == (True, False): return False
        if (x, y) == (False, True): return False
        return x, y

  still green, I remove the other statements

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2

    def logical_nor(x, y):
        return (x, y) == (False, False)


    def logical_nand(x, y):
        return (x, y) != (True, True)

* :ref:`material_implication<test_material_implication>` has only one case that returns :ref:`False<test_what_is_false>`, I add a `return statement`_ for the other 3

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 2

    def material_implication(x, y):
        return (x, y) != (True, False)
        if (x, y) == (True, False): return False
        return x, y

  the test is still green. I remove the other statements

  .. code-block:: python
    :lineno-start: 25

    def material_implication(x, y):
        return (x, y) != (True, False)


    def logical_nor(x, y):
        return (x, y) == (False, False)

* :ref:`material_non_implication<test_material_non_implication>` has 3 cases that return :ref:`False<test_what_is_false>`. I add a `return statement`_ for the 1 case that returns :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 2

    def material_non_implication(x, y):
        return (x, y) == (True, False)
        if (x, y) == (True, True): return False
        if (x, y) == (False, True): return False
        if (x, y) == (False, False): return False
        return x, y

  the terminal_ still shows green. I remove the other statements

  .. code-block:: python
    :lineno-start: 25

    def material_non_implication(x, y):
        return (x, y) == (True, False)


    def material_implication(x, y):
        return (x, y) != (True, False)

* ``x`` is :ref:`True<test_what_is_true>` in the 2 cases where :ref:`negate_first<test_negate_first>` returns :ref:`False<test_what_is_false>`, I add an `if statement`_ for them

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 2

    def negate_first(x, y):
        if x == True: return False
        if (x, y) == (True, True): return False
        if (x, y) == (True, False): return False
        return x, y

  the test is still green.  I add a simpler `return statement`_

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 2

    def negate_first(x, y):
        return x != True
        if x == True: return False
        return x, y

  the test is still green, I remove the other statements

  .. code-block:: python
    :lineno-start: 19

    def negate_first(x, y):
        return x != True


    def material_non_implication(x, y):
        return (x, y) == (True, False)

* ``y`` is :ref:`True<test_what_is_true>` in the 2 cases where :ref:`negate_second<test_negate_second>` returns :ref:`False<test_what_is_false>`. I add a `return statement`_ like the one from :ref:`negate_first<test_negate_first>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

    def negate_second(x, y):
        return y != True
        if (x, y) == (True, True): return False
        if (x, y) == (False, True): return False
        return x, y

  still green. I remove the other statements

  .. code-block:: python
    :lineno-start: 13

    def negate_second(x, y):
        return y != True


    def negate_first(x, y):
        return x != True

* :ref:`project_second<test_project_second>`, :ref:`project_first<test_project_first>` and :ref:`tautology<test_tautology>` are already simple

* I change the `return statement`_ in :ref:`negate_second<test_negate_second>` to make it simpler

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

    def negate_second(x, y):
        return not y == True
        return y != True

  when ``not y`` is :ref:`True<test_what_is_true>` it means the `return statement` will be ``True == True`` which is a duplication. I remove the second part of the statement and the second `return statement`_

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

    def negate_second(x, y):
        return not y


    def negate_first(x, y):

  the test is still green

* I do the same thing with :ref:`negate_first<test_negate_first>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 2

    def negate_first(x, y):
        return not x
        return x != True

  still green. I remove the second `return statement`_

  .. code-block:: python
      :lineno-start: 17

      def negate_first(x, y):
          return not x


      def material_non_implication(x, y):

* I use this with :ref:`material_non_implication<test_material_non_implication>`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2

    def material_non_implication(x, y):
        return x and not y
        return (x, y) == (True, False)

  the terminal_ shows all tests are still passing. I remove the second `return statement`_

  .. code-block:: python
    :lineno-start: 21

    def material_non_implication(x, y):
        return x and not y


    def material_implication(x, y):

* I try it with :ref:`material_implication<test_material_implication>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 2

    def material_implication(x, y):
        return not x and y
        return (x, y) != (True, False)

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: False is not true

  I change "and_" to "or_"

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 2

    def material_implication(x, y):
        return not x or y
        return (x, y) != (True, False)

  the test is green again, I will use "or_" the next time I see ``!=`` in these tests. I remove the other `return statement`_

  .. code-block:: python
    :lineno-start: 25

    def material_implication(x, y):
        return not x or y


    def logical_nor(x, y):

* I do the same thing with :ref:`logical_nor<test_logical_nor>`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2

    def logical_nor(x, y):
        return not x and not y
        return (x, y) == (False, False)

  the test is still green. I remove the second `return statement`_ and change the first `return statement`_ in terms of "not_" since it happens 2 times

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2

    def logical_nor(x, y):
        return not x not or not y
        return not x and not y

  the terminal_ shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  I comment the line out then factor out "not_"

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2-3

    def logical_nor(x, y):
        return not (x or y)
        # return not x not or not y
        return not x and not y

  the terminal_ still shows green. I remove the other statements

  .. code-block:: python
    :lineno-start: 29

    def logical_nor(x, y):
        return not (x or y)


    def logical_nand(x, y):

* I add a `return statement`_ to :ref:`logical_nand<test_logical_nand>`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2

    def logical_nand(x, y):
        return not x or not y
        return (x, y) != (True, True)

  the test is still green, I factor out "not_"

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2

    def logical_nand(x, y):
        return not (x and y)
        return not x or not y
        return (x, y) != (True, True)

  still green. I remove the other `return statements`_

  .. code-block:: python
    :lineno-start: 33

    def logical_nand(x, y):
        return not (x and y)


    def logical_equality(x, y):

* I add a `return statement`_ to :ref:`logical_equality<test_logical_equality>`

  .. code-block:: python

    def logical_equality(x, y):
        return (not x or y) and (x or not y)
        return (x, y) != (True, False) and (x, y) != (False, True)

  the test is still green, I remove the other `return statement`_

  .. code-block:: python
    :lineno-start: 37

    def logical_equality(x, y):
        return (not x or y) and (x or not y)


    def logical_disjunction(x, y):

* :ref:`logical_disjunction<test_logical_disjunction>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 2

    def logical_disjunction(x, y):
        return x or y
        return (x, y) != (False, False)

  still green. I remove the other `return statement`_

  .. code-block:: python
    :lineno-start: 41

    def logical_disjunction(x, y):
        return x or y


    def logical_conjunction(x, y):

* :ref:`logical_conjunction<test_logical_conjunction>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2

    def logical_conjunction(x, y):
        return x and y
        return (x, y) == (True, True)

  the terminal_ still shows green. I remove the other `return statement`_

  .. code-block:: python
    :lineno-start: 45

    def logical_conjunction(x, y):
        return x and y


    def exclusive_disjunction(x, y):

* I add a `return statement` to :ref:`exclusive_disjunction<test_exclusive_disjunction>`

  .. code-block:: python
    :lineno-start: 49

    def exclusive_disjunction(x, y):
        return (not x or not y) and (x or y)
        return (x, y) != (True, True) and (x, y) != (False, False)

  still green, I can factor out "not_" from the first part of the statement

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2

    def exclusive_disjunction(x, y):
        return not (x and y) and (x or y)
        return (not x or not y) and (x or y)
        return (x, y) != (True, True) and (x, y) != (False, False)

  the test is still green. I remove the other statements

  .. code-block:: python
    :lineno-start: 49

    def exclusive_disjunction(x, y):
        return not (x and y) and (x or y)


    def converse_non_implication(x, y):

* I do the same thing to :ref:`converse_non_implication<test_converse_non_implication>`

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 2

    def converse_non_implication(x, y):
        return not x and y
        return (x, y) == (False, True)

  still green. I remove the other line

  .. code-block:: python
    :lineno-start: 53

    def converse_non_implication(x, y):
        return not x and y


    def converse_implication(x, y):

* time for :ref:`converse_implication<test_converse_implication>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 2

    def converse_implication(x, y):
        return x or not y
        return (x, y) != (False, True)

  I remove the second `return statement`_

  .. code-block:: python
    :lineno-start: 57

    def converse_implication(x, y):
        return x or not y


    def contradiction(x, y):

all the tests are still passing

*********************************************************************************
review
*********************************************************************************

I ran tests using :ref:`booleans` which can be :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>` for the operations of the `Truth Table`_ from Mathematics

* there are 2 :ref:`nullary operations<Nullary Operations>`, they do not take input and always return the same thing, they are :ref:`constant<test_constant_function>`

  - :ref:`Logical False<test_logical_false>` always returns :ref:`False<test_what_is_false>`
  - :ref:`Logical True<test_logical_true>` always returns :ref:`True<test_what_is_true>`

* there are 2 :ref:`unary operations<Unary Operations>`, they take one input

  - :ref:`Logical Identity<test_logical_identity>` returns its input as output
  - :ref:`Logical Negation<test_logical_negation>` returns the negation of its input as output

* there are 16 binary operations, they each take 2 inputs, in this case I named the second input ``y`` and the first one ``x``

  - :ref:`Contradiction<test_contradiction>` always returns :ref:`False<test_what_is_false>`
  - :ref:`Converse Implication<test_converse_implication>` returns ``x or not y``
  - :ref:`Converse NonImplication<test_converse_non_implication>` returns ``not x and y``
  - :ref:`Exclusive Disjunction<test_exclusive_disjunction>` returns ``not (x and y) and (x or y)``
  - :ref:`Logical Conjunction<test_logical_conjunction>` returns ``x and y``
  - :ref:`Logical Disjunction<test_logical_disjunction>` returns ``x or y``
  - :ref:`Logical Equality<test_logical_equality>` returns ``(not x or y) and (x or not y)``
  - :ref:`Logical NAND<test_logical_nand>` returns ``not (x and y)``
  - :ref:`Logical NOR<test_logical_nor>` returns ``not (x or y)``
  - :ref:`Material Implication<test_material_implication>` returns ``not x or y``
  - :ref:`Material NonImplication <test_material_non_implication>` returns ``x and not y``
  - :ref:`Negate First<test_negate_first>` always returns ``not x``
  - :ref:`Negate Second<test_negate_second>` always returns ``not y``
  - :ref:`Project First<test_project_first>` always returns ``x``
  - :ref:`Project Second<test_project_second>` always returns ``y``
  - :ref:`Tautology<test_tautology>` always returns :ref:`True<test_what_is_true>`

and

* :ref:`Logical Disjunction <test_logical_disjunction>` is "or_"
* :ref:`Logical Conjunction <test_logical_conjunction>` is "and_"
* :ref:`Logical Negation <test_logical_negation>` is "not_"

Would you like to :ref:`test making a calculator?<how to make a calculator>`

----

:ref:`Click Here for the code for the Truth Table tests and solutions<truth table: tests and solutions>`

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">Click Here to leave a 5 star review on TrustPilot, if you found this helpful</a>
  </div>
  <!-- End TrustBox widget -->