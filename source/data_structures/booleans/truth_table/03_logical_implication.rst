.. include:: ../../../links.rst

#################################################################################
truth table: Logical Implication and Logical Equality
#################################################################################

.. contents:: table of contents
  :local:
  :depth: 1

----

*********************************************************************************
requirements
*********************************************************************************

:doc:`how to make a python test driven development environment </how_to/make_tdd_environment>` with ``truth_table`` as the name of the project

*********************************************************************************
test_logical_implication
*********************************************************************************

red: make it fail
#################################################################################

I add a test

.. code-block:: python

    def test_logical_or_material_implication(self):
        self.assertTrue(src.truth_table.logical_implication(True, True))

the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.truth_table' has no attribute 'logical_implication'. Did you mean: 'logical_disjunction'?

green: make it pass
#################################################################################

I add the :ref:`method<functions>`

.. code-block:: python

  def logical_implication(p, q):
      return p or q

the terminal shows green

refactor: make it better
#################################################################################


* I add the next case

  .. code-block:: python

    def test_logical_or_material_implication(self):
        self.assertTrue(src.truth_table.logical_implication(True, True))
        self.assertFalse(src.truth_table.logical_implication(True, False))

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True is not false

  I add an if statement_

  .. code-block:: python

    def logical_implication(p, q):
        if p == True:
            if q == False:
                return False
        return p or q

  the terminal shows green again

* I add

  .. code-block:: python


    def test_logical_or_material_implication(self):
        self.assertTrue(src.truth_table.logical_implication(True, True))
        self.assertFalse(src.truth_table.logical_implication(True, False))
        self.assertTrue(src.truth_table.logical_implication(False, True))
        self.assertTrue(src.truth_table.logical_implication(False, False))


  .. code-block:: python

    def test_logical_or_material_implication(self):
        self.assertTrue(src.truth_table.logical_implication(True, True))
        self.assertFalse(src.truth_table.logical_implication(True, False))
        self.assertTrue(src.truth_table.logical_implication(False, True))
        self.assertTrue(src.truth_table.logical_implication(False, False))


* I add a condition for this case

  .. code-block:: python

    def logical_implication(p, q):
        if p == True:
            if q == False:
                return False
        return True

  the tests pass!



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

*********************************************************************************
test_logical_equality
*********************************************************************************

----

*********************************************************************************
review
*********************************************************************************

----

:doc:`/code/code_truth_table`