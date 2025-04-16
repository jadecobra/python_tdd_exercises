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

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    TypeError: tautology() takes 0 positional arguments but 2 were given

  I add input arguments in the :ref:`function<functions>` definition

  .. code-block:: python

    def tautology(a, b):
        return None

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None is not true

  I change :ref:`None` to :ref:`True<test_what_is_true>` in the `return statement`_

  .. code-block:: python

    def tautology(a, b):
        return True

* I have another :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.truth_table' has no attribute 'project_second'

  I add a :ref:`function<functions>`

  .. code-block:: python

    def project_second(a, b):
        return True

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I change the `return statement`_

  .. code-block:: python

    def project_second(a, b):
        return False
        return True

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  this test expects :ref:`False<test_what_is_false>` sometimes and :ref:`True<test_what_is_true>` other times. I return the inputs to see why

  .. code-block:: python

    def project_second(a, b):
        return (a, b)
        return False
        return True

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, False) is not false

  I change the `return statement`_ to return ``b`` since it is the same as the expectation

  .. code-block:: python

    def project_second(a, b):
        return b
        return (a, b)
        return False
        return True

  I remove the other `return statements`_

  .. code-block:: python

    def project_second(a, b):
        return b

* I have the next :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.truth_table' has no attribute 'project_first'

  I add the :ref:`function<functions>`

  .. code-block:: python

    def project_first(a, b):
        return b

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  using the name as a clue and since it worked for :ref:`project second<test_project_second>` I change the `return statement`_

  .. code-block:: python

    def project_first(a, b):
        return a

  the name is a clue

* now there is another :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.truth_table' has no attribute 'negate_second'

  I add the :ref:`function<functions>`

  .. code-block:: python

    def negate_second(a, b):
        return a

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I change the `return statement`_ to see how the input relates to the output

  .. code-block:: python

    def negate_second(a, b):
        return (a, b)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, True) is not false

  they are opposites, I change the statement and use not_

  .. code-block:: python

    def negate_second(a, b):
        return not b

* I get the next :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.truth_table' has no attribute 'negate_first'

  I add a definition for it, using the name as a clue and what I know from :ref:`negate second<test_negate_second>`

  .. code-block:: python

    def negate_first(a, b):
        return not a

* the terminal shows the next :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.truth_table' has no attribute 'material_non_implication'

  I add the :ref:`function<functions>`

  .. code-block:: python

    def material_non_implication(a, b):
        return not a

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I change the `return statement`_

  .. code-block:: python

    def material_non_implication(a, b):
        return False

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: False is not true

  I return the inputs

  .. code-block:: python

    def material_non_implication(a, b):
        return (a, b)
        return False

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, True) is not false

  this test also expects :ref:`True<test_what_is_true>` in some cases and :ref:`False<test_what_is_false>` in others. I add an `if statement`_

  .. code-block:: python

    def material_non_implication(a, b):
        if a == True and b == True:
            return False
        return (a, b)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, True) is not false

  I add another `if statement`_

  .. code-block:: python

    def material_non_implication(a, b):
        if a == False and b == True:
            return False
        if a == True and b == True:
            return False
        return (a, b)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, False) is not false

  I add another `if statement`_

  .. code-block:: python

    def material_non_implication(a, b):
        if a == False and b == False:
            return False
        if a == False and b == True:
            return False
        if a == True and b == True:
            return False
        return (a, b)

* I get the next :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.truth_table' has no attribute 'logical_implication'

  I add the :ref:`function<functions>`

  .. code-block:: python

    def logical_implication(a, b):
        return (a, b)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, False) is not false

  I add an `if statement`_

  .. code-block:: python

    def logical_implication(a, b):
        if a == True and b == False:
            return False
        return (a, b)

* I get the next :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.truth_table' has no attribute 'logical_nor'

  I add a definition for it

  .. code-block:: python

    def logical_nor(a, b):
        return (a, b)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, True) is not false

  I add an `if statement`_

  .. code-block:: python

    def logical_nor(a, b):
        if a == True and b == True:
            return False
        return (a, b)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, False) is not false

  I add another `if statement`_

  .. code-block:: python

    def logical_nor(a, b):
        if a == True and b == False:
            return False
        if a == True and b == True:
            return False
        return (a, b)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, True) is not false

  I add another `if statement`_

  .. code-block:: python

    def logical_nor(a, b):
        if a == False and b == True:
            return False
        if a == True and b == False:
            return False
        if a == True and b == True:
            return False
        return (a, b)

* I get :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'logical_nand'. Did you mean: 'logical_nor'?

  I add the :ref:`function<functions>`

  .. code-block:: python

    def logical_nand(a, b):
        return (a, b)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, True) is not false

  I add an `if statement`_

  .. code-block:: python

    def logical_nand(a, b):
        if a == True and b == True:
            return False
        return (a, b)

* on to the next :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.truth_table' has no attribute 'logical_equality'

  I add the :ref:`function<functions>`

  .. code-block:: python

    def logical_equality(a, b):
        return (a, b)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, False) is not false

  I add an `if statement`_

  .. code-block:: python

    def logical_equality(a, b):
        if a == True and b == False:
            return False
        return (a, b)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, True) is not false

  I add another `if statement`_

  .. code-block:: python

    def logical_equality(a, b):
        if a == False and b == True:
            return False
        if a == True and b == False:
            return False
        return (a, b)

* another :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'logical_disjunction'. Did you mean: 'logical_implication'?

  I add a :ref:`function<functions>`

  .. code-block:: python

    def logical_disjunction(a, b):
        return (a, b)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, False) is not false

  I add an `if statement`_

  .. code-block:: python

    def logical_disjunction(a, b):
        if a == False and b == False:
            return False
        return (a, b)

* the next :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'logical_conjunction'. Did you mean: 'logical_disjunction'?

  I add it

  .. code-block:: python

    def logical_conjunction(a, b):
        return (a, b)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, False) is not false

  I add an `if statement`_

  .. code-block:: python

    def logical_conjunction(a, b):
        if a == True and b == False:
            return False
        return (a, b)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, True) is not false

  I add another `if statement`_

  .. code-block:: python

    def logical_conjunction(a, b):
        if a == False and b == True:
            return False
        if a == True and b == False:
            return False
        return (a, b)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, False) is not false

  I add an `if statement`_

  .. code-block:: python

    def logical_conjunction(a, b):
        if a == False and b == False:
            return False
        if a == False and b == True:
            return False
        if a == True and b == False:
            return False
        return (a, b)

* I get another :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.truth_table' has no attribute 'exclusive_disjunction

  I add a :ref:`function<functions>` for it

  .. code-block:: python

    def exclusive_disjunction(a, b):
        return (a, b)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, True) is not false

  I add an `if statement`

  .. code-block:: python

    def exclusive_disjunction(a, b):
        if a == True and b == True:
            return False
        return (a, b)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, False) is not false

  I add another `if statement`_

  .. code-block:: python

    def exclusive_disjunction(a, b):
        if a == False and b == False:
            return False
        if a == True and b == True:
            return False
        return (a, b)

* next :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'converse_non_implication'. Did you mean: 'material_non_implication'?

  I add the :ref:`function<functions>`

  .. code-block:: python

    def material_non_implication(a, b):
        return (a, b)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, True) is not false

  I add an `if statement`_

  .. code-block:: python

    def material_non_implication(a, b):
        if a == True and b == True:
            return False
        return (a, b)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, True) is not false

  I add another `if statement`_

  .. code-block:: python

    def material_non_implication(a, b):
        if a == False and b == True:
            return False
        if a == True and b == True:
            return False
        return (a, b)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, False) is not false

  I add an `if statement`_

  .. code-block:: python

    def material_non_implication(a, b):
        if a == False and b == False:
            return False
        if a == False and b == True:
            return False
        if a == True and b == True:
            return False
        return (a, b)

* I have the next :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'converse_non_implication'. Did you mean: 'material_non_implication'?

  I add the :ref:`function<functions>`

  .. code-block:: python

    def converse_non_implication(a, b):
        return (a, b)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, True) is not false

  I add an `if statement`_

  .. code-block:: python

    def converse_non_implication(a, b):
        if a == True and b == True:
            return False
        return (a, b)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, False) is not false

  I add another `if statement`_

  .. code-block:: python

    def converse_non_implication(a, b):
        if a == True and b == False:
            return False
        if a == True and b == True:
            return False
        return (a, b)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, False) is not false

  I add a new `if statement`_

  .. code-block:: python

    def converse_non_implication(a, b):
        if a == False and b == False:
            return False
        if a == True and b == False:
            return False
        if a == True and b == True:
            return False
        return (a, b)

* the terminal shows :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'converse_implication'. Did you mean: 'converse_non_implication'?

  I add a :ref:`function<functions>`

  .. code-block:: python

    def converse_non_implication(a, b):
        return (a, b)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, True) is not false

  I add an `if statement`_

  .. code-block:: python

    def converse_non_implication(a, b):
        if a == True and b == True:
            return False
        return (a, b)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, False) is not false

  I add an `if statement`_

  .. code-block:: python

    def converse_non_implication(a, b):
        if a == True and b == False:
            return False
        if a == True and b == True:
            return False
        return (a, b)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, False) is not false

  I add another `if statement`_

  .. code-block:: python

    def converse_non_implication(a, b):
        if a == False and b == False:
            return False
        if a == True and b == False:
            return False
        if a == True and b == True:
            return False
        return (a, b)

* next :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'converse_implication'. Did you mean: 'converse_non_implication'?

  I add the :ref:`function<functions>`

  .. code-block:: python

    def converse_implication(a, b):
        return (a, b)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, True) is not false

  I add an `if statement`_

  .. code-block:: python

    def converse_implication(a, b):
        if a == False and b == True:
            return False
        return (a, b)

* the next :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.truth_table' has no attribute 'contradiction'

  I add the :ref:`function<functions>`

  .. code-block:: python

    def contradiction(a, b):
        return (a, b)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, True) is not false

  I add an `if statement`_

  .. code-block:: python

    def contradiction(a, b):
        if a == True and b == True:
            return False
        return (a, b)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (True, False) is not false

  I add another `if statement`_

  .. code-block:: python

    def contradiction(a, b):
        if a == True and b == False:
            return False
        if a == True and b == True:
            return False
        return (a, b)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, True) is not false

  I add another `if statement`

  .. code-block:: python

    def contradiction(a, b):
        if a == False and b == True:
            return False
        if a == True and b == False:
            return False
        if a == True and b == True:
            return False
        return (a, b)

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: (False, False) is not false

  I add an `if statement`_

  .. code-block:: python

    def contradiction(a, b):
        if a == False and b == False:
            return False
        if a == False and b == True:
            return False
        if a == True and b == False:
            return False
        if a == True and b == True:
            return False
        return (a, b)

* another :ref:`AttributeError`

  .. code-block:: python
    :force:

    AttributeError: module 'src.truth_table' has no attribute 'logical_negation'. Did you mean: 'logical_conjunction'?

  I add the :ref:`function<functions>`

  .. code-block:: python

    def logical_negation(a, b):
        return (a, b)

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