
Truth Table: Converse NonImplication
====================================

The tests in this chapter cover Converse NonImplication from  the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_


RED: make it fail
^^^^^^^^^^^^^^^^^

I add a test for converse nonimplication to ``TestBinaryOperations`` in ``test_truth_table.py``

.. code-block:: python

    def test_converse_non_implication(self):
        self.assertFalse(truth_table.converse_non_implication(True, True))
        self.assertFalse(truth_table.converse_non_implication(True, False))
        self.assertTrue(truth_table.converse_non_implication(False, True))
        self.assertFalse(truth_table.converse_non_implication(False, False))

the terminal shows an :doc:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

* I add a function definition to ``truth_table.py``

  .. code-block:: python

    def converse_non_implication(p, q):
        return False

  since the first two cases pass, the terminal shows an :doc:`/AssertionError` for the third case
* I add a condition for it

  .. code-block:: python

    def converse_non_implication(p, q):
        if p == False and q == True:
            return True
        return False

  all the tests pass

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

* I use implied conditional testing with ``not`` for the first part of the if statement

  .. code-block:: python

    def converse_non_implication(p, q):
        if not p and q  == True:
            return True
        else:
            return False

  and the test passes

* I do the same for the second part of the statement

  .. code-block:: python

    def converse_non_implication(p, q):
        if not p and q:
            return True
        else:
            return False

* I rewrite with a ``return`` statement

  .. code-block:: python

    def converse_non_implication(p, q):
        return not p and q

  Another success! All tests pass

From the tests I see that for any boolean operation involving 2 inputs: ``p`` and ``q`` which can take the values :doc:`True </data_structures_booleans>` or :doc:`False </data_structures_booleans>`

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
