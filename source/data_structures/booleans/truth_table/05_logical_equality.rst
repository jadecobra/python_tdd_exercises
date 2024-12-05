.. include:: ../../../links.rst

#################################
truth table: Logical Equality
#################################

.. contents:: table of contents
  :local:
  :depth: 1

----

The journey of conditional statements using the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_ continues with Logical Equality

So far the tests have shown that for any boolean operation involving 2 inputs: ``p`` and ``q`` which can take the values :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`

* ``logical implication`` is ``not p or q``
* ``and`` is "not ``or``"
* ``or`` is "not ``and``"
* ``logical disjunction`` is ``or``
* ``logical conjunction`` is ``and``
* :ref:`False<test_what_is_false>` is ``not True``
* :ref:`True<test_what_is_true>` is ``not False``
* :ref:`False<test_what_is_false>` is :ref:`False<test_what_is_false>`
* :ref:`True<test_what_is_true>` is :ref:`True<test_what_is_true>`
* ``return True if x else y`` can be rewritten as ``return x`` if ``x`` evaluates to :ref:`True<test_what_is_true>`
* when there are multiple outcomes I only need to write the condition for the special case and use ``else`` for the others


red: make it fail
#################################################################################

I add a test for logical equality to ``TestBinaryOperations`` in ``test_truth_table.py``

.. code-block:: python

    def test_logical_equality_or_logical_biconditional(self):
        self.assertTrue(truth_table.logical_equality(True, True))
        self.assertFalse(truth_table.logical_equality(True, False))
        self.assertFalse(truth_table.logical_equality(False, True))
        self.assertTrue(truth_table.logical_equality(False, False))

and the terminal shows an :ref:`AttributeError`

green: make it pass
#################################################################################


* I then add a definition to ``truth_table.py`` with a `return statement`_, I can pick :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>` since 2 out of the 4 cases are either :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`

  .. code-block:: python

    def logical_equality(p, q):
        return True

  the terminal shows a failure for the second case
* I add a condition for it

  .. code-block:: python

    def logical_equality(p, q):
        if p == True and q == False:
            return False
        return True

  the terminal shows a failure for the 3rd case
* I add a condition for it

  .. code-block:: python

    def logical_equality(p, q):
        if p == True and q == False:
            return False
        if p == False and q == True:
            return False
        return True

  Green! All tests pass

refactor: make it better
#################################################################################

What can I do to make this better?


* looking at the test cases, I see that there are only 2 states

  * logical_equality returns True when ``p`` and ``q`` are the same
  * logical_equality returns False when ``p`` and ``q`` are not the same

* I rewrite the conditional statements to reflect the second observation

  .. code-block:: python

    def logical_equality(p, q):
        if p != q:
            return False
        return True

* then add the first observation

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

* then change the second condition with ``else``

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

* I can use implicit conditional comparison

  .. code-block:: python

    def logical_equality(p, q):
        return p == q

  and the tests are still green

what I know so far from the tests is that for any boolean operation involving 2 inputs: ``p`` and ``q`` which can take the values :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`

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