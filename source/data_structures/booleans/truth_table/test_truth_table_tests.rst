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

* :ref:`Binary Operations part 1<truth table: Binary Operations part 1>`
* :ref:`Binary Operations part 2<truth table: Binary Operations part 2>`
* :ref:`Binary Operations part 3<truth table: Binary Operations part 3>`
* :ref:`Binary Operations part 4<truth table: Binary Operations part 4>`

----

I want to write a program that makes the tests in ``test_truth_table.py`` pass without looking at them

*********************************************************************************
red: make it fail
*********************************************************************************

* I close ``test_truth_table.py``
* then delete all the tests in ``truth_table.py``, which gives 20 failures, I start with the last one

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

  the terminal shows :ref:`TypeError`

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

* the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.truth_table' has no attribute 'project_second'

  I add the :ref:`function<functions>`

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

  I return the inputs to see the difference between them and the expected output

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

* another :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.truth_table' has no attribute 'negate_second'

  I add the :ref:`function<functions>`

  .. code-block:: python

    def negate_second(x, y):
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, True) is not false

  I add an `if statement`_

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

  ``y`` is :ref:`True<test_what_is_true>` in 2 cases

* :ref:`AttributeError`

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

  ``x`` is :ref:`True<test_what_is_true>` in 2 cases

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

  I add an `if statement`_ for it

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

  I add another `if statement`_

  .. code-block:: python

    def logical_nor(x, y):
        if (x, y) == (True, True): return False
        if (x, y) == (True, False): return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, True) is not false

  I add an `if statement`_

  .. code-block:: python

    def logical_nor(x, y):
        if (x, y) == (True, True): return False
        if (x, y) == (True, False): return False
        if (x, y) == (False, True): return False
        return x, y

* the terminal shows :ref:`AttributeError`

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

* :ref:`AttributeError`

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

* :ref:`AttributeError`

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

* the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.truth_table' has no attribute 'exclusive_disjunction

  I add a :ref:`function<functions>` for it

  .. code-block:: python

    def exclusive_disjunction(x, y):
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, True) is not false

  I add an `if statement`_

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

* :ref:`AttributeError`

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

* the terminal shows :ref:`AttributeError`

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

* the terminal shows :ref:`AttributeError`

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

  I add an `if statement`_

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

  I add "not_" to the `return statement`_

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
        return not x

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I remove "not_"

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

* the terminal shows :ref:`AttributeError`

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

* :ref:`logical_false<test_logical_false>`, :ref:`logical_true<test_logical_true>`, :ref:`logical_identity<test_logical_identity>` and :ref:`logical_negation<test_logical_negation>` are already simple

* :ref:`contradiction<test_contradiction>` returns :ref:`False<test_what_is_false>` in 4 cases and with 2 inputs there are only 4 cases. I  add a `return statement`_

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

* :ref:`converse_implication<test_converse_implication>` returns :ref:`False<test_what_is_false>` in only one case, I return the :ref:`logical negation<test_logical_negation>` of the `if statement`_, for the 3 cases that return :ref:`True<test_what_is_true>`

  .. code-block:: python

    def converse_implication(x, y):
        return (x, y) != (False, True)
        if (x, y) == (False, True): return False
        return x, y

  still green. I remove the other statements

  .. code-block:: python

    def converse_implication(x, y):
        return (x, y) != (False, True)

* :ref:`converse_non_implication<test_converse_non_implication>` has only one case that returns :ref:`True<test_what_is_true>`, it is the missing case. I add a `return statement`_ for it

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

* :ref:`exclusive_disjunction<test_exclusive_disjunction>` has two `if statements`_ I can put them together

  .. code-block:: python

    def exclusive_disjunction(x, y):
        if (x, y) == (True, True) or (x, y) == (False, False): return False
        if (x, y) == (True, True): return False
        if (x, y) == (False, False): return False
        return x, y

  the test is still green. I remove the other `if statements`_ then return the :ref:`logical negation<test_logical_negation>`

  .. code-block:: python

    def exclusive_disjunction(x, y):
        return (x, y) != (True, True) and (x, y) != (False, False)
        if (x, y) == (True, True) or (x, y) == (False, False): return False
        return x, y

  the test is still green again, I remove the other statements

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

* :ref:`logical_equality<test_logical_equality>` has two `if statements`_, I use what I know from :ref:`Exclusive Disjunction<test_exclusive_disjunction>`

  .. code-block:: python

    def logical_equality(x, y):
        return (x, y) != (True, False) and (x, y) != (False, True)

  the terminal still shows green

* :ref:`logical_nand<test_logical_nand>` only has one case that returns :ref:`False<test_what_is_false>`

  .. code-block:: python

    def logical_nand(x, y):
        return (x, y) != (True, True)

  still green

* :ref:`logical_nor<test_logical_nor>` only has one case that returns :ref:`True<test_what_is_true>`

  .. code-block:: python

    def logical_nor(x, y):
        return (x, y) == (False, False)

* :ref:`material_implication<test_material_implication>` has only case that returns :ref:`False<test_what_is_false>`

  .. code-block:: python

    def material_non_implication(x, y):
        return (x, y) == (True, False)

* :ref:`material_non_implication<test_material_non_implication>` has 3 cases that return :ref:`False<test_what_is_false>`

  .. code-block:: python

    def material_implication(x, y):
        return (x, y) != (True, False)

* ``x`` is :ref:`True<test_what_is_true>` in both cases of :ref:`negate_first<test_negate_first>` that return :ref:`False<test_what_is_false>`, I add an `if statement`_ to show this

  .. code-block:: python

    def negate_first(x, y):
        if x == True: return False
        if (x, y) == (True, True): return False
        if (x, y) == (True, False): return False
        return x, y

  the test is still green.  I add a `return statement`_

  .. code-block:: python

    def negate_first(x, y):
        return x != True
        if x == True: return False
        return x, y

  still green, I remove the other statements

  .. code-block:: python

    def negate_first(x, y):
        return x != True

* ``y`` is :ref:`True<test_what_is_true>` in the 2 cases that return :ref:`False<test_what_is_false>` in :ref:`negate_second<test_negate_second>`. I add a `return statement`_ like the one from :ref:`Negate First<test_negate_first>`

  .. code-block:: python

    def negate_second(x, y):
        return y != True

  still green

* :ref:`project_second<test_project_second>`, :ref:`project_first<test_project_first>` and :ref:`tautology<test_tautology>` are already simple

* I change the `return statement`_ in :ref:`negate_second<test_negate_second>`

  .. code-block:: python

    def negate_second(x, y):
        return not y == True
        return y != True

  when ``not y`` is :ref:`True<test_what_is_true>` this statement will be a duplication - ``True == True``, I remove the second part of the statement

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

  I change "and_" to

  .. code-block:: python

    def material_implication(x, y):
        return not x or y

  the test is green again, I will use "or_" when I see ``!=``

* I do it with :ref:`logical_nor<test_logical_nor>`

  .. code-block:: python

    def logical_nor(x, y):
        return not x and not y

  then rewrite the `return statement`_ in terms of "not_" since it happens 2 times

  .. code-block:: python

    def logical_nor(x, y):
        return not x not or not y
        return not x and not y

  the terminal shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  I comment the line out then factor out "not_"

  .. code-block:: python

    def logical_nor(x, y):
        return not (x or y)
        # return not x not or not y
        return not x and not y

  the terminal still shows green. I remove the other statements

  .. code-block:: python

    def logical_nor(x, y):
        return not (x or y)

* I add a `return statement`_ for :ref:`logical_nand<test_logical_nand>`

  .. code-block:: python

    def logical_nand(x, y):
        return not x or not y

  still green and it factors to

  .. code-block:: python

    def logical_nand(x, y):
        return not (x and y)

* :ref:`logical_equality<test_logical_equality>`

  .. code-block:: python

    def logical_equality(x, y):
        return (not x or y) and (x or not y)
        return (x, y) != (True, False) and (x, y) != (False, True)

  the test is still green, I remove the other statement

* :ref:`logical_disjunction<test_logical_disjunction>`

  .. code-block:: python

    def logical_disjunction(x, y):
        return x or y

* :ref:`logical_conjunction<test_logical_conjunction>`

  .. code-block:: python

    def logical_conjunction(x, y):
        return x and y

* :ref:`exclusive_disjunction<test_exclusive_disjunction>` has 2 conditions

  .. code-block:: python

    def exclusive_disjunction(x, y):
        return (not x or not y) and (x or y)
        return (x, y) != (True, True) and (x, y) != (False, False)

  still green, I can factor out "not_" from the first part of the statement

  .. code-block:: python

    def exclusive_disjunction(x, y):
        return not (x and y) and (x or y)
        return (not x or not y) and (x or y)

  the test is still green. I remove the other statement

* :ref:`converse_non_implication<test_converse_non_implication>`

  .. code-block:: python

    def converse_non_implication(x, y):
        return not x and y

* :ref:`converse_implication<test_converse_implication>`

  .. code-block:: python

    def converse_implication(x, y):
        return x or not y

all the tests are still passing

*********************************************************************************
review
*********************************************************************************

I ran tests for the operations of the `Truth Table`_ involving booleans_ which can be :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`

* :ref:`Logical False<test_logical_false>` always returns :ref:`False<test_what_is_false>` it is a :ref:`nullary operation<Nullary Operations>`, it does not take input
* :ref:`Logical True<test_logical_true>` always returns :ref:`True<test_what_is_true>` is also :ref:`nullary<Nullary Operations>`
* :ref:`Logical Identity<test_logical_identity>` returns what it receives and only takes one input, it is a :ref:`unary operation<Unary Operations>`
* :ref:`Logical Negation<test_logical_negation>` returns the negation of its input, it is also :ref:`unary<Unary Operations>`

:ref:`Contradiction<test_contradiction>` to :ref:`Tautology<test_tautology>` are binary operations which take in 2 inputs, in this case I named the first one ``x`` and the second one ``y``

* :ref:`Contradiction<test_contradiction>` always returns :ref:`False<test_what_is_false>`
* :ref:`Converse Implication<test_converse_implication>` returns ``x or not y``
* :ref:`Converse NonImplication<test_converse_non_implication>` returns ``not x and y``
* :ref:`Exclusive Disjunction<test_exclusive_disjunction>` returns ``not (x and y) and (x or y)``
* :ref:`Logical Conjunction<test_logical_conjunction>` returns ``x and y``
* :ref:`Logical Disjunction<test_logical_disjunction>` returns ``x or y``
* :ref:`Logical Equality<test_logical_equality>` returns ``(not x or y) and (x or not y)``
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

* not_ :ref:`False<test_what_is_false>` is :ref:`True<test_what_is_true>`
* not_ :ref:`True<test_what_is_true>` is :ref:`False<test_what_is_false>`
* :ref:`False<test_what_is_false>` is :ref:`False<test_what_is_false>`
* :ref:`True<test_what_is_true>` is :ref:`True<test_what_is_true>`
* :ref:`True<test_what_is_true>` and :ref:`False<test_what_is_false>` are booleans_

Would you like to :doc:`test lists?</data_structures/lists/lists>`

----

:doc:`/code/code_truth_table`