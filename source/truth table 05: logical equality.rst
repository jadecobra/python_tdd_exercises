Truth Table: Logical Equality
=============================

The journey through conditional statements in python using Test Driven Development with the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_ continues with Logical Equality

To review, for any boolean operation involving 2 inputs - ``p`` and ``q`` which can take the values :doc:`True </data structures: booleans>` or :doc:`False </data structures: booleans>`

* ``logical_implication`` is ``not p or q``
* ``and`` is "not ``or``"
* ``or`` is "not ``and``"
* ``logical_disjunction`` is ``or``
* ``logical_conjunction`` is ``and``
* :doc:`False </data structures: booleans>` is ``not True``
* :doc:`True </data structures: booleans>` is ``not False``
* :doc:`False </data structures: booleans>` is :doc:`False </data structures: booleans>`
* :doc:`True </data structures: booleans>` is :doc:`True </data structures: booleans>`
* ``return True if x else y`` can be rewritten as ``return x`` if ``x`` evaluates to :doc:`True </data structures: booleans>`
* when there are multiple outcomes I only need to write the condition for the special case and use ``else`` for the others

Logical Equality/Logical Bi-conditional
---------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a test for logical equality to ``TestBinaryOperations`` in ``test_truth_table.py``

.. code-block:: python

    def test_logical_equality_aka_logical_biconditional(self):
        self.assertTrue(truth_table.logical_equality(True, True))
        self.assertFalse(truth_table.logical_equality(True, False))
        self.assertFalse(truth_table.logical_equality(False, True))
        self.assertTrue(truth_table.logical_equality(False, False))

the terminal shows an :doc:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* I add a definition to ``truth_table.py`` with a return statement, I can pick :doc:`True </data structures: booleans>` or :doc:`False </data structures: booleans>` since 2 out of the 4 cases are either :doc:`True </data structures: booleans>` or :doc:`False </data structures: booleans>`

  .. code-block:: python

    def logical_equality(p, q):
        return True

  the terminal updates to show a failure for the second case
* I add a condition for it

  .. code-block:: python

    def logical_equality(p, q):
        if p == True and q == False:
            return False
        return True

  the terminal now shows a failure for the 3rd case
* I add a condition for it

  .. code-block:: python

    def logical_equality(p, q):
        if p == True and q == False:
            return False
        if p == False and q == True:
            return False
        return True

  I am green!

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

What can I do to make this better?


* looking at the test cases, I can summarize them as 2 states

  * logical_equality returns True when ``p`` and ``q`` are the same
  * logical_equality returns False when ``p`` and ``q`` are not the same

* I rewrite the condition statements to reflect the second observation

  .. code-block:: python

    def logical_equality(p, q):
        if p != q:
            return False
        return True

* updating the function with the first observation I have

  .. code-block:: python

    def logical_equality(p, q):
        if p != q:
            return False
        if p == q:
            return True

* I reorder the statements

  .. code-block:: python

    def logical_equality(p, q):
        if p == q:
            return True
        if p != q:
            return False

* then replace the second condition with ``else``

  .. code-block:: python

    def logical_equality(p, q):
        if p == q:
            return True
        else:
            return False

* rewriting both statements as one line with the ``return`` statement

  .. code-block:: python

    def logical_equality(p, q):
        return True if p == q else False

* I then use implicit conditional comparison

  .. code-block:: python

    def logical_equality(p, q):
        return p == q

  and the tests are still green

I can update what I know so far from the tests to say, For any boolean operation involving 2 inputs - ``p`` and ``q`` which can take the values :doc:`True </data structures: booleans>` or :doc:`False </data structures: booleans>`


* ``logical_equality`` is ``==``
* ``logical_implication`` is ``not p or q``
* ``logical_disjunction`` is ``or``
* ``logical_conjunction`` is ``and``
* ``and`` is "not ``or``"
* ``or`` is "not ``and``"
* :doc:`False </data structures: booleans>` is ``not True``
* :doc:`True </data structures: booleans>` is ``not False``
* :doc:`False </data structures: booleans>` is :doc:`False </data structures: booleans>`
* :doc:`True </data structures: booleans>` is :doc:`True </data structures: booleans>`
* ``return True if x else y`` can be rewritten as ``return x`` if ``x`` evaluates to :doc:`True </data structures: booleans>`
