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

the possible states for the inputs are

=====================  =====================
motion (first)          code (second)
=====================  =====================
:green:`motion`        :green:`right code`
:green:`motion`        :red:`wrong code`
:red:`no motion`       :green:`right code`
:red:`no motion`       :red:`wrong code`
=====================  =====================

and the possible outputs are

* :green:`ON`
* :red:`OFF`

the :ref:`truth table` shows all the logically possible states of the alarm

* :ref:`contradiction<test_contradiction>`: ``return False``

  =====================  =====================  =====================
  motion (first)          code (second)         output
  =====================  =====================  =====================
  :green:`motion`        :green:`right code`    :red:`OFF`
  :green:`motion`        :red:`wrong code`      :red:`OFF`
  :red:`no motion`       :green:`right code`    :red:`OFF`
  :red:`no motion`       :red:`wrong code`      :red:`OFF`
  =====================  =====================  =====================

  the alarm always outputs :red:`OFF`. It does not care about the inputs.

* :ref:`logical_conjunction<test_logical_conjunction>`: ``return first and second``

  =====================  =====================  =====================
  motion (first)          code (second)         output
  =====================  =====================  =====================
  :green:`motion`        :green:`right code`    :green:`ON`
  :green:`motion`        :red:`wrong code`      :red:`OFF`
  :red:`no motion`       :green:`right code`    :red:`OFF`
  :red:`no motion`       :red:`wrong code`      :red:`OFF`
  =====================  =====================  =====================

  outputs :green:`ON` only if there is :green:`motion` AND the :green:`right code` is entered. Authorized entry.

* :ref:`project_second<test_project_second>`: ``return second``

  =====================  =====================  =====================
  motion (first)          code (second)         output
  =====================  =====================  =====================
  :green:`motion`        :green:`right code`    :green:`ON`
  :green:`motion`        :red:`wrong code`      :red:`OFF`
  :red:`no motion`       :green:`right code`    :green:`ON`
  :red:`no motion`       :red:`wrong code`      :red:`OFF`
  =====================  =====================  =====================

  outputs :green:`ON` if the :green:`right code` is entered, it does not care about motion. How is the :green:`right code` entered without motion?

* :ref:`converse_non_implication<test_converse_non_implication>`: ``return (not first) and second``

  =====================  =====================  =====================
  motion (first)          code (second)         output
  =====================  =====================  =====================
  :green:`motion`        :green:`right code`    :red:`OFF`
  :green:`motion`        :red:`wrong code`      :red:`OFF`
  :red:`no motion`       :green:`right code`    :green:`ON`
  :red:`no motion`       :red:`wrong code`      :red:`OFF`
  =====================  =====================  =====================

  outputs :green:`ON` only if there is :red:`NOT motion` AND the :green:`right code` is entered. How is the :green:`right code` entered without motion?

* :ref:`negate_first<test_negate_first>`: ``return not first``

  =====================  =====================  =====================
  motion (first)          code (second)         output
  =====================  =====================  =====================
  :green:`motion`        :green:`right code`    :red:`OFF`
  :green:`motion`        :red:`wrong code`      :red:`OFF`
  :red:`no motion`       :green:`right code`    :green:`ON`
  :red:`no motion`       :red:`wrong code`      :green:`ON`
  =====================  =====================  =====================

  outputs :green:`ON` only if there is :red:`NOT motion`, it does not care about the code.

* :ref:`logical_nand<test_logical_nand>`: ``return not (first and second)``

  =====================  =====================  =====================
  motion (first)          code (second)         output
  =====================  =====================  =====================
  :green:`motion`        :green:`right code`    :red:`OFF`
  :green:`motion`        :red:`wrong code`      :green:`ON`
  :red:`no motion`       :green:`right code`    :green:`ON`
  :red:`no motion`       :red:`wrong code`      :green:`ON`
  =====================  =====================  =====================

  outputs :red:`OFF` only if there is :green:`motion` AND the :green:`right code` is entered.

* :ref:`tautology<test_tautology>`: ``return True``

  =====================  =====================  =====================
  motion (first)          code (second)         output
  =====================  =====================  =====================
  :green:`motion`        :green:`right code`    :green:`ON`
  :green:`motion`        :red:`wrong code`      :green:`ON`
  :red:`no motion`       :green:`right code`    :green:`ON`
  :red:`no motion`       :red:`wrong code`      :green:`ON`
  =====================  =====================  =====================

  outputs :green:`ON` always, it does not care about the inputs.

* :ref:`logical_disjunction<test_logical_disjunction>`: ``return first or second``

  =====================  =====================  =====================
  motion (first)          code (second)         output
  =====================  =====================  =====================
  :green:`motion`        :green:`right code`    :green:`ON`
  :green:`motion`        :red:`wrong code`      :green:`ON`
  :red:`no motion`       :green:`right code`    :green:`ON`
  :red:`no motion`       :red:`wrong code`      :red:`OFF`
  =====================  =====================  =====================

  outputs :red:`OFF` only if there is :red:`NOT motion` and :red:`NOT the right code` is entered. How is the code entered without motion?

* :ref:`exclusive_disjunction<test_exclusive_disjunction>`: ``return (not (first and second) and (first or second))``

  =====================  =====================  =====================
  motion (first)          code (second)         output
  =====================  =====================  =====================
  :green:`motion`        :green:`right code`    :red:`OFF`
  :green:`motion`        :red:`wrong code`      :green:`ON`
  :red:`no motion`       :green:`right code`    :green:`ON`
  :red:`no motion`       :red:`wrong code`      :red:`OFF`
  =====================  =====================  =====================

  - outputs :red:`OFF` if there is :green:`motion` AND the :green:`right code` is entered
  - outputs :red:`OFF` if there is :red:`NOT motion` AND :red:`NOT the right code` is entered

  Wait a minute! Why is "motion AND the :green:`right code`" the same as "NOT motion AND :red:`NOT the right code`"?

* :ref:`material_non_implication<test_material_non_implication>`: ``return first and (not second)``

  =====================  =====================  =====================
  motion (first)          code (second)         output
  =====================  =====================  =====================
  :green:`motion`        :green:`right code`    :red:`OFF`
  :green:`motion`        :red:`wrong code`      :green:`ON`
  :red:`no motion`       :green:`right code`    :red:`OFF`
  :red:`no motion`       :red:`wrong code`      :red:`OFF`
  =====================  =====================  =====================

  outputs :green:`ON` if there is :green:`motion` AND :red:`NOT the right code` is entered. Is there a burglar?

* :ref:`project_first<test_project_first>`: ``return first``

  =====================  =====================  =====================
  motion (first)          code (second)         output
  =====================  =====================  =====================
  :green:`motion`        :green:`right code`    :green:`ON`
  :green:`motion`        :red:`wrong code`      :green:`ON`
  :red:`no motion`       :green:`right code`    :red:`OFF`
  :red:`no motion`       :red:`wrong code`      :red:`OFF`
  =====================  =====================  =====================

  outputs :green:`ON` if there is :green:`motion`, it does not matter what code is entered.

* :ref:`converse_implication<test_converse_implication>`: ``return first or (not second)``

  =====================  =====================  =====================
  motion (first)          code (second)         output
  =====================  =====================  =====================
  :green:`motion`        :green:`right code`    :green:`ON`
  :green:`motion`        :red:`wrong code`      :green:`ON`
  :red:`no motion`       :green:`right code`    :red:`OFF`
  :red:`no motion`       :red:`wrong code`      :green:`ON`
  =====================  =====================  =====================

  outputs :red:`OFF` if there is :red:`NOT motion` AND the :green:`right code` is entered. How is the code entered if there is no motion?

* :ref:`negate_second<test_negate_second>`: ``return not second``

  =====================  =====================  =====================
  motion (first)          code (second)         output
  =====================  =====================  =====================
  :green:`motion`        :green:`right code`    :red:`OFF`
  :green:`motion`        :red:`wrong code`      :green:`ON`
  :red:`no motion`       :green:`right code`    :red:`OFF`
  :red:`no motion`       :red:`wrong code`      :green:`ON`
  =====================  =====================  =====================

  outputs :green:`ON` only if :red:`NOT the right code` is entered, it does not care about motion.

* :ref:`logical_nor<test_logical_nor>`: ``return not (first or second)``

  =====================  =====================  =====================
  motion (first)          code (second)         output
  =====================  =====================  =====================
  :green:`motion`        :green:`right code`    :red:`OFF`
  :green:`motion`        :red:`wrong code`      :red:`OFF`
  :red:`no motion`       :green:`right code`    :red:`OFF`
  :red:`no motion`       :red:`wrong code`      :green:`ON`
  =====================  =====================  =====================

  outputs :green:`ON` only if there is :red:`NOT motion` AND :red:`NOT the right code` is entered

* :ref:`logical_equality<test_logical_equality>`: ``return (not first or second) and (first or not second)``

  =====================  =====================  =====================
  motion (first)          code (second)         output
  =====================  =====================  =====================
  :green:`motion`        :green:`right code`    :green:`ON`
  :green:`motion`        :red:`wrong code`      :red:`OFF`
  :red:`no motion`       :green:`right code`    :red:`OFF`
  :red:`no motion`       :red:`wrong code`      :green:`ON`
  =====================  =====================  =====================

  - outputs :green:`ON` if there is :green:`motion` AND the :green:`right code` is entered
  - outputs :green:`ON` if there is :red:`NOT motion` AND :red:`NOT the right code` is entered

* :ref:`material_implication<test_material_implication>`: ``return (not first) or second``

  =====================  =====================  =====================
  motion (first)          code (second)         output
  =====================  =====================  =====================
  :green:`motion`        :green:`right code`    :green:`ON`
  :green:`motion`        :red:`wrong code`      :red:`OFF`
  :red:`no motion`       :green:`right code`    :green:`ON`
  :red:`no motion`       :red:`wrong code`      :green:`ON`
  =====================  =====================  =====================

  output is :red:`OFF` if there is :green:`motion` AND :red:`NOT the right code` is entered.

I do not need to know or memorize every operation, the only operations that matter in this case are

* :ref:`logical_conjunction<test_logical_conjunction>`, where it outputs :green:`ON` only if there is :green:`motion` AND the :green:`right code` is entered. I assume this is an authorized entry.
* :ref:`material_non_implication<test_material_non_implication>`, where it outputs :green:`ON` if there is :green:`motion` AND the :red:`wrong code` is entered. I assume this is NOT an authorized entry.

Because I want to first check if there is motion, then it check if the code entered is correct.

----

=================================================================================
hiring
=================================================================================

----

if the inputs are

- is the person a strong option?
- is the person a strong fit?

the possible states for the inputs are

======================  =====================
option (first)          fit (second)
======================  =====================
:green:`strong option`  :green:`strong fit`
:green:`strong option`  :red:`weak fit`
:red:`weak option`      :green:`strong fit`
:red:`weak option`      :red:`weak fit`
======================  =====================

and the possible outputs are

* :green:`HIRE`
* :red:`REJECT`

the :ref:`truth table` shows all the logically possible states of

* :ref:`contradiction<test_contradiction>`: ``return False``

  ======================  =====================  =====================
  option (first)          fit (second)           output
  ======================  =====================  =====================
  :green:`strong option`  :green:`strong fit`    :red:`REJECT`
  :green:`strong option`  :red:`weak fit`        :red:`REJECT`
  :red:`weak option`      :green:`strong fit`    :red:`REJECT`
  :red:`weak option`      :red:`weak fit`        :red:`REJECT`
  ======================  =====================  =====================

  always :red:`REJECT`. The inputs do not matter.

* :ref:`logical_conjunction<test_logical_conjunction>`: ``return first and second``

  ======================  =====================  =====================
  option (first)          fit (second)           output
  ======================  =====================  =====================
  :green:`strong option`  :green:`strong fit`    :green:`HIRE`
  :green:`strong option`  :red:`weak fit`        :red:`REJECT`
  :red:`weak option`      :green:`strong fit`    :red:`REJECT`
  :red:`weak option`      :red:`weak fit`        :red:`REJECT`
  ======================  =====================  =====================

  :green:`HIRE` only if it is a :green:`strong option` AND it is a :green:`strong fit`. I only hire A players.

* :ref:`project_second<test_project_second>`: ``return second``

  ======================  =====================  =====================
  option (first)          fit (second)           output
  ======================  =====================  =====================
  :green:`strong option`  :green:`strong fit`    :green:`HIRE`
  :green:`strong option`  :red:`weak fit`        :red:`REJECT`
  :red:`weak option`      :green:`strong fit`    :green:`HIRE`
  :red:`weak option`      :red:`weak fit`        :red:`REJECT`
  ======================  =====================  =====================

  :green:`HIRE` if it is a :green:`strong fit`, it does not matter it is a :green:`strong option` or  :red:`weak option`. I like this person and do not care about whether it is a strong or weak option. How does the team feel about this?

* :ref:`converse_non_implication<test_converse_non_implication>`: ``return (not first) and second``

  ======================  =====================  =====================
  option (first)          fit (second)           output
  ======================  =====================  =====================
  :green:`strong option`  :green:`strong fit`    :red:`REJECT`
  :green:`strong option`  :red:`weak fit`        :red:`REJECT`
  :red:`weak option`      :green:`strong fit`    :green:`HIRE`
  :red:`weak option`      :red:`weak fit`        :red:`REJECT`
  ======================  =====================  =====================

  :green:`HIRE` only if it is :red:`NOT a strong option` AND it is a :green:`strong fit`. What is the benefit of a weak option that is a strong fit?

* :ref:`negate_first<test_negate_first>`: ``return not first``

  ======================  =====================  =====================
  option (first)          fit (second)           output
  ======================  =====================  =====================
  :green:`strong option`  :green:`strong fit`    :red:`REJECT`
  :green:`strong option`  :red:`weak fit`        :red:`REJECT`
  :red:`weak option`      :green:`strong fit`    :green:`HIRE`
  :red:`weak option`      :red:`weak fit`        :green:`HIRE`
  ======================  =====================  =====================

  :green:`HIRE` only if it is :red:`NOT a strong option`, I do not care about fit. Why would I hire a weak option?

* :ref:`logical_nand<test_logical_nand>`: ``return not (first and second)``

  ======================  =====================  =====================
  option (first)          fit (second)           output
  ======================  =====================  =====================
  :green:`strong option`  :green:`strong fit`    :red:`REJECT`
  :green:`strong option`  :red:`weak fit`        :green:`HIRE`
  :red:`weak option`      :green:`strong fit`    :green:`HIRE`
  :red:`weak option`      :red:`weak fit`        :green:`HIRE`
  ======================  =====================  =====================

  :red:`REJECT` only if it is a :green:`strong option` AND it is a :green:`strong fit`. Why do I not want a strong option that is a strong fit?

* :ref:`tautology<test_tautology>`: ``return True``

  ======================  =====================  =====================
  option (first)          fit (second)           output
  ======================  =====================  =====================
  :green:`strong option`  :green:`strong fit`    :green:`HIRE`
  :green:`strong option`  :red:`weak fit`        :green:`HIRE`
  :red:`weak option`      :green:`strong fit`    :green:`HIRE`
  :red:`weak option`      :red:`weak fit`        :green:`HIRE`
  ======================  =====================  =====================

  :green:`HIRE` always, it does not care about the inputs. Anybody can get a job here.

* :ref:`logical_disjunction<test_logical_disjunction>`: ``return first or second``

  ======================  =====================  =====================
  option (first)          fit (second)           output
  ======================  =====================  =====================
  :green:`strong option`  :green:`strong fit`    :green:`HIRE`
  :green:`strong option`  :red:`weak fit`        :green:`HIRE`
  :red:`weak option`      :green:`strong fit`    :green:`HIRE`
  :red:`weak option`      :red:`weak fit`        :red:`REJECT`
  ======================  =====================  =====================

  :red:`REJECT` only if it is :red:`NOT a strong option` and :red:`NOT a strong fit`. I hire just about anybody but have to draw the line somewhere.

* :ref:`exclusive_disjunction<test_exclusive_disjunction>`: ``return (not (first and second) and (first or second))``

  ======================  =====================  =====================
  option (first)          fit (second)           output
  ======================  =====================  =====================
  :green:`strong option`  :green:`strong fit`    :red:`REJECT`
  :green:`strong option`  :red:`weak fit`        :green:`HIRE`
  :red:`weak option`      :green:`strong fit`    :green:`HIRE`
  :red:`weak option`      :red:`weak fit`        :red:`REJECT`
  ======================  =====================  =====================

  - :red:`REJECT` if it is a :green:`strong option` AND it is a :green:`strong fit`
  - :red:`REJECT` if it is :red:`NOT a strong option` AND :red:`NOT a strong fit`

  Wait a minute! Why is "strong option AND strong fit" the same as "weak option AND weak fit"? Do I just not like extremes?

* :ref:`material_non_implication<test_material_non_implication>`: ``return first and (not second)``

  ======================  =====================  =====================
  option (first)          fit (second)           output
  ======================  =====================  =====================
  :green:`strong option`  :green:`strong fit`    :red:`REJECT`
  :green:`strong option`  :red:`weak fit`        :green:`HIRE`
  :red:`weak option`      :green:`strong fit`    :red:`REJECT`
  :red:`weak option`      :red:`weak fit`        :red:`REJECT`
  ======================  =====================  =====================

  :green:`HIRE` if it is a :green:`strong option` AND :red:`NOT a strong fit`. How does the team feel about this?

* :ref:`project_first<test_project_first>`: ``return first``

  ======================  =====================  =====================
  option (first)          fit (second)           output
  ======================  =====================  =====================
  :green:`strong option`  :green:`strong fit`    :green:`HIRE`
  :green:`strong option`  :red:`weak fit`        :green:`HIRE`
  :red:`weak option`      :green:`strong fit`    :red:`REJECT`
  :red:`weak option`      :red:`weak fit`        :red:`REJECT`
  ======================  =====================  =====================

  :green:`HIRE` if it is a :green:`strong option`, I do not care about fit.

* :ref:`converse_implication<test_converse_implication>`: ``return first or (not second)``

  ======================  =====================  =====================
  option (first)          fit (second)           output
  ======================  =====================  =====================
  :green:`strong option`  :green:`strong fit`    :green:`HIRE`
  :green:`strong option`  :red:`weak fit`        :green:`HIRE`
  :red:`weak option`      :green:`strong fit`    :red:`REJECT`
  :red:`weak option`      :red:`weak fit`        :green:`HIRE`
  ======================  =====================  =====================

  :red:`REJECT` if it is :red:`NOT a strong option` AND it is a :green:`strong fit`. Did I just hire a weak option that is also a weak fit?

* :ref:`negate_second<test_negate_second>`: ``return not second``

  ======================  =====================  =====================
  option (first)          fit (second)           output
  ======================  =====================  =====================
  :green:`strong option`  :green:`strong fit`    :red:`REJECT`
  :green:`strong option`  :red:`weak fit`        :green:`HIRE`
  :red:`weak option`      :green:`strong fit`    :red:`REJECT`
  :red:`weak option`      :red:`weak fit`        :green:`HIRE`
  ======================  =====================  =====================

  :green:`HIRE` only if :red:`NOT a strong fit`, I do not care whether it is a strong or weak option.

* :ref:`logical_nor<test_logical_nor>`: ``return not (first or second)``

  ======================  =====================  =====================
  option (first)          fit (second)           output
  ======================  =====================  =====================
  :green:`strong option`  :green:`strong fit`    :red:`REJECT`
  :green:`strong option`  :red:`weak fit`        :red:`REJECT`
  :red:`weak option`      :green:`strong fit`    :red:`REJECT`
  :red:`weak option`      :red:`weak fit`        :green:`HIRE`
  ======================  =====================  =====================

  :green:`HIRE` only if it is :red:`NOT a strong option` AND :red:`NOT a strong fit`. Trouble.

* :ref:`logical_equality<test_logical_equality>`: ``return (not first or second) and (first or not second)``

  ======================  =====================  =====================
  option (first)          fit (second)           output
  ======================  =====================  =====================
  :green:`strong option`  :green:`strong fit`    :green:`HIRE`
  :green:`strong option`  :red:`weak fit`        :red:`REJECT`
  :red:`weak option`      :green:`strong fit`    :red:`REJECT`
  :red:`weak option`      :red:`weak fit`        :green:`HIRE`
  ======================  =====================  =====================

  - :green:`HIRE` if it is a :green:`strong option` AND it is a :green:`strong fit`
  - :green:`HIRE` if it is :red:`NOT a strong option` AND :red:`NOT a strong fit`

  maybe I need someone else making these decisions

* :ref:`material_implication<test_material_implication>`: ``return (not first) or second``

  ======================  =====================  =====================
  option (first)          fit (second)           output
  ======================  =====================  =====================
  :green:`strong option`  :green:`strong fit`    :green:`HIRE`
  :green:`strong option`  :red:`weak fit`        :red:`REJECT`
  :red:`weak option`      :green:`strong fit`    :green:`HIRE`
  :red:`weak option`      :red:`weak fit`        :green:`HIRE`
  ======================  =====================  =====================

  :red:`REJECT` if it is a :green:`strong option` AND :red:`NOT a strong fit`.

I do not need to know or memorize every operation, the only operations that matter in this case are

* :ref:`logical_conjunction<test_logical_conjunction>`, :green:`HIRE` only if it is a :green:`strong option` AND it is a :green:`strong fit` if I only want A players that can work with the team.
* :ref:`material_non_implication<test_material_non_implication>`, if I am okay with hiring someone who is a :green:`strong option` AND :red:`NOT a strong fit`.
* maybe :ref:`logical_disjunction<test_logical_disjunction>`, if I will :green:`HIRE` pretty much anyone and only :red:`REJECT` a :red:`weak option` that is also a :red:`weak fit`.

----

=================================================================================
store discount policy
=================================================================================

----

if the inputs are

- does the person have a coupon?
- is the person a member?

the possible states for the inputs are

======================  =====================
coupon (first)          member (second)
======================  =====================
:green:`coupon`         :green:`member`
:green:`coupon`         :red:`NOT a member`
:red:`no coupon`        :green:`member`
:red:`no coupon`        :red:`NOT a member`
======================  =====================

and the possible outputs are

* :green:`DISCOUNT`
* :red:`NO DISCOUNT`

the :ref:`truth table` shows all the logically possible states of

* :ref:`contradiction<test_contradiction>`: ``return False``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :red:`NO DISCOUNT`
  :green:`coupon`         :red:`NOT a member`    :red:`NO DISCOUNT`
  :red:`no coupon`        :green:`member`        :red:`NO DISCOUNT`
  :red:`no coupon`        :red:`NOT a member`    :red:`NO DISCOUNT`
  ======================  =====================  =====================

  always :red:`NO DISCOUNT`. I never give a discount, everyone pays full price.

* :ref:`logical_conjunction<test_logical_conjunction>`: ``return first and second``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :green:`DISCOUNT`
  :green:`coupon`         :red:`NOT a member`    :red:`NO DISCOUNT`
  :red:`no coupon`        :green:`member`        :red:`NO DISCOUNT`
  :red:`no coupon`        :red:`NOT a member`    :red:`NO DISCOUNT`
  ======================  =====================  =====================

  :green:`DISCOUNT` only if the person has a :green:`coupon` AND person is a :green:`member`. A loyalty/rewards program.

* :ref:`project_second<test_project_second>`: ``return second``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :green:`DISCOUNT`
  :green:`coupon`         :red:`NOT a member`    :red:`NO DISCOUNT`
  :red:`no coupon`        :green:`member`        :green:`DISCOUNT`
  :red:`no coupon`        :red:`NOT a member`    :red:`NO DISCOUNT`
  ======================  =====================  =====================

  :green:`DISCOUNT` if the person is a :green:`member`, it does not matter if they have a :green:`coupon` or  :red:`no coupon`. I give the discount only to members. A loyalty program. Sorry you brought a coupon.

* :ref:`converse_non_implication<test_converse_non_implication>`: ``return (not first) and second``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :red:`NO DISCOUNT`
  :green:`coupon`         :red:`NOT a member`    :red:`NO DISCOUNT`
  :red:`no coupon`        :green:`member`        :green:`DISCOUNT`
  :red:`no coupon`        :red:`NOT a member`    :red:`NO DISCOUNT`
  ======================  =====================  =====================

  :green:`DISCOUNT` only if the person does :red:`NOT have a coupon` AND the person is a :green:`member`. What happens to the members who have coupons?

* :ref:`negate_first<test_negate_first>`: ``return not first``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :red:`NO DISCOUNT`
  :green:`coupon`         :red:`NOT a member`    :red:`NO DISCOUNT`
  :red:`no coupon`        :green:`member`        :green:`DISCOUNT`
  :red:`no coupon`        :red:`NOT a member`    :green:`DISCOUNT`
  ======================  =====================  =====================

  :green:`DISCOUNT` only if the person does :red:`NOT have a coupon`, I do not care if it is a member or not. Do I want all the people with coupons to be upset?

* :ref:`logical_nand<test_logical_nand>`: ``return not (first and second)``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :red:`NO DISCOUNT`
  :green:`coupon`         :red:`NOT a member`    :green:`DISCOUNT`
  :red:`no coupon`        :green:`member`        :green:`DISCOUNT`
  :red:`no coupon`        :red:`NOT a member`    :green:`DISCOUNT`
  ======================  =====================  =====================

  :red:`NO DISCOUNT` only if the person has a :green:`coupon` AND is a :green:`member`. I might already have a benefit I give to members and do not want to give discounts with that.

* :ref:`tautology<test_tautology>`: ``return True``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :green:`DISCOUNT`
  :green:`coupon`         :red:`NOT a member`    :green:`DISCOUNT`
  :red:`no coupon`        :green:`member`        :green:`DISCOUNT`
  :red:`no coupon`        :red:`NOT a member`    :green:`DISCOUNT`
  ======================  =====================  =====================

  :green:`DISCOUNT` always. I am always giving a discount, everybody loves me.

* :ref:`logical_disjunction<test_logical_disjunction>`: ``return first or second``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :green:`DISCOUNT`
  :green:`coupon`         :red:`NOT a member`    :green:`DISCOUNT`
  :red:`no coupon`        :green:`member`        :green:`DISCOUNT`
  :red:`no coupon`        :red:`NOT a member`    :red:`NO DISCOUNT`
  ======================  =====================  =====================

  :red:`NO DISCOUNT` only if the person does :red:`NOT have a coupon` AND is :red:`NOT a member`. The person has to be a member, have a coupon, or both to get the discount.

* :ref:`exclusive_disjunction<test_exclusive_disjunction>`: ``return (not (first and second) and (first or second))``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :red:`NO DISCOUNT`
  :green:`coupon`         :red:`NOT a member`    :green:`DISCOUNT`
  :red:`no coupon`        :green:`member`        :green:`DISCOUNT`
  :red:`no coupon`        :red:`NOT a member`    :red:`NO DISCOUNT`
  ======================  =====================  =====================

  - :red:`NO DISCOUNT` if the person has a :green:`coupon` AND person is a :green:`member`
  - :red:`NO DISCOUNT` if it is :red:`NOT a coupon` AND :red:`NOT a member`

  Why is "coupon AND member" the same as "no coupon AND not member"? I do not want a members to have a coupon and I do not want someone who is not a member and does not have a coupon.

* :ref:`material_non_implication<test_material_non_implication>`: ``return first and (not second)``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :red:`NO DISCOUNT`
  :green:`coupon`         :red:`NOT a member`    :green:`DISCOUNT`
  :red:`no coupon`        :green:`member`        :red:`NO DISCOUNT`
  :red:`no coupon`        :red:`NOT a member`    :red:`NO DISCOUNT`
  ======================  =====================  =====================

  :green:`DISCOUNT` if the person has a :green:`coupon` AND is :red:`NOT a member`. A coupon for people that are not members.

* :ref:`project_first<test_project_first>`: ``return first``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :green:`DISCOUNT`
  :green:`coupon`         :red:`NOT a member`    :green:`DISCOUNT`
  :red:`no coupon`        :green:`member`        :red:`NO DISCOUNT`
  :red:`no coupon`        :red:`NOT a member`    :red:`NO DISCOUNT`
  ======================  =====================  =====================

  :green:`DISCOUNT` if the person has a :green:`coupon`, I do not care about if they are a member or not.

* :ref:`converse_implication<test_converse_implication>`: ``return first or (not second)``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :green:`DISCOUNT`
  :green:`coupon`         :red:`NOT a member`    :green:`DISCOUNT`
  :red:`no coupon`        :green:`member`        :red:`NO DISCOUNT`
  :red:`no coupon`        :red:`NOT a member`    :green:`DISCOUNT`
  ======================  =====================  =====================

  :red:`NO DISCOUNT` if the person :red:`does NOT have a coupon` AND is a :green:`member`.

* :ref:`negate_second<test_negate_second>`: ``return not second``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :red:`NO DISCOUNT`
  :green:`coupon`         :red:`NOT a member`    :green:`DISCOUNT`
  :red:`no coupon`        :green:`member`        :red:`NO DISCOUNT`
  :red:`no coupon`        :red:`NOT a member`    :green:`DISCOUNT`
  ======================  =====================  =====================

  :green:`DISCOUNT` only if the person is :red:`NOT a member`, I do not care if they have a coupon or not. Why do I have coupons?

* :ref:`logical_nor<test_logical_nor>`: ``return not (first or second)``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :red:`NO DISCOUNT`
  :green:`coupon`         :red:`NOT a member`    :red:`NO DISCOUNT`
  :red:`no coupon`        :green:`member`        :red:`NO DISCOUNT`
  :red:`no coupon`        :red:`NOT a member`    :green:`DISCOUNT`
  ======================  =====================  =====================

  :green:`DISCOUNT` only if the person :red:`does NOT have a coupon` AND is :red:`NOT a member`. Is it opposite day?

* :ref:`logical_equality<test_logical_equality>`: ``return (not first or second) and (first or not second)``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :green:`DISCOUNT`
  :green:`coupon`         :red:`NOT a member`    :red:`NO DISCOUNT`
  :red:`no coupon`        :green:`member`        :red:`NO DISCOUNT`
  :red:`no coupon`        :red:`NOT a member`    :green:`DISCOUNT`
  ======================  =====================  =====================

  - :green:`DISCOUNT` if the person has a :green:`coupon` AND is a :green:`member`
  - :green:`DISCOUNT` if the person :red:`does NOT have a coupon` AND is :red:`NOT a member`

  this is just confusing, what person fits both?

* :ref:`material_implication<test_material_implication>`: ``return (not first) or second``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :green:`DISCOUNT`
  :green:`coupon`         :red:`NOT a member`    :red:`NO DISCOUNT`
  :red:`no coupon`        :green:`member`        :green:`DISCOUNT`
  :red:`no coupon`        :red:`NOT a member`    :green:`DISCOUNT`
  ======================  =====================  =====================

  :red:`NO DISCOUNT` if the person has a :green:`coupon` AND :red:`NOT a member`.

I do not need to know or memorize every operation, the only operations that matter in this case are

* :ref:`logical_conjunction<test_logical_conjunction>`, if I give a :green:`DISCOUNT` only if the person has a :green:`coupon` AND person is a :green:`member` because I want to reward my most loyal customers.
* :ref:`material_non_implication<test_material_non_implication>`, if I give a :green:`DISCOUNT` to someone who has a :green:`coupon` and is :red:`NOT a member`. This could be a way to get people to become members though it is not as good as
* :ref:`project_second<test_project_second>` if I give a :green:`DISCOUNT` only if the person is a :green:`member` or
* :ref:`logical_disjunction<test_logical_disjunction>`, if I only charge a :red:`REGULAR PRICE` to the person who :red:`does NOT have a coupon` AND is :red:`not a member`.

----
----
----




the possible states for the inputs are

======================  ======================
option (first)    fit (second)
======================  ======================
:green:`strong option`  :green:`strong fit`
:green:`strong option`  :red:`weak fit`
:red:`weak option`      :green:`strong fit`
:red:`weak option`      :red:`weak fit`
======================  ======================

the inputs give the :ref:`truth table` below (all the logically possible states of hiring)

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
strong option or strong fit                                             :green:`hire`   :green:`hire`   :green:`hire`   :red:`reject`   :ref:`logical_disjunction<test_logical_disjunction>`
(not (strong option and strong fit)) and (strong option or strong fit)  :red:`reject`   :green:`hire`   :green:`hire`   :red:`reject`   :ref:`exclusive_disjunction<test_exclusive_disjunction>`
strong option and weak fit                                              :red:`reject`   :green:`hire`   :red:`reject`   :red:`reject`   :ref:`material_non_implication<test_material_non_implication>`
strong option                                                           :green:`hire`   :green:`hire`   :red:`reject`   :red:`reject`   :ref:`project_first<test_project_first>`
strong option or weak fit                                               :green:`hire`   :green:`hire`   :red:`reject`   :green:`hire`   :ref:`converse_implication<test_converse_implication>`
weak fit                                                                :red:`reject`   :green:`hire`   :red:`reject`   :green:`hire`   :ref:`negate_second<test_negate_second>`
not (strong option or strong fit)                                       :red:`reject`   :red:`reject`   :red:`reject`   :green:`hire`   :ref:`logical_nor<test_logical_nor>`
(weak option or strong fit) and (strong option or weak fit)             :green:`hire`   :red:`reject`   :red:`reject`   :green:`hire`   :ref:`logical_equality<test_logical_equality>`
weak option or strong fit                                               :green:`hire`   :red:`reject`   :green:`hire`   :green:`hire`   :ref:`material_implication<test_material_implication>`
======================================================================  =============== =============== =============== =============== ==============================================================

I can say this in English as

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

the possible states for the inputs are

======================  ======================
coupon (first)    member (second)
======================  ======================
:green:`coupon`         :green:`member`
:green:`coupon`         :red:`NOT a member`
:red:`no coupon`        :green:`member`
:red:`no coupon`        :red:`NOT a member`
======================  ======================

the inputs give the :ref:`truth table` below (all the logically possible states of the discount)

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
coupon or member                                    :green:`discount` :green:`discount` :green:`discount` :red:`regular`    :ref:`logical_disjunction<test_logical_disjunction>`
(not (coupon and member)) and (coupon or member)    :red:`regular`    :green:`discount` :green:`discount` :red:`regular`    :ref:`exclusive_disjunction<test_exclusive_disjunction>`
coupon and not member                               :red:`regular`    :green:`discount` :red:`regular`    :red:`regular`    :ref:`material_non_implication<test_material_non_implication>`
coupon                                              :green:`discount` :green:`discount` :red:`regular`    :red:`regular`    :ref:`project_first<test_project_first>`
coupon or not member                                :green:`discount` :green:`discount` :red:`regular`    :green:`discount` :ref:`converse_implication<test_converse_implication>`
not member                                          :red:`regular`    :green:`discount` :red:`regular`    :green:`discount` :ref:`negate_second<test_negate_second>`
not (coupon or member)                              :red:`regular`    :red:`regular`    :red:`regular`    :green:`discount` :ref:`logical_nor<test_logical_nor>`
(no coupon or member) and (coupon or not member)    :green:`discount` :red:`regular`    :red:`regular`    :green:`discount` :ref:`logical_equality<test_logical_equality>`
no coupon or member                                 :green:`discount` :red:`regular`    :green:`discount` :green:`discount` :ref:`material_implication<test_material_implication>`
==================================================  ================= ================= ================= ================= ==============================================================

I can say this in English as

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

the possible states for the inputs are

======================  ======================
soil (first)      rain (second)
======================  ======================
:green:`wet soil`       :green:`it rained`
:green:`wet soil`       :red:`no rain`
:red:`dry soil`         :green:`it rained`
:red:`dry soil`         :red:`no rain`
======================  ======================

the inputs give the :ref:`truth table` below (all the logically possible states of watering the plants)

======================================================  ============ ============ ============ ============ ==============================================================
water the plants                                        dry soil,    dry soil,    wet soil,    wet soil,    operation
                                                        no rain      it rained    no rain      it rained
======================================================  ============ ============ ============ ============ ==============================================================
do not water                                            :red:`no`    :red:`no`    :red:`no`    :red:`no`    :ref:`contradiction<test_contradiction>`
dry soil and no rain                                    :green:`yes` :red:`no`    :red:`no`    :red:`no`    :ref:`logical_conjunction<test_logical_conjunction>`
no rain                                                 :green:`yes` :red:`no`    :green:`yes` :red:`no`    :ref:`project_second<test_project_second>`
wet soil and no rain                                    :red:`no`    :red:`no`    :green:`yes` :red:`no`    :ref:`converse_non_implication<test_converse_non_implication>`
wet soil                                                :red:`no`    :red:`no`    :green:`yes` :green:`yes` :ref:`negate_first<test_negate_first>`
not (dry soil and no rain)                              :red:`no`    :green:`yes` :green:`yes` :green:`yes` :ref:`logical_nand<test_logical_nand>`
water                                                   :green:`yes` :green:`yes` :green:`yes` :green:`yes` :ref:`tautology<test_tautology>`
dry soil or no rain                                     :green:`yes` :green:`yes` :green:`yes` :red:`no`    :ref:`logical_disjunction<test_logical_disjunction>`
(not (dry soil and no rain)) and (dry soil or no rain)  :red:`no`    :green:`yes` :green:`yes` :red:`no`    :ref:`exclusive_disjunction<test_exclusive_disjunction>`
dry soil and it rained                                  :red:`no`    :green:`yes` :red:`no`    :red:`no`    :ref:`material_non_implication<test_material_non_implication>`
dry soil                                                :green:`yes` :green:`yes` :red:`no`    :red:`no`    :ref:`project_first<test_project_first>`
dry soil or it rained                                   :green:`yes` :green:`yes` :red:`no`    :green:`yes` :ref:`converse_implication<test_converse_implication>`
rain                                                    :red:`no`    :green:`yes` :red:`no`    :green:`yes` :ref:`negate_second<test_negate_second>`
not (dry soil or no rain)                               :red:`no`    :red:`no`    :red:`no`    :green:`yes` :ref:`logical_nor<test_logical_nor>`
(wet soil or no rain) and (dry soil or it rained)       :green:`yes` :red:`no`    :red:`no`    :green:`yes` :ref:`logical_equality<test_logical_equality>`
(wet soil) or no rain                                   :green:`yes` :red:`no`    :green:`yes` :green:`yes` :ref:`material_implication<test_material_implication>`
======================================================  ============ ============ ============ ============ ==============================================================

I can say this in English as

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


review

security alarm

========================================================  =========== =========== =========== =========== ========================================================
alarm                                                     motion,     motion,     no motion,  no motion,     operation
                                                          right code  wrong code  right code  wrong code
========================================================  =========== =========== =========== =========== ========================================================
alarm always off                                          :red:`off`  :red:`off`  :red:`off`  :red:`off`  :ref:`contradiction<test_contradiction>`
motion and wrong code                                     :red:`off`  :green:`on` :green:`on` :green:`on` :ref:`logical_conjunction<test_logical_conjunction>`
wrong code                                                :red:`off`  :green:`on` :red:`off`  :green:`on` :ref:`project_second<test_project_second>`
(no motion) and wrong code                                :green:`on` :green:`on` :red:`off`  :green:`on` :ref:`converse_non_implication<test_converse_non_implication>`
no motion                                                 :green:`on` :green:`on` :red:`off`  :red:`off`  :ref:`negate_first<test_negate_first>`
not (motion and wrong code)                               :green:`on` :red:`off`  :red:`off`  :red:`off`  :ref:`logical_nand<test_logical_nand>`
alarm always                                              :red:`off`  :red:`off`  :red:`off`  :red:`off`  :ref:`tautology<test_tautology>`
motion or wrong code                                      :red:`off`  :red:`off`  :red:`off`  :green:`on` :ref:`logical_disjunction<test_logical_disjunction>`
(not (motion and wrong code)) and (motion or wrong code)  :green:`on` :red:`off`  :red:`off`  :green:`on` :ref:`exclusive_disjunction<test_exclusive_disjunction>`
motion and right code                                     :green:`on` :red:`off`  :green:`on` :green:`on` :ref:`material_non_implication<test_material_non_implication>`
motion                                                    :red:`off`  :red:`off`  :green:`on` :green:`on` :ref:`project_first<test_project_first>`
motion or right code                                      :red:`off`  :red:`off`  :green:`on` :red:`off`  :ref:`converse_implication<test_converse_implication>`
right code                                                :green:`on` :red:`off`  :green:`on` :red:`off`  :ref:`negate_second<test_negate_second>`
not (motion or wrong code)                                :green:`on` :green:`on` :green:`on` :red:`off`  :ref:`logical_nor<test_logical_nor>`
(no motion or wrong code) and (motion or right code)      :red:`off`  :green:`on` :green:`on` :red:`off`  :ref:`logical_equality<test_logical_equality>`
no motion or wrong code                                   :red:`off`  :green:`on` :red:`off`  :red:`off`  :ref:`material_implication<test_material_implication>`
========================================================  =========== =========== =========== =========== ========================================================

I can say this in English as

==============================================================  ===========================================================================================================
operation                                                       rule
==============================================================  ===========================================================================================================
:ref:`contradiction<test_contradiction>`                        alarm always off
:ref:`logical_conjunction<test_logical_conjunction>`            alarm only if there is :green:`motion` and the code is wrong
:ref:`project_second<test_project_second>`                      alarm only if the code is wrong
:ref:`converse_non_implication<test_converse_non_implication>`  alarm only if there is no motion and the code is wrong
:ref:`negate_first<test_negate_first>`                          alarm only if there is no motion
:ref:`logical_nand<test_logical_nand>`                          alarm off only if there is :green:`motion` and the code is wrong
:ref:`tautology<test_tautology>`                                alarm always on
:ref:`logical_disjunction<test_logical_disjunction>`            alarm off if there is no motion and the code is right
:ref:`exclusive_disjunction<test_exclusive_disjunction>`        alarm off if there is :green:`motion` and the code is wrong, alarm off if there is no motion and the code is right
:ref:`material_non_implication<test_material_non_implication>`  alarm only if there is :green:`motion` and the code is right
:ref:`project_first<test_project_first>`                        alarm only if there is :green:`motion`
:ref:`converse_implication<test_converse_implication>`          alarm off only if there is no motion and the code is wrong
:ref:`negate_second<test_negate_second>`                        alarm only if the code is right
:ref:`logical_nor<test_logical_nor>`                            alarm only if there is no motion and the code is right
:ref:`logical_equality<test_logical_equality>`                  alarm if there is :green:`motion` and the code is wrong, alarm if there is no motion and the code is right
:ref:`material_implication<test_material_implication>`          alarm off only if there is :green:`motion` and the code is right
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