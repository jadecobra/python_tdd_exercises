.. include:: ../../../links.rst

###################################
truth table: Exclusive Disjunction
###################################

The following tests show Exclusive Disjunction from the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_

.. contents:: table of contents
  :local:
  :depth: 1

----


red: make it fail
#################################################################################

I add a test for exclusive disjunction to ``TestBinaryOperations`` in ``test_truth_table.py``

.. code-block:: python

    def test_exclusive_disjunction(self):
        self.assertFalse(src.truth_table.exclusive_disjunction(True, True))
        self.assertTrue(src.truth_table.exclusive_disjunction(True, False))
        self.assertTrue(src.truth_table.exclusive_disjunction(False, True))
        self.assertFalse(src.truth_table.exclusive_disjunction(False, False))

and the terminal shows :ref:`AttributeError`

green: make it pass
#################################################################################

* then add a definition that returns :ref:`True<test_what_is_true>`

  .. code-block:: python

    def exclusive_disjunction(p, q):
        return True

  the terminal shows :ref:`AssertionError` for the second case
* I add a condition for it

  .. code-block:: python

    def exclusive_disjunction(p , q):
        if p == True and q == True:
            return False
        return True

  and the terminal shows :ref:`AssertionError` for the fourth case
* I add a condition to resolve it

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p == True and q == True:
            return False
        if p == False and q == False:
            return False
        return True

  and all the tests pass. Wonderful!

refactor: make it better
#################################################################################

* In the first case ``p`` and ``q`` have the same value, I can change the statement to reflect this like I did with ``logical_equality``

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p == q:
            return False
        if p == False and q == False:
            return False
        return True

  tests still pass
* the second statement looks similar, I can rewrite it as

  .. code-block:: python

    def exclusive_disjunction(p, q):
      if p == q:
          return False
      if p == q:
          return False
      return True

* I remove the repetition since it is exactly the same statement as the first

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p == q:
            return False
        return True

* I add an ``else`` clause to be explicit

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p == q:
            return False
        else:
            return True

* then rewrite it as the opposite ``if`` statement

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p == q:
            return False
        if p != q:
            return True

* I reorder the statements

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p != q:
            return True
        if p == q:
            return False

* then change the second one with ``else``

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p != q:
            return True
        else:
            return False

* time to use the one line `return statement`_

  .. code-block:: python

    def exclusive_disjunction(p, q):
        return True if p != q else False

* then using implied conditional testing I can simplify it to

  .. code-block:: python

    def exclusive_disjunction(p, q):
        return p != q

From the tests I see that for any boolean operation involving 2 inputs: ``p`` and ``q`` which can take the values :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`



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