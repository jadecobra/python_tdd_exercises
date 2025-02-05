.. include:: ../../../links.rst

##########################
truth table: Logical NOR
##########################

.. contents:: table of contents
  :local:
  :depth: 1

----

These tests show Logical NOR from the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_

red: make it fail
#################################################################################

I add a test for exclusive disjunction to ``TestBinaryOperations`` in ``test_truth_table.py``

.. code-block:: python

    def test_logical_nor(self):
        self.assertFalse(src.truth_table.logical_nor(True, True))
        self.assertFalse(src.truth_table.logical_nor(True, False))
        self.assertFalse(src.truth_table.logical_nor(False, True))
        self.assertTrue(src.truth_table.logical_nor(False, False))

and the terminal shows :ref:`AttributeError`

green: make it pass
#################################################################################

* I add a function definition to ``truth_table.py``

  .. code-block:: python

    def logical_nor(p, q):
        return False

* and the first 3 pass, there is a failure for the 4th case, so I add a condition for it

  .. code-block:: python

    def logical_nor(p, q):
        if p == False and q == False:
            return True
        return False

refactor: make it better
#################################################################################

* I restate the ``if`` condition using implicit conditional testing

  .. code-block:: python

    def logical_nor(p, q):
        if not p and not q:
            return True
        return False

* I abstract the repetition of not_ by rewriting the entire statement in terms of not_

  .. code-block:: python

    def logical_nor(p, q):
        if (not p) (not or) (not q):
            return True
        return False

  the terminal shows a ``SyntaxError`` and I rewrite the statement with proper syntax, "factoring" out the not_

  .. code-block:: python

    def logical_nor(p, q):
        if not(p or q):
            return True
        return False

* then rewrite the entire thing on one line

  .. code-block:: python

    def logical_nor(p, q):
      return True if not(p or q) else False

* I simplify using implied conditional testing

  .. code-block:: python

    def logical_nor(p, q):
        return not(p or q)


From these tests, I can say that for any boolean operation involving 2 inputs: ``p`` and ``q`` which can take the values :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>`


* ``logical NOR`` is ``not (p or q)``
* ``logical NAND`` is ``not (p and q)``
* ``exclusive disjunction`` is ``!=`` or the opposite of ``logical_equality``
* ``logical equality`` is ``==``
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