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

* then I add a :ref:`function<functions>` definition to ``truth_table.py``

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


* I add a :ref:`function<functions>` definition to ``truth_table.py``

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


* then I add a :ref:`function<functions>` definition to ``truth_table.py``

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


* When I add a :ref:`function<functions>` definition to ``truth_table.py``

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
test_tautology
*********************************************************************************

red: make it fail
#################################################################################

I add a test for tautology to ``TestBinaryOperations`` in ``test_truth_table.py``

.. code-block:: python

    def test_tautology(self):
        self.assertTrue(src.truth_table.tautology(True, True))
        self.assertTrue(src.truth_table.tautology(True, False))
        self.assertTrue(src.truth_table.tautology(False, True))
        self.assertTrue(src.truth_table.tautology(False, False))

the terminal shows :ref:`AttributeError`

green: make it pass
#################################################################################


* I add a :ref:`function<functions>` definition to ``truth_table.py``

  .. code-block:: python

    def tautology(p, q):
        return False

  the terminal shows :ref:`AssertionError` for the first case
* I change the return value

  .. code-block:: python

    def tautology(p, q):
        return True

  and the test passes. Easy

----

*********************************************************************************
test_contradiction
*********************************************************************************

red: make it fail
#################################################################################

I add a test for contradiction to ``TestBinaryOperations``

.. code-block:: python

    def test_contradiction(self):
        self.assertFalse(src.truth_table.contradiction(True, True))
        self.assertFalse(src.truth_table.contradiction(True, False))
        self.assertFalse(src.truth_table.contradiction(False, True))
        self.assertFalse(src.truth_table.contradiction(False, False))

the terminal shows :ref:`AttributeError`

green: make it pass
#################################################################################

* I add a :ref:`function<functions>` definition to ``truth_table.py``

  .. code-block:: python

    def contradiction(p, q):
        return True

  the terminal shows :ref:`AssertionError` for the first case
* When I make the return value, the test passes

  .. code-block:: python

    def contradiction(p, q):
        return False

----

*********************************************************************************
review
*********************************************************************************

*YOU DID IT!* You made it to the end of the ``Truth Table`` series. Summarizing what the tests have shown so far, I know that for any boolean operation involving 2 inputs: ``p`` and ``q`` which can take the values :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`

* ``contradition`` always returns :ref:`False<test_what_is_false>` it is a :doc:`singleton function </functions/test_singleton_functions>`
* ``tautology`` always returns :ref:`True<test_what_is_true>` it is a :doc:`singleton function </functions/test_singleton_functions>`
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