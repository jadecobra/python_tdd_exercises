Truth Table: Exclusive Disjunction
==================================

We will continue to step through learning conditional statements in python using Test Driven Development using the `Truth Table <https://en.wikipedia.org/wiki/Truth_table>`_

Prerequisites
-------------


* `How I setup a Test Driven Development Environment <./How I How I setup a Test Driven Development Environment.rst>`_

----

Exclusive Disjunction
---------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

add a test for exclusive disjunction to ``TestBinaryOperations``

.. code-block:: python

       def test_exclusive_disjunction(self):
           self.assertFalse(truth_table.exclusive_disjunction(True, True))
           self.assertTrue(truth_table.exclusive_disjunction(True, False))
           self.assertTrue(truth_table.exclusive_disjunction(False, True))
           self.assertFalse(truth_table.exclusive_disjunction(False, False))

the terminal shows an `AttributeError <./ATTRIBUTE_ERROR.rst>`_

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* add a definition that returns ``True``
  .. code-block:: python

       def exclusive_disjunction(p, q):
           return True
    we get an `AssertionError <./ASSERTION_ERROR.rst>`_ for the second case
* add a condition for it
  .. code-block:: python

       def exclusive_disjunction(p , q):
           if p == True and q == True:
               return False
           return True
    the terminal shows an `AssertionError <./ASSERTION_ERROR.rst>`_ for the fourth case
* add a condition
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

let us try to refactor those statements to make them better


* in the first case ``p`` and ``q`` have the same value, can we change the statement to reflect this like we did with ``logical_equality``?
  .. code-block:: python

       def exclusive_disjunction(p, q):
           if p == q:
               return False
           if p == True and q == True:
               return False
           return True
    tests still pass
* the next statement looks similar, we can rewrite it as
  .. code-block:: python

       def exclusive_disjunction(p, q):
           if p == q:
               return False
           if p == q:
               return False
           return True
    since it's exactly the same statement, we remove the repetition
  .. code-block:: python

       def exclusive_disjunction(p, q):
           if p == q:
               return False
           return True

* add ``else``
  .. code-block:: python

       def exclusive_disjunction(p, q):
           if p == q:
               return False
           else:
               return True

* add the opposite ``if`` statement
  .. code-block:: python

       def exclusive_disjunction(p, q):
           if p == q:
               return False
           if p != q:
               return True

* reorder
  .. code-block:: python

       def exclusive_disjunction(p, q):
           if p != q:
               return True
           if p == q:
               return False

* replace with ``else``
  .. code-block:: python

       def exclusive_disjunction(p, q):
           if p != q:
               return True
           else:
               return False

* use one line return statement
  .. code-block:: python

       def exclusive_disjunction(p, q):
           return True if p != q else False

* remove excess
  .. code-block:: python

       def exclusive_disjunction(p, q):
           return p != q

What do we know so far? For any boolean operation involving 2 inputs - ``p`` and ``q`` which can take the values ``True`` or ``False``


* ``exclusive_disjunction`` is ``!=``
* ``logical_equality`` is ``==``
* ``logical_disjunction`` is ``or``
* ``logical_conjunction`` is ``and``
* ``and`` is "not ``or``"
* ``or`` is "not ``and``"
* ``False`` is ``not True``
* ``True`` is ``not False``
* ``False`` is ``False``
* ``True`` is ``True``
* ``return True if x else y`` can be rewritten as ``return x`` if ``x`` evaluates to ``True``
