Truth Table: Logical Implication
================================

We will continue to step through learning conditional statements in python using Test Driven Development using the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_

Reviewing what we know so far, for any boolean operation involving 2 inputs - ``(p)`` and ``(q)`` which can take the values ``(True)`` or ``(False)``


* ``(and)`` is "not ``(or)``\ "
* ``(or)`` is "not ``(and)``\ "
* ``(logical_disjunction)`` is ``(or)``
* ``(logical_conjunction)`` is ``(and)``
* ``(False)`` is ``not True``
* ``(True)`` is ``not False``
* ``(False)`` is ``(False)``
* ``(True)`` is ``(True)``
* ``return True if x else y`` can be rewritten as ``return x`` if ``(x)`` evaluates to ``(True)``
* when there are multiple outcomes we only need to write the condition for the special case and use ``(else)`` for the others

Prerequisites
-------------


* `How I setup a Test Driven Development Environment <./How I How I setup a Test Driven Development Environment.md>`_

----

Logical Implication/Material Implication
----------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

add a test for logical implication to ``(TestBinaryOperations)``

.. code-block:: python

       def test_logical_implication_aka_material_implication(self):
           self.assertTrue(truth_table.logical_implication(True, True))
           self.assertFalse(truth_table.logical_implication(True, False))
           self.assertTrue(truth_table.logical_implication(False, True))
           self.assertTrue(truth_table.logical_implication(False, False))

the terminal updates to show an `AttributeError <./ATTRIBUTE_ERROR.md>`_

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* add a function definition with ``(True)`` as the return value since that is what is expected in 3 out of the 4 cases
  .. code-block:: python

       def logical_implication(p, q):
           return True
    the terminal updates to show the second case failing
* add a condition for this case
  .. code-block:: python

       def logical_implication(p, q):
           if p == True:
               if q == False:
                   return False
           return True
    the tests pass!

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


* How can we make this better? let us make the nested condition one line
  .. code-block:: python

       def logical_implication(p, q):
           if p == True and q == False:
               return False
           return True
    the tests still pass
* in the earlier examples we replaced the equality tests with implied condition statements
  .. code-block:: python

       def logical_implication(p, q):
           if p and not q:
               return False
           return True
    this looks simpler and the tests still pass.
* let us write out the second half with an ``(else)`` statement to be explicit
  .. code-block:: python

       def logical_implication(p, q):
           if p and not q:
               return False
           else:
               return True

* if we replace the ``(else)`` with the opposite of the ``(if)`` statement we get
  .. code-block:: python

       def logical_implication(p, q):
           if p and not q:
               return False
           if not(p and not q):
               return True

* "multiplying" it out
  .. code-block:: python

       def logical_implication(p, q):
           if p and not q:
               return False
           if not p not and not not q:
               return True
    We get a ``(SyntaxError)`` and correct the syntax to get
  .. code-block:: python

       def logical_implication(p, q):
           if p and not q:
               return False
           if not p or q:
               return True

* We reorder
  .. code-block:: python

       def logical_implication(p, q):
           if not p or q:
               return True
           if p and not q:
               return False

* replace the second statement with an ``(else)``
  .. code-block:: python

       def logical_implication(p, q):
           if not p or q:
               return True
           else:
               return False

* try to write it as one line?
  .. code-block:: python

       def logical_implication(p, q):
           return True if not p or q else False

* we simplify using python's implicit conditional testing
  .. code-block:: python

       def logical_implication(p, q):
           return not p or q
    fantastic! the tests pass
