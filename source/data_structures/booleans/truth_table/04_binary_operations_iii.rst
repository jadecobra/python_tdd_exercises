.. include:: ../../../links.rst

#################################################################################
truth table: Binary Operations III
#################################################################################

.. contents:: table of contents
  :local:
  :depth: 1

----

*********************************************************************************
requirements
*********************************************************************************

:doc:`how to make a python test driven development environment </how_to/make_tdd_environment>` with ``truth_table`` as the name of the project

*********************************************************************************
test_material_non_implication
*********************************************************************************

red: make it fail
#################################################################################

I add a test for material non-implication to ``TestBinaryOperations`` in ``test_truth_table.py``

.. code-block:: python

    def test_material_non_implication(self):
        self.assertFalse(src.truth_table.material_non_implication(True, True))
        self.assertTrue(src.truth_table.material_non_implication(True, False))
        self.assertFalse(src.truth_table.material_non_implication(False, True))
        self.assertFalse(src.truth_table.material_non_implication(False, False))

the terminal shows :ref:`AttributeError`

green: make it pass
#################################################################################


* I add a:ref:`function<functions>`definition to ``truth_table.py``

  .. code-block:: python

    def material_non_implication(p, q):
        return False

  the terminal shows :ref:`AssertionError` for the second case
* I add a condition for it

  .. code-block:: python

      def material_non_implication(p, q):
          if p == True and q == False:
              return True
          return False

  and the tests pass

refactor: make it better
#################################################################################


* I use implied conditional testing for the first part of the if statement

  .. code-block:: python

    def material_non_implication(p, q):
        if p and q == False:
            return True
        else:
            return False

  all tests still pass

* then change the second part to use not_

  .. code-block:: python

    def material_non_implication(p, q):
        if p and not q:
            return True
        else:
            return False

* I rewrite with a ``return`` statement

  .. code-block:: python

    def material_non_implication(p, q):
        return p and not q

  and I am still green

----

*********************************************************************************
test_negate
*********************************************************************************

Negate First
------------

red: make it fail
#################################################################################

I add a test for negate first to ``TestBinaryOperations`` in ``test_truth_table.py``

.. code-block:: python

    def test_negate_first(self):
        self.assertFalse(src.truth_table.negate_first(True, True))
        self.assertFalse(src.truth_table.negate_first(True, False))
        self.assertTrue(src.truth_table.negate_first(False, True))
        self.assertTrue(src.truth_table.negate_first(False, False))

and the terminal shows :ref:`AttributeError`

green: make it pass
#################################################################################

* then I add a:ref:`function<functions>`definition to ``truth_table.py``

  .. code-block:: python

    def negate_first(p, q):
        return False

  the terminal shows :ref:`AssertionError` for the third case
* before I add a condition for it, this looks similar to ``logical_equality`` and ``exclusive_disjunction`` because 2 out of the 4 cases have the same return value. I see that

  * when ``p == True`` the result is :ref:`False<test_what_is_false>`
  * when ``p == False`` the result is :ref:`True<test_what_is_true>`

* I add conditions to match

  .. code-block:: python

    def negate_first(p, q):
        if p == True:
            return False
        if p == False:
            return True

  and the test passes

refactor: make it better
#################################################################################


* I use implied conditional testing

  .. code-block:: python

    def negate_first(p, q):
        if p:
            return False
        if not p:
            return True

* then reorder and use ``else``

  .. code-block:: python

    def negate_first(p, q):
        if not p:
            return True
        else:
            return False

* I simplify to one line

  .. code-block:: python

    def negate_first(p, q):
        return not p

  ah, just like the name

Negate Second
-------------

red: make it fail
#################################################################################

I add a test for negate second to ``TestBinaryOperations``

.. code-block:: python

    def test_negate_second(self):
        self.assertFalse(src.truth_table.negate_second(True, True))
        self.assertTrue(src.truth_table.negate_second(True, False))
        self.assertFalse(src.truth_table.negate_second(False, True))
        self.assertTrue(src.truth_table.negate_second(False, False))

and the terminal shows :ref:`AttributeError`

green: make it pass
#################################################################################


* I add a:ref:`function<functions>`definition to ``truth_table.py``

  .. code-block:: python

    def negate_second(p, q):
        return False

  and the terminal shows :ref:`AssertionError` for the third case
* before I add a condition for it, this looks similar to ``logical_equality``, ``exclusive_disjunction`` and ``negate_first`` because 2 out of the 4 cases have the same return value. I see that

  - when ``q == True`` the result is :ref:`False<test_what_is_false>`
  - when ``q == False`` the result is :ref:`True<test_what_is_true>`

* What if I try using the conclusion from ``negate_first``?

  .. code-block:: python

    def negate_second(p, q):
        return not p

  the terminal still shows :ref:`AssertionError`
* What if I try ``q`` instead?

  .. code-block:: python

    def negate_second(p, q):
        return not q

  All tests pass. Fantastic!

----

*********************************************************************************
test_project
*********************************************************************************

Project First
-------------

red: make it fail
#################################################################################

I add a test for project first to ``TestBinaryOperations`` in ``test_truth_table.py``

.. code-block:: python

    def test_project_first(self):
        self.assertTrue(src.truth_table.project_first(True, True))
        self.assertTrue(src.truth_table.project_first(True, False))
        self.assertFalse(src.truth_table.project_first(False, True))
        self.assertFalse(src.truth_table.project_first(False, False))

the terminal shows :ref:`AttributeError`

green: make it pass
#################################################################################


* then I add a:ref:`function<functions>`definition to ``truth_table.py``

  .. code-block:: python

    def project_first(p, q):
        return False

  and the terminal shows :ref:`AssertionError` for the first case
* I make the `return statement`_

  .. code-block:: python

    def project_first(p, q):
        return True

  and the :ref:`AssertionError` is now for the third case
* before I add a condition for it, this looks similar to ``logical_equality``, ``exclusive_disjunction``, ``negate_first`` and ``negate_second`` because 2 out of the 4 cases have the same return value. I see that

  * when ``p == True`` the result is :ref:`True<test_what_is_true>`
  * when ``p == False`` the result is :ref:`False<test_what_is_false>`

* I add conditions to represent this

  .. code-block:: python

    def project_first(p, q):
        if p == True:
            return True
        if p == False:
            return False

  and the tests pass

refactor: make it better
#################################################################################

* I use implied conditional testing to simplify the statements

  .. code-block:: python

    def project_first(p, q):
        if p:
            return True
        if not p:
            return False

* I simplify again

  .. code-block:: python

    def project_first(p, q):
        return True if p else False

* then simplify some more

  .. code-block:: python

    def project_first(p, q):
        return p

  I am still green. Lovely!

Project Second
--------------

red: make it fail
#################################################################################

I add a test for project second to ``TestBinaryOperations``

.. code-block:: python

    def test_project_second(self):
        self.assertTrue(src.truth_table.project_second(True, True))
        self.assertFalse(src.truth_table.project_second(True, False))
        self.assertTrue(src.truth_table.project_second(False, True))
        self.assertFalse(src.truth_table.project_second(False, False))

the terminal shows :ref:`AttributeError`

green: make it pass
#################################################################################


* When I add a:ref:`function<functions>`definition to ``truth_table.py``

  .. code-block:: python

    def project_second(p, q):
        return False

  the terminal shows :ref:`AssertionError` for the first case
* and I make the return value to make it pass

  .. code-block:: python

    def project_second(p, q):
        return True

  the terminal shows :ref:`AssertionError` for the second case
* before I add a condition for it, this looks similar to ``logical_equality``, ``exclusive_disjunction``, ``negate_first``, ``negate_second`` and ``project_first`` because 2 out of the 4 cases have the same return value. I see that

  * when ``q == True`` the result is :ref:`True<test_what_is_true>`
  * when ``q == False`` the result is :ref:`False<test_what_is_false>`

* What if I try using the conclusion from ``project_first``?

  .. code-block:: python

    def project_second(p, q):
        return p

  the terminal still shows :ref:`AssertionError`
* What if I return ``q`` instead?
  .. code-block:: python

    def project_second(p, q):
        return q

  All tests pass and it is a simple line

----

*********************************************************************************
review
*********************************************************************************


----

:doc:`/code/code_truth_table`