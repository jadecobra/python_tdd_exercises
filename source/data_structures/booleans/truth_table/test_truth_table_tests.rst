.. include:: ../../../links.rst

.. _test_truth_table_tests:

#################################################################################
truth table: test_truth_table_tests
#################################################################################

.. contents:: table of contents
  :local:
  :depth: 1

----

*********************************************************************************
requirements
*********************************************************************************

:doc:`how to make a python test driven development environment </how_to/make_tdd_environment>` with ``truth_table`` as the name of the project

----

I want to write a program that makes the tests in ``test_truth_table.py`` pass without looking at them

*********************************************************************************
red: make it fail
*********************************************************************************

* I close ``test_truth_table.py``
* then delete all the test in ``truth_table.py``, which gives me a list of :ref:`AttributeErrors<AttributeError>` I start with the last one

  .. code-block:: python

    AttributeError: module 'src.truth_table' has no attribute 'tautology'

*********************************************************************************
green: make it pass
*********************************************************************************

* I add the name

  .. code-block:: python

    tautology

  the terminal shows NameError_

  .. code-block:: python

    NameError: name 'tautology' is not defined

  I point it to :ref:`None`

  .. code-block:: python

    tautology = None

  which gives me :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  I make it a :ref:`function<functions>`

  .. code-block:: python

    def tautology():
        return None

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: tautology() takes 0 positional arguments but 2 were given

  I add input arguments in the :ref:`function<functions>` definition

  .. code-block:: python

    def tautology(x, y):
        return None

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None is not true

  I change :ref:`None` to :ref:`True<test_what_is_true>` in the `return statement`_

  .. code-block:: python

    def tautology(x, y):
        return True

* I have another :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.truth_table' has no attribute 'project_second'

  I add a :ref:`function<functions>`

  .. code-block:: python

    def project_second(x, y):
        return True

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I change the `return statement`_

  .. code-block:: python

    def project_second(x, y):
        return False

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  this test expects :ref:`False<test_what_is_false>` sometimes and :ref:`True<test_what_is_true>` other times. I return the inputs instead

  .. code-block:: python

    def project_second(x, y):
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, False) is not false

  ``y`` is :ref:`False<test_what_is_false>`, I remove ``x``

  .. code-block:: python

    def project_second(x, y):
        return y

* the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.truth_table' has no attribute 'project_first'

  I add the :ref:`function<functions>`

  .. code-block:: python

    def project_first(x, y):
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, True) is not false

  ``x`` is :ref:`False<test_what_is_false>`, I remove ``y``

  .. code-block:: python

    def project_first(x, y):
        return x

* there is another :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.truth_table' has no attribute 'negate_second'

  I add the :ref:`function<functions>`

  .. code-block:: python

    def negate_second(x, y):
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, True) is not false

  I do not know how the input relates to the output so I add an `if statement`_

  .. code-block:: python

    def negate_second(x, y):
        if (x, y) == (True, True): return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, True) is not false

  I add another `if statement`_

  .. code-block:: python

    def negate_second(x, y):
        if (x, y) == (True, True): return False
        if (x, y) == (False, True): return False
        return x, y

* I get :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.truth_table' has no attribute 'negate_first'

  I add a definition for it

  .. code-block:: python

    def negate_first(x, y):
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, True)

  I add an `if statement`_

  .. code-block:: python

    def negate_first(x, y):
        if (x, y) == (True, True): return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, False) is not false

  I add an `if statement`_ for it

  .. code-block:: python

    def negate_first(x, y):
        if (x, y) == (True, True): return False
        if (x, y) == (True, False): return False
        return x, y

* the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.truth_table' has no attribute 'material_non_implication'

  I add the :ref:`function<functions>`

  .. code-block:: python

    def material_non_implication(x, y):
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, True) is not false

  I add an `if statement`_

  .. code-block:: python

    def material_non_implication(x, y):
        if (x, y) == (True, True): return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, True) is not false

  I add another `if statement`_

  .. code-block:: python

    def material_non_implication(x, y):
        if (x, y) == (True, True): return False
        if (x, y) == (False, True): return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, False) is not false

  another `if statement`_

  .. code-block:: python

    def material_non_implication(x, y):
        if (x, y) == (True, True): return False
        if (x, y) == (False, True): return False
        if (x, y) == (False, False): return False
        return x, y

* the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.truth_table' has no attribute 'material_implication'

  I add the :ref:`function<functions>`

  .. code-block:: python

    def material_implication(x, y):
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, False) is not false

  I add an `if statement`_

  .. code-block:: python

    def material_implication(x, y):
        if (x, y) == (True, False): return False
        return x, y

* I get :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.truth_table' has no attribute 'logical_nor'

  I add a definition for it

  .. code-block:: python

    def logical_nor(x, y):
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, True) is not false

  I add an `if statement`_

  .. code-block:: python

    def logical_nor(x, y):
        if (x, y) == (True, True): return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, False) is not false

  another `if statement`_

  .. code-block:: python

    def logical_nor(x, y):
        if (x, y) == (True, True): return False
        if (x, y) == (True, False): return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, True) is not false

  I add another `if statement`_

  .. code-block:: python

    def logical_nor(x, y):
        if (x, y) == (True, True): return False
        if (x, y) == (True, False): return False
        if (x, y) == (False, True): return False
        return x, y

* I get :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'logical_nand'. Did you mean: 'logical_nor'?

  I add the :ref:`function<functions>`

  .. code-block:: python

    def logical_nand(x, y):
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, True) is not false

  I add an `if statement`_

  .. code-block:: python

    def logical_nand(x, y):
        if (x, y) == (True, True): return False
        return x, y

* on to the next :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.truth_table' has no attribute 'logical_equality'

  I add the :ref:`function<functions>`

  .. code-block:: python

    def logical_equality(x, y):
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, False) is not false

  I add an `if statement`_

  .. code-block:: python

    def logical_equality(x, y):
        if (x, y) == (True, False): return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, True) is not false

  I add another `if statement`_

  .. code-block:: python

    def logical_equality(x, y):
        if (x, y) == (True, False): return False
        if (x, y) == (False, True): return False
        return x, y

* another :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'logical_disjunction'

  I add the :ref:`function<functions>`

  .. code-block:: python

    def logical_disjunction(x, y):
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, False) is not false

  I add an `if statement`_

  .. code-block:: python

    def logical_disjunction(x, y):
        if (x, y) == (False, False): return False
        return x, y

* the next :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'logical_conjunction'. Did you mean: 'logical_disjunction'?

  I add it

  .. code-block:: python

    def logical_conjunction(x, y):
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, False) is not false

  I add an `if statement`_

  .. code-block:: python

    def logical_conjunction(x, y):
        if (x, y) == (True, False): return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, True) is not false

  I add another `if statement`_

  .. code-block:: python

    def logical_conjunction(x, y):
        if (x, y) == (True, False): return False
        if (x, y) == (False, True): return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, False) is not false

  I add an `if statement`_

  .. code-block:: python

    def logical_conjunction(x, y):
        if (x, y) == (True, False): return False
        if (x, y) == (False, True): return False
        if (x, y) == (False, False): return False
        return x, y

* I get another :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.truth_table' has no attribute 'exclusive_disjunction

  I add a :ref:`function<functions>` for it

  .. code-block:: python

    def exclusive_disjunction(x, y):
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, True) is not false

  I add an `if statement`

  .. code-block:: python

    def exclusive_disjunction(x, y):
        if (x, y) == (True, True): return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, False) is not false

  I add another `if statement`_

  .. code-block:: python

    def exclusive_disjunction(x, y):
        if (x, y) == (True, True): return False
        if (x, y) == (False, False): return False
        return x, y

* next :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'converse_non_implication'. Did you mean: 'material_non_implication'?

  I add the :ref:`function<functions>`

  .. code-block:: python

    def converse_non_implication(x, y):
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, True) is not false

  I add an `if statement`_

  .. code-block:: python

    def converse_non_implication(x, y):
        if (x, y) == (True, True): return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, False) is not false

  I add another `if statement`_

  .. code-block:: python

    def converse_non_implication(x, y):
        if (x, y) == (True, True): return False
        if (x, y) == (True, False): return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, False) is not false

  I add an `if statement`_

  .. code-block:: python

    def converse_non_implication(x, y):
        if (x, y) == (True, True): return False
        if (x, y) == (True, False): return False
        if (x, y) == (False, False): return False
        return x, y

* next :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'converse_implication'. Did you mean: 'converse_non_implication'?

  I add the :ref:`function<functions>`

  .. code-block:: python

    def converse_implication(x, y):
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, True) is not false

  I add an `if statement`_

  .. code-block:: python

    def converse_implication(x, y):
        if (x, y) == (False, True): return False
        return x, y

* I get :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.truth_table' has no attribute 'contradiction'

  I add the :ref:`function<functions>`

  .. code-block:: python

    def contradiction(x, y):
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, True) is not false

  I add an `if statement`_

  .. code-block:: python

    def contradiction(x, y):
        if (x, y) == (True, True): return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, False) is not false

  I add another `if statement`_

  .. code-block:: python

    def contradiction(x, y):
        if (x, y) == (True, True): return False
        if (x, y) == (True, False): return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, True) is not false

  I add another `if statement`

  .. code-block:: python

    def contradiction(x, y):
        if (x, y) == (True, True): return False
        if (x, y) == (True, False): return False
        if (x, y) == (False, True): return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, False) is not false

  I add an `if statement`_

  .. code-block:: python

    def contradiction(x, y):
        if (x, y) == (True, True): return False
        if (x, y) == (True, False): return False
        if (x, y) == (False, True): return False
        if (x, y) == (False, False): return False
        return x, y

* the terminal shows :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'logical_negation'. Did you mean: 'logical_conjunction'?

  I add the :ref:`function<functions>`

  .. code-block:: python

    def logical_negation(x, y):
        return x, y

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: logical_negation() missing 1 required positional argument: 'x'

  I change the signature

  .. code-block:: python

    def logical_negation(x):
        return x

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  ah, it expects the opposite. I add not_ to the `return statement`_

  .. code-block:: python

    def logical_negation(x):
        return not x

* the terminal shows :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'logical_identity'. Did you mean: 'logical_equality'?

  I add a :ref:`function<functions>`

  .. code-block:: python

    def logical_identity(x):
        return x

* the terminal shows :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'logical_true'. Did you mean: 'logical_nand'?

  I add the :ref:`function<functions>`

  .. code-block:: python

    def logical_true(x):
        return x

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: logical_true() missing 1 required positional argument: 'x'

  I remove the input parameter and change the `return statement`_

  .. code-block:: python

    def logical_true():
        return None

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None is not true

  I change :ref:`None` to :ref:`True<test_what_is_true>` in the `return statement`_

  .. code-block:: python

    def logical_true():
        return True

* another :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'logical_false'. Did you mean: 'logical_nand'?

  I add the :ref:`function<functions>`

  .. code-block:: python

    def logical_false():
        return False

  the terminal shows green!

refactor: make it better
#################################################################################

Since all the tests are passing, I can refactor the :ref:`functions<functions>` to make them simpler

* :ref:`contradiction<test_contradiction>` returns :ref:`False<test_what_is_false>` in every case, I can use a simple `return statement`_

  .. code-block:: python

    def contradiction(x, y):
        return False
        if (x, y) == (True, True): return False
        if (x, y) == (True, False): return False
        if (x, y) == (False, True): return False
        if (x, y) == (False, False): return False
        return x, y

  the test is still green. I remove the other statements

  .. code-block:: python

    def contradiction(x, y):
        return False

* I use a one line `return statement`_ for :ref:`converse_implication<test_converse_implication>` to return the opposite of the `if statement`_, there is only one case that returns :ref:`False<test_what_is_false>`

  .. code-block:: python

    def converse_implication(x, y):
        return (x, y) != (False, True)
        if (x, y) == (False, True): return False
        return x, y

  still green. I remove the other statements

  .. code-block:: python

    def converse_implication(x, y):
        return (x, y) != (False, True)

* :ref:`converse_non_implication<test_converse_non_implication>` has only one case that returns :ref:`True<test_what_is_true>`, I use that

  .. code-block:: python

    def converse_non_implication(x, y):
        return (x, y) == (False, True)
        if (x, y) == (True, True): return False
        if (x, y) == (True, False): return False
        if (x, y) == (False, False): return False
        return x, y

  the terminal still shows green and I remove the other statements

  .. code-block:: python

    def converse_non_implication(x, y):
        return (x, y) == (False, True)

* :ref:`exclusive_disjunction<test_exclusive_disjunction>` has two `if statements`_ I try to combine them

  .. code-block:: python

    def exclusive_disjunction(x, y):
        return (x, y) != (True, True) or (x, y) != (False, False)
        if (x, y) == (True, True): return False
        if (x, y) == (False, False): return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  Oops! It looks like I cannot do that since this statement is the opposite of the combination of the 2 `if statements`_, I change or_ to and_

  .. code-block:: python

    def exclusive_disjunction(x, y):
        return (x, y) != (True, True) and (x, y) != (False, False)
        if (x, y) == (True, True): return False
        if (x, y) == (False, False): return False
        return x, y

  the test is green again, I remove the other statements

  .. code-block:: python

    def exclusive_disjunction(x, y):
        return (x, y) != (True, True) and (x, y) != (False, False)

* :ref:`logical_conjunction<test_logical_conjunction>` only has one case that returns :ref:`True<test_what_is_true>`

  .. code-block:: python

    def logical_conjunction(x, y):
        return (x, y) == (True, True)
        if (x, y) == (True, False): return False
        if (x, y) == (False, True): return False
        if (x, y) == (False, False): return False
        return x, y

  still green, I remove the other statements

  .. code-block:: python

    def logical_conjunction(x, y):
        return (x, y) == (True, True)

* :ref:`logical_disjunction<test_logical_disjunction>` only has one case that returns :ref:`False<test_what_is_false>`

  .. code-block:: python

    def logical_disjunction(x, y):
        return (x, y) != (False, False)

* :ref:`logical_equality<test_logical_equality>` has two `if statements`_, I put their opposites together

  .. code-block:: python

    def logical_equality(x, y):
        return (x, y) != (True, False) and (x, y) != (False, True)

  the terminal still shows green

* I use the opposite of the condition in the `if statement`_ for :ref:`logical_nand<test_logical_nand>`

  .. code-block:: python

    def logical_nand(x, y):
        return (x, y) != (True, True)

  still green

* :ref:`logical_nor<test_logical_nor>` only has one case that returns :ref:`True<test_what_is_true>`

  .. code-block:: python

    def logical_nor(x, y):
        return (x, y) == (False, False)

* :ref:`material_non_implication<test_material_non_implication>` and :ref:`material_implication<test_material_implication>`

  .. code-block:: python

    def material_non_implication(x, y):
        return (x, y) == (True, False)


    def material_implication(x, y):
        return (x, y) != (True, False)

* ``x`` is :ref:`True<test_what_is_true>` in both cases of :ref:`negate_first<test_negate_first>` that return :ref:`False<test_what_is_false>`

  .. code-block:: python

    def negate_first(x, y):
        return x != True

* ``y`` is :ref:`True<test_what_is_true>` in both cases of :ref:`negate_second<test_negate_second>` that return :ref:`False<test_what_is_false>`

  .. code-block:: python

    def negate_second(x, y):
        return y != True

  I change the `return statement`_

  .. code-block:: python

    def negate_second(x, y):
        return not y == True
        return y != True

  since ``not y`` is equal to :ref:`True<test_what_is_true>` I can remove the duplication

  .. code-block:: python

    def negate_second(x, y):
        return not y

  the test is still green

* I do the same thing with :ref:`negate_first<test_negate_first>`

  .. code-block:: python

    def negate_first(x, y):
        return not x

  still green

* I use this with :ref:`material_non_implication<test_material_non_implication>`

  .. code-block:: python

    def material_non_implication(x, y):
        return x and not y

  the terminal shows all tests are still passing

* I try it with :ref:`material_implication<test_material_implication>`

  .. code-block:: python

    def material_implication(x, y):
        return not x and y
        return (x, y) != (True, False)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I change and_ to or_

  .. code-block:: python

    def material_implication(x, y):
        return not x or y

  the test is green again, I will use or_ when I see ``!=``

* I use this with :ref:`logical_nor<test_logical_nor>`

  .. code-block:: python

    def logical_nor(x, y):
        return not x and not y

  which factors to

  .. code-block:: python

    def logical_nor(x, y):
        return not (x or y)

* :ref:`logical_nand<test_logical_nand>`

  .. code-block:: python

    def logical_nand(x, y):
        return not x or not y

  still green and it factors to

  .. code-block:: python

    def logical_nand(x, y):
        return not (x and y)

* I do it with :ref:`logical_equality<test_logical_equality>`

  .. code-block:: python

    def logical_equality(x, y):
        return (not x or y) and (x or not y)
        return (x, y) != (True, False) and (x, y) != (False, True)

  the tests are all still passing, I remove the other statement

* :ref:`logical_disjunction<test_logical_disjunction>` and :ref:`logical_conjunction<test_logical_conjunction>`

  .. code-block:: python

    def logical_disjunction(x, y):
        return x or y


    def logical_conjunction(x, y):
        return x and y

* :ref:`exclusive_disjunction<test_exclusive_disjunction>` has 2 conditions

  .. code-block:: python

    def exclusive_disjunction(x, y):
        return (not x or not y) and (x or y)
        return (x, y) != (True, True) and (x, y) != (False, False)

  still green, I can factor out not_ from the first part of the statement

  .. code-block:: python

    def exclusive_disjunction(x, y):
        return not (x and y) and (x or y)
        return (not x or not y) and (x or y)

  the test is still green. I remove the other statement

* :ref:`converse_non_implication<test_converse_non_implication>` and :ref:`converse_implication<test_converse_implication>`

  .. code-block:: python

    def converse_non_implication(x, y):
        return not x and y


    def converse_implication(x, y):
        return x or not y

all the tests are still passing

*********************************************************************************
review
*********************************************************************************

I ran tests for the operations of the `Truth Table`_ involving booleans_ which can be :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`

* :ref:`Logical False<test_logical_false>` always returns :ref:`False<test_what_is_false>` it is a nullary operation, it does not take input
* :ref:`Logical True<test_logical_true>` always returns :ref:`True<test_what_is_true>` is also nullary
* :ref:`Logical Identity<test_logical_identity>` returns what it receives and only takes one input, it is a unary operation
* :ref:`Logical Negation<test_logical_negation>` returns the negation of its input, it is also unary

:ref:`Contradiction<test_contradiction>` to :ref:`Tautology<test_tautology>` are binary operations which take in 2 inputs, in this case I named them ``x`` and ``y``

* :ref:`Contradiction<test_contradiction>` always returns :ref:`False<test_what_is_false>`
* :ref:`Converse Implication<test_converse_implication>` returns ``x or not y``
* :ref:`Converse NonImplication<test_converse_non_implication>` returns ``not x and y``
* :ref:`Exclusive Disjunction<test_exclusive_disjunction>` returns ``x != y``
* :ref:`Logical Conjunction<test_logical_conjunction>` returns ``x and y``
* :ref:`Logical Disjunction<test_logical_disjunction>` returns ``x or y``
* :ref:`Logical Equality<test_logical_equality>` returns ``x == y``
* :ref:`Logical NAND<test_logical_nand>` returns ``not (x and y)``
* :ref:`Logical NOR<test_logical_nor>` returns ``not (x or y)``
* :ref:`Material Implication<test_material_implication>` returns ``not x or y``
* :ref:`Material NonImplication <test_material_non_implication>` returns ``x and not y``
* :ref:`Negate First<test_negate_first>` always returns ``not x``
* :ref:`Negate Second<test_negate_second>` always returns ``not y``
* :ref:`Project First<test_project_first>` always returns ``x``
* :ref:`Project Second<test_project_second>` always returns ``y``
* :ref:`Tautology<test_tautology>` always returns :ref:`True<test_what_is_true>`

As a reminder

* not_ or_ is and_
* not_ and_ is or_
* not_ :ref:`False<test_what_is_false>` is :ref:`True<test_what_is_true>`
* not_ :ref:`True<test_what_is_true>` is :ref:`False<test_what_is_false>`
* :ref:`False<test_what_is_false>` is :ref:`False<test_what_is_false>`
* :ref:`True<test_what_is_true>` is :ref:`True<test_what_is_true>`
* :ref:`True<test_what_is_true>` and :ref:`False<test_what_is_false>` are booleans_

Would you like to :doc:`test lists?</data_structures/lists/lists>`

----

:doc:`/code/code_truth_table`