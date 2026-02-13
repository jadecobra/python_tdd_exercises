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

The last chapter covered 2 types of operations. :ref:`Nullary Operations` which do not take input, and :ref:`Unary Operations` which take 1 input.

There are also Binary Operations, these take 2 inputs. Each of the inputs in this exercise will be :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>` which means there are 4 possible ways the inputs can be sent to an :ref:`operation<what is a function?>`

=================================   =================================
first input                         second input
=================================   =================================
:ref:`True <test_what_is_true>`     :ref:`True <test_what_is_true>`
:ref:`True <test_what_is_true>`     :ref:`False <test_what_is_false>`
:ref:`False <test_what_is_false>`   :ref:`True <test_what_is_true>`
:ref:`False <test_what_is_false>`   :ref:`False <test_what_is_false>`
=================================   =================================

These combinations give 16 binary operations, each operations returns :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>` when it gets input. Here are the 16 operations that are covered in these chapters and what they return

================================================================ =====================================================
operation                                                         return
================================================================ =====================================================
:ref:`contradiction<test_contradiction>`                          False
:ref:`converse_implication<test_converse_implication>`            first or not second
:ref:`converse_non_implication<test_converse_non_implication>`    not first and second
:ref:`exclusive_disjunction<test_exclusive_disjunction>`          (not (first and second)) and (first or second)
:ref:`logical_conjunction<test_logical_conjunction>`              first and second
:ref:`logical_disjunction<test_logical_disjunction>`              first or second
:ref:`logical_equality<test_logical_equality>`                    (not first or second) and (first or not second)
:ref:`logical_nand<test_logical_nand>`                            not (first and second)
:ref:`logical_nor<test_logical_nor>`                              not (first or second)
:ref:`material_implication<test_material_implication>`            not first or second
:ref:`material_non_implication<test_material_non_implication>`    first and not second
:ref:`negate_first<test_negate_first>`                            not first
:ref:`negate_second<test_negate_second>`                          not second
:ref:`project_first<test_project_first>`                          first
:ref:`project_second<test_project_second>`                        second
:ref:`tautology<test_tautology>`                                  True
================================================================ =====================================================

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

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->