
#####################
Truth Table: Project
#####################

This chapter shows the projection Binary Operations from the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_ using tests


Project First
-------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a test for project first to ``TestBinaryOperations`` in ``test_truth_table.py``

.. code-block:: python

    def test_project_first(self):
        self.assertTrue(truth_table.project_first(True, True))
        self.assertTrue(truth_table.project_first(True, False))
        self.assertFalse(truth_table.project_first(False, True))
        self.assertFalse(truth_table.project_first(False, False))

the terminal shows an :ref:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* then I add a function definition to ``truth_table.py``

  .. code-block:: python

    def project_first(p, q):
        return False

  and the terminal shows an :ref:`AssertionError` for the first case
* I change the return statement

  .. code-block:: python

    def project_first(p, q):
        return True

  and the :ref:`AssertionError` is now for the third case
* before I add a condition for it, this looks similar to ``logical_equality``, ``exclusive_disjunction``, ``negate_first`` and ``negate_second`` because 2 out of the 4 cases have the same return value. I see that

  * when ``p == True`` the result is :doc:`True </data_structures/booleans/booleans>`
  * when ``p == False`` the result is :doc:`False </data_structures/booleans/booleans>`

* I add conditions to represent this

  .. code-block:: python

    def project_first(p, q):
        if p == True:
            return True
        if p == False:
            return False

  and the tests pass

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

* I use implied conditional testing to simplify the statements

  .. code-block:: python

    def project_first(p, q):
        if p:
            return True
        if not p:
            return False

* I simplify again

  .. code-block:: python

    def project_first(p, q):
        return True if p else False

* then simplify some more

  .. code-block:: python

    def project_first(p, q):
        return p

  I am still green. Lovely!

Project Second
--------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a test for project second to ``TestBinaryOperations``

.. code-block:: python

    def test_project_second(self):
        self.assertTrue(truth_table.project_second(True, True))
        self.assertFalse(truth_table.project_second(True, False))
        self.assertTrue(truth_table.project_second(False, True))
        self.assertFalse(truth_table.project_second(False, False))

the terminal shows an :ref:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* When I add a function definition to ``truth_table.py``

  .. code-block:: python

    def project_second(p, q):
        return False

  the terminal shows an :ref:`AssertionError` for the first case
* and I change the return value to make it pass

  .. code-block:: python

    def project_second(p, q):
        return True

  the terminal shows an :ref:`AssertionError` for the second case
* before I add a condition for it, this looks similar to ``logical_equality``, ``exclusive_disjunction``, ``negate_first``, ``negate_second`` and ``project_first`` because 2 out of the 4 cases have the same return value. I see that

  * when ``q == True`` the result is :doc:`True </data_structures/booleans/booleans>`
  * when ``q == False`` the result is :doc:`False </data_structures/booleans/booleans>`

* What if I try using the conclusion from ``project_first``?

  .. code-block:: python

    def project_second(p, q):
        return p

  the terminal still shows an :ref:`AssertionError`
* What if I return ``q`` instead?
  .. code-block:: python

    def project_second(p, q):
        return q

  All tests pass and it is a simple line

-----

From the tests I know that for any boolean operation involving 2 inputs: ``p`` and ``q`` which can take the values :doc:`True </data_structures/booleans/booleans>` or :doc:`False </data_structures/booleans/booleans>`


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
