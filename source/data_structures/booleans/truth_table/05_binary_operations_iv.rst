.. include:: ../../../links.rst

.. _binary_operations_iv:

#################################################################################
truth table: test_truth_table
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

*********************************************************************************
review
*********************************************************************************

*YOU DID IT!* You made it to the end of the ``Truth Table`` series. Summarizing what the tests have shown so far, I know that for any boolean operation involving 2 inputs: ``p`` and ``q`` which can take the values :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`

* ``contradition`` always returns :ref:`False<test_what_is_false>` it is a :ref:`singleton function<test_singleton_functions>`
* ``tautology`` always returns :ref:`True<test_what_is_true>` it is a :ref:`singleton function<test_singleton_functions>`
* ``converse implication`` is ``not p and q`` which is different from ``not(p and q)``
* ``project second`` always returns ``q``
* ``project first`` always returns ``p``
* ``negate second`` always returns ``not q``
* ``negate first`` always return ``not p``
* ``material non implication`` is ``p and not q``
* ``converse non implication`` is ``not p and q`` which is different from ``not(p and q)``
* ``logical NOR`` is ``not(p or q)``
* ``logical NAND`` is ``not(p and q)``
* ``exclusive disjunction`` is ``!=`` or the opposite of ``logical_equality``
* ``logical equality`` is ``==``
* ``logical implication`` is ``not p or q``
* ``logical disjunction`` is or_
* ``logical conjunction`` is and_
* and_ is "not or_"
* or_ is "not and_"
* :ref:`False<test_what_is_false>` is not_ :ref:`True<test_what_is_true>`
* :ref:`True<test_what_is_true>` is not_ :ref:`False<test_what_is_false>`
* :ref:`False<test_what_is_false>` is :ref:`False<test_what_is_false>`
* :ref:`True<test_what_is_true>` is :ref:`True<test_what_is_true>`

Would you like to :doc:`test lists</data_structures/lists/lists>`?

----

:doc:`/code/code_truth_table`