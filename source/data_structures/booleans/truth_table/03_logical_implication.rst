.. include:: ../../../links.rst

#################################################################################
truth table: Logical Implication
#################################################################################

.. contents:: table of contents
  :local:
  :depth: 1

----

This chapter has tests for Logical Implication from the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_

Reviewing what I know so far, for any boolean operation involving 2 inputs: ``p`` and ``q`` which can take the values :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`


* ``logical disjunction`` is or_
* and_ is "not or_"
* or_ is "not and_"
* ``logical conjunction`` is and_
* ``return True if x else y`` can be rewritten as ``return x``, if ``x`` evaluates to :ref:`True<test_what_is_true>`
* when there are multiple outcomes I only need to write the condition for the special case and use ``else`` for the others
* :ref:`False<test_what_is_false>` is not_ :ref:`True<test_what_is_true>`
* :ref:`True<test_what_is_true>` is not_ :ref:`False<test_what_is_false>`
* :ref:`False<test_what_is_false>` is :ref:`False<test_what_is_false>`
* :ref:`True<test_what_is_true>` is :ref:`True<test_what_is_true>`

red: make it fail
#################################################################################

I add a test for logical implication to ``TestBinaryOperations`` in ``test_truth_table.py``

.. code-block:: python

    def test_logical_implication_or_material_implication(self):
        self.assertTrue(src.truth_table.logical_implication(True, True))
        self.assertFalse(src.truth_table.logical_implication(True, False))
        self.assertTrue(src.truth_table.logical_implication(False, True))
        self.assertTrue(src.truth_table.logical_implication(False, False))

the terminal shows :ref:`AttributeError`

green: make it pass
#################################################################################


* I add a:ref:`function<functions>`definition with :ref:`True<test_what_is_true>` as the return value since it is expected in 3 out of the 4 cases

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
#################################################################################


* What if I make the nested condition one line?

  .. code-block:: python

    def logical_implication(p, q):
        if p == True and q == False:
            return False
        return True

  the tests still pass
* in the earlier examples I changed the equality tests with implied condition statements

  .. code-block:: python

    def logical_implication(p, q):
        if p and not q:
            return False
        return True

  this looks simpler and the tests still pass
* I write out the second part with an else_ clause to be explicit

  .. code-block:: python

    def logical_implication(p, q):
        if p and not q:
            return False
        else:
            return True

* then change the else_ clause with the opposite of the `if statement`_ to get

  .. code-block:: python

    def logical_implication(p, q):
        if p and not q:
            return False
        if not(p and not q):
            return True

* when I "multiply" out the statement with not_ to

  .. code-block:: python

    def logical_implication(p, q):
        if p and not q:
            return False
        if not p not and not not q:
            return True

  I get a SyntaxError_ and change it to get

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

* then change the second statement with an ``else``

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


fantastic! the tests pass. I can see that for any boolean operation involving 2 inputs: ``p`` and ``q`` which can take the values :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`

* ``logical implication`` is ``not p or q``
* ``logical disjunction`` is or_
* ``logical conjunction`` is and_
* and_ is "not or_"
* or_ is "not and_"
* :ref:`False<test_what_is_false>` is not_ :ref:`True<test_what_is_true>`
* :ref:`True<test_what_is_true>` is not_ :ref:`False<test_what_is_false>`
* :ref:`False<test_what_is_false>` is :ref:`False<test_what_is_false>`
* :ref:`True<test_what_is_true>` is :ref:`True<test_what_is_true>`

----

:doc:`/code/code_truth_table`