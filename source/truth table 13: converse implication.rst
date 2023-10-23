Truth Table: Converse Implication
=================================

We will continue to step through learning conditional statements in python using Test Driven Development using the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_

Prerequisites
-------------


* `How I setup a Test Driven Development Environment.md <./How I How I setup a Test Driven Development Environment.md.md>`_

----

Converse Implication
--------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

add a test for converse implication to ``(TestBinaryOperations)``

.. code-block:: python

       def test_converse_implication(self):
           self.assertTrue(truth_table.converse_implication(True, True))
           self.assertTrue(truth_table.converse_implication(True, False))
           self.assertFalse(truth_table.converse_implication(False, True))
           self.assertTrue(truth_table.converse_implication(False, False))

the terminal shows an `AttributeError <./ATTRIBUTE_ERROR.md>`_

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* add a function definition to ``truth_table.py``
  .. code-block:: python

       def converse_implication(p, q):
           return False
    the terminal updates to show an `AssertionError <./ASSERTION_ERROR.md>`_ for the first case
* change the return value
  .. code-block:: python

       def converse_implication(p, q):
           return True
    the terminal updates to show an `AssertionError <./ASSERTION_ERROR.md>`_ for the third case
* add a condition for it
  .. code-block:: python

       def converse_implication(p, q):
           if p == False and q == True:
               return False
           else:
               return True
    all the tests pass

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


* use implied conditional testing
  .. code-block:: python

       def converse_implication(p, q):
           if not p and q:
               return False
           else:
               return True
    still passing
* change ``(else)`` to the opposite of the ``(if)`` statement
  .. code-block:: python

       def converse_implication(p, q):
           if not p and q:
               return False
           if not(not p and q):
               return True

* "multiply" out the values in the second condition
  .. code-block:: python

       def converse_implication(p, q):
           if not p and q:
               return False
           if not not p not and not q:
               return True
    the terminal shows a ``(SyntaxError)``\ , fix the syntax
  .. code-block:: python

       def converse_implication(p, q):
           if not p and q:
               return False
           if p or not q:
               return True

* reorder the statements
  .. code-block:: python

       def converse_implication(p, q):
           if p or not q:
               return True
           if not p and q:
               return False

* replace the second condition with ``(else)``
  .. code-block:: python

       def converse_implication(p, q):
           if p or not q:
               return True
           else:
               return False

* simplify it to one line
  .. code-block:: python

       def converse_implication(p, q):
           return p or not q
    You win again! All tests pass

Our knowledge has increased


* ``(converse_implication)`` is ``not p and q`` which is different from ``not(p and q)``
* ``(logical_nor)`` is ``not(p or q)``
* ``(logical_nand)`` is ``not(p and q)``
* ``(exclusive_disjunction)`` is ``!=`` aka opposite of ``(logical_equality)``
* ``(logical_equality)`` is ``==``
* ``(logical_disjunction)`` is ``(or)``
* ``(logical_conjunction)`` is ``(and)``
* ``(and)`` is "not ``(or)``\ "
* ``(or)`` is "not ``(and)``\ "
* ``(False)`` is ``not True``
* ``(True)`` is ``not False``
* ``(False)`` is ``(False)``
* ``(True)`` is ``(True)``
