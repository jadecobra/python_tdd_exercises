.. include:: ../../../links.rst

##########################
truth table: Logical NAND
##########################

Let us take a look at Logical NAND from the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_

.. contents:: table of contents
  :local:
  :depth: 1

----

red: make it fail
#############################################################################

I add a test for Logical NAND to ``TestBinaryOperations`` in ``test_truth_table.py``

.. code-block:: python

    def test_logical_nand(self):
        self.assertFalse(truth_table.logical_nand(True, True))
        self.assertTrue(truth_table.logical_nand(True, False))
        self.assertTrue(truth_table.logical_nand(False, True))
        self.assertTrue(truth_table.logical_nand(False, False))

the terminal shows an :ref:`AttributeError`

green: make it pass
#############################################################################


* I add a definition for the function to ``truth_table.py`` returning :doc:`True </data_structures/booleans/booleans>` since 3 out of the 4 cases return it

  .. code-block:: python

    def logical_nand(p, q):
      return True

  the terminal shows an :ref:`AssertionError` for the first case
* and I add a condition for the one case that returns :doc:`False </data_structures/booleans/booleans>`

  .. code-block:: python

    def logical_nand(p, q):
        if p == True and q == True:
            return False
        return True

  Green! All tests pass

refactor: make it better
#############################################################################

* I add an ``else`` clause to be explicit

  .. code-block:: python

    def logical_nand(p, q):
        if p == True and q == True:
            return False
        else:
            return True

* then change the first condition to an implied conditional test

  .. code-block:: python

    def logical_nand(p, q):
        if p and q:
            return False
        else:
            return True

* I make the ``else`` clause to the opposite of the ``if`` statement

  .. code-block:: python

    def logical_nand(p, q):
        if p and q:
            return False
        if not (p and q):
            return True

* then reorder the statements

  .. code-block:: python

    def logical_nand(p, q):
        if not(p and q):
            return True
        if p and q:
            return False

* I replace the second statement with ``else`` to simplify

  .. code-block:: python

    def logical_nand(p, q):
        if not(p and q):
            return True
        else:
            return False

* then change it to a one line return statement

  .. code-block:: python

    def logical_nand(p, q):
        return True if not(p and q) else False

* which I simplify to

  .. code-block:: python

    def logical_nand(p, q):
        return not(p and q)

----

To review, I know from the tests that for any boolean operation involving 2 inputs: ``p`` and ``q`` which can take the values :doc:`True </data_structures/booleans/booleans>` or :doc:`False </data_structures/booleans/booleans>`


* ``logical NAND`` is ``not (p and q)``
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