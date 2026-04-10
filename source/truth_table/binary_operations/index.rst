.. meta::
  :description: Master Python truth tables for binary operations. This guide simplifies 'if' statements with clear, step-by-step Python code examples. Watch the tutorial!
  :keywords: Jacob Itegboje, python truth table for if statements, python truth table generator from expression, python logical operators truth table, python truth table for two variables, how to make a truth table in python, python contradiction function, python logical conjunction truth table

.. include:: ../../links.rst

.. _binary_operations:

#################################################################################
truth table: Binary Operations
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/Q_jhE204MoE?si=m9_EvOX-4lrmSzo7" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

.. WARNING:: Welcome to the wonderful world of Boolean Logic. If this is new to you, then prepare for headaches and moving closer to the edge of insanity. This is part of the process as you stretch yourself and learn new things that will help you solve problems.

  Do you still want to continue?


The last chapter covered 2 types of operations. :ref:`Nullary Operations` which do not take input, and :ref:`Unary Operations` which take 1 input.

We know that there are two :ref:`booleans<what are booleans?>`

:ref:`True<test_what_is_true>` and :ref:`False<test_what_is_false>`

There are also Binary Operations, these take 2 inputs. Each of the inputs in this exercise will be :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>` which means there are 4 possible ways the inputs can be sent to an :ref:`operation<what is a function?>`

=================================   =================================
first input                         second input
=================================   =================================
:ref:`True <test_what_is_true>`     :ref:`True <test_what_is_true>`
:ref:`True <test_what_is_true>`     :ref:`False <test_what_is_false>`
:ref:`False <test_what_is_false>`   :ref:`True <test_what_is_true>`
:ref:`False <test_what_is_false>`   :ref:`False <test_what_is_false>`
=================================   =================================

These combinations give 16 binary operations or outcomes when 2 :ref:`booleans<what are booleans?>` interact, and each operation returns :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>` when it gets input. Here are the 16 operations that are covered in these chapters and what they return

=============================================== ======  ======  ======  ======  ==============================================================
return                                          True,   True,   False,  False,  name of the operation
                                                True    False   True    False
=============================================== ======  ======  ======  ======  ==============================================================
False                                           False   False   False   False   :ref:`contradiction<test_contradiction>`
first and second                                True    False   False   False   :ref:`logical_conjunction<test_logical_conjunction>`
second                                          True    False   True    False   :ref:`project_second<test_project_second>`
(not first) and second                          False   False   True    False   :ref:`converse_non_implication<test_converse_non_implication>`
not first                                       False   False   True    True    :ref:`negate_first<test_negate_first>`
not (first and second)                          False   True    True    True    :ref:`logical_nand<test_logical_nand>`
True                                            True    True    True    True    :ref:`tautology<test_tautology>`
first or second                                 True    True    True    False   :ref:`logical_disjunction<test_logical_disjunction>`
(not (first and second)) and (first or second)  False   True    True    False   :ref:`exclusive_disjunction<test_exclusive_disjunction>`
first and (not second)                          False   True    False   False   :ref:`material_non_implication<test_material_non_implication>`
first                                           True    True    False   False   :ref:`project_first<test_project_first>`
first or (not second)                           True    True    False   True    :ref:`converse_implication<test_converse_implication>`
not second                                      False   True    False   True    :ref:`negate_second<test_negate_second>`
not (first or second)                           True    True    True    False   :ref:`logical_nor<test_logical_nor>`
(not first or second) and (first or not second) True    False   False   True    :ref:`logical_equality<test_logical_equality>`
(not first) or second                           True    False   True    True    :ref:`material_implication<test_material_implication>`
=============================================== ======  ======  ======  ======  ==============================================================

----

*********************************************************************************
preview
*********************************************************************************

Here are the tests I have at the end of the chapters

.. literalinclude:: ../../code/truth_table/tests/test_binary.py
  :language: python
  :linenos:

----

*********************************************************************************
requirements
*********************************************************************************

:ref:`truth table: Nullary and Unary Operations`

----

*********************************************************************************
Binary Operations
*********************************************************************************

.. toctree::
  :titlesonly:

  Binary Operations 1<binary_operations_1>
  Booleans 2<../../data_structures/booleans/booleans_2>
  Binary Operations 2<binary_operations_2>
  Binary Operations 3<binary_operations_3>
  Binary Operations 4<binary_operations_4>

----

*************************************************************************************
what is next?
*************************************************************************************

:ref:`are you ready to test Binary Operations?<binary_operations_1>`