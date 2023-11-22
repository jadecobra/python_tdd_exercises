Truth Table: Project
====================

I will continue to step through learning conditional statements in python using Test Driven Development with the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_



Project First
-------------

RED: make it fail
^^^^^^^^^^^^^^^^^

add a test for project first to ``TestBinaryOperations`` in ``test_truth_table.py``

.. code-block:: python

    def test_project_first(self):
      self.assertTrue(truth_table.project_first(True, True))
      self.assertTrue(truth_table.project_first(True, False))
      self.assertFalse(truth_table.project_first(False, True))
      self.assertFalse(truth_table.project_first(False, False))

the terminal shows an :doc:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* add a function definition to ``truth_table.py``
  .. code-block:: python

    def project_first(p, q):
      return False
  the terminal updates to show an :doc:`AssertionError` foe the first case
* change the return statement
  .. code-block:: python

    def project_first(p, q):
      return True
  the terminal updates to show an :doc:`AssertionError` for the third case
* before I add a condition for it, this looks similar to ``logical_equality``, ``exclusive_disjunction``, ``negate_first`` and ``negate_second`` because 2 out of the 4 cases have the same return value. I observe that

  * if ``p == True`` the result is :doc:`True <data_structures_booleans>`
  * if ``p == False`` the result is :doc:`False <data_structures_booleans>`

* add conditions to represent the observations
  .. code-block:: python

    def project_first(p, q):
      if p == True:
       return True
      if p == False:
       return False
  all the tests pass

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


* use implied conditional testing
  .. code-block:: python

    def project_first(p, q):
      if p:
       return True
      if not p:
       return False

* simplify
  .. code-block:: python

    def project_first(p, q):
      return True if p else False

* simplify further
  .. code-block:: python

    def project_first(p, q):
      return p
  I am still green

Project Second
--------------

RED: make it fail
^^^^^^^^^^^^^^^^^

add a test for project second to ``TestBinaryOperations``

.. code-block:: python

    def test_project_second(self):
      self.assertTrue(truth_table.project_second(True, True))
      self.assertFalse(truth_table.project_second(True, False))
      self.assertTrue(truth_table.project_second(False, True))
      self.assertFalse(truth_table.project_second(False, False))

the terminal shows an :doc:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* add a function definition to ``truth_table.py``
  .. code-block:: python

    def project_second(p, q):
      return False
  the terminal updates to show an :doc:`AssertionError` for the first case
* change the return value to make it pass
  .. code-block:: python

    def project_second(p, q):
      return True
  the terminal updates to show an :doc:`AssertionError` for the second case
* before I add a condition for it, this looks similar to ``logical_equality``, ``exclusive_disjunction``, ``negate_first``, ``negate_second`` and ``project_first`` because 2 out of the 4 cases have the same return value. I observe that

  * if ``q == True`` the result is :doc:`True <data_structures_booleans>`
  * if ``q == False`` the result is :doc:`False <data_structures_booleans>`

* What if I try using the conclusion from ``project_first``
  .. code-block:: python

    def project_second(p, q):
      return p
  the terminal still shows an :doc:`AssertionError`. What if I return ``q`` instead
  .. code-block:: python

    def project_second(p, q):
      return q
  All tests pass and it's a simple line

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

Since there is no refactoring to do here, I update what I know so far. For any boolean operation involving 2 inputs - ``p`` and ``q`` which can take the values :doc:`True <data_structures_booleans>` or :doc:`False <data_structures_booleans>`


* ``project_first`` always returns ``p``
* ``project_second`` always returns ``q``
* ``negate_first`` always returns ``not p``
* ``negate_second`` always returns ``not q``
* ``material_non_implication`` is ``p and not q``
* ``converse_non_implication`` is ``not p and q`` which is different from ``not(p and q)``
* ``logical_nor`` is ``not(p or q)``
* ``logical_nand`` is ``not(p and q)``
* ``exclusive_disjunction`` is ``!=`` aka opposite of ``logical_equality``
* ``logical_implication`` is ``not p or q``
* ``logical_equality`` is ``==``
* ``logical_disjunction`` is ``or``
* ``logical_conjunction`` is ``and``
* ``and`` is "not ``or``"
* ``or`` is "not ``and``"
* :doc:`False <data_structures_booleans>` is ``not True``
* :doc:`True <data_structures_booleans>` is ``not False``
* :doc:`False <data_structures_booleans>` is :doc:`False <data_structures_booleans>`
* :doc:`True <data_structures_booleans>` is :doc:`True <data_structures_booleans>`
