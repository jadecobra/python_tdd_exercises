.. include:: ../../../links.rst

###################################
truth table: Converse Implication
###################################

.. contents:: table of contents
  :local:
  :depth: 1

----

This chapter continues the journey of writing conditional statements using the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_


red: make it fail
#################################################################################

I add a test for converse implication to ``TestBinaryOperations`` in ``test_truth_table.py``

.. code-block:: python

    def test_converse_implication(self):
        self.assertTrue(truth_table.converse_implication(True, True))
        self.assertTrue(truth_table.converse_implication(True, False))
        self.assertFalse(truth_table.converse_implication(False, True))
        self.assertTrue(truth_table.converse_implication(False, False))

the terminal shows an :ref:`AttributeError`

green: make it pass
#################################################################################

* I add a function definition to ``truth_table.py``

  .. code-block:: python

    def converse_implication(p, q):
        return False

  and the terminal shows an :ref:`AssertionError` for the first case
* I make the return value

  .. code-block:: python

    def converse_implication(p, q):
        return True

  the terminal shows an :ref:`AssertionError` for the third case
* I add a condition for it and an explicit ``else`` clause

  .. code-block:: python

    def converse_implication(p, q):
        if p == False and q == True:
            return False
        else:
            return True

  all the tests pass

refactor: make it better
#################################################################################

* I change the ``if`` condition using python's implied conditional testing

  .. code-block:: python

    def converse_implication(p, q):
        if not p and q:
            return False
        else:
            return True

  the tests are still passing
* I make ``else`` to the opposite of the ``if`` statement

  .. code-block:: python

    def converse_implication(p, q):
        if not p and q:
            return False
        if not (not p and q):
            return True

* When I "multiply" out the values in the second condition I get

  .. code-block:: python

    def converse_implication(p, q):
        if not p and q:
            return False
        if (not not p) (not and) (not q):
            return True

  the terminal shows a ``SyntaxError``
* which I fix by canceling out ``not not`` and replacing ``not and`` with ``or``

  .. code-block:: python

    def converse_implication(p, q):
        if not p and q:
            return False
        if p or not q:
            return True

* then reorder the statements

  .. code-block:: python

    def converse_implication(p, q):
        if p or not q:
            return True
        if not p and q:
            return False

* I change the second condition with ``else``

  .. code-block:: python

    def converse_implication(p, q):
        if p or not q:
            return True
        else:
            return False

* then simplify it to one line

  .. code-block:: python

    def converse_implication(p, q):
        return p or not q

  I win again! All tests pass

My knowledge has increased, from the tests I know that for any boolean operation involving 2 inputs: ``p`` and ``q`` which can take the values :doc:`True </data_structures/booleans/booleans>` or :doc:`False </data_structures/booleans/booleans>`

* ``converse implication`` is ``not p and q`` which is different from ``not (p and q)``
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

----

:doc:`/code/code_truth_table`