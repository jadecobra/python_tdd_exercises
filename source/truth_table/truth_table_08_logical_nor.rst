
Truth Table: Logical NOR
========================

These tests cover Logical NOR from  the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_


RED: make it fail
^^^^^^^^^^^^^^^^^

I add a test for exclusive disjunction to ``TestBinaryOperations`` in ``test_truth_table.py``

.. code-block:: python

    def test_logical_nor(self):
        self.assertFalse(truth_table.logical_nor(True, True))
        self.assertFalse(truth_table.logical_nor(True, False))
        self.assertFalse(truth_table.logical_nor(False, True))
        self.assertTrue(truth_table.logical_nor(False, False))

and the terminal shows an :doc:`/exceptions/AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

* I add a function definition to ``truth_table.py``

  .. code-block:: python

    def logical_nor(p, q):
        return False

* and the first 3 pass, there is a failure for the 4th case, so I add a condition for it

  .. code-block:: python

    def logical_nor(p, q):
        if p == False and q == False:
            return True
        return False

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

* I restate the ``if`` condition using implicit conditional testing

  .. code-block:: python

    def logical_nor(p, q):
        if not p and not q:
            return True
        return False

* I abstract the repetition of ``not`` by rewriting the entire statement in terms of ``not``

  .. code-block:: python

    def logical_nor(p, q):
        if (not p) (not or) (not q):
            return True
        return False

  the terminal shows a ``SyntaxError`` and I rewrite the statement with proper syntax, "factoring" out the ``not``

  .. code-block:: python

    def logical_nor(p, q):
        if not(p or q):
            return True
        return False

* then rewrite the entire thing on one line

  .. code-block:: python

    def logical_nor(p, q):
      return True if not(p or q) else False

* I simplify using implied conditional testing

  .. code-block:: python

    def logical_nor(p, q):
        return not(p or q)


From the tests I can see that for any boolean operation involving 2 inputs: ``p`` and ``q`` which can take the values :doc:`True </data_structures/booleans>` or :doc:`False </data_structures/booleans>`


* ``logical NOR`` is ``not (p or q)``
* ``logical NAND`` is ``not (p and q)``
* ``exclusive disjunction`` is ``!=`` or the opposite of ``logical_equality``
* ``logical equality`` is ``==``
* ``logical implication`` is ``not p or q``
* ``logical disjunction`` is ``or``
* ``logical conjunction`` is ``and``
* ``and`` is "not ``or``"
* ``or`` is "not ``and``"
* :doc:`False </data_structures/booleans>` is ``not True``
* :doc:`True </data_structures/booleans>` is ``not False``
* :doc:`False </data_structures/booleans>` is :doc:`False </data_structures/booleans>`
* :doc:`True </data_structures/booleans>` is :doc:`True </data_structures/booleans>`
