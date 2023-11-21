Truth Table: Exclusive Disjunction
==================================

I will continue to step through learning conditional statements in python using Test Driven Development with the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_



Exclusive Disjunction
---------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a test for exclusive disjunction to ``TestBinaryOperations``

.. code-block:: python

    def test_exclusive_disjunction(self):
        self.assertFalse(truth_table.exclusive_disjunction(True, True))
        self.assertTrue(truth_table.exclusive_disjunction(True, False))
        self.assertTrue(truth_table.exclusive_disjunction(False, True))
        self.assertFalse(truth_table.exclusive_disjunction(False, False))

the terminal shows an :doc:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* and I add a definition that returns :doc:`True </data structures: booleans>`

  .. code-block:: python

    def exclusive_disjunction(p, q):
        return True

  I get an :doc:`AssertionError` for the second case
* then add a condition for it

  .. code-block:: python

    def exclusive_disjunction(p , q):
        if p == True and q == True:
            return False
        return True

  the terminal shows an :doc:`AssertionError` for the fourth case
* I add a condition to resolve it

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p == False and q == False:
            return False
        if p == True and q == True:
            return False
        return True

  Wonderful! All the tests are passing

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

* In the first case ``p`` and ``q`` have the same value, I can change the statement to reflect this like I did with ``logical_equality``

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p == q:
            return False
        if p == True and q == True:
            return False
        return True

  tests still pass
* the next statement looks similar, I can rewrite it as

  .. code-block:: python

    def exclusive_disjunction(p, q):
      if p == q:
          return False
      if p == q:
          return False
      return True

  I remove the repetition since it's exactly the same statement as the first

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p == q:
            return False
        return True

* I add an ``else`` statement to be explicit

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

* then replace the second one with ``else``

  .. code-block:: python

    def exclusive_disjunction(p, q):
        if p != q:
            return True
        else:
            return False

* time to use the one line return statement

  .. code-block:: python

    def exclusive_disjunction(p, q):
        return True if p != q else False

* then using implied conditional testing I can simplify it to

  .. code-block:: python

    def exclusive_disjunction(p, q):
        return p != q

So far I know that For any boolean operation involving 2 inputs - ``p`` and ``q`` which can take the values :doc:`True </data structures: booleans>` or :doc:`False </data structures: booleans>`


* ``exclusive_disjunction`` is ``!=``
* ``logical_equality`` is ``==``
* ``logical_disjunction`` is ``or``
* ``logical_conjunction`` is ``and``
* ``and`` is "not ``or``"
* ``or`` is "not ``and``"
* :doc:`False </data structures: booleans>` is ``not True``
* :doc:`True </data structures: booleans>` is ``not False``
* :doc:`False </data structures: booleans>` is :doc:`False </data structures: booleans>`
* :doc:`True </data structures: booleans>` is :doc:`True </data structures: booleans>`
* ``return True if x else y`` can be rewritten as ``return x`` if ``x`` evaluates to :doc:`True </data structures: booleans>`
