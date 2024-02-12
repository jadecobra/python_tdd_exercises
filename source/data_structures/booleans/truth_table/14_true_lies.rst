.. include:: ../../../links.rst

#######################
Truth Table: True Lies
#######################

More tests for the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_



Tautology
---------

red: make it fail
^^^^^^^^^^^^^^^^^

I add a test for tautology to ``TestBinaryOperations`` in ``test_truth_table.py``

.. code-block:: python

    def test_tautology(self):
        self.assertTrue(truth_table.tautology(True, True))
        self.assertTrue(truth_table.tautology(True, False))
        self.assertTrue(truth_table.tautology(False, True))
        self.assertTrue(truth_table.tautology(False, False))

the terminal shows an :ref:`AttributeError`

green: make it pass
^^^^^^^^^^^^^^^^^^^


* I add a function definition to ``truth_table.py``

  .. code-block:: python

    def tautology(p, q):
        return False

  the terminal shows an :ref:`AssertionError` for the first case
* I replace the return value

  .. code-block:: python

    def tautology(p, q):
        return True

  and the test passes. Easy


Contradiction
-------------

red: make it fail
^^^^^^^^^^^^^^^^^

I add a test for contradiction to ``TestBinaryOperations``

.. code-block:: python

    def test_contradiction(self):
        self.assertFalse(truth_table.contradiction(True, True))
        self.assertFalse(truth_table.contradiction(True, False))
        self.assertFalse(truth_table.contradiction(False, True))
        self.assertFalse(truth_table.contradiction(False, False))

the terminal shows an :ref:`AttributeError`

green: make it pass
^^^^^^^^^^^^^^^^^^^

* I add a function definition to ``truth_table.py``

  .. code-block:: python

    def contradiction(p, q):
        return True

  the terminal shows an :ref:`AssertionError` for the first case
* When I make the return value, the test passes

  .. code-block:: python

    def contradiction(p, q):
        return False

----

*YOU DID IT!* You made it to the end of the ``Truth Table`` series. Summarizing what the tests have shown so far, I know that for any boolean operation involving 2 inputs: ``p`` and ``q`` which can take the values :doc:`True </data_structures/booleans/booleans>` or :doc:`False </data_structures/booleans/booleans>`


* ``contradition`` always returns :doc:`False </data_structures/booleans/booleans>` it is a :doc:`singleton function </functions/functions_singleton>`
* ``tautology`` always returns :doc:`True </data_structures/booleans/booleans>` it is a :doc:`singleton function </functions/functions_singleton>`
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
* ``logical disjunction`` is ``or``
* ``logical conjunction`` is ``and``
* ``and`` is "not ``or``"
* ``or`` is "not ``and``"
* :doc:`False </data_structures/booleans/booleans>` is ``not True``
* :doc:`True </data_structures/booleans/booleans>` is ``not False``
* :doc:`False </data_structures/booleans/booleans>` is :doc:`False </data_structures/booleans/booleans>`
* :doc:`True </data_structures/booleans/booleans>` is :doc:`True </data_structures/booleans/booleans>`
