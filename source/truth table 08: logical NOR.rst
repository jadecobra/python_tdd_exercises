Truth Table: Logical NOR
========================

I will continue to step through learning conditional statements in python using Test Driven Development with the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_



Logical NOR
-----------

RED: make it fail
^^^^^^^^^^^^^^^^^

add a test for exclusive disjunction to ``TestBinaryOperations``

.. code-block:: python

    def test_logical_nor(self):
      self.assertFalse(truth_table.logical_nor(True, True))
      self.assertFalse(truth_table.logical_nor(True, False))
      self.assertFalse(truth_table.logical_nor(False, True))
      self.assertTrue(truth_table.logical_nor(False, False))

the terminal shows an :doc:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* add a function definition to ``truth_table.py``
  .. code-block:: python

    def logical_nor(p, q):
      return False

* the first 3 pass and I see a failure for the 4th case, add a condition for it
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
      if not p not or not q:
       return True
      return False
  the terminal shows a ``SyntaxError`` and I rewrite the syntax properly
  .. code-block:: python

    def logical_nor(p, q):
      if not(p or q):
       return True
      return False

* rewrite the entire thing on one line
  .. code-block:: python

    def logical_nor(p, q):
      return True if not(p or q) else False

* simplify using implied conditional testing
  .. code-block:: python

    def logical_nor(p, q):
      return not(p or q)
  BOOM! all the tests pass. Are I getting better at this?

Knowledge update. For any boolean operation involving 2 inputs - ``p`` and ``q`` which can take the values :doc:`True </data structures: booleans>` or :doc:`False </data structures: booleans>`


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
