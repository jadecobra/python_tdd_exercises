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

.. WARNING:: Welcome to the wonderful world of Boolean Logic. If this is new to you, then prepare for headaches and moving closer to the edge of insanity.

  This is part of the process as you stretch yourself and learn new things that help you solve problems and see the world in a new way.

  Do you still want to continue?


The last chapter covered two types of operations

- :ref:`Nullary Operations` which do not take input
- :ref:`Unary Operations` which take one input

There are also :ref:`Binary Operations<truth table: Binary Operations>`, they take two inputs. Each input can be :ref:`False<test_what_is_false>` or :ref:`True<test_what_is_true>` which means there are 4 possible ways the inputs can be sent to a :ref:`binary operation<truth table: binary operations>`

==============  ==============
first input     second input
==============  ==============
:green:`True`   :green:`True`
:green:`True`   :red:`False`
:red:`False`    :green:`True`
:red:`False`    :red:`False`
==============  ==============

These combinations give :ref:`16 binary operations<truth table: binary operations>`, and each operation returns :green:`True` or :red:`False`. The :ref:`truth table<truth table: Binary Operations>` shows the 16 operations covered in these chapters and what they return when they receive input.

=============================================== ============= ============= ============= ============= ==============================================================
return                                          True,         True,         False,        False,        operation
                                                True          False         True          False
=============================================== ============= ============= ============= ============= ==============================================================
:red:`False`                                    :red:`False`  :red:`False`  :red:`False`  :red:`False`  :ref:`contradiction<test_contradiction>`
first and second                                :green:`True` :red:`False`  :red:`False`  :red:`False`  :ref:`logical_conjunction<test_logical_conjunction>`
second                                          :green:`True` :red:`False`  :green:`True` :red:`False`  :ref:`project_second<test_project_second>`
(not first) and second                          :red:`False`  :red:`False`  :green:`True` :red:`False`  :ref:`converse_non_implication<test_converse_non_implication>`
not first                                       :red:`False`  :red:`False`  :green:`True` :green:`True` :ref:`negate_first<test_negate_first>`
not (first and second)                          :red:`False`  :green:`True` :green:`True` :green:`True` :ref:`logical_nand<test_logical_nand>`
:green:`True`                                   :green:`True` :green:`True` :green:`True` :green:`True` :ref:`tautology<test_tautology>`
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
  Binary Operations 5: more examples<binary_operations_5>

----

*************************************************************************************
what is next?
*************************************************************************************

:ref:`are you ready to test Binary Operations?<binary_operations_1>`