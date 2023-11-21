Truth Table: Material NonImplication
====================================

I will continue to step through learning conditional statements in python using Test Driven Development using the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_

Prerequisites
-------------


:doc:`How to Setup a Test Driven Development Environment`

----

Material NonImplication
-----------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

add a test for material non-implication to ``TestBinaryOperations``

.. code-block:: python

    def test_material_non_implication(self):
      self.assertFalse(truth_table.material_non_implication(True, True))
      self.assertTrue(truth_table.material_non_implication(True, False))
      self.assertFalse(truth_table.material_non_implication(False, True))
      self.assertFalse(truth_table.material_non_implication(False, False))

the terminal shows an :doc:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* add a function definition to ``truth_table.py``
  .. code-block:: python

    def material_non_implication(p, q):
      return False
  the terminal updates to show an :doc:`AssertionError` for the second case
* add a condition for it
  .. code-block:: python

    def material_non_implication(p, q):
      if p == True and q == False:
       return True
      return False
  all the tests pass

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


* use implied conditional testing
  .. code-block:: python

    def material_non_implication(p, q):
      if p and q == False:
       return True
      else:
       return False
  tests still pass
  .. code-block:: python

    def material_non_implication(p, q):
      if p and not q:
       return True
      else:
       return False

* rewrite with a ``return`` statement
  .. code-block:: python

    def material_non_implication(p, q):
      return p and not q
  I am still green

Our knowledge is growing, I now know that for any boolean operation involving 2 inputs - ``p`` and ``q`` which can take the values :doc:`True </data structures: booleans>` or :doc:`False </data structures: booleans>`


* ``material_non_implication`` is ``p and not q``
* ``converse_non_implication`` is ``not p and q`` which is different from ``not(p and q)``
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
