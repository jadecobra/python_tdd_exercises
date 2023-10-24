Truth Table: Logical Disjunction
================================

We will continue to step through learning conditional statements in python using Test Driven Development using the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_

Reviewing what we know so far


* we can express ``conditional statements`` on one line with ``return``
* when there are multiple outcomes we only need to write the condition for the special case and use ``else`` for the others
* ``logical_conjunction`` is ``and``
* ``False`` is ``not True``
* ``True`` is ``not False``
* ``False`` is ``False``
* ``True`` is ``True``

Prerequisites
-------------


* `How I setup a Test Driven Development Environment <./How I setup a Test Driven Development Environment.rst>`_

----

Logical Disjunction
-------------------

RED: make it fail
~~~~~~~~~~~~~~~~~

add a test for logical disjunction to ``TestBinaryOperations`` in ``test_truth_table.py``

.. code-block:: python

       def test_logical_disjunction(self):
           self.assertTrue(truth_table.logical_disjunction(True, True))
           self.assertTrue(truth_table.logical_disjunction(True, False))
           self.assertTrue(truth_table.logical_disjunction(False, True))
           self.assertFalse(truth_table.logical_disjunction(False, False))

the terminal updates to show an `AttributeError <./AttributeError.rst>`_

GREEN: make it pass
~~~~~~~~~~~~~~~~~~~


* update ``truth_table.py`` with a function definition like we did for ``logical_conjunction``

  .. code-block:: python

       def logical_disjunction(p, q):
           return True

  the terminal updates to show an `AssertionError <./AssertionError.rst>`_

* 3 of the test cases are passing because ``logical_disjunction`` returns ``True`` in 3 of the 4. We need a condition for the fourth case to pass. update the definition

  .. code-block:: python

       def logical_disjunction(p, q):
           if p == False:
               if q == False:
                   return False
           return True

  the terminal updates to show passing tests

REFACTOR: make it better
~~~~~~~~~~~~~~~~~~~~~~~~


* we know from earlier that when we have a nested if statement it can be replaced with an ``and``, so we update our condition

  .. code-block:: python

       def logical_disjunction(p, q):
           if p == False and q == False:
               return False
           return True

  the terminal shows our tests are still passing

* we can restate the equality comparison against ``False`` in terms of ``True`` by using the ``not equal`` comparison operator ``!=``

  .. code-block:: python

       def logical_disjunction(p, q):
           if p != False and q != False:
               return False
           return True

* how can we express the ``if`` statement using python's implied comparison evaluation? we can use the ``not`` keyword like we did with ``logical_negation``

  .. code-block:: python

       def logical_disjunction(p, q):
           if not p and not q:
               return False
           return True

* ``not`` happens twice in that statement. What if we see if we can "factor" it out using algebra

  .. code-block:: python

       def logical_disjunction(p, q):
           if not(p and q):
               return False
           return True

  the terminal shows a failing test. OOPS! We've introduced a regression. If we expand our statement using "multiplication" rules. What we have above is

  .. code-block:: python

       def logical_disjunction(p, q):
           if not p not and not q:
               return False
           return True

  We get a ``SyntaxError``, the result of the "multiplication" is different from what we started with so we need something different. It should be something that expands out to

  .. code-block:: python

       def logical_disjunction(p, q):
           if not p not not and not q:
               return False
           return True

  this would "factor" out to be

  .. code-block:: python

       def logical_disjunction(p, q):
           if not(p not and q):
               return False
           return True

  okay, this looks more like, if we "multiply" this out we get our original statement since the opposite of the opposite of something is something. What if we fix the syntax. The opposite of and is ``or``

  .. code-block:: python

       def logical_disjunction(p, q):
           if not(p or q):
               return False
           return True

  Hooray! tests are passing again

* add an else statement

  .. code-block:: python

       def logical_disjunction(p, q):
           if not(p or q):
               return False
           else:
               return True

* the ``else`` statement that returns ``True`` can be restated as the opposite of the ``if`` statement

  .. code-block:: python

       def logical_disjunction(p, q):
           if not(p or q):
               return False
           if not(not(p or q)):
               return True

  since the negation of a negation gives the original thing we can say

  .. code-block:: python

       def logical_disjunction(p, q):
           if not(p or q):
               return False
           if p or q:
               return True

* reorder the statements

  .. code-block:: python

       def logical_disjunction(p, q):
           if p or q:
               return True
           if not(p or q):
               return False

* restate using ``else``

  .. code-block:: python

       def logical_disjunction(p, q):
           if p or q:
               return True
           else:
               return False

* rewriting to one line with a ``return`` statement

  .. code-block:: python

       def logical_disjunction(p, q):
           return True if p or q else return False

* using python's implicit conditional evaluation we simplify to

  .. code-block:: python

       def logical_disjunction(p, q):
           return p or q

  *VOILA!* the tests still pass and we have a simple statement that makes all 4 states pass for ``logical_disjunction``

Our knowledge is updated to show that for any boolean operation involving 2 inputs - ``p`` and ``q`` which can take the values ``True`` or ``False``


* ``and`` is "not ``or``"
* ``or`` is "not ``and``"
* ``logical_disjunction`` is ``or``
* ``logical_conjunction`` is ``and``
* ``False`` is ``not True``
* ``True`` is ``not False``
* ``False`` is ``False``
* ``True`` is ``True``
* ``return True if x else y`` can be rewritten as ``return x`` if ``x`` evaluates to ``True``
* when there are multiple outcomes we only need to write the condition for the special case and use ``else`` for the others
