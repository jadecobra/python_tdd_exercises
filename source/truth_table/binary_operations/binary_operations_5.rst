.. meta::
  :description: Master Python truth tables by implementing binary operations like negation, NOR, and material implication. Learn to code these logical functions step-by-step. Watch the full tutorial.
  :keywords: Jacob Itegboje, python truth table for binary operations, how to implement logical NOR in python, python material implication explained, python truth table for loop, python logical operations tutorial, truth table for negation in python, python binary operations tutorial, how to create a truth table in python with multiple inputs

.. include:: ../../links.rst

.. _binary_operations_5:

#################################################################################
truth table: Binary Operations 5
#################################################################################

----

*********************************************************************************
requirements
*********************************************************************************

:ref:`Binary Operations 1<truth table: Binary Operations 1>`
:ref:`Binary Operations 2<truth table: Binary Operations 2>`
:ref:`Binary Operations 3<truth table: Binary Operations 3>`
:ref:`Binary Operations 4<truth table: Binary Operations 4>`

----

*************************************************************************************
more examples
*************************************************************************************


----

=================================================================================
home security alarm
=================================================================================

----

if the inputs are

- is there motion in the house?
- is the code right?

========================================================  =========== =========== =========== =========== ========================================================
alarm                                                     motion,     motion,     no motion,  no motion,  operation
                                                          wrong code  right code  wrong code  right code
========================================================  =========== =========== =========== =========== ========================================================
alarm always off                                          :red:`off`  :red:`off`  :red:`off`  :red:`off`  :ref:`contradiction<test_contradiction>`
motion and wrong code                                     :green:`on` :red:`off`  :red:`off`  :red:`off`  :ref:`logical_conjunction<test_logical_conjunction>`
wrong code                                                :green:`on` :red:`off`  :green:`on` :red:`off`  :ref:`project_second<test_project_second>`
(no motion) and wrong code                                :red:`off`  :red:`off`  :green:`on` :red:`off`  :ref:`converse_non_implication<test_converse_non_implication>`
no motion                                                 :red:`off`  :red:`off`  :green:`on` :green:`on` :ref:`negate_first<test_negate_first>`
not (motion and wrong code)                               :red:`off`  :green:`on` :green:`on` :green:`on` :ref:`logical_nand<test_logical_nand>`
alarm always                                              :green:`on` :green:`on` :green:`on` :green:`on` :ref:`tautology<test_tautology>`
motion or right code                                      :green:`on` :green:`on` :green:`on` :red:`off`  :ref:`logical_disjunction<test_logical_disjunction>`
(not (motion and wrong code)) and (motion or wrong code)  :red:`off`  :green:`on` :green:`on` :red:`off`  :ref:`exclusive_disjunction<test_exclusive_disjunction>`
motion and (right code)                                   :red:`off`  :green:`on` :red:`off`  :red:`off`  :ref:`material_non_implication<test_material_non_implication>`
motion                                                    :green:`on` :green:`on` :red:`off`  :red:`off`  :ref:`project_first<test_project_first>`
motion or (right code)                                    :green:`on` :green:`on` :red:`off`  :green:`on` :ref:`converse_implication<test_converse_implication>`
right code                                                :red:`off`  :green:`on` :red:`off`  :green:`on` :ref:`negate_second<test_negate_second>`
not (motion or wrong code)                                :red:`off`  :red:`off`  :red:`off`  :green:`on` :ref:`logical_nor<test_logical_nor>`
(no motion or wrong code) and (motion or right code)      :green:`on` :red:`off`  :red:`off`  :green:`on` :ref:`logical_equality<test_logical_equality>`
(no motion) or wrong code                                 :green:`on` :red:`off`  :green:`on` :green:`on` :ref:`material_implication<test_material_implication>`
========================================================  =========== =========== =========== =========== ========================================================

==============================================================  ===========================================================================================================
operation                                                       rule
==============================================================  ===========================================================================================================
:ref:`contradiction<test_contradiction>`                        alarm always off
:ref:`logical_conjunction<test_logical_conjunction>`            alarm only if there is motion and if it is the wrong code
:ref:`project_second<test_project_second>`                      alarm only if it is the wrong code
:ref:`converse_non_implication<test_converse_non_implication>`  alarm only if there is no motion and if it is the wrong code
:ref:`negate_first<test_negate_first>`                          alarm only if there is no motion
:ref:`logical_nand<test_logical_nand>`                          alarm off only if there is motion and if it is the wrong code
:ref:`tautology<test_tautology>`                                alarm always on
:ref:`logical_disjunction<test_logical_disjunction>`            alarm off if there is no motion and if it is the right code
:ref:`exclusive_disjunction<test_exclusive_disjunction>`        alarm off if there is motion with the wrong code and if there is no motion with the right code
:ref:`material_non_implication<test_material_non_implication>`  alarm only if there is motion and if it is the right code
:ref:`project_first<test_project_first>`                        alarm only if there is motion
:ref:`converse_implication<test_converse_implication>`          alarm off only if there is no motion and if it is the wrong code
:ref:`negate_second<test_negate_second>`                        alarm only if it is the right code
:ref:`logical_nor<test_logical_nor>`                            alarm only if there is no motion and if it is the right code
:ref:`logical_equality<test_logical_equality>`                  alarm only if there is motion with the wrong code and if there is no motion with the right code
:ref:`material_implication<test_material_implication>`          alarm off only if there is motion and if it is the right code
==============================================================  ===========================================================================================================

----

=================================================================================
hiring
=================================================================================

----

if the inputs are

- is the person a strong option?
- is the person a strong fit?

======================================================================  =============== =============== =============== =============== ==============================================================
hire/reject                                                             strong option,  strong option,  weak option,    weak option,    operation
                                                                        strong fit      weak fit        strong fit      weak fit
======================================================================  =============== =============== =============== =============== ==============================================================
reject                                                                  :red:`reject`   :red:`reject`   :red:`reject`   :red:`reject`   :ref:`contradiction<test_contradiction>`
strong option and strong fit                                            :green:`hire`   :red:`reject`   :red:`reject`   :red:`reject`   :ref:`logical_conjunction<test_logical_conjunction>`
strong fit                                                              :green:`hire`   :red:`reject`   :green:`hire`   :red:`reject`   :ref:`project_second<test_project_second>`
weak option and strong fit                                              :red:`reject`   :red:`reject`   :green:`hire`   :red:`reject`   :ref:`converse_non_implication<test_converse_non_implication>`
weak option                                                             :red:`reject`   :red:`reject`   :green:`hire`   :green:`hire`   :ref:`negate_first<test_negate_first>`
not (strong option and strong fit)                                      :red:`reject`   :green:`hire`   :green:`hire`   :green:`hire`   :ref:`logical_nand<test_logical_nand>`
hire                                                                    :green:`hire`   :green:`hire`   :green:`hire`   :green:`hire`   :ref:`tautology<test_tautology>`
strong option or weak fit                                               :green:`hire`   :green:`hire`   :green:`hire`   :red:`reject`   :ref:`logical_disjunction<test_logical_disjunction>`
(not (strong option and strong fit)) and (strong option or strong fit)  :red:`reject`   :green:`hire`   :green:`hire`   :red:`reject`   :ref:`exclusive_disjunction<test_exclusive_disjunction>`
strong option and (weak fit)                                            :red:`reject`   :green:`hire`   :red:`reject`   :red:`reject`   :ref:`material_non_implication<test_material_non_implication>`
strong option                                                           :green:`hire`   :green:`hire`   :red:`reject`   :red:`reject`   :ref:`project_first<test_project_first>`
strong option or (weak fit)                                             :green:`hire`   :green:`hire`   :red:`reject`   :green:`hire`   :ref:`converse_implication<test_converse_implication>`
weak fit                                                                :red:`reject`   :green:`hire`   :red:`reject`   :green:`hire`   :ref:`negate_second<test_negate_second>`
not (strong option or strong fit)                                       :red:`reject`   :red:`reject`   :red:`reject`   :green:`hire`   :ref:`logical_nor<test_logical_nor>`
(weak option or strong fit) and (strong option or weak fit)             :green:`hire`   :red:`reject`   :red:`reject`   :green:`hire`   :ref:`logical_equality<test_logical_equality>`
(weak option) or strong fit                                             :green:`hire`   :red:`reject`   :green:`hire`   :green:`hire`   :ref:`material_implication<test_material_implication>`
======================================================================  =============== =============== =============== =============== ==============================================================

==============================================================  ===========================================================================================================
operation                                                       rule
==============================================================  ===========================================================================================================
:ref:`contradiction<test_contradiction>`                        not hiring
:ref:`logical_conjunction<test_logical_conjunction>`            hire only if it is a strong option and if it is a strong fit
:ref:`project_second<test_project_second>`                      hire only if it is a strong fit
:ref:`converse_non_implication<test_converse_non_implication>`  hire only if it is weak option and if it is a strong fit
:ref:`negate_first<test_negate_first>`                          hire only if it is weak option
:ref:`logical_nand<test_logical_nand>`                          reject only if it is a strong option and if it is a strong fit
:ref:`tautology<test_tautology>`                                hiring
:ref:`logical_disjunction<test_logical_disjunction>`            reject only if it is weak option and if it is a weak fit
:ref:`exclusive_disjunction<test_exclusive_disjunction>`        reject only if it is a strong option with a strong fit and if it is a weak option with a weak fit
:ref:`material_non_implication<test_material_non_implication>`  hire only if it is a strong option and if it is a weak fit
:ref:`project_first<test_project_first>`                        hire only if it is a strong option
:ref:`converse_implication<test_converse_implication>`          reject only if it is weak option and if it is a strong fit
:ref:`negate_second<test_negate_second>`                        hire only if it is a weak fit
:ref:`logical_nor<test_logical_nor>`                            hire only if it is a weak option and if it is a weak fit
:ref:`logical_equality<test_logical_equality>`                  hire only if it is a strong option with a strong fit and if it is weak option with a weak fit
:ref:`material_implication<test_material_implication>`          reject only if it is a strong option and if it is a weak fit
==============================================================  ===========================================================================================================

----

*************************************************************************************
what is next?
*************************************************************************************

:ref:`Would you like to test the truth table tests?<test_truth_table_tests>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->