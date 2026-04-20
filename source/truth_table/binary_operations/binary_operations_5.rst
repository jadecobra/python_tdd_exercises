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

  outputs :red:`OFF` always, it does not care about the inputs.

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

  outputs :green:`ON` only if the :green:`right code` is entered, it does not care about motion. How is the :green:`right code` entered without motion?

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

  outputs :green:`ON` only if there is :red:`NOT motion`, it does not care if the :green:`right code` or :red:`wrong code` was entered.

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

  outputs :green:`ON` if there is :green:`motion`, it does not care if the :green:`right code` or :red:`wrong code` was entered.

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

  outputs :red:`OFF` if there is :green:`motion` AND :red:`NOT the right code` is entered.

I do not need to know or memorize every operation, the only operations that I want in this case are:

* :ref:`logical_conjunction<test_logical_conjunction>`, where it outputs :green:`ON` only if there is :green:`motion` AND the :green:`right code` is entered. I assume this is an authorized entry.
* :ref:`material_non_implication<test_material_non_implication>`, where it outputs :green:`ON` if there is :green:`motion` AND the :red:`wrong code` is entered. I assume this is NOT an authorized entry.

Because I want to first check if there is motion, then check if the code entered is correct.

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

  :green:`HIRE` if it is a :green:`strong fit`, I do not care if it is a :green:`strong option` or  :red:`weak option`. I like this person and do not care about whether it is a strong or weak option. How does the team feel about this?

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

  :green:`HIRE` only if it is :red:`NOT a strong option`, I do not care if it is a :green:`strong fit` or :red:`weak fit`. Why would I hire a weak option?

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

  :green:`HIRE` if it is a :green:`strong option`, I do not care if it is a :green:`strong fit` or :red:`weak fit`.

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

  :green:`HIRE` only if :red:`NOT a strong fit`, I do not care if it is a strong or weak option.

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

I do not need to know or memorize every operation, the only operations that I want in this case are:

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

* :green:`DISCOUNT PRICE`
* :red:`REGULAR PRICE`

the :ref:`truth table` shows all the logically possible states of

* :ref:`contradiction<test_contradiction>`: ``return False``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :red:`REGULAR PRICE`
  :green:`coupon`         :red:`NOT a member`    :red:`REGULAR PRICE`
  :red:`no coupon`        :green:`member`        :red:`REGULAR PRICE`
  :red:`no coupon`        :red:`NOT a member`    :red:`REGULAR PRICE`
  ======================  =====================  =====================

  :red:`REGULAR PRICE` always. I never give a discount, everyone pays full price.

* :ref:`logical_conjunction<test_logical_conjunction>`: ``return first and second``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :green:`DISCOUNT PRICE`
  :green:`coupon`         :red:`NOT a member`    :red:`REGULAR PRICE`
  :red:`no coupon`        :green:`member`        :red:`REGULAR PRICE`
  :red:`no coupon`        :red:`NOT a member`    :red:`REGULAR PRICE`
  ======================  =====================  =====================

  :green:`DISCOUNT PRICE` only if the person has a :green:`coupon` AND is a :green:`member`. A loyalty/rewards program.

* :ref:`project_second<test_project_second>`: ``return second``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :green:`DISCOUNT PRICE`
  :green:`coupon`         :red:`NOT a member`    :red:`REGULAR PRICE`
  :red:`no coupon`        :green:`member`        :green:`DISCOUNT PRICE`
  :red:`no coupon`        :red:`NOT a member`    :red:`REGULAR PRICE`
  ======================  =====================  =====================

  :green:`DISCOUNT PRICE` only if the person is a :green:`member`, it does not care if they have a :green:`coupon` or  :red:`no coupon`. I give the discount only to members. A loyalty program. Sorry you brought a coupon.

* :ref:`converse_non_implication<test_converse_non_implication>`: ``return (not first) and second``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :red:`REGULAR PRICE`
  :green:`coupon`         :red:`NOT a member`    :red:`REGULAR PRICE`
  :red:`no coupon`        :green:`member`        :green:`DISCOUNT PRICE`
  :red:`no coupon`        :red:`NOT a member`    :red:`REGULAR PRICE`
  ======================  =====================  =====================

  :green:`DISCOUNT PRICE` only if the person does :red:`NOT have a coupon` AND is a :green:`member`. What happens to the members who have coupons?

* :ref:`negate_first<test_negate_first>`: ``return not first``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :red:`REGULAR PRICE`
  :green:`coupon`         :red:`NOT a member`    :red:`REGULAR PRICE`
  :red:`no coupon`        :green:`member`        :green:`DISCOUNT PRICE`
  :red:`no coupon`        :red:`NOT a member`    :green:`DISCOUNT PRICE`
  ======================  =====================  =====================

  :green:`DISCOUNT PRICE` only if the person does :red:`NOT have a coupon`, I do not care if it is a member or not. Do I want all the people with coupons to be upset?

* :ref:`logical_nand<test_logical_nand>`: ``return not (first and second)``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :red:`REGULAR PRICE`
  :green:`coupon`         :red:`NOT a member`    :green:`DISCOUNT PRICE`
  :red:`no coupon`        :green:`member`        :green:`DISCOUNT PRICE`
  :red:`no coupon`        :red:`NOT a member`    :green:`DISCOUNT PRICE`
  ======================  =====================  =====================

  :red:`REGULAR PRICE` only if the person has a :green:`coupon` AND is a :green:`member`. I might already have a benefit I give to members and do not want to give discounts with that.

* :ref:`tautology<test_tautology>`: ``return True``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :green:`DISCOUNT PRICE`
  :green:`coupon`         :red:`NOT a member`    :green:`DISCOUNT PRICE`
  :red:`no coupon`        :green:`member`        :green:`DISCOUNT PRICE`
  :red:`no coupon`        :red:`NOT a member`    :green:`DISCOUNT PRICE`
  ======================  =====================  =====================

  :green:`DISCOUNT PRICE` always. I am always giving a discount, everybody loves me.

* :ref:`logical_disjunction<test_logical_disjunction>`: ``return first or second``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :green:`DISCOUNT PRICE`
  :green:`coupon`         :red:`NOT a member`    :green:`DISCOUNT PRICE`
  :red:`no coupon`        :green:`member`        :green:`DISCOUNT PRICE`
  :red:`no coupon`        :red:`NOT a member`    :red:`REGULAR PRICE`
  ======================  =====================  =====================

  :red:`REGULAR PRICE` only if the person does :red:`NOT have a coupon` AND is :red:`NOT a member`. The person has to be a member, have a coupon, or both to get the discount.

* :ref:`exclusive_disjunction<test_exclusive_disjunction>`: ``return (not (first and second) and (first or second))``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :red:`REGULAR PRICE`
  :green:`coupon`         :red:`NOT a member`    :green:`DISCOUNT PRICE`
  :red:`no coupon`        :green:`member`        :green:`DISCOUNT PRICE`
  :red:`no coupon`        :red:`NOT a member`    :red:`REGULAR PRICE`
  ======================  =====================  =====================

  - :red:`REGULAR PRICE` if the person has a :green:`coupon` AND is a :green:`member`
  - :red:`REGULAR PRICE` if the person does :red:`NOT have a coupon` AND is :red:`NOT a member`

  Why is "coupon AND member" the same as "no coupon AND not member"? I do not want a member to have a coupon and I do not want someone who is not a member and does not have a coupon.

* :ref:`material_non_implication<test_material_non_implication>`: ``return first and (not second)``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :red:`REGULAR PRICE`
  :green:`coupon`         :red:`NOT a member`    :green:`DISCOUNT PRICE`
  :red:`no coupon`        :green:`member`        :red:`REGULAR PRICE`
  :red:`no coupon`        :red:`NOT a member`    :red:`REGULAR PRICE`
  ======================  =====================  =====================

  :green:`DISCOUNT PRICE` only if the person has a :green:`coupon` AND is :red:`NOT a member`. A coupon for people that are not members.

* :ref:`project_first<test_project_first>`: ``return first``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :green:`DISCOUNT PRICE`
  :green:`coupon`         :red:`NOT a member`    :green:`DISCOUNT PRICE`
  :red:`no coupon`        :green:`member`        :red:`REGULAR PRICE`
  :red:`no coupon`        :red:`NOT a member`    :red:`REGULAR PRICE`
  ======================  =====================  =====================

  :green:`DISCOUNT PRICE` only if the person has a :green:`coupon`, I do not care about if they are a :green:`member` or :red:`NOT a member`.

* :ref:`converse_implication<test_converse_implication>`: ``return first or (not second)``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :green:`DISCOUNT PRICE`
  :green:`coupon`         :red:`NOT a member`    :green:`DISCOUNT PRICE`
  :red:`no coupon`        :green:`member`        :red:`REGULAR PRICE`
  :red:`no coupon`        :red:`NOT a member`    :green:`DISCOUNT PRICE`
  ======================  =====================  =====================

  :red:`REGULAR PRICE` only if the person :red:`does NOT have a coupon` AND is a :green:`member`.

* :ref:`negate_second<test_negate_second>`: ``return not second``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :red:`REGULAR PRICE`
  :green:`coupon`         :red:`NOT a member`    :green:`DISCOUNT PRICE`
  :red:`no coupon`        :green:`member`        :red:`REGULAR PRICE`
  :red:`no coupon`        :red:`NOT a member`    :green:`DISCOUNT PRICE`
  ======================  =====================  =====================

  :green:`DISCOUNT PRICE` only if the person is :red:`NOT a member`, I do not care if they have a coupon or not. Why do I have coupons?

* :ref:`logical_nor<test_logical_nor>`: ``return not (first or second)``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :red:`REGULAR PRICE`
  :green:`coupon`         :red:`NOT a member`    :red:`REGULAR PRICE`
  :red:`no coupon`        :green:`member`        :red:`REGULAR PRICE`
  :red:`no coupon`        :red:`NOT a member`    :green:`DISCOUNT PRICE`
  ======================  =====================  =====================

  :green:`DISCOUNT PRICE` only if the person :red:`does NOT have a coupon` AND is :red:`NOT a member`. Is it opposite day?

* :ref:`logical_equality<test_logical_equality>`: ``return (not first or second) and (first or not second)``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :green:`DISCOUNT PRICE`
  :green:`coupon`         :red:`NOT a member`    :red:`REGULAR PRICE`
  :red:`no coupon`        :green:`member`        :red:`REGULAR PRICE`
  :red:`no coupon`        :red:`NOT a member`    :green:`DISCOUNT PRICE`
  ======================  =====================  =====================

  - :green:`DISCOUNT PRICE` if the person has a :green:`coupon` AND is a :green:`member`
  - :green:`DISCOUNT PRICE` if the person :red:`does NOT have a coupon` AND is :red:`NOT a member`

  this is just confusing, which meets both conditions?

* :ref:`material_implication<test_material_implication>`: ``return (not first) or second``

  ======================  =====================  =====================
  coupon (first)          member (second)        output
  ======================  =====================  =====================
  :green:`coupon`         :green:`member`        :green:`DISCOUNT PRICE`
  :green:`coupon`         :red:`NOT a member`    :red:`REGULAR PRICE`
  :red:`no coupon`        :green:`member`        :green:`DISCOUNT PRICE`
  :red:`no coupon`        :red:`NOT a member`    :green:`DISCOUNT PRICE`
  ======================  =====================  =====================

  :red:`REGULAR PRICE` if the person has a :green:`coupon` AND :red:`NOT a member`.

I do not need to know or memorize every operation, the only operations that I want in this case are:

* :ref:`logical_conjunction<test_logical_conjunction>`, if I give a :green:`DISCOUNT PRICE` only if the person has a :green:`coupon` AND is a :green:`member` because I want to reward my most loyal customers.
* :ref:`material_non_implication<test_material_non_implication>`, if I give a :green:`DISCOUNT PRICE` to someone who has a :green:`coupon` and is :red:`NOT a member`. This could be a way to get people to become members though it is not as good as
* :ref:`project_second<test_project_second>` if I give a :green:`DISCOUNT PRICE` only if the person is a :green:`member` or
* :ref:`logical_disjunction<test_logical_disjunction>`, if I only charge a :red:`REGULAR PRICE` to the person who :red:`does NOT have a coupon` AND is :red:`not a member`.

----

=================================================================================
watering plants
=================================================================================

----

if the inputs are

- is the soil dry?
- did it rain?

the possible states for the inputs are

======================  =====================
soil (first)            rain (second)
======================  =====================
:green:`soil is dry`    :green:`it rained`
:green:`soil is dry`    :red:`NOT rain`
:red:`soil is wet`      :green:`it rained`
:red:`soil is wet`      :red:`NOT rain`
======================  =====================

and the possible outputs are

* :green:`WATER`
* :red:`DO NOT WATER`

the :ref:`truth table` shows all the logically possible states of

* :ref:`contradiction<test_contradiction>`: ``return False``

  ======================  =====================  =====================
  soil (first)            rain (second)          output
  ======================  =====================  =====================
  :green:`soil is dry`    :green:`it rained`     :red:`DO NOT WATER`
  :green:`soil is dry`    :red:`NOT rain`        :red:`DO NOT WATER`
  :red:`soil is wet`      :green:`it rained`     :red:`DO NOT WATER`
  :red:`soil is wet`      :red:`NOT rain`        :red:`DO NOT WATER`
  ======================  =====================  =====================

  :red:`DO NOT WATER` always. I never water, survival of the fittest.

* :ref:`logical_conjunction<test_logical_conjunction>`: ``return first and second``

  ======================  =====================  =====================
  soil (first)            rain (second)          output
  ======================  =====================  =====================
  :green:`soil is dry`    :green:`it rained`     :green:`WATER`
  :green:`soil is dry`    :red:`NOT rain`        :red:`DO NOT WATER`
  :red:`soil is wet`      :green:`it rained`     :red:`DO NOT WATER`
  :red:`soil is wet`      :red:`NOT rain`        :red:`DO NOT WATER`
  ======================  =====================  =====================

  :green:`WATER` only if the :green:`soil is dry` AND :green:`it rained`. Why is the soil still dry after it rained?

* :ref:`project_second<test_project_second>`: ``return second``

  ======================  =====================  =====================
  soil (first)            rain (second)          output
  ======================  =====================  =====================
  :green:`soil is dry`    :green:`it rained`     :green:`WATER`
  :green:`soil is dry`    :red:`NOT rain`        :red:`DO NOT WATER`
  :red:`soil is wet`      :green:`it rained`     :green:`WATER`
  :red:`soil is wet`      :red:`NOT rain`        :red:`DO NOT WATER`
  ======================  =====================  =====================

  :green:`WATER` only if :green:`it rained`, I do not care if the :green:`soil is dry` or  :red:`wet`. Am I trying to make a swamp?

* :ref:`converse_non_implication<test_converse_non_implication>`: ``return (not first) and second``

  ======================  =====================  =====================
  soil (first)            rain (second)          output
  ======================  =====================  =====================
  :green:`soil is dry`    :green:`it rained`     :red:`DO NOT WATER`
  :green:`soil is dry`    :red:`NOT rain`        :red:`DO NOT WATER`
  :red:`soil is wet`      :green:`it rained`     :green:`WATER`
  :red:`soil is wet`      :red:`NOT rain`        :red:`DO NOT WATER`
  ======================  =====================  =====================

  :green:`WATER` only if the :red:`soil is wet` AND :green:`it rained`. Maybe this is why all my plants die, I keep over watering them.

* :ref:`negate_first<test_negate_first>`: ``return not first``

  ======================  =====================  =====================
  soil (first)            rain (second)          output
  ======================  =====================  =====================
  :green:`soil is dry`    :green:`it rained`     :red:`DO NOT WATER`
  :green:`soil is dry`    :red:`NOT rain`        :red:`DO NOT WATER`
  :red:`soil is wet`      :green:`it rained`     :green:`WATER`
  :red:`soil is wet`      :red:`NOT rain`        :green:`WATER`
  ======================  =====================  =====================

  :green:`WATER` only if the :red:`soil is wet`, I do not care if it :green:`rained` or did :red:`NOT rain`. I must really want a swamp.

* :ref:`logical_nand<test_logical_nand>`: ``return not (first and second)``

  ======================  =====================  =====================
  soil (first)            rain (second)          output
  ======================  =====================  =====================
  :green:`soil is dry`    :green:`it rained`     :red:`DO NOT WATER`
  :green:`soil is dry`    :red:`NOT rain`        :green:`WATER`
  :red:`soil is wet`      :green:`it rained`     :green:`WATER`
  :red:`soil is wet`      :red:`NOT rain`        :green:`WATER`
  ======================  =====================  =====================

  :red:`DO NOT WATER` only if the :green:`soil is dry` AND :green:`it rained`. Why do I water when the soil is wet and it rained?

* :ref:`tautology<test_tautology>`: ``return True``

  ======================  =====================  =====================
  soil (first)            rain (second)          output
  ======================  =====================  =====================
  :green:`soil is dry`    :green:`it rained`     :green:`WATER`
  :green:`soil is dry`    :red:`NOT rain`        :green:`WATER`
  :red:`soil is wet`      :green:`it rained`     :green:`WATER`
  :red:`soil is wet`      :red:`NOT rain`        :green:`WATER`
  ======================  =====================  =====================

  :green:`WATER` always.

* :ref:`logical_disjunction<test_logical_disjunction>`: ``return first or second``

  ======================  =====================  =====================
  soil (first)            rain (second)          output
  ======================  =====================  =====================
  :green:`soil is dry`    :green:`it rained`     :green:`WATER`
  :green:`soil is dry`    :red:`NOT rain`        :green:`WATER`
  :red:`soil is wet`      :green:`it rained`     :green:`WATER`
  :red:`soil is wet`      :red:`NOT rain`        :red:`DO NOT WATER`
  ======================  =====================  =====================

  :red:`DO NOT WATER` only if the :red:`soil is wet` AND it did :red:`NOT rain`. I pretty much always water unless the soil is wet and it did not rain.

* :ref:`exclusive_disjunction<test_exclusive_disjunction>`: ``return (not (first and second) and (first or second))``

  ======================  =====================  =====================
  soil (first)            rain (second)          output
  ======================  =====================  =====================
  :green:`soil is dry`    :green:`it rained`     :red:`DO NOT WATER`
  :green:`soil is dry`    :red:`NOT rain`        :green:`WATER`
  :red:`soil is wet`      :green:`it rained`     :green:`WATER`
  :red:`soil is wet`      :red:`NOT rain`        :red:`DO NOT WATER`
  ======================  =====================  =====================

  - :red:`DO NOT WATER` if the :green:`soil is dry` AND :green:`it rained`
  - :red:`DO NOT WATER` if the :red:`soil is wet` AND :red:`it did NOT rain`

* :ref:`material_non_implication<test_material_non_implication>`: ``return first and (not second)``

  ======================  =====================  =====================
  soil (first)            rain (second)          output
  ======================  =====================  =====================
  :green:`soil is dry`    :green:`it rained`     :red:`DO NOT WATER`
  :green:`soil is dry`    :red:`NOT rain`        :green:`WATER`
  :red:`soil is wet`      :green:`it rained`     :red:`DO NOT WATER`
  :red:`soil is wet`      :red:`NOT rain`        :red:`DO NOT WATER`
  ======================  =====================  =====================

  :green:`WATER` only if the :green:`soil is dry` AND it did :red:`NOT rain`. I think the plants might like this.

* :ref:`project_first<test_project_first>`: ``return first``

  ======================  =====================  =====================
  soil (first)            rain (second)          output
  ======================  =====================  =====================
  :green:`soil is dry`    :green:`it rained`     :green:`WATER`
  :green:`soil is dry`    :red:`NOT rain`        :green:`WATER`
  :red:`soil is wet`      :green:`it rained`     :red:`DO NOT WATER`
  :red:`soil is wet`      :red:`NOT rain`        :red:`DO NOT WATER`
  ======================  =====================  =====================

  :green:`WATER` only if the :green:`soil is dry`, I do not care if it :green:`rained` or did :red:`NOT rain`. Maybe there was not enough rain.

* :ref:`converse_implication<test_converse_implication>`: ``return first or (not second)``

  ======================  =====================  =====================
  soil (first)            rain (second)          output
  ======================  =====================  =====================
  :green:`soil is dry`    :green:`it rained`     :green:`WATER`
  :green:`soil is dry`    :red:`NOT rain`        :green:`WATER`
  :red:`soil is wet`      :green:`it rained`     :red:`DO NOT WATER`
  :red:`soil is wet`      :red:`NOT rain`        :green:`WATER`
  ======================  =====================  =====================

  :red:`DO NOT WATER` only if the :red:`soil is wet` AND :green:`it rained`. Too much water.

* :ref:`negate_second<test_negate_second>`: ``return not second``

  ======================  =====================  =====================
  soil (first)            rain (second)          output
  ======================  =====================  =====================
  :green:`soil is dry`    :green:`it rained`     :red:`DO NOT WATER`
  :green:`soil is dry`    :red:`NOT rain`        :green:`WATER`
  :red:`soil is wet`      :green:`it rained`     :red:`DO NOT WATER`
  :red:`soil is wet`      :red:`NOT rain`        :green:`WATER`
  ======================  =====================  =====================

  :green:`WATER` only if it did :red:`NOT rain`, I do not care if the soil is :green:`dry` or :red:`wet`. What if the soil is wet?

* :ref:`logical_nor<test_logical_nor>`: ``return not (first or second)``

  ======================  =====================  =====================
  soil (first)            rain (second)          output
  ======================  =====================  =====================
  :green:`soil is dry`    :green:`it rained`     :red:`DO NOT WATER`
  :green:`soil is dry`    :red:`NOT rain`        :red:`DO NOT WATER`
  :red:`soil is wet`      :green:`it rained`     :red:`DO NOT WATER`
  :red:`soil is wet`      :red:`NOT rain`        :green:`WATER`
  ======================  =====================  =====================

  :green:`WATER` only if the :red:`soil is wet` AND it did :red:`NOT rain`. How did the soil get wet? Did I water it and forget?

* :ref:`logical_equality<test_logical_equality>`: ``return (not first or second) and (first or not second)``

  ======================  =====================  =====================
  soil (first)            rain (second)          output
  ======================  =====================  =====================
  :green:`soil is dry`    :green:`it rained`     :green:`WATER`
  :green:`soil is dry`    :red:`NOT rain`        :red:`DO NOT WATER`
  :red:`soil is wet`      :green:`it rained`     :red:`DO NOT WATER`
  :red:`soil is wet`      :red:`NOT rain`        :green:`WATER`
  ======================  =====================  =====================

  - :green:`WATER` if the :green:`soil is dry` AND :green:`it rained`
  - :green:`WATER` if the :red:`soil is wet` AND it did :red:`NOT rain`

  this could be ideal if I treat it as one or the other, but both things cannot be :ref:`True<test_what_is_true>` at the same time

* :ref:`material_implication<test_material_implication>`: ``return (not first) or second``

  ======================  =====================  =====================
  soil (first)            rain (second)          output
  ======================  =====================  =====================
  :green:`soil is dry`    :green:`it rained`     :green:`WATER`
  :green:`soil is dry`    :red:`NOT rain`        :red:`DO NOT WATER`
  :red:`soil is wet`      :green:`it rained`     :green:`WATER`
  :red:`soil is wet`      :red:`NOT rain`        :green:`WATER`
  ======================  =====================  =====================

  :red:`DO NOT WATER` if the :green:`soil is dry` AND it did :red:`NOT rain`. I want to kill the plants

I do not need to know or memorize every operation, the only operations that I want in this case are:

* :ref:`material_non_implication<test_material_non_implication>`, if I :green:`WATER` the plants only if the :green:`soil is dry` AND it did :red:`NOT rain` or
* :ref:`project_first<test_project_first>` if I :green:`WATER` only if the :red:`soil is dry` because I want the plants to stay wet
* :ref:`converse_implication<test_converse_implication>` to stop me from watering if the :red:`soil is wet` AND :green:`it rained`.

----

*********************************************************************************
review
*********************************************************************************

The :ref:`truth table` shows the possible states inputs can take and how they interact to give possible outputs. In most cases I do not need to know all the operations, just the conditions for the problem I am solving, and as always remember that they can be made with some combination of :ref:`NOT<test_logical_negation>`, :ref:`AND<test_logical_conjunction>` and :ref:`OR<test_logical_disjunction>`


The examples above show

* :ref:`security alarm`

  ============================================================================================  ==================== ================= ===================  ================= ==============================================================
  output                                                                                        :green:`motion`,     :green:`motion`,  :red:`no motion`,    :red:`no motion`, operation
                                                                                                :green:`right code`  :red:`wrong code` :green:`right code`  :red:`wrong code`
  ============================================================================================  ==================== ================= ===================  ================= ==============================================================
  :red:`OFF`                                                                                    :red:`OFF`           :red:`OFF`        :red:`OFF`           :red:`OFF`        :ref:`contradiction<test_contradiction>`
  :green:`motion` AND :green:`right code`                                                       :green:`ON`          :red:`OFF`        :red:`OFF`           :red:`OFF`        :ref:`logical_conjunction<test_logical_conjunction>`
  :green:`right code`                                                                           :green:`ON`          :red:`OFF`        :green:`ON`          :red:`OFF`        :ref:`project_second<test_project_second>`
  :red:`no motion` AND :green:`right code`                                                      :red:`OFF`           :red:`OFF`        :green:`ON`          :red:`OFF`        :ref:`converse_non_implication<test_converse_non_implication>`
  :red:`no motion`                                                                              :red:`OFF`           :red:`OFF`        :green:`ON`          :green:`ON`       :ref:`negate_first<test_negate_first>`
  NOT (:green:`motion` AND :green:`right code`)                                                 :red:`OFF`           :green:`ON`       :green:`ON`          :green:`ON`       :ref:`logical_nand<test_logical_nand>`
  :green:`ON`                                                                                   :green:`ON`          :green:`ON`       :green:`ON`          :green:`ON`       :ref:`tautology<test_tautology>`
  :green:`motion` OR :green:`right code`                                                        :green:`ON`          :green:`ON`       :green:`ON`          :red:`OFF`        :ref:`logical_disjunction<test_logical_disjunction>`
  (NOT (:green:`motion` AND :green:`right code`)) AND (:green:`motion` OR :green:`right code`)  :red:`OFF`           :green:`ON`       :green:`ON`          :red:`OFF`        :ref:`exclusive_disjunction<test_exclusive_disjunction>`
  :green:`motion` AND :red:`wrong code`                                                         :red:`OFF`           :green:`ON`       :red:`OFF`           :red:`OFF`        :ref:`material_non_implication<test_material_non_implication>`
  :green:`motion`                                                                               :green:`ON`          :green:`ON`       :red:`OFF`           :red:`OFF`        :ref:`project_first<test_project_first>`
  :green:`motion` OR :red:`wrong code`                                                          :green:`ON`          :green:`ON`       :red:`OFF`           :green:`ON`       :ref:`converse_implication<test_converse_implication>`
  :red:`wrong code`                                                                             :red:`OFF`           :green:`ON`       :red:`OFF`           :green:`ON`       :ref:`negate_second<test_negate_second>`
  NOT (:green:`motion` OR :green:`right code`)                                                  :red:`OFF`           :red:`OFF`        :red:`OFF`           :green:`ON`       :ref:`logical_nor<test_logical_nor>`
  (:red:`no motion` OR :green:`right code`) AND (:green:`motion` OR :red:`wrong code`)          :green:`ON`          :red:`OFF`        :red:`OFF`           :green:`ON`       :ref:`logical_equality<test_logical_equality>`
  :red:`no motion` OR :green:`right code`                                                       :green:`ON`          :red:`OFF`        :green:`ON`          :green:`ON`       :ref:`material_implication<test_material_implication>`
  ============================================================================================  ==================== ================= ===================  ================= ==============================================================

  I can say this in English as

  ==============================================================  ===================================================================================================================================================================
  operation                                                       rule
  ==============================================================  ===================================================================================================================================================================
  :ref:`contradiction<test_contradiction>`                        outputs :red:`OFF` always, it does not care about the inputs
  :ref:`logical_conjunction<test_logical_conjunction>`            outputs :green:`ON` only if there is :green:`motion` AND the :green:`right code` is entered
  :ref:`project_second<test_project_second>`                      outputs :green:`ON` only if the :green:`right code` is entered
  :ref:`converse_non_implication<test_converse_non_implication>`  outputs :green:`ON` only if there is :red:`NOT motion` AND the :green:`right code` is entered
  :ref:`negate_first<test_negate_first>`                          outputs :green:`ON` only if there is :red:`NOT motion`, it does not care if the :green:`right code` or :red:`wrong code` was entered
  :ref:`logical_nand<test_logical_nand>`                          outputs :red:`OFF` only if there is :green:`motion` AND the :green:`right code` is entered.
  :ref:`tautology<test_tautology>`                                outputs :green:`ON` always, it does not care about the inputs
  :ref:`logical_disjunction<test_logical_disjunction>`            outputs :red:`OFF` only if there is :red:`NOT motion` and :red:`NOT the right code` is entered
  :ref:`exclusive_disjunction<test_exclusive_disjunction>`        outputs :red:`OFF` if there is :green:`motion` AND the :green:`right code` is entered, OR if there is :red:`NOT motion` AND :red:`NOT the right code` is entered
  :ref:`material_non_implication<test_material_non_implication>`  outputs :green:`ON` if there is :green:`motion` AND :red:`NOT the right code` is entered
  :ref:`project_first<test_project_first>`                        outputs :green:`ON` if there is :green:`motion`, it does not care if the :green:`right code` or :red:`wrong code` was entered
  :ref:`converse_implication<test_converse_implication>`          outputs :red:`OFF` if there is :red:`NOT motion` AND the :green:`right code` is entered
  :ref:`negate_second<test_negate_second>`                        outputs :green:`ON` only if :red:`NOT the right code` is entered
  :ref:`logical_nor<test_logical_nor>`                            outputs :green:`ON` only if there is :red:`NOT motion` AND :red:`NOT the right code` is entered
  :ref:`logical_equality<test_logical_equality>`                  outputs :green:`ON` if there is :green:`motion` AND the :green:`right code` is entered, AND if there is :red:`NOT motion` AND :red:`NOT the right code` is entered
  :ref:`material_implication<test_material_implication>`          outputs :red:`OFF` if there is :green:`motion` AND :red:`NOT the right code` is entered.
  ==============================================================  ===================================================================================================================================================================

* :ref:`hiring`

  ==========================================================================================================  ======================= ======================= ====================  =================== ==============================================================
  output                                                                                                      :green:`strong option`, :green:`strong option`, :red:`weak option`,   :red:`weak option`, operation
                                                                                                              :green:`strong fit`     :red:`weak fit`         :green:`strong fit`   :red:`weak fit`
  ==========================================================================================================  ======================= ======================= ====================  =================== ==============================================================
  :red:`REJECT`                                                                                               :red:`REJECT`           :red:`REJECT`           :red:`REJECT`         :red:`REJECT`       :ref:`contradiction<test_contradiction>`
  :green:`strong option` AND :green:`strong fit`                                                              :green:`HIRE`           :red:`REJECT`           :red:`REJECT`         :red:`REJECT`       :ref:`logical_conjunction<test_logical_conjunction>`
  :green:`strong fit`                                                                                         :green:`HIRE`           :red:`REJECT`           :green:`HIRE`         :red:`REJECT`       :ref:`project_second<test_project_second>`
  :red:`weak option` AND :green:`strong fit`                                                                  :red:`REJECT`           :red:`REJECT`           :green:`HIRE`         :red:`REJECT`       :ref:`converse_non_implication<test_converse_non_implication>`
  :red:`weak option`                                                                                          :red:`REJECT`           :red:`REJECT`           :green:`HIRE`         :green:`HIRE`       :ref:`negate_first<test_negate_first>`
  NOT (:green:`strong option` AND :green:`strong fit`)                                                        :red:`REJECT`           :green:`HIRE`           :green:`HIRE`         :green:`HIRE`       :ref:`logical_nand<test_logical_nand>`
  :green:`HIRE`                                                                                               :green:`HIRE`           :green:`HIRE`           :green:`HIRE`         :green:`HIRE`       :ref:`tautology<test_tautology>`
  :green:`strong option` OR :green:`strong fit`                                                               :green:`HIRE`           :green:`HIRE`           :green:`HIRE`         :red:`REJECT`       :ref:`logical_disjunction<test_logical_disjunction>`
  (NOT (:green:`strong option` AND :green:`strong fit`)) AND (:green:`strong option` OR :green:`strong fit`)  :red:`REJECT`           :green:`HIRE`           :green:`HIRE`         :red:`REJECT`       :ref:`exclusive_disjunction<test_exclusive_disjunction>`
  :green:`strong option` AND :red:`weak fit`                                                                  :red:`REJECT`           :green:`HIRE`           :red:`REJECT`         :red:`REJECT`       :ref:`material_non_implication<test_material_non_implication>`
  :green:`strong option`                                                                                      :green:`HIRE`           :green:`HIRE`           :red:`REJECT`         :red:`REJECT`       :ref:`project_first<test_project_first>`
  :green:`strong option` OR :red:`weak fit`                                                                   :green:`HIRE`           :green:`HIRE`           :red:`REJECT`         :green:`HIRE`       :ref:`converse_implication<test_converse_implication>`
  :red:`weak fit`                                                                                             :red:`REJECT`           :green:`HIRE`           :red:`REJECT`         :green:`HIRE`       :ref:`negate_second<test_negate_second>`
  NOT (:green:`strong option` OR :green:`strong fit`)                                                         :red:`REJECT`           :red:`REJECT`           :red:`REJECT`         :green:`HIRE`       :ref:`logical_nor<test_logical_nor>`
  (:red:`weak option` OR :green:`strong fit`) AND (:green:`strong option` OR :red:`weak fit`)                 :green:`HIRE`           :red:`REJECT`           :red:`REJECT`         :green:`HIRE`       :ref:`logical_equality<test_logical_equality>`
  :red:`weak option` OR :green:`strong fit`                                                                   :green:`HIRE`           :red:`REJECT`           :green:`HIRE`         :green:`HIRE`       :ref:`material_implication<test_material_implication>`
  ==========================================================================================================  ======================= ======================= ====================  =================== ==============================================================

  I can say this in English as

  ==============================================================  =====================================================================================================================================================
  operation                                                       rule
  ==============================================================  =====================================================================================================================================================
  :ref:`contradiction<test_contradiction>`                        always :red:`REJECT`
  :ref:`logical_conjunction<test_logical_conjunction>`            :green:`HIRE` only if it is a :green:`strong option` AND it is a :green:`strong fit`
  :ref:`project_second<test_project_second>`                      :green:`HIRE` if it is a :green:`strong fit`, I do not care if it is a :green:`strong option` or  :red:`weak option`
  :ref:`converse_non_implication<test_converse_non_implication>`  :green:`HIRE` only if it is :red:`NOT a strong option` AND it is a :green:`strong fit`
  :ref:`negate_first<test_negate_first>`                          :green:`HIRE` only if it is :red:`NOT a strong option`, I do not care if it is a :green:`strong fit` or :red:`weak fit`
  :ref:`logical_nand<test_logical_nand>`                          :red:`REJECT` only if it is a :green:`strong option` AND it is a :green:`strong fit`
  :ref:`tautology<test_tautology>`                                :green:`HIRE` always, it does not care about the inputs
  :ref:`logical_disjunction<test_logical_disjunction>`            :red:`REJECT` only if it is :red:`NOT a strong option` and :red:`NOT a strong fit`
  :ref:`exclusive_disjunction<test_exclusive_disjunction>`        :red:`REJECT` if it is a :green:`strong option` AND it is a :green:`strong fit`, OR if it is :red:`NOT a strong option` AND :red:`NOT a strong fit`
  :ref:`material_non_implication<test_material_non_implication>`  :green:`HIRE` if it is a :green:`strong option` AND :red:`NOT a strong fit`
  :ref:`project_first<test_project_first>`                        :green:`HIRE` if it is a :green:`strong option`, I do not care if it is a :green:`strong fit` or :red:`weak fit`
  :ref:`converse_implication<test_converse_implication>`          :red:`REJECT` if it is :red:`NOT a strong option` AND it is a :green:`strong fit`
  :ref:`negate_second<test_negate_second>`                        :green:`HIRE` only if :red:`NOT a strong fit`, I do not care if it is a strong or weak option
  :ref:`logical_nor<test_logical_nor>`                            :green:`HIRE` only if it is :red:`NOT a strong option` AND :red:`NOT a strong fit`
  :ref:`logical_equality<test_logical_equality>`                  :green:`HIRE` if it is a :green:`strong option` AND it is a :green:`strong fit`, AND if it is :red:`NOT a strong option` AND :red:`NOT a strong fit`
  :ref:`material_implication<test_material_implication>`          :red:`REJECT` if it is a :green:`strong option` AND :red:`NOT a strong fit`
  ==============================================================  =====================================================================================================================================================

* :ref:`store discount policy`

  ====================================================================================  =======================  =======================  =======================  =======================  ==============================================================
  output                                                                                :green:`coupon`,         :green:`coupon`,         :red:`no coupon`,        :red:`no coupon`,        operation
                                                                                        :green:`member`          :red:`NOT a member`      :green:`member`          :red:`NOT a member`
  ====================================================================================  =======================  =======================  =======================  =======================  ==============================================================
  :red:`REGULAR PRICE`                                                                  :red:`REGULAR PRICE`     :red:`REGULAR PRICE`     :red:`REGULAR PRICE`     :red:`REGULAR PRICE`     :ref:`contradiction<test_contradiction>`
  :green:`coupon` AND :green:`member`                                                   :green:`DISCOUNT PRICE`  :red:`REGULAR PRICE`     :red:`REGULAR PRICE`     :red:`REGULAR PRICE`     :ref:`logical_conjunction<test_logical_conjunction>`
  :green:`member`                                                                       :green:`DISCOUNT PRICE`  :red:`REGULAR PRICE`     :green:`DISCOUNT PRICE`  :red:`REGULAR PRICE`     :ref:`project_second<test_project_second>`
  :red:`no coupon` AND :green:`member`                                                  :red:`REGULAR PRICE`     :red:`REGULAR PRICE`     :green:`DISCOUNT PRICE`  :red:`REGULAR PRICE`     :ref:`converse_non_implication<test_converse_non_implication>`
  :red:`no coupon`                                                                      :red:`REGULAR PRICE`     :red:`REGULAR PRICE`     :green:`DISCOUNT PRICE`  :green:`DISCOUNT PRICE`  :ref:`negate_first<test_negate_first>`
  NOT (:green:`coupon` AND :green:`member`)                                             :red:`REGULAR PRICE`     :green:`DISCOUNT PRICE`  :green:`DISCOUNT PRICE`  :green:`DISCOUNT PRICE`  :ref:`logical_nand<test_logical_nand>`
  :green:`DISCOUNT PRICE`                                                               :green:`DISCOUNT PRICE`  :green:`DISCOUNT PRICE`  :green:`DISCOUNT PRICE`  :green:`DISCOUNT PRICE`  :ref:`tautology<test_tautology>`
  :green:`coupon` OR :green:`member`                                                    :green:`DISCOUNT PRICE`  :green:`DISCOUNT PRICE`  :green:`DISCOUNT PRICE`  :red:`REGULAR PRICE`     :ref:`logical_disjunction<test_logical_disjunction>`
  (NOT (:green:`coupon` AND :green:`member`)) AND (:green:`coupon` OR :green:`member`)  :red:`REGULAR PRICE`     :green:`DISCOUNT PRICE`  :green:`DISCOUNT PRICE`  :red:`REGULAR PRICE`     :ref:`exclusive_disjunction<test_exclusive_disjunction>`
  :green:`coupon` AND :red:`NOT a member`                                               :red:`REGULAR PRICE`     :green:`DISCOUNT PRICE`  :red:`REGULAR PRICE`     :red:`REGULAR PRICE`     :ref:`material_non_implication<test_material_non_implication>`
  :green:`coupon`                                                                       :green:`DISCOUNT PRICE`  :green:`DISCOUNT PRICE`  :red:`REGULAR PRICE`     :red:`REGULAR PRICE`     :ref:`project_first<test_project_first>`
  :green:`coupon` OR :red:`NOT a member`                                                :green:`DISCOUNT PRICE`  :green:`DISCOUNT PRICE`  :red:`REGULAR PRICE`     :green:`DISCOUNT PRICE`  :ref:`converse_implication<test_converse_implication>`
  :red:`NOT a member`                                                                   :red:`REGULAR PRICE`     :green:`DISCOUNT PRICE`  :red:`REGULAR PRICE`     :green:`DISCOUNT PRICE`  :ref:`negate_second<test_negate_second>`
  NOT (:green:`coupon` OR :green:`member`)                                              :red:`REGULAR PRICE`     :red:`REGULAR PRICE`     :red:`REGULAR PRICE`     :green:`DISCOUNT PRICE`  :ref:`logical_nor<test_logical_nor>`
  (:red:`no coupon` OR :green:`member`) AND (:green:`coupon` OR :red:`NOT a member`)    :green:`DISCOUNT PRICE`  :red:`REGULAR PRICE`     :red:`REGULAR PRICE`     :green:`DISCOUNT PRICE`  :ref:`logical_equality<test_logical_equality>`
  :red:`no coupon` OR :green:`member`                                                   :green:`DISCOUNT PRICE`  :red:`REGULAR PRICE`     :green:`DISCOUNT PRICE`  :green:`DISCOUNT PRICE`  :ref:`material_implication<test_material_implication>`
  ====================================================================================  =======================  =======================  =======================  =======================  ==============================================================

  I can say this in English as

  ==============================================================  ================================================================================================================================================================
  operation                                                       rule
  ==============================================================  ================================================================================================================================================================
  :ref:`contradiction<test_contradiction>`                        :red:`REGULAR PRICE` always
  :ref:`logical_conjunction<test_logical_conjunction>`            :green:`DISCOUNT PRICE` only if the person has a :green:`coupon` AND is a :green:`member`
  :ref:`project_second<test_project_second>`                      :green:`DISCOUNT PRICE` only if the person is a :green:`member`, it does not care if they have a :green:`coupon` or  :red:`no coupon`
  :ref:`converse_non_implication<test_converse_non_implication>`  :green:`DISCOUNT PRICE` only if the person does :red:`NOT have a coupon` AND is a :green:`member`
  :ref:`negate_first<test_negate_first>`                          :green:`DISCOUNT PRICE` only if the person does :red:`NOT have a coupon`, I do not care if it is a member or not
  :ref:`logical_nand<test_logical_nand>`                          :red:`REGULAR PRICE` only if the person has a :green:`coupon` AND is a :green:`member`
  :ref:`tautology<test_tautology>`                                :green:`DISCOUNT PRICE` always
  :ref:`logical_disjunction<test_logical_disjunction>`            :red:`REGULAR PRICE` only if the person does :red:`NOT have a coupon` AND is :red:`NOT a member`
  :ref:`exclusive_disjunction<test_exclusive_disjunction>`        :red:`REGULAR PRICE` if the person has a :green:`coupon` AND is a :green:`member`, OR if the person does :red:`NOT have a coupon` AND is :red:`NOT a member`
  :ref:`material_non_implication<test_material_non_implication>`  :green:`DISCOUNT PRICE` only if the person has a :green:`coupon` AND is :red:`NOT a member`
  :ref:`project_first<test_project_first>`                        :green:`DISCOUNT PRICE` only if the person has a :green:`coupon`
  :ref:`converse_implication<test_converse_implication>`          :red:`REGULAR PRICE` only if the person :red:`does NOT have a coupon` AND is a :green:`member`
  :ref:`negate_second<test_negate_second>`                        :green:`DISCOUNT PRICE` only if the person is :red:`NOT a member`, I do not care if they have a coupon or not
  :ref:`logical_nor<test_logical_nor>`                            :green:`DISCOUNT PRICE` only if the person :red:`does NOT have a coupon` AND is :red:`NOT a member`
  :ref:`logical_equality<test_logical_equality>`                  :green:`DISCOUNT PRICE` if the person has a :green:`coupon` AND is a :green:`member`, AND if the person :red:`does NOT have a coupon` AND is :red:`NOT a member`
  :ref:`material_implication<test_material_implication>`          :red:`REGULAR PRICE` if the person has a :green:`coupon` AND :red:`NOT a member`
  ==============================================================  ================================================================================================================================================================

* :ref:`watering plants`

  ====================================================================================================  ======================= ======================= ======================= ======================= ==============================================================
  output                                                                                                :green:`soil is dry`,   :green:`soil is dry`,   :red:`soil is wet`,     :red:`soil is wet`,     operation
                                                                                                        :green:`it rained`      :red:`NOT rain`         :green:`it rained`      :red:`NOT rain`
  ====================================================================================================  ======================= ======================= ======================= ======================= ==============================================================
  :red:`DO NOT WATER`                                                                                   :red:`DO NOT WATER`     :red:`DO NOT WATER`     :red:`DO NOT WATER`     :red:`DO NOT WATER`     :ref:`contradiction<test_contradiction>`
  :green:`soil is dry` AND :green:`it rained`                                                           :green:`WATER`          :red:`DO NOT WATER`     :red:`DO NOT WATER`     :red:`DO NOT WATER`     :ref:`logical_conjunction<test_logical_conjunction>`
  :green:`it rained`                                                                                    :green:`WATER`          :red:`DO NOT WATER`     :green:`WATER`          :red:`DO NOT WATER`     :ref:`project_second<test_project_second>`
  :red:`soil is wet` AND :green:`it rained`                                                             :red:`DO NOT WATER`     :red:`DO NOT WATER`     :green:`WATER`          :red:`DO NOT WATER`     :ref:`converse_non_implication<test_converse_non_implication>`
  :red:`soil is wet`                                                                                    :red:`DO NOT WATER`     :red:`DO NOT WATER`     :green:`WATER`          :green:`WATER`          :ref:`negate_first<test_negate_first>`
  NOT (:green:`soil is dry` AND :green:`it rained`)                                                     :red:`DO NOT WATER`     :green:`WATER`          :green:`WATER`          :green:`WATER`          :ref:`logical_nand<test_logical_nand>`
  :green:`WATER`                                                                                        :green:`WATER`          :green:`WATER`          :green:`WATER`          :green:`WATER`          :ref:`tautology<test_tautology>`
  :green:`soil is dry` OR :green:`it rained`                                                            :green:`WATER`          :green:`WATER`          :green:`WATER`          :red:`DO NOT WATER`     :ref:`logical_disjunction<test_logical_disjunction>`
  (NOT (:green:`soil is dry` AND :green:`it rained`)) AND (:green:`soil is dry` OR :green:`it rained`)  :red:`DO NOT WATER`     :green:`WATER`          :green:`WATER`          :red:`DO NOT WATER`     :ref:`exclusive_disjunction<test_exclusive_disjunction>`
  :green:`soil is dry` AND :red:`NOT rain`                                                              :red:`DO NOT WATER`     :green:`WATER`          :red:`DO NOT WATER`     :red:`DO NOT WATER`     :ref:`material_non_implication<test_material_non_implication>`
  :green:`soil is dry`                                                                                  :green:`WATER`          :green:`WATER`          :red:`DO NOT WATER`     :red:`DO NOT WATER`     :ref:`project_first<test_project_first>`
  :green:`soil is dry` OR :red:`NOT rain`                                                               :green:`WATER`          :green:`WATER`          :red:`DO NOT WATER`     :green:`WATER`          :ref:`converse_implication<test_converse_implication>`
  :red:`NOT rain`                                                                                       :red:`DO NOT WATER`     :green:`WATER`          :red:`DO NOT WATER`     :green:`WATER`          :ref:`negate_second<test_negate_second>`
  NOT (:green:`soil is dry` OR :green:`it rained`)                                                      :red:`DO NOT WATER`     :red:`DO NOT WATER`     :red:`DO NOT WATER`     :green:`WATER`          :ref:`logical_nor<test_logical_nor>`
  (:red:`soil is wet` OR :green:`it rained`) AND (:green:`soil is dry` OR :red:`NOT rain`)              :green:`WATER`          :red:`DO NOT WATER`     :red:`DO NOT WATER`     :green:`WATER`          :ref:`logical_equality<test_logical_equality>`
  :red:`soil is wet` OR :green:`it rained`                                                              :green:`WATER`          :red:`DO NOT WATER`     :green:`WATER`          :green:`WATER`          :ref:`material_implication<test_material_implication>`
  ====================================================================================================  ======================= ======================= ======================= ======================= ==============================================================

  I can say this in English as

  ==============================================================  =====================================================================================================================================================
  operation                                                       rule
  ==============================================================  =====================================================================================================================================================
  :ref:`contradiction<test_contradiction>`                        :red:`DO NOT WATER` always
  :ref:`logical_conjunction<test_logical_conjunction>`            :green:`WATER` only if the :green:`soil is dry` AND :green:`it rained`
  :ref:`project_second<test_project_second>`                      :green:`WATER` only if :green:`it rained`, I do not care if the :green:`soil is dry` or  :red:`wet`
  :ref:`converse_non_implication<test_converse_non_implication>`  :green:`WATER` only if the :red:`soil is wet` AND :green:`it rained`
  :ref:`negate_first<test_negate_first>`                          :green:`WATER` only if the :red:`soil is wet`, I do not care if it :green:`rained` or did :red:`NOT rain`
  :ref:`logical_nand<test_logical_nand>`                          :red:`DO NOT WATER` only if the :green:`soil is dry` AND :green:`it rained`
  :ref:`tautology<test_tautology>`                                :green:`WATER` always
  :ref:`logical_disjunction<test_logical_disjunction>`            :red:`DO NOT WATER` only if the :red:`soil is wet` AND it did :red:`NOT rain`
  :ref:`exclusive_disjunction<test_exclusive_disjunction>`        :red:`DO NOT WATER` if the :green:`soil is dry` AND :green:`it rained`, OR if the :red:`soil is wet` AND :red:`it did NOT rain`
  :ref:`material_non_implication<test_material_non_implication>`  :green:`WATER` only if the :green:`soil is dry` AND it did :red:`NOT rain`
  :ref:`project_first<test_project_first>`                        :green:`WATER` only if the :green:`soil is dry`, I do not care if it :green:`rained` or did :red:`NOT rain`
  :ref:`converse_implication<test_converse_implication>`          :red:`DO NOT WATER` only if the :red:`soil is wet` AND :green:`it rained`
  :ref:`negate_second<test_negate_second>`                        :green:`WATER` only if it did :red:`NOT rain`, I do not care if the soil is :green:`dry` or :red:`wet`
  :ref:`logical_nor<test_logical_nor>`                            :green:`WATER` only if the :red:`soil is wet` AND it did :red:`NOT rain`
  :ref:`logical_equality<test_logical_equality>`                  :green:`WATER` if the :green:`soil is dry` AND :green:`it rained`, AND if the :red:`soil is wet` AND it did :red:`NOT rain`
  :ref:`material_implication<test_material_implication>`          :red:`DO NOT WATER` if the :green:`soil is dry` AND it did :red:`NOT rain`
  ==============================================================  =====================================================================================================================================================

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