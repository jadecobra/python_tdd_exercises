.. include:: ../../../links.rst

#######################
truth table: True Lies
#######################

.. contents:: table of contents
  :local:
  :depth: 1

----

More tests for the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_

Tautology
---------

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


* I add a:ref:`function<functions>`definition to ``truth_table.py``

  .. code-block:: python

    def tautology(p, q):
        return False

  the terminal shows :ref:`AssertionError` for the first case
* I change the return value

  .. code-block:: python

    def tautology(p, q):
        return True

  and the test passes. Easy


Contradiction
-------------

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

* I add a:ref:`function<functions>`definition to ``truth_table.py``

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