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

    def tautoy(x, y):
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

  I change the `return statement`_ to return the second input because it is the same as the expectation

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

  the first input matches the expectation, I remove the second input from the `return statement`_

  .. code-block:: python

    def project_first(x, y):
        return x

  the name is a clue

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
        return not a

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I change the `return statement`_

  .. code-block:: python

    def material_non_implication(x, y):
        return False

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I return the inputs

  .. code-block:: python

    def material_non_implication(x, y):
        return x, y
        return False

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, True) is not false

  this test also expects :ref:`True<test_what_is_true>` in some cases and :ref:`False<test_what_is_false>` in others. I add an `if statement`_

  .. code-block:: python

    def material_non_implication(x, y):
        if a == True and b == True:
            return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, True) is not false

  I add another `if statement`_

  .. code-block:: python

    def material_non_implication(x, y):
        if a == False and b == True:
            return False
        if a == True and b == True:
            return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, False) is not false

  I add another `if statement`_

  .. code-block:: python

    def material_non_implication(x, y):
        if a == False and b == False:
            return False
        if a == False and b == True:
            return False
        if a == True and b == True:
            return False
        return x, y

* I get the next :ref:`AttributeError`

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
        if a == True and b == False:
            return False
        return x, y

* I get the next :ref:`AttributeError`

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
        if a == True and b == True:
            return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, False) is not false

  I add another `if statement`_

  .. code-block:: python

    def logical_nor(x, y):
        if a == True and b == False:
            return False
        if a == True and b == True:
            return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, True) is not false

  I add another `if statement`_

  .. code-block:: python

    def logical_nor(x, y):
        if a == False and b == True:
            return False
        if a == True and b == False:
            return False
        if a == True and b == True:
            return False
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
        if a == True and b == True:
            return False
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
        if a == True and b == False:
            return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, True) is not false

  I add another `if statement`_

  .. code-block:: python

    def logical_equality(x, y):
        if a == False and b == True:
            return False
        if a == True and b == False:
            return False
        return x, y

* another :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'logical_disjunction'. Did you mean: 'logical_implication'?

  I add a :ref:`function<functions>`

  .. code-block:: python

    def logical_disjunction(x, y):
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, False) is not false

  I add an `if statement`_

  .. code-block:: python

    def logical_disjunction(x, y):
        if a == False and b == False:
            return False
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
        if a == True and b == False:
            return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, True) is not false

  I add another `if statement`_

  .. code-block:: python

    def logical_conjunction(x, y):
        if a == False and b == True:
            return False
        if a == True and b == False:
            return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, False) is not false

  I add an `if statement`_

  .. code-block:: python

    def logical_conjunction(x, y):
        if a == False and b == False:
            return False
        if a == False and b == True:
            return False
        if a == True and b == False:
            return False
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
        if a == True and b == True:
            return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, False) is not false

  I add another `if statement`_

  .. code-block:: python

    def exclusive_disjunction(x, y):
        if a == False and b == False:
            return False
        if a == True and b == True:
            return False
        return x, y

* next :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'converse_non_implication'. Did you mean: 'material_non_implication'?

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
        if a == True and b == True:
            return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, True) is not false

  I add another `if statement`_

  .. code-block:: python

    def material_non_implication(x, y):
        if a == False and b == True:
            return False
        if a == True and b == True:
            return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, False) is not false

  I add an `if statement`_

  .. code-block:: python

    def material_non_implication(x, y):
        if a == False and b == False:
            return False
        if a == False and b == True:
            return False
        if a == True and b == True:
            return False
        return x, y

* I have the next :ref:`AttributeError`

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
        if a == True and b == True:
            return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, False) is not false

  I add another `if statement`_

  .. code-block:: python

    def converse_non_implication(x, y):
        if a == True and b == False:
            return False
        if a == True and b == True:
            return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, False) is not false

  I add a new `if statement`_

  .. code-block:: python

    def converse_non_implication(x, y):
        if a == False and b == False:
            return False
        if a == True and b == False:
            return False
        if a == True and b == True:
            return False
        return x, y

* the terminal shows :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'converse_implication'. Did you mean: 'converse_non_implication'?

  I add a :ref:`function<functions>`

  .. code-block:: python

    def converse_non_implication(x, y):
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, True) is not false

  I add an `if statement`_

  .. code-block:: python

    def converse_non_implication(x, y):
        if a == True and b == True:
            return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, False) is not false

  I add an `if statement`_

  .. code-block:: python

    def converse_non_implication(x, y):
        if a == True and b == False:
            return False
        if a == True and b == True:
            return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, False) is not false

  I add another `if statement`_

  .. code-block:: python

    def converse_non_implication(x, y):
        if a == False and b == False:
            return False
        if a == True and b == False:
            return False
        if a == True and b == True:
            return False
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
        if a == False and b == True:
            return False
        return x, y

* the next :ref:`AttributeError`

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
        if a == True and b == True:
            return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, False) is not false

  I add another `if statement`_

  .. code-block:: python

    def contradiction(x, y):
        if a == True and b == False:
            return False
        if a == True and b == True:
            return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, True) is not false

  I add another `if statement`

  .. code-block:: python

    def contradiction(x, y):
        if a == False and b == True:
            return False
        if a == True and b == False:
            return False
        if a == True and b == True:
            return False
        return x, y

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, False) is not false

  I add an `if statement`_

  .. code-block:: python

    def contradiction(x, y):
        if a == False and b == False:
            return False
        if a == False and b == True:
            return False
        if a == True and b == False:
            return False
        if a == True and b == True:
            return False
        return x, y

* another :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'logical_negation'. Did you mean: 'logical_conjunction'?

  I add the :ref:`function<functions>`

  .. code-block:: python

    def logical_negation(x, y):
        return x, y

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: logical_negation() missing 1 required positional argument: 'b'

  I change the signature

  .. code-block:: python

    def logical_negation(a):
        return (a, )

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True,) is not false

  ah, it expects the opposite. I change the `return statement`_ with not_

  .. code-block:: python

    def logical_negation(a):
        return not a

* The terminal shows :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'logical_identity'. Did you mean: 'logical_equality'?

  I add a :ref:`function<functions>`

  .. code-block:: python

    def logical_identity(a):
        return (a,)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, ) is not false

  okay, the input and output are the same, I change the `return statement`_

  .. code-block:: python

    def logical_identity(a):
        return a

* the next :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'logical_true'. Did you mean: 'logical_nand'?

  I add the :ref:`function<functions>`

  .. code-block:: python

    def logical_true(a):
        return a

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: logical_true() missing 1 required positional argument: 'a'

  I remove the input parameter

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
        return True

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the `return statement`_

  .. code-block:: python

    def logical_false():
        return False

  the terminal shows green!

refactor: make it better
#################################################################################

This is your part. See if you can refactor each operation to a `conditional expression`_. Good Luck!


*********************************************************************************
review
*********************************************************************************

I ran tests for the operations of the `Truth Table`_ involving booleans_ which can either be :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`

* :ref:`Contradiction <test_contradiction>` always returns :ref:`False<test_what_is_false>`
* :ref:`Tautology <test_tautology>` always returns :ref:`True<test_what_is_true>`
* :ref:`Negate Second <test_negate_second>` always returns ``not q``
* :ref:`Project Second <test_project_second>` always returns ``q``
* :ref:`Negate First<test_negate_first>` always returns ``not p``
* :ref:`Project First <test_project_first>` always returns ``p``
* :ref:`Exclusive Disjunction <test_exclusive_disjunction>` is ``!=``, or the :ref:`Logical Negation<test_logical_negation>` of :ref:`Logical Equality <test_logical_equality>`
* :ref:`Logical Equality <test_logical_equality>` is ``==``
* :ref:`Converse NonImplication <test_converse_non_implication>` returns ``not p and q``
*  :ref:`Converse Implication <test_converse_implication>` returns ``p or not q``
* :ref:`Material NonImplication <test_material_non_implication>` returns ``p and not q``
* :ref:`Logical or Material Implication  <test_material_implication>` returns ``not p or q``
* :ref:`Logical NOR <test_logical_nor>` returns ``not (p or q)``
* :ref:`Logical Disjunction <test_logical_disjunction>` returns ``p or q``
* :ref:`Logical NAND <test_logical_nand>` returns ``not (p and q)``
* :ref:`Logical Conjunction <test_logical_conjunction>` returns ``p and q``
* :ref:`Logical Negation<test_logical_negation>` is not_
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