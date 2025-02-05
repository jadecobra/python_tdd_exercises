.. include:: ../../../links.rst

#####################
truth table: Project
#####################

.. contents:: table of contents
  :local:
  :depth: 1

----

This chapter shows the projection Binary Operations from the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_ using tests


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


* then I add a function definition to ``truth_table.py``

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


* When I add a function definition to ``truth_table.py``

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

-----

From the tests I know that for any boolean operation involving 2 inputs: ``p`` and ``q`` which can take the values :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`


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

----

:doc:`/code/code_truth_table`