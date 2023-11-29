
Truth Table: Negate
===================

I will continue to step through learning conditional statements using Binary Operations from the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_



Negate First
------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a test for negate first to ``TestBinaryOperations`` in ``test_truth_table.py``

.. code-block:: python

    def test_negate_first(self):
        self.assertFalse(truth_table.negate_first(True, True))
        self.assertFalse(truth_table.negate_first(True, False))
        self.assertTrue(truth_table.negate_first(False, True))
        self.assertTrue(truth_table.negate_first(False, False))

and the terminal shows an :doc:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

* then I add a function definition to ``truth_table.py``

  .. code-block:: python

    def negate_first(p, q):
        return False

  the terminal shows an :doc:`/AssertionError` for the third case
* before I add a condition for it, this looks similar to ``logical_equality`` and ``exclusive_disjunction`` because 2 out of the 4 cases have the same return value. I see that

  * if ``p == True`` the result is :doc:`False </data_structures_booleans>`
  * if ``p == False`` the result is :doc:`True </data_structures_booleans>`

* I add conditions to match

  .. code-block:: python

    def negate_first(p, q):
        if p == True:
            return False
        if p == False:
            return True

  and the test passes

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


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

  ah, just like the name and all tests pass

Negate Second
-------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a test for negate second to ``TestBinaryOperations``

.. code-block:: python

    def test_negate_second(self):
        self.assertFalse(truth_table.negate_second(True, True))
        self.assertTrue(truth_table.negate_second(True, False))
        self.assertFalse(truth_table.negate_second(False, True))
        self.assertTrue(truth_table.negate_second(False, False))

and the terminal shows an :doc:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* I add a function definition to ``truth_table.py``

  .. code-block:: python

    def negate_second(p, q):
        return False

  and the terminal shows an :doc:`/AssertionError` for the third case
* before I add a condition for it, this looks similar to ``logical_equality``, ``exclusive_disjunction`` and ``negate_first`` because 2 out of the 4 cases have the same return value. I see that

  * if ``q == True`` the result is :doc:`False </data_structures_booleans>`
  * if ``q == False`` the result is :doc:`True </data_structures_booleans>`

* What if I try using the conclusion from ``negate_first``?

  .. code-block:: python

    def negate_second(p, q):
        return not p

  the terminal still shows an :doc:`/AssertionError`
* What if I try ``q`` instead?

  .. code-block:: python

    def negate_second(p, q):
        return not q

  All tests pass. Fantastic!

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

I don't think I can make it better so I change what I know so far

For any boolean operation involving 2 inputs: ``p`` and ``q`` which can take the values :doc:`True </data_structures_booleans>` or :doc:`False </data_structures_booleans>`


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
* :doc:`False </data_structures_booleans>` is ``not True``
* :doc:`True </data_structures_booleans>` is ``not False``
* :doc:`False </data_structures_booleans>` is :doc:`False </data_structures_booleans>`
* :doc:`True </data_structures_booleans>` is :doc:`True </data_structures_booleans>`