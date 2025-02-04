.. include:: ../../../links.rst

#####################################
truth table: Material NonImplication
#####################################

.. contents:: table of contents
  :local:
  :depth: 1

----

More conditional statements from the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_, this time for Material NonImplication

red: make it fail
#################################################################################

I add a test for material non-implication to ``TestBinaryOperations`` in ``test_truth_table.py``

.. code-block:: python

    def test_material_non_implication(self):
        self.assertFalse(src.truth_table.material_non_implication(True, True))
        self.assertTrue(src.truth_table.material_non_implication(True, False))
        self.assertFalse(src.truth_table.material_non_implication(False, True))
        self.assertFalse(src.truth_table.material_non_implication(False, False))

the terminal shows :ref:`AttributeError`

green: make it pass
#################################################################################


* I add a function definition to ``truth_table.py``

  .. code-block:: python

    def material_non_implication(p, q):
        return False

  the terminal shows :ref:`AssertionError` for the second case
* I add a condition for it

  .. code-block:: python

      def material_non_implication(p, q):
          if p == True and q == False:
              return True
          return False

  and the tests pass

refactor: make it better
#################################################################################


* I use implied conditional testing for the first part of the if statement

  .. code-block:: python

    def material_non_implication(p, q):
        if p and q == False:
            return True
        else:
            return False

  all tests still pass

* then change the second part to use ``not``

  .. code-block:: python

    def material_non_implication(p, q):
        if p and not q:
            return True
        else:
            return False

* I rewrite with a ``return`` statement

  .. code-block:: python

    def material_non_implication(p, q):
        return p and not q

  and I am still green

From these tests, I can say that for any boolean operation involving 2 inputs: ``p`` and ``q`` which can take the values :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`


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
* :ref:`False<test_what_is_false>` is ``not True``
* :ref:`True<test_what_is_true>` is ``not False``
* :ref:`False<test_what_is_false>` is :ref:`False<test_what_is_false>`
* :ref:`True<test_what_is_true>` is :ref:`True<test_what_is_true>`

----

:doc:`/code/code_truth_table`