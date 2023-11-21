Truth Table: True Lies
======================

I will continue to step through learning conditional statements in python using Test Driven Development with the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_



Tautology
---------

RED: make it fail
^^^^^^^^^^^^^^^^^

add a test for tautology to ``TestBinaryOperations``

.. code-block:: python

    def test_tautology(self):
      self.assertTrue(truth_table.tautology(True, True))
      self.assertTrue(truth_table.tautology(True, False))
      self.assertTrue(truth_table.tautology(False, True))
      self.assertTrue(truth_table.tautology(False, False))

the terminal shows an :doc:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* add a function definition to ``truth_table.py``
  .. code-block:: python

    def tautology(p, q):
      return False
  the terminal updates to show an :doc:`AssertionError` for the first case
* replace the return value
  .. code-block:: python

    def tautology(p, q):
      return True
  all tests pass

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

Nothing to refactor here

Contradiction
-------------

RED: make it fail
^^^^^^^^^^^^^^^^^

add a test for contradiction to ``TestBinaryOperations``

.. code-block:: python

    def test_contradiction(self):
      self.assertFalse(truth_table.contradiction(True, True))
      self.assertFalse(truth_table.contradiction(True, False))
      self.assertFalse(truth_table.contradiction(False, True))
      self.assertFalse(truth_table.contradiction(False, False))

the terminal shows an :doc:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* add a function definition to ``truth_table.py``
  .. code-block:: python

    def contradiction(p, q):
      return True
  the terminal updates to show an :doc:`AssertionError` for the first case
* update the return value
  .. code-block:: python

    def contradiction(p, q):
      return False

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

Nothing to do here either. update what I know so far

*YOU DID IT!*
For any boolean operation involving 2 inputs - ``p`` and ``q`` which can take the values :doc:`True </data structures: booleans>` or :doc:`False </data structures: booleans>`


* ``contradition`` always returns :doc:`False </data structures: booleans>`
* ``tautology`` always returns :doc:`True </data structures: booleans>`
* ``converse_implication`` is ``not p and q`` which is different from ``not(p and q)``
* ``logical_nor`` is ``not(p or q)``
* ``logical_nand`` is ``not(p and q)``
* ``exclusive_disjunction`` is ``!=`` aka opposite of ``logical_equality``
* ``logical_equality`` is ``==``
* ``logical_disjunction`` is ``or``
* ``logical_conjunction`` is ``and``
* ``and`` is "not ``or``"
* ``or`` is "not ``and``"
* :doc:`False </data structures: booleans>` is ``not True``
* :doc:`True </data structures: booleans>` is ``not False``
* :doc:`False </data structures: booleans>` is :doc:`False </data structures: booleans>`
* :doc:`True </data structures: booleans>` is :doc:`True </data structures: booleans>`
