.. include:: ../../../links.rst

####################
truth table: Negate
####################

.. contents:: table of contents
  :local:
  :depth: 1

----

I continue to step through conditional statements using Binary Operations from the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_


Negate First
------------

red: make it fail
#################################################################################

I add a test for negate first to ``TestBinaryOperations`` in ``test_truth_table.py``

.. code-block:: python

    def test_negate_first(self):
        self.assertFalse(truth_table.negate_first(True, True))
        self.assertFalse(truth_table.negate_first(True, False))
        self.assertTrue(truth_table.negate_first(False, True))
        self.assertTrue(truth_table.negate_first(False, False))

and the terminal shows :ref:`AttributeError`

green: make it pass
#################################################################################

* then I add a function definition to ``truth_table.py``

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
        self.assertFalse(truth_table.negate_second(True, True))
        self.assertTrue(truth_table.negate_second(True, False))
        self.assertFalse(truth_table.negate_second(False, True))
        self.assertTrue(truth_table.negate_second(False, False))

and the terminal shows :ref:`AttributeError`

green: make it pass
#################################################################################


* I add a function definition to ``truth_table.py``

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


From the tests so far, I know that for any boolean operation involving 2 inputs: ``p`` and ``q`` which can take the values :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`


* ``negate second`` always returns ``not q``
* ``negate first`` always return ``not p``
* ``material non implication`` is ``p and not q``
* ``converse non implication`` is ``not p and q`` which is different from ``not(p and q)``
* ``logical NOR`` is ``not(p or q)``
* ``logical NAND`` is ``not(p and q)``
* ``exclusive disjunction`` is ``!=`` or the opposite of ``logical_equality``
* ``logical equality`` is ``==``
* ``logical implication`` is ``not p or q``
* ``logical disjunction`` is ``or``
* ``logical conjunction`` is ``and``
* ``and`` is "not ``or``"
* ``or`` is "not ``and``"
* :ref:`False<test_what_is_false>` is ``not True``
* :ref:`True<test_what_is_true>` is ``not False``
* :ref:`False<test_what_is_false>` is :ref:`False<test_what_is_false>`
* :ref:`True<test_what_is_true>` is :ref:`True<test_what_is_true>`

----

:doc:`/code/code_truth_table`