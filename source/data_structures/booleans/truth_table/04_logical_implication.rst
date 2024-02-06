.. include:: ../../../links.rst

#################################
Truth Table: Logical Implication
#################################

This chapter contains tests for Logical Implication from the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_

Reviewing what I know so far, for any boolean operation involving 2 inputs: ``p`` and ``q`` which can take the values :doc:`True </data_structures/booleans/booleans>` or :doc:`False </data_structures/booleans/booleans>`


* ``logical disjunction`` is ``or``
* ``and`` is "not ``or``"
* ``or`` is "not ``and``"
* ``logical conjunction`` is ``and``
* ``return True if x else y`` can be rewritten as ``return x``, if ``x`` evaluates to :doc:`True </data_structures/booleans/booleans>`
* when there are multiple outcomes I only need to write the condition for the special case and use ``else`` for the others
* :doc:`False </data_structures/booleans/booleans>` is ``not True``
* :doc:`True </data_structures/booleans/booleans>` is ``not False``
* :doc:`False </data_structures/booleans/booleans>` is :doc:`False </data_structures/booleans/booleans>`
* :doc:`True </data_structures/booleans/booleans>` is :doc:`True </data_structures/booleans/booleans>`


red: make it fail
^^^^^^^^^^^^^^^^^

I add a test for logical implication to ``TestBinaryOperations`` in ``test_truth_table.py``

.. code-block:: python

    def test_logical_implication_or the_material_implication(self):
        self.assertTrue(truth_table.logical_implication(True, True))
        self.assertFalse(truth_table.logical_implication(True, False))
        self.assertTrue(truth_table.logical_implication(False, True))
        self.assertTrue(truth_table.logical_implication(False, False))

the terminal shows an :ref:`AttributeError`

green: make it pass
^^^^^^^^^^^^^^^^^^^


* I add a function definition with :doc:`True </data_structures/booleans/booleans>` as the return value since it is expected in 3 out of the 4 cases

  .. code-block:: python

    def logical_implication(p, q):
        return True

  the terminal shows the second case failing
* I add a condition for this case

  .. code-block:: python

    def logical_implication(p, q):
        if p == True:
            if q == False:
                return False
        return True

  the tests pass!

refactor: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


* What if I make the nested condition one line?

  .. code-block:: python

    def logical_implication(p, q):
        if p == True and q == False:
            return False
        return True

  the tests still pass
* in the earlier examples I replaced the equality tests with implied condition statements

  .. code-block:: python

    def logical_implication(p, q):
        if p and not q:
            return False
        return True

  this looks simpler and the tests still pass
* I write out the second part with an ``else`` clause to be explicit

  .. code-block:: python

    def logical_implication(p, q):
        if p and not q:
            return False
        else:
            return True

* then replace the ``else`` clause with the opposite of the ``if`` statement to get

  .. code-block:: python

    def logical_implication(p, q):
        if p and not q:
            return False
        if not(p and not q):
            return True

* when I "multiply" out the statement with ``not`` to

  .. code-block:: python

    def logical_implication(p, q):
        if p and not q:
            return False
        if not p not and not not q:
            return True

  I get a ``SyntaxError`` and correct the syntax to get

  .. code-block:: python

    def logical_implication(p, q):
        if p and not q:
            return False
        if not p or q:
            return True

* I reorder the statements

  .. code-block:: python

    def logical_implication(p, q):
        if not p or q:
            return True
        if p and not q:
            return False

* then replace the second statement with an ``else``

  .. code-block:: python

    def logical_implication(p, q):
        if not p or q:
            return True
        else:
            return False

* and rewrite the statements as one line

  .. code-block:: python

    def logical_implication(p, q):
        return True if not p or q else False

* I simplify using python's implicit conditional testing

  .. code-block:: python

    def logical_implication(p, q):
        return not p or q


fantastic! the tests pass. I can see that for any boolean operation involving 2 inputs: ``p`` and ``q`` which can take the values :doc:`True </data_structures/booleans/booleans>` or :doc:`False </data_structures/booleans/booleans>`

* ``logical implication`` is ``not p or q``
* ``logical disjunction`` is ``or``
* ``logical conjunction`` is ``and``
* ``and`` is "not ``or``"
* ``or`` is "not ``and``"
* :doc:`False </data_structures/booleans/booleans>` is ``not True``
* :doc:`True </data_structures/booleans/booleans>` is ``not False``
* :doc:`False </data_structures/booleans/booleans>` is :doc:`False </data_structures/booleans/booleans>`
* :doc:`True </data_structures/booleans/booleans>` is :doc:`True </data_structures/booleans/booleans>`