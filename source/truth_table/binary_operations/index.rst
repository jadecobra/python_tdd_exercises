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

We know that there are two :ref:`booleans<what are booleans?>` - :ref:`True<test_what_is_true>` and :ref:`False<test_what_is_false>`

There are also Binary Operations, these take 2 inputs. Each of the inputs can be :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>` which means there are 4 possible ways the inputs can be sent to an :ref:`operation<what is a function?>`

==============  ==============
first input     second input
==============  ==============
:green:`True`   :green:`True`
:green:`True`   :red:`False`
:red:`False`    :green:`True`
:red:`False`    :red:`False`
==============  ==============

These combinations give 16 binary operations or outcomes when the :ref:`booleans<what are booleans?>` are put together, and each operation returns :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>` when it gets input.

Here are the 16 operations that are covered in these chapters and what they return

=============================================== ============= ============= ============= ============= ==============================================================
return                                          True,         True,         False,        False,        operation
                                                True          False         True          False
=============================================== ============= ============= ============= ============= ==============================================================
False                                           :red:`False`  :red:`False`  :red:`False`  :red:`False`  :ref:`contradiction<test_contradiction>`
first and second                                :green:`True` :red:`False`  :red:`False`  :red:`False`  :ref:`logical_conjunction<test_logical_conjunction>`
second                                          :green:`True` :red:`False`  :green:`True` :red:`False`  :ref:`project_second<test_project_second>`
(not first) and second                          :red:`False`  :red:`False`  :green:`True` :red:`False`  :ref:`converse_non_implication<test_converse_non_implication>`
not first                                       :red:`False`  :red:`False`  :green:`True` :green:`True` :ref:`negate_first<test_negate_first>`
not (first and second)                          :red:`False`  :green:`True` :green:`True` :green:`True` :ref:`logical_nand<test_logical_nand>`
True                                            :green:`True` :green:`True` :green:`True` :green:`True` :ref:`tautology<test_tautology>`
first or second                                 :green:`True` :green:`True` :green:`True` :red:`False`  :ref:`logical_disjunction<test_logical_disjunction>`
(not (first and second)) and (first or second)  :red:`False`  :green:`True` :green:`True` :red:`False`  :ref:`exclusive_disjunction<test_exclusive_disjunction>`
first and (not second)                          :red:`False`  :green:`True` :red:`False`  :red:`False`  :ref:`material_non_implication<test_material_non_implication>`
first                                           :green:`True` :green:`True` :red:`False`  :red:`False`  :ref:`project_first<test_project_first>`
first or (not second)                           :green:`True` :green:`True` :red:`False`  :green:`True` :ref:`converse_implication<test_converse_implication>`
not second                                      :red:`False`  :green:`True` :red:`False`  :green:`True` :ref:`negate_second<test_negate_second>`
not (first or second)                           :red:`False`  :red:`False`  :red:`False`  :green:`True` :ref:`logical_nor<test_logical_nor>`
(not first or second) and (first or not second) :green:`True` :red:`False`  :red:`False`  :green:`True` :ref:`logical_equality<test_logical_equality>`
(not first) or second                           :green:`True` :red:`False`  :green:`True` :green:`True` :ref:`material_implication<test_material_implication>`
=============================================== ============= ============= ============= ============= ==============================================================

----

*********************************************************************************
preview
*********************************************************************************

These are the tests I have at the end of the chapters

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
  Binary Operations 5<binary_operations_5>

----

*************************************************************************************
what is next?
*************************************************************************************

:ref:`are you ready to test Binary Operations?<binary_operations_1>`