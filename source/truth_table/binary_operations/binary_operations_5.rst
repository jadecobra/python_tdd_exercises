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

* :ref:`Binary Operations 4<truth table: Binary Operations 4>`

----

*************************************************************************************
more examples
*************************************************************************************


----

=================================================================================
security alarm
=================================================================================

----

if the inputs are

- is there motion?
- is the code right?

it means the possible states are

==================  ==================
motion?             code?
==================  ==================
:green:`no motion`  :green:`right code`
:green:`no motion`  :red:`wrong code`
:red:`motion`       :green:`right code`
:red:`motion`       :red:`wrong code`
==================  ==================

the inputs give the :ref:`truth table` below

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
motion or wrong code                                      :green:`on` :green:`on` :green:`on` :red:`off`  :ref:`logical_disjunction<test_logical_disjunction>`
(not (motion and wrong code)) and (motion or wrong code)  :red:`off`  :green:`on` :green:`on` :red:`off`  :ref:`exclusive_disjunction<test_exclusive_disjunction>`
motion and right code                                     :red:`off`  :green:`on` :red:`off`  :red:`off`  :ref:`material_non_implication<test_material_non_implication>`
motion                                                    :green:`on` :green:`on` :red:`off`  :red:`off`  :ref:`project_first<test_project_first>`
motion or right code                                      :green:`on` :green:`on` :red:`off`  :green:`on` :ref:`converse_implication<test_converse_implication>`
right code                                                :red:`off`  :green:`on` :red:`off`  :green:`on` :ref:`negate_second<test_negate_second>`
not (motion or wrong code)                                :red:`off`  :red:`off`  :red:`off`  :green:`on` :ref:`logical_nor<test_logical_nor>`
(no motion or wrong code) and (motion or right code)      :green:`on` :red:`off`  :red:`off`  :green:`on` :ref:`logical_equality<test_logical_equality>`
no motion or wrong code                                   :green:`on` :red:`off`  :green:`on` :green:`on` :ref:`material_implication<test_material_implication>`
========================================================  =========== =========== =========== =========== ========================================================

we can say this in English as

==============================================================  ===========================================================================================================
operation                                                       rule
==============================================================  ===========================================================================================================
:ref:`contradiction<test_contradiction>`                        alarm always off
:ref:`logical_conjunction<test_logical_conjunction>`            alarm only if there is motion and the code is wrong
:ref:`project_second<test_project_second>`                      alarm only if the code is wrong
:ref:`converse_non_implication<test_converse_non_implication>`  alarm only if there is no motion and the code is wrong
:ref:`negate_first<test_negate_first>`                          alarm only if there is no motion
:ref:`logical_nand<test_logical_nand>`                          alarm off only if there is motion and the code is wrong
:ref:`tautology<test_tautology>`                                alarm always on
:ref:`logical_disjunction<test_logical_disjunction>`            alarm off if there is no motion and the code is right
:ref:`exclusive_disjunction<test_exclusive_disjunction>`        alarm off if there is motion and the code is wrong, alarm off if there is no motion and the code is right
:ref:`material_non_implication<test_material_non_implication>`  alarm only if there is motion and the code is right
:ref:`project_first<test_project_first>`                        alarm only if there is motion
:ref:`converse_implication<test_converse_implication>`          alarm off only if there is no motion and the code is wrong
:ref:`negate_second<test_negate_second>`                        alarm only if the code is right
:ref:`logical_nor<test_logical_nor>`                            alarm only if there is no motion and the code is right
:ref:`logical_equality<test_logical_equality>`                  alarm if there is motion and the code is wrong, alarm if there is no motion and the code is right
:ref:`material_implication<test_material_implication>`          alarm off only if there is motion and the code is right
==============================================================  ===========================================================================================================

----

=================================================================================
hiring
=================================================================================

----

if the inputs are

- is the person a strong option?
- is the person a strong fit?

it means the possible states are

======================  ======================
option                  fit
======================  ======================
:green:`strong option`  :green:`strong fit`
:green:`strong option`  :red:`weak fit`
:red:`weak option`      :green:`strong fit`
:red:`weak option`      :red:`weak fit`
======================  ======================

the inputs give the :ref:`truth table` below

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
strong option or strong fit                                               :green:`hire`   :green:`hire`   :green:`hire`   :red:`reject`   :ref:`logical_disjunction<test_logical_disjunction>`
(not (strong option and strong fit)) and (strong option or strong fit)  :red:`reject`   :green:`hire`   :green:`hire`   :red:`reject`   :ref:`exclusive_disjunction<test_exclusive_disjunction>`
strong option and weak fit                                              :red:`reject`   :green:`hire`   :red:`reject`   :red:`reject`   :ref:`material_non_implication<test_material_non_implication>`
strong option                                                           :green:`hire`   :green:`hire`   :red:`reject`   :red:`reject`   :ref:`project_first<test_project_first>`
strong option or weak fit                                               :green:`hire`   :green:`hire`   :red:`reject`   :green:`hire`   :ref:`converse_implication<test_converse_implication>`
weak fit                                                                :red:`reject`   :green:`hire`   :red:`reject`   :green:`hire`   :ref:`negate_second<test_negate_second>`
not (strong option or strong fit)                                       :red:`reject`   :red:`reject`   :red:`reject`   :green:`hire`   :ref:`logical_nor<test_logical_nor>`
(weak option or strong fit) and (strong option or weak fit)             :green:`hire`   :red:`reject`   :red:`reject`   :green:`hire`   :ref:`logical_equality<test_logical_equality>`
weak option or strong fit                                               :green:`hire`   :red:`reject`   :green:`hire`   :green:`hire`   :ref:`material_implication<test_material_implication>`
======================================================================  =============== =============== =============== =============== ==============================================================

we can say this in English as

==============================================================  ===========================================================================================================
operation                                                       rule
==============================================================  ===========================================================================================================
:ref:`contradiction<test_contradiction>`                        not hiring
:ref:`logical_conjunction<test_logical_conjunction>`            hire only if it is a strong option that is a strong fit
:ref:`project_second<test_project_second>`                      hire only if it is a strong fit
:ref:`converse_non_implication<test_converse_non_implication>`  hire only if it is weak option that is a strong fit
:ref:`negate_first<test_negate_first>`                          hire only if it is weak option
:ref:`logical_nand<test_logical_nand>`                          reject only if it is a strong option that is a strong fit
:ref:`tautology<test_tautology>`                                hiring
:ref:`logical_disjunction<test_logical_disjunction>`            reject only if it is weak option that is a weak fit
:ref:`exclusive_disjunction<test_exclusive_disjunction>`        reject if it is a strong option that is a strong fit, reject if it is a weak option that is a weak fit
:ref:`material_non_implication<test_material_non_implication>`  hire only if it is a strong option that is a weak fit
:ref:`project_first<test_project_first>`                        hire only if it is a strong option
:ref:`converse_implication<test_converse_implication>`          reject only if it is weak option that is a strong fit
:ref:`negate_second<test_negate_second>`                        hire only if it is a weak fit
:ref:`logical_nor<test_logical_nor>`                            hire only if it is a weak option that is a weak fit
:ref:`logical_equality<test_logical_equality>`                  hire if it is a strong option that is a strong fit, hire if it is weak option that is a weak fit
:ref:`material_implication<test_material_implication>`          reject only if it is a strong option that is a weak fit
==============================================================  ===========================================================================================================

----

=================================================================================
store discount policy
=================================================================================

----

if the inputs are

- does the person have a coupon?
- is the person a member?

it means the possible states are

======================  ======================
option                  fit
======================  ======================
:green:`strong option`  :green:`strong fit`
:green:`strong option`  :red:`weak fit`
:red:`weak option`      :green:`strong fit`
:red:`weak option`      :red:`weak fit`
======================  ======================

the inputs give the :ref:`truth table` below

==================================================  ================= ================= ================= ================= ==============================================================
discount/regular price                              coupon,           coupon,           no coupon,        no coupon,        operation
                                                    member            not member        member            not member
==================================================  ================= ================= ================= ================= ==============================================================
regular                                             :red:`regular`    :red:`regular`    :red:`regular`    :red:`regular`    :ref:`contradiction<test_contradiction>`
coupon and member                                   :green:`discount` :red:`regular`    :red:`regular`    :red:`regular`    :ref:`logical_conjunction<test_logical_conjunction>`
member                                              :green:`discount` :red:`regular`    :green:`discount` :red:`regular`    :ref:`project_second<test_project_second>`
no coupon and member                                :red:`regular`    :red:`regular`    :green:`discount` :red:`regular`    :ref:`converse_non_implication<test_converse_non_implication>`
no coupon                                           :red:`regular`    :red:`regular`    :green:`discount` :green:`discount` :ref:`negate_first<test_negate_first>`
not (coupon and member)                             :red:`regular`    :green:`discount` :green:`discount` :green:`discount` :ref:`logical_nand<test_logical_nand>`
discount                                            :green:`discount` :green:`discount` :green:`discount` :green:`discount` :ref:`tautology<test_tautology>`
coupon or member                                :green:`discount` :green:`discount` :green:`discount` :red:`regular`    :ref:`logical_disjunction<test_logical_disjunction>`
(not (coupon and member)) and (coupon or member)    :red:`regular`    :green:`discount` :green:`discount` :red:`regular`    :ref:`exclusive_disjunction<test_exclusive_disjunction>`
coupon and not member                               :red:`regular`    :green:`discount` :red:`regular`    :red:`regular`    :ref:`material_non_implication<test_material_non_implication>`
coupon                                              :green:`discount` :green:`discount` :red:`regular`    :red:`regular`    :ref:`project_first<test_project_first>`
coupon or not member                                :green:`discount` :green:`discount` :red:`regular`    :green:`discount` :ref:`converse_implication<test_converse_implication>`
not member                                          :red:`regular`    :green:`discount` :red:`regular`    :green:`discount` :ref:`negate_second<test_negate_second>`
not (coupon or member)                              :red:`regular`    :red:`regular`    :red:`regular`    :green:`discount` :ref:`logical_nor<test_logical_nor>`
(no coupon or member) and (coupon or not member)    :green:`discount` :red:`regular`    :red:`regular`    :green:`discount` :ref:`logical_equality<test_logical_equality>`
no coupon or member                                 :green:`discount` :red:`regular`    :green:`discount` :green:`discount` :ref:`material_implication<test_material_implication>`
==================================================  ================= ================= ================= ================= ==============================================================

we can say this in English as

==============================================================  ===========================================================================================================
operation                                                       rule
==============================================================  ===========================================================================================================
:ref:`contradiction<test_contradiction>`                        everyone pays regular price, no discounts
:ref:`logical_conjunction<test_logical_conjunction>`            discount price only if person has a coupon and is a member
:ref:`project_second<test_project_second>`                      discount price only if person is a member
:ref:`converse_non_implication<test_converse_non_implication>`  discount price only if person does not have a coupon and is a member
:ref:`negate_first<test_negate_first>`                          discount price only if person does not have a coupon
:ref:`logical_nand<test_logical_nand>`                          regular price only if person has a coupon and is a member
:ref:`tautology<test_tautology>`                                everyone gets a discount
:ref:`logical_disjunction<test_logical_disjunction>`            regular price only if person does not have a coupon and is not a member
:ref:`exclusive_disjunction<test_exclusive_disjunction>`        regular price if person has a coupon and is a member, regular price if person does not have a coupon and is not a member
:ref:`material_non_implication<test_material_non_implication>`  discount price only if person has a coupon and is not a member
:ref:`project_first<test_project_first>`                        discount price only if person has a coupon
:ref:`converse_implication<test_converse_implication>`          regular price only if person does not have a coupon and is a member
:ref:`negate_second<test_negate_second>`                        discount price only if person is not a member
:ref:`logical_nor<test_logical_nor>`                            discount price only if person does not have a coupon and is not a member
:ref:`logical_equality<test_logical_equality>`                  discount price only if person has a coupon and is a member, discount price if person does not have a coupon and is not a member
:ref:`material_implication<test_material_implication>`          regular price only if person has a coupon and is not a member
==============================================================  ===========================================================================================================

----

=================================================================================
watering plants
=================================================================================

----

if the inputs are

- is the soil dry?
- did it rain?

======================================================  ============ ============ ============ ============ ==============================================================
water the plants                                        dry soil,    dry soil,    wet soil,    wet soil,         operation
                                                        no rain      it rained    no rain      it rained
======================================================  ============ ============ ============ ============ ==============================================================
do not water                                            :red:`no`    :red:`no`    :red:`no`    :red:`no`    :ref:`contradiction<test_contradiction>`
dry soil and no rain                                    :green:`yes` :red:`no`    :red:`no`    :red:`no`    :ref:`logical_conjunction<test_logical_conjunction>`
no rain                                                 :green:`yes` :red:`no`    :green:`yes` :red:`no`    :ref:`project_second<test_project_second>`
wet soil and no rain                                    :red:`no`    :red:`no`    :green:`yes` :red:`no`    :ref:`converse_non_implication<test_converse_non_implication>`
wet soil                                                :red:`no`    :red:`no`    :green:`yes` :green:`yes` :ref:`negate_first<test_negate_first>`
not (dry soil and no rain)                              :red:`no`    :green:`yes` :green:`yes` :green:`yes` :ref:`logical_nand<test_logical_nand>`
water                                                   :green:`yes` :green:`yes` :green:`yes` :green:`yes` :ref:`tautology<test_tautology>`
dry soil or no rain                                   :green:`yes` :green:`yes` :green:`yes` :red:`no`    :ref:`logical_disjunction<test_logical_disjunction>`
(not (dry soil and no rain)) and (dry soil or no rain)  :red:`no`    :green:`yes` :green:`yes` :red:`no`    :ref:`exclusive_disjunction<test_exclusive_disjunction>`
dry soil and it rained                                  :red:`no`    :green:`yes` :red:`no`    :red:`no`    :ref:`material_non_implication<test_material_non_implication>`
dry soil                                                :green:`yes` :green:`yes` :red:`no`    :red:`no`    :ref:`project_first<test_project_first>`
dry soil or it rained                                   :green:`yes` :green:`yes` :red:`no`    :green:`yes` :ref:`converse_implication<test_converse_implication>`
rain                                                    :red:`no`    :green:`yes` :red:`no`    :green:`yes` :ref:`negate_second<test_negate_second>`
not (dry soil or no rain)                               :red:`no`    :red:`no`    :red:`no`    :green:`yes` :ref:`logical_nor<test_logical_nor>`
(wet soil or no rain) and (dry soil or it rained)       :green:`yes` :red:`no`    :red:`no`    :green:`yes` :ref:`logical_equality<test_logical_equality>`
(wet soil) or no rain                                   :green:`yes` :red:`no`    :green:`yes` :green:`yes` :ref:`material_implication<test_material_implication>`
======================================================  ============ ============ ============ ============ ==============================================================

we can say this in English as

==============================================================  ===========================================================================================================
operation                                                       rule
==============================================================  ===========================================================================================================
:ref:`contradiction<test_contradiction>`                        do not water
:ref:`logical_conjunction<test_logical_conjunction>`            water only if soil is dry and it did not rain
:ref:`project_second<test_project_second>`                      water only if it did not rain
:ref:`converse_non_implication<test_converse_non_implication>`  water only if soil is wet and it did not rain
:ref:`negate_first<test_negate_first>`                          water only if soil is wet
:ref:`logical_nand<test_logical_nand>`                          do not water if soil is dry and it did not rain
:ref:`tautology<test_tautology>`                                everyone gets a yes
:ref:`logical_disjunction<test_logical_disjunction>`            do not water if soil is wet and it rained
:ref:`exclusive_disjunction<test_exclusive_disjunction>`        do not water if soil is dry and it did not rain, do not water if soil is wet and it did not rain
:ref:`material_non_implication<test_material_non_implication>`  water only if soil is dry and it rained
:ref:`project_first<test_project_first>`                        water only if soil is dry
:ref:`converse_implication<test_converse_implication>`          do not water if soil is wet and it did not rain
:ref:`negate_second<test_negate_second>`                        water only if it rained
:ref:`logical_nor<test_logical_nor>`                            water only if soil is wet and it rained
:ref:`logical_equality<test_logical_equality>`                  water only if soil is dry and it did not rain, water if soil is wet and it did not rain
:ref:`material_implication<test_material_implication>`          do not water if soil is dry and it rained
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